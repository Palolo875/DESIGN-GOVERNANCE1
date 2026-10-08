#!/usr/bin/env bash
# Après un run : journal de la transcription, réponse finale archivée, recette et captures.
# Usage : apres_run.sh RUN_ID DOSSIER_RUN TRANSCRIPT
set -u
S=/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/U5
id=$1; dir=$2; tr=$3
mkdir -p "$S/journaux" "$S/reponses" "$S/recettes" "$S/captures"
python3 "$S/outils/journal_run.py" "$tr" "$S/journaux/$id.md"
echo "--- appels hors périmètre :"
grep -E "^[0-9]+\." "$S/journaux/$id.md" | grep -v -e "$dir" -e "U5/paquet" -e "U5 && find paquet" -e "SubagentHandback" | cut -c1-200
python3 - "$tr" "$S/reponses/$id.md" <<'EOF'
import json, sys
text = None
for line in open(sys.argv[1], encoding="utf-8"):
    try:
        ev = json.loads(line)
    except json.JSONDecodeError:
        continue
    m = ev.get("message") or {}
    for p in (m.get("content") or []) if isinstance(m, dict) else []:
        if isinstance(p, dict) and p.get("type") == "tool_use" and p.get("name") == "SubagentHandback":
            vals = [v for v in (p.get("input") or {}).values() if isinstance(v, str)]
            text = max(vals, key=len) if vals else text
open(sys.argv[2], "w", encoding="utf-8").write(text or "(réponse finale introuvable)")
EOF
cd /home/user/DESIGN-GOVERNANCE1 && python3 scripts/check_render.py "$dir/index.html" --widths 390,1440 --allow-external \
  --captures "$S/captures/$id" --json "$S/recettes/$id.json" > "$S/recettes/$id.txt" 2>&1
echo "--- recette (code $?) :"
grep -E "^\[" "$S/recettes/$id.txt" | cut -c1-170
