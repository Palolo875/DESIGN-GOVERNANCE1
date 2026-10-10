from pathlib import Path
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
import json,datetime,hashlib
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parent
class Q(SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
s=ThreadingHTTPServer(('127.0.0.1',0),partial(Q,directory=str(R)));Thread(target=s.serve_forever,daemon=True).start()
def lum(h):
    v=[int(h[i:i+2],16)/255 for i in (1,3,5)];v=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in v];return sum(x*y for x,y in zip(v,[.2126,.7152,.0722]))
def ratio(a,b):
    x,y=sorted([lum(a),lum(b)]);return round((y+.05)/(x+.05),3)
colors=[('texte principal','#172d2b','#f7f8f2',4.5),('texte secondaire','#52625c','#f7f8f2',4.5),('facture secondaire','#52625c','#ffffff',4.5),('texte champ de preuve','#172d2b','#e4ecce',4.5),('texte de section sombre','#c8d3ca','#172d2b',4.5),('action sombre','#f7f8f2','#172d2b',4.5),('statut','#d5ea7d','#264440',4.5),('message d’erreur','#972c25','#ffebe6',4.5),('erreur locale','#972c25','#f7f8f2',4.5),('focus clair','#426339','#f7f8f2',3),('focus champ de preuve','#426339','#e4ecce',3),('focus sombre','#d5ea7d','#172d2b',3),('frontière input','#76887a','#ffffff',3)]
out={'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'artifact_sha256':hashlib.sha256((R/'index.html').read_bytes()).hexdigest(),'method':'Calcul sRGB et inspection DOM dans Chromium','contrast':[{'role':n,'foreground':a,'background':b,'ratio':ratio(a,b),'threshold':t,'result':'PASS' if ratio(a,b)>=t else 'FAIL'} for n,a,b,t in colors],'limits':['Ces paires couvrent les principaux rôles opaques ; aucune certification exhaustive.','Pseudo-contenus et opacité de numéros restent hors mesure de recette.','Lecture humaine non réalisée.']}
try:
    with sync_playwright() as p:
        b=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox']);page=b.new_page(viewport={'width':390,'height':844});page.goto(f'http://127.0.0.1:{s.server_port}/index.html');page.evaluate('document.fonts.ready');out['fonts']=page.evaluate('({manrope:document.fonts.check("14px Manrope"),instrument:document.fonts.check("59px Instrument"),main_count:document.querySelectorAll("main").length,main_sections:document.querySelector("main").querySelectorAll("section").length})');page.locator('#primary-action').focus();page.keyboard.press('Enter');page.locator('#amount').fill('abc');page.locator('.form-submit').click();(R/'accessible-dialog.txt').write_text(page.locator('#demo').aria_snapshot());page.screenshot(path=str(R/'focus-error-390.png'));out['error_focus']=page.evaluate('({id:document.activeElement.id,outline:getComputedStyle(document.activeElement).outlineColor,rect:document.activeElement.getBoundingClientRect().toJSON()})');page.keyboard.press('Escape');page.locator('[data-step="1"]').focus();page.locator('[data-step="1"]').scroll_into_view_if_needed();page.evaluate('window.scrollBy({top:-80,behavior:"instant"})');page.locator('[data-step="1"]').focus();page.keyboard.press('Tab');page.keyboard.press('Shift+Tab');page.screenshot(path=str(R/'focus-journey-390.png'));out['dark_focus']=page.locator('[data-step="1"]').evaluate('(e)=>({outline:getComputedStyle(e).outlineColor,outline_width:getComputedStyle(e).outlineWidth,outline_style:getComputedStyle(e).outlineStyle,active:e===document.activeElement})');b.close()
finally:s.shutdown();s.server_close();(R/'supplementary-checks.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
print(json.dumps(out,ensure_ascii=False,indent=2))
