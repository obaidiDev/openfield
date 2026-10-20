"""openfield gateway: speaks the Higgsfield FNF plugin API (v2alpha) + the
RFC 8628 device-auth the Blender add-on expects, so the add-on runs entirely
against this local server.

Endpoints implemented (from the bundled fnf_sdk-0.25.0 client's own contract):

  OAuth device flow      /.well-known/oauth-authorization-server
                         /oauth/device/code   /oauth/token
  Catalog                GET  /developer/v2alpha/job_types[?type&label&limit&cursor]
                         GET  /developer/v2alpha/job_types/{job_type}
  Generations            POST /developer/v2alpha/{images|videos|3d}/{job_type}/generations
                         POST /developer/v2alpha/jobs/{job_type}/cost
  Jobs                   GET  /developer/v2alpha/jobs/{job_id}
                         GET  /developer/v2alpha/jobs[?type&status&size&cursor]
  Account                GET  /developer/v2alpha/account/balance
                         GET  /developer/v2alpha/account/workspaces
  Media upload slots     POST /developer/v2alpha/media            (create slot)
                         PUT  /uploads/{media_id}                 (slot upload_url)
                         POST /developer/v2alpha/media/{id}/confirm?type=...
                         POST /developer/v2alpha/media/import     {url,type}
  Files                  GET  /media/{id}/file  GET /results/{filename}
                         GET  /healthz
"""
from __future__ import annotations

import base64
import hashlib
import json
import mimetypes
import re
import secrets
import socketserver
import threading
import time
import urllib.request
import uuid
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

from . import __version__
from .backends import make_backend
from .catalog import model_card
from .config import Config
from .store import Store, new_id

JOB_STATUSES_NONTERMINAL = {"queued", "in_progress"}


def iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def b64u(raw: bytes) -> str:
    return base64.urlsafe_b64encode(raw).decode().rstrip("=")


def make_id_token(email: str, ttl: float) -> str:
    """Unsigned dev JWT (the gateway is the trust root here; the add-on only
    reads exp/name locally — signature verification happens server-side at
    whoever minted the token, and that's us)."""
    now = int(time.time())
    header = b64u(json.dumps({"alg": "none", "typ": "JWT"}).encode())
    payload = b64u(
        json.dumps(
            {
                "iss": "openfield",
                "sub": "local-user",
                "email": email,
                "email_verified": True,
                "name": "Local User",
                "iat": now,
                "exp": now + int(ttl),
            }
        ).encode()
    )
    return f"{header}.{payload}."


class Handler(BaseHTTPRequestHandler):
    server_version = f"openfield/{__version__}"
    protocol_version = "HTTP/1.1"

    # ---- plumbing ---------------------------------------------------------
    def log_message(self, fmt, *args):  # quieter
        if getattr(self.server, "verbose", False):
            super().log_message(fmt, *args)

    def _send(self, status, payload=None, content_type="application/json", body=None, extra=None):
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
        body = body or b""
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        if body and self.command != "HEAD":
            self.wfile.write(body)

    def _send_error(self, status, error_type, message):
        self._send(status, {"error_type": error_type, "message": message})

    def _read_body(self, limit=1024 * 1024 * 1024):
        # always drain Content-Length exactly, even in handlers that ignore the
        # body: an unread body desynchronizes the keep-alive connection and the
        # leftover bytes get parsed as a garbage next request (501).
        if getattr(self, "_body_cached", None) is not None:
            return self._body_cached
        length = int(self.headers.get("Content-Length") or 0)
        if length > limit:
            raise ValueError("body too large")
        data = self.rfile.read(length) if length else b""
        self._body_cached = data
        return data

    def _query(self):
        return {k: v[0] for k, v in parse_qs(urlparse(self.path).query).items()}

    def _form(self, raw):
        return {k: v[0] for k, v in parse_qs(raw.decode("utf-8")).items()}

    def _bearer(self):
        auth = self.headers.get("Authorization", "")
        if auth.lower().startswith("bearer "):
            return auth[7:].strip()
        return ""

    def _require_auth(self):
        token = self._bearer()
        if not token:
            self._send_error(401, "validation_error", "missing bearer token")
            return False
        row = self.server.store.get_token(token)
        if not row:
            self._send_error(401, "validation_error", "invalid or expired token")
            return False
        if row["expires_at"] < time.time():
            self.server.store.drop_token(token)
            self._send_error(401, "validation_error", "expired token")
            return False
        return True

    # ---- routing ----------------------------------------------------------
    def do_GET(self):
        self._route("GET")

    def do_POST(self):
        self._route("POST")

    def do_PUT(self):
        self._route("PUT")

    def _route(self, method):
        cfg = self.server.cfg
        parsed = urlparse(self.path)
        path = parsed.path
        self._body_cached = None
        if method in ("POST", "PUT", "PATCH"):
            self._read_body()
        try:
            if path == "/healthz":
                return self._send(200, {"ok": True, "name": "openfield", "version": __version__})
            if path == "/.well-known/oauth-authorization-server":
                return self._auth_metadata(cfg)
            if path == "/.well-known/oauth-protected-resource":
                return self._send(
                    200,
                    {
                        "resource": cfg.base_url,
                        "authorization_servers": [cfg.base_url],
                        "scopes_supported": ["openid", "email", "offline_access"],
                        "bearer_methods_supported": ["header"],
                    },
                )
            if path == "/oauth/device/code" and method == "POST":
                return self._device_code()
            if path == "/oauth/token" and method == "POST":
                return self._token()
            if path == "/device" and method == "GET":
                # sign-in from Blender auto-approves; this page just explains it
                self.server.store.approve_pending_devices()
                html = (
                    "<html><body style='font-family:sans-serif;padding:3rem'>"
                    "<h2>openfield sign-in</h2><p>Nothing to do here — "
                    "Blender's login completes automatically on this machine.</p>"
                    "</body></html>"
                ).encode()
                return self._send(200, body=html, content_type="text/html; charset=utf-8")

            m = re.match(r"^/(media|results)/(.+)$", path)
            if m and method == "GET":
                return self._file(m.group(1), m.group(2))

            m = re.match(r"^/uploads/([0-9a-f-]{36})$", path)
            if m and method == "PUT":
                return self._uploads_put(m.group(1))

            if not path.startswith("/developer/"):
                return self._send_error(404, "validation_error", f"unknown path {path}")
            if not self._require_auth():
                return

            if path == "/developer/v2alpha/job_types" and method == "GET":
                return self._job_types()
            m = re.match(r"^/developer/v2alpha/job_types/([\w.-]+)$", path)
            if m and method == "GET":
                return self._job_type_one(m.group(1))
            m = re.match(r"^/developer/v2alpha/(images|videos|3d)/([\w.-]+)/generations$", path)
            if m and method == "POST":
                return self._create_generation(m.group(1), m.group(2))
            m = re.match(r"^/developer/v2alpha/jobs/([\w.-]+)/cost$", path)
            if m and method == "POST":
                return self._cost(m.group(1))
            m = re.match(r"^/developer/v2alpha/jobs/([0-9a-f-]{36})$", path)
            if m and method == "GET":
                return self._job_get(m.group(1))
            if path == "/developer/v2alpha/jobs" and method == "GET":
                return self._jobs_list()
            if path == "/developer/v2alpha/account/balance" and method == "GET":
                return self._balance()
            if path == "/developer/v2alpha/account/workspaces" and method == "GET":
                return self._workspaces()
            if path == "/developer/v2alpha/media" and method == "POST":
                return self._media_slot()
            m = re.match(r"^/developer/v2alpha/media/([0-9a-f-]{36})/confirm$", path)
            if m and method == "POST":
                return self._media_confirm(m.group(1))
            if path == "/developer/v2alpha/media/import" and method == "POST":
                return self._media_import()
            if path == "/developer/v2alpha/jobs" and method == "POST":
                return self._send_error(400, "validation_error", "jobs POST needs /{images|videos|3d}/...")
            return self._send_error(404, "validation_error", f"unknown endpoint {method} {path}")
        except Exception as exc:  # never leak a stack to the add-on's UI
            self._send_error(500, "internal_error", f"openfield: {exc}")

    # ---- OAuth ------------------------------------------------------------
    def _auth_metadata(self, cfg):
        self._send(
            200,
            {
                "issuer": cfg.base_url,
                "authorization_endpoint": f"{cfg.base_url}/device",
                "device_authorization_endpoint": f"{cfg.base_url}/oauth/device/code",
                "token_endpoint": f"{cfg.base_url}/oauth/token",
                "response_types_supported": ["code"],
                "grant_types_supported": [
                    "urn:ietf:params:oauth:grant-type:device_code",
                    "refresh_token",
                ],
                "token_endpoint_auth_methods_supported": ["client_secret_post", "none"],
                "scopes_supported": ["openid", "email", "offline_access", "profile"],
            },
        )

    def _device_code(self):
        cfg, store = self.server.cfg, self.server.store
        form = self._form(self._read_body(4096))
        client_id = form.get("client_id", "blender")
        ttl = float(cfg.data["auth"].get("refresh_ttl_seconds", 30 * 24 * 3600))
        device_code, user_code = store.create_device(
            client_id, interval=1.0, ttl=min(600.0, ttl)
        )
        if cfg.data["auth"].get("auto_approve", True):
            peer = self.client_address[0]
            loopback_only = cfg.data["auth"].get("auto_approve_loopback_only", True)
            if not loopback_only or peer in ("127.0.0.1", "::1"):
                store.approve_pending_devices()
        self._send(
            200,
            {
                "device_code": device_code,
                "user_code": user_code,
                "verification_uri": f"{cfg.base_url}/device",
                "verification_uri_complete": f"{cfg.base_url}/device?user_code={user_code}",
                "expires_in": int(min(600.0, ttl)),
                "interval": 1,
            },
        )

    def _token(self):
        cfg, store = self.server.cfg, self.server.store
        form = self._form(self._read_body(4096))
        grant = form.get("grant_type", "")
        access_ttl = float(cfg.data["auth"].get("access_ttl_seconds", 3600))
        refresh_ttl = float(cfg.data["auth"].get("refresh_ttl_seconds", 30 * 24 * 3600))
        email = cfg.data["account"].get("email", "local@localhost")

        if grant == "urn:ietf:params:oauth:grant-type:device_code":
            dev = store.get_device(form.get("device_code", ""))
            if not dev:
                return self._send(400, {"error": "invalid_grant", "error_description": "unknown device code"})
            if time.time() > dev["expires_at"]:
                return self._send(400, {"error": "expired_token", "error_description": "device code expired"})
            if dev["state"] == "pending":
                # auto-approve on poll in case the browser flow is being followed
                if cfg.data["auth"].get("auto_approve") and not cfg.data["auth"].get("auto_approve_loopback_only"):
                    store.approve_pending_devices()
                    dev = store.get_device(dev["device_code"])
                else:
                    return self._send(
                        400,
                        {"error": "authorization_pending", "error_description": "approve the code at /device"},
                    )
            access = secrets.token_urlsafe(32)
            refresh = secrets.token_urlsafe(32)
            id_token = make_id_token(email, max(access_ttl, refresh_ttl))
            store.issue_tokens(dev["device_code"], access, refresh, id_token, time.time() + access_ttl)
            return self._send(
                200,
                {
                    "access_token": access,
                    "refresh_token": refresh,
                    "id_token": id_token,
                    "token_type": "Bearer",
                    "expires_in": int(access_ttl),
                    "scope": "openid email offline_access profile",
                },
            )
        if grant == "refresh_token":
            row = store.rotate_refresh(form.get("refresh_token", ""))
            if not row:
                return self._send(400, {"error": "invalid_grant", "error_description": "unknown refresh token"})
            store.drop_token(row["access_token"])
            access = secrets.token_urlsafe(32)
            refresh = secrets.token_urlsafe(32)
            id_token = make_id_token(email, max(access_ttl, refresh_ttl))
            store._execute(
                "INSERT INTO tokens(access_token,refresh_token,sub,email,id_token,expires_at) VALUES(?,?,?,?,?,?)",
                (access, refresh, "local-user", email, id_token, time.time() + access_ttl),
            )
            return self._send(
                200,
                {
                    "access_token": access,
                    "refresh_token": refresh,
                    "id_token": id_token,
                    "token_type": "Bearer",
                    "expires_in": int(access_ttl),
                    "scope": "openid email offline_access profile",
                },
            )
        self._send(400, {"error": "unsupported_grant_type", "error_description": grant})

    # ---- catalog ----------------------------------------------------------
    def _job_types(self):
        q = self._query()
        want_type = q.get("type")
        items = [model_card(e) for e in self.server.cfg.catalog.values() if not want_type or e.get("type") == want_type]
        self._send(200, {"items": items, "next_cursor": None})

    def _job_type_one(self, job_type):
        entry = self.server.cfg.catalog.get(job_type)
        if not entry:
            return self._send_error(404, "unknown_job_type", f"no catalog entry {job_type}")
        self._send(200, model_card(entry))

    # ---- generations ------------------------------------------------------
    def _cost(self, job_type):
        entry = self.server.cfg.catalog.get(job_type)
        if not entry:
            return self._send_error(404, "unknown_job_type", f"no catalog entry {job_type}")
        self._send(200, {"credits": float(entry.get("cost", 0))})

    def _create_generation(self, kind, job_type):
        cfg, store = self.server.cfg, self.server.store
        entry = cfg.catalog.get(job_type)
        if not entry:
            return self._send_error(404, "unknown_job_type", f"no catalog entry {job_type}")
        body = json.loads(self._read_body() or b"{}")
        params = dict(body.get("params") or {})
        if not str(params.get("prompt") or "").strip() and not any(
            isinstance(v, dict) and "id" in v for v in params.values()
        ):
            return self._send_error(422, "validation_error", "params.prompt is required")
        job_id = store.create_job(job_type, params)
        self.server.executor.submit(job_id, entry, params)
        self._send(
            200,
            {"id": job_id, "job_type": job_type, "credits": float(entry.get("cost", 0))},
        )

    def _job_get(self, job_id):
        job = self.server.store.get_job(job_id)
        if not job:
            return self._send_error(404, "validation_error", "no such job")
        self._send(200, self._job_model(job))

    def _job_model(self, job):
        entry = self.server.cfg.catalog.get(job["job_type"], {})
        return {
            "id": job["id"],
            "status": job["status"],
            "job_type": job["job_type"],
            "display_name": str(entry.get("display_name") or job["job_type"]),
            "result_url": job["result_url"],
            "min_result_url": job["min_result_url"],
            "created_at": iso(job["created_at"]),
            "params": job["params"],
            **({"thumbnail_url": job["thumbnail_url"]} if job.get("thumbnail_url") else {}),
        }

    def _jobs_list(self):
        q = self._query()
        size = min(int(q.get("size", 50)), 100)
        ids = self.server.store.list_jobs(limit=size)
        items = [self._job_model(self.server.store.get_job(j)) for j in ids if self.server.store.get_job(j)]
        self._send(200, {"items": items, "cursor": None})

    # ---- account ----------------------------------------------------------
    def _balance(self):
        acc = self.server.cfg.data["account"]
        credits = acc["workspaces"][0].get("credits", 999999.0) if acc.get("workspaces") else 999999.0
        self._send(
            200,
            {
                "email": acc.get("email", "local@localhost"),
                "credits": float(credits),
                "subscription_plan_type": str(acc.get("plan_type", "max")),
            },
        )

    def _workspaces(self):
        acc = self.server.cfg.data["account"]
        items = []
        for ws in acc.get("workspaces") or [{"name": "Local", "credits": 999999.0}]:
            items.append(
                {
                    "id": str(uuid.uuid5(uuid.NAMESPACE_DNS, "openfield:" + str(ws.get("name", "Local")))),
                    "name": ws.get("name"),
                    "type": "private",
                    "user_role": "owner",
                    "is_selected": not items,
                    "plan_type": str(acc.get("plan_type", "max")),
                    "credits": float(ws.get("credits", 999999.0)),
                }
            )
        self._send(200, {"items": items})

    # ---- media ------------------------------------------------------------
    def _media_slot(self):
        q = self._query()
        body = json.loads(self._read_body(4096) or b"{}")
        # the SDK sends type/extension as query params on this POST
        mtype = str(q.get("type") or body.get("type") or "image")
        if mtype not in {"image", "video", "audio", "file"}:
            mtype = "image"
        ext = re.sub(
            r"[^a-z0-9]", "", str(q.get("extension") or body.get("extension") or "").lower()
        ) or (mimetypes.guess_extension(mtype) or "bin")
        media_id = self.server.store.create_media(mtype, f"{mtype}.{ext}", None, "pending")
        self._send(
            200,
            {
                "id": media_id,
                "type": mtype,
                "url": f"{self.server.cfg.base_url}/media/{media_id}/file",
                "upload_url": f"{self.server.cfg.base_url}/uploads/{media_id}",
                "content_type": mimetypes.guess_type(f"x.{ext}")[0] or "application/octet-stream",
            },
        )

    def _uploads_put(self, media_id):
        media = self.server.store.get_media(media_id)
        if not media:
            return self._send_error(404, "validation_error", "no such media slot")
        data = self._read_body()
        target = self.server.cfg.data_dir / "uploads" / f"{media_id}{Path(media['filename']).suffix}"
        target.write_bytes(data)
        self.server.store.set_media_status(media_id, "uploaded")
        self._send(200, {"ok": True})

    def _media_confirm(self, media_id):
        q = self._query()
        media = self.server.store.get_media(media_id)
        if not media:
            return self._send_error(404, "validation_error", "no such media")
        self.server.store.set_media_status(media_id, "uploaded")
        self._send(200, {"id": media_id, "status": "uploaded"})

    def _media_import(self):
        body = json.loads(self._read_body(4096) or b"{}")
        url = str(body.get("url") or "")
        if not url.startswith(("http://", "https://")):
            return self._send_error(422, "validation_error", "media import needs an http(s) url")
        try:
            data = urllib.request.urlopen(url, timeout=120).read()
        except Exception as exc:
            return self._send_error(422, "invalid_media", f"could not fetch url: {exc}")
        mtype = str(body.get("type") or "image")
        if mtype not in {"image", "video", "audio", "file"}:
            mtype = "image"
        suffix = Path(urlparse(url).path).suffix or ".png"
        media_id = self.server.store.create_media(mtype, f"imported{suffix}", None, "uploaded")
        (self.server.cfg.data_dir / "uploads" / f"{media_id}{suffix}").write_bytes(data)
        self._send(
            200,
            {
                "id": media_id,
                "type": mtype,
                "url": f"{self.server.cfg.base_url}/media/{media_id}/file",
                "status": "uploaded",
            },
        )

    def _file(self, kind, name):
        if not re.fullmatch(r"[0-9a-f-]{36}", name) and not re.fullmatch(r"[\w.-]+", name):
            return self._send_error(404, "validation_error", "bad file name")
        if kind == "media":
            media = self.server.store.get_media(name)
            if not media:
                return self._send_error(404, "validation_error", "no such media")
            stem = self.server.cfg.data_dir / "uploads" / f"{name}"
            files = sorted(stem.parent.glob(stem.name + ".*"))
            if not files:
                return self._send_error(404, "validation_error", "no stored bytes")
            path = files[0]
        else:
            path = self.server.cfg.data_dir / "results" / name
            if not path.exists() or path.is_symlink():
                return self._send_error(404, "validation_error", "no such result")
        ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        self._send(200, body=path.read_bytes(), content_type=ctype)


class Executor:
    """Runs generations on worker threads and updates job state."""

    def __init__(self, cfg: Config, store: Store):
        self.cfg, self.store = cfg, store

    def submit(self, job_id, entry, params):
        threading.Thread(target=self._run, args=(job_id, entry, params), daemon=True).start()

    def _collect_media(self, params):
        out = {}
        def walk(value):
            if isinstance(value, dict):
                if "id" in value and "type" in value and isinstance(value.get("id"), str):
                    media = self.store.get_media(value["id"])
                    if media:
                        stem = self.cfg.data_dir / "uploads" / str(value["id"])
                        files = sorted(stem.parent.glob(stem.name + ".*"))
                        if files:
                            out[value["id"]] = {
                                "path": str(files[0]),
                                "url": f"{self.cfg.base_url}/media/{value['id']}/file",
                                "type": media["type"],
                            }
                for v in value.values():
                    walk(v)
            elif isinstance(value, list):
                for v in value:
                    walk(v)
        walk(params)
        return out

    def _run(self, job_id, entry, params):
        self.store.update_job(job_id, status="in_progress")
        try:
            backend = make_backend(self.cfg, entry)
            media = self._collect_media(params)
            result = backend.run(entry, params, media, self)
            data = result.get("bytes") or b""
            suffix = result.get("suffix") or ".png"
            name = f"{job_id}{suffix}"
            (self.cfg.data_dir / "results" / name).write_bytes(data)
            url = f"{self.cfg.base_url}/results/{name}"
            self.store.update_job(
                job_id,
                status="completed",
                credits=float(entry.get("cost", 0)),
                result_url=url,
                min_result_url=url,
            )
        except Exception as exc:
            self.store.update_job(job_id, status="failed", error=str(exc)[:1000])

    def log(self, message):
        print(f"[job] {message}", flush=True)


class Gateway(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, cfg: Config, verbose=False):
        self.cfg = cfg
        self.store = Store(cfg.data_dir)
        self.executor = Executor(cfg, self.store)
        self.verbose = verbose
        super().__init__((cfg.data["server"]["host"], cfg.data["server"]["port"]), Handler)

    def serve_forever_quiet(self):
        print(f"openfield gateway on {self.cfg.base_url}", flush=True)
        print(f"  catalog: {', '.join(self.cfg.catalog) or '(empty)'}", flush=True)
        print(f"  add to Blender: HIGGSFIELD_SDK_BASE_URL={self.cfg.base_url}", flush=True)
        print(f"  add to Blender: HIGGSFIELD_DEVICE_AUTH_ORIGIN={self.cfg.base_url}", flush=True)
        super().serve_forever()


def main():
    import argparse

    ap = argparse.ArgumentParser(prog="openfield.gateway")
    ap.add_argument("--config", default=str(Path(__file__).resolve().parents[1] / "config.toml"))
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    cfg = Config(Path(args.config))
    Gateway(cfg, verbose=args.verbose).serve_forever_quiet()


if __name__ == "__main__":
    main()
