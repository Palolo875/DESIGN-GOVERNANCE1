#!/usr/bin/env python3
"""Refuse un support périmé ou une cible locale absente. Aucun jugement visuel."""
from __future__ import annotations

import importlib.util
import hashlib
import json
import sys
from pathlib import Path
from xml.etree import ElementTree as ET
from validate_design_governance import markdown_anchors

ROOT = Path(__file__).resolve().parents[1]
SUPPORTS = ROOT / 'supports'


def check() -> list[str]:
    errors = []
    try:
        spec = importlib.util.spec_from_file_location('dg_supports_generator', SUPPORTS / 'generer.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        coverage = json.loads((SUPPORTS / 'fonts/couverture.json').read_text(encoding='utf-8'))
        if coverage['requested_characters'] != module.used_characters():
            errors.append('police : couverture périmée ; régénérer la police puis les supports')
        for key, name in [('source_sha256', 'manrope.ttf'), ('font_sha256', 'manrope-supports.woff2')]:
            if coverage[key] != hashlib.sha256((SUPPORTS / 'fonts' / name).read_bytes()).hexdigest():
                errors.append('police : empreinte différente : ' + name)
        expected = module.render_outputs()
        for name, text in expected.items():
            path = SUPPORTS / name
            if not path.is_file() or path.read_text(encoding='utf-8') != text:
                errors.append(name + ' : sortie absente ou périmée ; régénérer les supports')
            limit = 100_000 if name.endswith('.html') else 50_000 if name.endswith('.svg') else None
            if limit and len(text.encode('utf-8')) > limit:
                errors.append(name + ' : budget de poids dépassé (' + str(limit) + ' octets)')
        for name in ['systeme', 'parcours', 'boucle']:
            data = json.loads((SUPPORTS / (name + '.json')).read_text(encoding='utf-8'))
            ids = [node['id'] for node in data['nodes']]
            if len(set(ids)) != len(ids): errors.append(name + ' : identifiant de partie répété')
            entries = data['entries']
            if len({e['id'] for e in entries}) != len(entries): errors.append(name + ' : identifiant de choix répété')
            for entry in entries:
                if not set(entry['focus']).issubset(ids): errors.append(name + ' : choix lié à une partie absente')
            if data.get('feedback') and not {data['feedback']['from'], data['feedback']['to']}.issubset(ids):
                errors.append(name + ' : retour lié à une partie absente')
            def inspect(value):
                if isinstance(value, dict):
                    if 'target' in value:
                        target, _, fragment = value['target'].partition('#')
                        path = (ROOT / target).resolve()
                        if not path.is_relative_to(ROOT) or not path.is_file():
                            errors.append(name + ' : cible absente ou hors paquet : ' + target)
                        elif fragment and path.suffix == '.md' and fragment not in markdown_anchors(path.read_text(encoding='utf-8')):
                            errors.append(name + ' : ancre absente : ' + value['target'])
                    for child in value.values(): inspect(child)
                elif isinstance(value, list):
                    for child in value: inspect(child)
            inspect(data)
        ns = {'s': 'http://www.w3.org/2000/svg'}
        license_text = (SUPPORTS / 'fonts/OFL-manrope.txt').read_text(encoding='utf-8')
        for name in expected:
            if not name.endswith('.svg'): continue
            svg = ET.fromstring(expected[name])
            if svg.find('s:title', ns) is None or svg.find('s:desc', ns) is None: errors.append(name + ' : alternative absente')
            if svg.find('s:metadata', ns).text != license_text: errors.append(name + ' : licence embarquée différente')
    except (OSError, ValueError, KeyError, TypeError, ET.ParseError) as exc:
        errors.append('lecture ou construction impossible : ' + str(exc))
    return errors


if __name__ == '__main__':
    errors = check()
    for error in errors: print('- ' + error)
    print('SUPPORTS VALIDATION ' + ('FAILED' if errors else 'PASSED') + ' — fraîcheur, cibles et alternatives ; rendu non évalué')
    raise SystemExit(bool(errors))
