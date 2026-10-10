#!/usr/bin/env python3
"""Réduit Manrope aux caractères des supports. Dépendances de fabrication seulement."""
import argparse
import hashlib
import io
import json
from pathlib import Path

import brotli
import fontTools
from fontTools import subset
from fontTools.ttLib import TTFont
from generer import used_characters

ROOT = Path(__file__).resolve().parent
VERSIONS = {'fonttools': '4.60.1', 'brotli': '1.1.0'}


def prepare():
    if fontTools.__version__ != VERSIONS['fonttools'] or brotli.__version__ != VERSIONS['brotli']:
        raise ValueError('Utiliser les versions de supports/fonts/requirements.txt pour une sortie reproductible.')
    source = ROOT / 'fonts/manrope.ttf'
    font = TTFont(source, recalcTimestamp=False)
    requested = {ord(char) for char in used_characters()}
    original = set(font.getBestCmap())
    options = subset.Options()
    options.recalc_timestamp = False
    options.name_IDs = ['*']
    options.name_languages = ['*']
    options.name_legacy = True
    options.layout_features = ['*']
    options.recommended_glyphs = True
    job = subset.Subsetter(options=options)
    job.populate(unicodes=requested & original)
    job.subset(font)
    supported = set(font.getBestCmap())
    assert supported == requested & original, 'Un caractère présent dans l’original a été perdu.'
    font.flavor = 'woff2'
    output = io.BytesIO()
    font.save(output)
    binary = output.getvalue()
    # Vérifier le fichier produit, pas seulement l’objet avant sérialisation.
    restored = TTFont(io.BytesIO(binary))
    assert set(restored.getBestCmap()) == supported
    assert [(a.axisTag, a.minValue, a.maxValue) for a in restored['fvar'].axes] == [('wght', 200.0, 800.0)]
    record = {'tools': VERSIONS, 'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
              'font_sha256': hashlib.sha256(binary).hexdigest(), 'requested_characters': used_characters(),
              'supported_codepoints': sorted(supported), 'fallback_codepoints': sorted(requested - original),
              'weight_axis': [200, 800]}
    return binary, json.dumps(record, ensure_ascii=False, indent=2) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='vérifier la reproduction sans écrire')
    args = parser.parse_args()
    binary, record = prepare()
    font = ROOT / 'fonts/manrope-supports.woff2'
    coverage = ROOT / 'fonts/couverture.json'
    if args.check:
        if not font.is_file() or not coverage.is_file() or font.read_bytes() != binary or coverage.read_text() != record:
            raise SystemExit('Police périmée : relancer supports/preparer_police.py puis supports/generer.py.')
        print('POLICE REPRODUCTIBLE — glyphes, axe de graisses, empreintes et couverture vérifiés')
    else:
        font.write_bytes(binary)
        coverage.write_text(record, encoding='utf-8')
        print('Police réduite :', len(binary), 'octets ;', len(json.loads(record)['supported_codepoints']), 'caractères.')


if __name__ == '__main__':
    main()
