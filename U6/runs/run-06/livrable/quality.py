from pathlib import Path
from playwright.sync_api import sync_playwright
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import threading,functools,tempfile,json
r=Path('/workspace/remesure-phase5/runs/run-06/livrable');tempfile.tempdir=str(r/'browser-temp');server=ThreadingHTTPServer(('127.0.0.1',0),functools.partial(SimpleHTTPRequestHandler,directory=str(r)));threading.Thread(target=server.serve_forever,daemon=True).start();url=f'http://127.0.0.1:{server.server_port}/index.html'
data=json.loads((r/'functional-tests.json').read_text());tests=data['tests']
def record(name,selectors,actions,fn):
 try:tests.append(dict(name=name,selectors=selectors,actions=actions,observations=fn(),result='PASS'))
 except Exception as e:tests.append(dict(name=name,selectors=selectors,actions=actions,observations=str(e),result='FAIL'))
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':390,'height':844});page.goto(url)
 def keyboard():
  page.locator('input[name=service]').first.focus();page.keyboard.press('ArrowDown');page.keyboard.press('Tab');page.keyboard.press('Enter');page.keyboard.press('Tab');assert page.locator('input[name=date]').first.evaluate('(e)=>e===document.activeElement');page.keyboard.press('ArrowRight');page.keyboard.press('Tab');page.keyboard.press('ArrowRight');assert page.locator('input[name=time][value="15:00"]').is_checked();page.keyboard.press('Tab');page.keyboard.press('Enter');page.keyboard.press('Tab');assert page.locator('#name').evaluate('(e)=>e===document.activeElement');page.keyboard.type('Clavier Exemple');page.keyboard.press('Tab');page.keyboard.type('clavier@example.com');page.keyboard.press('Tab');page.keyboard.type('Besoin de regler le frein.');page.keyboard.press('Tab');page.screenshot(path=str(r/'captures/clavier-mobile-final.png'));page.keyboard.press('Enter');assert page.locator('#step-4').is_visible();assert page.locator('#success-title').evaluate('(e)=>e===document.activeElement');page.keyboard.press('Tab');assert page.locator('#restart').evaluate('(e)=>e===document.activeElement');page.keyboard.press('Enter');assert page.locator('#step-1').is_visible();return {'viewport':'390×844','service':'Freins ou vitesses','slot':'Mercredi 14 octobre 15:00','contact':'Clavier Exemple / clavier@example.com','result':'récapitulatif puis réinitialisation au clavier'}
 record('Parcours entier au clavier sur mobile', ['input[name=service]','input[name=date]','input[name=time]','#name','#email','#step-3 button[type=submit]','#restart'],['ArrowDown, Tab, Enter vers les dates','Tab, ArrowRight vers mercredi','Tab, ArrowRight vers 15:00','Tab, Enter puis saisie des champs par keyboard.type','Tab, Enter vers résultat puis réinitialisation'],keyboard)
 def extremes():
  page.goto(url);page.locator('#to-slots').click();page.locator('input[name=time]').first.check();page.locator('#to-contact').click();page.locator('#step-3 button[type=submit]').click();out=[]
  for w in [390,320]:
   page.set_viewport_size({'width':w,'height':844});page.screenshot(path=str(r/f'captures/erreur-mobile-{w}-final.png'),full_page=True);sw=page.evaluate('document.documentElement.scrollWidth');assert sw<=w;out.append({'state':'error','width':w,'scrollWidth':sw})
  page.locator('#name').fill('NomTrèsLong'*7);page.locator('#email').fill('adresse.longue@example.com');page.locator('#note').fill('x'*400);page.locator('#step-3 button[type=submit]').click();assert page.locator('#step-4').is_visible();assert page.evaluate('document.documentElement.scrollWidth')==320;assert len(page.locator('#final-summary dd').last.inner_text())==400;page.screenshot(path=str(r/'captures/contenu-long-320-final.png'),full_page=True);out.append({'state':'long summary','width':320,'scrollWidth':320,'note_length':400});return out
 record('Erreurs mobile et contenu long à 320 px', ['#step-3','#name','#email','#note','#final-summary','html'],['Soumettre vide','Capturer erreur à 390 et 320 px','Saisir nom long et note de 400 caractères','Afficher récapitulatif à 320 px'],extremes)
 def semantics():
  rows=page.locator('input,textarea').evaluate_all('(els)=>els.map(e=>({id:e.id,name:e.name,label:Array.from(e.labels||[]).map(l=>l.textContent.trim()).join(" / ")}))');assert all(x['label'] for x in rows);return rows
 record('Association explicite des champs et labels', ['input','textarea'], ['Inspecter HTMLInputElement.labels et HTMLTextAreaElement.labels sur tous les champs'],semantics)
 b.close()
server.shutdown();server.server_close()
def lum(c):
 vals=[int(c[i:i+2],16)/255 for i in (1,3,5)];lin=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in vals];return sum(x*y for x,y in zip(lin,[.2126,.7152,.0722]))
def contrast(a,b):
 x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)
combos=[('corps','#28251f','#f3eee4'),('secondaire','#635e54','#f3eee4'),('aide/placeholder','#635e54','#fffdf8'),('action','#fffdf8','#b83322'),('erreur','#a32319','#fffdf8'),('selection-secondaire','#635e54','#f9eee8'),('footer-secondaire','#dbd2c4','#28251f'),('footer-accent','#f4a390','#28251f'),('focus','#b83322','#fffdf8'),('bordure-input','#827b6e','#fffdf8')]
ratios=[dict(role=k,foreground=a,background=b,ratio=round(contrast(a,b),2),minimum=3 if k in ['focus','bordure-input'] else 4.5) for k,a,b in combos]
for row in ratios:assert row['ratio']>=row['minimum'],row
(r/'contrast.json').write_text(json.dumps({'method':'WCAG 2.2, luminance relative sRGB, couleurs opaques déclarées en CSS sur fonds unis','artifact':'index.html','version':'final','results':ratios,'limits':['Calcul de paires représentatives, pas scan complet des pixels.','Rendu natif des radios dépend du navigateur ; non mesuré pixel par pixel.']},ensure_ascii=False,indent=2))
(r/'functional-tests.json').write_text(json.dumps(data,ensure_ascii=False,indent=2));print(json.dumps([{'name':x['name'],'result':x['result'],'observation':x['observations'] if x['result']=='FAIL' else None} for x in tests[-3:]],ensure_ascii=False));print(ratios)
