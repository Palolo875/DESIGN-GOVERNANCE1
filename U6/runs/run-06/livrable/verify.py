from pathlib import Path
import json, tempfile, time, threading, functools, sys
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright
root=Path('/workspace/remesure-phase5/runs/run-06/livrable'); (root/'captures').mkdir(exist_ok=True); (root/'browser-temp').mkdir(exist_ok=True); tempfile.tempdir=str(root/'browser-temp')
handler=functools.partial(SimpleHTTPRequestHandler,directory=str(root))
server=ThreadingHTTPServer(("127.0.0.1",0),handler)
threading.Thread(target=server.serve_forever,daemon=True).start()
base="http://127.0.0.1:"+str(server.server_port)+"/"
phase=sys.argv[1] if len(sys.argv)>1 else 'initial'
results=[];errors=[];requests=[]
def record(name, selectors, actions, fn):
    try:
        obs=fn(); results.append(dict(name=name,selectors=selectors,actions=actions,observations=obs,result='PASS'))
    except Exception as e:results.append(dict(name=name,selectors=selectors,actions=actions,observations=str(e),result='FAIL'))
with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'],env={'TMPDIR':str(root/'browser-temp')})
    page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
    page.on('pageerror',lambda e: errors.append(str(e))); page.on('request',lambda r:requests.append(r.url))
    page.goto(base+'typographie.html');page.evaluate('document.fonts.ready');page.screenshot(path=str(root/'captures/typographie.png'),full_page=True)
    page.goto(base+'index.html');page.evaluate('document.fonts.ready');page.screenshot(path=str(root/f'captures/desktop-{phase}.png'),full_page=True);page.screenshot(path=str(root/f'captures/desktop-{phase}-viewport.png'))
    page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(root/f'captures/mobile-{phase}.png'),full_page=True);page.screenshot(path=str(root/f'captures/mobile-{phase}-viewport.png'))
    def widths():
        out=[]
        for w in [1440,390,320]:
            page.set_viewport_size({'width':w,'height':1000 if w==1440 else 844}); o=page.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth})');assert o['scroll']<=w and o['body']<=w,o;out.append(o)
        return out
    record('Absence de débordement nominal', ['html','body'], ['Mesurer scrollWidth à 1440, 390 et 320 px'],widths)
    page.set_viewport_size({'width':1440,'height':1000})
    def keyboard():
        page.goto(base+'index.html'); page.keyboard.press('Tab');assert page.locator('.skip').evaluate('(e)=>e===document.activeElement'); page.keyboard.press('Enter'); page.keyboard.press('Tab');
        stops=[]
        for _ in range(17):
            o=page.evaluate('({tag:document.activeElement.tagName,id:document.activeElement.id,text:(document.activeElement.innerText||document.activeElement.value||document.activeElement.getAttribute("aria-label")||"").slice(0,90),outline:getComputedStyle(document.activeElement).outlineStyle,rect:document.activeElement.getBoundingClientRect().toJSON()})');stops.append(o);page.keyboard.press('Tab')
        page.locator('input[name=service]').first.focus();page.keyboard.press('ArrowDown');assert page.locator('input[value="Freins ou vitesses"]').is_checked();page.keyboard.press('Tab');assert page.locator('#to-slots').evaluate('(e)=>e===document.activeElement');page.keyboard.press('Enter');assert page.locator('#step-2').is_visible();assert page.locator('#slots-title').evaluate('(e)=>e===document.activeElement');page.screenshot(path=str(root/f'captures/focus-desktop-{phase}.png'))
        return {'tab_stops':stops,'radio_arrow_selection':'Freins ou vitesses','next_step':'step-2','focus':'slots-title'}
    record('Clavier : lien évitement, tabulation, radios et action', ['.skip','input[name=service]','#to-slots','#slots-title'], ['Tab puis Enter sur le lien d’évitement','17 tabulations relevées','ArrowDown sur le groupe besoin','Tab puis Enter vers le créneau'],keyboard)
    def slots():
        page.locator('#to-contact').click();assert page.locator('#slot-error').inner_text()=='Sélectionnez une heure pour continuer.';assert page.locator('input[name=time]').first.evaluate('(e)=>e===document.activeElement');assert page.locator('input[name=time][value="14:00"]').is_disabled();page.locator('input[name=date][value="Jeudi 15 octobre"]').check();assert 'Aucun créneau' in page.locator('#time-options').inner_text();page.locator('#to-contact').click();assert page.locator('#slot-error').inner_text()=='Choisissez un autre jour pour continuer.';page.screenshot(path=str(root/f'captures/indisponible-desktop-{phase}.png'));page.locator('input[name=date][value="Mercredi 14 octobre"]').check();page.locator('input[name=time][value="15:00"]').check();page.locator('#to-contact').click();assert page.locator('#step-3').is_visible();return {'empty_error':'Sélectionnez une heure pour continuer.','disabled':'14:00 mardi','empty_day':'Jeudi 15 octobre','recovery':'Mercredi 14 octobre 15:00 → step-3'}
    record('Créneaux : erreur, indisponible, jour vide et reprise', ['#to-contact','#slot-error','input[name=date]','input[name=time]','#time-options'], ['Continuer sans heure','Vérifier radio indisponible','Choisir jeudi puis continuer','Choisir mercredi 15:00 puis continuer'],slots)
    def contact():
        page.locator('#step-3 button[type=submit]').click();assert page.locator('#name-error').inner_text();assert page.locator('#email-error').inner_text();assert page.locator('#name').evaluate('(e)=>e===document.activeElement');page.locator('#name').fill('Camille Martin');page.locator('#email').fill('adresse-invalide');page.locator('#step-3 button[type=submit]').click();assert 'Vérifiez' in page.locator('#email-error').inner_text();assert page.locator('#email').evaluate('(e)=>e===document.activeElement');page.screenshot(path=str(root/f'captures/erreur-desktop-{phase}.png'));page.locator('#email').fill('camille@example.com');page.locator('#note').fill('Le frein arrière fait du bruit.');page.locator('#step-3 [data-back]').click();assert page.locator('input[name=time][value="15:00"]').is_checked();page.locator('#to-contact').click();assert page.locator('#name').input_value()=='Camille Martin';assert page.locator('#email').input_value()=='camille@example.com';page.locator('#step-3 button[type=submit]').click();assert page.locator('#step-4').is_visible();assert page.locator('.progress').is_hidden();text=page.locator('#final-summary').inner_text();assert 'Camille Martin' in text and '15:00' in text and 'Freins ou vitesses' in text;assert page.locator('#success-title').evaluate('(e)=>e===document.activeElement');page.screenshot(path=str(root/f'captures/recapitulatif-desktop-{phase}.png'));return {'empty_fields':'Erreurs présentes sur nom et e-mail ; focus nom','invalid_email':'Erreur e-mail ; focus e-mail','back':'Créneau, nom et e-mail conservés','summary':text,'focus':'success-title','notice':page.locator('.success-note').inner_text()}
    record('Coordonnées : erreurs, correction, retour et récapitulatif local', ['#name','#email','#name-error','#email-error','#step-3 [data-back]','#final-summary','#success-title'], ['Soumettre vide','Saisir nom et e-mail invalide puis soumettre','Corriger e-mail','Revenir au créneau puis poursuivre','Soumettre avec coordonnées d’exemple'],contact)
    def restart():
        page.locator('#restart').click();assert page.locator('#step-1').is_visible();assert page.locator('#name').input_value()=='';assert page.locator('#email').input_value()=='';assert page.locator('#final-summary').inner_text()=='';assert page.locator('input[value="Révision générale"]').is_checked();return {'step':1,'name':'','email':'','summary':'','service':'Révision générale'}
    record('Nouvelle simulation : effacement et retour initial', ['#restart','#name','#email','#final-summary'], ['Cliquer nouvelle simulation','Observer champs et récapitulatif'],restart)
    def mobile():
        page.set_viewport_size({'width':390,'height':844});page.locator('[data-service="Roue ou crevaison"]').click();assert page.locator('input[value="Roue ou crevaison"]').is_checked();page.locator('#to-slots').click();rect=page.locator('#slots-title').bounding_box();assert 0<=rect['y']<844,rect;page.locator('input[name=time][value="09:00"]').check();page.locator('#to-contact').click();page.locator('#name').fill('Alex Exemple');page.locator('#email').fill('alex@example.com');page.locator('#step-3 button[type=submit]').click();assert page.locator('#step-4').is_visible();assert page.locator('.progress').is_hidden();assert 'Roue ou crevaison' in page.locator('#final-summary').inner_text();page.locator('#rendez-vous').scroll_into_view_if_needed();page.screenshot(path=str(root/f'captures/recapitulatif-mobile-{phase}.png'));page.set_viewport_size({'width':320,'height':844});assert page.evaluate('document.documentElement.scrollWidth')==320;return {'entry':'Choisir une réparation de roue ou crevaison depuis la liste','date':'Mardi 13 octobre 09:00','summary':page.locator('#final-summary').inner_text(),'width320':page.evaluate('document.documentElement.scrollWidth')}
    record('Parcours mobile depuis une intervention et résultat à 320 px', ['[data-service="Roue ou crevaison"]','#to-slots','input[name=time]','#name','#email','#final-summary'], ['Cliquer intervention','Choisir mardi 09:00','Saisir coordonnées fictives','Afficher récapitulatif','Mesurer 320 px'],mobile)
    def privacy():
        page.locator('#privacy-toggle').click();assert page.locator('#privacy').is_visible();assert page.locator('#privacy-toggle').get_attribute('aria-expanded')=='true';page.locator('#privacy-toggle').click();assert page.locator('#privacy').is_hidden();return {'opened':True,'closed':True,'localStorage':page.evaluate('localStorage.length'),'sessionStorage':page.evaluate('sessionStorage.length')}
    record('Information sur les données et absence de stockage', ['#privacy-toggle','#privacy'], ['Ouvrir et fermer l’aide','Inspecter localStorage et sessionStorage'],privacy)
    page.set_viewport_size({'width':390,'height':844});page.locator('#restart').click();page.evaluate('scrollTo(0,0)')
    def network():
        external=[u for u in requests if u.startswith('http') and not u.startswith(base)];assert not external,external;assert not errors,errors;return {'external_http_requests':external,'page_errors':errors,'total_requests':len(requests)}
    record('Autonomie et JavaScript', ['document'], ['Relever les requests et pageerror sur tous les parcours'],network)
    browser.close()
server.shutdown();server.server_close()
(root/'functional-tests.json').write_text(json.dumps({'runtime':'Python Playwright 1.56.0 / Chromium / serveur local 127.0.0.1 à port éphémère','observed_at':datetime.now(timezone.utc).isoformat(),'artifact':'index.html','version':phase,'tests':results,'limits':['Parcours par le producteur, sans participant ni technologie d’assistance.','Aucun serveur ni réservation réelle.']},ensure_ascii=False,indent=2))
print(json.dumps([{'name':r['name'],'result':r['result'],'error':r['observations'] if r['result']=='FAIL' else None} for r in results],ensure_ascii=False,indent=2))
