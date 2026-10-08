#!/usr/bin/env python3
"""Données de la carte visuelle du système, extraites des sources (aucune saisie à la main).

Usage : donnees_carte.py SORTIE.json
"""
import json, re, subprocess, sys
from pathlib import Path
REPO = Path("/home/user/DESIGN-GOVERNANCE1")
sys.path.insert(0, str(REPO / "scripts"))
import read_route as rr
D = (rr.OFFICIAL / "DIRECTION.md").read_text(encoding="utf-8")
table = D[D.find("<!-- noyau:début CHARGE-TABLE"):D.find("<!-- noyau:fin CHARGE-TABLE")]
modes = {}
for line in table.splitlines():
    if line.startswith("| **"):
        cells = line.split("|")
        modes[cells[1].strip().strip("*")] = (cells[2], cells[3])
skill = (REPO / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8")
core = skill[skill.find("<!-- noyau:compilé début -->"):skill.find("<!-- noyau:compilé fin -->")]
routes = []
for loc, name, size, subs, role in rr.summary_rows():
    pat = re.compile(r"`" + re.escape(loc) + r"(/[^`]*)?`")
    charge = {}
    for mode, (first, cond) in modes.items():
        if pat.search(first):
            charge[mode] = "d"
        elif pat.search(cond):
            charge[mode] = "s"
    outline = [{"t": t, "sub": s, "k": round(z / 1000, 1), "l": l} for l, t, s, z in rr.outline(loc)]
    routes.append({"loc": loc, "src": name[:-3], "k": round(size / 1000, 1), "subs": subs, "role": role,
                   "charge": charge, "noyau": loc in core, "outline": outline})
topics = [{"sujet": s, "proprio": o, "aussi": a} for s, o, a in rr.topics().values()]
passage = re.search(r"\*\*Règle de passage\.\*\* (.+)", D).group(1)
out = {"routes": routes, "modes": list(modes), "topics": topics, "passage": passage,
       "noyau_octets": len(skill.encode("utf-8")),
       "commit": subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip(),
       "sources": {f: len((rr.OFFICIAL / f"{f}.md").read_text(encoding="utf-8")) for f in ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE")}}
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False)
print(len(routes), "routes ;", {m: sum(1 for r in routes if m in r["charge"]) for m in modes}, "; commit", out["commit"])
print(passage)
