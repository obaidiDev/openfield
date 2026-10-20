"""Catalog schemas: what the add-on's pickers and param forms render.

The add-on validates every catalog model through fnf/schema.py
(validate_catalog_models -> describe_object_schema), so each model needs a
json_schema object with a `properties` dict. Media params are detected by
shape: an object with `id` (string) + `type` (string) and a title containing
"media" (or a uuid format) renders as the add-on's file picker and gets
substituted with {"id": <media uuid>, "type": "image_input"|...}.
"""
from __future__ import annotations

# Base params every model exposes; per-entry schema_extra overrides/extends.
BASE_IMAGE_PARAMS = {
    "prompt": {"type": "string", "title": "Prompt", "minLength": 1, "maxLength": 4000},
    "negative_prompt": {"type": "string", "title": "Negative Prompt"},
    "seed": {"type": "integer", "title": "Seed", "minimum": 0, "default": 0},
    "image_references": {
        "type": "array",
        "title": "Media Input",
        "items": {
            "type": "object",
            "title": "Media Input",
            "properties": {
                "id": {"type": "string", "format": "uuid"},
                "type": {"type": "string"},
            },
            "required": ["id", "type"],
        },
        "maxItems": 8,
    },
}

BASE_VIDEO_PARAMS = {
    "prompt": {"type": "string", "title": "Prompt", "minLength": 1, "maxLength": 4000},
    "negative_prompt": {"type": "string", "title": "Negative Prompt"},
    "seed": {"type": "integer", "title": "Seed", "minimum": 0, "default": 0},
    "duration": {"type": "number", "title": "Duration (s)", "minimum": 1, "maximum": 30, "default": 5},
    "fps": {"type": "integer", "title": "FPS", "minimum": 8, "maximum": 60, "default": 16},
    "start_image": {
        "type": "object",
        "title": "Media Input",
        "properties": {
            "id": {"type": "string", "format": "uuid"},
            "type": {"type": "string"},
        },
        "required": ["id", "type"],
    },
}

BASE_3D_PARAMS = {
    "prompt": {"type": "string", "title": "Prompt", "minLength": 1, "maxLength": 4000},
    "seed": {"type": "integer", "title": "Seed", "minimum": 0, "default": 0},
    "input_image": {
        "type": "object",
        "title": "Media Input",
        "properties": {
            "id": {"type": "string", "format": "uuid"},
            "type": {"type": "string"},
        },
        "required": ["id", "type"],
    },
}

_BASES = {"image": BASE_IMAGE_PARAMS, "video": BASE_VIDEO_PARAMS, "3d": BASE_3D_PARAMS}


def model_schema(entry: dict) -> dict:
    props = dict(_BASES[str(entry.get("type", "image"))])
    for key, node in (entry.get("schema_extra") or {}).items():
        props[key] = node
    return {
        "type": "object",
        "properties": props,
        "required": ["prompt"],
        "additionalProperties": True,
    }


def model_card(entry: dict) -> dict:
    """The catalog item shape the SDK's Model model parses."""
    return {
        "job_type": str(entry["job_type"]),
        "display_name": str(entry.get("display_name") or entry["job_type"]),
        "type": str(entry.get("type", "image")),
        "label": "model",
        "provider": str(entry.get("provider", "local")),
        "tags": list(entry.get("tags") or ["local"]),
        "description": str(entry.get("description") or "Local model via openfield"),
        "json_schema": model_schema(entry),
        "rules": [],
    }
