from pathlib import Path
from playwright.sync_api import sync_playwright
import json
from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from threading import Thread
root=Path(__file__).parent
folder=root/'captures-final-v4';folder.mkdir(exist_ok=True)
class QuietHandler(SimpleHTTPRequestHandler):
 def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(root)))
Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 for name,width,height in [('desktop',1440,1000),('mobile',390,844),('narrow',320,844)]:
  page=browser.new_page(viewport={'width':width,'height':height},device_scale_factor=1)
  errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
  page.goto(url);page.wait_for_function('document.fonts.status==="loaded"')
  page.screenshot(path=str(folder/f'{name}-full.png'),full_page=True)
  page.screenshot(path=str(folder/f'{name}-viewport.png'))
  print(json.dumps({'viewport':name,'scrollWidth':page.evaluate('document.documentElement.scrollWidth'),'innerWidth':width,'errors':errors,'titleBox':page.locator('h1').bounding_box(),'invoiceBox':page.locator('.sheet').bounding_box()},ensure_ascii=False))
  if False:
   page.locator('h1').evaluate("e=>{e.style.fontFamily='Instrument,Georgia,serif';e.style.fontWeight='400';e.style.letterSpacing='-1.6px';e.style.fontSize='76px'}")
   page.screenshot(path=str(folder/'desktop-serif-voice.png'))
  page.close()
 browser.close()
server.shutdown();server.server_close()
