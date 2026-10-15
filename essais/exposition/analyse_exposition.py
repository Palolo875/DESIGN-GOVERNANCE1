#!/usr/bin/env python3
"""Exposition (étape 1) : quels passages ajoutés ont réellement été servis à l'agent, et quand ?

Entrées : journaux/sN.jsonl (un appel de read_route.py ou check_render.py par ligne, enregistré par une copie instrumentée du
paquet) et un dépôt DG propre à la version testée (argument 1). Chaque appel de lecture est rejoué sur ce dépôt propre pour savoir
quel texte il a servi ; les appels d'index (--sommaire, --trouver, --mode, --connexions) ne comptent pas comme lecture.
Limite : les dates d'accès aux fichiers (atime) sont inutilisables, read_route.py charge tout le corpus à chaque appel ;
seul ce journal fait foi, et les transcriptions montrent que les agents n'ont lu la skill que par ce script (plus SKILL.md).
"""
import json, subprocess, sys
from pathlib import Path

CLEAN = Path(sys.argv[1]); HERE = Path(__file__).parent
INDEX = {"--sommaire", "--trouver", "--mode", "--connexions"}
ROUTES = {  # passage ajouté -> route qui le porte
    "CFT-01 inventaire du sujet": "SAVOIR/CRAFT/CFT-01", "CFT-05 relations de couleur": "SAVOIR/CRAFT/CFT-05",
    "CFT-00 substance et mouvement": "SAVOIR/CRAFT/CFT-00", "CFT-06 écriture": "SAVOIR/CRAFT/CFT-06", "TYPE grand texte": "SAVOIR/TYPE",
    "CONTEXT durées": "SAVOIR/CONTEXT", "SOURCE images libres": "SAVOIR/SOURCE", "POINTS-DE-DEPART": "SAVOIR/TOOLS/POINTS-DE-DEPART",
    "GRID gabarit": "BIBLIOTHEQUE/GRID", "SCENE gabarit": "SCENE/EDITORIAL_FIELD",
}
print(f"{'passage ajouté (route lue en entier)':40s} " + " ".join(f"s{n}" for n in (1, 2, 3, 4)) + "   (t en s depuis le premier appel)")
logs = {n: [json.loads(l) for l in (HERE / "journaux" / f"s{n}.jsonl").read_text().splitlines()] for n in (1, 2, 3, 4)}
for label, route in ROUTES.items():
    cells = []
    for n in (1, 2, 3, 4):
        t0 = logs[n][0]["t"]
        full = [d["t"] - t0 for d in logs[n] if d["script"] == "read_route.py" and not (INDEX & set(d["argv"])) and route in " ".join(d["argv"])]
        idx = [d for d in logs[n] if d["script"] == "read_route.py" and (INDEX & set(d["argv"])) and route in " ".join(d["argv"])]
        cells.append(f"t={full[0]:3.0f}" if full else ("index" if idx else "  -  "))
    print(f"{label:40s} " + " ".join(f"{c:>6s}" for c in cells))
print()
for n in (1, 2, 3, 4):
    cr = [d["argv"] for d in logs[n] if d["script"] == "check_render.py"]
    rr = [d for d in logs[n] if d["script"] == "read_route.py" and not (INDEX & set(d["argv"]))]
    print(f"s{n}: {len(rr)} lectures de route ; {len(cr)} appels de check_render.py dont {sum('--mesures' in a for a in cr)} avec --mesures et {sum('--proof' in a for a in cr)} avec --proof")
