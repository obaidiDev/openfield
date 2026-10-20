#!/usr/bin/env python3
"""End-to-end proof: the vendored Higgsfield SDK (the exact wheel the Blender
add-on ships, fnf_sdk 0.25.0) driven against the local openfield gateway, using
the same RFC 8628 device flow the add-on uses, and the add-on's own catalog
schema validator on the catalog we serve.
"""
import json
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))          # openfield/
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "vendor"))  # higgsfield, hf_schema

BASE = "http://127.0.0.1:8745"


def post_form(url, fields):
    data = urllib.parse.urlencode(fields).encode()
    req = urllib.request.Request(url, data=data, method="POST",
                                 headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def device_login():
    # exactly what fnf/session.py does: discover, device code, poll token
    meta = json.loads(urllib.request.urlopen(
        f"{BASE}/.well-known/oauth-authorization-server", timeout=10).read())
    assert meta["device_authorization_endpoint"], "no device endpoint advertised"
    st, dev = post_form(meta["device_authorization_endpoint"], {"client_id": "blender"})
    assert st == 200, (st, dev)
    print(f"  device code issued: user_code={dev['user_code']}")
    deadline = time.time() + 20
    while time.time() < deadline:
        st, tok = post_form(meta["token_endpoint"], {
            "client_id": "blender",
            "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
            "device_code": dev["device_code"],
        })
        if st == 200 and tok.get("access_token"):
            print(f"  access token issued (expires_in={tok['expires_in']})")
            return tok
        if tok.get("error") not in ("authorization_pending", None):
            raise AssertionError(f"auth failed: {tok}")
        time.sleep(1)
    raise AssertionError("device flow never completed")


def main():
    print("[1] device-code sign-in (same flow as fnf/session.py)")
    tok = device_login()
    access = tok["access_token"]
    refresh = tok["refresh_token"]

    print("[2] refresh flow (same as _refresh_oauth_token)")
    st, tok2 = post_form(f"{BASE}/oauth/token",
                         {"client_id": "blender", "grant_type": "refresh_token",
                          "refresh_token": refresh})
    assert st == 200 and tok2.get("access_token") and tok2.get("id_token"), (st, tok2)
    # id_token must carry a readable exp for the add-on's refresh scheduler
    import base64
    payload = tok2["id_token"].split(".")[1]
    claims = json.loads(base64.urlsafe_b64decode(payload + "=="))
    assert claims["exp"] > time.time(), "id_token exp not in future"
    print(f"  refreshed; id_token exp={claims['exp']:.0f}")
    access = tok2["access_token"]

    print("[3] vendor SDK client against the gateway")
    from higgsfield import Higgsfield
    client = Higgsfield(api_key=access, base_url=BASE)

    balance = client.account.get_balance(timeout=15)
    assert balance.credits_ > 0, "no credits"
    print(f"  balance: {balance.credits_} credits, plan={balance.subscription_plan_type}, email={balance.email}")
    ws = client.account.list_workspaces(timeout=15)
    assert ws.items and ws.items[0].is_selected
    print(f"  workspaces: {[w.name for w in ws.items]}")

    print("[4] catalog + the add-on's own schema validator (fnf/schema.py)")
    import hf_schema
    page = client.job_types.list(type="image", label=["model"], limit=100)
    models = [m.to_dict() for m in page.items]
    hf_schema.validate_catalog_models(models)  # raises SchemaError if our cards are malformed
    print(f"  image catalog: {[m['job_type'] for m in models]} (validator ok)")
    descs = hf_schema.describe_object_schema(models[0]["json_schema"])
    kinds = {d["key"]: d["kind"] for d in descs}
    assert kinds.get("prompt") == "string" and kinds.get("image_references") == "media", kinds
    print(f"  param descriptors: {kinds}")

    print("[5] cost estimate + media upload (slot -> PUT -> confirm)")
    est = client.jobs.estimate_cost(job_type="hf_test_local", params={"prompt": "x"})
    assert est.credits_ == 0
    print(f"  cost estimate: {est.credits_}")
    ref_png = Path("tests/ref.png").resolve()
    env = {"WIDTH": "64", "HEIGHT": "64", "SEED": "1",
           "OUTPATH": str(ref_png), "PROMPT": "ref", "PATH": "/usr/bin:/bin"}
    subprocess.run([sys.executable, "tests/gen_test_image.py"], env=env, check=True,
                   capture_output=True)
    media_input = client.media.upload(str(ref_png), type="image", timeout=60)
    assert media_input.id
    inp = media_input.as_input()
    print(f"  uploaded media id={media_input.id} as_input={inp}")

    print("[6] submit generation -> poll wait_for_job (backend: local command)")
    submitted = client.images.create(job_type="hf_test_local",
                                     params={"prompt": "a test checkerboard",
                                             "image_references": [inp]})
    assert submitted.id and submitted.job_type == "hf_test_local"
    print(f"  submitted job {submitted.id}")
    finished = client.wait_for_job(str(submitted.id), interval=1.0, timeout=60)
    assert finished.status == "completed", finished.status
    assert finished.result_url, "no result_url"
    print(f"  job completed; result_url={finished.result_url}")

    print("[7] result bytes are fetchable (the add-on downloads these)")
    data = urllib.request.urlopen(finished.result_url, timeout=30).read()
    assert data[:8] == b"\x89PNG\r\n\x1a\n", "result is not a PNG"
    print(f"  downloaded {len(data)} bytes, valid PNG")

    print("[8] jobs list (history surface)")
    jobs = client.jobs.list(size=10)
    assert any(str(j.id) == str(submitted.id) for j in jobs.items)
    print(f"  history has {len(jobs.items)} job(s)")

    client.close()
    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
