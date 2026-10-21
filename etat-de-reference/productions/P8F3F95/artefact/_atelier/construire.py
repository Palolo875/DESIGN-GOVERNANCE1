"""Assemble index.html : gabarit + polices WOFF2 en base64 + copie verbatim de interventions.csv."""
import base64, pathlib
ici = pathlib.Path(__file__).resolve().parent
racine = ici.parent
src = (ici / "index.src.html").read_text(encoding="utf-8")
b64 = lambda p: base64.b64encode((ici / "fonts" / p).read_bytes()).decode()
csv = (racine / "interventions.csv").read_text(encoding="utf-8").strip()
assert "</script" not in csv.lower()
out = src.replace("__FONT_NEXT__", b64("next.woff2")).replace("__FONT_MONO__", b64("mono.woff2")).replace("__CSV__", csv)
(racine / "index.html").write_text(out, encoding="utf-8")
print("index.html", len(out.encode()), "octets")
