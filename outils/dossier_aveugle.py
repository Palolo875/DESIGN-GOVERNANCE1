#!/usr/bin/env python3
"""Construit le dossier d'évaluation à l'aveugle : paires A/B par brief, deux passages (ordre inversé), lettres neutres."""
import csv, random, shutil, sys
from pathlib import Path
base = Path(sys.argv[1]); out = base / "evaluation-aveugle"
if out.exists(): sys.exit(f"existe déjà : {out}")
rows = list(csv.DictReader(open(base / "correspondance.csv", encoding="utf-8")))
rng = random.SystemRandom()
paires = []
for brief in sorted({r["brief"] for r in rows}):
    a = sorted([r for r in rows if r["brief"] == brief and r["condition"] == "A"], key=lambda r: r["numero"])
    b = sorted([r for r in rows if r["brief"] == brief and r["condition"] == "B"], key=lambda r: r["numero"])
    paires += [(brief, x, y) for x, y in zip(a, b)]  # A n avec B n ; un A sans B en face reste hors évaluation
codes = rng.sample([a + b for a in "KLMNPRSTVXZ" for b in "AEIOU"], 4 * len(paires))
lettres = iter(codes)  # codes neutres à deux lettres, jamais réutilisés
cle, ordre1 = [], []
for brief, a, b in paires:
    g, d = (a, b) if rng.random() < .5 else (b, a)
    ordre1.append((brief, g, d))
rng.shuffle(ordre1)
ordre2 = [(brief, d, g) for brief, g, d in ordre1]; rng.shuffle(ordre2)
lignes = []
def copier(prod, dest):
    src = base / "productions" / prod["id"]
    shutil.copytree(src / "artefact", dest / "page", ignore=shutil.ignore_patterns("_atelier", "etude"))
    shutil.copytree(src / "captures", dest / "captures")
for passage, ordre in ((1, ordre1), (2, ordre2)):
    for i, (brief, p, s) in enumerate(ordre, 1):
        nom = f"passage-{passage}/{i:02d}-brief-{brief}"
        l1, l2 = next(lettres), next(lettres)
        copier(p, out / nom / f"premiere-{l1}"); copier(s, out / nom / f"seconde-{l2}")
        cle += [[passage, i, brief, "premiere", l1, p["id"]], [passage, i, brief, "seconde", l2, s["id"]]]
        for axe in ("fidelite", "realisation", "specificite", "usage"):
            lignes.append([passage, f"{i:02d}", brief, axe, "", ""])
with open(out / "evaluation.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f); w.writerow(["passage", "paire", "brief", "axe", "choix (premiere / seconde / equivalentes)", "raison en une phrase"]); w.writerows(lignes)
with open(base / "cle-aveugle.csv", "w", newline="", encoding="utf-8") as f:  # hors du dossier remis à l'évaluateur
    w = csv.writer(f); w.writerow(["passage", "paire", "brief", "position", "lettre", "id"]); w.writerows(cle)
print(len(paires), "paires ;", len(lignes), "lignes à remplir")
