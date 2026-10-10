from pathlib import Path
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread
from functools import partial
from playwright.sync_api import sync_playwright
import base64, json, sys

ROOT=Path(__file__).resolve().parent
class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(QuietHandler,directory=str(ROOT)))
thread=Thread(target=server.serve_forever,daemon=True);thread.start()
url=f'http://127.0.0.1:{server.server_port}/index.html'
tag=sys.argv[1] if len(sys.argv)>1 else 'before'
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
        page=browser.new_page(viewport={'width':1440,'height':1000},device_scale_factor=1)
        errors=[];page.on('pageerror',lambda e: errors.append(str(e)))
        for width,height in [(1440,1000),(390,844),(320,844)]:
            page.set_viewport_size({'width':width,'height':height})
            page.goto(url);page.evaluate('document.fonts.ready');page.screenshot(path=str(ROOT/'captures'/f'{tag}-{width}-full.png'),full_page=True)
            if width!=320: page.screenshot(path=str(ROOT/'captures'/f'{tag}-{width}-first.png'))
            print(json.dumps({'width':width,'scrollWidth':page.evaluate('document.documentElement.scrollWidth'),'viewport':page.evaluate('innerWidth'),'h1':page.locator('h1').bounding_box(),'errors':errors}))
        if tag=='before':
            manrope=base64.b64encode(Path('/workspace/remesure-phase5/moyens/manrope.ttf').read_bytes()).decode()
            serif=base64.b64encode(Path('/workspace/remesure-phase5/moyens/instrument-serif.ttf').read_bytes()).decode()
            page.set_viewport_size({'width':1440,'height':760})
            page.set_content('''<style>@font-face{font-family:M;src:url(data:font/ttf;base64,'''+manrope+''')}@font-face{font-family:I;src:url(data:font/ttf;base64,'''+serif+''')}*{box-sizing:border-box}body{margin:0;background:#e8f1ed;color:#173c32;display:flex;padding:60px;gap:80px}.sample{width:600px}small{font:14px M}h1{font-weight:600;letter-spacing:-3.4px;line-height:1.07;font-size:66px;font-family:M;margin-top:50px}.serif h1{font-family:I;font-weight:400;letter-spacing:-.5px;font-size:78px}p{font:17px/1.8 M;max-width:440px}button{font:700 14px M;background:#173c32;color:white;padding:18px;border:0;border-radius:6px}</style><section class="sample"><small>A / Manrope · titre 66 px</small><h1>Le projet est livré.<br>La facture aussi.</h1><p>Votre travail mérite une suite simple. Préparez une facture claire, retrouvez chaque montant et gardez le fil jusqu’au règlement.</p><button>Essayer la facture ↗</button></section><section class="sample serif"><small>B / Instrument Serif · titre 78 px</small><h1>Le projet est livré.<br>La facture aussi.</h1><p>Votre travail mérite une suite simple. Préparez une facture claire, retrouvez chaque montant et gardez le fil jusqu’au règlement.</p><button>Essayer la facture ↗</button></section>''')
            page.evaluate('document.fonts.ready');page.screenshot(path=str(ROOT/'captures'/'type-study.png'))
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
