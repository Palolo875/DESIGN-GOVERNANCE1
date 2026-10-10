from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from threading import Thread
from datetime import datetime,timezone
import json
from playwright.sync_api import sync_playwright
root=Path(__file__).parent
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':390,'height':844});page.goto(f'http://127.0.0.1:{server.server_port}/index.html')
 page.wait_for_function('document.fonts.status==="loaded"')
 snapshot=page.locator('body').aria_snapshot();(root/'accessibility-snapshot.txt').write_text(snapshot)
 assert page.get_by_role('button',name='Composer une facture',exact=True).count()==2
 page.get_by_role('button',name='Composer une facture',exact=True).first.click()
 assert page.get_by_role('dialog',name='Votre facture d’exemple').is_visible()
 names=[]
 for role,name in [('textbox','Nom du client'),('textbox','Prestation'),('spinbutton','Heures'),('spinbutton','Prix / heure (€ HT)'),('combobox','TVA illustrative'),('button','Fermer l’éditeur'),('button','Annuler'),('button','Voir mon brouillon')]:
  assert page.get_by_role(role,name=name,exact=True).is_visible();names.append({'role':role,'name':name,'result':'OBSERVED'})
 computed=page.locator('#client').evaluate("e=>({color:getComputedStyle(e).color,background:getComputedStyle(e).backgroundColor,border:getComputedStyle(e).borderColor,outline:getComputedStyle(e).outline})")
 controls=page.locator('#editor input, #editor select, #editor button').evaluate_all('es=>es.map(e=>({id:e.id,width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))')
 page.screenshot(path=str(root/'captures-states'/'focus-nominal-390.png'))
 (root/'semantic-evidence.json').write_text(json.dumps({'observed_at':datetime.now(timezone.utc).isoformat(),'runtime':browser.version,'method':'Playwright accessible role/name selectors and Chromium aria_snapshot; no screen reader','names':names,'firstFieldComputedStyle':computed,'dialogControlSizes':controls},ensure_ascii=False,indent=2))
 browser.close()
server.shutdown();server.server_close()
print(json.dumps({'namedControls':len(names),'firstFieldComputedStyle':computed,'dialogControlSizes':controls},ensure_ascii=False))
