#!/usr/bin/env python3
"""Une source de contenu et de couleurs → page, SVG, Mermaid et texte."""
import base64
import hashlib
import html
import json
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'carte.json').read_text())
BASE = 'https://github.com/Palolo875/DESIGN-GOVERNANCE1/blob/' + DATA['base_commit'] + '/'
FONT = base64.b64encode((ROOT / 'fonts/manrope.ttf').read_bytes()).decode('ascii')
SERIF = base64.b64encode((ROOT / 'fonts/instrument-serif.ttf').read_bytes()).decode('ascii')
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def el(parent, tag, **attrs):
    return ET.SubElement(parent, '{' + NS + '}' + tag, {k.rstrip('_').replace('_', '-'): str(v) for k, v in attrs.items()})


def text(parent, x, y, value, size=18, weight=400, cls='ink', anchor='start'):
    t = el(parent, 'text', x=x, y=y, font_size=size, font_weight=weight, class_=cls, text_anchor=anchor)
    t.text = value
    return t


def box(parent, x, y, w, h, color, radius=8, cls=''):
    attrs = dict(x=x, y=y, width=w, height=h, rx=radius, fill='var(--' + color + ')', stroke='var(--line)', stroke_width=1.3)
    if cls:
        attrs['class_'] = cls
    node = el(parent, 'rect', **attrs)
    return node


def svg(theme):
    root = ET.Element('{' + NS + '}svg', {'viewBox':'0 0 1104 920', 'width':'1104', 'height':'920', 'role':'img', 'aria-labelledby':'map-title map-desc', 'data-theme':theme, 'id':'responsibility-map'})
    el(root, 'title', id='map-title').text = 'Design Governance V1 — carte des responsabilités'
    el(root, 'desc', id='map-desc').text = ' '.join(n['title'] + ' : ' + ' '.join(n['lines'] + n.get('conditions', [])) for n in DATA['nodes']) + ' ' + DATA['authority']['rule'] + ' ' + DATA['authority']['retained'] + ' ' + DATA['scope']
    el(root, 'metadata', id='font-license').text = (ROOT / 'fonts/OFL-manrope.txt').read_text()
    css = '@font-face{font-family:Manrope;src:url(data:font/ttf;base64,' + FONT + ') format("truetype");font-weight:200 800;font-style:normal}'
    for name, palette in DATA['themes'].items():
        css += 'svg[data-theme="' + name + '"]{' + ''.join('--' + k + ':' + v + ';' for k,v in palette.items()) + '}'
    css += 'text{font-family:Manrope,Arial,sans-serif}.ink{fill:var(--text)}.muted{fill:var(--muted)}.accent{fill:var(--accent)}.highlighted>rect{stroke:var(--accent);stroke-width:3}.edge{stroke:var(--line);stroke-width:1.8;fill:none}'
    el(root, 'style').text=css
    defs=el(root,'defs');m=el(defs,'marker',id='arrow',viewBox='0 0 10 10',refX=8,refY=5,markerWidth=7,markerHeight=7,orient='auto-start-reverse');el(m,'path',d='M 1 1 L 8 5 L 1 9',fill='none',stroke='var(--line)',stroke_width=1.5)
    el(root,'rect',width=1104,height=920,fill='var(--page)')
    text(root,32,26,'DESIGN GOVERNANCE / ' + DATA['version'],14,650,'muted')
    text(root,1072,26,'CARTE DE LECTURE',14,650,'muted','end')
    nodes={n['id']:n for n in DATA['nodes']}
    for ident,x in [('guides',32),('agent',576)]:
        n=nodes[ident];g=el(root,'g',id='node-'+ident,data_node=ident);box(g,x,48,496,120,ident)
        text(g,x+24,77,n['role'].upper(),14,700,'muted');text(g,x+24,106,n['title'],26,650)
        text(g,x+472,77,n['path'],14,500,'muted','end')
        text(g,x+24,135,n['lines'][0],17);text(g,x+24,155,n['lines'][1],17)
    for x,label in [(280,DATA['relations'][0]['label']),(824,DATA['relations'][1]['label'])]:
        el(root,'path',d=f'M {x} 168 V 222',class_='edge',marker_end='url(#arrow)').set('class','edge')
        el(root,'rect',x=x-96,y=183,width=192,height=24,fill='var(--page)')
        text(root,x,201,label,15,500,'muted','middle')
    n=nodes['design'];g=el(root,'g',id='node-design',data_node='design');box(g,32,224,1040,228,'design')
    text(g,56,254,n['role'].upper(),14,700,'accent');text(g,56,288,n['title'],32,700)
    text(g,1048,254,n['path'],14,500,'muted','end');text(g,254,288,n['lines'][0],18,400,'muted')
    el(g,'path',d='M 56 308 H 1048',class_='edge').set('class','edge')
    for i,ch in enumerate(n['children']):
        x=56+i*248
        if i:el(g,'path',d=f'M {x-16} 330 V 430',stroke='var(--line)',stroke_width=1)
        text(g,x,344,ch['title'],22,650)
        text(g,x,377,ch['lines'][0],18);text(g,x,402,ch['lines'][1],18)
        text(g,x,430,ch['path'],14,500,'muted')
    el(root,'path',d='M 357 453 V 506',class_='edge',marker_start='url(#arrow)',marker_end='url(#arrow)').set('class','edge')
    el(root,'rect',x=372,y=468,width=294,height=26,fill='var(--page)');text(root,384,486,DATA['relations'][2]['label'],15,500,'muted')
    n=nodes['gouvernance'];g=el(root,'g',id='node-gouvernance',data_node='gouvernance');box(g,32,508,650,192,'gouvernance')
    text(g,56,536,n['role'].upper(),14,700,'muted');text(g,656,536,n['path'],14,500,'muted','end');text(g,56,565,n['title'],26,650)
    text(g,56,593,n['lines'][0],18)
    for i,line in enumerate(n['conditions']):text(g,56,626+i*24,line,16,450)
    n=nodes['maintenance'];g=el(root,'g',id='node-maintenance',data_node='maintenance');box(g,714,508,358,192,'maintenance')
    text(g,738,536,n['role'].upper(),14,700,'muted');text(g,1048,536,n['path'],14,500,'muted','end');text(g,738,565,n['title'],26,650)
    for i,line in enumerate(n['lines']):text(g,738,603+i*26,line,18)
    a=DATA['authority'];g=el(root,'g',id='authority');box(g,32,736,1040,138,'surface')
    text(g,56,772,a['title'],22,650);text(g,56,803,a['rule'],20,550)
    text(g,56,833,a['retained'],16,400,'muted');text(g,56,858,a['derived'],16,400,'muted')
    text(root,32,909,DATA['scope'],15,550,'muted')
    return ET.tostring(root,encoding='unicode')


def link(target, label, cls=''):
    return '<a class="'+cls+'" href="'+html.escape(BASE+target,quote=True)+'">'+html.escape(label)+'</a>'


def cards():
    out=[]
    for n in DATA['nodes']:
        c='<section class="map-node '+n['id']+'" data-node="'+n['id']+'"><div class="node-meta"><span>'+html.escape(n['role'])+'</span><span>'+html.escape(n['path'])+'</span></div><h3>'+html.escape(n['title'])+'</h3>'
        c+='<p>'+'<br>'.join(html.escape(s) for s in n['lines'])+'</p>'
        if n.get('children'):
            c+='<div class="subjects">'+''.join('<div><h4>'+html.escape(ch['title'])+'</h4><p>'+html.escape(' '.join(ch['lines']))+'</p><span class="path">'+html.escape(ch['path'])+'</span></div>' for ch in n['children'])+'</div>'
        if n.get('conditions'):c+='<p class="conditions">'+html.escape(' '.join(n['conditions']))+'</p>'
        c+='</section>';out.append(c)
    a=DATA['authority'];out.append('<section class="authority"><h3>'+html.escape(a['title'])+'</h3><p class="rule">'+html.escape(a['rule'])+'</p><p>'+html.escape(a['retained'])+'</p><p>'+html.escape(a['derived'])+'</p></section>')
    return ''.join(out)


def equivalent():
    a=DATA['authority'];out=['# Carte du système — équivalent textuel','',DATA['version']+'. Proposition de support, dérivée du produit `'+DATA['base_commit']+'`.','',DATA['scope'],'','## Entrées','']
    for e in DATA['entries'][1:]:out.append('- **'+e['label']+'** : ['+e['link']+']('+BASE+e['target']+'). '+e['description'])
    out+=['','## Responsabilités','']
    for n in DATA['nodes']:
        out+=['### '+n['title']+' — '+n['role'].lower(),'', ' '.join(n['lines']), '']
        for ch in n.get('children',[]):out.append('- **'+ch['title']+'** : '+ ' '.join(ch['lines'])+' ['+ch['path']+']('+BASE+ch['target']+').')
        if n.get('conditions'):out+=['',' '.join(n['conditions']),'']
        out.append('Source : ['+n['path']+']('+BASE+n['target']+').');out.append('')
    out+=['## Relations','']
    for e in DATA['relations']:out.append('- '+e['from'].capitalize()+(' ↔ ' if e['kind']=='reciprocal' else ' → ')+e['to'].capitalize()+' : '+e['label']+'.')
    out+=['','La maintenance entretient toutes les parties ; elle ne désigne pas une dernière étape.','','## '+a['title'],'',a['rule'],a['retained'],a['derived'],'','Source : [sommaire des sources]('+BASE+a['target']+').','']
    return '\n'.join(out)


def main():
    clear,dark=svg('clair'),svg('sombre')
    (ROOT/'carte-claire.svg').write_text(clear+'\n');(ROOT/'carte-sombre.svg').write_text(dark+'\n')
    template=(ROOT/'page.template.html').read_text()
    css='@font-face{font-family:Manrope;src:url(data:font/ttf;base64,'+FONT+') format("truetype");font-weight:200 800;font-style:normal}@font-face{font-family:Instrument;src:url(data:font/ttf;base64,'+SERIF+') format("truetype");font-weight:400;font-style:normal}'
    for name,palette in DATA['themes'].items():css+='html[data-theme="'+name+'"]{'+''.join('--'+k+':'+v+';' for k,v in palette.items())+'}'
    entries=''.join('<option value="'+e['id']+'">'+html.escape(e['label'])+'</option>' for e in DATA['entries'])
    all_links=''.join('<li>'+link(e['target'],e['link'])+'<span>'+html.escape(e['description'])+'</span></li>' for e in DATA['entries'][1:])
    roles=''.join('<li><strong>'+html.escape(n['title'])+'</strong> — '+html.escape(' '.join(n['lines']+n.get('conditions',[])))+(' <ul>'+''.join('<li><strong>'+html.escape(c['title'])+'</strong> — '+html.escape(' '.join(c['lines']))+'</li>' for c in n['children'])+'</ul>' if n.get('children') else '')+'</li>' for n in DATA['nodes'])
    entries_json=json.dumps(DATA['entries'],ensure_ascii=False).replace('<','\\u003c')
    for marker,value in {'__FONT_CSS__':css,'__TITLE__':''.join('<span>'+html.escape(part)+'</span>' for part in DATA['title'].split('\n')),'__INTRO__':html.escape(DATA['intro']),'__SVG__':clear,'__CARDS__':cards(),'__ENTRIES__':entries,'__LINKS__':all_links,'__ROLES__':roles,'__ENTRY_JSON__':entries_json,'__BASE__':BASE,'__SCOPE__':html.escape(DATA['scope']),'__AUTHORITY__':' '.join(html.escape(DATA['authority'][k]) for k in ['rule','retained','derived']),'__INITIAL_LINK__':BASE+DATA['entries'][0]['target'],'__INITIAL_TITLE__':html.escape(DATA['entries'][0]['title']),'__INITIAL_DESCRIPTION__':html.escape(DATA['entries'][0]['description']),'__INITIAL_LABEL__':html.escape(DATA['entries'][0]['link']),'__SHA__':DATA['base_commit'][:7]}.items():template=template.replace(marker,value)
    licenses='\n\n'.join((ROOT/'fonts'/name).read_text() for name in ['OFL-manrope.txt','OFL-instrument-serif.txt'])
    template=template.replace('</head>','<!-- Fontes OFL. Licences :\n'+licenses.replace('--','—')+'\n-->\n</head>')
    assert '__' not in template, 'Marqueur de template non remplacé'
    (ROOT/'index.html').write_text(template)
    (ROOT/'equivalent.md').write_text(equivalent())
    mermaid=['%% ' + DATA['scope'],'flowchart TB']
    for n in DATA['nodes']:
        label=n['title']+' · '+n['role'].lower()
        if n.get('children'):label+=' : '+', '.join(c['title'].lower() for c in n['children'])
        mermaid.append('  '+n['id']+'["'+label.replace('"','&quot;')+'"]')
    for edge in DATA['relations']:mermaid.append('  '+edge['from']+(' <-->|' if edge['kind']=='reciprocal' else ' -->|')+edge['label']+'| '+edge['to'])
    mermaid+=['  autorite["'+DATA['authority']['rule']+' '+DATA['authority']['retained']+'"]','']
    (ROOT/'carte.mmd').write_text('\n'.join(mermaid))
    names={'page':'Fond','surface':'Surface de lecture','text':'Texte principal','muted':'Texte secondaire','line':'Frontières et relations','accent':'Mise en évidence','guides':'Guides','agent':'Agent','design':'Design','gouvernance':'Gouvernance','maintenance':'Maintenance','focus':'Focus'}
    language=['# Langage visuel proposé pour les supports','', 'V1 expérimentale. Ce langage concerne les cartes et documents du système. Il n’impose pas de style aux productions des agents.','', '## Composition','', 'Un domaine Design plus large rassemble les quatre matières. Guides et agent sont des accès ; la gouvernance protège risque, preuve et reprise ; la maintenance entretient l’ensemble. Les flèches nomment des relations, pas une séquence imposée.','', 'Bordures fines, plans plats, espaces par responsabilité. Les noms et les fonctions distinguent les parties, en complément de leur couleur. Le petit écran recompose les responsabilités en texte lisible.','', '## Typographie','', 'Manrope sert les titres, labels et descriptions. Les SVG conservent du texte sélectionnable et la fonte embarquée, avec sa licence. Une comparaison du titre avec Instrument Serif est conservée dans les captures ; le choix de la voix reste une proposition à discuter.','', 'SVG : titre 32, rôle 14, domaine 26, matière 22, description 18, métadonnée 14 pixels à la taille native 1104 × 920. La page recompose ces rôles selon le viewport ; les contrôles natifs gardent un focus visible.','', '## Couleurs par rôle','', '| Rôle | Clair | Sombre |','|---|---|---|']
    for key,label in names.items():language.append('| '+label+' | `'+DATA['themes']['clair'][key]+'` | `'+DATA['themes']['sombre'][key]+'` |')
    language+=['','## Construction et preuve','','`carte.json` possède le contenu, les relations et les couleurs. `construire.py` génère page, SVG, équivalent textuel, Mermaid et cette fiche. Une modification partagée se fait dans cette source puis se régénère. Les résultats observés sont conservés dans `preuves/verification.json`, avec l’empreinte du HTML et le scope.','']
    (ROOT/'langage-visuel.md').write_text('\n'.join(language))
    outputs=['index.html','carte-claire.svg','carte-sombre.svg','equivalent.md','carte.mmd','langage-visuel.md']
    manifest={name:hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in outputs}
    (ROOT/'construction.json').write_text(json.dumps({'base_commit':DATA['base_commit'],'source_sha256':hashlib.sha256((ROOT/'carte.json').read_bytes()).hexdigest(),'outputs':manifest},indent=2)+'\n')
    print('Carte construite : page, deux SVG, équivalent textuel, Mermaid et empreintes.')


if __name__=='__main__':main()
