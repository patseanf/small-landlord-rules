# Builds base64 files + a SHA manifest for a Vercel MCP deploy (upload_file per file, then create_deployment with {file,sha,size}).
# Usage: python3 scripts/deploy-manifest.py /tmp/slr-deploy  -> writes NN.b64 and manifest.json
import base64, hashlib, json, os, subprocess, sys
out = sys.argv[1] if len(sys.argv) > 1 else "/tmp/slr-deploy"
os.makedirs(out, exist_ok=True)
files = [f for f in subprocess.check_output(["git", "ls-files"]).decode().split() if not f.startswith("scripts/build_data")]
man = []
for i, f in enumerate(files):
    b = open(f, "rb").read()
    p = f"{out}/{i:02d}.b64"
    open(p, "w").write(base64.b64encode(b).decode())
    man.append({"file": f, "sha": hashlib.sha1(b).hexdigest(), "size": len(b), "b64": p})
json.dump(man, open(f"{out}/manifest.json", "w"), indent=1)
print(f"{len(man)} files -> {out}/manifest.json")
