from pathlib import Path
import base64
from playwright.sync_api import sync_playwright
out=Path('/workspace/remesure-phase5/runs/run-03/livrable')
fonts={n:base64.b64encode(Path('/workspace/remesure-phase5/moyens/'+f).read_bytes()).decode() for n,f in [('Manrope','manrope.ttf'),('Instrument','instrument-serif.ttf')]}
css=''.join('@font-face{font-family:'+n+';src:url(data:font/ttf;base64,'+d+')}' for n,d in fonts.items())
html='<style>'+css+'body{background:#f3f6f2;color:#173b32;margin:50px}.sample{width:1050px;padding:28px;border-bottom:1px solid #173b32}p{font:14px sans-serif}h1{font-weight:500;font-size:66px;line-height:1.06;letter-spacing:-2.5px;margin:15px 0}.serif{font-family:Instrument;letter-spacing:0}.sans{font-family:Manrope}</style><div class="sample"><p>Manrope — voix d’outil, 66 px</p><h1 class="sans">Le travail est fait.<br>La facture aussi.</h1></div><div class="sample"><p>Instrument Serif — voix éditoriale, 66 px</p><h1 class="serif">Le travail est fait.<br>La facture aussi.</h1></div>'
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=b.new_page(viewport={'width':1200,'height':640});page.set_content(html);page.evaluate('document.fonts.ready');page.screenshot(path=str(out/'captures/typography.png'));b.close()
