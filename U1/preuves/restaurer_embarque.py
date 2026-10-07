import re, sys, hashlib, pathlib
src, dest = sys.argv[1], pathlib.Path(sys.argv[2])
text = pathlib.Path(src).read_bytes().decode("utf-8")
pat = r"<!-" r"- BEGIN FILE ([^\n]+?) sha256=([0-9a-f]{64}) fence=(\d*) -->\n((?s:.*?))\n<!-" r"- END FILE -->"
items = re.findall(pat, text)
count = re.search(r"<!-" r"- DG-COPY files=(\d+) -->", text)
if not count or not items or len(items) != int(count.group(1)):
    raise SystemExit("restauration refusée : inventaire incomplet ou absent")
files = {}; destinations = {}; base = dest.resolve()
for path, sha, fence, body in items:
    rel = pathlib.PurePosixPath(path)
    if rel.is_absolute() or ".." in rel.parts or "\\" in path or path != rel.as_posix() or path in files:
        raise SystemExit("restauration refusée : chemin incorrect ou répété : " + path)
    if fence:
        lines = body.split("\n"); marker = "`" * int(fence)
        if int(fence) < 3 or not lines[0].startswith(marker) or lines[-1] != marker:
            raise SystemExit("restauration refusée : clôture incorrecte : " + path)
        body = "\n".join(lines[1:-1])
    raw = body.encode("utf-8")
    if hashlib.sha256(raw).hexdigest() != sha:
        raise SystemExit("restauration refusée : empreinte divergente : " + path)
    out = (base / path).resolve()
    if out == base or not out.is_relative_to(base):
        raise SystemExit("restauration refusée : chemin hors destination : " + path)
    if out in destinations or any(out in previous.parents or previous in out.parents for previous in destinations):
        raise SystemExit("restauration refusée : destinations équivalentes ou fichier/dossier en collision : " + path)
    if (out.exists() and not out.is_file()) or any(parent.exists() and not parent.is_dir() for parent in out.parents):
        raise SystemExit("restauration refusée : destination incompatible : " + path)
    files[path] = raw
    destinations[out] = path
for path, raw in files.items():
    out = dest / path; out.parent.mkdir(parents=True, exist_ok=True); out.write_bytes(raw)
print(len(files), "fichiers restaurés et empreintes vérifiées dans", dest)
