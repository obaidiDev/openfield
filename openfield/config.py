"""Config loading (TOML, stdlib tomllib) for openfield."""
from __future__ import annotations

import os
import tomllib
from pathlib import Path

DEFAULTS = {
    "server": {"host": "127.0.0.1", "port": 8745},
    "auth": {
        "auto_approve": True,
        "auto_approve_loopback_only": True,
        "access_ttl_seconds": 3600,
        "refresh_ttl_seconds": 30 * 24 * 3600,
    },
    "account": {
        "email": "local@localhost",
        "plan_type": "max",
        "workspaces": [{"name": "Local", "credits": 999999.0}],
    },
    "paths": {"data_dir": "./data"},
    "comfy": {"poll_interval": 2.0, "job_timeout": 600},
    "bridge": {"disable_local_ws": True},
}


def _merge(base: dict, override: dict) -> dict:
    out = dict(base)
    for key, value in (override or {}).items():
        if isinstance(value, dict) and isinstance(out.get(key), dict):
            out[key] = _merge(out[key], value)
        else:
            out[key] = value
    return out


class Config:
    def __init__(self, path: Path):
        self.path = Path(path).resolve()
        self.root = self.path.parent
        raw = {}
        if self.path.exists():
            with open(self.path, "rb") as fh:
                raw = tomllib.load(fh)
        self.data = _merge(DEFAULTS, raw)
        self.base_url = "http://{}:{}".format(
            self.data["server"]["host"], self.data["server"]["port"]
        )
        data_dir = Path(self.data["paths"]["data_dir"])
        if not data_dir.is_absolute():
            data_dir = self.root / data_dir
        self.data_dir = data_dir
        (self.data_dir / "uploads").mkdir(parents=True, exist_ok=True)
        (self.data_dir / "results").mkdir(parents=True, exist_ok=True)
        self.catalog = {str(entry["job_type"]): entry for entry in self.data.get("catalog", [])}
        self.backends = self.data.get("backends", {})
        self._validate()

    def _validate(self) -> None:
        seen_types = set()
        for job_type, entry in self.catalog.items():
            jtype = str(entry.get("type"))
            if jtype not in {"image", "video", "3d"}:
                raise SystemExit(
                    f"catalog entry {job_type}: type must be image|video|3d (got {jtype!r})"
                )
            if jtype in seen_types:
                pass  # multiple models of the same kind are fine
            backend = str(entry.get("backend_type", "comfyui"))
            if backend not in {"comfyui", "openai_images", "local"}:
                raise SystemExit(
                    f"catalog entry {job_type}: backend_type must be comfyui|openai_images|local"
                )
            ref = entry.get("backend_ref")
            if backend != "local" and (not ref or ref not in self.backends):
                raise SystemExit(
                    f"catalog entry {job_type}: backend_ref {ref!r} not found in [backends]"
                )
        for name, backend in self.backends.items():
            btype = str(backend.get("type"))
            if btype == "comfyui" and not backend.get("url"):
                raise SystemExit(f"backends.{name}: comfyui needs url")
            if btype == "openai_images" and not backend.get("base_url"):
                raise SystemExit(f"backends.{name}: openai_images needs base_url")

    def workflow_path(self, entry: dict):
        name = entry.get("comfy_workflow")
        if not name:
            return None
        wf = Path(str(name))
        if not wf.is_absolute():
            wf = self.root / wf
        return wf

    def backend(self, entry: dict) -> dict:
        ref = entry.get("backend_ref")
        if ref and ref in self.backends:
            return _merge(self.backends[ref], {"type": str(entry.get("backend_type"))})
        return {"type": str(entry.get("backend_type", "local"))}

    def resolve_env_key(self, backend: dict, field: str = "api_key") -> str:
        value = str(backend.get(field, "") or "")
        if value.startswith("env:"):
            value = os.environ.get(value[4:], "")
        return value
