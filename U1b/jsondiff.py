import json, sys, glob, os
base = json.load(open(sys.argv[1]))
def diff(a, b, p=""):
    out = []
    if isinstance(a, dict) and isinstance(b, dict):
        for k in sorted(set(a) | set(b)):
            if k not in a: out.append(f"+ {p}/{k} = {json.dumps(b[k], ensure_ascii=False)}")
            elif k not in b: out.append(f"- {p}/{k}")
            else: out += diff(a[k], b[k], f"{p}/{k}")
    elif a != b:
        out.append(f"~ {p}: {json.dumps(a, ensure_ascii=False)} -> {json.dumps(b, ensure_ascii=False)}")
    return out
for f in sorted(glob.glob(sys.argv[2])):
    print("=== " + os.path.basename(f))
    for l in diff(base, json.load(open(f))): print("  " + l)
