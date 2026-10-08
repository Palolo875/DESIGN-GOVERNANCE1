#!/usr/bin/env python3
"""Agrège les jugements à l'aveugle : par critère, condition gagnante (avec / sans système), cohérence entre ordres.

Usage : agreger.py SORTIE.md
Lit cle/paires.json (A et B de chaque consigne → runs) et jugement/resultats/{juge}-{Jnn}.json.
"""
import json
import sys
from collections import Counter, defaultdict

S = "/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/U3"
cond = {"R1": "sans", "R2": "avec", "R3": "sans", "R4": "avec", "R5": "sans", "R6": "avec"}
paires = json.load(open(f"{S}/cle/paires.json"))
crit = ["presence", "specificite", "finition", "verite"]
lines = ["# U3 — Agrégation des jugements à l'aveugle", ""]
total = defaultdict(Counter)
detail = []
coh = Counter()
for juge in ("sonnet", "haiku"):
    par_paire = defaultdict(list)
    for p in paires:
        try:
            r = json.load(open(f"{S}/jugement/resultats/{juge}-{p['id']}.json"))
        except FileNotFoundError:
            detail.append(f"| {juge} | {p['id']} | manquant | | | | | |")
            continue
        def who(g):
            g = (g or "").strip().lower()
            return cond[p["A"]] if g == "a" else cond[p["B"]] if g == "b" else "égal"
        row = {c: who(r.get(c, {}).get("gagnant")) for c in crit}
        row["preference"] = who(r.get("preference"))
        for k, v in row.items():
            total[(juge, p["brief"], k)][v] += 1
        par_paire[frozenset((p["A"], p["B"]))].append(row["preference"])
        detail.append(f"| {juge} | {p['id']} | {p['brief']} | {p['A']}({cond[p['A']]}) contre {p['B']}({cond[p['B']]}) | "
                      + " | ".join(row[c] for c in crit) + f" | {row['preference']} ({r.get('force')}) |")
    for pair, prefs in par_paire.items():
        coh[(juge, "cohérent" if len(set(prefs)) == 1 else "inversé selon l'ordre")] += 1
lines += ["## Synthèse par juge, demande et critère (nombre de jugements remportés)", "",
          "| Juge | Demande | Critère | avec | sans | égal |", "|---|---|---|---|---|---|"]
for (juge, brief, k), c in sorted(total.items()):
    lines.append(f"| {juge} | {brief} | {k} | {c['avec']} | {c['sans']} | {c['égal']} |")
lines += ["", "## Cohérence de la préférence entre les deux ordres d'une même paire", ""]
lines += [f"- {j} : {etat} : {n}" for (j, etat), n in sorted(coh.items())]
lines += ["", "## Détail", "", "| Juge | Jugement | Demande | Paire | présence | spécificité | finition | vérité | préférence |",
          "|---|---|---|---|---|---|---|---|---|"] + detail
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines[:40]))
