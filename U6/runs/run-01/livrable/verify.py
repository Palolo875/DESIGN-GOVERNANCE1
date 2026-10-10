from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright
import json, hashlib, re

ROOT=Path(__file__).resolve().parent
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT)))
thread=Thread(target=server.serve_forever,daemon=True);thread.start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
report={'artifact':'index.html','sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(),'observed_at':datetime.now(timezone.utc).isoformat(),'runtime':'Python Playwright / /usr/bin/chromium','method':'Executed browser interactions, DOM measurements and screenshots; no participants or assistive technology','journeys':[],'limitations':['No screen reader, Firefox, Safari, real product, registration, fiscal conformity or real delivery tested.']}
def clean(s): return re.sub(r'\s+',' ',s).strip()
def case(name,viewport,steps,obs,condition):
    report['journeys'].append({'name':name,'viewport':viewport,'steps':steps,'observations':obs,'result':'PASS' if condition else 'FAIL'})
try:
  with sync_playwright() as p:
    browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
    page=browser.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
    errors=[];requests=[]
    page.on('pageerror',lambda e:errors.append(str(e)))
    page.on('request',lambda r:requests.append(r.url))
    for width,height in [(1440,1000),(390,844),(320,844)]:
      page.set_viewport_size({'width':width,'height':height});page.goto(url);page.evaluate('document.fonts.ready')
      geom=page.evaluate('''() => ({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth,fields:[...document.querySelectorAll('input,select,button')].filter(e=>e.getClientRects().length).map(e=>({id:e.id,w:e.getBoundingClientRect().width,h:e.getBoundingClientRect().height}))})''')
      case('Page nominale et débordement',f'{width}x{height}',[{'selector':'document','action':'navigate, await fonts, measure widths'}],geom,geom['scroll']==width and geom['body']<=width and all(e['h']>=44 for e in geom['fields']))
      total=clean(page.locator('#total').inner_text())
      case('Calcul initial',f'{width}x{height}',[{'selector':'#total','action':'read nominal value'}],{'total':total},total=='2 040,00 €')
      page.locator('.hero-actions [data-start]').click();page.wait_for_timeout(400)
      action=page.evaluate('''() => ({active:document.activeElement.id,rect:document.activeElement.getBoundingClientRect().toJSON(),height:innerHeight})''')
      case('Action principale',f'{width}x{height}',[{'selector':'.hero-actions [data-start]','action':'click'}],action,action['active']=='client' and action['rect']['top']>=0 and action['rect']['bottom']<=height)
      for sel,value in [('#client',''),('#service',''),('#quantity','0'),('#rate','-1')]:page.locator(sel).fill(value)
      page.locator('#prepare').click()
      invalid=page.evaluate('''() => ({focus:document.activeElement.id,errors:[...document.querySelectorAll('.error:not([hidden])')].map(e=>({id:e.id,text:e.textContent})),values:[...document.querySelectorAll('input')].map(e=>({id:e.id,value:e.value,invalid:e.getAttribute('aria-invalid')})),dialog:document.getElementById('preview-dialog').open,total:document.getElementById('total').textContent})''')
      case('Erreurs et saisie conservée',f'{width}x{height}',[{'selector':'#client,#service','action':'fill empty'},{'selector':'#quantity','action':'fill 0'},{'selector':'#rate','action':'fill -1'},{'selector':'#prepare','action':'click'}],invalid,invalid['focus']=='client' and len(invalid['errors'])==4 and not invalid['dialog'] and invalid['total']=='À compléter')
      page.screenshot(path=str(ROOT/'captures'/f'error-{width}.png'))
      for sel,value in [('#client','Atelier Horizon'),('#service','Conception du site vitrine'),('#quantity','3'),('#rate','240')]:page.locator(sel).fill(value)
      page.locator('#tax').select_option('20')
      recovery={'errors_visible':page.locator('.error:not([hidden])').count(),'subtotal':clean(page.locator('#subtotal').inner_text()),'vat':clean(page.locator('#tax-total').inner_text()),'total':clean(page.locator('#total').inner_text())}
      case('Reprise après erreur et recalcul',f'{width}x{height}',[{'selector':'#client,#service,#quantity,#rate','action':'fill Atelier Horizon / Conception du site vitrine / 3 / 240'},{'selector':'#tax','action':'select 20'}],recovery,recovery=={'errors_visible':0,'subtotal':'720,00 €','vat':'144,00 €','total':'864,00 €'})
      page.locator('#prepare').click()
      preview={'open':page.locator('#preview-dialog').evaluate('(e)=>e.open'),'focus':page.evaluate('document.activeElement.id'),'client':page.locator('#preview-client').inner_text(),'service':page.locator('#preview-service').inner_text(),'total':clean(page.locator('#preview-total').inner_text()),'scroll':page.locator('#preview-dialog').evaluate('(e)=>({client:e.clientWidth,scroll:e.scrollWidth})')}
      case('Aperçu réussi',f'{width}x{height}',[{'selector':'#prepare','action':'click'}],preview,preview['open'] and preview['focus']=='close-preview' and preview['client']=='Atelier Horizon' and preview['total']=='Total TTC · 864,00 €' and preview['scroll']['scroll']<=preview['scroll']['client'])
      page.screenshot(path=str(ROOT/'captures'/f'preview-{width}.png'))
      if width==1440:
        trap=[]
        for i in range(7):page.keyboard.press('Tab');trap.append(page.evaluate('document.activeElement.id'))
        case('Clavier dans la modale',f'{width}x{height}',[{'selector':'#preview-dialog','action':'press Tab seven times'}],{'focus_sequence':trap},set(trap)=={'close-preview','download','edit'})
        with page.expect_download() as download_info: page.locator('#download').click()
        download=download_info.value;download.save_as(str(ROOT/'download-observed.txt'))
        content=(ROOT/'download-observed.txt').read_text()
        case('Téléchargement local',f'{width}x{height}',[{'selector':'#download','action':'click and save browser download'}],{'suggested_filename':download.suggested_filename,'contains_total':'864,00' in content,'contains_client':'Atelier Horizon' in content,'contains_disclaimer':'PAS UNE FACTURE FISCALE' in content,'status':page.locator('#download-status').inner_text()},'864,00' in content and 'Atelier Horizon' in content and 'PAS UNE FACTURE FISCALE' in content)
      page.keyboard.press('Escape')
      case('Sortie par Escape',f'{width}x{height}',[{'selector':'#preview-dialog','action':'press Escape'}],{'open':page.locator('#preview-dialog').evaluate('(e)=>e.open'),'focus':page.evaluate('document.activeElement.id')},not page.locator('#preview-dialog').evaluate('(e)=>e.open') and page.evaluate('document.activeElement.id')=='prepare')
      page.locator('#tax').select_option('0')
      zero=clean(page.locator('#total').inner_text())
      case('TVA illustrative nulle',f'{width}x{height}',[{'selector':'#tax','action':'select 0'}],{'total':zero},zero=='720,00 €')
    page.set_viewport_size({'width':390,'height':844});page.goto(url)
    longclient='Studio des projets et des collaborations indépendantes — Horizon et ses partenaires créatifs'
    longservice='Conception et direction artistique du site, des supports éditoriaux et de la campagne de lancement — phase de validation finale'
    page.locator('#client').fill(longclient);page.locator('#service').fill(longservice);page.locator('#prepare').click()
    longobs=page.locator('#preview-dialog').evaluate('(e)=>({client:e.clientWidth,scroll:e.scrollWidth,height:e.clientHeight,scrollHeight:e.scrollHeight})')
    longobs['client_text']=page.locator('#preview-client').inner_text();longobs['service_text']=page.locator('#preview-service').inner_text()
    page.screenshot(path=str(ROOT/'captures'/'long-preview-390.png'))
    case('Contenu long', '390x844',[{'selector':'#client,#service','action':'fill long French client and service'},{'selector':'#prepare','action':'click'}],longobs,longobs['scroll']<=longobs['client'] and longobs['client_text']==longclient and longobs['service_text']==longservice)
    page.keyboard.press('Escape');page.goto(url)
    tabs=[]
    for i in range(27):
      page.keyboard.press('Tab');page.wait_for_timeout(450)
      tabs.append(page.evaluate('''() => {const e=document.activeElement,r=e.getBoundingClientRect(),s=getComputedStyle(e);return {tag:e.tagName,id:e.id,text:e.innerText?.slice(0,70)||e.getAttribute('aria-label')||e.name||'',outline:s.outline,visible:r.top>=0&&r.bottom<=innerHeight};}'''))
      if i>0 and tabs[-1]['text']=='Aller au contenu':break
    focus_pass=all(t['visible'] and '3px' in t['outline'] for t in tabs if t['tag']!='BODY')
    case('Parcours Tab de la page','390x844',[{'selector':'body','action':'reload, Tab through page until cycle or 27 steps'}],{'stops':tabs,'all_visible_and_outlined':focus_pass},focus_pass)
    page.locator('summary').nth(1).focus();page.keyboard.press('Enter')
    faq={'open':page.locator('details').nth(1).evaluate('(e)=>e.open'),'text':page.locator('details').nth(1).inner_text()}
    case('FAQ au clavier','390x844',[{'selector':'summary:nth(1)','action':'focus then Enter'}],faq,faq['open'] and 'Tout reste dans votre navigateur' in faq['text'])
    page.emulate_media(reduced_motion='reduce');page.goto(url)
    reduced=page.evaluate('({preference:matchMedia("(prefers-reduced-motion: reduce)").matches,scroll:getComputedStyle(document.documentElement).scrollBehavior})')
    case('Mouvement réduit','390x844',[{'selector':'html','action':'emulate reduced motion and read scroll-behavior'}],reduced,reduced['preference'] and reduced['scroll']=='auto')
    page.emulate_media(reduced_motion='no-preference');page.set_viewport_size({'width':320,'height':844});page.goto(url)
    page.evaluate("document.body.style.fontSize='200%'")
    zoom={'width':page.evaluate('innerWidth'),'scroll':page.evaluate('document.documentElement.scrollWidth')}
    case('Propriété body font-size à 200 % — ne prouve pas le zoom','320x844',[{'selector':'body','action':'set font-size 200%, measure page overflow'}],zoom,zoom['width']==zoom['scroll'])
    report['limitations'].append('The body font-size 200% probe does not establish browser zoom support: most typography uses explicit px sizes. Real browser zoom remains unverified.')
    page.set_viewport_size({'width':1440,'height':1000});page.goto(url)
    contrast=page.evaluate('''() => {
      const samples=[];
      const lum=c=>{let vals=c.match(/[\\d.]+/g).slice(0,3).map(Number).map(v=>{v/=255;return v<=.04045?v/12.92:Math.pow((v+.055)/1.055,2.4)});return .2126*vals[0]+.7152*vals[1]+.0722*vals[2]};
      const bg=e=>{while(e){const c=getComputedStyle(e).backgroundColor;if(!c.endsWith(', 0)')&&c!='transparent')return c;e=e.parentElement;}return 'rgb(255, 255, 255)'};
      for(const e of document.querySelectorAll('body *')){if(!e.getClientRects().length||getComputedStyle(e).visibility=='hidden')continue;const direct=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());if(!direct&&!['INPUT','SELECT'].includes(e.tagName))continue;const s=getComputedStyle(e),b=bg(e),l1=lum(s.color),l2=lum(b),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05),large=parseFloat(s.fontSize)>=24||(parseFloat(s.fontSize)>=18.66&&parseFloat(s.fontWeight)>=700),minimum=large?3:4.5;samples.push({tag:e.tagName,id:e.id,class:e.className,text:(e.textContent||e.value||'').slice(0,65),color:s.color,background:b,size:s.fontSize,weight:s.fontWeight,ratio:+ratio.toFixed(2),minimum,pass:ratio>=minimum})}return samples;
    }''')
    report['contrast_samples']=contrast
    case('Contrastes textuels sur fonds unis','1440x1000',[{'selector':'visible direct text,input,select','action':'calculate WCAG relative luminance, nearest opaque ancestor background'}],{'samples':len(contrast),'failures':[c for c in contrast if not c['pass']]},all(c['pass'] for c in contrast))
    report['console_errors']=errors;report['requests']=sorted(set(requests));external=[r for r in requests if not r.startswith(f'http://127.0.0.1:{server.server_port}/')]
    case('Autonomie et erreurs JS','all tested viewports',[{'selector':'page','action':'record pageerror and requests during executed journeys'}],{'errors':errors,'external_requests':external},not errors and not external)
    browser.close()
except Exception as e:
  report['execution_error']=repr(e)
finally:
  server.shutdown();server.server_close();thread.join(timeout=3)
  report['passed']=sum(c['result']=='PASS' for c in report['journeys']);report['failed']=sum(c['result']=='FAIL' for c in report['journeys'])
  (ROOT/'functional-tests.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
  print(json.dumps({'passed':report['passed'],'failed':report['failed'],'execution_error':report.get('execution_error'),'failures':[c for c in report['journeys'] if c['result']=='FAIL']},ensure_ascii=False))
