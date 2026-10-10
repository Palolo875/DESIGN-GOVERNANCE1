"""Mesure les caractères servis, en conservant doublons et lecture unique."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
def union_length(intervals):
    end=-1; total=0
    for a,b in sorted(intervals):
        if b>end:
            total+=b-max(a,end)
            end=b
    return total

metrics={}
for case in sorted((ROOT/'runs').iterdir()):
    log=case/'lectures.jsonl'
    if not log.exists():
        continue
    receipts=[json.loads(s) for s in log.read_text().splitlines()]
    by_key={}
    for item in receipts:
        entry=by_key.setdefault(item['key'],{'full_chars':item['full_chars'],'sha256':item['full_sha256'],'intervals':[],'before_artifact_intervals':[]})
        assert entry['sha256']==item['full_sha256']
        entry['intervals'].append((item['offset'],item['end']))
        if not item['artifact_already_exists']:
            entry['before_artifact_intervals'].append((item['offset'],item['end']))
    routes=[]
    for key,v in by_key.items():
        unique=union_length(v['intervals'])
        routes.append({'key':key,'full_chars':v['full_chars'],'unique_chars_served':unique,'read_completely':unique==v['full_chars'],'before_first_artifact_chars':union_length(v['before_artifact_intervals'])})
    metrics[case.name]={'requests':len(receipts),'chars_served_with_repetitions':sum(r['served_chars'] for r in receipts),'unique_chars_per_request_key':sum(x['unique_chars_served'] for x in routes),'chars_before_first_html_creation':sum(x['before_first_artifact_chars'] for x in routes),'routes':routes,'limits':'Instrumentation du lecteur seulement, en-têtes compris ; lecture directe non attestée ; aucun compteur de jetons ; avant premier fichier HTML, pas avant tout le travail de production.'}
(ROOT/'lecture-mesuree.json').write_text(json.dumps(metrics,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({k:{n:v[n] for n in ('requests','chars_served_with_repetitions','unique_chars_per_request_key','chars_before_first_html_creation')} for k,v in metrics.items()},ensure_ascii=False,indent=2))
