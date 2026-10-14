"""Analyses des données de Taste Skill v2 et du texte de Design Governance (lecture et comptage, aucun skill n'est lancé sur un brief).
Usage : python3 -I analyses.py <dossier taste-skill (contient SKILL.md)> <racine du paquet DG>
Sections : A2 polices, A3 blueprints contre les motifs bannis, A4 couverture, A5 stillness, A6 densité de valeurs chiffrées, A7 lexique."""
import sys, json, re, glob, os, collections, statistics as st
TS, DG = sys.argv[1].rstrip('/') + '/', sys.argv[2].rstrip('/') + '/'
L = TS + 'library/'
rd = lambda f: open(f, encoding='utf-8').read()
words = lambda t: len(re.findall(r"[\wÀ-ÿ’'-]+", t))
D = json.load(open(L+'directions.json')); H = json.load(open(L+'heroes.json')); S = json.load(open(L+'sections.json'))
P = json.load(open(L+'palettes.json')); T = json.load(open(L+'type.json')); M = json.load(open(L+'motions.json')); PH = json.load(open(L+'photos.json')); SITES = json.load(open(L+'sites.json'))

print('== A2 : systèmes typographiques contre les listes `default-font` et `mono` du lint de TS (lint.mjs:33 et :50)')
default = re.compile(r'\b(Inter|Poppins|Montserrat|Roboto|Open Sans|Space Grotesk|Instrument Serif|Playfair Display|Plus Jakarta Sans|Outfit|Sora|Lato|Nunito|Raleway)\b', re.I)
mono = re.compile(r'(JetBrains|Geist|IBM Plex|Space|DM|Roboto|Fragment|Azeret|Red Hat|Martian|Commit|Departure|Fira)[ _+]?Mono|Courier|Consolas|Menlo|Monaco|monospace', re.I)
fams = collections.Counter(x[r]['family'] for x in T for r in ('display', 'text'))
print('systèmes', len(T), '| familles distinctes', len(fams), '| à une seule famille', sum(1 for x in T if x['display']['family'] == x['text']['family']))
print('avec une famille de la liste default-font :', [x['id'] for x in T if any(default.search(x[r]['family']) for r in ('display', 'text'))])
print('avec une famille monospace :', [x['id'] for x in T if any(mono.search(x[r]['family']) for r in ('display', 'text'))])
print('familles les plus dealées :', fams.most_common(6))

print('\n== A3 : motifs bannis par les règles de la maison dans la prose des directions, héros et sections (240 entrées)')
pat = {'hairline/1px': r'hairline|1px (?:rule|line|border|outline)|thin rule|ruled|divider line', 'mono': r'\bmono(?:space)?\b',
       'numérotation 01/02': r'(?<![\d.])0[1-9]\b(?![.\d])|index numbers?|numbered|numbering', 'eyebrow/kicker': r'eyebrow|kicker|label above',
       'pill': r'\bpill\b', 'gradient': r'gradient', 'shadow': r'shadow', 'glass/blur': r'backdrop|glass|\bblur', 'crosshair/crop mark': r'crosshair|crop mark|visible grid'}
neg = re.compile(r"\b(no|never|without|not|nothing|zero|avoid|instead of|rather than)\b", re.I)
total = sum(len(x) for x in (D, H, S)); hits = []
for kind, items in (('direction', D), ('héros', H), ('section', S)):
    for x in items:
        for fk in ('blueprint', 'mobile', 'composition', 'typography', 'colour', 'imagery', 'idea', 'richness', 'headline', 'note'):
            txt = x.get(fk)
            if not isinstance(txt, str): continue
            for name, p in pat.items():
                for m in re.finditer(p, txt, re.I):
                    hits.append((name, kind, x['id'], fk, bool(neg.search(txt[max(0, m.start()-45):m.start()])), txt[max(0, m.start()-50):m.end()+50].replace('\n', ' ')))
print('entrées lues', total, '| occurrences', len(hits))
for h in hits: print('  ', h[0], h[1], h[2], '(' + h[3] + ')', 'négation' if h[4] else '', '…' + h[5] + '…')

print('\n== A4 : couverture de la bibliothèque')
src = rd(TS + 'scripts/draw.mjs'); sectors = re.search(r"const SECTORS = \[(.*?)\];", src).group(1).replace("'", '').replace(' ', '').split(',')
cnt = {s: sum(1 for d in D if s in d['sectors'] or '*' in d['sectors']) for s in sectors}
print('secteurs', len(sectors), '| directions par secteur min..max', min(cnt.values()), max(cnt.values()), '| secteurs à 5 directions ou moins', {s: c for s, c in cnt.items() if c <= 5})
print('tons', {t: sum(1 for d in D if t in d.get('tones', [])) for t in ['quiet', 'bold', 'warm', 'technical', 'playful', 'luxury', 'editorial']})
roles = collections.Counter(s['role'] for s in S); print('rôles de section', len(roles), dict(roles))
hd = collections.Counter(d for h in H for d in h['directions']); print('héros par direction min/méd/max', min(hd.values()), st.median(hd.values()), max(hd.values()))
palfor = lambda d: [p['id'] for p in P if p['id'] in d.get('palettes', []) or set(p.get('tags', [])) & set(d.get('paletteTags', []))]
pc = [len(palfor(d)) for d in D]; print('palettes par direction min/méd/max', min(pc), st.median(pc), max(pc))
tc = [sum(1 for t in T if t['id'] in d.get('type', []) or t['class'] in d.get('typeClasses', [])) for d in D]; print('systèmes typographiques par direction min/méd/max', min(tc), st.median(tc), max(tc))
combos = sum(hd.get(d['id'], 0) * len(palfor(d)) * max(1, tc[i]) for i, d in enumerate(D)); print('combinaisons héros × palette × système, somme sur les 20 directions', combos)
print('jeux de photos', len(PH['sets']), '| tailles min..max', min(len(v['photos']) for v in PH['sets'].values()), max(len(v['photos']) for v in PH['sets'].values()))
print('sites étudiés', len(SITES), '| notes', min(x['score'] for x in SITES), '→', max(x['score'] for x in SITES), '| ≥7,5 :', sum(1 for x in SITES if x['score'] >= 7.5), '| 7,0 à 7,4 :', sum(1 for x in SITES if 7.0 <= x['score'] < 7.5), '| 6,8 à 6,9 :', sum(1 for x in SITES if x['score'] < 7.0))

print('\n== A5 : directions qui tirent le mouvement « stillness » et dérogations `allow`')
print([(d['id'], d['motion'], d.get('allow')) for d in D if d['motion'] == 'stillness'], '| directions avec un `allow` non vide :', [d['id'] for d in D if d.get('allow')])
print('description de stillness :', [m['description'] for m in M if m['id'] == 'stillness'][0])

print('\n== A6 : valeurs chiffrées prescrites (px, vw, vh, em, rem, ms, ch, fr, %, clamp(), cubic-bezier())')
unit = re.compile(r'\d+(?:[.,]\d+)?\s?(?:px|vw|vh|svh|dvh|em|rem|ms|ch|fr|dp|pt|fps)\b|\d+(?:[.,]\d+)?\s?%|\bclamp\(|cubic-bezier\(', re.I)
tsref = [TS + 'SKILL.md'] + sorted(glob.glob(TS + 'references/*.md'))
t_all = ''.join(rd(f) + '\n' for f in tsref); t_res = rd(TS + 'references/research.md')
print('TS SKILL + references : mots %d, valeurs %d (dont research.md : %d)' % (words(t_all), len(unit.findall(t_all)), len(unit.findall(t_res))))
dg_files = sorted(glob.glob(DG + 'design/**/*.md', recursive=True)); dg_all = ''.join(rd(f) + '\n' for f in dg_files)
i = dg_all.index('### POINTS-DE-DEPART'); j = dg_all.index('\n---', i); dg0 = dg_all[:i] + dg_all[j:]
print('DG design/** : mots %d, valeurs %d | hors section POINTS-DE-DEPART : mots %d, valeurs %d | POINTS-DE-DEPART seule : mots %d, valeurs %d' % (words(dg_all), len(unit.findall(dg_all)), words(dg0), len(unit.findall(dg0)), words(dg_all[i:j]), len(unit.findall(dg_all[i:j]))))
for name, items in (('TS sections (blueprint + mobile)', [s['blueprint'] + ' ' + s.get('mobile', '') for s in S]), ('TS héros (blueprint + mobile)', [h['blueprint'] + ' ' + h.get('mobile', '') for h in H])):
    n = [len(unit.findall(x)) for x in items]; w = [words(x) for x in items]
    print('%-34s entrées %3d | valeurs par entrée : médiane %.1f, total %d | mots par entrée : médiane %.0f' % (name, len(items), st.median(n), sum(n), st.median(w)))
cat = rd(DG + 'design/formes/catalogue.md')
parts = [re.split(r'\n## ', p)[0] for p in re.split(r'\n(?=### `)', cat) if re.match(r'### `(SUPPORT|GRID|SCENE)/', p)]
n = [len(unit.findall(x)) for x in parts]; w = [words(x) for x in parts]
print('%-34s entrées %3d | valeurs par entrée : médiane %.1f, total %d | mots par entrée : médiane %.0f' % ('DG catalogue SUPPORT/GRID/SCENE', len(parts), st.median(n), sum(n), st.median(w)))

print('\n== A7 : termes à motif propre, occurrences (TS SKILL + references hors research ; DG design/** hors POINTS-DE-DEPART)')
ts_txt = rd(TS + 'SKILL.md') + '\n'.join(rd(f) for f in glob.glob(TS + 'references/*.md') if not f.endswith('research.md'))
terms = {'kerning / crénage': r'kerning|crénage', 'police variable': r'police variable|variable font', 'font-display / preconnect / chargement des polices': r'font-display|preconnect|loading the fonts', 'OKLCH': r'oklch', 'gamut': r'gamut',
 'hyphens / césure': r'hyphens|césure', 'full-bleed / bord à bord': r'full-bleed|\bbleed|bord à bord|à fleur', 'pas de teinte / tone step': r'tone step|step in tone|step in background|pas de teinte|écart de valeur',
 'inventaire du sujet': r'inventory the subject|inventaire du sujet|inventaire', 'interruption (animation)': r'interruption|interrupt', 'WCAG': r'wcag', "lecteur d'écran / screen reader": r"lecteur d.écran|screen reader|lecture assistée",
 'récupération après erreur': r'récupération|recovery', 'rollback / retour arrière': r'rollback|retour arrière', 'View Transitions / FLIP / Web Animations': r'view transitions|\bflip\b|web animations',
 'IntersectionObserver / scroll listener': r'intersectionobserver|scroll listener|addEventListener\(.scroll', 'text-wrap: balance': r'text-wrap: ?balance', 'tabular-nums': r'tabular-nums', 'clamp()': r'clamp\(',
 'cubic-bezier': r'cubic-bezier', 'prefers-reduced-motion (littéral)': r'prefers-reduced-motion', 'crédits enregistrés (credits.json)': r'credits\.json|crédits enregistrés|record(ed)? the credit', 'licences CC (CC BY, CC0)': r'cc by|cc0|creative commons'}
print('%-52s %4s %4s' % ('terme', 'TS', 'DG'))
for k, p in terms.items(): print('%-52s %4d %4d' % (k, len(re.findall(p, ts_txt, re.I)), len(re.findall(p, dg0, re.I))))
