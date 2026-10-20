Bundled copies used ONLY by tests/test_e2e.py, to prove protocol compatibility
with the exact client the Higgsfield Blender add-on ships:

- `higgsfield/` — the FNF Python SDK (fnf_sdk 0.25.0) extracted from the
  add-on's extension package. License: MIT (per the wheel's dist-info METADATA;
  the wheel's own metadata points to github.com/higgsfield-ai/fnf-sdk, which is
  currently private/not found, so the wheel is the only source).
- `hf_schema.py` — `fnf/schema.py` copied from the same add-on package
  (Copyright Higgsfield Inc., SPDX GPL-3.0-or-later), used to validate our
  catalog against the add-on's own validator.

Convenience copy for the "MCP side" setup in the README:

- `blender_mcp-1.0.0-py3-none-any.whl` — the official Blender MCP server
  (`blmcp`) by the Blender Authors, bundled unmodified inside the Higgsfield
  add-on package. SPDX GPL-3.0-or-later. Upstream:
  https://projects.blender.org/lab/blender_mcp

Everything else in this repository is original work under GPL-3.0-or-later.
"Higgsfield" is a trademark of its respective owner; this project is
independent and unaffiliated.
