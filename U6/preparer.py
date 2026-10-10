"""Fige les paquets, moyens et briefs avant toute génération."""
from pathlib import Path
import hashlib, json, random, shutil, subprocess, zipfile
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
REPO = Path('/workspace/DESIGN-GOVERNANCE1')
if (ROOT/'protocole.json').exists() or (ROOT/'runs').exists():
    raise SystemExit('Préparation existante : aucun protocole, paquet ou résultat ne sera écrasé. Utiliser un nouveau dossier et adapter ses chemins avant une nouvelle expérience.')
versions = {'ancien':'99caa027ddf08b077ab6664365df2f91e266ae66', 'nouveau':'6e5a8c2a9016b31969051499b1c895a116fd75b4'}
briefs = {
    'B2':'Il me faut une landing page pour notre SaaS de facturation.',
    'B4':'Il me faut une landing page pour notre atelier de réparation de vélos, avec prise de rendez-vous.',
}
conditions = [('B2','ancien',1),('B2','nouveau',1),('B2','nouveau',2),('B2','ancien',2),('B4','nouveau',1),('B4','ancien',1)]
labels = list('ABCDEF')
random.Random(1062026).shuffle(labels)
font_sources = {
    'manrope.ttf':'/workspace/maison-lisiere/assets/fonts/manrope.ttf',
    'instrument-serif.ttf':'/workspace/maison-lisiere/assets/fonts/instrument-serif.ttf',
    'instrument-serif-italic.ttf':'/workspace/maison-lisiere/assets/fonts/instrument-serif-italic.ttf',
    'dejavu-sans.ttf':'/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
    'dejavu-sans-bold.ttf':'/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
    'dejavu-serif.ttf':'/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',
    'dejavu-serif-italic.ttf':'/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf',
    'dejavu-mono.ttf':'/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',
    'OFL-manrope.txt':'/workspace/maison-lisiere/assets/fonts/OFL-manrope.txt',
    'OFL-instrument-serif.txt':'/workspace/maison-lisiere/assets/fonts/OFL-instrument-serif.txt',
    'DejaVu-copyright.txt':'/usr/share/doc/fonts-dejavu-core/copyright',
}
common = ROOT/'moyens'
common.mkdir(parents=True,exist_ok=True)
for name,src in font_sources.items():
    shutil.copy2(src, common/name)
fingerprints = {name:hashlib.sha256((common/name).read_bytes()).hexdigest() for name in font_sources}
(common/'manifest.json').write_text(json.dumps(fingerprints,indent=2)+'\n')
cases = []
for n, ((brief,condition,repeat),label) in enumerate(zip(conditions,labels),1):
    code = f'run-{n:02}'
    case = ROOT/'runs'/code
    packet = case/'paquet'
    packet.mkdir(parents=True,exist_ok=True)
    archive = ROOT/(code+'.zip')
    subprocess.run(['git','archive','--format=zip','--output='+str(archive),versions[condition]],cwd=REPO,check=True)
    with zipfile.ZipFile(archive) as z:
        z.extractall(packet)
    archive.unlink()
    out = case/'livrable'
    out.mkdir(exist_ok=True)
    skill = packet/'agent/skill/SKILL.md'
    entry={'run':code,'brief_id':brief,'condition':condition,'repeat':repeat,'anonymous_label':label,'commit':versions[condition],'brief':briefs[brief],'packet':str(packet),'output':str(out),'skill_sha256':hashlib.sha256(skill.read_bytes()).hexdigest(),'status':'prepared'}
    cases.append(entry)
    (case/'brief.txt').write_text(briefs[brief]+'\n')
protocol = {'frozen_at':datetime.now(timezone.utc).isoformat(),'versions':versions,'briefs':briefs,'run_order':[x['run'] for x in cases],'cases':cases,'font_manifest_sha256':hashlib.sha256((common/'manifest.json').read_bytes()).hexdigest(),'model':'modèle parent hérité, même configuration pour tous, sans override ; identifiant du service et graines de génération non attestés','network':'aucun asset externe ; polices locales communes, CSS/SVG explicites et contenus illustratifs','browser':'/usr/bin/chromium ; Playwright 1.56.0','per_run_budget':'une page ; au plus trois itérations de correction sur capture ; signaler un dépassement de 20 minutes','judges':'deux contextes séparés ; captures seules, briefs, noms anonymes et ordre inversé ; propriétaire ensuite','metrics':['charactères de bibliothèque servis','durée murale observée','contrôles de parcours','jugements pairés','différences de composition et de voix'],'unmeasured':['jetons API','effet général et significativité','choix final du propriétaire']}
(ROOT/'protocole.json').write_text(json.dumps(protocol,ensure_ascii=False,indent=2)+'\n')
(ROOT/'protocole.md').write_text('''# U6 — Comparaison indépendante de la suite de phase 5

Protocole figé avant la première génération. Référence avant : `99caa027` ; après : `6e5a8c2`. Les anciennes pages U3/U5 et Lisière ne sont pas montrées aux producteurs ni utilisées comme témoins.

Six productions en contexte neuf, une à la fois : quatre sur le même brief de facturation (deux par version), puis deux sur un brief nouveau d’atelier de réparation de vélos avec rendez-vous. Ce choix remplace la réutilisation de témoins anciens produits par un autre modèle : il permet une paire avant/après et une répétition à capacités constantes. Il dépasse les trois ou quatre runs envisagés avec réutilisation de témoins, pour éviter ce facteur de confusion.

Même modèle hérité, mêmes outils, même durée indicative, mêmes contraintes de livrable et mêmes polices disponibles. Aucun override de modèle, aucune image générée ou URL externe. Les agents peuvent choisir parmi les polices communes ; aucune palette ni mise en page ne leur est imposée. La seule variation contrôlée est la version du paquet. Les graines internes de génération et l’identifiant exact du service ne sont pas attestés.

Livrable : une page HTML autonome et interactive, une trace à côté, les essais et captures du producteur. La personne ne peut répondre pendant le run ; les hypothèses manquantes sont déclarées et la page reste une proposition. Aucun service réel, paiement, envoi ou disponibilité réelle. Les données et fonctions de démonstration sont marquées comme exemples.

Les producteurs ne voient que leur paquet, leur dossier et les moyens communs. Cette restriction est une consigne, pas un sandbox : elle doit être déclarée comme telle. Les juges ne reçoivent que les briefs et les captures anonymisées, sans code, trace, version ou résultats des autres juges. Deux juges de la même famille, dans des contextes séparés et des ordres inversés, restent un aveugle imparfait.

Critères fixés : direction reconnaissable, pertinence pour le métier, hiérarchie, finition, mobile et clarté de l’action. La vérité et les parcours sont vérifiés séparément dans le navigateur ; une belle capture n’établit pas une interaction correcte. La variété est examinée dans chaque paire de répétitions : différences structurelles utiles, voix typographique et relation au contenu ; aucune obligation d’être différent pour elle-même.

Décision : un défaut fonctionnel connu est rapporté comme régression. Une préférence visuelle n’est pas un verdict technique. Deux répétitions et deux briefs décrivent un échantillon : ils n’établissent ni effet général ni significativité. Le jugement du propriétaire sur R1 à R4 et R9 reste nécessaire avant une préférence finale. Les anciens essais U3/U5 ne servent qu’à formuler la question.

Coût : mesurer les caractères effectivement servis par le lecteur instrumenté et la durée murale. Les jetons restent non mesurés si l’outil ne rapporte aucun compteur fiable ; aucun ratio de caractères ne les remplace. Le temps inclut la navigation et les outils, et peut dépendre du service. Traces et captures complètes sont conservées, ainsi que les échecs.

Maximum indicatif : une page et trois tours de correction sur capture par run. Un dépassement de vingt minutes est signalé ; aucun résultat n’est supprimé ni remplacé silencieusement. Les contrôles postérieurs ne réécrivent pas les artefacts figés du producteur.
''')
print('Protocole figé ; six paquets prêts, mêmes moyens et briefs. Aucune génération lancée.')
