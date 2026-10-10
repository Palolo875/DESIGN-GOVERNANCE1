from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
import json, datetime, hashlib
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parent
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT)))
Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
results={'artifact':'index.html','sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(),'observed_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'runtime':'Chromium / Python Playwright 1.56.0','journeys':[],'limits':['Auteur seul ; pas de participant ni de lecteur d’écran.','Aucun compte, envoi, paiement ou conformité fiscale testé.']}
def record(name,selectors,actions,observations,ok):
    results['journeys'].append({'name':name,'selectors':selectors,'actions':actions,'observations':observations,'result':'PASS' if ok else 'FAIL'})
try:
    with sync_playwright() as pw:
        browser=pw.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
        errors=[];external=[]
        page.on('pageerror',lambda e:errors.append(str(e)))
        page.on('request',lambda r:external.append(r.url) if not r.url.startswith(('http://127.0.0.1:','data:','blob:')) else None)
        page.goto(url);page.evaluate('document.fonts.ready');page.screenshot(path=str(ROOT/'desktop.png'));page.screenshot(path=str(ROOT/'desktop-full.png'),full_page=True)
        widths=[]
        for w,h in [(390,844),(320,844),(768,1000)]:
            page.set_viewport_size({'width':w,'height':h});page.evaluate('window.scrollTo(0,0)')
            if w==390:
                page.screenshot(path=str(ROOT/'mobile.png'));page.screenshot(path=str(ROOT/'mobile-full.png'),full_page=True)
            dims=page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})');widths.append(dims)
        record('Responsive nominal',['html','body'],['Rendu 1440×1000 et captures','Rendu 390×844 et captures','Mesure à 320px et 768px'],{'widths':widths},all(x['viewport']==x['scroll'] for x in widths))
        page.set_viewport_size({'width':1440,'height':1000});page.evaluate('window.scrollTo(0,0)')
        style=page.add_style_tag(content='h1{font-family:Manrope,Arial,sans-serif;font-size:74px;font-weight:600;letter-spacing:-.06em}@media(max-width:700px){h1{font-size:49px}}')
        page.screenshot(path=str(ROOT/'type-alternative-desktop.png'))
        page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(ROOT/'type-alternative-mobile.png'))
        style.evaluate('(e)=>e.remove()')
        page.set_viewport_size({'width':1440,'height':1000});page.locator('#primary-action').click()
        record('Action principale',['#primary-action','#demo','#client'],['Clic sur Composer une facture'],{'dialog_open':page.locator('#demo').evaluate('(e)=>e.open'),'focus':page.evaluate('document.activeElement.id')},page.locator('#demo').evaluate('(e)=>e.open') and page.evaluate('document.activeElement.id')=='client')
        page.locator('#client').fill('');page.locator('#service').fill('');page.locator('#amount').fill('-12');page.locator('.form-submit').click()
        obs={'summary':page.locator('#errors').inner_text(),'invalid':page.locator('[aria-invalid="true"]').count(),'focus':page.evaluate('document.activeElement.id'),'amount_preserved':page.locator('#amount').input_value()}
        page.screenshot(path=str(ROOT/'error-desktop.png'))
        record('Erreurs et saisie conservée',['#client','#service','#amount','.form-submit','#errors'],['Vider client et prestation','Saisir -12 €','Soumettre'],obs,obs['invalid']==3 and obs['focus']=='client' and obs['amount_preserved']=='-12')
        page.locator('#client').fill('La Maison des projets et des métiers créatifs — exemple de client au nom long');page.locator('#service').fill('Accompagnement éditorial, conception et production de supports pour une activité indépendante');page.locator('#amount').fill('1234,56');page.locator('#tax').select_option('20');page.locator('.form-submit').click()
        obs={'success':page.locator('#success').is_visible(),'total':page.locator('#success-total').inner_text(),'preview_total':page.locator('#invoice-total').inner_text(),'tax':page.locator('#invoice-tax').inner_text(),'focus':page.evaluate('document.activeElement.id')}
        record('Correction et calcul avec décimales',['#client','#service','#amount','#tax','.form-submit','#success','#invoice-total'],['Corriger avec un contenu long','Saisir 1234,56 € HT à 20 %','Soumettre'],obs,obs['success'] and '1' in obs['total'] and '481,47' in obs['total'] and '246,91' in obs['tax'] and obs['total']==obs['preview_total'] and obs['focus']=='success-title')
        with page.expect_download() as dl:
            page.locator('#download').click()
        download=dl.value;download.save_as(str(ROOT/'download-observed.txt'));txt=(ROOT/'download-observed.txt').read_text()
        record('Téléchargement local',['#download'],['Télécharger le récapitulatif texte','Lire le fichier obtenu'],{'filename':download.suggested_filename,'contains_disclaimer':'SANS VALEUR COMPTABLE' in txt,'contains_total':'481,47' in txt},'SANS VALEUR COMPTABLE' in txt and '481,47' in txt)
        page.locator('#edit').click();obs={'client':page.locator('#client').input_value(),'amount':page.locator('#amount').input_value(),'focus':page.evaluate('document.activeElement.id')}
        record('Retour à la modification',['#edit','#client','#amount'],['Cliquer Modifier'],obs,'La Maison' in obs['client'] and obs['amount']=='1234,56' and obs['focus']=='client')
        page.keyboard.press('Escape');obs={'closed':not page.locator('#demo').evaluate('(e)=>e.open'),'focus':page.evaluate('document.activeElement.id')}
        record('Escape et restitution du focus',['#demo','#primary-action'],['Appuyer sur Escape'],obs,obs['closed'] and obs['focus']=='primary-action')
        page.screenshot(path=str(ROOT/'long-desktop.png'))
        page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(ROOT/'long-mobile.png'),full_page=True);page.locator('.invoice').screenshot(path=str(ROOT/'long-invoice-detail.png'))
        page.set_viewport_size({'width':320,'height':844});longdims=page.evaluate('({viewport:innerWidth,scroll:document.documentElement.scrollWidth})')
        record('Contenu long à 320px',['#invoice-client','#invoice-service','#status-document'],['Inspecter la page après données longues à 320px'],longdims,longdims['viewport']==longdims['scroll'])
        page.locator('#primary-action').click();page.locator('#amount').fill('abc');page.locator('.form-submit').click();page.screenshot(path=str(ROOT/'error-mobile.png'))
        dialogdims=page.locator('#demo').evaluate('(e)=>({width:e.clientWidth,scroll:e.scrollWidth,left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right})')
        record('Erreur mobile dans le dialog',['#demo','#amount','.form-submit'],['Ouvrir à 320px','Saisir abc','Soumettre'],{'dialog':dialogdims,'error':page.locator('#amount-error').inner_text()},dialogdims['width']==dialogdims['scroll'] and page.locator('#amount').get_attribute('aria-invalid')=='true')
        page.keyboard.press('Escape');page.set_viewport_size({'width':1440,'height':1000});page.reload();page.evaluate('document.fonts.ready')
        page.locator('#primary-action').focus();page.keyboard.press('Enter');stops=[]
        for _ in range(8):
            stops.append(page.evaluate('({id:document.activeElement.id,tag:document.activeElement.tagName,outline:getComputedStyle(document.activeElement).outlineStyle,width:getComputedStyle(document.activeElement).outlineWidth})'))
            page.keyboard.press('Tab')
        page.keyboard.press('Shift+Tab');lastfocus=page.evaluate('document.activeElement.id');page.keyboard.press('Escape')
        record('Dialog au clavier',['#primary-action','#client','#service','#amount','#tax','.form-submit','#close-demo'],['Focus du CTA puis Enter','8 Tab dans le dialog','Shift+Tab','Escape'],{'stops':stops,'shift_tab_focus':lastfocus,'returned_focus':page.evaluate('document.activeElement.id')},set(s['id'] for s in stops).issuperset({'client','service','amount','tax','close-demo'}) and page.evaluate('document.activeElement.id')=='primary-action' and all(s['outline']=='solid' and s['width']=='3px' for s in stops if s['tag'] in ['INPUT','SELECT','BUTTON']))
        page.locator('[data-step="1"]').click();s1=page.locator('#status-pill').inner_text();page.locator('[data-step="2"]').click();s2=page.locator('#status-pill').inner_text()
        record('États de parcours',['[data-step="1"]','[data-step="2"]','#status-pill'],['Cliquer Suivre puis Retrouver'],{'states':[s1,s2],'pressed':page.locator('[aria-pressed="true"]').count()},s1=='À régler' and s2=='Réglée' and page.locator('[aria-pressed="true"]').count()==1)
        summaries=page.locator('summary');summaries.nth(0).focus();page.keyboard.press('Enter');opened=page.locator('details').nth(0).get_attribute('open') is not None
        record('FAQ clavier',['summary','details'],['Focus première question','Enter'],{'opened':opened},opened)
        page.emulate_media(reduced_motion='reduce');scroll=page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')
        record('Mouvement réduit',['html'],['Activer prefers-reduced-motion: reduce'],{'scroll_behavior':scroll},scroll=='auto')
        record('Isolation réseau et erreurs JS',['document'],['Observer les requêtes et erreurs pendant tous les parcours'],{'external_requests':external,'javascript_errors':errors},not external and not errors)
        browser.close()
finally:
    server.shutdown();server.server_close()
    (ROOT/'functional-tests.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
print(json.dumps(results,ensure_ascii=False,indent=2))
