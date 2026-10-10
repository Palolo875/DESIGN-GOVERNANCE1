#!/usr/bin/env python3
"""Complément borné : couleurs de champs, frontières, focus et cibles réellement rendus."""
import hashlib
import http.server
import json
import re
import threading
from functools import partial
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'preuves'

def luminance(color):
    values = [float(x)/255 for x in re.findall(r'[\d.]+', color)[:3]]
    assert len(values)==3, color
    linear = [v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in values]
    return sum(v*w for v,w in zip(linear,[.2126,.7152,.0722]))

def ratio(a,b):
    l1,l2=sorted([luminance(a),luminance(b)])
    return (l2+.05)/(l1+.05)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):
        pass

server=http.server.ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
results=[]
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True)
        version=browser.version
        for width in [1440,390,320]:
            context=browser.new_context(viewport={'width':width,'height':1000 if width==1440 else 844},reduced_motion='reduce')
            page=context.new_page();page.goto(f'http://127.0.0.1:{server.server_port}/index.html');page.evaluate('document.fonts.ready')
            nominal=page.locator('body').aria_snapshot()
            (OUT/f'{width}-noms-nominal.txt').write_text(nominal)
            assert page.get_by_role('button',name='Ajouter une demi-heure',exact=True).count()==1
            assert page.get_by_role('button',name='Modifier cette prestation',exact=True).count()==1
            page.locator('#edit').click()
            (OUT/f'{width}-noms-editeur.txt').write_text(page.locator('#editor').aria_snapshot())
            assert page.get_by_role('dialog',name='Le détail compte.',exact=True).count()==1
            assert page.get_by_role('textbox',name='Votre client',exact=True).count()==1
            colors=page.evaluate('''()=>{
                const style=s=>getComputedStyle(document.querySelector(s));
                const field=style('#input-client'),handle=style('#handle');
                document.querySelector('#input-client').focus();
                const focus=style('#input-client');
                return {field:{color:field.color,background:field.backgroundColor,border:field.borderTopColor},focus:{color:focus.outlineColor,width:focus.outlineWidth},paper:style('#editor').backgroundColor,handle:handle.color,
                    targets:[...document.querySelectorAll('#editor button,#editor input')].map(n=>{const r=n.getBoundingClientRect();return{id:n.id||n.textContent.trim(),width:r.width,height:r.height};})};
            }''')
            checks=[{'pair':'valeur de champ / fond','ratio':ratio(colors['field']['color'],colors['field']['background']),'minimum':4.5}, {'pair':'frontière de champ / fond','ratio':ratio(colors['field']['border'],colors['field']['background']),'minimum':3}, {'pair':'focus / surface','ratio':ratio(colors['focus']['color'],colors['paper']),'minimum':3}]
            assert all(c['ratio']>=c['minimum'] for c in checks),checks
            assert float(colors['focus']['width'].replace('px',''))>=2
            assert all(t['width']>=43.9 and t['height']>=43.9 for t in colors['targets']),colors['targets']
            page.screenshot(path=str(OUT/f'{width}-editeur-focus.png'))
            results.append({'width':width,'checks':checks,'rendered_styles':colors,'accessible_names':'Sélecteurs de rôle/nom et snapshots Playwright dans Chromium ; pas test de lecteur d’écran.'})
            context.close()
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
report={'artifact_sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(),'browser_version':version,'results':results,'server_stopped':not thread.is_alive(),'passed':True,'limits':['Paires opaques sélectionnées ; aucun audit complet de contraste','Cibles mesurées dans le panneau ouvert, pas sur un téléphone physique','Sélecteurs accessibles et clavier ; aucun lecteur d’écran humain']}
(OUT/'complement-qualite.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'width':r['width'],'ratios':[{**x,'ratio':round(x['ratio'],3)} for x in r['checks']],'targets':len(r['rendered_styles']['targets'])} for r in results],ensure_ascii=False))
