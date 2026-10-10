#!/usr/bin/env python3
"""Compare la masse de l'entrée au même scope ; préférence du coordinateur, pas jugement aveugle."""
import hashlib
import http.server
import json
import threading
from functools import partial
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'preuves' / 'comparaison'
OUT.mkdir(exist_ok=True)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), partial(Handler, directory=str(ROOT)))
thread = threading.Thread(target=server.serve_forever, daemon=True)
thread.start()
results = []
try:
    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path='/usr/bin/chromium', headless=True)
        version = browser.version
        for width, height in [(1440, 1000), (390, 844), (320, 844)]:
            for name, enlarged in [('entree-ample', True), ('entree-reduite', False)]:
                context = browser.new_context(viewport={'width': width, 'height': height}, reduced_motion='reduce')
                page = context.new_page()
                page.goto(f'http://127.0.0.1:{server.server_port}/index.html')
                page.evaluate('document.fonts.ready')
                if enlarged:page.locator('body').evaluate('(n)=>n.classList.add("editorial-entry")')
                evidence = page.evaluate('''()=>({
                    viewport: {width:innerWidth,height:innerHeight},
                    title:document.querySelector('h1').textContent,
                    client:document.querySelector('#client').textContent,
                    service:document.querySelector('#service').textContent,
                    amount:document.querySelector('#total').textContent,
                    geometry:Object.fromEntries(['title','edit','quantity','total'].map(id=>{
                        const r=document.getElementById(id).getBoundingClientRect();
                        return[id,{top:r.top,bottom:r.bottom,height:r.height,fully_in_view:r.top>=0&&r.bottom<=innerHeight}];
                    }))
                })''')
                screenshot = OUT / f'{width}-{name}.png'
                page.screenshot(path=str(screenshot))
                evidence.update(width=width,variant=name,screenshot=screenshot.name,screenshot_sha256=hashlib.sha256(screenshot.read_bytes()).hexdigest())
                results.append(evidence)
                context.close()
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
for width in [1440,390,320]:
    a,b = [x for x in results if x['width']==width]
    for key in ['title','client','service','amount']:assert a[key]==b[key],key
report={'artifact_sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(),'browser_version':version,'server_stopped':not thread.is_alive(),'comparison':'Réduction de la masse du titre et de son espace supérieur ; contenu, familles, palette et tâche conservés. Le test ne compare pas deux architectures complètes.','results':results,'verdict':'À rédiger après inspection des captures ; pas de jugement aveugle.'}
(OUT/'comparaison.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'width':x['width'],'variant':x['variant'],'edit_visible':x['geometry']['edit']['fully_in_view'],'total_visible':x['geometry']['total']['fully_in_view'],'total_top':round(x['geometry']['total']['top'],1)} for x in results],ensure_ascii=False))
