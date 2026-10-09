#!/usr/bin/env python3
"""Audit 2 (F12) : qui cite quoi, quels scripts verrouillent quelles phrases, quels blocs partent dans la skill.

Usage : dependances.py MESURES.json SORTIE.md
"""
import json, re, sys
from collections import defaultdict
from pathlib import Path
REPO = Path("/home/user/DESIGN-GOVERNANCE1")
m = json.load(open(sys.argv[1]))
names = {Path(d["fichier"]).name: d["fichier"] for d in m["documents"]}
cited_by = defaultdict(set)
for d in m["documents"]:
    for target in d["liens_relatifs"] + d["fichiers_cites"]:
        n = Path(target).name
        if n in names and names[n] != d["fichier"]:
            cited_by[names[n]].add(d["fichier"])
for c in m["controles"]:
    src = (REPO / c["fichier"]).read_text(encoding="utf-8")
    for n, full in names.items():
        if n in src:
            cited_by[full].add(c["fichier"])
locked = defaultdict(dict)
for c in m["controles"]:
    for f, k in (c.get("phrases_verrouillees_par_fichier") or {}).items():
        locked[f][c["fichier"].split("/")[-1]] = k
core = defaultdict(int)
for f in ("DIRECTION", "ACTION", "SAVOIR", "BIBLIOTHEQUE"):
    t = (REPO / f"V1/official/{f}.md").read_text(encoding="utf-8")
    core[f"V1/official/{f}.md"] = len(re.findall(r"<!-- noyau:début ", t))
lines = ["# Dépendances par fichier", "", "Produit par `AUDIT2/outils/dependances.py` à partir de `mesures.json`. Limite : les deux `README.md` portent le même nom ; "
         "leurs citations sont attribuées au README des sources, et « README.md » peut apparaître deux fois.", "",
         "| Fichier | Cité par (documents et scripts) | Phrases verrouillées par script | Blocs copiés dans la skill |", "|---|---|---|---:|"]
for d in sorted(m["documents"], key=lambda d: -d["caracteres"]):
    f = d["fichier"]
    lk = locked.get(f, {})
    lines.append(f"| `{f}` | {', '.join(sorted(Path(x).name for x in cited_by[f])) or '—'} | "
                 f"{', '.join(f'{k} {v}' for k, v in sorted(lk.items(), key=lambda x: -x[1])) or '—'} (total {sum(lk.values())}) | {core.get(f, 0)} |")
Path(sys.argv[2]).write_text("\n".join(lines) + "\n", encoding="utf-8")
print("\n".join(lines))
