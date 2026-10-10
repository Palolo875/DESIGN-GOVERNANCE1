import http.server,threading,re,json,os
from pathlib import Path
from functools import partial
from playwright.sync_api import sync_playwright
ROOT=Path('/workspace/DESIGN-GOVERNANCE1');OUT=Path(__file__).parent
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();base=f'http://127.0.0.1:{server.server_port}/'
results=[]
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True)
        for name,stem in [('README.md','systeme'),('design/README.md','boucle'),('agent/skill/references/flow.md','parcours')]:
            picture=re.search(r'<a href="[^"]+">\s*<picture>.*?</picture>\s*</a>',(ROOT/name).read_text(),re.S).group()
            for theme in ['light','dark']:
                context=browser.new_context(color_scheme=theme,viewport={'width':1104,'height':1250});page=context.new_page()
                page.set_content('<base href="'+base+str(Path(name).parent)+'/"><style>body{margin:0}img{max-width:100%;height:auto}</style>'+picture)
                page.wait_for_function('document.querySelector("img").complete && document.querySelector("img").naturalWidth>0')
                expected=stem+('-sombre.svg' if theme=='dark' else '-clair.svg')
                current=page.locator('img').evaluate('(image)=>image.currentSrc');assert current.endswith('/supports/'+expected),current
                target=page.locator('a').get_attribute('href');assert target.endswith(stem+'.md')
                page.screenshot(path=str(OUT/(stem+'-picture-'+theme+'.png')),full_page=True)
                results.append({'document':name,'theme':theme,'selected':expected,'link':target,'result':'PASS'})
                context.close()
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
(OUT/'picture.json').write_text(json.dumps({'checks':results,'server_stopped':not thread.is_alive(),'scope':'Structure conservée par le moteur Markdown GitHub ; sélection native du navigateur observée sous Chromium, sans prétendre auditer toute l’interface GitHub.'},ensure_ascii=False,indent=2)+'\n')
print('PICTURE PASSED — six sélections de thème et trois destinations Markdown')
