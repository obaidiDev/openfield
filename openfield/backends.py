"""Generation backends: ComfyUI, OpenAI-compatible image APIs, local commands.

Every backend exposes run(entry, params, media, ctx) -> {"suffix": ".png",
"bytes": b"..." } where `media` maps media-id -> {"path", "url", "type"}.
ctx gives .log(str) for progress text.
"""
from __future__ import annotations

import base64
import json
import mimetypes
import os
import random
import subprocess
import tempfile
import time
import urllib.parse
import urllib.request
from pathlib import Path


def _http(url, *, method="GET", data=None, headers=None, timeout=120):
    req = urllib.request.Request(url, data=data, method=method)
    for key, value in (headers or {}).items():
        req.add_header(key, value)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.status, resp.read()


def _http_json(url, **kw):
    status, body = _http(url, headers={"Accept": "application/json"}, **kw)
    return json.loads(body.decode("utf-8")) if body else {}


# ---------------------------------------------------------------------------
# ComfyUI (API-format workflow file with {{token}} substitution)
# ---------------------------------------------------------------------------

def _substitute(node, tokens):
    """Deep-substitute {{token}} placeholders inside a JSON workflow.

    A whole-string placeholder is replaced by the token's raw value (which may
    be a number); embedded placeholders substitute textually.
    """
    if isinstance(node, dict):
        return {k: _substitute(v, tokens) for k, v in node.items()}
    if isinstance(node, list):
        return [_substitute(v, tokens) for v in node]
    if isinstance(node, str) and "{{" in node:
        stripped = node.strip()
        if stripped.startswith("{{") and stripped.endswith("}}") and node.count("{{") == 1:
            return tokens.get(stripped[2:-2].strip())
        out = node
        for key, value in tokens.items():
            out = out.replace("{{" + key + "}}", str(value))
        return out
    return node


class ComfyBackend:
    def __init__(self, cfg, backend, entry):
        self.url = str(backend.get("url", "http://127.0.0.1:8188")).rstrip("/")
        self.client_id = str(backend.get("client_id", "openfield"))
        # optional: copy uploaded references into ComfyUI's input dir so stock
        # LoadImage nodes work; media tokens then become filenames, not URLs.
        input_dir = backend.get("input_dir")
        self.input_dir = Path(input_dir) if input_dir else None
        wf_path = cfg.workflow_path(entry)
        if not wf_path or not Path(wf_path).exists():
            raise RuntimeError(
                f"ComfyUI workflow file not found for {entry['job_type']}: {wf_path}"
            )
        self.workflow = json.loads(Path(wf_path).read_text(encoding="utf-8"))
        self.poll_interval = float(cfg.data["comfy"].get("poll_interval", 2.0))
        self.job_timeout = float(cfg.data["comfy"].get("job_timeout", 600))

    def _tokens(self, params, media):
        tokens = {
            "prompt": str(params.get("prompt") or ""),
            "negative_prompt": str(params.get("negative_prompt") or ""),
            "seed": int(params.get("seed") or random.randrange(1, 2**31 - 1)),
            "width": int(params.get("width") or 1024),
            "height": int(params.get("height") or 1024),
            "duration": params.get("duration", 5),
            "fps": params.get("fps", 16),
            "steps": int(params.get("steps") or 20),
        }
        # With input_dir configured, copy references into ComfyUI's input folder
        # so plain LoadImage nodes work; tokens become file names.
        names = []
        for mid, m in media.items():
            src = Path(m["path"])
            if self.input_dir:
                self.input_dir.mkdir(parents=True, exist_ok=True)
                dst = self.input_dir / f"openfield_{mid[:8]}{src.suffix}"
                dst.write_bytes(src.read_bytes())
                names.append(dst.name)
            else:
                names.append(m["url"])  # workflows using LoadImageFromUrl-style nodes
        for i, value in enumerate(names):
            tokens[f"media:{i}"] = value
        if names:
            tokens.setdefault("media", names[0])
        return tokens

    def run(self, entry, params, media, ctx):
        tokens = self._tokens(params, media)
        workflow = _substitute(self.workflow, tokens)
        prompt_id = _http_json(
            f"{self.url}/prompt",
            method="POST",
            data=json.dumps({"prompt": workflow, "client_id": self.client_id}).encode(),
            headers={"Content-Type": "application/json"},
        )
        pid = prompt_id.get("prompt_id")
        if not pid:
            raise RuntimeError(f"ComfyUI rejected the workflow: {prompt_id}")
        ctx.log(f"comfy prompt {pid}")
        deadline = time.time() + self.job_timeout
        while time.time() < deadline:
            time.sleep(self.poll_interval)
            hist = _http_json(f"{self.url}/history/{pid}")
            record = hist.get(pid)
            if not record:
                continue
            status = (record.get("status") or {})
            if status.get("status_str") == "error" or status.get("completed") is False:
                raise RuntimeError(f"ComfyUI job failed: {json.dumps(status)[:400]}")
            outputs = record.get("outputs") or {}
            for node_out in outputs.values():
                for img in node_out.get("images", []) or []:
                    status2, data = _http(
                        f"{self.url}/view",
                        data=urllib.parse.urlencode(
                            {"filename": img["filename"], "subfolder": img.get("subfolder", ""), "type": img.get("type", "output")}
                        ).encode(),
                        method="POST",
                    )
                    suffix = Path(img["filename"]).suffix or ".png"
                    ctx.log(f"comfy done {img['filename']}")
                    return {"suffix": suffix, "bytes": data}
                for vid in node_out.get("videos", []) or []:
                    status2, data = _http(
                        f"{self.url}/view",
                        data=urllib.parse.urlencode(
                            {"filename": vid["filename"], "subfolder": vid.get("subfolder", ""), "type": vid.get("type", "output")}
                        ).encode(),
                        method="POST",
                    )
                    suffix = Path(vid["filename"]).suffix or ".mp4"
                    ctx.log(f"comfy done {vid['filename']}")
                    return {"suffix": suffix, "bytes": data}
                glb = node_out.get("gltf") or node_out.get("glb")
                if isinstance(glb, dict) and glb.get("filename"):
                    status2, data = _http(
                        f"{self.url}/view",
                        data=urllib.parse.urlencode(
                            {"filename": glb["filename"], "subfolder": glb.get("subfolder", ""), "type": glb.get("type", "output")}
                        ).encode(),
                        method="POST",
                    )
                    return {"suffix": Path(glb["filename"]).suffix or ".glb", "bytes": data}
            if status.get("completed"):
                raise RuntimeError("ComfyUI finished but produced no image/video/glb output")
        raise RuntimeError(f"ComfyUI job timed out after {self.job_timeout}s")


# ---------------------------------------------------------------------------
# OpenAI-compatible images (images.gens: OpenAI, fal, replicate-proxy, local vLLM)
# ---------------------------------------------------------------------------

class OpenAIImagesBackend:
    def __init__(self, cfg, backend, entry):
        self.base_url = str(backend.get("base_url", "")).rstrip("/")
        self.api_key = cfg.resolve_env_key(backend)
        self.model = str(entry.get("openai_model") or "gpt-image-1")
        self.size_map = backend.get("size_map") or {}

    def run(self, entry, params, media, ctx):
        width = int(params.get("width") or 1024)
        height = int(params.get("height") or 1024)
        size = self.size_map.get(f"{width}x{height}", f"{width}x{height}")
        body = {
            "model": self.model,
            "prompt": str(params.get("prompt") or ""),
            "size": size,
            "n": 1,
        }
        if params.get("negative_prompt"):
            body["negative_prompt"] = params["negative_prompt"]
        if str(entry.get("openai_mode", "")) == "edit":
            raise RuntimeError("openai_mode=edit not wired yet; use comfyui for img2img")
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        status, payload = _http(
            f"{self.base_url}/images/generations",
            method="POST",
            data=json.dumps(body).encode(),
            headers=headers,
            timeout=600,
        )
        data = json.loads(payload.decode("utf-8"))
        item = (data.get("data") or [{}])[0]
        if item.get("b64_json"):
            return {"suffix": ".png", "bytes": base64.b64decode(item["b64_json"])}
        url = item.get("url")
        if not url:
            raise RuntimeError(f"provider returned no image: {json.dumps(data)[:300]}")
        return {"suffix": ".png", "bytes": _http(url, timeout=300)[1]}


# ---------------------------------------------------------------------------
# Local command: PROMPT/WIDTH/HEIGHT/SEED/OUTPATH (+ MEDIA_URL_0..) in env.
# ---------------------------------------------------------------------------

class LocalCommandBackend:
    def __init__(self, cfg, backend, entry):
        self.command = str(backend.get("command") or entry.get("command") or "")
        if not self.command:
            raise RuntimeError("local backend needs a command")
        self.timeout = float(backend.get("timeout", 1800))
        self.env_extra = {str(k): str(v) for k, v in (backend.get("env") or {}).items()}

    def run(self, entry, params, media, ctx):
        with tempfile.TemporaryDirectory() as tmp:
            outpath = Path(tmp) / "result"
            env = dict(os.environ)
            env.update(self.env_extra)
            env.update(
                {
                    "PROMPT": str(params.get("prompt") or ""),
                    "NEGATIVE_PROMPT": str(params.get("negative_prompt") or ""),
                    "WIDTH": str(int(params.get("width") or 1024)),
                    "HEIGHT": str(int(params.get("height") or 1024)),
                    "SEED": str(int(params.get("seed") or 0)),
                    "DURATION": str(params.get("duration") or ""),
                    "FPS": str(params.get("fps") or ""),
                    "OUTPATH": str(outpath),
                }
            )
            for i, m in enumerate(media.values()):
                env[f"MEDIA_URL_{i}"] = m["url"]
            proc = subprocess.run(
                self.command,
                shell=True,
                env=env,
                capture_output=True,
                timeout=self.timeout,
            )
            produced = None
            if outpath.exists():
                produced = outpath
            else:
                kids = sorted(Path(tmp).iterdir())
                if kids:
                    produced = kids[0]
            if not produced:
                raise RuntimeError(
                    f"local command wrote nothing (exit {proc.returncode}): "
                    f"{proc.stderr.decode('utf-8','replace')[:300]}"
                )
            return {"suffix": produced.suffix or ".png", "bytes": produced.read_bytes()}


BACKENDS = {
    "comfyui": ComfyBackend,
    "openai_images": OpenAIImagesBackend,
    "local": LocalCommandBackend,
}


def make_backend(cfg, entry):
    ref = entry.get("backend_ref")
    backend = dict((cfg.backends.get(ref) or {}) if ref else {})
    btype = str(entry.get("backend_type") or backend.get("type") or "local")
    backend.setdefault("type", btype)
    factory = BACKENDS.get(btype)
    if not factory:
        raise RuntimeError(f"unknown backend_type {btype!r}")
    return factory(cfg, backend, entry)
