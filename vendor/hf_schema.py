"""JSON-Schema helpers for the dynamic FNF generation UI.

This module deliberately has no Blender dependency so schema normalization and
parameter validation can be tested with ordinary Python.
"""

from __future__ import annotations

import copy
import math
import re
from typing import Any


class SchemaError(ValueError):
    """Raised when a model schema or user-supplied JSON value is invalid."""


# A media picker is an interactive control, not an unbounded representation of
# a server-side array. This is also a hard safety boundary: catalog counts are
# never allowed to become larger RNA allocation/loop bounds.
MAX_MEDIA_SLOTS = 32
RNA_INT_MIN = -(2**31)
RNA_INT_MAX = 2**31 - 1
RNA_FLOAT_MAX = 3.402823466e38


def safe_descriptor(value):
    """Copy/sanitize catalog or persisted numeric metadata before UI arithmetic."""
    result = dict(value) if isinstance(value, dict) else {}
    integral = result.get("kind") == "integer"
    low, high = (
        (RNA_INT_MIN, RNA_INT_MAX) if integral else (-RNA_FLOAT_MAX, RNA_FLOAT_MAX)
    )
    invalid = bool(result.get("_invalid_bounds"))
    for key in (
        "minimum",
        "maximum",
        "exclusive_minimum",
        "exclusive_maximum",
        "multiple_of",
    ):
        number = result.get(key)
        if number is None:
            continue
        valid = _json_number(number) and low <= number <= high
        if key == "multiple_of":
            valid = valid and number >= (1 if integral else 1e-12)
        if not valid:
            result[key] = None
            invalid = True
    for key in ("min_items", "max_items", "min_length", "max_length"):
        number = result.get(key)
        ceiling = MAX_MEDIA_SLOTS if key.endswith("items") else RNA_INT_MAX
        if number is not None and (
            type(number) is not int or not 0 <= number <= ceiling
        ):
            result[key] = None
            invalid = True
    if (
        result.get("minimum") is not None
        and result.get("maximum") is not None
        and result["minimum"] > result["maximum"]
    ):
        result["minimum"] = result["maximum"] = None
        invalid = True
    if result.get("kind") in {"integer", "number"} and result.get("has_default"):
        number = result.get("default")
        if not _json_number(number) or not low <= number <= high:
            result["has_default"] = False
            result["default"] = None
    if invalid:
        result["_invalid_bounds"] = True
    return result


# Catalog schemas are untrusted graphs processed on Blender's main thread.
# These caps bound both the raw document walk and the work done while expanding
# local references. Normal FNF schemas are two orders of magnitude smaller.
MAX_SCHEMA_NODES = 4096
MAX_SCHEMA_DEPTH = 128
MAX_SCHEMA_RESOLUTION_STEPS = 8192


_SIZE_RULE_CANDIDATE = re.compile(
    r"^size\(params\.(\w+)\)\s*(==|<=|>=|<|>)\s*(\S+)\s*$"
)


def _json_number(value: Any) -> bool:
    if isinstance(value, bool):
        return False
    if isinstance(value, int):
        return True
    return isinstance(value, float) and math.isfinite(value)


def _item_count(node: dict[str, Any], keyword: str, path: str) -> int | None:
    value = node.get(keyword)
    if value is None:
        return None
    if type(value) is not int or not 0 <= value <= MAX_MEDIA_SLOTS:
        raise SchemaError(
            f"{path}.{keyword} must be an integer from 0 to {MAX_MEDIA_SLOTS}."
        )
    return value


def _validate_schema_node(node: dict[str, Any], path: str) -> None:
    minimum_items = _item_count(node, "minItems", path)
    maximum_items = _item_count(node, "maxItems", path)
    if (
        minimum_items is not None
        and maximum_items is not None
        and minimum_items > maximum_items
    ):
        raise SchemaError(f"{path}.minItems cannot exceed maxItems.")

    numeric = {}
    for keyword in (
        "minimum",
        "maximum",
        "exclusiveMinimum",
        "exclusiveMaximum",
        "multipleOf",
    ):
        value = node.get(keyword)
        if value is None:
            continue
        if not _json_number(value):
            raise SchemaError(f"{path}.{keyword} must be a finite JSON number.")
        numeric[keyword] = value
    if numeric.get("multipleOf", 1) <= 0:
        raise SchemaError(f"{path}.multipleOf must be greater than zero.")
    if (
        "minimum" in numeric
        and "maximum" in numeric
        and numeric["minimum"] > numeric["maximum"]
    ):
        raise SchemaError(f"{path}.minimum cannot exceed maximum.")

    if "default" not in node or node["default"] is None:
        return
    default = node["default"]
    node_type = node.get("type")
    if node_type == "integer" and type(default) is not int:
        raise SchemaError(f"{path}.default must be an integer.")
    if node_type == "number" and not _json_number(default):
        raise SchemaError(f"{path}.default must be a finite JSON number.")
    if node_type in {"integer", "number"}:
        if "minimum" in numeric and default < numeric["minimum"]:
            raise SchemaError(f"{path}.default is below minimum.")
        if "maximum" in numeric and default > numeric["maximum"]:
            raise SchemaError(f"{path}.default is above maximum.")
        if "exclusiveMinimum" in numeric and default <= numeric["exclusiveMinimum"]:
            raise SchemaError(f"{path}.default is not above exclusiveMinimum.")
        if "exclusiveMaximum" in numeric and default >= numeric["exclusiveMaximum"]:
            raise SchemaError(f"{path}.default is not below exclusiveMaximum.")
    if node_type == "array":
        if not isinstance(default, list):
            raise SchemaError(f"{path}.default must be an array.")
        if minimum_items is not None and len(default) < minimum_items:
            raise SchemaError(f"{path}.default has fewer than minItems values.")
        if maximum_items is not None and len(default) > maximum_items:
            raise SchemaError(f"{path}.default has more than maxItems values.")


def validate_json_schema(schema: dict[str, Any]) -> None:
    """Validate catalog-controlled bounds without resolving the schema graph.

    Walking declared subschemas directly is linear in the JSON document. In
    particular, validation must not expand a hostile ``$ref``/``allOf`` graph
    merely to decide whether a catalog is safe to cache.
    """
    if not isinstance(schema, dict):
        raise SchemaError("Model JSON Schema must be an object.")
    pending = [(schema, "schema", 0)]
    seen = set()
    while pending:
        node, path, depth = pending.pop()
        if depth > MAX_SCHEMA_DEPTH:
            raise SchemaError(
                f"Model JSON Schema exceeds depth limit {MAX_SCHEMA_DEPTH}."
            )
        identity = id(node)
        if identity in seen:
            continue
        seen.add(identity)
        if len(seen) > MAX_SCHEMA_NODES:
            raise SchemaError(
                f"Model JSON Schema exceeds node limit {MAX_SCHEMA_NODES}."
            )
        _validate_schema_node(node, path)

        for keyword in (
            "$defs",
            "definitions",
            "properties",
            "patternProperties",
            "dependentSchemas",
        ):
            children = node.get(keyword)
            if not isinstance(children, dict):
                continue
            for key, child in children.items():
                if isinstance(child, dict):
                    pending.append((child, f"{path}.{keyword}.{key}", depth + 1))
        for keyword in (
            "items",
            "additionalProperties",
            "contains",
            "not",
            "if",
            "then",
            "else",
            "propertyNames",
            "unevaluatedProperties",
        ):
            child = node.get(keyword)
            if isinstance(child, dict):
                pending.append((child, f"{path}.{keyword}", depth + 1))
        for keyword in ("allOf", "anyOf", "oneOf", "prefixItems"):
            children = node.get(keyword)
            if not isinstance(children, list):
                continue
            for index, child in enumerate(children):
                if isinstance(child, dict):
                    pending.append(
                        (child, f"{path}.{keyword}[{index}]", depth + 1)
                    )


def validate_media_rule_counts(rules: Any) -> None:
    """Reject unconditional CEL size bounds that cannot be safe UI limits."""
    if rules is None:
        return
    if not isinstance(rules, (list, tuple)):
        raise SchemaError("Model rules must be an array.")
    lows: dict[str, int] = {}
    highs: dict[str, int] = {}
    for index, rule in enumerate(rules):
        if not isinstance(rule, dict):
            raise SchemaError(f"Model rule {index} must be an object.")
        expression = str(rule.get("cel") or "").strip()
        match = _SIZE_RULE_CANDIDATE.fullmatch(expression)
        if not match:
            continue
        key, operator, raw_count = match.groups()
        if not raw_count.isascii() or not raw_count.isdigit():
            raise SchemaError(
                f"Media count in rule {index} must be a non-negative integer."
            )
        normalized_count = raw_count.lstrip("0") or "0"
        maximum_text = str(MAX_MEDIA_SLOTS)
        if len(normalized_count) > len(maximum_text) or (
            len(normalized_count) == len(maximum_text)
            and normalized_count > maximum_text
        ):
            raise SchemaError(
                f"Media count in rule {index} exceeds {MAX_MEDIA_SLOTS}."
            )
        count = int(normalized_count)
        low = count + (1 if operator == ">" else 0)
        high = count - (1 if operator == "<" else 0)
        if operator in {"==", ">=", ">"}:
            lows[key] = max(lows.get(key, 0), low)
        if operator in {"==", "<=", "<"}:
            highs[key] = min(highs.get(key, MAX_MEDIA_SLOTS), high)
        if not 0 <= lows.get(key, 0) <= highs.get(key, MAX_MEDIA_SLOTS):
            raise SchemaError(f"Media count rules for {key} are inconsistent.")


def validate_catalog_models(models: Any) -> None:
    """Fully describe every model before it is cached or exposed to Blender."""
    if not isinstance(models, list):
        raise SchemaError("Catalog models must be an array.")
    for index, model in enumerate(models):
        if not isinstance(model, dict):
            raise SchemaError(f"Catalog model {index} must be an object.")
        describe_object_schema(model.get("json_schema") or {})
        validate_media_rule_counts(model.get("rules"))


def _json_pointer(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise SchemaError(
            f"Only local JSON Schema references are supported: {reference}"
        )
    value: Any = root
    for raw_part in reference[2:].split("/"):
        part = raw_part.replace("~1", "/").replace("~0", "~")
        if not isinstance(value, dict) or part not in value:
            raise SchemaError(f"Unresolved JSON Schema reference: {reference}")
        value = value[part]
    if not isinstance(value, dict):
        raise SchemaError(f"JSON Schema reference is not an object: {reference}")
    return value


class _SchemaResolver:
    """One bounded, memoized resolution context for a schema root."""

    def __init__(self, root: dict[str, Any]):
        self.root = root
        self.memo: dict[str, dict[str, Any]] = {}
        self.steps = 0

    def resolve(
        self,
        node: dict[str, Any],
        seen: frozenset[str] = frozenset(),
        depth: int = 0,
    ) -> dict[str, Any]:
        if not isinstance(node, dict):
            return {}
        if depth > MAX_SCHEMA_DEPTH:
            raise SchemaError(
                f"JSON Schema resolution exceeds depth limit {MAX_SCHEMA_DEPTH}."
            )
        self.steps += 1
        if self.steps > MAX_SCHEMA_RESOLUTION_STEPS:
            raise SchemaError(
                "JSON Schema resolution exceeds work limit "
                f"{MAX_SCHEMA_RESOLUTION_STEPS}."
            )

        # Resolution only mutates top-level keys. A shallow copy prevents those
        # edits from touching the catalog without repeatedly copying whole
        # definition subtrees at every reference occurrence.
        resolved = dict(node)
        reference = resolved.pop("$ref", None)
        if reference is not None:
            if not isinstance(reference, str) or not reference:
                raise SchemaError("JSON Schema $ref must be a non-empty string.")
            if reference in seen:
                raise SchemaError(f"Circular JSON Schema reference: {reference}")
            if reference not in self.memo:
                target = self.resolve(
                    _json_pointer(self.root, reference),
                    seen | {reference},
                    depth + 1,
                )
                self.memo[reference] = target
            target = dict(self.memo[reference])
            target.update(resolved)
            resolved = target

        all_of = resolved.pop("allOf", None)
        if isinstance(all_of, list):
            merged: dict[str, Any] = {}
            for branch in all_of:
                if isinstance(branch, dict):
                    merged.update(self.resolve(branch, seen, depth + 1))
            merged.update(resolved)
            resolved = merged

        any_of = resolved.get("anyOf")
        if isinstance(any_of, list):
            non_null = [
                branch
                for branch in any_of
                if isinstance(branch, dict) and branch.get("type") != "null"
            ]
            nullable = len(non_null) != len(any_of)
            if len(non_null) == 1:
                branch = self.resolve(non_null[0], seen, depth + 1)
                branch.update(
                    {key: value for key, value in resolved.items() if key != "anyOf"}
                )
                if nullable:
                    branch["nullable"] = True
                resolved = branch

        return resolved


def resolve_schema_node(
    root: dict[str, Any], node: dict[str, Any], seen: frozenset[str] = frozenset()
) -> dict[str, Any]:
    """Resolve one schema node with bounded work and memoized local refs."""
    return _SchemaResolver(root).resolve(node, seen)


def _enum_options(
    resolver: _SchemaResolver, node: dict[str, Any]
) -> list[dict[str, Any]]:
    enum = node.get("enum")
    if isinstance(enum, list):
        return [{"value": value, "title": str(value)} for value in enum]

    one_of = node.get("oneOf")
    if not isinstance(one_of, list):
        return []
    options = []
    for raw_option in one_of:
        if not isinstance(raw_option, dict):
            return []
        option = resolver.resolve(raw_option)
        if "const" not in option:
            return []
        options.append(
            {
                "value": option["const"],
                "title": str(option.get("title", option["const"])),
                "description": str(option.get("description", "")),
            }
        )
    return options


def _is_media_object(resolver: _SchemaResolver, node: dict[str, Any]) -> bool:
    """True when ``node`` is a DeveloperAPIMediaInput object (id + type)."""
    properties = node.get("properties")
    if node.get("type") != "object" or not isinstance(properties, dict):
        return False
    id_schema = resolver.resolve(properties.get("id", {}))
    type_schema = resolver.resolve(properties.get("type", {}))
    return (
        id_schema.get("type") == "string"
        and (
            id_schema.get("format") == "uuid"
            or "media" in str(node.get("title", "")).lower()
        )
        and type_schema.get("type") == "string"
    )


def _is_media_input(resolver: _SchemaResolver, node: dict[str, Any]) -> bool:
    """True for an array of media objects, or a single media object.

    Kling, Veo and similar video models declare ``start_image`` /
    ``end_image`` / ``input_video`` / ``input_audio`` as one
    ``DeveloperAPIMediaInput``, not as an array. Treating only arrays as
    media left those fields as ``kind="json"``.
    """
    if _is_media_object(resolver, node):
        return True
    if node.get("type") != "array" or not isinstance(node.get("items"), dict):
        return False
    return _is_media_object(resolver, resolver.resolve(node["items"]))


def media_field_is_list(schema: dict[str, Any], key: str) -> bool:
    """Whether a media param is submitted as a list (array schema) or one dict."""
    if not isinstance(schema, dict):
        return True
    resolver = _SchemaResolver(schema)
    properties = resolver.resolve(schema).get("properties") or {}
    raw = properties.get(key)
    if not isinstance(raw, dict):
        return True
    return resolver.resolve(raw).get("type") == "array"


def describe_object_schema(schema: dict[str, Any]) -> list[dict[str, Any]]:
    """Convert an FNF model object schema into serializable UI descriptors."""
    validate_json_schema(schema)
    root = schema
    resolver = _SchemaResolver(root)
    object_schema = resolver.resolve(schema)
    properties = object_schema.get("properties", {})
    if not isinstance(properties, dict):
        raise SchemaError("Model JSON Schema properties must be an object.")
    required = set(object_schema.get("required") or [])
    descriptors = []
    for key, raw_node in properties.items():
        node = resolver.resolve(raw_node if isinstance(raw_node, dict) else {})
        options = _enum_options(resolver, node)
        node_type = node.get("type")
        if options:
            kind = "enum"
        elif _is_media_input(resolver, node):
            kind = "media"
        elif (
            node_type == "array"
            and isinstance(node.get("items"), dict)
            and resolver.resolve(node["items"]).get("type") == "string"
        ):
            kind = "string_list"
        elif node_type == "boolean":
            kind = "boolean"
        elif node_type == "integer":
            kind = "integer"
        elif node_type == "number":
            kind = "number"
        elif node_type == "string":
            kind = "string"
        else:
            kind = "json"

        has_default = "default" in node and node.get("default") is not None
        min_items = node.get("minItems")
        max_items = node.get("maxItems")
        media_list = True
        if kind == "media":
            media_list = node.get("type") == "array"
            if not media_list:
                if max_items is None:
                    max_items = 1
                if key in required and min_items is None:
                    min_items = 1
        descriptor = {
            "key": str(key),
            "title": str(node.get("title") or str(key).replace("_", " ").title()),
            "description": str(node.get("description") or ""),
            "kind": kind,
            "required": key in required,
            "nullable": bool(node.get("nullable")),
            "has_default": has_default,
            "default": copy.deepcopy(node.get("default")),
            "options": options,
            "minimum": node.get("minimum"),
            "maximum": node.get("maximum"),
            "exclusive_minimum": node.get("exclusiveMinimum"),
            "exclusive_maximum": node.get("exclusiveMaximum"),
            "multiple_of": node.get("multipleOf"),
            # A prompt's real length limit. Only some models declare one — Wan
            # takes 5000 characters, Seedance 60000, Meshy's text-to-3D 600 —
            # and the composer's field sizes itself from this rather than from
            # one number chosen for all of them.
            "max_length": node.get("maxLength"),
            "min_length": node.get("minLength"),
            "min_items": min_items,
            "max_items": max_items,
            "media_list": media_list,
            "schema": node,
        }
        descriptors.append(safe_descriptor(descriptor))
    return descriptors


def duration_for_seconds(
    descriptor: dict[str, Any], seconds: float
) -> float | int | None:
    """The `duration` this descriptor can express that covers ``seconds``.

    A duration is an enum of whole seconds on some models and a bounded integer
    on others, so a caller with a timeline length in hand cannot just assign it.
    Rounding *up* to the nearest offered value is deliberate: a shorter clip than
    the animation silently drops the end of the shot, while a longer one only
    pads it. When nothing on offer reaches ``seconds`` the longest wins, which is
    the same truncation `_fnf_viewport_video_plan` already reports.

    None when the descriptor is not a numeric duration at all.
    """
    options = [
        option.get("value")
        for option in descriptor.get("options") or ()
        if isinstance(option.get("value"), (int, float))
    ]
    if options:
        larger = [value for value in options if float(value) >= seconds]
        return min(larger) if larger else max(options)
    kind = descriptor.get("kind")
    if kind not in {"integer", "number"}:
        return None
    value = math.ceil(seconds)
    if descriptor.get("minimum") is not None:
        value = max(value, descriptor["minimum"])
    if descriptor.get("maximum") is not None:
        value = min(value, descriptor["maximum"])
    return int(value) if kind == "integer" else float(value)


def string_max_length(descriptor: dict[str, Any]) -> int | None:
    """The declared ``maxLength`` for a string field, or None.

    Falls back to the raw node because a params collection is saved in the
    .blend: one built before ``max_length`` was promoted still carries only the
    schema it was described from.
    """
    limit = descriptor.get("max_length")
    if limit is None:
        limit = (descriptor.get("schema") or {}).get("maxLength")
    if not isinstance(limit, (int, float)) or isinstance(limit, bool) or limit <= 0:
        return None
    return int(limit)


def check_string_length(descriptor: dict[str, Any], value: str) -> None:
    """Validate a declared string length Blender properties cannot enforce.

    A `StringProperty` takes a static `maxlen`, and this one is per model, so
    the sidebar can hold a prompt the model will refuse. Catching it here turns
    a backend rejection — after the credits question has been asked — into a
    message naming the field and the number.
    """
    limit = string_max_length(descriptor)
    if limit is None or len(value) <= limit:
        return
    title = str(descriptor.get("title") or descriptor.get("key") or "Value")
    raise SchemaError(
        f"{title} is {len(value)} characters; this model accepts at most {limit}."
    )


def check_numeric_bounds(descriptor: dict[str, Any], value: float | int) -> None:
    """Validate dynamic numeric bounds that Blender properties cannot declare per item."""
    minimum = descriptor.get("minimum")
    maximum = descriptor.get("maximum")
    exclusive_minimum = descriptor.get("exclusive_minimum")
    exclusive_maximum = descriptor.get("exclusive_maximum")
    if minimum is not None and value < minimum:
        raise SchemaError(f"{descriptor['title']} must be at least {minimum}.")
    if maximum is not None and value > maximum:
        raise SchemaError(f"{descriptor['title']} must be at most {maximum}.")
    if exclusive_minimum is not None and value <= exclusive_minimum:
        raise SchemaError(
            f"{descriptor['title']} must be greater than {exclusive_minimum}."
        )
    if exclusive_maximum is not None and value >= exclusive_maximum:
        raise SchemaError(
            f"{descriptor['title']} must be less than {exclusive_maximum}."
        )
