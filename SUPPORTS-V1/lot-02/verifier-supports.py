"""Observe les trois pages livrées ; aucune règle de composition injectée."""
import hashlib,http.server,json,os,re,threading
from datetime import datetime,timezone
from functools import partial
from pathlib import Path
from xml.etree import ElementTree as ET
from playwright.sync_api import sync_playwright

ROOT=Path(os.environ.get('DG_SUPPORTS_REPO','/workspace/DESIGN-GOVERNANCE1'))
OUT=Path(__file__).parent/'preuves';OUT.mkdir(exist_ok=True)
maps=[json.loads((ROOT/'supports'/f'{name}.json').read_text()) for name in ['systeme','parcours','boucle']]
results=[];errors=[];requests=[];contrasts=[]
class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start();url=f'http://127.0.0.1:{server.server_port}/'

def record(name,fn):
    try:
        evidence=fn() or {};results.append({'name':name,'result':'PASS','evidence':evidence});print('PASS',name,flush=True)
    except Exception as exc:
        results.append({'name':name,'result':'FAIL','error':str(exc)});print('FAIL',name,str(exc),flush=True)

def ratio(a,b):
    def lum(color):
        vals=[float(x)/255 for x in re.findall(r'[\d.]+',color)[:3]]
        assert len(vals)==3,color
        vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals]
        return sum(v*w for v,w in zip(vals,[.2126,.7152,.0722]))
    x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)

def geometry(page):
    return page.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth})')

try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=os.environ.get('DG_BROWSER_EXECUTABLE','/usr/bin/chromium'),headless=True);version=browser.version
        def open_page(data,width=1440,dark=False,js=True):
            context=browser.new_context(viewport={'width':width,'height':1000},color_scheme='dark' if dark else 'light',java_script_enabled=js,reduced_motion='reduce',accept_downloads=True)
            page=context.new_page();page.on('pageerror',lambda e:errors.append(str(e)));page.on('request',lambda r:requests.append(r.url));page.goto(url+'supports/'+data['file']);page.evaluate('document.fonts.ready');return context,page
        for data in maps:
            for width in [320,390,768,1024,1280,1440]:
                for dark in [False,True]:
                    def nominal(data=data,width=width,dark=dark):
                        context,page=open_page(data,width,dark)
                        try:
                            size=geometry(page);assert size['scroll']<=width+1 and size['body']<=width+1,size
                            assert page.locator('h1').inner_text().replace('\n',' ')==' '.join(data['title'].splitlines())
                            assert page.locator('.diagram-svg').is_visible()==(width>=1200)
                            assert page.locator('h1').evaluate('(h)=>parseFloat(getComputedStyle(h).fontSize)')>=28
                            if data['id']=='boucle' and width>=1200:assert page.locator('svg [data-feedback]').count()==1
                            assert page.locator('html').get_attribute('data-theme')==('sombre' if dark else 'clair')
                            assert page.evaluate('document.fonts.check("600 16px Manrope")')
                            assert page.locator('.map-nav [aria-current=page]').count()==1
                            if width in [320,390,1440]:
                                page.screenshot(path=str(OUT/f"{data['id']}-{width}-{'sombre' if dark else 'clair'}.png"),full_page=True)
                                if width==320:page.screenshot(path=str(OUT/f"{data['id']}-320-premiere-{'sombre' if dark else 'clair'}.png"))
                            if width==1440:
                                colors=page.locator('svg').evaluate("svg=>[...svg.querySelectorAll('text')].map(t=>{let q=t.parentElement.querySelector(':scope > rect')||svg.querySelector(':scope > rect'),b=t.getBBox();return {text:t.textContent,fg:getComputedStyle(t).fill,bg:getComputedStyle(q).fill,bounds:{x:+q.getAttribute('x')||0,y:+q.getAttribute('y')||0,width:+q.getAttribute('width'),height:+q.getAttribute('height')},box:{x:b.x,y:b.y,width:b.width,height:b.height}}})")
                                for row in colors:
                                    b,q=row['box'],row['bounds'];assert b['x']>=q['x']-1 and b['x']+b['width']<=q['x']+q['width']+1,('largeur',row['text'])
                                    assert b['y']>=q['y']-1 and b['y']+b['height']<=q['y']+q['height']+1,('hauteur',row['text'],b,q)
                                    assert ratio(row['fg'],row['bg'])>=4.5,('contraste',row['text'])
                                contrasts.append({'map':data['id'],'theme':'sombre' if dark else 'clair','minimum':min(ratio(c['fg'],c['bg']) for c in colors),'pairs':colors})
                            return {'geometry':size,'layout':'SVG' if width>=1200 else 'texte recomposé'}
                        finally:context.close()
                    record(f"{data['id']} / {width} / {'sombre' if dark else 'clair'}",nominal)
            context,page=open_page(data)
            try:
                for entry in data['entries'][1:]:
                    def choose(entry=entry):
                        control=page.get_by_role('combobox');control.focus();control.select_option(entry['id'])
                        assert page.locator('#entry-title').inner_text()==entry['title']
                        assert page.locator('#entry-link').get_attribute('href')=='../'+entry['target']
                        assert (ROOT/entry['target'].split('#')[0]).is_file()
                        active=page.locator('svg [data-node].highlighted').evaluate_all('(nodes)=>nodes.map(n=>n.dataset.node)');assert sorted(active)==sorted(entry['focus'])
                        assert page.locator('svg [data-node]').count()==len(data['nodes'])
                        assert page.evaluate('document.activeElement.id')=='entry'
                        return {'target':entry['target'],'highlighted':active,'context_preserved':True}
                    record(f"{data['id']} / choix / {entry['id']}",choose)
            finally:context.close()
            def keyboard(data=data):
                context,page=open_page(data,390)
                try:
                    page.get_by_role('button',name='Thème sombre').focus();page.keyboard.press('Space');assert page.locator('html').get_attribute('data-theme')=='sombre'
                    page.get_by_role('combobox').focus();page.keyboard.press('ArrowDown');page.keyboard.press('Enter');assert page.locator('#entry-title').inner_text()==data['entries'][1]['title']
                    page.get_by_text('Lire la carte en texte',exact=True).focus();page.keyboard.press('Enter');assert page.locator('#equivalent').get_attribute('open') is not None
                    page.screenshot(path=str(OUT/(data['id']+'-390-clavier.png')),full_page=True)
                    return {'theme':'sombre','native_selection':True,'text_open':True}
                finally:context.close()
            record(data['id']+' / clavier',keyboard)
            def exported(data=data):
                context,page=open_page(data,390)
                try:
                    page.get_by_role('button',name='Thème sombre').click();page.get_by_role('combobox').select_option(data['entries'][1]['id'])
                    with page.expect_download() as event:page.get_by_role('button',name='Exporter cette vue en SVG').click()
                    download=event.value;path=OUT/download.suggested_filename;download.save_as(path)
                    svg=ET.fromstring(path.read_text());assert svg.attrib['data-theme']=='sombre'
                    assert svg.find('{http://www.w3.org/2000/svg}metadata').text==(ROOT/'supports/fonts/OFL-manrope.txt').read_text()
                    relative=Path('supports')/('export-'+data['id']+'.svg');local=ROOT/relative;local.write_bytes(path.read_bytes())
                    try:
                        page.set_viewport_size({'width':1104,'height':int(svg.attrib['height'])});page.goto(url+str(relative));page.evaluate('document.fonts.ready');assert page.locator('svg').count()==1
                        page.screenshot(path=str(OUT/(data['id']+'-export.png')))
                    finally:local.unlink()
                    return {'file':download.suggested_filename,'reopened':True,'license_preserved':True}
                finally:context.close()
            record(data['id']+' / export sélectionné puis rouvert',exported)
            for width in [320,390]:
                def enlarged(data=data,width=width):
                    context,page=open_page(data,width)
                    try:
                        page.add_style_tag(content='p,a,label,summary,select,button,.node-meta,.path,.scope,.footer,.brand small{font-size:32px!important;line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}h1{font-size:56px!important;line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}')
                        size=geometry(page);assert size['scroll']<=width+1 and size['body']<=width+1,size
                        page.screenshot(path=str(OUT/f"{data['id']}-{width}-texte-agrandi.png"),full_page=True)
                        return {'geometry':size,'scope':'texte et espacement agrandis, aucune grille ni règle de wrapping injectée ; pas zoom navigateur'}
                    finally:context.close()
                record(f"{data['id']} / {width} / texte agrandi",enlarged)
            def no_script(data=data):
                context,page=open_page(data,390,js=False)
                try:
                    assert page.get_by_role('combobox').is_disabled();assert page.locator('.diagram-html').is_visible()
                    page.get_by_text('Lire la carte en texte',exact=True).click();assert page.locator('#equivalent .text').is_visible()
                    for a in page.locator('a').all():
                        target=a.get_attribute('href');assert (ROOT/'supports'/target).resolve().is_file(),target
                    return {'content':True,'sources':True,'controls_disabled':True}
                finally:context.close()
            record(data['id']+' / JavaScript absent',no_script)
            for theme in ['clair','sombre']:
                def autonomous(data=data,theme=theme):
                    native=ET.fromstring((ROOT/'supports'/f"{data['id']}-{theme}.svg").read_text());context=browser.new_context(viewport={'width':1104,'height':int(native.attrib['height'])},device_scale_factor=2);page=context.new_page()
                    try:
                        page.goto(url+f"supports/{data['id']}-{theme}.svg");page.evaluate('document.fonts.ready');assert page.evaluate('document.fonts.check("600 16px Manrope")')
                        page.screenshot(path=str(OUT/f"{data['id']}-{theme}.png"))
                        return {'opened':True,'font_loaded':True}
                    finally:context.close()
                record(f"{data['id']} / SVG autonome / {theme}",autonomous)
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
external=[r for r in requests if not r.startswith(url) and not r.startswith('data:')]
results.append({'name':'Dépendances et erreurs','result':'PASS' if not errors and not external else 'FAIL','evidence':{'external':external,'errors':errors}})
report={'observed_at':datetime.now(timezone.utc).isoformat(),'browser':version,'artifact_sha256':{d['file']:hashlib.sha256((ROOT/'supports'/d['file']).read_bytes()).hexdigest() for d in maps},'server_stopped':not thread.is_alive(),'results':results,'passed':sum(r['result']=='PASS' for r in results),'failed':sum(r['result']=='FAIL' for r in results),'svg_contrasts':contrasts,'limits':['Chromium et émulation, pas téléphone physique ni lecteur d’écran observé.','Compréhension et préférence humaine non mesurées ; pas certification exhaustive.']}
(OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Résultat :',report['passed'],'PASS,',report['failed'],'FAIL',flush=True)
raise SystemExit(bool(report['failed']))
