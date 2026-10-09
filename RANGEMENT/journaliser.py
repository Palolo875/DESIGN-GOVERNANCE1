#!/usr/bin/env python3
"""Phase 4 : inscrire au journal des retraits les blocs de la base qui ont été réécrits, avec une raison.
Refuse d'écrire si un bloc perdu ne vient pas des fichiers annoncés (rien ne part par mégarde).
Usage : journaliser.py DEPOT LOT RAISON FICHIER_DE_BASE [FICHIER_DE_BASE ...]"""
import csv, importlib.util, json, sys
from pathlib import Path

here = Path(__file__).parent
repo, lot, raison, allowed = Path(sys.argv[1]), sys.argv[2], sys.argv[3], set(sys.argv[4:])
spec = importlib.util.spec_from_file_location("cons", here / "conservation.py"); c = importlib.util.module_from_spec(spec)
argv, sys.argv = sys.argv, ["x"]; spec.loader.exec_module(c); sys.argv = argv
base = json.load(open(here / "base.json", encoding="utf-8"))["blocs"]
retired = {r["empreinte"] for r in csv.DictReader(open(here / "retraits.csv", encoding="utf-8"))}
found = c.scan(repo)
lost = [(d, v) for d, v in base.items() if d not in found and d not in retired]
stray = [v["origine"] for _, v in lost if v["origine"].split(":")[0] not in allowed]
if stray:
    raise SystemExit(f"REFUS — blocs perdus hors des fichiers annoncés : {stray}")
with open(here / "retraits.csv", "a", encoding="utf-8", newline="") as fh:
    csv.writer(fh).writerows([d, lot, v["origine"], raison, v["debut"][:90]] for d, v in lost)
print(f"{len(lost)} bloc(s) inscrit(s) : " + ", ".join(v["origine"] for _, v in lost))
