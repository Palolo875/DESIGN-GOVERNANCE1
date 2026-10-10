from pathlib import Path
r=Path('/workspace/remesure-phase5/runs/run-06/livrable')
p=r/'index.html';s=p.read_text()
arrow='<svg width="17" height="17" viewBox="0 0 20 20" aria-hidden="true"><path d="M4 16L16 4M5 4h11v11" fill="none" stroke="currentColor" stroke-width="1.5"/></svg>'
s=s.replace('<span aria-hidden="true">↗</span>',arrow).replace('>↗</button>','>'+arrow+'</button>')
s=s.replace('.progress{display:flex;', '.progress[hidden]{display:none}.progress{display:flex;')
s=s.replace('target.focus({preventScroll:true});}', 'target.focus();}')
s=s.replace('<head><meta charset="utf-8">','<head><meta charset="utf-8"><link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 32 32\'%3E%3Ccircle cx=\'16\' cy=\'16\' r=\'12\' fill=\'none\' stroke=\'%23b83322\' stroke-width=\'3\'/%3E%3C/svg%3E">')
license=(Path('/workspace/remesure-phase5/moyens/OFL-manrope.txt')).read_text()
s=s.replace('<html lang="fr">','<html lang="fr">\n<!-- Police Manrope intégrée, licence :\n'+license+'\n-->')
p.write_text(s)
(r/'OFL-instrument-serif.txt').write_text(Path('/workspace/remesure-phase5/moyens/OFL-instrument-serif.txt').read_text())
# Le résultat final est index.html ; le script de fabrication reste un historique, pas la source de référence.
