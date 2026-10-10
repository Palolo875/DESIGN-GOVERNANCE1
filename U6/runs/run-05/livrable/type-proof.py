from pathlib import Path
import base64
from playwright.sync_api import sync_playwright

root=Path(__file__).parent
fonts={n:base64.b64encode(Path('/workspace/remesure-phase5/moyens/'+f).read_bytes()).decode() for n,f in [('Manrope','manrope.ttf'),('Instrument','instrument-serif.ttf')]}
css=''.join(f"@font-face{{font-family:{n};src:url(data:font/ttf;base64,{v})}}" for n,v in fonts.items())
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':900})
 page.set_content(f'''<style>{css}body{{background:#f3f2e9;color:#192b28;padding:40px}}section{{border-bottom:1px solid;padding:20px}}p{{font:16px Manrope}}h1{{font-size:80px;line-height:1.02;margin:20px 0;width:1100px}}</style><section><p>Manrope · graisse 800</p><h1 style="font-family:Manrope;font-weight:800">La route<br>vous attend.</h1></section><section><p>Instrument Serif · romain</p><h1 style="font-family:Instrument;font-weight:400">La route<br>vous attend.</h1></section>''')
 page.evaluate('document.fonts.ready')
 page.screenshot(path=str(root/'captures/typography.png'),full_page=True)
 browser.close()
