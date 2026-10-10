from pathlib import Path
import json, threading, functools, http.server, datetime, hashlib
from playwright.sync_api import sync_playwright

root=Path(__file__).parent
capture=root/'captures/final-v4'
capture.mkdir(exist_ok=True)
results=[]
def record(name, actions, observations, passed):
 results.append({'name':name,'actions':actions,'observations':observations,'result':'PASS' if passed else 'FAIL'})
class QuietHandler(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(QuietHandler,directory=str(root)))
threading.Thread(target=server.serve_forever,daemon=True).start()
base=f'http://127.0.0.1:{server.server_port}/index.html'
errors=[];requests=[]
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1440,'height':1000})
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.on('request',lambda r:requests.append(r.url))
  page.goto(base);page.evaluate('document.fonts.ready')
  page.screenshot(path=str(capture/'desktop-initial.png'),full_page=True)
  page.screenshot(path=str(capture/'desktop-viewport.png'))
  page.add_style_tag(content='@media(min-width:761px){h1{font-size:88px;letter-spacing:-4.5px}}')
  page.screenshot(path=str(capture/'desktop-reduced-title.png'),full_page=True)
  page.reload();page.evaluate('document.fonts.ready')
  page.set_viewport_size({'width':390,'height':844})
  page.screenshot(path=str(capture/'mobile-initial.png'),full_page=True)
  page.screenshot(path=str(capture/'mobile-viewport.png'))
  page.locator('#primary-cta').click()
  focused=page.evaluate('document.activeElement.id')
  y=page.locator('#rendez-vous').bounding_box()['y']
  record('Action principale mobile',[{'selector':'#primary-cta','action':'click'}],{'focused':focused,'booking_y':y},focused=='booking-title' and y<844)
  page.locator('#continue').click()
  timeerror=page.locator('#time-error').is_visible();focused=page.evaluate('document.activeElement.id')
  page.screenshot(path=str(capture/'mobile-time-error.png'),full_page=True)
  record('Erreur de créneau',[{'selector':'#continue','action':'click without selected time'}],{'error_visible':timeerror,'focus':focused},timeerror and focused=='time-0900')
  page.locator('label[for="time-1130"]').click()
  page.locator('label[for="day-wed"]').click()
  cleared=page.locator('input[name="time"]:checked').count()==0
  record('Changement de date',[{'selector':'label[for="time-1130"]','action':'click'},{'selector':'label[for="day-wed"]','action':'click'}],{'time_reset':cleared,'disabled_time':page.locator('#time-1400').is_disabled()},cleared and page.locator('#time-1400').is_disabled())
  page.locator('label[for="time-1630"]').click()
  page.locator('label[for="service-check"]').click()
  page.locator('#continue').click()
  text=page.locator('#selection-summary').inner_text()
  record('Choix vers coordonnées',[{'selector':'label[for="time-1630"]','action':'click'},{'selector':'label[for="service-check"]','action':'click'},{'selector':'#continue','action':'click'}],{'summary':text,'focus':page.evaluate('document.activeElement.id')},'Une révision' in text and '14 octobre' in text and '16:30' in text and page.locator('#stage-two').is_visible())
  page.locator('#prepare').click()
  record('Coordonnées obligatoires',[{'selector':'#prepare','action':'click with empty fields'}],{'name_error':page.locator('#name-error').is_visible(),'email_error':page.locator('#email-error').is_visible(),'focus':page.evaluate('document.activeElement.id')},page.locator('#name-error').is_visible() and page.locator('#email-error').is_visible() and page.evaluate('document.activeElement.id')=='customer-name')
  page.locator('#customer-name').fill('Camille Exemple')
  page.locator('#customer-email').fill('adresse-invalide')
  page.locator('#prepare').click()
  page.screenshot(path=str(capture/'mobile-email-error.png'),full_page=True)
  record('E-mail invalide',[{'selector':'#customer-name','action':'fill Camille Exemple'},{'selector':'#customer-email','action':'fill adresse-invalide'},{'selector':'#prepare','action':'click'}],{'email_error':page.locator('#email-error').is_visible(),'name_preserved':page.locator('#customer-name').input_value(),'focus':page.evaluate('document.activeElement.id')},page.locator('#email-error').is_visible() and page.locator('#customer-name').input_value()=='Camille Exemple' and page.evaluate('document.activeElement.id')=='customer-email')
  page.locator('#customer-email').fill('camille@example.com')
  page.locator('#bike-notes').fill('Le frein arrière frotte après quelques kilomètres.')
  page.locator('#back').click();page.locator('#continue').click()
  preserved=page.locator('#customer-name').input_value()=='Camille Exemple' and page.locator('#customer-email').input_value()=='camille@example.com'
  record('Retour sans perte',[{'selector':'#back','action':'click'},{'selector':'#continue','action':'click'}],{'contact_preserved':preserved,'notes':page.locator('#bike-notes').input_value()},preserved)
  page.locator('#prepare').click()
  success=page.locator('#success').is_visible();text=page.locator('#success').inner_text()
  page.screenshot(path=str(capture/'mobile-success.png'),full_page=True)
  record('Récapitulatif local',[{'selector':'#prepare','action':'click with valid sample fields'}],{'success':success,'text':text,'focus':page.evaluate('document.activeElement.id'),'storage_count':page.evaluate('localStorage.length + sessionStorage.length')},success and 'Aucune réservation' in text and '16:30' in text and 'Camille Exemple' in text and page.evaluate('document.activeElement.id')=='success-title')
  page.locator('#restart').click()
  record('Recommencer',[{'selector':'#restart','action':'click'}],{'stage_one_visible':page.locator('#stage-one').is_visible(),'name':page.locator('#customer-name').input_value(),'selected_time_count':page.locator('input[name="time"]:checked').count()},page.locator('#stage-one').is_visible() and page.locator('#customer-name').input_value()=='' and page.locator('input[name="time"]:checked').count()==0)
  # Native keyboard journey: Tab, radio arrows, Space, Enter.
  page.reload();page.set_viewport_size({'width':1440,'height':1000});page.evaluate('document.fonts.ready')
  page.keyboard.press('Tab')
  skip_visible=page.locator('.skip').evaluate('(e)=>getComputedStyle(e).clipPath')
  page.keyboard.press('Enter')
  main_focus=page.evaluate('document.activeElement.id')
  record('Lien d’évitement',[{'selector':'.skip','action':'Tab from fresh page, then Enter'}],{'focused_clip':skip_visible,'main_focus':main_focus},skip_visible=='none' and main_focus=='main')
  page.reload()
  stops=[]
  for i in range(10):
   page.keyboard.press('Tab')
   stops.append(page.evaluate('({tag:document.activeElement.tagName,id:document.activeElement.id,text:document.activeElement.textContent.trim().slice(0,65),outline:getComputedStyle(document.activeElement).outlineWidth})'))
  page.locator('#service-repair').focus();page.keyboard.press('ArrowRight')
  service=page.locator('#service-check').is_checked()
  page.keyboard.press('Tab');dayfocus=page.evaluate('document.activeElement.id')
  page.keyboard.press('ArrowRight');day=page.locator('#day-wed').is_checked()
  page.keyboard.press('Tab');timefocus=page.evaluate('document.activeElement.id')
  page.keyboard.press('Space');page.keyboard.press('Tab');continuefocus=page.evaluate('document.activeElement.id')
  page.keyboard.press('Enter')
  page.locator('#customer-name').fill('Alex Exemple');page.keyboard.press('Tab');page.keyboard.type('alex@example.com');page.keyboard.press('Tab');page.keyboard.type('Vélo de ville');page.keyboard.press('Tab');page.keyboard.press('Enter')
  key_success=page.locator('#success').is_visible()
  record('Parcours clavier',[{'selector':'document','action':'Tab ×10; observations focus'},{'selector':'#service-repair','action':'focus then ArrowRight, Tab, ArrowRight, Tab, Space, Tab, Enter'},{'selector':'#customer-name','action':'fill then Tab/type email, Tab/type note, Tab/Enter'}],{'initial_stops':stops,'service_selected_by_arrow':service,'day_focus':dayfocus,'day_selected_by_arrow':day,'time_focus':timefocus,'continue_focus':continuefocus,'success':key_success},service and day and timefocus=='time-0900' and continuefocus=='continue' and key_success)
  page.screenshot(path=str(capture/'desktop-success.png'),full_page=True)
  page.reload();page.set_viewport_size({'width':320,'height':844})
  overflow=page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})')
  page.screenshot(path=str(capture/'mobile-320.png'),full_page=True)
  record('Reflow 320px',[{'selector':'viewport','action':'resize to 320×844'}],overflow,overflow['scroll']<=overflow['viewport'])
  page.locator('label[for="time-0900"]').click();page.locator('#continue').click()
  page.locator('#customer-name').fill('X'*100);page.locator('#customer-email').fill('long@example.com');page.locator('#bike-notes').fill('X'*500);page.locator('#prepare').click()
  longoverflow=page.evaluate('document.documentElement.scrollWidth<=innerWidth')
  page.screenshot(path=str(capture/'mobile-long-content.png'),full_page=True)
  record('Contenu long 320px',[{'selector':'#customer-name','action':'fill 100 letters'},{'selector':'#bike-notes','action':'fill 500 letters'},{'selector':'#customer-email','action':'fill long@example.com'},{'selector':'#prepare','action':'click'}],{'success':page.locator('#success').is_visible(),'no_overflow':longoverflow},page.locator('#success').is_visible() and longoverflow)
  page.emulate_media(reduced_motion='reduce')
  behavior=page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')
  record('Mouvement réduit',[{'selector':'media','action':'prefers-reduced-motion reduce'}],{'scroll_behavior':behavior},behavior=='auto')
  page.set_viewport_size({'width':390,'height':844});page.reload();page.evaluate('document.fonts.ready')
  # Visible label hit areas, excluding prose links and native hidden radios.
  sizes=page.locator('.choice label,button,.nav-cta,.btn').evaluate_all('(els)=>els.filter(e=>e.getClientRects().length).map(e=>({text:e.textContent.trim(),width:e.getBoundingClientRect().width,height:e.getBoundingClientRect().height}))')
  record('Cibles mobiles',[{'selector':'.choice label,button,.nav-cta,.btn','action':'measure visible rectangles at 390px'}],{'sizes':sizes},all(s['width']>=24 and s['height']>=24 for s in sizes))
  noexternal=all(u.startswith('http://127.0.0.1:') or u.startswith('data:') for u in requests)
  record('Runtime et requêtes',[{'selector':'page','action':'collect pageerror and network requests through all journeys'}],{'page_errors':errors,'external_requests':[u for u in requests if not u.startswith('http://127.0.0.1:') and not u.startswith('data:')]},not errors and noexternal)
  browser.close()
finally:
 server.shutdown();server.server_close()

def lum(h):
 c=[int(h[i:i+2],16)/255 for i in (1,3,5)]
 c=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in c]
 return sum(x*y for x,y in zip(c,[.2126,.7152,.0722]))
pairs=[('Texte/papier','#192b28','#f3f2e9'),('Texte/carnet','#192b28','#deef64'),('Secondaire/papier','#53645d','#f3f2e9'),('Erreur/carnet','#86251d','#deef64'),('Footer','#c4cbbb','#192b28'),('Texte aide/carnet','#344324','#deef64'),('Indisponible/carnet','#566135','#deef64'),('Texte/champ','#192b28','#f8f9dc'),('Texte/récap','#192b28','#eff6ac'),('Frontière/champ','#60702d','#f8f9dc'),('Frontière/carnet','#60702d','#deef64'),('Frontière/papier','#71807a','#f3f2e9')]
contrast=[]
for role,a,b in pairs:
 l1,l2=sorted([lum(a),lum(b)],reverse=True);ratio=(l1+.05)/(l2+.05);threshold=3 if role.startswith('Frontière') else 4.5
 contrast.append({'role':role,'foreground':a,'background':b,'ratio':round(ratio,2),'threshold':threshold,'result':'PASS' if ratio>=threshold else 'FAIL'})
(root/'contrast.json').write_text(json.dumps(contrast,ensure_ascii=False,indent=2))
doc={'artifact':'index.html','sha256':hashlib.sha256((root/'index.html').read_bytes()).hexdigest(),'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime':'Chromium / Python Playwright 1.56.0','server':'ephemeral loopback; shut down after execution','tests':results,'limitations':['No screen reader or real user task test','No real availability, booking service, persistence or email sending','Theoretical solid-color contrast pairs; no automated full WCAG audit']}
(root/'functional-tests.json').write_text(json.dumps(doc,ensure_ascii=False,indent=2))
print(json.dumps({'tests':len(results),'passed':sum(x['result']=='PASS' for x in results),'failed':[x['name'] for x in results if x['result']=='FAIL'],'contrast_failed':[x['role'] for x in contrast if x['result']=='FAIL']},ensure_ascii=False))
