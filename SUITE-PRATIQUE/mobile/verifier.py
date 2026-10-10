#!/usr/bin/env python3
"""Parcours exécutables, isolés, du prototype Web mobile ; pas un audit WCAG complet."""
import hashlib
import http.server
import json
import threading
import traceback
from datetime import datetime, timezone
from pathlib import Path
from functools import partial
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'preuves'
OUT.mkdir(exist_ok=True)

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass

def stripped(s):
    return ''.join(s.split()).replace('\u202f', '').replace('\xa0', '')

def expect_total(page, text):
    got = stripped(page.locator('#total').inner_text())
    assert got == stripped(text), (got, text)

def open_editor(page):
    page.locator('#edit').click()
    assert page.locator('#editor').evaluate('(n)=>n.open')

def fill(page, **values):
    for key, value in values.items():
        page.locator('#input-'+key).fill(value)

def apply(page):
    page.get_by_role('button', name='Appliquer au brouillon', exact=True).click()

def assert_closed(page):
    assert not page.locator('#editor').evaluate('(n)=>n.open')
    assert page.locator('#edit').evaluate('(n)=>n===document.activeElement')

def no_overflow(page):
    geometry = page.evaluate('''()=>({viewport:innerWidth,page:document.documentElement.scrollWidth,
        boxes:[...document.querySelectorAll('.document,.service-row,.mechanism,.total-final')].map(n=>({name:n.className,left:n.getBoundingClientRect().left,right:n.getBoundingClientRect().right,scroll:n.scrollWidth,width:n.clientWidth}))})''')
    assert geometry['page'] <= geometry['viewport']+1, geometry
    for b in geometry['boxes']:
        assert b['left'] >= -1 and b['right'] <= geometry['viewport']+1, b
        assert b['scroll'] <= b['width']+1, b
    return geometry

def nominal(page, width):
    expect_total(page, '720,00 €')
    assert page.locator('#quantity').inner_text() == '8 h'
    assert page.locator('#edit').is_visible()
    assert page.locator('#edit').is_enabled()
    geometry = no_overflow(page)
    page.screenshot(path=str(OUT/f'{width}-nominal.png'),full_page=True)
    page.screenshot(path=str(OUT/f'{width}-premiere.png'))
    return {'total':'720,00 €','geometry':geometry,'selectors':['#quantity','#total','#edit']}

def rapid(page, width):
    page.evaluate("()=>{for(let i=0;i<20;i++)document.querySelector('#plus').click();for(let i=0;i<2;i++)document.querySelector('#minus').click();}")
    expect_total(page, '1 530,00 €')
    assert page.locator('#quantity').inner_text() == '17 h'
    page.wait_for_timeout(260)
    expect_total(page, '1 530,00 €')
    assert page.evaluate('document.getAnimations().length') == 0
    return {'actions':'20 ajouts et 2 retraits sans attendre les animations','heures':17,'total':'1530,00 €','animations_finales':0}

def errors_recovery(page, width):
    open_editor(page)
    fill(page,client='',service='',quantity='-2',rate='abc',vat='101')
    apply(page)
    assert page.locator('[aria-invalid=true]').count() == 5
    assert page.locator('#input-rate').input_value() == 'abc'
    assert page.locator('#input-client').evaluate('(n)=>n===document.activeElement')
    expect_total(page,'720,00 €')
    if width in (320,390):page.screenshot(path=str(OUT/f'{width}-erreur.png'))
    fill(page,client='Studio de test',service='Une prestation modifiée',quantity='10,5',rate='80,25',vat='5,5')
    apply(page)
    assert_closed(page)
    expect_total(page,'888,97 €')
    assert stripped(page.locator('#subtotal').inner_text()) == stripped('842,63 €')
    assert stripped(page.locator('#tax').inner_text()) == stripped('46,34 €')
    if width == 390:page.screenshot(path=str(OUT/'390-apres-modification.png'),full_page=True)
    return {'erreurs_liees':5,'saisie_conservee':'abc','calcul':'10,5 × 80,25 => 842,63 HT ; TVA 5,5 % => 46,34 ; TTC 888,97','focus_retour':'#edit'}

def cancellation(page, width):
    open_editor(page)
    fill(page,client='Modification à annuler',quantity='25')
    page.locator('#close').click()
    assert_closed(page)
    expect_total(page,'720,00 €')
    open_editor(page)
    assert page.locator('#input-client').input_value() == 'Studio Horizon'
    assert page.locator('#input-quantity').input_value() == '8'
    page.keyboard.press('Escape')
    assert_closed(page)
    return {'modifications_annulees':True,'fermetures':['bouton','Escape'],'total':'720,00 €'}

def keyboard(page, width):
    open_editor(page)
    page.locator('#handle').focus()
    page.keyboard.press('Shift+Tab')
    assert page.get_by_role('button',name='Appliquer au brouillon',exact=True).evaluate('(n)=>n===document.activeElement')
    page.keyboard.press('Tab')
    assert page.locator('#handle').evaluate('(n)=>n===document.activeElement')
    page.keyboard.press('Escape')
    assert_closed(page)
    return {'boucle':['Shift+Tab premier vers dernier','Tab dernier vers premier'],'retour_focus':True}

def interrupted_open(page, width):
    page.evaluate("()=>{for(let i=0;i<8;i++){document.querySelector('#edit').click();document.querySelector('#close').click();}}")
    assert_closed(page)
    page.wait_for_timeout(350)
    assert_closed(page)
    assert page.evaluate('document.getAnimations().length') == 0
    expect_total(page,'720,00 €')
    return {'ouvertures_fermetures_rapides':8,'reouverture_tardive':False,'animations_finales':0}

def drag(page, width):
    open_editor(page)
    page.wait_for_timeout(280)
    box = page.locator('#handle').bounding_box()
    x,y = box['x']+box['width']/2,box['y']+box['height']/2
    page.mouse.move(x,y);page.mouse.down();page.mouse.move(x,y+38,steps=4);page.mouse.up()
    page.wait_for_timeout(220)
    assert page.locator('#editor').evaluate('(n)=>n.open')
    assert page.locator('#editor').evaluate("(n)=>n.style.transform==='' ")
    box=page.locator('#handle').bounding_box();x,y=box['x']+box['width']/2,box['y']+box['height']/2
    page.mouse.move(x,y);page.mouse.down();page.mouse.move(x,y+105,steps=5);page.mouse.up()
    assert_closed(page)
    return {'petit_glissement':'retour sans fermer','grand_glissement':'fermeture et focus restauré','scope':'pointeur Chromium, pas geste système natif'}

def pointer_cancel(page, width):
    open_editor(page);page.wait_for_timeout(280)
    page.locator('#handle').evaluate('(n)=>n.addEventListener("pointerdown",e=>window.testPointerId=e.pointerId,{once:true})')
    b=page.locator('#handle').bounding_box();x,y=b['x']+b['width']/2,b['y']+b['height']/2
    page.mouse.move(x,y);page.mouse.down();page.mouse.move(x,y+42,steps=3)
    pointer_id=page.evaluate('window.testPointerId')
    page.dispatch_event('#handle','pointercancel',{'pointerId':pointer_id,'isPrimary':True})
    page.mouse.move(2,2);page.mouse.up();page.wait_for_timeout(220)
    assert page.locator('#editor').evaluate('(n)=>n.open')
    assert page.locator('#editor').evaluate("(n)=>n.style.transform==='' ")
    expect_total(page,'720,00 €')
    return {'annulation':'pointercancel injecté après pointeur réel','panneau':'ouvert, position restaurée','donnée':'inchangée'}

def low_height(page, width):
    page.set_viewport_size({'width':width,'height':420})
    open_editor(page)
    apply_box=page.get_by_role('button',name='Appliquer au brouillon',exact=True).bounding_box()
    assert apply_box['y']>=0 and apply_box['y']+apply_box['height']<=421, apply_box
    fill(page,vat='0')
    apply(page)
    expect_total(page,'600,00 €')
    assert_closed(page)
    return {'hauteur':420,'action_visible':apply_box,'limite':'réduction de viewport, pas clavier logiciel physique'}

def long_and_boundary(page, width):
    open_editor(page)
    fill(page,client='Un client dont le nom est long '+('et précis '*10),service='Une prestation détaillée '+('sans rupture de compréhension '*6),quantity='1000',rate='100000',vat='100')
    apply(page)
    assert_closed(page)
    expect_total(page,'200 000 000,00 €')
    geometry=no_overflow(page)
    open_editor(page)
    apply(page)
    assert_closed(page)
    expect_total(page,'200 000 000,00 €')
    return {'valeurs_limites':'1000 h, 100000 €, 100 %','réouverture_sans_perte':True,'geometry':geometry}

def persisted(page, width):
    open_editor(page);fill(page,quantity='10,5',rate='80,25',vat='5,5');apply(page)
    page.reload();page.evaluate('document.fonts.ready')
    expect_total(page,'888,97 €')
    assert 'retrouvé' in page.locator('#status').inner_text()
    return {'rechargement':'brouillon retrouvé','total':'888,97 €','scope':'stockage du contexte de navigateur'}

def download(page, width):
    button=page.locator('#export-mobile' if width<701 else '#export-desktop')
    with page.expect_download() as event:button.click()
    target=OUT/f'{width}-brouillon.txt';event.value.save_as(str(target));body=target.read_text()
    assert 'sans valeur comptable' in body and '720,00' in body and 'Aucun envoi' in body
    return {'fichier':target.name,'limites_presentes':True,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}

def reduced(page, width):
    open_editor(page)
    assert page.evaluate('document.getAnimations().length') == 0
    fill(page,quantity='9');apply(page)
    expect_total(page,'810,00 €')
    assert page.evaluate('document.getAnimations().length') == 0
    return {'préférence':'reduce','calcul':'810,00 €','animations':0}

def reduce_during(page, width):
    page.evaluate("document.querySelector('#edit').click()")
    before=page.evaluate('document.getAnimations().length')
    assert before>0
    page.emulate_media(reduced_motion='reduce')
    page.wait_for_timeout(30)
    assert page.evaluate('document.getAnimations().length') == 0
    assert page.locator('#editor').evaluate('(n)=>n.open')
    page.locator('#close').click();assert_closed(page)
    return {'animation_observée_avant':before,'après_reduce':0,'état_conservé':True}

def no_api(page, width):
    open_editor(page);fill(page,quantity='9');apply(page)
    expect_total(page,'810,00 €');assert_closed(page)
    assert page.evaluate('document.getAnimations().length') == 0
    return {'API':'Element.animate indisponible','état_final_correct':True}

def no_storage(page, width):
    assert 'temporaire' in page.locator('[data-storage]').first.inner_text()
    open_editor(page);fill(page,quantity='9');apply(page);expect_total(page,'810,00 €')
    return {'stockage':'indisponible et annoncé','calcul':'810,00 €'}

def touch(page, width):
    page.locator('#plus').scroll_into_view_if_needed()
    b=page.locator('#plus').bounding_box();page.touchscreen.tap(b['x']+b['width']/2,b['y']+b['height']/2)
    expect_total(page,'765,00 €')
    return {'action':'tap tactile émulé sur Ajouter une demi-heure','total':'765,00 €','cible':b}

def no_js(page, width):
    assert page.locator('noscript').is_visible()
    assert page.locator('[data-js]:not([disabled])').count()==0
    assert '720,00' in page.locator('#total').inner_text()
    return {'état':'document statique, actions désactivées et limite annoncée'}

cases=[('nominal',nominal),('actions-rapides',rapid),('erreurs-et-reprise',errors_recovery),('annulation',cancellation),('clavier',keyboard),('fermeture-interrompue',interrupted_open),('glissement',drag),('pointeur-annule',pointer_cancel),('hauteur-reduite',low_height),('contenu-long-et-bornes',long_and_boundary),('reprise-locale',persisted),('telechargement',download)]
results=[]
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True)
        browser_version=browser.version
        for width in [1440,390,320]:
            extra=[('mouvement-reduit',reduced),('reduce-pendant-animation',reduce_during),('API-animation-absente',no_api),('stockage-absent',no_storage),('sans-JavaScript',no_js)]
            if width<701:extra.append(('tap-mobile',touch))
            for name,fn in cases+extra:
                context=browser.new_context(viewport={'width':width,'height':1000 if width==1440 else 844},device_scale_factor=1,has_touch=width<701,is_mobile=width<701,accept_downloads=True,reduced_motion='reduce' if name=='mouvement-reduit' else 'no-preference',java_script_enabled=name!='sans-JavaScript')
                if name=='API-animation-absente':context.add_init_script('Element.prototype.animate = undefined;')
                if name=='stockage-absent':context.add_init_script('Storage.prototype.getItem=()=>{throw new Error("storage unavailable")};Storage.prototype.setItem=()=>{throw new Error("storage unavailable")};')
                page=context.new_page();script_errors=[];external=[]
                page.on('pageerror',lambda e:script_errors.append(str(e)))
                context.on('request',lambda req:external.append(req.url) if not req.url.startswith(('http://127.0.0.1:','data:','blob:')) else None)
                row={'case':name,'width':width,'method':'Playwright/Chromium ; contexte neuf','status':'RUNNING'}
                try:
                    page.goto(f'http://127.0.0.1:{server.server_port}/index.html',wait_until='load')
                    if name!='sans-JavaScript':page.evaluate('document.fonts.ready')
                    row['observations']=fn(page,width)
                    assert not script_errors,script_errors
                    assert not external,external
                    row['status']='PASS'
                except Exception as e:
                    row.update(status='FAIL',error=str(e),traceback=traceback.format_exc())
                    page.screenshot(path=str(OUT/f'{width}-{name}-echec.png'),full_page=True)
                finally:
                    row['javascript_errors']=script_errors;row['external_requests']=external;results.append(row);context.close()
                print(width,name,row['status'],row.get('error',''),flush=True)
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
report={'recorded_at_utc':datetime.now(timezone.utc).isoformat(),'artifact_sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(),'browser_executable':'/usr/bin/chromium','browser_version':browser_version,'server_bound':'127.0.0.1','server_stopped':not thread.is_alive(),'cases':results,'passed':sum(x['status']=='PASS' for x in results),'failed':sum(x['status']=='FAIL' for x in results),'limitations':['Web mobile émulé ; aucun téléphone physique ni build natif','Aucun lecteur d’écran, utilisateur représentatif ou audit WCAG exhaustif','Mouvements testés comme transitions d’état ; fluidité sur appareil non établie']}
(OUT/'parcours.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('RESULTAT',report['passed'],'PASS',report['failed'],'FAIL ; serveur arrêté',report['server_stopped'])
raise SystemExit(1 if report['failed'] else 0)
