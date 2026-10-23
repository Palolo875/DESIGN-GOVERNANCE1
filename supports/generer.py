#!/usr/bin/env python3
"""Supports dérivés : une source par carte, une palette, trois formats."""
import base64
import hashlib
import html
import json
from html.parser import HTMLParser
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
DATA = json.loads((ROOT / 'systeme.json').read_text())
# La version affichée vient du manifeste du paquet, source unique ; aucune carte ne déclare la sienne.
VERSION_LABEL = 'V' + json.loads((ROOT.parent / 'scripts' / 'package_manifest.json').read_text())['version'] + ' expérimentale'
# Le dessin de la carte système place ses flèches à des positions fixes : les relations du JSON doivent suivre cette topologie.
DRAWN_RELATIONS = [('guides', 'design'), ('agent', 'design'), ('design', 'gouvernance')]
BASE = '../'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)


def font_css(embed_font=True):
    if not embed_font:
        return ''
    font = base64.b64encode((ROOT / 'fonts/manrope-supports.woff2').read_bytes()).decode('ascii')
    return '@font-face{font-family:Manrope;src:url(data:font/woff2;base64,' + font + ') format("woff2");font-weight:200 800;font-style:normal}'

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


def svg(theme, embed_font=True):
    root = ET.Element('{' + NS + '}svg', {'viewBox':'0 0 1104 920', 'width':'1104', 'height':'920', 'role':'img', 'aria-labelledby':'map-title map-desc', 'data-theme':theme, 'id':'responsibility-map'})
    el(root, 'title', id='map-title').text = 'Design Governance V1 — carte des responsabilités'
    el(root, 'desc', id='map-desc').text = ' '.join(n['title'] + ' : ' + ' '.join(n['lines'] + n.get('conditions', [])) for n in DATA['nodes']) + ' ' + DATA['authority']['rule'] + ' ' + DATA['authority']['retained'] + ' ' + DATA['scope']
    el(root, 'metadata', id='font-license').text = (ROOT / 'fonts/OFL-manrope.txt').read_text()
    css = font_css(embed_font)
    for name, palette in DATA['themes'].items():
        css += 'svg[data-theme="' + name + '"]{' + ''.join('--' + k + ':' + v + ';' for k,v in palette.items()) + '}'
    css += 'text{font-family:Manrope,Arial,sans-serif}.ink{fill:var(--text)}.muted{fill:var(--muted)}.accent{fill:var(--accent)}.highlighted>rect{stroke:var(--accent);stroke-width:3}.edge{stroke:var(--line);stroke-width:1.8;fill:none}'
    el(root, 'style').text=css
    defs=el(root,'defs');m=el(defs,'marker',id='arrow',viewBox='0 0 10 10',refX=8,refY=5,markerWidth=7,markerHeight=7,orient='auto-start-reverse');el(m,'path',d='M 1 1 L 8 5 L 1 9',fill='none',stroke='var(--line)',stroke_width=1.5)
    el(root,'rect',width=1104,height=920,fill='var(--page)')
    text(root,32,26,'DESIGN GOVERNANCE / ' + VERSION_LABEL,14,650,'muted')
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
    text(g,56,593,n['lines'][0],18);text(g,56,615,n['lines'][1],15)
    for i,line in enumerate(n['conditions']):text(g,56,642+i*24,line,16,450)
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


def sequence_svg(data, theme, embed_font=True):
    start = 264 if data['id'] == 'boucle' else 80
    height = start + 6 * 120 + 152
    root = ET.Element('{' + NS + '}svg', {'viewBox': f'0 0 1104 {height}', 'width': '1104', 'height': str(height), 'role': 'img', 'aria-labelledby': 'map-title map-desc', 'data-theme': theme, 'id': 'responsibility-map'})
    el(root, 'title', id='map-title').text = data['title'].replace('\n', ' ')
    el(root, 'desc', id='map-desc').text = ' '.join(n['title'] + ' : ' + ' '.join(n['lines']) for n in data['nodes']) + ' ' + data['scope']
    el(root, 'metadata', id='font-license').text = (ROOT / 'fonts/OFL-manrope.txt').read_text()
    style = svg(theme, embed_font)
    original = ET.fromstring(style)
    root.append(original.find('{' + NS + '}style'))
    root.append(original.find('{' + NS + '}defs'))
    el(root, 'rect', width=1104, height=height, fill='var(--page)')
    text(root, 32, 26, 'DESIGN GOVERNANCE / ' + VERSION_LABEL, 14, 650, 'muted')
    text(root, 1072, 26, 'CARTE ' + data['number'], 14, 650, 'muted', 'end')
    if data.get('creation'):
        n = data['creation']; g = el(root, 'g'); box(g, 32, 60, 1040, 154, 'design')
        text(g, 56, 94, 'CRÉER', 14, 700, 'accent'); text(g, 56, 132, n['title'], 26, 650)
        for i, line in enumerate(n['lines']): text(g, 56, 166 + i * 25, line, 17)
        el(root, 'path', d='M 357 214 V 258', class_='edge', marker_end='url(#arrow)')
        text(root, 390, 244, 'puis observer et corriger', 15, 500, 'muted')
    for i, n in enumerate(data['nodes']):
        y = start + i * 120; g = el(root, 'g', data_node=n['id'])
        box(g, 32, y, 650, 108, n['color'])
        text(g, 56, y + 24, n['role'].upper(), 13, 700, 'accent')
        text(g, 56, y + 54, n['title'], 22, 650)
        for j, line in enumerate(n['lines']): text(g, 56, y + 78 + j * 22, line, 17)
        if i < len(data['nodes']) - 1:
            el(root, 'path', d=f'M 357 {y + 108} V {y + 119}', class_='edge', marker_end='url(#arrow)')
    for i, n in enumerate(data['panels']):
        y = start + i * 216; g = el(root, 'g'); box(g, 714, y, 358, 196, n['color'])
        text(g, 738, y + 34, n['title'], 20, 650)
        for j, line in enumerate(n['lines']): text(g, 738, y + 70 + j * 25, line, 16)
    if data.get('feedback'):
        branch = data['feedback']
        positions = {n['id']: start + i * 120 + 54 for i, n in enumerate(data['nodes'])}
        el(root, 'path', d=f"M 32 {positions[branch['from']]} H 16 V {positions[branch['to']]} H 31", class_='edge', stroke_dasharray='4 3', marker_end='url(#arrow)', data_feedback='diagnostic')
        text(root, 56, start + 6 * 120 + 6, branch['label'], 14, 650, 'muted')
    y = start + 6 * 120 + 20; n = data['foot']; g = el(root, 'g'); box(g, 32, y, 1040, 96, 'agent')
    text(g, 56, y + 32, n['title'], 22, 650)
    for i, line in enumerate(n['lines']): text(g, 56, y + 59 + i * 23, line, 17)
    text(root, 32, height - 12, data['scope'], 14, 500, 'muted')
    return ET.tostring(root, encoding='unicode')


def sequence_cards(data):
    parts = []
    def context(node, cls):
        return '<section class="' + cls + '"><h3>' + html.escape(node['title']) + '</h3><p>' + html.escape(' '.join(node['lines'])) + '</p>' + ('<p class="source-line">' + link(node['target'], 'Lire la section propriétaire') + '</p>' if node.get('target') else '') + '</section>'
    if data.get('creation'): parts.append(context(data['creation'], 'creation'))
    parts.append('<ol class="stage-list">')
    for n in data['nodes']:
        parts.append('<li><section class="map-node ' + n['color'] + '" data-node="' + n['id'] + '"><div class="node-meta">' + html.escape(n['role']) + '</div><h3>' + html.escape(n['title']) + '</h3><p>' + html.escape(' '.join(n['lines'])) + '</p><p class="source-line">' + link(n['target'], 'Lire la section propriétaire') + '</p></section></li>')
    parts.append('</ol>')
    if data.get('feedback'):
        parts.append('<p class="context-foot">' + html.escape(data['feedback']['label']) + '</p>')
    parts.append('<div class="context-panels">')
    for n in data['panels']: parts.append(context(n, 'map-node ' + n['color']))
    parts.append('</div>' + context(data['foot'], 'context-foot'))
    return ''.join(parts)


def text_sections(data):
    nodes = data['nodes'] + data.get('panels', [])
    if data.get('creation'): nodes = [data['creation']] + nodes
    if data.get('foot'): nodes = nodes + [data['foot']]
    if data.get('feedback'): nodes = nodes + [{'title': 'Retour au diagnostic', 'lines': [data['feedback']['label']]}]
    return nodes


def equivalent(data):
    out = ['# ' + data['title'].replace('\n', ' '), '', VERSION_LABEL + '. Vue dérivée : les sections propriétaires font foi.', '', data['scope'], '']
    for n in text_sections(data):
        out += ['## ' + n.get('role', n['title']), '', '**' + n['title'] + ('** ' if n['title'].rstrip()[-1:] in '.!?…' else '**. ') + ' '.join(n['lines'] + n.get('conditions', [])), '']
        for child in n.get('children', []):
            out.append('- **' + child['title'] + '** : ' + ' '.join(child['lines']) + ' [Source](' + BASE + child['target'] + ').')
        if n.get('target'): out += ['', ('[Entrée](' if n.get('entree') else '[Section propriétaire](') + BASE + n['target'] + ').', '']  # une entrée oriente, sans autorité
    if data.get('relations'):
        out += ['## Relations', '']
        for e in data['relations']: out.append('- ' + e['from'].capitalize() + (' ↔ ' if e['kind'] == 'reciprocal' else ' → ') + e['to'].capitalize() + ' : ' + e['label'] + '.')
        out += ['', 'La maintenance entretient toutes les parties.', '', '## Ce qui fait foi', '', ' '.join(data['authority'][k] for k in ['rule', 'retained', 'derived'])]
    return '\n'.join(out) + '\n'


def render_outputs(embed_font=True):
    global DATA
    DATA = json.loads((ROOT / 'systeme.json').read_text())
    drawn = [(r['from'], r['to']) for r in DATA['relations']]
    if drawn != DRAWN_RELATIONS:
        raise ValueError('relations de systeme.json différentes du dessin fixe ' + str(DRAWN_RELATIONS) + ' : adapter le générateur')
    palettes = DATA['themes']
    collection = [DATA] + [json.loads((ROOT / (name + '.json')).read_text()) for name in ['parcours', 'boucle']]
    names = {'systeme': 'Carte du système', 'parcours': 'Parcours d’un travail', 'boucle': 'Créer puis apprendre'}
    outputs = {}
    for data in collection:
        ident = data['id']; entry = data['entries'][0]
        drawing = {theme: (svg(theme, embed_font) if ident == 'systeme' else sequence_svg(data, theme, embed_font)) for theme in palettes}
        for theme, value in drawing.items(): outputs[ident + '-' + theme + '.svg'] = value + '\n'
        css = font_css(embed_font)
        for name, palette in palettes.items(): css += 'html[data-theme="' + name + '"]{' + ''.join('--' + k + ':' + v + ';' for k, v in palette.items()) + '}'
        nodes = text_sections(data)
        roles = ''.join('<li><strong>' + html.escape(n['title']) + '</strong> — ' + html.escape(' '.join(n['lines'] + n.get('conditions', []))) + ('<ul>' + ''.join('<li><strong>' + html.escape(c['title']) + '</strong> — ' + html.escape(' '.join(c['lines'])) + '</li>' for c in n['children']) + '</ul>' if n.get('children') else '') + '</li>' for n in nodes)
        mapping = {
            '__PAGE_NAME__': names[ident], '__FONT_CSS__': css, '__NUMBER__': data['number'], '__ID__': ident,
            '__TITLE__': ''.join('<span>' + html.escape(t) + '</span>' for t in data['title'].split('\n')), '__INTRO__': html.escape(data['intro']),
            '__NAV__': ''.join('<a href="' + other['file'] + '"' + (' aria-current="page"' if ident == other['id'] else '') + '>' + names[other['id']] + '</a>' for other in collection),
            '__SELECT_LABEL__': 'Votre entrée' if ident == 'systeme' else 'Une étape à examiner',
            '__MAP_HEADING__': 'Les responsabilités reliées' if ident == 'systeme' else ('Le parcours et ses protections' if ident == 'parcours' else 'Créer puis corriger utilement'),
            '__SOURCES_HEADING__': 'Ouvrir la bonne porte' if ident == 'systeme' else 'Retrouver les sections propriétaires',
            '__ENTRIES__': ''.join('<option value="' + e['id'] + '">' + html.escape(e['label']) + '</option>' for e in data['entries']),
            '__INITIAL_TITLE__': html.escape(entry['title']), '__INITIAL_DESCRIPTION__': html.escape(entry['description']), '__INITIAL_LINK__': BASE + entry['target'], '__INITIAL_LABEL__': html.escape(entry['link']),
            '__SCOPE__': html.escape(data['scope']), '__SVG__': drawing['clair'], '__CARDS__': cards() if ident == 'systeme' else sequence_cards(data),
            '__LINKS__': ''.join('<li>' + link(e['target'], e['label']) + '<span>' + html.escape(e['description']) + '</span></li>' for e in data['entries'][1:]),
            '__ROLES__': roles, '__RELATIONS__': 'La maintenance entretient toutes les parties ; le design et la gouvernance se répondent selon le risque, la décision et la reprise.' if ident == 'systeme' else html.escape(' '.join(data['foot']['lines'])),
            '__AUTHORITY__': 'La section propriétaire, à son emplacement actuel, fait foi. Les cartes orientent la lecture.', '__EQUIVALENT_FILE__': ident + '.md',
            '__ENTRY_JSON__': json.dumps(data['entries'], ensure_ascii=False).replace('<', '\\u003c'), '__BASE__': BASE,
        }
        page = (ROOT / 'page.template.html').read_text()
        for marker, value in mapping.items(): page = page.replace(marker, value)
        page = page.replace('</head>', '<!-- Fonte Manrope sous OFL :\n' + (ROOT / 'fonts/OFL-manrope.txt').read_text().replace('--', '—') + '\n-->\n</head>')
        if '__' in page: raise ValueError('marqueur de template restant pour ' + ident)
        outputs[data['file']] = page
        outputs[ident + '.md'] = equivalent(data)
    return outputs


def used_characters():
    """Textes des pages et des SVG, plus tous les choix affichables après sélection."""
    class TextReader(HTMLParser):
        def __init__(self):
            super().__init__()
            self.hidden = 0
            self.texts = []

        def handle_starttag(self, tag, attrs):
            if tag in ('style', 'script', 'metadata'):
                self.hidden += 1

        def handle_endtag(self, tag):
            if tag in ('style', 'script', 'metadata'):
                self.hidden -= 1

        def handle_data(self, data):
            if not self.hidden:
                self.texts.append(data)

    reader = TextReader()
    for name, page in render_outputs(embed_font=False).items():
        if name.endswith('.html'):
            reader.feed(page)
    for name in ('systeme', 'parcours', 'boucle'):
        data = json.loads((ROOT / (name + '.json')).read_text())
        for entry in data['entries']:
            reader.texts.extend(entry[key] for key in ('label', 'title', 'description', 'link'))
    # Le bouton change son texte au basculement de thème.
    reader.texts.append('Thème clair Thème sombre')
    return ''.join(sorted(set(''.join(reader.texts)) - set('\n\r\t')))


def main():
    for name, content in render_outputs().items(): (ROOT / name).write_text(content, encoding='utf-8')
    print('Trois cartes construites : HTML, SVG clair/sombre et équivalents écrits.')


if __name__ == '__main__': main()


