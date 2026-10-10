from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from datetime import datetime, timezone
import json, hashlib
from playwright.sync_api import sync_playwright
OUT=Path('/workspace/remesure-phase5/runs/run-03/livrable')
log=(OUT/'server.log').open('w')
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,format,*args): log.write(format%args+'\n');log.flush()
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(OUT)))
Thread(target=server.serve_forever,daemon=True).start()
url='http://127.0.0.1:'+str(server.server_port)+'/index.html'
cases=[];errors=[];requests=[];observations={}
def case(name,steps,observed,expected,ok):
 cases.append({'name':name,'steps':steps,'expected':expected,'observed':observed,'result':'PASS' if ok else 'FAIL'})
def step(selector,action,value=None):
 d={'selector':selector,'action':action}
 if value is not None:d['value']=value
 return d
try:
 with sync_playwright() as p:
  browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
  page=browser.new_page(viewport={'width':1440,'height':1000},accept_downloads=True)
  page.on('pageerror',lambda e:errors.append(str(e)))
  page.on('request',lambda r:requests.append(r.url))
  page.goto(url,wait_until='networkidle');page.evaluate('document.fonts.ready')
  observations['font_loaded']=page.evaluate('document.fonts.check("500 66px Manrope")')
  observations['viewports']=[]
  for width,height in [(1440,1000),(390,844),(320,844)]:
   page.set_viewport_size({'width':width,'height':height});page.evaluate('window.scrollTo(0,0)')
   result=page.evaluate('''() => ({width:innerWidth,scrollWidth:document.documentElement.scrollWidth,bodyWidth:document.body.scrollWidth,overflowElements:[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+.5||r.left<-.5)&&getComputedStyle(e).position!=='absolute'}).map(e=>({tag:e.tagName,id:e.id,class:e.className,left:e.getBoundingClientRect().left,right:e.getBoundingClientRect().right})).slice(0,20)})''')
   observations['viewports'].append(result)
   page.screenshot(path=str(OUT/f'captures/delivered-{width}.png'),full_page=True)
   page.screenshot(path=str(OUT/f'captures/delivered-viewport-{width}.png'))
   case(f'No overflow at {width}px',[step('html','set viewport',f'{width}x{height}')],result,'document width equals viewport; no page overflow',result['scrollWidth']==width and result['bodyWidth']==width)
  page.set_viewport_size({'width':1440,'height':1000});page.evaluate('window.scrollTo(0,0)')
  page.locator('.stage').evaluate("el=>el.style.background='#f3f6f2'")
  page.screenshot(path=str(OUT/'captures/variant-reduced-field-delivered-1440.png'),full_page=True)
  page.locator('.stage').evaluate('el=>el.style.removeProperty("background")')
  # Keyboard entry: primary action via actual Enter.
  page.locator('.hero [data-open-demo]').focus();page.keyboard.press('Enter')
  openobs={'open':page.locator('#demo-dialog').evaluate('el=>el.open'),'focus':page.evaluate('document.activeElement.id'),'description':page.locator('#demo-description').inner_text()}
  case('Primary action by keyboard',[step('.hero [data-open-demo]','focus'),step('.hero [data-open-demo]','press','Enter')],openobs,'dialog opens, client field receives focus',openobs['open'] and openobs['focus']=='client')
  # Native modal containment and visible focus.
  stops=[]
  for _ in range(10):
   page.keyboard.press('Tab');stops.append(page.evaluate('''() => {const e=document.activeElement,s=getComputedStyle(e),r=e.getBoundingClientRect();return {tag:e.tagName,id:e.id,text:e.tagName==='BUTTON'?e.textContent.trim():'',inside:!!e.closest('#demo-dialog'),outline:s.outlineStyle,outlineWidth:s.outlineWidth,visible:r.width>0&&r.height>0}}'''))
  reverse=[]
  for _ in range(10):
   page.keyboard.press('Shift+Tab');reverse.append(page.evaluate('({id:document.activeElement.id,inside:!!document.activeElement.closest("#demo-dialog")})'))
  case('Dialog reverse Tab containment',[step('#demo-dialog','press Shift+Tab','10 times')],reverse,'all focus stops remain in dialog',all(x['inside'] for x in reverse))
  case('Dialog Tab containment and focus',[step('#demo-dialog','press Tab','10 times')],stops,'all focus stops remain inside dialog and show a visible outline',all(s['inside'] and s['visible'] and s['outline']!='none' for s in stops))
  page.locator('#client').fill('');page.locator('#service').fill('');page.locator('#amount').fill('-3');page.locator('#invoice-form button[type=submit]').click()
  errorobs={'status':page.locator('#form-status').inner_text(),'invalid':[e.get_attribute('id') for e in page.locator('[aria-invalid=true]').all()],'focus':page.evaluate('document.activeElement.id'),'amountRetained':page.locator('#amount').input_value(),'errors':{f:page.locator('#'+f+'-error').inner_text() for f in ['client','service','amount']}}
  page.screenshot(path=str(OUT/'captures/delivered-error-1440.png'))
  page.set_viewport_size({'width':390,'height':844});page.screenshot(path=str(OUT/'captures/delivered-error-390.png'))
  page.set_viewport_size({'width':320,'height':844});modal320=page.locator('dialog').evaluate('el=>({client:el.clientWidth,scroll:el.scrollWidth})')
  case('Modal error state at 320px',[step('#demo-dialog','set viewport','320x844')],modal320,'no horizontal overflow within dialog',modal320['scroll']<=modal320['client'])
  page.set_viewport_size({'width':1440,'height':1000})
  case('Empty and invalid input with recovery instructions',[step('#client','fill',''),step('#service','fill',''),step('#amount','fill','-3'),step('#invoice-form button[type=submit]','click')],errorobs,'three inline errors; first invalid field focused; entered amount retained',len(errorobs['invalid'])==3 and errorobs['focus']=='client' and errorobs['amountRetained']=='-3')
  page.locator('#client').fill('Studio Horizon');page.locator('#service').fill('Design d’une identité');page.locator('#amount').fill('1200');page.locator('#vat').select_option('20');page.locator('#invoice-form button[type=submit]').click()
  success={'visible':page.locator('#result-view').is_visible(),'total':page.locator('#result-sheet [data-doc-total]').inner_text(),'tax':page.locator('#result-sheet [data-doc-tax]').inner_text(),'focus':page.evaluate('document.activeElement.id'),'client':page.locator('#result-sheet [data-doc-client]').inner_text()}
  page.screenshot(path=str(OUT/'captures/delivered-success-1440.png'))
  case('Correct errors and create preview',[step('#client','fill','Studio Horizon'),step('#service','fill','Design d’une identité'),step('#amount','fill','1200'),step('#vat','select_option','20'),step('#invoice-form button[type=submit]','click')],success,'preview visible; 240 € tax and 1 440 € total; heading focused',success['visible'] and success['total'].replace('\u202f',' ').replace('\xa0',' ')=='1 440,00 €' and success['focus']=='result-title')
  with page.expect_download() as info:page.locator('#download-example').click()
  download=info.value;download.save_as(str(OUT/'download-observed.txt'));download_text=(OUT/'download-observed.txt').read_text()
  downloadobs={'suggestedFilename':download.suggested_filename,'text':download_text,'status':page.locator('#download-status').inner_text()}
  case('Local download',[step('#download-example','click'),step('download','save_as','download-observed.txt')],downloadobs,'text download contains correct total and disclosure, no server submission',download.suggested_filename=='facture-exemple.txt' and 'sans valeur comptable' in download_text and '1\u202f440,00' in download_text)
  page.locator('#edit-example').click();editobs={'visible':page.locator('#edit-view').is_visible(),'client':page.locator('#client').input_value(),'focus':page.evaluate('document.activeElement.id')}
  case('Return to editing without lost data',[step('#edit-example','click')],editobs,'original client is retained and focused',editobs['visible'] and editobs['client']=='Studio Horizon' and editobs['focus']=='client')
  # Precision guard, then largest allowed amount and long text on mobile.
  page.locator('#amount').fill('1.001');page.locator('#invoice-form button[type=submit]').click();precision=page.locator('#amount-error').inner_text()
  case('Reject fractional cents',[step('#amount','fill','1.001'),step('#invoice-form button[type=submit]','click')],precision,'specific error blocks preview',bool(precision) and page.locator('#edit-view').is_visible())
  longclient='Studio de création et de communication pour les petites entreprises françaises'
  longservice='Conception et réalisation de supports de communication, direction artistique et accompagnement éditorial — prestation'
  page.locator('#client').fill(longclient);page.locator('#service').fill(longservice);page.locator('#amount').fill('99999.99');page.locator('#vat').select_option('20');page.locator('#invoice-form button[type=submit]').click()
  page.set_viewport_size({'width':390,'height':844})
  extreme=page.evaluate('''() => ({width:innerWidth,pageScroll:document.documentElement.scrollWidth,dialogClient:document.querySelector('dialog').clientWidth,dialogScroll:document.querySelector('dialog').scrollWidth,resultScroll:document.querySelector('#result-view').scrollWidth,resultClient:document.querySelector('#result-view').clientWidth,total:document.querySelector('#result-sheet [data-doc-total]').textContent})''')
  page.screenshot(path=str(OUT/'captures/delivered-long-success-390.png'))
  case('Long content and maximum amount on mobile',[step('#client','fill',longclient),step('#service','fill',longservice),step('#amount','fill','99999.99'),step('#vat','select_option','20'),step('#invoice-form button[type=submit]','click'),step('html','set viewport','390x844')],extreme,'no page or dialog horizontal overflow, total 119 999,99 €',extreme['pageScroll']==390 and extreme['dialogScroll']<=extreme['dialogClient'] and extreme['total'].replace('\u202f',' ').replace('\xa0',' ')=='119 999,99 €')
  page.keyboard.press('Escape');closeobs={'open':page.locator('#demo-dialog').evaluate('el=>el.open'),'focusMatchesOpener':page.locator('.hero [data-open-demo]').evaluate('el=>el===document.activeElement'),'bodyLocked':page.locator('body').evaluate("el=>el.classList.contains('modal-open')")}
  case('Escape closes and restores focus',[step('#demo-dialog','press','Escape')],closeobs,'dialog closed; opener focused; page scrolling restored',not closeobs['open'] and closeobs['focusMatchesOpener'] and not closeobs['bodyLocked'])
  page.locator('.hero [data-open-demo]').click();page.locator('#client').fill('<img src=x onerror=alert(1)>');page.locator('#service').fill('Prestation d’exemple');page.locator('#amount').fill('50');page.locator('#vat').select_option('0');page.locator('#invoice-form button[type=submit]').click()
  safeobs={'text':page.locator('#result-sheet [data-doc-client]').inner_text(),'images':page.locator('#result-sheet img').count(),'total':page.locator('#result-sheet [data-doc-total]').inner_text()}
  case('User text stays plain text, zero VAT',[step('#client','fill','<img src=x onerror=alert(1)>'),step('#amount','fill','50'),step('#vat','select_option','0'),step('#invoice-form button[type=submit]','click')],safeobs,'input rendered literally, no injected image, total 50 €',safeobs['images']==0 and safeobs['text']=='<img src=x onerror=alert(1)>' and safeobs['total'].replace('\xa0',' ')=='50,00 €')
  page.locator('#close-demo').click();page.locator('#questions details').first.locator('summary').focus();page.keyboard.press('Enter');faqobs=page.locator('#questions details').first.evaluate('el=>el.open')
  case('FAQ by keyboard',[step('#questions details:first-child summary','focus'),step('#questions details:first-child summary','press','Enter')],{'open':faqobs},'FAQ opens on Enter',faqobs)
  page.locator('#questions details').first.locator('summary').press('Enter')
  # Reduced motion observed rather than declared.
  page.emulate_media(reduced_motion='reduce');reduced=page.evaluate('getComputedStyle(document.documentElement).scrollBehavior')
  case('Reduced motion',[step('html','emulate prefers-reduced-motion','reduce')],{'scrollBehavior':reduced},'scroll behavior is auto',reduced=='auto')
  page.emulate_media(reduced_motion='no-preference');page.set_viewport_size({'width':1440,'height':1000});page.evaluate('window.scrollTo(0,0)')
  # Main page focus order is observed through actual Tab, from a fresh page.
  page.goto(url,wait_until='networkidle');page.evaluate('document.fonts.ready')
  mainstops=[]
  for _ in range(15):
   page.keyboard.press('Tab');mainstops.append(page.evaluate('''() => {const e=document.activeElement,s=getComputedStyle(e),r=e.getBoundingClientRect();return {tag:e.tagName,id:e.id,name:e.getAttribute('aria-label')||e.textContent.trim().slice(0,100),outline:s.outlineStyle,width:s.outlineWidth,visible:r.width>0&&r.height>0,withinViewport:r.top>=0&&r.bottom<=innerHeight}}'''))
  case('All main-page keyboard stops',[step('body','press Tab','15 successive stops after reload')],mainstops,'15 focusable controls reached with visible focus and no masked focus',all(x['tag']!='BODY' and x['outline']!='none' and x['visible'] and x['withinViewport'] for x in mainstops))
  page.evaluate('window.scrollTo(0,0)')
  # Contrast sample from actual styles, plain opaque backgrounds only.
  contrast=page.evaluate('''() => {
 const rgb=c=>{const m=c.match(/rgba?\\(([^)]+)\\)/);return m?m[1].split(',').map(Number):null};
 const lum=c=>{const x=c.slice(0,3).map(v=>{v/=255;return v<=.04045?v/12.92:((v+.055)/1.055)**2.4});return .2126*x[0]+.7152*x[1]+.0722*x[2]};
 let data=[];let walker=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let node;
 while(node=walker.nextNode()){if(!node.textContent.trim())continue;const e=node.parentElement;if(['SCRIPT','STYLE','NOSCRIPT'].includes(e.tagName)||!e.getClientRects().length)continue;const style=getComputedStyle(e);let bg=null;let a=e;while(a){const c=rgb(getComputedStyle(a).backgroundColor);if(c&&(c.length<4||c[3]===1)){bg=c;break}a=a.parentElement}bg=bg||[255,255,255];const fg=rgb(style.color);if(!fg)continue;const l1=lum(fg),l2=lum(bg),ratio=(Math.max(l1,l2)+.05)/(Math.min(l1,l2)+.05);const size=parseFloat(style.fontSize),bold=parseFloat(style.fontWeight)>=700,threshold=(size>=24||(bold&&size>=18.66))?3:4.5;data.push({text:node.textContent.trim().slice(0,100),selector:e.id?'#'+e.id:e.tagName.toLowerCase()+'.'+e.className,color:style.color,background:bg,size,weight:style.fontWeight,ratio:Math.round(ratio*100)/100,threshold,pass:ratio>=threshold})}
 return {samples:data,failures:data.filter(x=>!x.pass)}
}''')
  observations['contrast']=contrast
  case('Text contrast on representative rendered text',[step('body text nodes','calculate WCAG luminance ratios against opaque ancestor backgrounds')],{'sampleCount':len(contrast['samples']),'failures':contrast['failures']},'all measured nominal page text >= relevant AA threshold',not contrast['failures'])
  external=[u for u in requests if not u.startswith('http://127.0.0.1:') and not u.startswith('blob:') and not u.startswith('data:')]
  case('No external requests or script error',[step('page','listen request and pageerror events throughout all tests')],{'externalRequests':external,'pageErrors':errors},'no external request and no script error',not external and not errors)
  observations['requests']=requests;observations['page_errors']=errors;observations['chromium_version']=browser.version;observations['html_bytes']=(OUT/'index.html').stat().st_size
  browser.close()
finally:
 server.shutdown();server.server_close();log.close()
result={'artifact':'index.html','artifact_sha256':hashlib.sha256((OUT/'index.html').read_bytes()).hexdigest(),'observed_at':datetime.now(timezone.utc).isoformat(),'method':'Python Playwright 1.56.0 with local Chromium, author-written executed scenarios','runtime':observations.get('chromium_version'),'server_stopped':True,'cases':cases,'observations':observations,'limits':['No user participant or independent review','No screen reader or second browser tested','Contrast measurements cover opaque nominal page text; dialog and non-text checks are recorded separately','No service, accounting validity, tax compliance, subscription or sending tested']}
(OUT/'functional-tests.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps({'case_count':len(cases),'failures':[c['name'] for c in cases if c['result']=='FAIL'],'server_stopped':True,'html_bytes':observations.get('html_bytes')},ensure_ascii=False))
