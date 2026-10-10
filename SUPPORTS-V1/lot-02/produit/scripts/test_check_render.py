#!/usr/bin/env python3
"""Tests de comportement de `scripts/check_render.py`.

Partie A, toujours exécutée (bibliothèque standard seulement) : l'interprétation des mesures, avec des mesures
synthétiques. Partie B, exécutée si Playwright et Chromium sont présents : des pages pièges, une par défaut connu.
Sans navigateur, la partie B est déclarée NOT-VERIFIED, jamais réussie ; `--require-browser` en fait un échec.
Partie C, si un runtime Node est déjà disponible : le JavaScript livré sur des DOM simulés, sans rendu.
Un runtime C absent est déclaré NOT-VERIFIED ; aucun runtime ni navigateur n'est installé par les tests.

Un test qui échoue fait échouer le script (code 1). Ce fichier ne valide aucun rendu : il vérifie que la recette
dit vrai sur des cas dont la réponse est connue.
"""
from __future__ import annotations

import argparse
import contextlib
import functools
import http.server
import http.client
import importlib.util
import io
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
from pathlib import Path
from urllib.parse import urlsplit
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("check_render", HERE / "check_render.py")
cr = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cr)
PASS, RESERVE, RETURN, NOTVER = cr.PASS, cr.RESERVE, cr.RETURN, cr.NOTVER

failures: list[str] = []
count = {"A": 0, "B": 0, "C": 0}


def status(checks, prefix: str) -> str:
    for title, st, _ in checks:
        if title.startswith(prefix):
            return st
    return "(absent)"


def expect(part: str, name: str, got, want) -> None:
    count[part] += 1
    ok = got == want
    print(f"  [{'ok' if ok else 'ÉCHEC'}] {part}{count[part]:02d} {name} : {got}" + ("" if ok else f" (attendu {want})"))
    if not ok:
        failures.append(f"{part} {name}")


# ---------------------------------------------------------------- Partie A : interprétation, sans navigateur
def raw_case(audit=None, proof=None, stops=None, missing=None, running=None, overflow=(390, 390), errs=None, keyboard=None) -> dict:
    base = {"contrast": [], "nonSolid": [], "unknown": [], "targets": [], "uaControls": 0, "names": [], "imgs": [], "inner": [],
            "h1": 1, "lang": "fr", "title": "t"}
    base.update(audit or {})
    pw = {"overflow": {"sw": overflow[0], "cw": overflow[1]}, "offenders": [], "errs": errs or [], "audit": base,
          "proof": proof, "stops": stops if stops is not None else ["#a"], "missing_ind": missing or []}
    if keyboard is not None:
        pw['keyboard'] = keyboard
    return {"widths": [390], "per_width": {390: pw}, "running": running or [], "blocked": 0}


def part_a() -> None:
    with patch.dict(os.environ, {"DG_BROWSER_EXECUTABLE": "/browser/configure"}):
        expect("A", "navigateur explicitement configuré", cr.parser().parse_args(["page.html"]).browser_executable, "/browser/configure")
        expect("A", "option navigateur prioritaire sur la configuration", cr.parser().parse_args(["page.html", "--browser-executable", "/browser/choisi"]).browser_executable, "/browser/choisi")
    with tempfile.TemporaryDirectory() as tmp:
        page = Path(tmp) / 'page été #1.html'
        page.write_text('<h1>Local</h1>', encoding='utf-8')
        args = cr.parser().parse_args([str(page), '--serve-local'])
        with cr.page_url(args) as url:
            parsed = urlsplit(url)
            client = http.client.HTTPConnection(parsed.hostname, parsed.port, timeout=2)
            client.request('GET', parsed.path)
            response = client.getresponse()
            expect('A', 'serveur local : nom encodé et contenu servi', [parsed.hostname, response.status, response.read()],
                   ['127.0.0.1', 200, b'<h1>Local</h1>'])
            client.close()
        try:
            with cr.page_url(args) as url:
                port = urlsplit(url).port
                raise RuntimeError('mesure interrompue')
        except RuntimeError:
            pass
        with socket.socket() as listener:
            listener.bind(('127.0.0.1', port))
            expect('A', 'serveur fermé après interruption de la mesure', listener.getsockname(), ('127.0.0.1', port))
    print("Partie A — interprétation (sans navigateur)")
    clean = cr.interpret(raw_case())
    expect("A", "page propre : aucun RETURN", any(s == RETURN for _, s, _ in clean), False)
    expect("A", "sans sélecteur, objet de preuve NOT-VERIFIED", status(clean, "Objet de preuve"), NOTVER)
    expect("A", "objet introuvable", status(cr.interpret(raw_case(proof={"found": False}), "#p"), "Objet de preuve"), RETURN)
    expect("A", "objet de hauteur nulle", status(cr.interpret(raw_case(proof={"found": True, "w": 300, "h": 0, "hidden": False, "visible": 0}), "#p"), "Objet de preuve"), RETURN)
    expect("A", "objet masqué", status(cr.interpret(raw_case(proof={"found": True, "w": 300, "h": 200, "hidden": True, "visible": 0}), "#p"), "Objet de preuve"), RETURN)
    expect("A", "objet sous la ligne de flottaison", status(cr.interpret(raw_case(proof={"found": True, "w": 300, "h": 600, "hidden": False, "visible": 10}), "#p"), "Objet de preuve"), RESERVE)
    visible = {"found": True, "method": "css-rectangle-bounded", "w": 300, "h": 600, "hidden": False,
               "visible": 300, "intersectionWidth": 300, "opacity": 1, "limits": []}
    expect("A", "objet : CSS et rectangle couverts", status(cr.interpret(raw_case(proof=visible), "#p"), "Objet de preuve"), PASS)
    for label, changes, want in [('transparent', {'opacity': 0}, RETURN), ('hors écran horizontal', {'intersectionWidth': 0}, RESERVE),
                               ('faible bande horizontale', {'intersectionWidth': 3}, RESERVE), ('opacité partielle', {'opacity': .5}, RESERVE),
                               ('découpe inconnue', {'limits': ['masque']}, RESERVE), ('ancienne mesure', {'method': 'legacy'}, RESERVE)]:
        expect('A', 'objet ' + label, status(cr.interpret(raw_case(proof={**visible, **changes}), '#p'), 'Objet de preuve'), want)
    expect("A", "couleur non convertible : jamais PASS", status(cr.interpret(raw_case(audit={"unknown": [{"sel": "p", "value": "color(foo 1 2 3)"}]})), "Contraste"), RESERVE)
    expect("A", "texte SVG non mesuré : réserve explicite", status(cr.interpret(raw_case(audit={"svgText": [{"sel": "text"}]})), "Contraste"), RESERVE)
    expect("A", "fond en dégradé : jamais PASS", status(cr.interpret(raw_case(audit={"nonSolid": [{"sel": "mark"}]})), "Contraste"), RESERVE)
    fail = {"sel": "p", "fg": "#aaaaaa", "bg": "#ffffff", "size": 16, "ratio": 2.32, "need": 4.5, "text": "x"}
    expect("A", "contraste insuffisant", status(cr.interpret(raw_case(audit={"contrast": [fail]})), "Contraste"), RETURN)
    expect("A", "petite cible espacée", status(cr.interpret(raw_case(audit={"targets": [{"sel": "a", "w": 20, "h": 20, "spaced": True}]})), "Taille"), PASS)
    expect("A", "petites cibles serrées : réserve, pas RETURN", status(cr.interpret(raw_case(audit={"targets": [{"sel": "b", "w": 16, "h": 16, "spaced": False}]})), "Taille"), RESERVE)
    expect("A", "focus sans changement de style", status(cr.interpret(raw_case(missing=["button"])), "Parcours clavier"), RESERVE)
    expect("A", "feuille ouverte qui défile", status(cr.interpret(raw_case(audit={"inner": [{"sel": "#d", "dialog": True, "sw": 580, "cw": 390}]})), "Défilement"), RETURN)
    expect("A", "conteneur défilant voulu ou non", status(cr.interpret(raw_case(audit={"inner": [{"sel": ".table", "dialog": False, "sw": 900, "cw": 390}]})), "Défilement"), RESERVE)
    expect("A", "animation infinie en mouvement réduit", status(cr.interpret(raw_case(running=[{"name": "spin", "infinite": True}])), "Mouvement"), RETURN)
    expect("A", "débordement du document", status(cr.interpret(raw_case(overflow=(510, 390))), "Débordement horizontal"), RETURN)
    expect("A", "contrôle sans nom", status(cr.interpret(raw_case(audit={"names": [{"sel": "button.x"}]})), "Nom accessible"), RETURN)
    expect("A", "opacité de groupe : réserve", status(cr.interpret(raw_case(audit={'groupOpacity':[{'sel':'#g','opacity':0.5}]})), 'Contraste'), RESERVE)
    expect("A", "opacité non couverte et défaut ailleurs : retour conservé", status(cr.interpret(raw_case(audit={'groupOpacity':[{'sel':'#g'}], 'contrast':[fail]})), 'Contraste'), RETURN)
    expect("A", "candidat DOM présent : nom calculé non prouvé", status(cr.interpret(raw_case(audit={'nameMethod':'dom-candidate','nameControls':1})), 'Nom accessible'), RESERVE)
    expect("A", "aucun contrôle DOM applicable", status(cr.interpret(raw_case(audit={'nameMethod':'dom-candidate','nameControls':0})), 'Nom accessible'), PASS)
    expect("A", "ancienne mesure sans méthode de nom", status(cr.interpret(raw_case()), 'Nom accessible'), RESERVE)
    expect("A", "zéro arrêt sans couverture", status(cr.interpret(raw_case(stops=[])), 'Parcours clavier'), RESERVE)
    complete={'reason':'end','expected':[{'key':'control-0','id':'#a'}],'unreached':[],'scope':'page'}
    expect("A", "parcours terminé et candidats atteints", status(cr.interpret(raw_case(keyboard=complete)), 'Parcours clavier'), PASS)
    expect("A", "borne atteinte malgré tous les candidats vus", status(cr.interpret(raw_case(keyboard={**complete,'reason':'limit'})), 'Parcours clavier'), RESERVE)
    expect("A", "interactif candidat et zéro arrêt", status(cr.interpret(raw_case(stops=[],keyboard={**complete,'unreached':['#a']})), 'Parcours clavier'), RESERVE)
    expect("A", "absence justifiée de candidat et parcours fini", status(cr.interpret(raw_case(stops=[],keyboard={**complete,'expected':[]})), 'Parcours clavier'), PASS)
    expect("A", "cycle complet", status(cr.interpret(raw_case(keyboard={**complete,'reason':'cycle'})), 'Parcours clavier'), PASS)
    multiple=raw_case(keyboard=complete);multiple['widths']=[390,1440]
    multiple['per_width'][1440]={**multiple['per_width'][390],'keyboard':{**complete,'reason':'limit'}}
    expect("A", "une largeur tronquée suffit à réserver", status(cr.interpret(multiple), 'Parcours clavier'), RESERVE)
    expect('A','arrêt hors inventaire : réserve',status(cr.interpret(raw_case(keyboard={**complete,'unexpected':['iframe']})),'Parcours clavier'),RESERVE)
    unknown=raw_case(audit={'nameMethod':'dom-candidate','nameControls':1,'nameUncertain':[{'sel':'button'}]})
    detail=next(d for t,_,d in cr.interpret(unknown) if t.startswith('Nom accessible'))
    expect('A','nom inconnu ne promet pas un candidat présent','hors couverture' in detail and 'candidats DOM présents' not in detail,True)
    covered = {'method': 'dom-text-bounded', 'candidates': 1, 'evaluated': 1, 'excluded': 0, 'unmeasured': []}
    for label, coverage, want in [('texte opaque évalué', covered, PASS), ('aucun texte applicable', {**covered, 'candidates': 0, 'evaluated': 0}, PASS),
                                 ('candidat non évalué', {**covered, 'evaluated': 0}, RESERVE),
                                 ('placeholder non évalué', {**covered, 'evaluated': 0, 'unmeasured': [{'sel': 'input', 'kind': 'placeholder affiché'}]}, RESERVE)]:
        expect('A', label, status(cr.interpret(raw_case(audit={'contrastCoverage': coverage})), 'Contraste'), want)
    expect('A', 'ancienne mesure de contraste : réserve', status(cr.interpret(raw_case()), 'Contraste'), RESERVE)
    mult = raw_case(audit={'contrastCoverage': covered}); mult['widths'] = [390, 1440]
    mult['per_width'][1440] = {**mult['per_width'][390], 'audit': {**mult['per_width'][390]['audit'], 'contrastCoverage': {**covered, 'evaluated': 0}}}
    expect('A', 'une largeur non couverte suffit à réserver le contraste', status(cr.interpret(mult), 'Contraste'), RESERVE)
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / 'recipe.json'
        sample = raw_case(audit={'contrastCoverage': covered}, proof=visible, keyboard=complete)
        args = cr.parser().parse_args([str(Path(__file__).resolve()), '--proof', '#p', '--json', str(out)])
        with patch.object(cr, 'measure', return_value=sample), contextlib.redirect_stdout(io.StringIO()):
            code = cr.run(args)
        result = json.loads(out.read_text())
        expect('A', 'sortie JSON simulée sans navigateur', code, 0)
        expect('A', 'JSON conserve couverture contraste et observation de preuve',
               [result['contrast_coverage']['390'], result['proof_observations']['390']], [covered, visible])
        expect('A', 'JSON conserve couverture clavier', result['keyboard_coverage']['390']['reason'], 'end')
    with tempfile.TemporaryDirectory() as tmp:
        shots = Path(tmp) / 'v1'
        args = cr.parser().parse_args([str(Path(__file__).resolve()), '--widths', '390', '--captures', str(shots), '--json', str(Path(tmp) / 'r.json')])
        sample = {**raw_case(), 'captures': [str(shots / 'capture-390px.png')],
                  'browser': {'engine': 'chromium', 'version': 'version-test', 'executable': '/browser/choisi'}}
        with patch.object(cr, 'measure', return_value=sample), contextlib.redirect_stdout(io.StringIO()):
            cr.run(args)
        expect('A', 'captures listées dans la provenance', json.loads((Path(tmp) / 'r.json').read_text())['provenance']['captures'], sample['captures'])
        expect('A', 'navigateur observé conservé dans la provenance', json.loads((Path(tmp) / 'r.json').read_text())['provenance']['browser'], sample['browser'])
        shots.mkdir(); (shots / 'capture-390px.png').write_bytes(b'avant')
        with patch.object(cr, 'measure', side_effect=AssertionError('mesure lancée')), contextlib.redirect_stderr(io.StringIO()):
            code = cr.run(args)
        expect('A', 'capture existante : refus avant toute mesure, rien écrasé', [code, (shots / 'capture-390px.png').read_bytes()], [2, b'avant'])


# Partie C : code JavaScript livré, DOM simulé ; aucun navigateur et aucun rendu.
MOCK_JS = r"""
const refs = {};
const node = (tag, attrs={}, children=[], style={}) => {
  const e = {nodeType:1, tagName:tag, attrs, childNodes:children, parentElement:null, style, classList:[],
    id:attrs.id||'', textContent:children.map(c=>c.textContent||'').join(''), labels:[],
    getAttribute:k=>Object.hasOwn(attrs,k)?attrs[k]:null, hasAttribute:k=>Object.hasOwn(attrs,k),
    closest:()=>null, getBoundingClientRect:()=>({width:100,height:20}), type:attrs.type||'', value:attrs.value||''};
  for (const c of children) if(c.nodeType===1)c.parentElement=e;
  if (e.id)refs[e.id]=e;return e;
};
const txt = textContent => ({nodeType:3,textContent});
global.getComputedStyle = (e,pseudo) => pseudo ? {content:e.attrs.generated||'none'} :
  {display:'block',visibility:'visible',opacity:'1',backgroundImage:'none',backgroundColor:'rgb(255, 255, 255)',
   color:'rgb(0, 0, 0)',fontSize:'16px',fontWeight:'400',...e.style};
global.document = {getElementById:id=>refs[id]||null};
"""


def part_c() -> str:
    node = os.environ.get('CODEX_PRIMARY_RUNTIME_NODE') or shutil.which('node')
    if not node:
        return 'NOT-VERIFIED : runtime JavaScript absent, DOM simulés non exécutés'
    print('Partie C — fonctions JavaScript livrées sur DOM simulés, sans navigateur')
    def js(body):
        result=subprocess.run([node,'-e',MOCK_JS+'\nconst candidate=('+cr.NAME_JS+');\n'+body],capture_output=True,text=True)
        if result.returncode:
            failures.append('C : exécution JavaScript impossible '+result.stderr[:200]);return None
        return json.loads(result.stdout)
    cases=[
        ('bouton dont seul le texte masqué fournit le nom',"node('BUTTON',{},[node('SPAN',{'aria-hidden':'true'},[txt('×')])])",''),
        ('descendant display none exclu',"node('BUTTON',{},[node('SPAN',{},[txt('×')],{display:'none'})])",''),
        ('texte visible conservé',"node('BUTTON',{},[txt('Valider'),node('SPAN',{'aria-hidden':'true'},[txt('×')])])",'Valider'),
        ('aria label',"node('BUTTON',{'aria-label':'Fermer'},[])",'Fermer'),
        ('référence masquée explicite',"(node('SPAN',{id:'lab',hidden:''},[txt('Fermer')]),node('BUTTON',{'aria-labelledby':'lab'},[]))",'Fermer'),
        ('référence avant aria label',"(node('SPAN',{id:'lab'},[txt('Confirmer')]),node('BUTTON',{'aria-labelledby':'lab','aria-label':'Ignorer'},[]))",'Confirmer'),
        ('label natif masqué référencé',"(()=>{const e=node('INPUT',{type:'text'});e.labels=[node('LABEL',{hidden:''},[txt('Prénom')])];return e;})()",'Prénom'),
        ('image avec alternative',"node('BUTTON',{},[node('IMG',{alt:'Exporter'})])",'Exporter'),
        ('référence inexistante : repli aria label',"node('BUTTON',{'aria-labelledby':'absent','aria-label':'Valider'})",'Valider'),
        ('référence à soi',"node('BUTTON',{id:'self','aria-labelledby':'self','aria-label':'Supprimer'})",'Supprimer'),
        ('référence masquée par un ancêtre',"(()=>{node('DIV',{hidden:''},[node('SPAN',{id:'lab'},[txt('Fermer')])]);return node('BUTTON',{'aria-labelledby':'lab'});})()",'Fermer'),
    ]
    for title,expr,want in cases:
        got=js('process.stdout.write(JSON.stringify(candidate('+expr+').candidate));')
        expect('C',title,got,want)
    expect('C','pseudo contenu : cas non couvert',js("process.stdout.write(JSON.stringify(candidate(node('BUTTON',{generated:'\"Fermer\"'})).uncertain));"),True)
    expect('C','valeur native implicite : cas non couvert',js("process.stdout.write(JSON.stringify(candidate(node('INPUT',{type:'submit'})).uncertain));"),True)
    for label,opacity,bg,fg,ancestor,want in [
        ('opacité sur le texte et son fond',0.5,'rgb(0, 0, 0)','rgb(255, 255, 255)',False,'reserve'),
        ('opacité d’un ancêtre',0.5,'rgb(0, 0, 0)','rgb(255, 255, 255)',True,'reserve'),
        ('texte opaque conforme',1,'rgb(0, 0, 0)','rgb(255, 255, 255)',False,'pass'),
        ('texte opaque insuffisant',1,'rgb(255, 255, 255)','rgb(170, 170, 170)',False,'return'),
    ]:
        body="""global.SVGElement=class {};const body=node('BODY');
        const e=node('DIV',{},[txt('Texte')],{backgroundColor:BG,color:FG});e.parentElement=body;
        (ANCESTOR?body:e).style.opacity=OPACITY;
        document.createElement=()=>({getContext:()=>({})});document.documentElement={lang:'fr'};document.title='test';
        document.querySelectorAll=s=>s==='body *'?[e]:[];
        const a=(AUDIT)('unused');process.stdout.write(JSON.stringify(a.groupOpacity.length?'reserve':a.contrast.length?'return':'pass'));"""
        body=body.replace('BG',json.dumps(bg)).replace('FG',json.dumps(fg)).replace('ANCESTOR',json.dumps(ancestor)).replace('OPACITY',json.dumps(str(opacity))).replace('AUDIT',cr.AUDIT_JS)
        expect('C',label,js(body),want)
    keyboard_setup=r"""
    global.window={};const body=node('BODY');const a=node('BUTTON'),b=node('BUTTON');a.parentElement=b.parentElement=body;
    const controls=[a,b];body.querySelectorAll=()=>controls;body.insertBefore=()=>{};
    document.body=body;document.documentElement=node('HTML');document.activeElement=body;
    document.querySelectorAll=s=>s==='dialog[open]'?[]:controls;
    const focusable=e=>{e.matches=()=>false;e.focus=()=>{document.activeElement=e;};e.blur=()=>{document.activeElement=body;};return e;};
    controls.forEach(focusable);document.createElement=()=>focusable(node('SPAN'));
    const baseline=(BASELINE),focus=(FOCUS);
    """.replace('BASELINE',cr.BASELINE_JS).replace('FOCUS',cr.FOCUS_JS)
    expect('C','inventaire de deux boutons sans identifiant',js(keyboard_setup+"const k=baseline('unused');process.stdout.write(JSON.stringify(k.expected.map(x=>x.key)));"),['control-0','control-1'])
    expect('C','arrêts homonymes gardent deux identités',js(keyboard_setup+"baseline('unused');a.focus();const x=focus();b.focus();const y=focus();process.stdout.write(JSON.stringify([x.key,y.key]));"),['control-0','control-1'])
    expect('C','un seul bouton répété clôt le cycle',js(keyboard_setup+"baseline('unused');a.focus();focus();process.stdout.write(JSON.stringify(focus().cycle));"),True)
    expect('C','retour à la page : raison de fin observable',js(keyboard_setup+"baseline('unused');document.activeElement=body;process.stdout.write(JSON.stringify(focus().end));"),True)
    expect('C','contrôle masqué hors inventaire actif',js(keyboard_setup+"b.style.display='none';const k=baseline('unused');process.stdout.write(JSON.stringify([k.expected.length,k.excluded.length]));"),[1,1])
    audit_setup = r"""
    global.SVGElement=class {};const body=node('BODY');
    document.createElement=()=>({getContext:()=>({})});document.documentElement={lang:'fr'};document.title='test';
    const audit=(AUDIT);
    """.replace('AUDIT', cr.AUDIT_JS)
    text_cases = [
        ('valeur input ignorée auparavant', "node('INPUT',{type:'text',value:'Texte'},[],{color:'rgb(170,170,170)'})", RESERVE),
        ('placeholder ignoré auparavant', "node('INPUT',{type:'text',placeholder:'Nom'})", RESERVE),
        ('textarea courant sans childNode', "node('TEXTAREA',{value:'Texte'})", RESERVE),
        ('textarea vide avec ancienne valeur HTML', "node('TEXTAREA',{},[txt('Ancienne valeur')])", PASS),
        ('placeholder non affiché derrière une valeur espace', "node('INPUT',{type:'text',value:' ',placeholder:'Nom'})", RESERVE),
        ('input vide sans texte', "node('INPUT',{type:'text'})", PASS),
        ('placeholder masqué', "node('INPUT',{placeholder:'Nom'},[],{display:'none'})", PASS),
        ('select natif', "node('SELECT')", RESERVE),
        ('mot de passe : valeur jamais publiée', "node('INPUT',{type:'password',value:'secret-témoin'})", RESERVE),
        ('texte opaque conforme', "node('P',{},[txt('Texte')])", PASS),
        ('texte opaque insuffisant', "node('P',{},[txt('Texte')],{color:'rgb(170,170,170)'})", RETURN),
        ('aria hidden ne dispense pas le texte visible de contraste', "node('P',{'aria-hidden':'true'},[txt('Texte')],{color:'rgb(170,170,170)'})", RETURN),
        ('opacité très faible non nulle', "node('P',{},[txt('Texte')],{opacity:'0.01'})", RESERVE),
        ('texte pseudo détecté', "node('DIV',{generated:'\"Texte\"'})", RESERVE),
    ]
    for title, expr, want in text_cases:
        got = js(audit_setup + 'const e=' + expr + ";e.parentElement=body;document.querySelectorAll=s=>s==='body *'?[e]:[];process.stdout.write(JSON.stringify(audit('unused')));")
        if got is not None:
            expect('C', title, status(cr.interpret(raw_case(audit=got)), 'Contraste'), want)
            if title.startswith('mot de passe'):
                expect('C', 'valeur sensible absente du relevé', 'secret-témoin' in json.dumps(got), False)
    mixed = js(audit_setup + "const p=node('P',{},[txt('Texte')],{color:'rgb(170,170,170)'}),e=node('INPUT',{placeholder:'Nom'});p.parentElement=e.parentElement=body;document.querySelectorAll=s=>s==='body *'?[p,e]:[];process.stdout.write(JSON.stringify(audit('unused')));")
    if mixed is not None:
        expect('C', 'défaut connu prioritaire sur placeholder non évalué', status(cr.interpret(raw_case(audit=mixed)), 'Contraste'), RETURN)
    direct = js(audit_setup + "body.childNodes=[txt('Direct')];document.body=body;body.style.color='rgb(170,170,170)';document.querySelectorAll=()=>[];process.stdout.write(JSON.stringify(audit('unused')));")
    if direct is not None:
        expect('C', 'texte directement dans body couvert', status(cr.interpret(raw_case(audit=direct)), 'Contraste'), RETURN)
        expect('C', 'dénominateur de couverture', direct['contrastCoverage'], {'method':'dom-text-bounded','candidates':1,'evaluated':1,'excluded':0,'unmeasured':[]})
    proof_setup = "global.innerWidth=390;global.innerHeight=844;const parent=node('DIV');const e=node('DIV');e.parentElement=parent;document.querySelector=()=>e;const proof=(" + cr.PROOF_JS + ");"
    rect = "e.getBoundingClientRect=()=>({width:300,height:100,left:LEFT,right:RIGHT,top:TOP,bottom:BOTTOM});"
    for title, left, top, extra, want in [
        ('objet opaque dans écran', 0, 0, '', PASS), ('objet transparent', 0, 0, "e.style.opacity='0';", RETURN),
        ('ancêtre transparent', 0, 0, "parent.style.opacity='0';", RETURN), ('ancêtre display none', 0, 0, "parent.style.display='none';", RETURN),
        ('visibilité masquée', 0, 0, "e.style.visibility='hidden';", RETURN), ('objet hors écran à gauche', -400, 0, '', RESERVE),
        ('visibilité rétablie sur le descendant', 0, 0, "parent.style.visibility='hidden';e.style.visibility='visible';", PASS),
        ('objet hors écran à droite', 500, 0, '', RESERVE), ('objet sous écran', 0, 1000, '', RESERVE),
        ('découpe ancêtre', 0, 0, "parent.style.overflow='hidden';", RESERVE), ('masque objet', 0, 0, "e.style.maskImage='url(mask)';", RESERVE),
    ]:
        dims = rect.replace('LEFT', str(left)).replace('RIGHT', str(left+300)).replace('TOP', str(top)).replace('BOTTOM', str(top+100))
        got = js(proof_setup + dims + extra + "process.stdout.write(JSON.stringify(proof('#p')));")
        if got is not None:
            expect('C', title, status(cr.interpret(raw_case(proof=got), '#p'), 'Objet de preuve'), want)
    return f"{count['C']} cas"


# ---------------------------------------------------------------- Partie B : pages pièges, avec navigateur
PAGES = {
    "oklch.html": '<p style="color:oklch(0.9 0 0)">Texte presque blanc</p>',
    "ombre.html": '<style>button{box-shadow:0 2px 6px rgba(0,0,0,.3);min-width:60px;min-height:40px}button:focus{outline:none}</style><button>Un</button> <button>Deux</button>',
    "zero.html": '<div id="preuve" style="height:0"></div><p>ok</p>',
    "espace.html": '<div style="padding:60px"><button aria-label="Fermer" style="width:20px;height:20px;padding:0">x</button></div>',
    "serre.html": '<div style="display:flex;gap:2px"><button aria-label="A" style="width:16px;height:16px;padding:0">a</button><button aria-label="B" style="width:16px;height:16px;padding:0">b</button></div>',
    "url.html": '<p>Servie en HTTP</p><img alt="" src="https://example.invalid/x.png">',
    "modal.html": ('<button id="open" onclick="document.getElementById(\'d\').showModal();document.getElementById(\'f2\').focus()">Ouvrir</button>'
                   '<dialog id="d"><button id="close">Fermer</button><input id="f1" aria-label="Un"><input id="f2" aria-label="Deux"></dialog>'),
    "svgtexte.html": '<svg viewBox="0 0 200 60" width="200" height="60"><rect width="200" height="60" fill="#1F5563"/><text x="10" y="38" fill="#ffffff" font-size="20">08:31</text></svg>',
    "svgforeignobject.html": '<svg width="200" height="60"><rect width="200" height="60" fill="#111111"/><foreignObject width="200" height="60"><p style="color:#111111">Texte dans une scène SVG</p></foreignObject></svg>',
    "revele.html": '<style>.r{opacity:0;transition:opacity .2s}.r.in{opacity:1}</style><div style="height:2400px"></div><p class="r" style="color:#bbb;background:#fff">Texte révélé au défilement</p><script>new IntersectionObserver(es=>es.forEach(e=>e.isIntersecting&&e.target.classList.add("in"))).observe(document.querySelector(".r"))</script>',
    "propre.html": '<style>button:focus-visible{outline:3px solid #000}</style><p>Texte lisible</p><button>Valider</button>',
    "opacite.html": '<div style="color:white;background:black;opacity:.5">Texte blanc normal</div>',
    "nommasque.html": '<button><span aria-hidden="true">×</span></button>',
    "nomreference.html": '<span id="label" hidden>Fermer</span><button aria-labelledby="label"></button>',
    "dialogferme.html": '<dialog><label for="arrivee">Arrivée</label><input id="arrivee" type="date"><button>Continuer</button></dialog>',
    "ancetremasque.html": '<div style="display:none"><button></button></div>',
    "inatteignable.html": '<button tabindex="-1">Valider</button>',
    "sanscontrole.html": '<p>Texte sans interaction</p>',
    "valeur.html": '<input aria-label="Nom" value="Texte" style="color:#aaa;background:white">',
    "placeholder.html": '<style>input::placeholder{color:#aaa;opacity:1}</style><input aria-label="Nom" placeholder="Nom">',
    "transparent.html": '<div id="preuve" style="width:300px;height:100px;opacity:0">Objet</div>',
    "horscran.html": '<div id="preuve" style="position:absolute;left:-400px;width:300px;height:100px">Objet</div>',
}


def page_html(body: str) -> str:
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>test</title></head><body><h1>Test</h1>{body}</body></html>'


def measure(path: str, *extra: str):
    args = cr.parser().parse_args([path, "--widths", "390", "--wait-ms", "200", *extra])
    raw = cr.measure(args)
    return raw, cr.interpret(raw, args.proof)


def part_b(require: bool) -> str:
    print("Partie B — pages pièges (navigateur)")
    try:
        import playwright.sync_api  # noqa: F401
    except ImportError:
        msg = "NOT-VERIFIED : Playwright absent, pages pièges non exécutées"
        print("  " + msg)
        if require:
            failures.append("B navigateur requis")
        return msg
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        for name, body in PAGES.items():
            (d / name).write_text(page_html(body), encoding="utf-8")
        handler = functools.partial(QuietHandler, directory=tmp)
        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
        threading.Thread(target=server.serve_forever, daemon=True).start()
        try:
            try:
                _, c = measure(str(d / "oklch.html"))
            except cr.BrowserUnavailable as exc:
                msg = "NOT-VERIFIED : Chromium indisponible, pages pièges non exécutées (" + str(exc) + ")"
                print("  " + msg)
                if require:
                    failures.append("B navigateur requis")
                return msg
            expect("B", "couleur oklch presque blanche", status(c, "Contraste"), RETURN)
            try:
                measure(str(d / "oklch.html"), "--browser-executable", str(d / "navigateur-absent"))
                rejected = False
            except cr.BrowserUnavailable:
                rejected = True
            expect("B", "navigateur choisi absent : aucun repli silencieux", rejected, True)
            raw, c = measure(str(d / "ombre.html"))
            expect("B", "ombre permanente sans focus visible", status(c, "Parcours clavier"), RESERVE)
            expect("B", "deux boutons sans id = deux arrêts", len(raw["per_width"][390]["stops"]), 2)
            _, c = measure(str(d / "zero.html"), "--proof", "#preuve")
            expect("B", "objet de preuve de hauteur nulle", status(c, "Objet de preuve"), RETURN)
            _, c = measure(str(d / "svgtexte.html"))
            expect("B", "texte SVG non mesuré sur forme sombre : réserve explicite", status(c, "Contraste"), RESERVE)
            _, c = measure(str(d / "svgforeignobject.html"))
            expect("B", "texte HTML dans SVG : fond des formes non évalué", status(c, "Contraste"), RESERVE)
            _, c = measure(str(d / "espace.html"))
            expect("B", "bouton de 20 px isolé (espacement)", status(c, "Taille"), PASS)
            _, c = measure(str(d / "serre.html"))
            expect("B", "boutons de 16 px collés", status(c, "Taille"), RESERVE)
            raw, c = measure(f"http://127.0.0.1:{server.server_address[1]}/url.html")
            expect("B", "page servie en HTTP chargée", status(c, "Erreurs JavaScript"), PASS)
            expect("B", "ressource d'une autre origine bloquée", raw["blocked"] >= 1, True)
            raw, _ = measure(str(d / "modal.html"), "--click", "#open")
            expect("B", "feuille modale : tabulation depuis son début", raw["per_width"][390]["stops"][:1], ["#close"])
            for filename,prefix,want in [('opacite.html','Contraste',RESERVE),('nommasque.html','Nom accessible',RETURN),
                                         ('nomreference.html','Nom accessible',RESERVE),('inatteignable.html','Parcours clavier',RESERVE),
                                         ('sanscontrole.html','Parcours clavier',PASS)]:
                _,c=measure(str(d/filename));expect('B',filename,status(c,prefix),want)
            for filename in ('dialogferme.html', 'ancetremasque.html'):
                raw,c=measure(str(d/filename))
                expect('B',filename+' aucun faux nom manquant',status(c,'Nom accessible'),PASS)
                expect('B',filename+' aucun contrôle rendu',raw['per_width'][390]['audit']['nameControls'],0)
            _,c=measure(str(d/'propre.html'),'--tab-stops','1')
            expect('B','limite atteinte même avec un bouton observé',status(c,'Parcours clavier'),RESERVE)
            for filename in ('valeur.html', 'placeholder.html'):
                raw,c=measure(str(d/filename));expect('B',filename,status(c,'Contraste'),RESERVE)
                expect('B',filename+' couverture publiée',bool(raw['per_width'][390]['audit']['contrastCoverage']['unmeasured']),True)
            for filename, want in [('transparent.html',RETURN), ('horscran.html',RESERVE)]:
                _,c=measure(str(d/filename),'--proof','#preuve');expect('B',filename,status(c,'Objet de preuve'),want)
            out = Path(tmp) / "r.json"
            code = subprocess.run([sys.executable, str(HERE / "check_render.py"), str(d / "propre.html"), "--widths", "390", "--json", str(out)],
                                  capture_output=True, text=True).returncode
            expect("B", "page propre : code de sortie", code, 0)
            expect("B", "JSON avec provenance AUTOMATED", json.loads(out.read_text(encoding="utf-8"))["provenance"]["method"], "AUTOMATED")
            code = subprocess.run([sys.executable, str(HERE / "check_render.py"), str(d / "oklch.html"), "--widths", "390"], capture_output=True, text=True).returncode
            expect("B", "page fautive : code de sortie", code, 1)
            _, c = measure(str(d / "revele.html"))
            expect("B", "contenu révélé au défilement : mesuré (contraste faible détecté)", status(c, "Contraste"), RETURN)
            raw, _ = measure(str(d / "propre.html"), "--captures", str(d / "captures"))
            png = Path(raw["captures"][0]).read_bytes() if raw["captures"] else b""
            expect("B", "capture pleine page écrite (PNG)", [Path(p).name for p in raw["captures"]] + [png[:8] == b"\x89PNG\r\n\x1a\n"], ["capture-390px.png", True])
        finally:
            server.shutdown()
    return f"{count['B']} cas"


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):  # pas de bruit dans la sortie des tests
        pass


def main() -> int:
    ap = argparse.ArgumentParser(description="Tests de comportement de check_render.py.")
    ap.add_argument("--require-browser", action="store_true", help="échouer si Playwright est absent")
    ap.add_argument("--skip-browser", action="store_true", help="exécuter uniquement A et C, sans navigateur")
    args = ap.parse_args()
    part_a()
    c = part_c()
    b = 'NOT-VERIFIED : navigateur écarté explicitement' if args.skip_browser else part_b(args.require_browser)
    if args.skip_browser and args.require_browser:
        failures.append('options incompatibles : --skip-browser et --require-browser')
    if failures:
        print(f"CHECK_RENDER TESTS FAILED — {len(failures)} échec(s) : " + ", ".join(failures))
        return 1
    print(f"CHECK_RENDER TESTS PASSED — A : {count['A']} cas ; C : {c} ; B : {b}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
