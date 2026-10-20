#!/usr/bin/env python3
"""Minimal PNG writer used as the 'local' backend for the e2e test.
Reads PROMPT/WIDTH/HEIGHT/SEED/OUTPATH from env; writes a valid PNG to OUTPATH.
"""
import os
import struct
import zlib

W = int(os.environ.get("WIDTH") or 1024)
H = int(os.environ.get("HEIGHT") or 1024)
W, H = min(W, 256), min(H, 256)  # test image stays small
seed = int(os.environ.get("SEED") or 0)


def chunk(tag, data):
    return (
        struct.pack(">I", len(data))
        + tag
        + data
        + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    )


rows = b""
for y in range(H):
    row = b"\x00"
    for x in range(W):
        r = (x * 255 // max(W - 1, 1) + seed) % 256
        g = (y * 255 // max(H - 1, 1)) % 256
        b = ((x + y) * 255 // max(W + H - 2, 1)) % 256
        row += bytes((r, g, b))
    rows += row

png = (
    b"\x89PNG\r\n\x1a\n"
    + chunk(b"IHDR", struct.pack(">IIBBBBB", W, H, 8, 2, 0, 0, 0))
    + chunk(b"IDAT", zlib.compress(rows, 6))
    + chunk(b"IEND", b"")
)
out = os.environ.get("OUTPATH") or "out.png"
with open(out, "wb") as fh:
    fh.write(png)
print(f"wrote {out} ({W}x{H}) prompt={os.environ.get('PROMPT','')!r}")
