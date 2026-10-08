#!/usr/bin/env python3
"""U5 : étiquettes anonymes, images (même découpe que U3), paires et consignes (même texte que U3)."""
import json, os, random, secrets
from PIL import Image
S = '/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad'
U5 = f'{S}/U5'
src = {'V': f'{S}/U3/captures_defilees/R2', 'X': f'{S}/U3/captures_defilees/R4', 'K': f'{S}/U3/captures_defilees/R6'}
src.update({n: f'{U5}/captures_defilees/{n}' for n in ('N1', 'N2', 'N3', 'N4', 'N5')})
rng = random.Random(secrets.randbits(64))
labels = ['B', 'D', 'F', 'G', 'H', 'J', 'L', 'Q', 'R', 'S', 'W', 'Z']; rng.shuffle(labels)
key = dict(zip(src, labels))
json.dump(key, open(f'{U5}/cle/cle.json', 'w'), indent=1)
img = f'{U5}/jugement/images'
for r, l in key.items():
    d = Image.open(f'{src[r]}/capture-1440px.png').convert('RGB')
    m = Image.open(f'{src[r]}/capture-390px.png').convert('RGB')
    d.crop((0, 0, 1440, min(900, d.height))).save(f'{img}/{l}-desktop-premier-ecran.png')
    m.crop((0, 0, 390, min(844, m.height))).save(f'{img}/{l}-mobile-premier-ecran.png')
    sc = 1900 / d.height; d.resize((int(1440 * sc), 1900)).save(f'{img}/{l}-desktop-page-entiere.png')
    for i, y in enumerate(range(0, d.height, 1400)):
        d.crop((0, y, 1440, min(y + 1400, d.height))).save(f'{img}/{l}-desktop-tranche-{i + 1}.png')
briefs = {'B2': "« Il me faut une landing page pour notre SaaS de facturation. »",
          'B3': "« Il me faut un site pour mon école de natation pour enfants. »"}
pairs = [('B2', n, r) for n in ('N1', 'N2') for r in ('V', 'X')] + [('B3', 'N3', 'K')] \
      + [('B2', 'N4', r) for r in ('V', 'X', 'N1', 'N2')] + [('B3', 'N5', r) for r in ('K', 'N3')]
def views(l):
    v = [f'{img}/{l}-desktop-premier-ecran.png', f'{img}/{l}-mobile-premier-ecran.png', f'{img}/{l}-desktop-page-entiere.png']
    return v + [p for p in (f'{img}/{l}-desktop-tranche-1.png', f'{img}/{l}-desktop-tranche-2.png') if os.path.exists(p)]
jobs, n = [], 0
for brief, x, y in pairs:
    for first, second in ((x, y), (y, x)):
        n += 1; A, B = key[first], key[second]
        txt = f"""Tu es directeur·rice artistique senior et tu juges deux propositions de design répondant à la même demande d'un client : {briefs[brief]} Le client n'a rien fourni d'autre ; les deux propositions inventent donc des contenus d'exemple.

Regarde les images avec l'outil Read, dans cet ordre. Proposition A : {', '.join(views(A))}. Proposition B : {', '.join(views(B))}.
(premier écran ordinateur, premier écran mobile, page entière réduite, puis tranches de la page à taille réelle.)

Compare A et B sur cinq critères, en une phrase chacun, et dis lequel l'emporte (A, B ou égal) :
1. présence : la page retient-elle, a-t-elle un point de vue ?
2. spécificité : si l'on retire le nom, la page reste-t-elle propre à ce métier, ou pourrait-elle servir à n'importe qui ?
3. finition : hiérarchie, alignements, typographie, détails, mobile ;
4. vérité : la page évite-t-elle les fausses preuves (faux avis, faux logos, chiffres présentés comme réels) et signale-t-elle ce qui est exemple ?
5. défaut dominant de chacune, en une phrase.
Puis donne ta préférence globale (A ou B) et sa force (nette, légère, indécise).

Ne cherche rien d'autre que ces images ; n'ouvre aucun autre fichier. Réponds uniquement par un objet JSON :
{{"presence":{{"gagnant":"A|B|egal","raison":"…"}},"specificite":{{…}},"finition":{{…}},"verite":{{…}},"defaut_A":"…","defaut_B":"…","preference":"A|B","force":"nette|legere|indecise"}}"""
        open(f'{U5}/jugement/consignes/J{n:02d}.txt', 'w').write(txt)
        jobs.append({'id': f'J{n:02d}', 'brief': brief, 'A': first, 'B': second})
json.dump(jobs, open(f'{U5}/cle/paires.json', 'w'), indent=1)
print(len(jobs), 'consignes ;', len(os.listdir(img)), 'images')
