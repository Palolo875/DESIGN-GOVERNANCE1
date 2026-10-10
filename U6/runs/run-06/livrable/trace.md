# Run-06 — trace de proposition

RUN — run-06 — DIRECTION — premier contact d'un atelier vélo avec prise de rendez-vous — risque dominant : confusion entre démonstration et réservation réelle — preuve suivante : captures et parcours locaux — EXPLORATORY.
DECISION-INTENT — Montrer qu'un accueil direct, centré sur le besoin du vélo et un rendez-vous visible, rend la prise de contact plus claire qu'un hero de réputation.
SCOPE — Une landing page autonome ; desktop 1440×1000, mobile 390×844, robustesse à 320 px ; formulaire local, erreurs et clavier.
OWNER — Producteur de cette proposition ; la personne de l'atelier conserve la décision sur la marque, l'offre et la future mise en service.
LIMIT — Pas de marque, contenus ni photographie fournis ; tous les contenus commerciaux sont des exemples ; aucune disponibilité réelle et aucun envoi. Polices locales et HTML/CSS/JS seulement.
EXIT-CONDITION — Première proposition complète, captures inspectées, une édition comparée, parcours réels consignés ; pas d'acceptation de marque ni publication.

## Cible et fabrication avant build

- Situation : cycliste francophone, souvent peu expert, cherchant à faire réparer son vélo et à prévoir un dépôt. Le créneau représente un accueil/diagnostic, pas une durée garantie de réparation. Convention conservée : labels explicites, radios natives, coordonnées simples. Risque propre au métier : confondre rendez-vous de dépôt et vélo prêt ; microcopie et récapitulatif le distinguent.
- Thèse : un atelier accessible et concret ; promesse → prise en charge lisible → fiche de besoin avec créneau de dépôt → choisir puis vérifier une demande locale.
- Modal hypothétique, sans claim de fréquence : photo de mécanicien, slogan, trois bénéfices, avis, tarifs, contact. Parti : faire du besoin du vélo et du rendez-vous l'objet de la première scène, puis montrer les interventions et le déroulement. Aucun faux avis, photo ou chiffre de réputation.
- Alternative située : portrait photographique de l'équipe avec CTA vers un formulaire séparé ; meilleur potentiel d'ancrage humain si une photographie réelle est fournie, mais ici aucune image authentique et l'action serait éloignée. Matérialisation textuelle suffisante pour ce choix ; retrait du parti actuel si l'atelier fait principalement du sans-rendez-vous.
- Tensions : ACTION centrale ↔ contextuelle (centrale retenue) ; DENSITY respiration ↔ compression (titre respirant / formulaire précis). Silhouette : masse typographique à gauche, fiche claire à droite, liste d'interventions horizontale ensuite. Le formulaire est le seul objet opérationnel dominant.
- Support : page Web plane autonome, sans héritage. Grille : GRID/HIERARCHICAL ; 1280 px maximum, marges 64 px desktop / 22 px mobile, rapport gauche-droite ~55/45. Scène : accueil + fiche de dépôt conventionnelle ; aucune nouvelle route durable. Objet : formulaire natif en trois étapes, avec retour préservant les données. Sur mobile : introduction plus courte, formulaire immédiatement ensuite, interventions en lignes compactes.
- Palette par rôles : fond crème #f3eee4, surface blanche #fffdf8, texte #28251f, accent/action #b83322, secondaire #635e54, état erreur #a32319. Planéité assumée, frontières contrastées et aucun effet de matière simulée. Accent rouge choisi pour la signalétique d'action visible ; il ne prétend pas appartenir à une marque existante.
- Typographie à comparer sur « Un vélo qui roule. Et vous avec. » : Manrope (directe, pratique, forte silhouette) contre Instrument Serif (voix plus littéraire). Corps et contrôles Manrope 15–17 px ; titre 82 px desktop / 48 px mobile, lignes réglées sur le texte. Polices françaises locales disponibles et licences OFL lues en entier ; aucune ressource distante.
- Ancre : absente, NOT-VERIFIED ; une cible textuelle ne remplace pas une référence observée. Proposition EXPLORATORY, aucune acceptation. Enjeu identitaire normal pour cette proposition, aucune marque réelle adoptée.
- Fabrication : structure/type/couleur/états réalisables entièrement ; contenu commercial plafonné aux exemples ; authenticité humaine/photographique et disponibilité réelle indisponibles. Route SANS-ASSET, la tâche et le contenu portent la promesse ; les petits pictogrammes SVG seront explicitement des signes illustratifs, jamais des photographies ou des preuves.
- Résolution attendue : page entière écrite, services/prix/horaires/adresse fictifs signalés, choix du besoin, créneaux d'exemple dont un indisponible, coordonnées, validation, erreurs, retour, récapitulatif et réinitialisation. Ni envoi ni stockage persistant ni paiement.
- Relation fragile anticipée : masse du titre contre masse du formulaire. Geste préparé : réduire la taille du titre sans ajouter d'objet, comparer les premières captures, préserver la tâche.
- Arrêt de lecture : prochaine décision, moyens, propriétaire, limites et preuves sont connus ; aucune lecture de référence externe ni d'ancien run.

## Périmètre de vérification déclaré

Web Chromium / Playwright ; 1440×1000, 390×844, absence de débordement à 320×844. WCAG 2.2 AA comme cible de conception ; vérifications partielles par DOM/CSS et parcours clavier, sans certification. Captures pleine page et viewport, erreurs et état final. Budget : HTML autonome local, sans dépendance réseau ni motion décorative. Hors couverture : Safari/Firefox, technologies d'assistance et participants réels. Prochaine preuve après proposition : contenus de l'atelier et tests utilisateurs.

## Modules conditionnels

DOUBLE-LOOP : appliqué via noyau, une édition comparée. ROUTING : écarté, responsabilités stables. CFT-00 : revue du noyau appliquée aux captures. DIRECTION-ATELIER : écarté, tension/objet/contre-choix déjà concrets. FRAME : écarté, hypothèse de dépôt explicitée. CRAFT : gestes du noyau suffisants pour la relation masse/états, aucun objet métier inédit. SOURCE : écarté, aucun asset authentique ; droits des polices vérifiés localement. SELECT : ouvert pour choisir la hiérarchie. SEQUENCE : ouvert pour mettre le rendez-vous avant les arguments. DOMAIN-FRAME : ouvert pour distinguer dépôt et réparation. STYLE : écarté, aucun registre culturel à transférer. CFT-03 : noyau, réduction d'une masse. STATE : noyau, reprise en erreur et préservation des données. INTEGRITY : ouvert avant jugement, pour empêcher l'inférence de preuve.

## Observations et décisions

Voix typographiques comparées sur le vrai titre dans captures/typographie.png : Manrope garde des masses compactes et une lecture pratique ; Instrument Serif change le ton vers un accueil littéraire plus contemplatif. Manrope retenue pour relier le titre aux contrôles et au besoin immédiat. Comparaison du producteur, aucun effet de compréhension mesuré auprès d'utilisateurs.

Lecture initiale sans rationale : page d'un atelier de quartier au ton direct, marque typographique proposée, preuve de fonctionnement limitée au formulaire de démonstration. Présence : grande accroche face à une fiche de rendez-vous. Spécificité : choix du problème, prix hors pièces, dépôt distingué de réparation. Transformation culturelle : aucune référence externe observée, donc non revendiquée. Générique : le split titre/formulaire reste une composition conventionnelle ; conservé parce que le second bloc est l'action elle-même, pas un screenshot décoratif. Manque de résolution : flèches absentes dans la fonte pour certaines actions.

Édition 1, masse visuelle : h1 réduit de 82 à 72 px, approche de −4,5 à −3,9 px, sans ajout compensatoire. Comparaison captures/desktop-initial-viewport.png → captures/desktop-reduction-viewport.png. Le titre reste l'entrée de lecture mais son troisième vers libère une marge à droite et le formulaire gagne une priorité relative ; conservé. Mobile reste à 48 px, la relation y était déjà lisible. DECISION-CHANGE — CHANGED : priorité relative du formulaire accrue par réduction du titre ; paire réinspectée.

Édition 2, résolution locale : glyphes ↗ remplacés par SVG de signalétique, retrait des étapes au récapitulatif via .progress[hidden], focus de changement d'étape autorisé à défiler pour rester visible sur mobile. Captures finales et parcours rejoués après la modification. Effet : flèches visibles, récapitulatif sans compteur d'étapes inactif, entrée de nouvelle étape visible lors du parcours mobile. Aucune nouvelle scène, aucun effet ajouté ; usage et robustesse améliorés. Deux tours de correction, sous le maximum de trois.

Revue finale : silhouette plane et nette, espace du titre conservé sans écraser la fiche, séquence interventions → déroulement → accès cohérente. L'objet de craft le plus utile est l'erreur liée au champ, focus visible et données conservées lors du retour. Le défaut restant dominant est l'absence d'identité et de matière humaines authentiques : la page repose sur une proposition typographique et une offre d'exemple. La direction reste exploratoire. STOP — aucun gain utile attendu d'une troisième repasse avec ces moyens et contenus.

## Preuves exécutées et limites

- Navigateur Chromium réel, Python Playwright 1.56.0 ; premières lectures file:// bloquées par la politique du navigateur. Alternative autorisée : serveur 127.0.0.1 à port éphémère, arrêté après chaque session. Aucun changement de configuration nécessaire. Favicon de la page principale intégré en data URL ; 404 de favicon sur le seul spécimen typographique sans effet sur l'artefact.
- functional-tests.json : 11 parcours et inspections exécutés, 11 PASS au périmètre consigné. Sélecteurs, actions et observations réels, incluant clavier complet sur mobile, dates et radios indisponibles, jour vide, erreurs de coordonnées, correction, retour avec saisie conservée, résultat local, reset, aide des données, absence de requête HTTP externe et d'erreur JavaScript, labels et contenu long.
- Captures 1440×1000 et 390×844, vues pleine page et viewport nominales inspectées ; erreur desktop et mobile, focus et récapitulatif inspectés. Mesure scrollWidth à 320 px nominal et récapitulatif ; erreur et contenu de 400 caractères également à 320 px, sans débordement.
- contrast.json : dix paires opaques calculées. Texte secondaire 5,57:1 sur crème ; action 5,84:1 ; erreur 7,35:1 ; focus 5,84:1 ; bordure de saisie 4,13:1. SVG de navigation : couleur du texte héritée sur fond opaque, pictogrammes sans claim de média authentique. Les frontières décoratives claires ne portent pas seules l'information de sélection.
- Sémantique : un h1, sections nommées, fieldsets/legends, radios natifs, labels de tous les champs, noms de boutons d'intervention ; erreurs role=alert et aria-describedby, focus transféré puis navigation native.
- Cibles : radios inclus dans labels de 56 px minimum ; boutons principaux ≥54 px. Boutons de sélection d'intervention 34 px mobile et 32 px à 320, espacés ; cible minimale AA de 24 px respectée par la boîte. Pas de glisser, authentification, motion décorative, attente serveur, permission ni paiement : N/A-JUSTIFIED. Chargement serveur/succès partiel réels : N/A-JUSTIFIED, aucune intégration dans cette démo.
- Gate A : preuves positives locales de contraste, noms/labels, erreurs, clavier et responsive ; accessibilité complète NOT-VERIFIED. Radios natifs non mesurés pixel par pixel, aucun lecteur d'écran exécuté, aucun audit de conformité complet.
- Gate B : auto-comparaison déclarée ; aucune ancre observée ou fournie, aucun regard indépendant ou participant, contexte de l'atelier NOT-VERIFIED. Comparaison à la spec seulement, aucun verdict accepté.
- Gate C : stratégie plane, rôle typographique comparé, priorité du formulaire et résolution des erreurs observés sur les captures finales. Signature métier portée par la tâche, pas par une marque réelle. Réserve identitaire explicite.
- Axes de sortie : V NOT-VERIFIED pour une direction réelle ancrée ; U PASS-WITH-RESERVATION pour les parcours locaux seulement ; A PASS-WITH-RESERVATION pour les contrôles partiels décrits ; T PASS au runtime et viewports observés, aucune compatibilité multibrowser revendiquée.

## Handoff et clôture

STATE CLOSED — ISSUE EXPLORATORY — VERDICT EXPLORATORY — DIRECTION-STATUS PARTIALLY-HELD. La clôture concerne la proposition et sa trace, jamais l'adoption ou la mise en service d'une marque. Artefact de référence : index.html version finale ; scripts build.py et finalize.py documentent la fabrication et ne constituent pas un contrat de rebuild à l'identique des preuves finales.

OWNER — Producteur pour les tests et la proposition ; personne de l'atelier pour l'identité, les contenus et la mise en service. NEXT-ACTION — recueillir (1) nom/logo ou identité existante, (2) offre/prix/horaires/adresse et photo réelle autorisée si souhaitée, (3) fonctionnement de l'agenda et confirmation. NEXT-PROOF — confronter l'offre et le parcours à ces éléments puis tester auprès de cyclistes ; vérifier Safari/Firefox et lecteur d'écran avant diffusion. EXIT-CONDITION — contenus réels approuvés et intégration de réservation vérifiée de bout en bout dans un travail ultérieur. Publication, envoi et paiement non exécutés.

## Sources complètes réellement lues

Toutes les routes ci-dessous ont été lues jusqu'à « lecture terminée » via /workspace/remesure-phase5/lire.py run-06 ; le mode --mode n'est pas disponible dans ce lecteur, aucune modification du paquet. La skill entière compte 42 866 caractères, offsets 0, 6000, 12000, 18000, 24000, 30000, 36000 et 42000.

Base absolue des sources : /workspace/remesure-phase5/runs/run-06/paquet/.

| Routes utiles | Source complète propriétaire |
| --- | --- |
| Skill / noyau | /workspace/remesure-phase5/runs/run-06/paquet/agent/skill/SKILL.md |
| DIRECTION/START, DIRECTION/CREATIVE-BOOT, DIRECTION/DOMAIN-FRAME, ACTION/RUN-DIRECTION | /workspace/remesure-phase5/runs/run-06/paquet/agent/chemins.md, sections « classer avant d'agir », « activer la boucle avant le premier pixel », « adapter le design au domaine », « ACTION/RUN-DIRECTION » |
| DIRECTION/EXTERNAL-START | /workspace/remesure-phase5/runs/run-06/paquet/design/direction/cadrer.md, activation portable sur brief vague |
| DIRECTION/VISUAL_TARGET | /workspace/remesure-phase5/runs/run-06/paquet/design/direction/diriger.md, rendre la direction pilotable |
| DIRECTION/FIRST-OBJECT | /workspace/remesure-phase5/runs/run-06/paquet/design/direction/premier-objet.md, compiler le brief et produire le premier objet |
| SAVOIR/TYPE | /workspace/remesure-phase5/runs/run-06/paquet/design/savoir/typographie.md, typographie et données |
| ACTION/FIRST-RENDER, ACTION/UI-UX-REALITY | /workspace/remesure-phase5/runs/run-06/paquet/design/produit/premier-rendu.md, qualité initiale et construire interface/tâche |
| ACTION/PIPELINE-DIRECTION | /workspace/remesure-phase5/runs/run-06/paquet/V1/sections/ACTION.md, direction vérifiable |
| ACTION/VISUAL_PROOF | /workspace/remesure-phase5/runs/run-06/paquet/design/produit/preuve-visuelle.md, rendre la direction vérifiable |
| ACTION/GATE-A | /workspace/remesure-phase5/runs/run-06/paquet/design/produit/plancher.md, plancher objectivable |
| ACTION/GATE-B | /workspace/remesure-phase5/runs/run-06/paquet/gouvernance/verification.md, jugement contextualisé et risques |
| ACTION/GATE-C | /workspace/remesure-phase5/runs/run-06/paquet/design/produit/finition.md, craft sur rendu réel |
| ACTION/HANDOFF | /workspace/remesure-phase5/runs/run-06/paquet/agent/repondre.md, sortie minimale commune |
| ACTION/RUN_CARD | /workspace/remesure-phase5/runs/run-06/paquet/gouvernance/travail.md, carte de run minimale |
| ACTION/CLOSE-PACKAGE | /workspace/remesure-phase5/runs/run-06/paquet/gouvernance/cloture.md, paquet de clôture |
| BIBLIOTHEQUE/SELECT | /workspace/remesure-phase5/runs/run-06/paquet/design/formes/choisir.md, choisir avant de composer |
| BIBLIOTHEQUE/SEQUENCE, GRID/HIERARCHICAL | /workspace/remesure-phase5/runs/run-06/paquet/design/formes/catalogue.md, séquence et hiérarchie |
| BIBLIOTHEQUE/CONTRACTS | /workspace/remesure-phase5/runs/run-06/paquet/gouvernance/structure.md, contrat commun et calibration locale |
| BIBLIOTHEQUE/GATE | /workspace/remesure-phase5/runs/run-06/paquet/V1/sections/BIBLIOTHEQUE.md, contrôle structurel complémentaire |
| SAVOIR/INTEGRITY | /workspace/remesure-phase5/runs/run-06/paquet/V1/sections/SAVOIR.md, limites, délégation et critique |
| Projection observée / validateur utilisé | /workspace/remesure-phase5/runs/run-06/paquet/gouvernance/schemas/run_card.example.json ; /workspace/remesure-phase5/runs/run-06/paquet/gouvernance/outils/validate_run_card.py |

Polices : /workspace/remesure-phase5/moyens/manrope.ttf et instrument-serif.ttf. Licences entières : /workspace/remesure-phase5/moyens/OFL-manrope.txt et OFL-instrument-serif.txt, redistribuées à côté et licence Manrope embarquée dans index.html. Aucun fichier des autres runs ou résultat de comparaison lu. Skill de préparation d'environnement requise par le contexte : skill://plugin_connector_1p_ed5feb9070a08191b08c81c47947bc16/setup/SKILL.md, lue ; vérification du runtime existant seulement, sans installation ni modification de configuration.

Validation finale : run-card.json validée avec le validateur du paquet et --strict ; résultat « RUN_CARD VALIDATION PASSED ». Ce résultat atteste la projection et ses locators, pas une acceptation de direction ou une conformité globale. Les serveurs de vérification ont tous été arrêtés. L'HTML final porte le hash/version conservé dans run-card.json et ne dépend d'aucun autre fichier pour son rendu ou son interaction.

Marquage interne de vérité : nom, offre, prix, horaires et adresse TRUTH/ILLUSTRATIVE ; dates et créneaux du formulaire TRUTH/ILLUSTRATIVE + TRUTH/MECHANISM. Les résultats locaux des parcours sont OBSERVED dans functional-tests.json ; ils ne rendent pas une disponibilité réelle observée. Aucun de ces labels internes n’apparaît dans l’interface.
