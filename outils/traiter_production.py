#!/usr/bin/env python3
"""Traite une production de l'état de référence : mesures identiques pour A et B, rangement anonyme.

Usage : python3 traiter_production.py RUN_DIR BRIEF_NUM CONDITION NUMERO ETAT_DE_REFERENCE PAQUET
  RUN_DIR      dossier du run (travail/ et, pour B, journal.jsonl)
  PAQUET       paquet Design Governance dont on utilise check_render.py, check_caractere.py, journal_mobilisation.py
Écrit productions/<ID>/ (artefact, captures, sorties des recettes, réponse, trace, journal, fiche) et ajoute
une ligne à correspondance.csv (ID → brief, condition, numéro). L'ID est tiré au hasard.
"""
import csv
import json
import secrets
import shutil
import subprocess
import sys
from pathlib import Path

run, brief, cond, num, base, paquet = Path(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4], Path(sys.argv[5]), Path(sys.argv[6])
travail = run / "travail"
index = travail / "index.html"
if not index.is_file():
    sys.exit(f"pas d'index.html dans {travail}")
ident = "P" + secrets.token_hex(3).upper()
out = base / "productions" / ident
out.mkdir(parents=True)
# artefact : tout sauf la skill installée, le brief et ses données
ignorer = shutil.ignore_patterns(".claude", "brief.md", "reponse.md", "trace*", "*.jsonl", "__pycache__")
shutil.copytree(travail, out / "artefact", ignore=ignorer)
for f in travail.glob("reponse.md"):
    shutil.copy(f, out / "reponse.md")
for f in list(travail.glob("trace*")):
    (shutil.copytree if f.is_dir() else shutil.copy)(f, out / f.name)
# Aveugle : les commentaires HTML (trace en en-tête, notes) sont retirés de la copie évaluée et gardés à part.
import re
retires = []
for f in (out / "artefact").rglob("*.html"):
    texte = f.read_text(encoding="utf-8")
    retires += [f"--- {f.relative_to(out / 'artefact')}\n{c}" for c in re.findall(r"<!--.*?-->", texte, re.S)]
    f.write_text(re.sub(r"<!--.*?-->\n?", "", texte, flags=re.S), encoding="utf-8")
if retires:
    (out / "commentaires-retires.txt").write_text("\n\n".join(retires), encoding="utf-8")
env = {"PATH": "/usr/bin:/bin", "PLAYWRIGHT_BROWSERS_PATH": "/opt/pw-browsers", "HOME": str(Path.home())}
page = out / "artefact" / "index.html"
def lancer(args, nom):
    r = subprocess.run([sys.executable, *args], capture_output=True, text=True, env=env, cwd=paquet)
    (out / f"{nom}.txt").write_text(r.stdout + ("\n[stderr]\n" + r.stderr if r.stderr.strip() else ""), encoding="utf-8")
    return r.returncode
lancer([str(paquet / "scripts/check_render.py"), str(page), "--captures", str(out / "captures"), "--json", str(out / "recette-rendu.json")], "recette-rendu")
decl = base / "evaluateur" / f"caractere-{brief}.json"
lancer([str(paquet / "scripts/check_caractere.py"), str(page), str(decl), "--json", str(out / "caractere-attendu.json")], "caractere-attendu")
def est_declaration(p: Path) -> bool:
    try:
        d = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return False
    return isinstance(d, dict) and bool({"density", "material", "fonts"} & set(d))
propres = [p for p in travail.rglob("*.json") if ".claude" not in p.parts and est_declaration(p)]
if propres:
    shutil.copy(propres[0], out / "caractere-declare-par-le-run.json")
    lancer([str(paquet / "scripts/check_caractere.py"), str(page), str(propres[0]), "--json", str(out / "caractere-declare.json")], "caractere-declare")
journal = run / "journal.jsonl"
if journal.is_file():
    shutil.copy(journal, out / "journal.jsonl")
    lancer([str(paquet / "scripts/journal_mobilisation.py"), str(journal)], "fiche-mobilisation")
corr = base / "correspondance.csv"
nouveau = not corr.exists()
with corr.open("a", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    if nouveau:
        w.writerow(["id", "brief", "condition", "numero", "run"])
    w.writerow([ident, brief, cond, num, run.name])
print(ident)
