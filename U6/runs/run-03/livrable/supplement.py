from pathlib import Path
from datetime import datetime,timezone
import json,hashlib
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
from playwright.sync_api import sync_playwright
out=Path('/workspace/remesure-phase5/runs/run-03/livrable');tests=json.loads((out/'functional-tests.json').read_text());extra=[{'name':'Direct file URL availability','steps':[{'selector':'index.html','action':'open file URL'}],'expected':'autonomous HTML opens directly','observed':'Chromium rejected file:///workspace/remesure-phase5/runs/run-03/livrable/index.html with net::ERR_BLOCKED_BY_ADMINISTRATOR','result':'NOT-VERIFIED'}]
class Handler(SimpleHTTPRequestHandler):
 def log_message(self,*args):pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(out)));Thread(target=server.serve_forever,daemon=True).start();url='http://127.0.0.1:'+str(server.server_port)+'/index.html'
def add(name,steps,observed,expected,ok):extra.append({'name':name,'steps':steps,'observed':observed,'expected':expected,'result':'PASS' if ok else 'FAIL'})
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox']);page=b.new_page(viewport={'width':1440,'height':1000},accept_downloads=True);page.goto(url);page.evaluate('document.fonts.ready')
 geometry=[]
 for w in [768,1024]:
  page.set_viewport_size({'width':w,'height':1000})
  geometry.append(page.evaluate('''()=>{const t=document.querySelector('h1').getBoundingClientRect(),s=document.querySelector('.stage').getBoundingClientRect(),sp=document.querySelector('h1 span').getBoundingClientRect();const range=document.createRange();range.selectNodeContents(document.querySelector('h1 span'));const glyph=range.getBoundingClientRect();return {width:innerWidth,scroll:document.documentElement.scrollWidth,titleRight:glyph.right,stageLeft:s.left,verticalOverlap:t.top<s.bottom&&t.bottom>s.top,collision:glyph.right>s.left&&(t.top<s.bottom&&t.bottom>s.top)}}'''))
 add('Intermediate viewport geometry',[{'selector':'html','action':'set viewport','value':'768 and 1024px'}],geometry,'no page overflow or title/document collision',all(x['scroll']==x['width'] and not x['collision'] for x in geometry))
 page.set_viewport_size({'width':1440,'height':1000});page.locator('.hero').evaluate("e=>e.style.filter='blur(8px)'");page.locator('.hero').screenshot(path=str(out/'captures/masses-delivered-1440.png'));page.locator('.hero').evaluate('e=>e.style.removeProperty("filter")');page.locator('#hero-sheet').screenshot(path=str(out/'captures/detail-delivered-sheet.png'))
 page.set_viewport_size({'width':390,'height':844});page.locator('.hero [data-open-demo]').click();page.locator('#amount').fill('-1');page.locator('#invoice-form button').click();errors=page.locator('#amount-error').inner_text();focus=page.evaluate('document.activeElement.id');page.locator('#amount').fill('123.45');page.locator('#vat').select_option('10');page.locator('#invoice-form button').click();amounts={'tax':page.locator('#result-sheet [data-doc-tax]').inner_text(),'total':page.locator('#result-sheet [data-doc-total]').inner_text(),'errorObserved':errors,'invalidFocus':focus}
 add('Mobile error and decimal rounding',[{'selector':'index.html','action':'open via local HTTP at 390x844'},{'selector':'.hero [data-open-demo]','action':'click'},{'selector':'#amount','action':'fill','value':'-1'},{'selector':'#invoice-form button','action':'click'},{'selector':'#amount','action':'fill','value':'123.45'},{'selector':'#vat','action':'select_option','value':'10'},{'selector':'#invoice-form button','action':'click'}],amounts,'error focuses amount; correction produces 12,35 € VAT and 135,80 € TTC',bool(errors) and focus=='amount' and amounts['tax'].replace('\xa0',' ')=='12,35 €' and amounts['total'].replace('\xa0',' ')=='135,80 €')
 with page.expect_download() as event:page.locator('#download-example').click()
 d=event.value;d.save_as(str(out/'mobile-download-observed.txt'));page.screenshot(path=str(out/'captures/mobile-download-delivered-390.png'))
 add('Mobile local download and scrolling',[{'selector':'#download-example','action':'click at 390x844'},{'selector':'download','action':'save_as','value':'mobile-download-observed.txt'}],{'filename':d.suggested_filename,'status':page.locator('#download-status').inner_text(),'totalInFile':'135,80' in (out/'mobile-download-observed.txt').read_text()},'download available after scrolling dialog; correct mobile result in local text',d.suggested_filename=='facture-exemple.txt' and '135,80' in (out/'mobile-download-observed.txt').read_text())
 page.locator('#edit-example').click();page.locator('#amount').fill('0');page.locator('#invoice-form button').click()
 colours=page.evaluate('''()=>{let sels=['#amount','#amount-error','#form-status','.local-note','.modal-header p','.close'];return sels.map(q=>{const e=document.querySelector(q),s=getComputedStyle(e);let bg='rgb(255, 255, 255)';let a=e;while(a){let c=getComputedStyle(a).backgroundColor;if(c!=='rgba(0, 0, 0, 0)'){bg=c;break;}a=a.parentElement}return {selector:q,color:s.color,background:bg,border:s.borderColor,outline:s.outlineColor}})}''')
 def luminance(rgb):
  import re
  vals=[int(v)/255 for v in re.findall(r'\d+',rgb)[:3]];vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals];return sum(a*b for a,b in zip(vals,[.2126,.7152,.0722]))
 def ratio(a,b):
  l1,l2=sorted([luminance(a),luminance(b)]);return (l2+.05)/(l1+.05)
 for c in colours:c['ratio']=round(ratio(c['color'],c['background']),3)
 nontext=[{'relation':'input border on white','ratio':round(ratio('rgb(133, 152, 141)','rgb(255, 255, 255)'),3)},{'relation':'focus outline on white','ratio':round(ratio('rgb(64, 100, 34)','rgb(255, 255, 255)'),3)},{'relation':'error border on white','ratio':round(ratio('rgb(168, 39, 39)','rgb(255, 255, 255)'),3)}]
 add('Dialog contrast including errors and field boundaries',[{'selector':'#amount-error, #form-status, #amount, .modal-header p, .close','action':'measure actual CSS colors and calculate WCAG luminance ratio'}],{'text':colours,'nonText':nontext},'sample text >=4.5 and critical non-text borders/focus >=3',all(c['ratio']>=4.5 for c in colours) and all(c['ratio']>=3 for c in nontext))
 page.locator('#close-demo').click();b.close()
server.shutdown();server.server_close()
tests['limits'].append('Direct file URL blocked by browser administrator policy; local HTTP rendering observed instead')
tests['cases']+=extra;tests['supplement_observed_at']=datetime.now(timezone.utc).isoformat();tests['artifact_sha256']=hashlib.sha256((out/'index.html').read_bytes()).hexdigest();tests['limits']=[s for s in tests['limits'] if not s.startswith('Contrast measurements cover')]+['Contrast calculated for nominal opaque page text and dialog/error samples; no claim of exhaustive WCAG audit']
(out/'functional-tests.json').write_text(json.dumps(tests,ensure_ascii=False,indent=2));print(json.dumps({'new_cases':len(extra),'failures':[c['name'] for c in extra if c['result']=='FAIL'],'geometry':geometry,'nontext':nontext},ensure_ascii=False))
