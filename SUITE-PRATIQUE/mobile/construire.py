#!/usr/bin/env python3
"""Embarque les deux fontes déjà fournies et leurs licences dans le prototype."""
import base64
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESOURCES = ROOT / 'fonts'
html = (ROOT / 'index.template.html').read_text()
for marker, name in [('__MANROPE__', 'manrope.ttf'), ('__INSTRUMENT__', 'instrument-serif.ttf')]:
    html = html.replace(marker, base64.b64encode((RESOURCES / name).read_bytes()).decode('ascii'))
licenses = '\n\n'.join((RESOURCES / name).read_text() for name in ['OFL-manrope.txt', 'OFL-instrument-serif.txt'])
html = html.replace('</head>', '<!-- Fontes OFL embarquées. Licences :\n' + licenses.replace('--', '—') + '\n-->\n</head>')
(ROOT / 'index.html').write_text(html)
(ROOT / 'licences-fontes.txt').write_text(licenses)
print('Prototype autonome construit :', len(html.encode()), 'octets')
