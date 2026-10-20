#!/usr/bin/env bash
# Launch the openfield gateway, then Blender pointed at it.
# Usage: ./launch_blender.sh [path-to-blender]
set -euo pipefail
cd "$(dirname "$0")"

HF_URL="http://127.0.0.1:8745"
BLENDER_BIN="${1:-blender}"

# start the gateway if nothing owns the port yet
if ! curl -s -m 2 "$HF_URL/healthz" >/dev/null 2>&1; then
  .venv/bin/python -m openfield.gateway --config config.toml >> gateway.log 2>&1 &
  echo "gateway started (pid $!), log: gateway.log"
  for _ in $(seq 1 20); do
    curl -s -m 2 "$HF_URL/healthz" >/dev/null 2>&1 && break
    sleep 0.3
  done
fi

export HIGGSFIELD_ENV=dev                       # allows loopback-HTTP OAuth
export HIGGSFIELD_SDK_BASE_URL="$HF_URL"        # generations + account
export HIGGSFIELD_NOTIFICATION_BASE_URL="$HF_URL"
export HIGGSFIELD_DEVICE_AUTH_ORIGIN="$HF_URL"  # our device-flow auth
# keep the hosted bridge & phonecam OFF / inert
export HIGGSFIELD_MCP_WS_URL="ws://127.0.0.1:1/disabled"
export HIGGSFIELD_PHONECAM_ORIGIN=""
# silence the baked Amplitude analytics key
export HIGGSFIELD_AMPLITUDE_API_KEY=""

# --online-mode lets the Blender Lab "MCP" extension auto-start its socket
# bridge on localhost:9876, which the `blmcp` server (and Claude Code) use.
exec "$BLENDER_BIN" --online-mode
