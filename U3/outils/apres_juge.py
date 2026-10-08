#!/usr/bin/env python3
"""Archive le JSON rendu par un juge et vérifie modèle et fichiers ouverts dans sa transcription.
Usage : apres_juge.py JUGE JID TRANSCRIPT"""
import json, sys, re
juge, jid, src = sys.argv[1:4]
S = "/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/U3/jugement"
models, reads, final = set(), [], None
for line in open(src, encoding="utf-8"):
    try:
        ev = json.loads(line)
    except json.JSONDecodeError:
        continue
    m = ev.get("message") or {}
    if not isinstance(m, dict):
        continue
    if m.get("model"):
        models.add(m["model"])
    for p in m.get("content") or []:
        if isinstance(p, dict) and p.get("type") == "tool_use":
            inp = p.get("input") or {}
            if p.get("name") == "SubagentHandback":
                vals = [v for v in inp.values() if isinstance(v, str)]
                final = max(vals, key=len) if vals else final
            else:
                reads.append(f"{p.get('name')}:{inp.get('file_path') or inp.get('command') or ''}")
txt = final or ""
mt = re.search(r"\{.*\}", txt, re.S)
data = json.loads(mt.group(0)) if mt else {"brut": txt}
data["_modele"] = sorted(models)
json.dump(data, open(f"{S}/resultats/{juge}-{jid}.json", "w"), ensure_ascii=False, indent=1)
hors = [r for r in reads if "/U3/jugement/" not in r]
print(f"{juge} {jid} : modèle {sorted(models)} ; {len(reads)} lectures ; hors jugement : {hors[:3]} ; préférence {data.get('preference')} ({data.get('force')})")
