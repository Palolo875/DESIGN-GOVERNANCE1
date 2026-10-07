#!/usr/bin/env python3
"""Validateur de structure : gardes de propriété « une chose, un lieu ».

Gardes :
  1. CONCEPTS — un concept protégé est repéré par une balise invisible `<!-- concept:ID -->` placée juste
     avant sa définition. La balise existe une seule fois, dans le fichier propriétaire, suivie d'un bloc
     non vide (au moins 12 mots) ; toute balise hors registre est refusée.
  2. RENVOIS — une route qui dépend d'un concept cite un locator dont le bloc servi contient ce concept
     (atteignabilité en un saut).
  3. VOCABULAIRE RETIRÉ — un terme remplacé par décision n'apparaît plus hors de l'historique (CHANGELOG).
  4. FIDÉLITÉ DES RÉSUMÉS — tout lieu qui résume une règle en garde la condition canonique.
  5. GLOSSAIRE — chaque terme du vocabulaire de fabrication a sa ligne dans GLOSSAIRE.md.
  6. LIGNES DE TABLE UNIQUES — dans un même fichier, deux lignes de table d'au moins 8 mots ne sont pas identiques.
  7. REGISTRE — les façades humaines vouvoient (formes de tutoiement impératif refusées dans QUICKSTART).
  8. NOYAU — les blocs `<!-- noyau:début ID -->` / `<!-- noyau:fin ID -->` sont appariés, uniques et placés
     dans les sources normatives ; la section compilée de la skill est identique à `scripts/build_core.py`.
 11. CHOIX CONTEXTUELS (garde bornée) — refuse le retour des formulations universelles retirées et les impératifs
     universels explicites (« toujours », « à tous les »…) sur un traitement ou une famille unique ; accepte un choix situé.
 10. ORDRE — dans DIRECTION, rôle, posture et récapitulatif de protection précèdent les sections détaillées.
  9. CHARGEMENT — une seule table de chargement (`DIRECTION/CHARGE`, et sa copie compilée dans la skill) ;
     les façades y renvoient ; la ligne `DIRECTION` garde le build et l'ordre cible → premier objet ;
     Gate B n'y est chargée qu'en trace complète, comme dans la carte de lecture d'ACTION.
 12. LOCATORS DU VALIDATEUR — un message de `validate_run_card.py` cite un lieu nommé, jamais un numéro de ligne.
 13. ENTRÉE HUMAINE — une seule entrée balisée (README du package, reprise par le README Local), quatre questions,
     aucun mode demandé, vouvoiement ; une seule constitution minimale (ENT-01, CST-01).
 15. PRÉAMBULE DE BIBLIOTHEQUE — ni catégories de lecture ni contrat de promotion avant les routes (MNT-01).
 16. EN-TÊTE DE LA SKILL — métadonnées `name` et `description` lisibles en YAML : valeur citée dès qu'elle porte « : » (SKL-01).
 17. DÉCLENCHEUR UI/UX — `CHARGE` appelle `ACTION/UI-UX-REALITY` en STANDARD et DIRECTION avant fabrication, pas en LITE (UIX-01).
 18. FAÇADES — trace légère et proposition dans les guides, glossaire et carte ; exemple hors domaine de référence ; liens vers « Commencer » (FAC-01).

Une reformulation ne casse pas ces gardes ; une suppression, un déplacement, une copie ou un retour du
vocabulaire retiré les cassent. `scripts/read_route.py` retire les balises à la lecture.

Usage : python3 scripts/validate_structure.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import read_route as rr  # noqa: E402
import build_core as bc  # noqa: E402

OFFICIAL = rr.OFFICIAL
SKILL_DIR = ROOT / "skills" / "design-governance-practice" if (ROOT / "skills").is_dir() else ROOT / "skill"
MARKER = re.compile(r"^\s*<!-- concept:([A-Z0-9][A-Z0-9\-]*) -->\s*$")
LOCATOR = re.compile(r"`((?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE)/[A-Z0-9_\-]+(?:/[A-Z0-9_\-]+)?)`")
MIN_WORDS = 12

# 1. Registre des concepts protégés : identifiant, fichier propriétaire, propriété.
CONCEPTS: list[tuple[str, str, str]] = [
    ("HON-01", "DIRECTION.md", "vérité de scène : exemples marqués, divulgation en langage produit"),
    ("HON-02", "SAVOIR.md", "aucun faux asset présenté comme authentique"),
    ("HON-03", "DIRECTION.md", "plafond déclaré quand une capacité manque (FABRICATION)"),
    ("HON-04", "ACTION.md", "frontière de validation : ce que la machine atteste et n'atteste pas"),
    ("HON-05", "ACTION.md", "agent seul : preuve dégradée et conclusions interdites"),
    ("HON-06", "ACTION.md", "NOT-VERIFIED plutôt qu'un PASS sans preuve"),
    ("HON-07", "ACTION.md", "une capture prouve un rendu, pas une tâche"),
    ("HON-08", "ACTION.md", "droit inconnu : ACCEPTED interdit"),
    ("ANT-01", "SAVOIR.md", "marqueurs de vague datés, pour nommer MODAL"),
    ("MOY-01", "SAVOIR.md", "carte des moyens par couche"),
    ("SOR-01", "ACTION.md", "réponse visible en langage produit, trace sur demande"),
    ("TRA-01", "ACTION.md", "trace légère par défaut ; trace complète si persistant, partagé, audité ou acceptation demandée"),
    ("CHK-01", "ACTION.md", "la première proposition vaut checkpoint, sauf action irréversible ou coûteuse"),
    ("CNT-01", "DIRECTION.md", "destination réelle sans contenu : exemple marqué plutôt qu'emplacements vides"),
    ("TRM-01", "BIBLIOTHEQUE.md", "test de trame : nommer la trame modale du brief, la rompre ou la justifier"),
    ("GTA-01", "ACTION.md", "Gate A par profil de surface : contrôles d'office et contrôles selon le contenu"),
    ("ROL-01", "DIRECTION.md", "rôle de directeur·rice artistique senior, défini une seule fois, en tête de DIRECTION"),
    ("PRC-01", "BIBLIOTHEQUE.md", "tests perceptifs de structure (non-généricité, silhouette, grille), atteignables depuis Gate C"),
    ("EXD-01", "DIRECTION.md", "données d'exemple cohérentes entre elles ; aucun chiffre sans référence"),
    ("TIT-01", "SAVOIR.md", "équilibre d'un titre : coupe par le sens, lignes équilibrées, écart d'échelle net"),
    ("TXI-01", "SAVOIR.md", "texte sur image : zone calme, recadrage ou voile, contraste au point le plus défavorable"),
    ("RCV-01", "SAVOIR.md", "récupération après erreur : message, saisie conservée, focus, reprise observée par interaction"),
    ("ANC-01", "DIRECTION.md", "ancre graduée : explorer sans ancre (limite déclarée), accepter avec ancre, observée ou fournie pour un produit réel"),
    ("VAL-01", "ACTION.md", "promesse du validateur : ce qu'atteste et n'atteste pas une RUN_CARD validée, texte unique"),
    ("ALT-01", "DIRECTION.md", "alternative située : déclenchement en un seul lieu ; leviers SAVOIR ; matérialisation, trace et comparaison ACTION"),
    ("FIN-01", "SAVOIR.md", "activation du craft : signal, savoir, geste conditionné, réinspection et décision"),
]

# 2. Renvois : la route cite un locator dont le bloc contient le concept.
REFERENCES: list[tuple[str, str]] = [
    ("DIRECTION/CREATIVE-BOOT", "ANT-01"),
    ("DIRECTION/VISUAL_TARGET", "MOY-01"),
    ("ACTION/GATE-C", "PRC-01"),
    ("ACTION/GATE-C", "RCV-01"),
    ("SAVOIR/CRAFT/CFT-00", "FIN-01"),
    ("DIRECTION/CHARGE", "FIN-01"),
    ("DIRECTION/DOUBLE-LOOP", "FIN-01"),
    ("ACTION/HANDOFF", "FIN-01"),
    ("ACTION/GATE-C", "FIN-01"),
]

# 3. Vocabulaire retiré : motif, remplacement, fichiers exemptés (historique).
RETIRED: list[tuple[str, str, set[str]]] = [
    (r"vocabulaire perceptuel ci-dessous|le geste retenu est l’un de ses diffs",
     "renvoi stable à SAVOIR/STATE et gestes conditionnels non fermés", {"CHANGELOG.md"}),
    (r"Il est accepté uniquement si la version après", "validité de la comparaison distincte de la version retenue", {"CHANGELOG.md"}),
    (r"Sinon, reconsidère-les", "si rien ne les justifie, reconsidère-les", {"CHANGELOG.md"}),
    (r"dérive cinq artefacts de preuve", "cinq responsabilités de preuve, regroupables", {"CHANGELOG.md"}),
    (r"Établissez le mode", "classer d'abord avec DIRECTION/START, par l'opérateur ou l'agent", {"CHANGELOG.md"}),
    (r"Forme courte LITE non persistante", "forme courte LITE : trace complète d'un LITE clôturé, distincte de la trace légère", {"CHANGELOG.md"}),
    (r"`CLOSED` uniquement si la direction est tenue", "CLOSED décrit la persistance ; le résultat se déclare à part (ACTION/STATUS)", {"CHANGELOG.md"}),
    (r"anti-directions?", "MODAL / PARTI", {"CHANGELOG.md"}),
    (r"MODE — DECISION — CHANGE — PROOF", "réponse visible en langage produit (ACTION/HANDOFF)", {"CHANGELOG.md"}),
    (r"déclenche un (?:nouveau )?checkpoint", "la première proposition vaut checkpoint (ACTION/PIPELINE-DIRECTION)", {"CHANGELOG.md"}),
    (r"checkpoint humain intervient avant le build|demande une validation avant le build",
     "la première proposition vaut checkpoint (ACTION/PIPELINE-DIRECTION)", {"CHANGELOG.md"}),
    (r"\*\*Ce qu’atteste une `RUN_CARD` validée :\*\*", "renvoi à la frontière de validation d'ACTION/RUN_CARD (VAL-01)",
     {"ACTION.md", "CHANGELOG.md"}),
    # Boucle d'édition : une seule description (DIRECTION/DOUBLE-LOOP, copiée dans le noyau). Aucune exemption.
    (r"→ isoler|observer, isoler", "boucle d'édition de DIRECTION/DOUBLE-LOOP (noyau)",
     {"DIRECTION.md", "SKILL.md", "CHANGELOG.md"}),
    (r"Distingue trois niveaux", "un seul modèle de niveaux : Correction, Précision, Intention", {"CHANGELOG.md"}),
    # L'agent lit le noyau et CHARGE ; READING_MAP est une vue pour les personnes.
    (r"seul document canonique de cadrage chargé au démarrage", "noyau compilé et DIRECTION/CHARGE", {"CHANGELOG.md"}),
    (r"utilisez `READING_MAP\.md` comme vue dérivée", "READING_MAP pour une personne ; l'agent charge par DIRECTION/CHARGE",
     {"CHANGELOG.md"}),
    # One-shot : une seule définition (branche one-shot d'ACTION/PIPELINE-DIRECTION).
    (r"Le `one-shot` est une stratégie de préparation", "branche one-shot d'ACTION/PIPELINE-DIRECTION", {"CHANGELOG.md"}),
    (r"cette vue reste interne", "la prise de brief reste dans la trace", {"CHANGELOG.md"}),
    (r"Mandat de fonctionnement|Adopte le niveau d’exigence", "rôle unique (ROL-01)", {"CHANGELOG.md"}),
    (r"`VISUAL_TARGET` la spécifie", "chaîne de lecture interne unique (DIRECTION)", {"CHANGELOG.md"}),
    (r"`DAILY`", "DIRECTION/CHARGE", {"CHANGELOG.md"}),
    (r"ancre fraîche et inspectable|\bancre inspectable\b|Ne dessine jamais une surface identitaire uniquement de mémoire|"
     r"établis une ancre fraîche|bloque la livraison validée, sauf `FAIL-ASSUMED`",
     "ancre graduée (ANC-01, absolu 2 de DIRECTION) ; FAIL-ASSUMED n'accepte jamais", {"CHANGELOG.md"}),
    # Formulations inexactes ou périmées.
    (r"Forme seule, dans la trace|la machine ne le vérifie pas",
     "contrôle machine nommé par mode (CLOSE-PACKAGE, VAL-01)", {"CHANGELOG.md"}),
    (r"la triade d’`ACTION/STATUS` s’applique|sinon la triade d’|porte la triade de `ACTION/STATUS`|\(triade d’`ACTION/STATUS`\)",
     "triade = changée, confirmée, abandonnée ; sinon valeurs de repli", {"CHANGELOG.md"}),
    (r"est définie une seule fois, par `ACTION/CLOSE-PACKAGE`", "paquet défini par CLOSE-PACKAGE, précisé par les routes",
     {"CHANGELOG.md"}),
    (r"Un risque critique exclut `LITE` et `ITER` \(", "exclusion conditionnelle de DIRECTION/START", {"CHANGELOG.md"}),
    (r"Une ancre `transformed` est compatible avec tout verdict", "exigence limitée à DIRECTION", {"CHANGELOG.md"}),
    (r"`decision_change` \(`outcome`, `reason`\)|`direction\.calibration` : `real_constraint`|est abandonnée au profit d|"
     r"abandonnée jusqu’à correction|vérifie le titre exact du propriétaire|sinon la direction est traitée d’abord",
     "références alignées sur le schéma et les propriétaires", {"CHANGELOG.md"}),
    # Une ancre absente reste NOT-VERIFIED ; FAIL-ASSUMED exige un échec connu (ACTION/OVERRIDE).
    # Seul le raccourci « ancre absente → FAIL-ASSUMED » est retiré ; une diffusion limitée
    # d'un échec connu qui « passe par FAIL-ASSUMED » reste une phrase légitime.
    (r"(?:sans (?:l’)?ancre|ancre (?:absente|manquante))[^.]{0,200}(?:passe par|possible par) `FAIL-ASSUMED`|"
     r"`FAIL-ASSUMED` ne permet qu’une diffusion limitée",
     "sans ancre : EXPLORATORY ; FAIL-ASSUMED seulement pour un échec connu", set()),
    # Une seule entrée humaine ; plus de démarrages concurrents ; une seule constitution minimale.
    (r"Démarrage en 90 secondes|démarrage en 90 secondes|Démarrage express|Le chemin en trente secondes|"
     r"Le parcours complet en cinq minutes|Commencer en deux minutes|\| Si vous avez… \|",
     "entrée humaine unique (« Commencer », README du package) ; parcours commun du guide opérateur", {"CHANGELOG.md"}),
    (r"dessinée uniquement de mémoire|coordination du réel et du beau",
     "constitution minimale unique, exacte (README du package, bloc « constitution »)", {"CHANGELOG.md"}),
    # Copies du handoff, instrumentation de lecture, copies du déclenchement de l'alternative.
    (r"conserve au minimum `MODE`|Conservez aussi `MODE`", "renvoi au handoff canonique (ACTION/HANDOFF)", {"CHANGELOG.md"}),
    (r"Charges de lecture à ne pas confondre|Déclare dans la trace la nature de chaque lecture",
     "catégories de lecture de DIRECTION, pour un run instrumenté ou audité", {"CHANGELOG.md"}),
    (r"considère une proposition crédible répondant à un public|Matérialise-la seulement au niveau nécessaire pour comparer|"
     r"sa trace avant le build",
     "alternative située : déclenchement DIRECTION (ALT-01), leviers SAVOIR, matérialisation et trace ACTION", {"CHANGELOG.md"}),
    # Reprise ITER depuis une trace légère ; trace de l'alternative graduée ; ordre de chargement.
    (r"retrouvables dans la session, la `RUN_CARD` ou le manifeste local|retrouvables dans la `RUN_CARD`, le manifeste ou le projet",
     "reprise ITER : la trace légère (ligne de thèse) compte parmi les lieux retrouvables", {"CHANGELOG.md"}),
    (r"Pour chaque alternative, préciser dans la trace existante",
     "trace de l'alternative graduée : trace complète, sinon alternative écartée nommée dans la proposition", {"CHANGELOG.md"}),
    (r"`DIRECTION/CREATIVE-BOOT`, `DIRECTION/EXTERNAL-START` si le brief est vague",
     "prise de brief avant le boot : EXTERNAL-START puis CREATIVE-BOOT", {"CHANGELOG.md"}),
]

# 11. Choix contextuels — garde BORNÉE. Elle ne juge pas le sens d'une phrase quelconque ; elle détecte
#     seulement (a) le retour des formulations universelles retirées, et (b) les impératifs universels explicites
#     (« toujours », « à tous les », « dans tous les cas »…) portant sur un traitement ou une famille unique, sauf négation.
#     Un choix situé (« pour cette série, un seul traitement a été retenu ») est accepté ; la revue juge le reste.
RETIRED_UNIVERSAL = re.compile(r"applique un traitement unique et cohérent|reçoit un traitement unique et justifié|"
                               r"un seul traitement pour les assets moyens|un seul traitement cohérent|Icônes : une seule famille",
                               re.I)
UNIVERSAL = re.compile(r"traitement unique|un seul traitement|une seule famille", re.I)
ALWAYS = re.compile(r"\btoujours\b|systématiquement|dans tous les cas|en toutes circonstances|quel que soit|"
                    r"à tou(?:s|tes) les|pour tou(?:s|tes) les", re.I)
NEGATION = re.compile(r"\bjamais\b|\bne\b|\bn[’']", re.I)


def check_universal(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for path, lines in corpus.items():
        if path.name == "CHANGELOG.md":
            continue
        for para in paragraphs(lines):
            for sentence in re.split(r"(?<=[.!?])\s+", para):
                if RETIRED_UNIVERSAL.search(sentence) or (UNIVERSAL.search(sentence) and ALWAYS.search(sentence)
                                                          and not NEGATION.search(sentence)):
                    errors.append(f"[UNI-01] choix présenté comme universel ({path.name}) : « {sentence[:90]}… »")


# 10. Ordre de DIRECTION : rôle, posture et récapitulatif de protection avant les sections détaillées.
ORDER: list[tuple[str, str]] = [("## Rôle", "## DIRECTION/START"),
                                ("## Posture — à lire avant toute action", "## DIRECTION/START"),
                                ("### Récapitulatif de protection", "## DIRECTION/START")]

# 4. Fidélité des résumés : tout paragraphe qui contient le déclencheur contient la condition canonique.
FIDELITY: list[tuple[str, str, str]] = [
    ("prise de brief", r"au plus trois", "destination si elle est incertaine"),
    ("checkpoint", r"checkpoint[^.]{0,60}avant (?:le )?build|avant (?:le )?build[^.]{0,60}checkpoint", "irréversible ou coûteuse"),
    ("question de convergence", r"Question de convergence", "police de titre"),
    ("carte des moyens", r"\*\*Carte des moyens par couche\*\*", "chaque ressource retenue"),
    ("relecture de l'ensemble", r"la correction a affaibli", "l’ensemble"),
    ("titre : composition voulue", r"\*\*Équilibre d’un titre\.\*\*", "on le garde si"),
    ("récupération : focus selon le moment", r"\*\*Récupération après erreur\.\*\*", "sans déplacer le focus"),
    # Cohérence ciblée
    ("promesse du validateur par mode", r"Ce qu’elle n’atteste pas", "invariants communs"),
    ("arrêt one-shot et B1b",
     r"branche `one-shot` est une exécution raccourcie|`one-shot` est une branche raccourcie|rendu one-shot peut être clôturé", "B1b"),
    ("protection de niveau", r"Un risque critique que le changement touche", "strictement local"),
    ("scopes de la direction et de l'artefact", r"Direction qualifiée", "distinct d’`artifact.scope`"),
    ("B1b et decision_change", r"`confirmed`, `modified` ou `abandoned`", "`CHANGED`"),
    ("COMPONENTS en SYSTÈME", r"`ACTION/RUN-SYSTEM` \+ `BIBLIOTHEQUE/COMPONENTS`", "si un composant change"),
    ("zéro contrat", r"Zéro contrat est valide", "`production_contracts`"),
    ("champ voisin", r"jamais glissé dans un champ voisin", "non prévu par cette table"),
    # Répétitions retirées
    ("lecture instrumentée : ouverture", r"distingue dans la trace :", "run instrumenté ou audité"),
    ("lecture instrumentée : déclaration", r"déclare dans la trace la catégorie de lecture", "run instrumenté ou audité"),
    ("trace de l'alternative graduée", r"la raison de son niveau de matérialisation", "En trace légère"),
    ("signal de matière (PRINT_FIELD)", r"Trois cartes égales sous un titre centré", "`MODIFIER/PRINT_FIELD`"),
    # Parcours
    ("checkpoint : valider n'est pas accepter", r"la personne valide, réoriente ou arrête", "pas une acceptation"),
    ("entrée humaine : valider ou retenir", r"\*\*4\. Comment poursuivre \?\*\*", "vrai produit"),
    ("prise de brief : construire dans le même tour", r"\*\*Prise de brief\.\*\*", "dans le même tour"),
    ("sortie des routes en trace légère", r"\*\*Sortie\.\*\* Paquet `(?:LITE|ITER|STANDARD|SYSTÈME)`", "Trace légère : la proposition"),
    ("réponse visible : alternative écartée", r"Pourquoi : la thèse", "l’alternative écartée"),
    # Une route RUN-* ne prescrit DECIDED puis CLOSED qu'en trace complète (TRA-01)
    ("clôture des routes en trace complète", r"\*\*Clôture\.\*\*[^.]{0,40}`DECIDED`", "En trace complète"),
    # Une valeur inconnue ne retire pas l'action principale ; elle reste fonctionnelle et marquée
    ("contenu marqué : action principale", r"\*\*Destination réelle sans contenu\.\*\*", "action principale"),
    # Ancre, trace complète, règle CTA, lecture de l'agent, veille
    ("ancre absente : pas de FAIL-ASSUMED, pipeline", r"Sans ancre utile et spec exploitable", "échec connu"),
    ("preuve indisponible : pas de FAIL-ASSUMED", r"Si une preuve est indisponible, le mode ne baisse pas", "échec connu"),
    ("trace persistante en trace complète", r"conserve(?:nt)? une trace persistante", "trace complète"),
    ("FAST-PATH : clôture en trace complète", r"clôture avec (?:la forme courte LITE|le paquet de son mode)", "trace complète"),
    ("sélection structurelle persistée en trace complète", r"sélection structurelle[^.?]{0,40}persisté", "trace complète"),
    ("flux : fermer en trace complète", r"[Dd]écider et fermer", "trace complète"),
    ("exemples : niveau de trace", r"Les champs affichés respectent les contrats d’ACTION", "trace complète"),
    ("règle CTA : valeur d'exemple marquée", r"Un CTA doit soit déclencher", "CNT-01"),
    ("flux : READING_MAP pour une personne", r"la section « Combinaisons par résultat recherché » de `READING_MAP", "si une personne le demande"),
    ("veille : signaux à confirmer", r"\*\*Marqueurs de vague\*\*", "Signaux à confirmer"),
    # Une seule liste de chargement, plancher SAVOIR dans le noyau, lieu de la trace légère
    ("carte d'ACTION : vue de CHARGE", r"\*\*Socle pour tous les modes", "DIRECTION/CHARGE"),
    ("ACTION, responsabilité : chargement par CHARGE", r"est le propriétaire des preuves exécutables, des gates, des statuts de run", "DIRECTION/CHARGE"),
    ("déclencheurs critiques : conditionnels, par CHARGE", r"\| Détail final susceptible", "DIRECTION/CHARGE"),
    ("ACTION/ROUTING : renvoi à CHARGE", r"DIRECTION déclenche la classification générale", "DIRECTION/CHARGE"),
    ("SAVOIR/READ : plancher dans le noyau", r"\*\*Chemin minimal\.\*\* Décide d’abord", "noyau"),
    ("trace légère : lieu", r"\*\*Trace légère par défaut\.\*\*", "à côté de l’artefact"),
    # Ancre et FAIL-ASSUMED
    ("ancre et FAIL-ASSUMED", r"sans (?:l’)?ancre[^.]{0,200}`FAIL-ASSUMED`|ancre (?:absente|manquante)[^.]{0,200}`FAIL-ASSUMED`|"
     r"`FAIL-ASSUMED`[^.]{0,120}ancre (?:absente|manquante)", "échec connu"),
    # Procédure et fabrication
    ("RUN-DIRECTION : CLOSED distinct du résultat", r"puis `CLOSED` lorsque l’artefact et la trace sont persistés", "ACTION/STATUS"),
    ("FAST-PATH : paquet du mode, ITER vers ITER", r"Pour `LITE` et les petits `ITER`", "paquet `ITER` pour un `ITER`"),
    ("niveau requis : preuve manquante distincte du N/A", r"Obligation spécialisée\. \|", "NOT-VERIFIED"),
    ("recherche : confirmation distincte du N/A", r"Une recherche de domaine et une recherche de calibration visuelle", "confirmation"),
    ("module sans effet : confirmation distincte du N/A", r"Quelle décision concrète a changé grâce à ce module", "confirmation"),
    ("QUICKSTART, fermeture : preuve manquante distincte du N/A", r"la preuve attendue est obtenue ou déclarée", "ne vaut que si la preuve ne s’applique pas"),
    ("règle d'or 8 : réserve structurée recevable", r"ne compense jamais un axe bloquant par une moyenne", "ACCEPTED-WITH-RESERVATION"),
    ("contenu marqué : fonctions d'un produit fictif", r"\*\*Destination réelle sans contenu\.\*\*", "fonctions, intégrations et conformités affirmées"),
    # Façades dérivées des contrats stabilisés
    ("QUICKSTART : suite par défaut, la proposition", r"choisissez une seule suite", "trace complète"),
    ("QUICKSTART : niveau de trace distinct du mode", r"Une sortie de run a deux formes : la \*\*réponse visible\*\*", "trace légère"),
    ("QUICKSTART : sortie one-shot selon la trace", r"la sortie one-shot peut être une décision directement clôturée", "trace complète"),
    ("QUICKSTART : l'agent lit le noyau et CHARGE", r"L’agent localise le package réellement fourni", "DIRECTION/CHARGE"),
    ("QUICKSTART : la ligne de run suit le classement", r"Pour piloter un run, commencez ici", "DIRECTION/START"),
    ("READING_MAP : sortie par défaut", r"^Sortie : réponse visible", "trace légère"),
    ("README : parcours, proposer ou fermer", r"Le parcours complet d’un run est", "trace légère"),
    ("flux : la proposition vaut checkpoint", r"présenter la proposition \(trace légère", "checkpoint"),
    ("HANDOFF : forme courte LITE distincte de la trace légère", r"\*\*Forme courte LITE", "distincte de la trace légère"),
    ("exemples : la sortie par défaut porte sa trace légère", r"montre la sortie par défaut", "trace légère"),
    # Raccords de chargement et de précision
    ("SAVOIR/STYLE : FRAME conditionnel comme dans CHARGE", r"Le parcours est : `DIRECTION/START → SAVOIR/FRAME", "si le cadrage est à éclaircir"),
    ("contrat de composant : delta local qualifié", r"S’applique à un pattern réutilisable, à un composant critique ou à un composant partagé", "reclasser"),
    ("avant/après : version retenue, l'original possible", r"La comparaison est valide si elle isole la décision", "l’original"),
    ("test de masquage : dépendance porteuse recevable", r"Si texte, données et images sont masqués", "dépendance est recevable"),
]

# 13. Entrée humaine : une seule entrée, balisée dans le README du package et reprise par le README Local ;
#     quatre questions ; aucun mode interne demandé ; vouvoiement. Une seule constitution minimale, balisée au même lieu.
ENTRY = re.compile(r"<!-- entree:début -->(.*?)<!-- entree:fin -->", re.S)
CONSTITUTION = re.compile(r"<!-- constitution:début -->(.*?)<!-- constitution:fin -->", re.S)
QUESTIONS = ("**1. Que demander ?**", "**2. Que fournir ?**", "**3. Que recevoir ?**", "**4. Comment poursuivre ?**")
MODE_ASKED = re.compile(r"`(?:LITE|ITER|STANDARD|DIRECTION|SYSTÈME)`|MODE —")
CONSTITUTION_SIGNATURE = "le réel et le beau sont cadrés ensemble"


def check_entry(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    readme = ROOT / "README.md"
    if not readme.is_file():
        errors.append("[ENT-01] README.md absent à la racine du package")
        return
    text = readme.read_text(encoding="utf-8")
    entries = ENTRY.findall(text)
    if len(entries) != 1:
        errors.append(f"[ENT-01] entrée humaine balisée {len(entries)} fois dans README.md (attendu : 1)")
    else:
        block = entries[0]
        for question in QUESTIONS:
            if question not in block:
                errors.append(f"[ENT-01] question absente de l'entrée humaine : {question}")
        asked = MODE_ASKED.search(block)
        if asked:
            errors.append(f"[ENT-01] l'entrée humaine demande un mode interne : « {asked.group(0)} »")
        familiar = re.search(TUTOIEMENT.pattern, block, re.I)  # insensible à la casse (début de phrase)
        if familiar:
            errors.append(f"[ENT-01] registre : tutoiement « {familiar.group(0)} » dans l'entrée humaine")
        if block.count("retenir cette direction pour") > 1:  # une seule mention, à la question 4
            errors.append("[ENT-01] redite : « retenir cette direction pour » plus d'une fois dans l'entrée humaine")
    constitutions = CONSTITUTION.findall(text)
    if len(constitutions) != 1 or CONSTITUTION_SIGNATURE not in constitutions[0]:
        errors.append("[CST-01] constitution minimale absente, multiple ou inexacte dans README.md (bloc « constitution »)")
    for path, lines in corpus.items():
        if path.resolve() == readme.resolve() or path.name == "CHANGELOG.md":
            continue
        if any(CONSTITUTION_SIGNATURE in line for line in lines):
            errors.append(f"[CST-01] copie de la constitution minimale hors du README : {path.name}")


# 15. Préambule de BIBLIOTHEQUE : ni instrumentation de lecture ni contrat de promotion avant les routes.
def check_preamble(errors: list[str]) -> None:
    text = (OFFICIAL / "BIBLIOTHEQUE.md").read_text(encoding="utf-8")
    start, end = text.find("## Responsabilité"), text.find("## BIBLIOTHEQUE/READ")
    if start < 0 or end < 0:
        errors.append("[MNT-01] préambule de BIBLIOTHEQUE introuvable")
        return
    preamble = text[start:end]
    for marker in ("STARTUP-NOMINAL", "AUDIT-READ", "### Contrat minimal par périmètre"):
        if marker in preamble:
            errors.append(f"[MNT-01] maintenance dans le préambule de BIBLIOTHEQUE (lu en premier) : « {marker} »")


# 14. Cartes réunies : les combinaisons par résultat vivent dans READING_MAP ; ORCHESTRATION_MAP n'est qu'un pointeur.
def check_maps(errors: list[str]) -> None:
    reading = (OFFICIAL / "READING_MAP.md").read_text(encoding="utf-8")
    if reading.count("## Combinaisons par résultat recherché") != 1:
        errors.append("[MAP-01] READING_MAP doit porter une seule section « Combinaisons par résultat recherché »")
    pointer = OFFICIAL / "ORCHESTRATION_MAP.md"
    if pointer.is_file():
        text = pointer.read_text(encoding="utf-8")
        if any(line.startswith("|") or line.startswith("## ") for line in text.splitlines()) or len(text.split()) > 80:
            errors.append("[MAP-01] ORCHESTRATION_MAP porte de nouveau un contenu propre (pointeur de compatibilité attendu)")


# 12. Locators numériques : un message du validateur cite un lieu nommé, jamais un numéro de ligne.
NUMERIC_LOCATOR = re.compile(r"\((?:[^()]*, )?(?:DIRECTION|ACTION|SAVOIR|BIBLIOTHEQUE) \d+\)")


def check_numeric_locators(errors: list[str]) -> None:
    path = ROOT / "scripts" / "validate_run_card.py"
    if not path.is_file():
        return
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if "ValidationError(" in line and NUMERIC_LOCATOR.search(line):
            errors.append(f"[LOC-01] locator numérique dans un message du validateur : validate_run_card.py:{i + 1}")

# 5. Termes du vocabulaire de fabrication présents dans GLOSSAIRE.md (première cellule d'une ligne de table).
GLOSSARY_TERMS = ["Thèse", "Ancre", "Creative Boot", "MODAL", "PARTI", "FABRICATION", "Plafond",
                  "Objet de preuve", "Défaut dominant", "Vérité de scène", "Slop",
                  "Trace légère", "Trace complète", "Première proposition", "Trame modale", "Profil de surface"]

# 7. Registre des façades humaines : formes de tutoiement impératif refusées.
REGISTER_FILES = ["QUICKSTART.md"]
TUTOIEMENT = re.compile(r"\b(?:ne confonds|utilise le|Charge `|active `|Augmente la|ajoute le|garde en tête|reste sur)\b")


# 8. Noyau : fichiers autorisés à porter des blocs.
NORMATIVE = {"DIRECTION.md", "ACTION.md", "SAVOIR.md", "BIBLIOTHEQUE.md"}
NOYAU_MARK = re.compile(r"^<!-- noyau:(début|fin) ([A-Z0-9\-]+) -->$")

# 9. Chargement : en-têtes d'une table de chargement ; lignes de façade qui doivent renvoyer à DIRECTION/CHARGE.
LOAD_HEADERS = re.compile(r"^\|\s*Mode\s*\|\s*(Charger d’abord|Démarrage minimal|Chargement)")  # « Chargement » inclus
LOAD_OWNERS = {"DIRECTION.md", "SKILL.md"}
LOAD_POINTERS = [("QUICKSTART.md", "| Une direction visuelle ouverte |"),
                 ("READING_MAP.md", "| Direction identitaire |"),
                 ("READING_MAP.md", "| **Direction forte et spécifique** |")]


def texts() -> dict[Path, list[str]]:
    files = sorted(OFFICIAL.glob("*.md")) + sorted(SKILL_DIR.rglob("*.md"))
    readme = ROOT / "README.md"
    if readme.is_file():
        files.append(readme)
    return {p: p.read_text(encoding="utf-8").splitlines() for p in files}


def paragraphs(lines: list[str]) -> list[str]:
    out, buf = [], []
    for line in lines:
        if not line.strip():
            if buf:
                out.append(" ".join(buf))
            buf = []
        else:
            buf.append(line)
    if buf:
        out.append(" ".join(buf))
    return out


def check_concepts(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    found: dict[str, list[tuple[Path, int]]] = {}
    for path, lines in corpus.items():
        for i, line in enumerate(lines):
            m = MARKER.match(line)
            if m:
                found.setdefault(m.group(1), []).append((path, i))
    known = {cid for cid, _, _ in CONCEPTS}
    for cid in sorted(set(found) - known):
        errors.append(f"balise hors registre : {cid}")
    for cid, owner, prop in CONCEPTS:
        places = found.get(cid, [])
        if not places:
            errors.append(f"{cid} absent ({prop})")
            continue
        if len(places) > 1:
            where = ", ".join(f"{p.name}:{i + 1}" for p, i in places)
            errors.append(f"{cid} défini {len(places)} fois : {where}")
            continue
        path, i = places[0]
        if path.name != owner or path.parent != OFFICIAL:
            errors.append(f"{cid} hors de son fichier propriétaire ({owner}) : {path.name}")
            continue
        block = []
        for line in corpus[path][i + 1:]:
            if not line.strip():
                break
            block.append(line)
        if len(" ".join(block).split()) < MIN_WORDS:
            errors.append(f"{cid} : bloc vide ou trop court après la balise ({owner}:{i + 1})")


def raw_block(locator: str) -> list[str]:
    path, lines, index = rr.resolve(locator)
    return lines[index:rr.block_end(lines, rr.headings(lines), index)]


def check_references(errors: list[str]) -> None:
    for route, cid in REFERENCES:
        try:
            path, lines, index = rr.resolve(route)
        except rr.RouteError as exc:
            errors.append(f"renvoi {route} → {cid} : route introuvable ({exc})")
            continue
        served = "\n".join(rr.extract(lines, index))
        hit = False
        for loc in sorted(set(LOCATOR.findall(served))):
            try:
                block = raw_block(loc)
            except rr.RouteError:
                continue
            if any(MARKER.match(l) and MARKER.match(l).group(1) == cid for l in block):
                hit = True
                break
        if not hit:
            errors.append(f"renvoi {route} → {cid} : aucun locator cité par la route ne mène au concept")


def check_retired(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for pattern, repl, exempt in RETIRED:
        rx = re.compile(pattern, re.I)
        for path, lines in corpus.items():
            if path.name in exempt:
                continue
            for i, line in enumerate(lines):
                if rx.search(line):
                    errors.append(f"vocabulaire retiré « {pattern} » ({repl}) : {path.name}:{i + 1}")


def check_fidelity(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for name, trigger, needle in FIDELITY:
        rx = re.compile(trigger, re.I)
        for path, lines in corpus.items():
            for para in paragraphs(lines):
                if rx.search(para) and needle not in para:
                    errors.append(f"résumé infidèle ({name}) : {path.name} « {para[:70]}… » sans « {needle} »")


def cell(text: str) -> str:
    return re.sub(r"[`*]", "", text).strip()


def check_glossary(errors: list[str]) -> None:
    g = OFFICIAL / "GLOSSAIRE.md"
    heads = set()
    for line in g.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith("|"):
            parts = line.split("|")
            if len(parts) > 2:
                heads.add(cell(parts[1]))
    for term in GLOSSARY_TERMS:
        if term not in heads:
            errors.append(f"glossaire : terme absent « {term} »")


def check_unique_rows(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for path, lines in corpus.items():
        seen: dict[str, int] = {}
        for i, line in enumerate(lines):
            if not line.lstrip().startswith("|") or re.match(r"^\s*\|[\s\-:|]+\|\s*$", line):
                continue
            key = re.sub(r"[`*\s|]+", " ", line).strip().lower()
            if len(key.split()) < 8:
                continue
            if key in seen:
                errors.append(f"ligne de table en double : {path.name}:{seen[key] + 1} et {i + 1}")
            else:
                seen[key] = i


def check_register(errors: list[str]) -> None:
    for name in REGISTER_FILES:
        for i, line in enumerate((OFFICIAL / name).read_text(encoding="utf-8").splitlines()):
            m = TUTOIEMENT.search(line)
            if m:
                errors.append(f"registre : tutoiement « {m.group(0)} » dans {name}:{i + 1}")


def check_noyau(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    seen: dict[str, str] = {}
    for path, lines in corpus.items():
        open_id = None
        for i, line in enumerate(lines):
            m = NOYAU_MARK.match(line.strip())
            if not m:
                continue
            if path.name not in NORMATIVE or path.parent != OFFICIAL:
                errors.append(f"noyau : balise hors source normative ({path.name}:{i + 1})")
                continue
            kind, bid = m.groups()
            if kind == "début":
                if open_id:
                    errors.append(f"noyau : {bid} ouvert dans {open_id} ({path.name}:{i + 1})")
                if bid in seen:
                    errors.append(f"noyau : bloc {bid} défini deux fois ({seen[bid]} et {path.name})")
                seen[bid] = path.name
                open_id = bid
            else:
                if bid != open_id:
                    errors.append(f"noyau : fin {bid} sans début ({path.name}:{i + 1})")
                open_id = None
        if open_id:
            errors.append(f"noyau : bloc {open_id} non fermé ({path.name})")
    try:
        raw = bc.SKILL.read_bytes()
        bc.check_budget(raw)
        skill = raw.decode("utf-8")
        if bc.render(skill, bc.compile_core()) != skill:
            errors.append("[NOY-02] noyau : la skill diffère de sa compilation (scripts/build_core.py)")
    except (bc.CoreError, OSError, UnicodeError) as exc:
        errors.append(f"noyau : {exc}")


def load_row(lines: list[str], mode: str) -> str:
    rows = [l for l in lines if l.startswith(f"| **{mode}** |")]
    return rows[0] if len(rows) == 1 else ""


def check_load(corpus: dict[Path, list[str]], errors: list[str]) -> None:
    for path, lines in corpus.items():
        for i, line in enumerate(lines):
            if LOAD_HEADERS.match(line) and path.name not in LOAD_OWNERS:
                errors.append(f"[CHG-05] chargement : table de chargement hors DIRECTION/CHARGE ({path.name}:{i + 1})")
    for name, prefix in LOAD_POINTERS:
        rows = [l for l in (OFFICIAL / name).read_text(encoding="utf-8").splitlines() if l.startswith(prefix)]
        if rows and not all("`DIRECTION/CHARGE`" in r for r in rows):
            errors.append(f"[CHG-06] chargement : {name} redéfinit la liste « {prefix.strip('| *')} » au lieu de renvoyer à DIRECTION/CHARGE")
    try:
        path, lines, index = rr.resolve("DIRECTION/CHARGE")
    except rr.RouteError as exc:
        errors.append(f"chargement : DIRECTION/CHARGE introuvable ({exc})")
        return
    served = rr.extract(lines, index)
    body = "\n".join(served)

    def cells(mode: str) -> list[str]:
        r = load_row(served, mode)
        return [c.strip() for c in r.strip().strip("|").split("|")] if r else []
    d = cells("DIRECTION")
    first = d[1] if len(d) > 1 else ""
    vt, fo = first.find("`DIRECTION/VISUAL_TARGET`"), first.find("`DIRECTION/FIRST-OBJECT`")
    if "`ACTION/RUN-DIRECTION`" not in first or "`ACTION/FIRST-RENDER`" not in first or not (0 <= vt < fo):
        errors.append("[CHG-07] chargement : la ligne DIRECTION de DIRECTION/CHARGE doit charger RUN-DIRECTION et FIRST-RENDER, "
                      "et placer VISUAL_TARGET avant FIRST-OBJECT")
    gb, tc = first.find("`ACTION/GATE-B`"), first.find("trace complète")
    if gb >= 0 and not (0 <= tc < gb):
        errors.append("[CHG-08] chargement : en DIRECTION, Gate B n'est chargée qu'en trace complète (ACTION/HANDOFF)")
    carte = [l for l in (OFFICIAL / "ACTION.md").read_text(encoding="utf-8").splitlines()
             if l.startswith("| `DIRECTION` |") and "`ACTION/RUN-DIRECTION`" in l]
    row = carte[0] if len(carte) == 1 else ""
    if not row or ("`ACTION/GATE-B`" in row and "`ACTION/GATE-B` en trace complète" not in row
                   and not 0 <= row.find("trace complète") < row.find("`ACTION/GATE-B`")):
        errors.append("[CHG-09] chargement : la carte de lecture d'ACTION charge Gate B en DIRECTION hors trace complète")
    if "`ACTION/CLOSE-PACKAGE`" not in body or any("Clôture" in l for l in served if l.startswith("| Mode |")):
        errors.append("[CHG-01] chargement : la clôture de chaque mode renvoie à ACTION/CLOSE-PACKAGE, sans colonne de clôture")
    lite = cells("LITE")
    if len(lite) < 3 or "`ITER`" not in lite[2]:
        errors.append("[CHG-02] chargement : depuis LITE, la reclassification inclut ITER")
    sysm = cells("SYSTÈME")
    if len(sysm) < 2 or "`BIBLIOTHEQUE/COMPONENTS` si un composant change" not in sysm[1]:
        errors.append("[CHG-03] chargement : en SYSTÈME, BIBLIOTHEQUE/COMPONENTS seulement si un composant change")
    for mode in ("LITE", "ITER"):
        c = cells(mode)
        if len(c) < 2 or "`ACTION/GATE-A`" not in c[1] or "`ACTION/GATE-B`" not in c[1]:
            errors.append(f"[CHG-04] chargement : en {mode}, Gate A applicable et Gate B du risque sont chargés d'abord")


def check_order(errors: list[str]) -> None:
    lines = (OFFICIAL / "DIRECTION.md").read_text(encoding="utf-8").splitlines()
    for first, then in ORDER:
        a = [i for i, l in enumerate(lines) if l.strip() == first or l.startswith(first + " —")]
        b = [i for i, l in enumerate(lines) if l.strip() == then or l.startswith(then + " —")]
        if len(a) != 1 or len(b) != 1 or a[0] > b[0]:
            errors.append(f"[ORD-01] ordre de DIRECTION : « {first} » doit exister une fois, avant « {then} »")


# Ce que la section compilée de la skill doit porter
CORE_FLOOR = [("| Ajouter seulement si", "colonne « Ajouter seulement si » de DIRECTION/CHARGE"),
              ("`SAVOIR/TOOLS/CONVERGENCE`", "activation conditionnelle des observations datées"),
              ("`SAVOIR/TOOLS/MOYENS`", "activation conditionnelle des ressources par rôle"),
              ("python3 scripts/read_route.py --trouver", "recherche conditionnelle de savoir dans CHARGE"),
              ("sans conclure à l’absence du savoir", "limite de la recherche littérale dans CHARGE"),
              ("Conçois une palette par rôles", "plancher couleur de SAVOIR/CRAFT/CFT-05"),
              ("Choisis une typographie pour ses langues", "plancher typographique de SAVOIR/TYPE"),
              ("Dans le scope de B1b", "portée de l'atelier d'édition et ses deux exceptions"),
              ("`ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée",
               "déclencheur UI/UX avant fabrication"),
              ("fonctions, intégrations et conformités affirmées", "fonctions d'un produit fictif marquées"),
              ("`DIRECTION/DOMAIN-FRAME` si la demande est nouvelle", "déclencheur DOMAIN-FRAME dans CHARGE")]


def check_core_floor(errors: list[str]) -> None:
    text = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    core = text[text.find("<!-- noyau:compilé début -->"):text.find("<!-- noyau:compilé fin -->")]
    for needle, label in CORE_FLOOR:
        if needle not in core:
            errors.append(f"[CORE-01] noyau : {label} absent de la section compilée")


# 16. En-tête de la skill () : métadonnées YAML lisibles par un hôte, sans dépendance tierce.
# Sous-ensemble contrôlé : une paire « clé: valeur » par ligne ; une valeur non citée ne porte ni « : », ni « # »
# précédé d'une espace, ni indicateur initial ; une valeur citée est décodée (doubles : échappements JSON ; simples : '').
SKILL_KEYS = ("name", "description")
PLAIN_FORBIDDEN_START = tuple("[]{}#&*!|>'\"%@`,") + ("- ", "? ", ": ")


def skill_header(text: str) -> tuple[dict[str, str], list[str]]:
    lines = text.splitlines()
    if not lines or lines[0] != "---" or "---" not in lines[1:]:
        return {}, ["en-tête YAML absent (--- en première ligne, puis ---)"]
    values: dict[str, str] = {}
    problems: list[str] = []
    for number, line in enumerate(lines[1:lines.index("---", 1)], start=2):
        key, sep, raw = line.partition(":")
        if not sep or not re.fullmatch(r"[a-z][a-z0-9_-]*", key) or not raw.startswith(" "):
            problems.append(f"ligne {number} : paire « clé: valeur » attendue")
            continue
        raw = raw[1:].rstrip()
        if raw.startswith('"'):
            try:
                value = json.loads(raw)
            except json.JSONDecodeError:
                problems.append(f"{key} : chaîne entre guillemets doubles mal formée")
                continue
        elif raw.startswith("'"):
            if len(raw) < 2 or not raw.endswith("'") or "'" in raw[1:-1].replace("''", ""):
                problems.append(f"{key} : chaîne entre guillemets simples mal formée")
                continue
            value = raw[1:-1].replace("''", "'")
        else:
            if raw.startswith(PLAIN_FORBIDDEN_START) or ": " in raw or " #" in raw or raw.endswith(":"):
                problems.append(f"{key} : valeur non citée contenant « : », « # » ou un indicateur YAML (citer la valeur)")
                continue
            value = raw
        if key in values:
            problems.append(f"{key} : clé répétée")
        values[key] = value
    return values, problems


def check_skill_header(errors: list[str]) -> None:
    path = SKILL_DIR / "SKILL.md"
    if not path.is_file():
        errors.append("[SKL-01] SKILL.md absent")
        return
    values, problems = skill_header(path.read_text(encoding="utf-8"))
    for problem in problems:
        errors.append(f"[SKL-01] en-tête de la skill : {problem}")
    for key in SKILL_KEYS:
        if not values.get(key, "").strip() and not any(problem.startswith(f"{key} :") for problem in problems):
            errors.append(f"[SKL-01] en-tête de la skill : champ {key} absent ou vide")
    if values.get("name") and values["name"] != "design-governance-practice":
        errors.append(f"[SKL-01] en-tête de la skill : name « {values['name']} » ≠ design-governance-practice")


# 17. Déclencheur UI/UX () : dans DIRECTION/CHARGE, la colonne « Charger d'abord » des lignes
# STANDARD et DIRECTION appelle ACTION/UI-UX-REALITY pour une surface UI/UX nouvelle ou substantiellement modifiée ;
# la ligne LITE ne l'appelle pas (un delta local n'est pas une surface nouvelle).
UI_TRIGGER = "`ACTION/UI-UX-REALITY` si la surface UI/UX est nouvelle ou substantiellement modifiée"


def check_ui_trigger(errors: list[str]) -> None:
    source = (OFFICIAL / "DIRECTION.md").read_text(encoding="utf-8")
    start = source.find("## DIRECTION/CHARGE")
    skill = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    places = [("CHARGE", source[start:source.find("\n## ", start + 1)] if start >= 0 else ""),
              ("noyau compilé", skill[skill.find("<!-- noyau:compilé début -->"):skill.find("<!-- noyau:compilé fin -->")])]
    for place, section in places:
        rows = {line.split("|")[1].strip(): line.split("|") for line in section.splitlines() if line.startswith("| **")}
        for mode in ("**STANDARD**", "**DIRECTION**"):
            cells = rows.get(mode)
            if not cells or UI_TRIGGER not in cells[2]:
                errors.append(f"[UIX-01] {place} : la ligne {mode.strip('*')} ne charge pas ACTION/UI-UX-REALITY avant fabrication")
        if "UI-UX-REALITY" in "|".join(rows.get("**LITE**", [])):
            errors.append(f"[UIX-01] {place} : la ligne LITE appelle ACTION/UI-UX-REALITY (delta local)")


# 18. Façades  : lignes de table, sections et liens que les façades doivent porter.
ROW_NEEDLES = [  # (fichier, début de ligne, mot attendu, constat)
    ("GLOSSAIRE.md", "| **Mode** |", "se choisit à part", "C04"),
    ("GLOSSAIRE.md", "| **Run** |", "proposition", "C04"),
    ("GLOSSAIRE.md", "| **Trace légère** |", "plafond atteint et contenus marqués", "C04"),
    ("GLOSSAIRE.md", "| **Livraison** |", "checkpoint", "C33"),
    ("READING_MAP.md", "| **Agent contrôlé** |", "trace complète", "C04"),
    ("DIRECTION.md", "| Décision suffisamment établie |", "trace légère", "C33"),
    ("DIRECTION.md", "| **STANDARD** |", "DIRECTION/DOMAIN-FRAME", "C25"),
    ("DIRECTION.md", "| **DIRECTION** |", "DIRECTION/DOMAIN-FRAME", "C25"),
    ("DIRECTION.md", "| Détail final susceptible", "selon la question ouverte", "C26"),
    ("ACTION.md", "| Token, composant ou blast radius |", "si un composant change", "C26"),
]
EXAMPLE_SECTION = "## DIRECTION — fabrication depuis un brief flou"
COMMENCER = re.compile(r"\]\((?:\.\./)+README\.md#commencer\)")


def check_facades(errors: list[str]) -> None:
    for name, prefix, needle, origin in ROW_NEEDLES:
        path = OFFICIAL / name
        rows = [line for line in path.read_text(encoding="utf-8").splitlines() if line.startswith(prefix)] if path.is_file() else []
        if len(rows) != 1 or needle not in rows[0]:
            errors.append(f"[FAC-01] {name} : ligne « {prefix} » absente, multiple ou sans « {needle} » ({origin})")
    examples = SKILL_DIR / "references" / "examples.md"
    text = examples.read_text(encoding="utf-8") if examples.is_file() else ""
    start = text.find(EXAMPLE_SECTION)
    section = text[start:text.find("\n## ", start + 1)] if start >= 0 else ""
    if not section or "Trace (trace légère" not in section or "PROCHAINE PREUVE" not in section:
        errors.append("[FAC-01] examples.md : la fabrication depuis un brief flou ne montre pas sa trace légère")
    if re.search(r"boulangerie", section, re.I):
        errors.append("[FAC-01] examples.md : exemple dans le domaine du brief de référence")
    for name in ("README.md", "QUICKSTART.md"):
        path = OFFICIAL / name
        if path.is_file() and not COMMENCER.search(path.read_text(encoding="utf-8")):
            errors.append(f"[FAC-01] {name} : la section « Commencer » du README du package n'est pas liée")
    readme = ROOT / "README.md"
    if readme.is_file() and "## Commencer" not in readme.read_text(encoding="utf-8"):
        errors.append("[FAC-01] README du package : titre « Commencer » absent, cible des liens")
    notes = ROOT / "RELEASE_NOTES.md"
    if notes.is_file():
        body = notes.read_text(encoding="utf-8")
        if "lire README et QUICKSTART" in body:
            errors.append("[FAC-01] RELEASE_NOTES : ancien parcours d'agent présenté comme courant")
        # Les notes de version déclarent l'efficacité non vérifiée, l'absence de mesure comparative et la
        # frontière de ce que le validateur atteste.
        for needle in ("**Efficacité : `NOT-VERIFIED`.**", "Aucune mesure comparative", "## Ce que le validateur atteste"):
            if needle not in body:
                errors.append(f"[FAC-01] RELEASE_NOTES : « {needle} » absent")


def check() -> list[str]:
    errors: list[str] = []
    corpus = texts()
    check_concepts(corpus, errors)
    check_references(errors)
    check_retired(corpus, errors)
    check_fidelity(corpus, errors)
    check_glossary(errors)
    check_unique_rows(corpus, errors)
    check_register(errors)
    check_noyau(corpus, errors)
    check_load(corpus, errors)
    check_order(errors)
    check_universal(corpus, errors)
    check_numeric_locators(errors)
    check_entry(corpus, errors)
    check_maps(errors)
    check_preamble(errors)
    check_core_floor(errors)
    check_skill_header(errors)
    check_ui_trigger(errors)
    check_facades(errors)
    return errors


def main() -> int:
    bad = rr.non_utf8(ROOT)  # encodage nommé avant toute lecture (arrêt, pas contrôle complet)
    if bad:
        print(f"STRUCTURE VALIDATION FAILED — Markdown non UTF-8 : {', '.join(bad)}")
        return 1
    errors = check()
    if errors:
        print("STRUCTURE VALIDATION FAILED — gardes de propriété")
        for e in errors:
            print(f"- {e}")
        return 1
    print(f"STRUCTURE VALIDATION PASSED — {len(CONCEPTS)} concepts, {len(REFERENCES)} renvois, "
          f"{len(RETIRED)} vocabulaire(s) retiré(s), {len(FIDELITY)} résumé(s) fidèle(s), "
          f"{len(GLOSSARY_TERMS)} termes de glossaire, lignes de table uniques, registre des façades, "
          f"noyau compilé, chargement unique")
    return 0


if __name__ == "__main__":
    sys.exit(main())
