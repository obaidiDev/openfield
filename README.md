# OpenField

**OpenField is the Higgsfield Blender MCP stack, modified to be local-first.**
A self-hosted, stdlib-only backend that speaks the exact protocol of the
Higgsfield AI Blender add-on (its generation gateway + OAuth + MCP bridge
surfaces), so the add-on — floating viewport bar, model pickers, reference
uploads, asset library, agent-driven scene workflows — runs against **your**
models: a local ComfyUI, any OpenAI-compatible provider you hold an API key
for, or any command-line generator you write.

No Higgsfield account. No credits. Your prompts, your GPU, your provider keys.

```
Higgsfield Blender add-on  ──env overrides──▶  OpenField gateway (:8745)
      (unmodified, GPL-3.0)                          │
                                      ┌──────────────┼───────────────┐
                                 ComfyUI       OpenAI-compat      any local
                                (Flux, Wan,    providers          command
                                 Hunyuan3D)    (keys in config)
```

Everything is stdlib Python 3.11+. The wire contract was mapped from the
add-on's own shipped source (GPL-3.0) and the fnf_sdk-0.25.0 client it
bundles; `tests/test_e2e.py` proves compatibility by driving this gateway
**with that same vendored SDK** through sign-in, catalog validation (using
the add-on's own schema validator), upload, generation, polling and result
download — all green.

## Quick start

1. Install the Higgsfield Blender add-on from higgsfield.ai (Blender 5.1+).
2. Configure `config.toml`, then:

```bash
python3 -m venv .venv                                 # gateway is stdlib-only;
.venv/bin/pip install httpx attrs python-dateutil    # these power the test
./launch_blender.sh                                  # gateway + Blender pointed at it
```

3. In Blender click **Sign in** — the OAuth device flow auto-approves against
   localhost and you're in. The picker shows the catalog from `config.toml`.

## Pointing it at your models (`config.toml`)

**Catalog** — `[[catalog]]` entries drive the add-on's model pickers and
param forms (`type = image|video|3d` decides the tab; `schema_extra` adds
sliders/inputs):

```toml
[[catalog]]
job_type = "hf_flux_dev"
display_name = "Flux.1 dev (ComfyUI)"
type = "image"
backend_type = "comfyui"
backend_ref = "comfy-main"
comfy_workflow = "workflows/flux_dev.json"
```

**Backends** — local servers or hosted providers, with your keys:

- **ComfyUI**: `url = "http://127.0.0.1:8188"`, optional `input_dir` (your
  ComfyUI `input/` folder, so uploaded references land where `LoadImage`
  nodes read them). Workflows are exported **API-format** JSON; tokens:
  `{{prompt}} {{negative_prompt}} {{seed}} {{width}} {{height}} {{steps}}
  {{duration}} {{fps}} {{media}} {{media:0}}`.
- **OpenAI-compatible** (OpenAI, fal-style, local vLLM…): `base_url` +
  `api_key = "env:VARNAME"` to keep secrets out of the file.
- **Anything else**: `backend_type = "local"` with a `command`; receives
  `PROMPT/WIDTH/HEIGHT/SEED/DURATION/FPS/OUTPATH/MEDIA_URL_0..` and writes
  the result file to `OUTPATH`.

Auth, workspace and the cosmetic credit number are configured in the same
file.

## What the env overrides do (`launch_blender.sh`)

The add-on resolves every backend URL as `env var > baked > default`
(`runtime_config.py`) — no patching needed:

| var | effect |
|---|---|
| `HIGGSFIELD_SDK_BASE_URL` | generations, catalog, account → OpenField |
| `HIGGSFIELD_DEVICE_AUTH_ORIGIN` | OAuth device flow → OpenField |
| `HIGGSFIELD_ENV=dev` | allows loopback-HTTP OAuth (the add-on's own rule) |
| `HIGGSFIELD_MCP_WS_URL=ws://127.0.0.1:1/disabled` | kills the hosted bridge reconnect loop |
| `HIGGSFIELD_PHONECAM_ORIGIN=""` | disables phone-camera tab |
| `HIGGSFIELD_AMPLITUDE_API_KEY=""` | disables analytics |

Sign-in state lives in `~/.local/state/Higgsfield/Blender/auth.json` —
delete it to re-login.

## The MCP side

1. **Keep the add-on's bridge local:** point `HIGGSFIELD_MCP_URL` /
   `HIGGSFIELD_MCP_WS_URL` at your own relay — the add-on's outbound
   websocket protocol is a trivial JSON command/result envelope (see
   `bridge_runner.py` in its GPL source), agent side is plain MCP.
2. **Skip it:** the scene-control half of the add-on is Blender's own
   upstream MCP server (`blmcp`, by the Blender Authors). Standalone:

```bash
pip install "mcp<2" websockets pyyaml      # mcp<2 pin: blmcp targets FastMCP 1.x
python -m blmcp --transport http --port 8000
```

It speaks to Blender's socket bridge on `localhost:9876`; expose your
ComfyUI as MCP tools beside it and an agent gets the full loop.

## Status & limits

- ✅ image / video / 3D generation tabs, reference uploads, asset
  library/history, param forms, cost line (cosmetic), workspaces.
- ⚠️ Character-Animation rigging, phone-camera, and the chat "Supercomputer"
  surface are vendor pipelines — remove those catalog entries / env-disable;
  they show as unavailable.
- The add-on binary itself still installs from Higgsfield's site; OpenField
  replaces the backend only.
- First public release: tested against fnf_sdk 0.25.0 (add-on v1.5.58). If
  Higgsfield changes their client contract, expect a shim update — issues and
  PRs welcome.

## Layout

```
config.toml          # server, auth, catalog, backends — edit this
openfield/           # stdlib gateway (auth, catalog, jobs, media, executors)
workflows/           # ComfyUI API-format JSON workflows (sample provided)
vendor/              # vendor client copies used by the compatibility test only
tests/test_e2e.py    # full-flow proof driven by the vendor's own SDK
launch_blender.sh    # gateway + Blender with env overrides
```

Run tests: `.venv/bin/python tests/test_e2e.py` (needs the gateway up).

## License & provenance

GPL-3.0-or-later (consistent with the add-on's own license, from whose source
and bundled MIT-licensed SDK the wire protocol was read; attribution in
`vendor/README.md`).

**OpenField is independent and not affiliated with, endorsed by, or
sponsoring Higgsfield Inc.** "Higgsfield" is a trademark of its owner. The
add-on ships under GPL-3.0 with documented endpoint-override knobs; OpenField
is what those knobs are for — your machine talking to itself.
