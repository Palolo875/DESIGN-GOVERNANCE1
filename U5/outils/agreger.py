#!/usr/bin/env python3
"""U5 : agrège les jugements à l'aveugle par paire (runs nommés, après levée de l'anonymat).

Usage : agreger.py SORTIE.md
Pour chaque paire : préférences des deux ordres et des deux juges, victoires par critère.
"""
import json
import sys
from collections import Counter, defaultdict

U5 = "/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/U5"
paires = json.load(open(f"{U5}/cle/paires.json"))
crit = ["presence", "specificite", "finition", "verite"]
par_paire = defaultdict(lambda: {"pref": [], **{c: Counter() for c in crit}})
detail = []
for juge in ("sonnet", "haiku"):
    for p in paires:
        try:
            r = json.load(open(f"{U5}/jugement/resultats/{juge}-{p['id']}.json"))
        except FileNotFoundError:
            detail.append(f"| {juge} | {p['id']} | manquant | | | | | |")
            continue
        def who(g):
            g = (g or "").strip().lower()
            return p["A"] if g == "a" else p["B"] if g == "b" else "égal"
        cle = " contre ".join(sorted((p["A"], p["B"])))
        row = {c: who(r.get(c, {}).get("gagnant")) for c in crit}
        pref = who(r.get("preference"))
        par_paire[cle]["pref"].append(f"{juge[0]}:{pref}({r.get('force')})")
        for c in crit:
            par_paire[cle][c][row[c]] += 1
        detail.append(f"| {juge} | {p['id']} | {p['A']} contre {p['B']} | " + " | ".join(row[c] for c in crit)
                      + f" | {pref} ({r.get('force')}) |")
lines = ["# U5 — Agrégation des jugements à l'aveugle", "",
         "| Paire | Préférences (s = Sonnet, h = Haiku ; quatre jugements) | présence | spécificité | finition | vérité |",
         "|---|---|---|---|---|---|"]
for cle, d in par_paire.items():
    fmt = lambda c: ", ".join(f"{k} {v}" for k, v in d[c].most_common())
    lines.append(f"| {cle} | {' ; '.join(d['pref'])} | " + " | ".join(fmt(c) for c in crit) + " |")
lines += ["", "## Détail", "", "| Juge | Jugement | Paire (A contre B) | présence | spécificité | finition | vérité | préférence |",
          "|---|---|---|---|---|---|---|---|"] + detail
open(sys.argv[1], "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("\n".join(lines[:16]))
