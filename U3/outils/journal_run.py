#!/usr/bin/env python3
"""Résumé d'une transcription de sous-agent (JSONL) : outils appelés, fichiers lus, commandes, routes chargées.

Usage : python3 journal_run.py TRANSCRIPT.jsonl SORTIE.md
Ne recopie pas les contenus lus : seulement ce qui permet de vérifier le périmètre et les routes ouvertes.
"""
import json
import re
import sys
from collections import Counter

src, out = sys.argv[1], sys.argv[2]
calls, model, usage = [], set(), Counter()
for line in open(src, encoding="utf-8"):
    try:
        ev = json.loads(line)
    except json.JSONDecodeError:
        continue
    msg = ev.get("message") or {}
    if isinstance(msg, dict):
        if msg.get("model"):
            model.add(msg["model"])
        for k, v in (msg.get("usage") or {}).items():
            if isinstance(v, int):
                usage[k] += v
        for part in msg.get("content") or []:
            if isinstance(part, dict) and part.get("type") == "tool_use":
                inp = part.get("input") or {}
                detail = inp.get("file_path") or inp.get("command") or inp.get("pattern") or inp.get("path") or ""
                calls.append((part.get("name"), str(detail).replace("\n", " ")[:220]))

routes = []
for name, detail in calls:
    for m in re.finditer(r"read_route\.py\s+([^\s|;&]+(?:\s+\"[^\"]*\")?)", detail):
        routes.append(m.group(1))
lines = [f"# Journal de {src.rsplit('/', 1)[-1]}", "",
         f"- Modèle(s) déclaré(s) par la transcription : {', '.join(sorted(model)) or 'non indiqué'}",
         f"- Appels d'outils : {len(calls)} ({', '.join(f'{k} {v}' for k, v in Counter(c[0] for c in calls).most_common())})",
         f"- Jetons (somme des usages rapportés) : {dict(usage)}",
         f"- Routes lues par read_route : {', '.join(routes) or 'aucune'}", "", "## Appels", ""]
lines += [f"{i + 1}. `{n}` — {d}" for i, (n, d) in enumerate(calls)]
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"{len(calls)} appels ; routes : {len(routes)} ; modèle : {', '.join(sorted(model)) or '?'}")
