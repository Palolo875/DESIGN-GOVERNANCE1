import json,shutil,tempfile,subprocess,hashlib,io
from pathlib import Path
from fontTools.ttLib import TTFont
ROOT=Path('/workspace/DESIGN-GOVERNANCE1');OUT=Path(__file__).parent;results=[]
files=json.loads((ROOT/'scripts/package_manifest.json').read_text())['github']
for scenario in ['baseline','couverture_perimee','police_alteree','police_complete']:
    with tempfile.TemporaryDirectory(prefix='dg-police-') as temporary:
        copy=Path(temporary)
        for name in files:
            p=copy/name;p.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/name,p)
        if scenario=='couverture_perimee':
            p=copy/'supports/systeme.json';data=json.loads(p.read_text());data['entries'][0]['description']+=' ñ';p.write_text(json.dumps(data,ensure_ascii=False))
        if scenario=='police_alteree':
            p=copy/'supports/fonts/manrope-supports.woff2';binary=bytearray(p.read_bytes());binary[-1]^=1;p.write_bytes(binary)
        if scenario=='police_complete':
            font=TTFont(copy/'supports/fonts/manrope.ttf',recalcTimestamp=False);font.flavor='woff2';stream=io.BytesIO();font.save(stream)
            (copy/'supports/fonts/manrope-supports.woff2').write_bytes(stream.getvalue())
            p=copy/'supports/fonts/couverture.json';data=json.loads(p.read_text());data['font_sha256']=hashlib.sha256(stream.getvalue()).hexdigest();p.write_text(json.dumps(data,ensure_ascii=False))
            subprocess.run(['python3','supports/generer.py'],cwd=copy,check=True,capture_output=True)
        run=subprocess.run(['python3','scripts/validate_supports.py'],cwd=copy,capture_output=True,text=True)
        expected={'couverture_perimee':'couverture périmée','police_alteree':'empreinte différente','police_complete':'budget de poids dépassé'}
        assert (run.returncode==0) == (scenario=='baseline'),(scenario,run.stdout,run.stderr)
        if scenario!='baseline':assert expected[scenario] in run.stdout,(scenario,run.stdout)
        results.append({'scenario':scenario,'result':'PASS' if scenario=='baseline' else 'REFUSED','diagnostics':run.stdout.splitlines()})
(OUT/'mutations-police.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print('POLICE CONTROL PASSED — baseline valide ; trois mutations refusées avec diagnostic attendu')
