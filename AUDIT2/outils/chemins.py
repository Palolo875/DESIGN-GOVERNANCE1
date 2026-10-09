#!/usr/bin/env python3
"""Audit 2 (phase 1) : ce que l'agent lit avant de produire, par chemin (critère S2).

Taille servie par le lecteur (`read_route.py LOCATOR`, avec repli des blocs du noyau), plus la skill.
Les listes viennent de la colonne « Charger d'abord » de DIRECTION/CHARGE ; les routes conditionnelles sont
comptées à part. Chaque route est rangée dans une famille : design (direction, savoir, formes), produit
(premier rendu, réalité UI/UX, preuve visuelle, craft sur rendu) ou gouvernance (runs, gates, traces, clôture).

Usage : chemins.py SORTIE.json
"""
import json, re, subprocess, sys
from pathlib import Path
REPO = Path("/home/user/DESIGN-GOVERNANCE1")
PRODUIT = {"ACTION/FIRST-RENDER", "ACTION/UI-UX-REALITY", "ACTION/VISUAL_PROOF", "ACTION/GATE-C"}

def famille(loc):
    if loc.startswith(("DIRECTION/", "SAVOIR/", "BIBLIOTHEQUE/")):
        return "design"
    return "produit" if loc in PRODUIT else "gouvernance"

def servi(loc):
    r = subprocess.run([sys.executable, "scripts/read_route.py", loc], cwd=REPO, capture_output=True, text=True)
    return len(r.stdout) if r.returncode == 0 else None

skill = len((REPO / "skills/design-governance-practice/SKILL.md").read_text(encoding="utf-8"))
CHEMINS = {
    "LITE (petite correction)": ["ACTION/RUN-LITE", "ACTION/FAST-PATH", "ACTION/GATE-A", "ACTION/GATE-B/B2", "ACTION/GATE-B/B6"],
    "ITER (itération sur l'existant)": ["ACTION/RUN-ITER", "ACTION/GATE-A", "ACTION/GATE-B"],
    "STANDARD (écran ou page cadrés)": ["ACTION/RUN-STANDARD", "ACTION/UI-UX-REALITY", "BIBLIOTHEQUE/SELECT", "ACTION/GATE-A", "ACTION/GATE-B"],
    "DIRECTION, trace légère (page nouvelle)": ["DIRECTION/EXTERNAL-START", "DIRECTION/CREATIVE-BOOT", "DIRECTION/VISUAL_TARGET",
        "DIRECTION/FIRST-OBJECT", "SAVOIR/TYPE", "ACTION/FIRST-RENDER", "ACTION/UI-UX-REALITY", "ACTION/RUN-DIRECTION",
        "ACTION/PIPELINE-DIRECTION", "ACTION/VISUAL_PROOF", "ACTION/GATE-A", "ACTION/GATE-C"],
}
CHEMINS["DIRECTION, trace complète (produit livré)"] = CHEMINS["DIRECTION, trace légère (page nouvelle)"] + ["ACTION/GATE-B", "ACTION/RUN_CARD", "ACTION/CLOSE-PACKAGE"]
CONDITIONNELLES_DIRECTION = ["DIRECTION/DOUBLE-LOOP", "ACTION/ROUTING", "SAVOIR/CRAFT/CFT-00", "DIRECTION/DIRECTION-ATELIER",
    "SAVOIR/FRAME", "SAVOIR/CRAFT", "SAVOIR/SOURCE", "BIBLIOTHEQUE/SELECT", "BIBLIOTHEQUE/SEQUENCE", "DIRECTION/DOMAIN-FRAME",
    "SAVOIR/STYLE", "SAVOIR/STATE", "SAVOIR/INTEGRITY"]
out = {"skill": skill, "chemins": {}, "conditionnelles_direction": {}}
for nom, locs in CHEMINS.items():
    rows = [(l, servi(l), famille(l)) for l in locs]
    tot = {f: sum(s or 0 for _, s, g in rows if g == f) for f in ("design", "produit", "gouvernance")}
    out["chemins"][nom] = {"routes": rows, "par_famille": tot, "routes_total": sum(tot.values()),
                           "avec_skill": skill + sum(tot.values()), "introuvables": [l for l, s, _ in rows if s is None]}
for l in CONDITIONNELLES_DIRECTION:
    out["conditionnelles_direction"][l] = servi(l)
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(f"skill {skill:,} caractères")
for nom, c in out["chemins"].items():
    print(f"{nom:45} routes {c['routes_total']:>7,}  + skill = {c['avec_skill']:>7,}  {c['par_famille']}  {c['introuvables'] or ''}")
print("conditionnelles DIRECTION :", sum(v or 0 for v in out["conditionnelles_direction"].values()), out["conditionnelles_direction"])
