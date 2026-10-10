from pathlib import Path
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from datetime import datetime,timezone
import hashlib,json,traceback
from playwright.sync_api import sync_playwright
root=Path(__file__).parent
caps=root/'captures-states';caps.mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
report={'artifact':'index.html','sha256':hashlib.sha256((root/'index.html').read_bytes()).hexdigest(),'observed_at':datetime.now(timezone.utc).isoformat(),'runtime':'Chromium /usr/bin/chromium, Python Playwright 1.56.0','method':'Browser actions and DOM assertions, no real user or assistive technology','cases':[]}
errors=[];requests=[]
def case(name,viewport,fn):
 entry={'name':name,'viewport':viewport,'steps':[]}
 report['cases'].append(entry)
 def step(selector,action,observation):entry['steps'].append({'selector':selector,'action':action,'observation':observation})
 try:fn(step);entry['result']='PASS'
 except Exception as e:entry['result']='FAIL';entry['failure']=str(e);entry['traceback']=traceback.format_exc();errors.append(name)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for width,height in [(1440,1000),(390,844),(320,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},accept_downloads=True)
  page_errors=[];page.on('pageerror',lambda e:page_errors.append(str(e)))
  page.on('request',lambda r:requests.append(r.url))
  page.goto(url);page.wait_for_function('document.fonts.status==="loaded"')
  def layout(step):
   sw=page.evaluate('document.documentElement.scrollWidth');assert sw==width,(sw,width)
   assert page.locator('#grand-total').inner_text().replace('\xa0',' ').replace('\u202f',' ')=='720,00 €'
   assert page.locator('.sheet').is_visible()
   step('html, .sheet, #grand-total','load initial page and inspect document width/amount',{'scrollWidth':sw,'viewportWidth':width,'amount':page.locator('#grand-total').inner_text(),'fontStatus':page.evaluate('document.fonts.status'),'pageErrors':page_errors})
  case('Initial layout and coherent calculation',width,layout)
  def invalid(step):
   page.locator('#primary-cta').click();assert page.locator('#editor').is_visible();assert page.evaluate('document.activeElement.id')=='client'
   step('#primary-cta','click',{'dialogVisible':True,'activeElement':'client'})
   for sel,val in [('#client',''),('#service',''),('#hours','0'),('#rate','-1')]:page.locator(sel).fill(val);step(sel,'fill',{'value':val})
   assert page.locator('#form-total').inner_text()=='À vérifier'
   page.locator('#submit-invoice').click()
   invalid_ids=page.locator('[aria-invalid="true"]').evaluate_all('(els)=>els.map(e=>e.id)');assert invalid_ids==['client','service','hours','rate']
   assert page.evaluate('document.activeElement.id')=='client';assert page.locator('#hours').input_value()=='0';assert page.locator('#rate').input_value()=='-1'
   page.screenshot(path=str(caps/f'error-{width}.png'))
   step('#submit-invoice','click with empty text, zero hours and negative rate',{'invalidFields':invalid_ids,'activeElement':'client','hoursRetained':page.locator('#hours').input_value(),'rateRetained':page.locator('#rate').input_value(),'total':'À vérifier','alert':page.locator('#error-summary').inner_text(),'capture':f'captures-states/error-{width}.png'})
  case('Primary action and error state',width,invalid)
  def recovery(step):
   for sel,val in [('#client','Collectif des artisans indépendants — nom de client très long pour vérifier le retour à la ligne'),('#service','Conception et accompagnement de la nouvelle identité visuelle, atelier de cadrage et préparation des livrables'),('#hours','10.5'),('#rate','80.25')]:page.locator(sel).fill(val);step(sel,'fill after validation error',{'value':val})
   page.locator('#tax').select_option('5.5');assert page.locator('#form-total').inner_text().replace('\xa0',' ').replace('\u202f',' ')=='888,97 €'
   step('#tax','select option 5.5',{'previewTotal':page.locator('#form-total').inner_text()})
   page.locator('#submit-invoice').click();assert not page.locator('#editor').is_visible();assert page.locator('#success').is_visible();assert page.evaluate('document.activeElement.id')=='success'
   assert page.locator('#subtotal').inner_text().replace('\xa0',' ').replace('\u202f',' ')=='842,63 €';assert page.locator('#tax-total').inner_text().replace('\xa0',' ').replace('\u202f',' ')=='46,34 €';assert page.locator('#grand-total').inner_text().replace('\xa0',' ').replace('\u202f',' ')=='888,97 €'
   assert page.evaluate('document.documentElement.scrollWidth')==width
   page.screenshot(path=str(caps/f'success-long-{width}.png'),full_page=True)
   step('#submit-invoice','submit corrected and long content',{'dialogVisible':False,'activeElement':page.evaluate('document.activeElement.id'),'subtotal':page.locator('#subtotal').inner_text(),'tax':page.locator('#tax-total').inner_text(),'total':page.locator('#grand-total').inner_text(),'scrollWidth':page.evaluate('document.documentElement.scrollWidth'),'capture':f'captures-states/success-long-{width}.png'})
   with page.expect_download() as d:page.locator('#download').click()
   download=d.value;path=root/f'download-test-{width}.txt';download.save_as(str(path));content=path.read_text()
   assert '888,97' in content;assert 'SANS VALEUR DE FACTURE LÉGALE' in content;assert len(content.splitlines())>=10
   step('#download','click and read actual downloaded file',{'suggestedFilename':download.suggested_filename,'path':path.name,'lineCount':len(content.splitlines()),'containsUpdatedTotal':True,'containsExampleWarning':True})
  case('Recovery, recalculation, long content and download',width,recovery)
  def keyboard(step):
   page.locator('#edit-example').focus();page.keyboard.press('Enter');assert page.locator('#editor').is_visible();assert page.evaluate('document.activeElement.id')=='client'
   step('#edit-example','focus and press Enter',{'dialogVisible':True,'activeElement':'client'})
   order=[]
   for _ in range(8):
    page.keyboard.press('Tab');order.append(page.evaluate('document.activeElement.id'))
   assert order==['service','hours','rate','tax','cancel','submit-invoice','close-dialog','client'],order
   assert page.locator('#client').evaluate("e=>getComputedStyle(e).outlineStyle")!='none'
   step('#editor','8 successive Tab keypresses',{'focusOrder':order,'focusRemainsInDialog':True,'clientOutline':page.locator('#client').evaluate("e=>getComputedStyle(e).outline")})
   page.keyboard.press('Escape');assert not page.locator('#editor').is_visible();assert page.evaluate('document.activeElement.id')=='edit-example'
   step('#editor','Escape',{'dialogVisible':False,'focusReturnedTo':'edit-example'})
   page.locator('#edit-example').click();page.locator('#client').fill('Saisie non validée');page.locator('#cancel').click();page.locator('#edit-example').click();assert page.locator('#client').input_value().startswith('Collectif des artisans')
   step('#client, #cancel, #edit-example','change value, cancel, reopen',{'unsubmittedChangeDiscarded':True,'confirmedDraftRetained':True})
   page.locator('#close-dialog').click();assert not page.locator('#editor').is_visible()
   step('#close-dialog','click',{'dialogVisible':False})
  case('Keyboard trap, Escape, cancel and focus recovery',width,keyboard)
  def faq(step):
   for i in range(4):
    item=page.locator('details').nth(i);summary=item.locator('summary');summary.focus();page.keyboard.press('Enter');assert item.get_attribute('open') is not None
    step(f'details:nth-of-type({i+1}) summary','focus and Enter',{'open':True,'contentVisible':item.locator('p').is_visible()});page.keyboard.press('Enter');assert item.get_attribute('open') is None
  case('FAQ keyboard disclosure',width,faq)
  assert not page_errors,page_errors
  page.close()
 page=browser.new_page(viewport={'width':390,'height':844},reduced_motion='reduce');page.goto(url)
 def reduced(step):
  observed=page.evaluate("({reduce:matchMedia('(prefers-reduced-motion: reduce)').matches,scrollBehavior:getComputedStyle(document.documentElement).scrollBehavior})");assert observed=={'reduce':True,'scrollBehavior':'auto'}
  step('html','load with reduced_motion=reduce',observed)
 case('Reduced movement preference',390,reduced)
 def reload(step):
  assert page.locator('#client-output').inner_text()=='Studio Lundi';assert not page.locator('#success').is_visible()
  step('#client-output, #success','load a fresh page after previous draft tests',{'client':'Studio Lundi','successVisible':False,'noPersistedDraft':True})
 case('Fresh session has no saved draft',390,reload)
 def external(step):
  external_urls=sorted({r for r in requests if not r.startswith(f'http://127.0.0.1:{server.server_port}/')});assert not external_urls,external_urls
  step('network request events','inspect requests observed during all functional cases',{'externalRequests':external_urls,'observedRequests':len(requests)})
 case('No external network requests',None,external)
 browser.close()
server.shutdown();server.server_close()
report['summary']={'executed':len(report['cases']),'passed':sum(c['result']=='PASS' for c in report['cases']),'failed':sum(c['result']=='FAIL' for c in report['cases'])}
(root/'functional-tests.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report['summary']))
if errors:print('Failed cases: '+', '.join(errors));raise SystemExit(1)
