"""Lecteur instrumenté commun aux six producteurs ; aucune règle ajoutée."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, hashlib, json, os, subprocess, sys

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('run', choices=[f'run-{i:02}' for i in range(1,7)])
parser.add_argument('action', choices=['skill','route','mode','find','outline','connexions'])
parser.add_argument('argument', nargs='?')
parser.add_argument('--offset', type=int, default=0)
parser.add_argument('--limit', type=int, default=6000)
args = parser.parse_args()
case = ROOT/'runs'/args.run
packet = case/'paquet'
out = case/'livrable'
if args.offset < 0 or not 1 <= args.limit <= 6000:
    parser.error('offset >= 0 et 1 <= limit <= 6000')
if args.action == 'skill':
    if args.argument:
        parser.error('skill ne prend pas d’argument')
    text = (packet/'agent/skill/SKILL.md').read_text()
    key = 'skill'
else:
    if args.action in ('route','mode','find') and not args.argument:
        parser.error('argument requis')
    options = {'route': [], 'mode':['--mode'], 'find':['--trouver'], 'outline':['--sommaire'], 'connexions':['--connexions']}[args.action]
    if args.argument:
        options.append(args.argument)
    run = subprocess.run([sys.executable,'-B','scripts/read_route.py',*options],cwd=packet,capture_output=True,text=True)
    if run.returncode and not (args.action=='find' and run.returncode==1):
        sys.stderr.write(run.stderr or run.stdout)
        raise SystemExit(run.returncode)
    text = run.stdout
    key = args.action + ':' + (args.argument or '')
end = min(len(text),args.offset+args.limit)
chunk = text[args.offset:end]
receipt = {'time':datetime.now(timezone.utc).isoformat(),'key':key,'full_chars':len(text),'full_sha256':hashlib.sha256(text.encode()).hexdigest(),'offset':args.offset,'end':end,'served_chars':len(chunk),'artifact_already_exists':(out/'index.html').exists()}
log = case/'lectures.jsonl'
with log.open('a') as stream:
    stream.write(json.dumps(receipt,ensure_ascii=False)+'\n')
texts = case/'textes-servis'
texts.mkdir(exist_ok=True)
path = texts/(hashlib.sha256(key.encode()).hexdigest()[:16]+'.txt')
if path.exists() and path.read_text() != text:
    raise SystemExit('source modifiée pendant le run : arrêt')
path.write_text(text)
print(chunk,end='')
print(f'\n[LECTURE {key} : caractères {args.offset}..{end}/{len(text)} ; '+(f'suite --offset {end}' if end<len(text) else 'lecture terminée')+']')
