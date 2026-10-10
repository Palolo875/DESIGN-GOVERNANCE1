#!/usr/bin/env python3
"""Parcours, reflow, fontes, contrastes et export réellement ouverts dans Chromium."""
import hashlib
import http.server
import json
import os
import re
import subprocess
import threading
from datetime import datetime, timezone
from functools import partial
from pathlib import Path
from xml.etree import ElementTree as ET
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'preuves';OUT.mkdir(exist_ok=True)
DATA=json.loads((ROOT/'carte.json').read_text())
EXECUTABLE=os.environ.get('DG_BROWSER_EXECUTABLE','/usr/bin/chromium')
REPO=Path(os.environ.get('DG_SOURCE_REPO',next((str(p) for p in ROOT.parents if (p/'.git').exists()),'/workspace/DESIGN-GOVERNANCE1')))
BASE='https://github.com/Palolo875/DESIGN-GOVERNANCE1/blob/'+DATA['base_commit']+'/'
results=[];errors=[];requests=[];contrasts=[]


class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*args):pass


def rgb(value):
    if value.startswith('#'):return [int(value[i:i+2],16)/255 for i in [1,3,5]]
    vals=[float(x) for x in re.findall(r'[\d.]+',value)];assert len(vals)>=3,value
    assert len(vals)<4 or vals[3]==1,value
    return [v/255 for v in vals[:3]]


def contrast(a,b):
    def lum(color):
        vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in rgb(color)]
        return sum(v*w for v,w in zip(vals,[.2126,.7152,.0722]))
    x,y=sorted([lum(a),lum(b)]);return (y+.05)/(x+.05)


def record(name,fn):
    try:
        evidence=fn() or {};results.append({'name':name,'result':'PASS','evidence':evidence});print('PASS',name,flush=True)
    except Exception as exc:
        results.append({'name':name,'result':'FAIL','error':str(exc)});print('FAIL',name,str(exc),flush=True)


def overflow(page):
    return page.evaluate('({width:innerWidth,scroll:document.documentElement.scrollWidth,body:document.body.scrollWidth})')


server=http.server.ThreadingHTTPServer(('127.0.0.1',0),partial(Handler,directory=str(ROOT)))
thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
URL=f'http://127.0.0.1:{server.server_port}/'
try:
    with sync_playwright() as p:
        browser=p.chromium.launch(executable_path=EXECUTABLE,headless=True);version=browser.version
        def page_for(width=1440,height=1000,dark=False,js=True):
            context=browser.new_context(viewport={'width':width,'height':height},color_scheme='dark' if dark else 'light',reduced_motion='reduce',java_script_enabled=js,accept_downloads=True)
            page=context.new_page();page.on('pageerror',lambda error:errors.append(str(error)));page.on('request',lambda request:requests.append(request.url));page.goto(URL+'index.html');page.evaluate('document.fonts.ready');return context,page
        for width in [1440,1280,1024,768,390,320]:
            for dark in [False,True]:
                def nominal(width=width,dark=dark):
                    context,page=page_for(width,dark=dark)
                    try:
                        size=overflow(page);assert size['scroll']<=width+1,size;assert size['body']<=width+1,size
                        assert page.evaluate('document.fonts.check("600 16px Manrope")')
                        svg_visible=page.locator('.diagram-svg').is_visible();assert svg_visible==(width>=1200)
                        if not svg_visible:
                            assert page.locator('.diagram-html .design').is_visible()
                            assert page.locator('.diagram-html .authority').is_visible()
                        assert page.get_by_role('heading',name='Les responsabilités reliées').is_visible()
                        assert page.locator('html').get_attribute('data-theme')==('sombre' if dark else 'clair')
                        if width in [1440,390,320]:page.screenshot(path=str(OUT/(f'{width}-'+('sombre' if dark else 'clair')+'.png')),full_page=True)
                        if width==1440:
                            pairs=page.locator('#responsibility-map').evaluate('''svg=>[...svg.querySelectorAll('text')].map(t=>{let rect=t.parentElement.querySelector(':scope > rect');if(!rect)rect=svg.querySelector(':scope > rect');return {text:t.textContent,fg:getComputedStyle(t).fill,bg:getComputedStyle(rect).fill,bbox:{x:t.getBBox().x,y:t.getBBox().y,width:t.getBBox().width,height:t.getBBox().height},bounds:{x:+rect.getAttribute('x')||0,y:+rect.getAttribute('y')||0,width:+rect.getAttribute('width'),height:+rect.getAttribute('height')}}})''')
                            for pair in pairs:
                                ratio=contrast(pair['fg'],pair['bg']);assert ratio>=4.5,(pair['text'],ratio)
                                b,q=pair['bbox'],pair['bounds'];assert b['x']>=q['x']-1 and b['x']+b['width']<=q['x']+q['width']+1,('texte déborde',pair)
                            contrasts.append({'theme':'sombre' if dark else 'clair','minimum':min(contrast(x['fg'],x['bg']) for x in pairs),'pairs':pairs})
                        return {'geometry':size,'layout':'SVG' if svg_visible else 'recomposé','fonts':True}
                    finally:context.close()
                record(f'{width} / '+('sombre' if dark else 'clair')+' / rendu',nominal)
        context,page=page_for()
        try:
            for entry in DATA['entries'][1:]:
                def route(entry=entry):
                    page.get_by_label('Votre entrée').focus()
                    page.get_by_label('Votre entrée').select_option(entry['id'])
                    assert page.locator('#entry-link').get_attribute('href')==BASE+entry['target']
                    assert page.locator('#entry-title').inner_text()==entry['title']
                    active=page.locator('svg [data-node].highlighted').evaluate_all('(nodes)=>nodes.map(n=>n.dataset.node)');assert sorted(active)==sorted(entry['focus'])
                    assert page.locator('svg [data-node]').count()==5
                    assert page.evaluate('document.activeElement.id')=='entry', 'Le choix a déplacé le focus'
                    source=subprocess.run(['git','-C',str(REPO),'cat-file','-e',DATA['base_commit']+':'+entry['target']],capture_output=True,text=True)
                    assert source.returncode==0,entry['target']+': '+source.stderr
                    return {'entry':entry['label'],'target':entry['target'],'highlighted':active,'all_parts_present':True}
                record('Entrée : '+entry['label'],route)
            def keyboard():
                page.get_by_role('button',name='Thème sombre').focus();page.keyboard.press('Space');assert page.locator('html').get_attribute('data-theme')=='sombre';assert page.locator('svg').get_attribute('data-theme')=='sombre'
                page.keyboard.press('Tab');assert page.evaluate('document.activeElement.id')=='entry';page.keyboard.press('Home');page.keyboard.press('Enter');assert page.locator('#entry-title').inner_text()==DATA['entries'][0]['title']
                page.get_by_text('Lire la carte en texte',exact=True).focus();page.keyboard.press('Enter');assert page.locator('#equivalent').get_attribute('open') is not None
                assert page.locator('.text').is_visible()
                return {'theme':'sombre','text_open':True,'native_keyboard':True}
            record('Clavier : thème, entrée, équivalent textuel',keyboard)
            def export():
                page.get_by_label('Votre entrée').select_option('agent')
                with page.expect_download() as info:page.get_by_role('button',name='Exporter cette vue en SVG').click()
                download=info.value;target=OUT/'export-agent-sombre.svg';download.save_as(target);assert download.suggested_filename=='carte-systeme-v1-sombre-agent.svg';doc=ET.fromstring(target.read_bytes());assert doc.attrib['data-theme']=='sombre'
                assert doc.find('{http://www.w3.org/2000/svg}metadata').text==(ROOT/'fonts/OFL-manrope.txt').read_text(), 'La licence de la fonte embarquée doit accompagner le SVG'
                exported=browser.new_context(viewport={'width':1104,'height':920});ep=exported.new_page()
                try:
                    ep.goto(URL+'preuves/'+target.name);ep.evaluate('document.fonts.ready');assert ep.locator('svg').get_attribute('data-theme')=='sombre';assert ep.locator('g.highlighted').count()==2;ep.screenshot(path=str(OUT/'export-agent-sombre.png'))
                finally:exported.close()
                return {'name':download.suggested_filename,'svg_reopened':True,'sha256':hashlib.sha256(target.read_bytes()).hexdigest()}
            record('Export de la vue sélectionnée, puis ouverture du SVG',export)
            page.get_by_label('Votre entrée').select_option('overview')
            (OUT/'noms-accessibles.txt').write_text(page.locator('body').aria_snapshot())
        finally:context.close()
        for width in [390,320]:
            def reflow(width=width):
                context,page=page_for(width)
                try:
                    page.add_style_tag(content='body,button,select{font-size:32px!important}p,a,span,label,small,summary,h3,h4{font-size:32px!important;line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}h1{font-size:56px!important;line-height:1.5!important;letter-spacing:.12em!important;word-spacing:.16em!important}h1 span{font-size:inherit!important}')
                    size=overflow(page);assert size['scroll']<=width+1,size
                    page.screenshot(path=str(OUT/f'{width}-texte-agrandi.png'),full_page=True)
                    return {'geometry':size,'scope':'texte porté à 32 px et titre à 56 px avec espacements renforcés ; aucun changement de grille ou de wrapping ajouté par la mesure, pas zoom navigateur'}
                finally:context.close()
            record(f'{width} / texte agrandi et espacé',reflow)
        def no_js():
            context,page=page_for(390,js=False)
            try:
                assert page.locator('.diagram-html .design').is_visible();assert page.locator('noscript').is_visible();assert page.get_by_label('Votre entrée').is_disabled()
                page.get_by_text('Lire la carte en texte',exact=True).click();assert page.locator('.text').is_visible()
                return {'content':True,'source_links':page.locator('.reading a').count(),'interactive_controls_disabled':True}
            finally:context.close()
        record('JavaScript absent : carte, texte et sources accessibles',no_js)
        def fallback_font():
            context,page=page_for(390)
            try:
                page.add_style_tag(content='*{font-family:Arial,sans-serif!important}')
                size=overflow(page);assert size['scroll']<=391,size;page.screenshot(path=str(OUT/'390-fonte-repli.png'),full_page=True);return {'geometry':size,'family':'Arial'}
            finally:context.close()
        record('Fonte de repli : lecture étroite',fallback_font)
        for theme in ['claire','sombre']:
            def static_export(theme=theme):
                context=browser.new_context(viewport={'width':1104,'height':920},device_scale_factor=2);page=context.new_page()
                try:
                    page.goto(URL+'carte-'+theme+'.svg');page.evaluate('document.fonts.ready');assert page.locator('svg').count()==1;page.screenshot(path=str(ROOT/('carte-'+theme+'.png')));return {'file':'carte-'+theme+'.png','pixels':[2208,1840],'font':page.evaluate('document.fonts.check("600 16px Manrope")')}
                finally:context.close()
            record('SVG autonome '+theme+' : ouverture et export PNG',static_export)
        for width in [1440,390]:
            for family in ['sans','serif']:
                context,page=page_for(width)
                try:
                    if family=='serif':page.goto(URL+'index.html?typo=serif');page.evaluate('document.fonts.ready')
                    page.screenshot(path=str(OUT/f'{width}-titre-{family}.png'))
                finally:context.close()
        browser.close()
finally:
    server.shutdown();server.server_close();thread.join(timeout=3)
external=[u for u in requests if not u.startswith(URL) and not u.startswith('data:')]
results.append({'name':'Dépendances externes et erreurs JavaScript','result':'PASS' if not external and not errors else 'FAIL','evidence':{'external_requests':external,'javascript_errors':errors}})
report={'observed_at':datetime.now(timezone.utc).isoformat(),'browser_executable':EXECUTABLE,'browser_version':version,'artifact_sha256':hashlib.sha256((ROOT/'index.html').read_bytes()).hexdigest(),'server_stopped':not thread.is_alive(),'passed':sum(x['result']=='PASS' for x in results),'failed':sum(x['result']=='FAIL' for x in results),'results':results,'svg_contrasts':contrasts,'limits':['Aucun participant représentatif ni observation de lecteur d’écran.','Chromium seulement ; pas de certification de compréhension ou d’accessibilité exhaustive.','Les captures ne démontrent pas la préférence esthétique du propriétaire.']}
(OUT/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Résultat :',report['passed'],'PASS,',report['failed'],'FAIL',flush=True)
raise SystemExit(bool(report['failed']))
