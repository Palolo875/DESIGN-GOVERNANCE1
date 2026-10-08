# Trace — École de natation pour enfants (run N5-B3-plafond)

Trace complète (run audité, B1b et revue créative demandés). Artefact : `index.html`. Projection : `run_card.json`.
Owner de décision : la personne qui commande le site (propriétaire de l'école) ; owner du run : l'agent (Claude), jusqu'au checkpoint.

## 0. Ligne de run (avant build)

RUN — N5-B3-plafond — DIRECTION — faire comprendre à un parent, en une scène, où son enfant commencerait et dans quelles conditions (profondeur, groupe, créneau), puis réserver un essai — risque : site d'école interchangeable (photo d'enfant souriant + 3 cartes de cours) qui ne répond ni à la peur ni au placement — preuve : captures 390/768/1440 + check_render + états cliqués (palier choisi, formulaire erreur, succès) — état : CLASSIFIED.
DECISION-INTENT — trancher si un objet codé « coupe du bassin par paliers » + question d'aisance porte mieux le premier geste (choisir le bon groupe) qu'un hero photo générique.
Condition d'arrêt : défaut dominant corrigé ou réservé, B1b fait, gates A/C passés sur capture, pas de gain attendu d'une passe supplémentaire.

Classification (DIRECTION/START) : question 2 positive (premier contact + identité d'une école sans direction existante) → DIRECTION. Pas de risque critique au sens de la protection de niveau (pas de santé/paiement) ; données de mineurs dans le formulaire → minimisation déclarée (prénom + âge seulement). Brief vague → EXTERNAL-START.

## 1. Routes ouvertes (lues en entier) et effet

Ligne « Charger d'abord » DIRECTION :
- DIRECTION/START, DIRECTION/CHARGE, DIRECTION/EXTERNAL-START : mode, priorité TRUTH, contenu d'exemple marqué, action principale fonctionnelle avec valeur d'exemple (tel:, formulaire local).
- DIRECTION/CREATIVE-BOOT, DIRECTION/VISUAL_TARGET, DIRECTION/FIRST-OBJECT, ACTION/FIRST-RENDER, ACTION/UI-UX-REALITY, ACTION/RUN-DIRECTION, ACTION/PIPELINE-DIRECTION, ACTION/VISUAL_PROOF, ACTION/GATE-A, ACTION/GATE-C.
- Trace complète : ACTION/GATE-B, ACTION/HANDOFF, ACTION/RUN_CARD, ACTION/CLOSE-PACKAGE.

Routes conditionnelles — décision explicite :
| Route | Peut changer une décision ? | Ouverte | Effet |
|---|---|---|---|
| DIRECTION/DOMAIN-FRAME | Oui : brief nouveau et vague ; public (parents) ≠ usager (enfant), confiance/sécurité | Oui | Le parent devient le lecteur ; le placement par niveau et la peur de l'eau deviennent la tâche ; minimisation des données d'enfant. |
| DIRECTION/DIRECTION-ATELIER | Oui : tension peur/aisance et geste « trouver son palier » modifient la 1re scène | Oui | Moment humain, tension, geste, exclusion et contre-choix (§3). |
| DIRECTION/DOUBLE-LOOP | Oui : boucle + B1b + test de résilience | Oui | Ordre observer → défaut dominant → geste ; test de résilience « asset retiré / mobile ». |
| SAVOIR/FRAME (FND-01..03) | Oui : cadrage ambigu (qui décide, qui nage) | Oui | JTBD formulé ; hypothèses de contenu marquées. |
| SAVOIR/CRAFT/CFT-00 | Oui : revue créative demandée | Oui | Grille de revue (§6). |
| SAVOIR/CRAFT/CFT-02 | Oui : alternative située | Oui | Alternative photo-led formulée sur l'axe texte/image. |
| SAVOIR/CRAFT/CFT-03 | Oui : composition à deux masses en hero | Oui | Contrôles d'alignement, recomposition mobile. |
| SAVOIR/CRAFT/CFT-04 (+04a) | Oui : objet de preuve tôt vs promesse d'abord | Oui | Objet tôt retenu : mécanisme abstrait sans exemple, usage mobile ; l'objet ne montre aucun enfant réel. |
| SAVOIR/CRAFT/CFT-05 | Oui : palette identitaire | Oui | Palette par rôles (carrelage, ligne de fond, eau codée par profondeur, flotteurs, frite jaune = sélection). |
| SAVOIR/TYPE | Oui : chiffres de profondeur, voix du titre | Oui | Comparaison de 4 voix sur le vrai titre (`etudes/specimen-titre.png`). |
| SAVOIR/SOURCE | Oui : asset directeur (photos d'enfants) | Oui | Route CODE-NATIVE ; contre-épreuve photo formulée ; aucune image de stock d'enfants. |
| SAVOIR/STYLE | Oui : registre « enfant » cartoon vs utilitaire | Oui | PICTORIAL_UTILITY retenu (dials §3). |
| SAVOIR/TOOLS/CONVERGENCE | Oui : nommer MODAL | Oui | Marqueurs vague 1/2 + signal « grotesque condensée sur blanc à un accent » vérifiés contre le choix typo/palette. |
| SAVOIR/TOOLS/MOYENS | Oui : polices externes à choisir | Oui | Google Fonts (OFL), accès vérifié (HTTP 200) ; check_render avec --allow-external déclaré. |
| SAVOIR/STATE | Oui : formulaire, créneau complet, âge hors tranche | Oui | États empty/complet/hors âge/erreur/succès ; récupération après erreur. |
| SAVOIR/CONTEXT | Oui : enfants, formulaire | Oui | Pas de contexte critique listé ; motion réduite ; responsive recomposé. |
| SAVOIR/INTEGRITY | Oui : avant verdict | Oui | Questions de blocage (§9). |
| BIBLIOTHEQUE/SELECT, TENSION, SIGNATURE, OBJECT, CONTRACTS | Oui : structure ouverte | Oui | Sélection §4. |
| Connexions C01, C02, C03, C04, C07 | Oui (contexte incertain, typo, asset, récupération, ambition) | Oui | Ont renvoyé aux mêmes propriétaires ; C03 a confirmé « pas d'image de remplissage », C04 la reprise après erreur. |
| SAVOIR/ROUTING | Orientation | Oui | Localiser TYPE/SOURCE/STYLE. |
| Connexions C05, C06, C08, C09 | C05 : aucun antécédent lisible dans le périmètre autorisé ; C06/C09 : pas de changement partagé ni de déclinaison ; C08 : couvert par CONTRACTS | Non | N/A-JUSTIFIED. |
| ACTION/ROUTING | Le chargement est déjà déterminé par CHARGE | Non | N/A-JUSTIFIED. |
| SAVOIR/DESIGN-ATLAS | Silencieux : aucune famille d'asset à choisir (pas d'asset photo) | Non | N/A-JUSTIFIED. |
| ACTION/ANTI-SLOP | Lu via recherche (renvoi FND-01) | Oui | Sortie par élément observé (§6). |

Recherche `--trouver` : « enfant », « mineur » sans occurrence (limite déclarée, pas d'absence de savoir) ; « fort enjeu » → SAVOIR/CONTEXT.

## 2. Cadrage (DOMAIN-FRAME, FND-03)

- domain : école de natation pour enfants 4–12 ans, France, cours hebdomadaires en saison.
- audience : parents qui décident et paient, souvent sur téléphone, le soir ; l'enfant n'est pas le lecteur.
- expertise : faible en pédagogie aquatique ; vocabulaire connu : « petit bain / grand bain », « avoir pied ».
- jtbd : « Quand mon enfant doit apprendre à nager (ou a peur de l'eau), je veux savoir dans quel groupe il irait, à quelle profondeur, avec combien d'enfants et quand, afin de réserver un essai sans me tromper de niveau. »
- trust_model : rassure = encadrement chiffré, profondeur où l'enfant a pied, déroulé prévisible, prix clair ; détruit = photos d'enfants de stock présentées comme élèves, promesses (« nage en 10 séances »), faux avis.
- critical_actions : choisir le palier ; réserver un essai ; appeler. Données d'enfant minimisées (prénom + âge).
- domain_conventions : paliers/tests (Sauv'nage, test d'aisance aquatique), saison sept.–juin. Contestée : mascotte/cartoon, vagues SVG, turquoise dégradé.
- originality_tolerance : medium.
- proof_requirements : niveau → groupe → profondeur → encadrement → créneau → prix.
- domain_risks : mauvais placement, sur-promesse de sécurité, droit à l'image des mineurs.
- critical_states : créneau complet (liste d'attente), âge hors tranche, aucun créneau pour l'âge, erreur/succès de formulaire.
- evidence_plan : check_render 390/768/1440, --click sur états, captures avant/après B1b.
- Hypothèses : CONTENU (nom, adresse, prix, créneaux, ratios, température) — inférées, coût d'erreur moyen, owner : école, preuve : remplacement par vraies données ; user input requis : YES. DIRECTION (le parent veut d'abord savoir où commencer) — inférée, owner : école, preuve : 3 parents testent la question d'aisance.
- GROUNDING-DECISION : NEEDED — NO. COUNTER-HYPOTHESIS : les vrais ratios d'encadrement et profondeurs du bassin diffèrent. EFFECT-IF-TRUE : valeurs de la coupe et des fiches changent, pas la structure. REJECTION-BASIS : la coupe est générée depuis les données (changer 5 nombres suffit). RESIDUAL-UNKNOWN : normes locales, existence d'un bassin à fond mobile. REFUSAL-BASIS : SELF-ASSESSED.
- REUSE-CHALLENGE : antécédent non lisible (les autres runs sont hors du périmètre autorisé) → LIMIT : non-répétition non vérifiée.

## 3. Creative Boot / VISUAL_TARGET / ATELIER

- DECISION : la première scène peut-elle montrer « où commence votre enfant » plutôt que « l'école est sympathique » ?
- PROMISE : votre enfant commence là où il en est, là où il a pied, en petit groupe.
- PROOF-OBJECT : coupe du bassin à l'échelle (profondeurs exactes, graduation 10 cm), 5 paliers posés à leur profondeur, repère de taille d'enfant par âge ; fiche du palier (profondeur, groupe, durée, 3 gestes, créneaux). TRUTH/ILLUSTRATIVE + TRUTH/MECHANISM.
- GESTURE : choisir la phrase qui ressemble à son enfant (+ âge) → palier surligné → créneau → « Réserver une séance d'essai ».
- MODAL : hero photo d'enfant souriant avec lunettes, vague SVG, turquoise dégradé, police arrondie (Baloo/Fredoka), mascotte poisson/canard, 3 cartes (bébés nageurs / enfants / ados), « pourquoi nous », témoignages, tarifs, FAQ. Trame : promesse → 3 cours → avantages → avis → tarifs → contact.
- PARTI : s'écarter de l'image d'ambiance et du cartoon (parle à l'enfant alors que le parent décide ; photo de stock = faux asset) ; garder le registre « piscine » mais par sa signalétique (graduations de profondeur, carrelage, ligne d'eau), pas par des vagues. Trame rompue : l'objet de placement ouvre la page ; pas d'avis, pas de cartes de cours.
- STRUCTURAL-TENSION : PROOF-POSITION → intégrée (la preuve est le hero) ; TEMPORALITY → séquencée dans la 2e scène (déroulé d'une séance).
- STRUCTURAL-SIGNATURE : la profondeur devient l'axe de lecture : lire de gauche à droite = progresser ; PREVIOUS-LIMIT : la trame à cartes égalise les cours ; OBSERVABLE-CONSEQUENCE : au premier regard, petit bain/grand bain et « il a pied » se lisent sans texte ; EXIT-CONDITION : si à 390 px la coupe ne se lit plus (paliers illisibles), recomposer.
- CFT-TARGETS : spécificité, résolution (états), désirabilité située (calme rassurant sans mièvrerie).
- Moment humain : parent, le soir, après que l'enfant a refusé de mettre la tête sous l'eau à la piscine municipale. Tension : appréhension ↔ autonomie. Exclusion : l'enfant-mascotte et la photo d'ambiance. Contre-choix situé : direction photo-led (moniteur + enfant dans le petit bain, photographiés par l'école avec autorisation parentale) — meilleure si de vraies photos consenties existent et si l'école se distingue d'abord par ses personnes ; matérialisation : phrase (pas d'asset disponible), condition de retrait : photos réelles fournies → la photo vient en 2e scène à côté de la coupe, pas à sa place.
- FABRICATION (plafond par couche) : structure — complète ; typographie — Google Fonts accessibles (Barlow Condensed / Barlow, OFL) ; couleur — complète ; assets — aucune photo, aucun logo réel → CODE-NATIVE (coupe SVG, pictogrammes de signalétique assumés comme repères) ; contenu — exemples marqués (nom « Ligne d'eau », adresse, tel, prix, créneaux, places, ratios, température). Ancre : aucune observée/fournie ; références de signalétique de piscine = MODEL-KNOWLEDGE-NOT-RECHECKED, pas une ancre → issue EXPLORATORY.
- Typographie : comparaison sur le vrai titre (`etudes/specimen-titre.png`) : A Barlow Condensed (signalétique, chiffres de profondeur), B Fraunces (serif de caractère, vague 2), C Baloo 2 (arrondie « enfant », modal), D Rubik (grotesque douce, générique). Retenu A + Barlow texte : la même voix porte titre et données (« 0,80 m »), comme les marquages de bord de bassin. Convergence : signal « grotesque condensée sur blanc + un accent » — écart tenu par fond carrelage et palette codée multicolore, non par la police.
- Palette par rôles : surfaces carrelage #f1f6f5 / joints #cddcdb ; texte ligne de fond #0d2a3a ; eau en dégradé de profondeur (donnée : plus foncé = plus profond) ; flotteurs rouge/blanc (ligne d'eau, frise du temps) ; jaune frite #f5c22e = sélection « son palier » (doublé par bordure, aria-pressed et étiquette texte) ; action #0d2a3a ; erreur #a8231a + icône « ! » + texte.
- Style : STYLE/PICTORIAL_UTILITY — PROFILE-DECISION : l'image est une explication (coupe), pas une ambiance. DIALS : formalité bas, intensité émotionnelle basse (calme), matérialité basse (carrelage seulement dans la coque et le fond), originalité moyenne. COUNTERINDICATION : si le parent ne comprend pas la coupe (lecture technique), elle devient un schéma froid → preuve : test parent.
- Résolution initiale : vrais textes, 5 paliers, 14 créneaux, états complet/hors âge/aucun créneau, formulaire avec erreurs et succès, mobile recomposé.
- Alternative CFT-02 : axe texte/image (preuve souveraine ↔ photo) ; décision changée : asset directeur ; public : école qui a des photos ; matérialisation : phrase ; preuve : comparaison avec photos réelles ; retrait : sans photos consenties.

## 4. Structure (BIBLIOTHEQUE/SELECT, TENSION, SIGNATURE, OBJECT, CONTRACTS)

- Trame modale (une ligne) : hero photo + 2 CTA → 3 cartes de cours → pourquoi nous → avis → tarifs → FAQ → contact. Rompue : l'ordre est tâche → preuve → déroulé → prix → pratique ; l'objet qui organise la page est la coupe, pas une liste de cours.
- SUPPORT : champ carrelage (`#f1f6f5` + joints) hérité de la piscine, pas de nouvelle route. GRID : deux masses 5/7 en hero (titre+question | coupe+fiche), recomposées en une colonne < 1020 px. SCENE : preuve intégrée (PROOF-POSITION = intégrée). OBJECT : dérivé local d'`OBJECT/CONTROL_VALUE_TILE` (valeur + contexte + action) pour la fiche du palier ; la coupe est une forme locale (pas de route durable). MICRO : créneaux (état places / complet). MODIFIER : aucun.
- TENSION-AXES : PROOF-POSITION=intégrée (impact : la coupe est en hero, pas en section 3) ; TEMPORALITY=séquencée pour la 2e scène (frise de 9 flotteurs). OWNER : agent ; NEXT-OBSERVATION : capture ; EXIT-CONDITION : coupe illisible à 390 px → recomposer.
- Calibration (CONTRACTS) : 1 m = 125 unités, graduation 10 cm ; libellés HTML 15 px (13 px mobile) ; sélection = jaune + bordure + aria-pressed + étiquette ; états de l'objet : vide, palier, âge hors tranche, aucun créneau, complet.

## 5. Premier rendu (v1) — observation

Captures : `captures/v1/` (390/768/1440). check_render v1 : RETURN « nom accessible » (contrôles du dialogue fermé, puis liens de nav masqués en mobile) ; le reste PASS ou réserve.
- Lecture ordinateur : 1) titre condensé, 2) carte-question (bloc blanc haut), 3) la coupe — petite et plate (rapport 3:1), chiffres de profondeur ≈ 11 px. Mobile : coupe ≈ 340×110 px, libellés de profondeur ≈ 6 px, illisibles ; « GRAND BAIN » chevauche « 2,00 m ».
- Lecture légère (texte ignoré) : catégorie « équipement aquatique / piscine », marque « signalétique municipale calme », niveau de preuve « schéma chiffré illustratif ». Conforme à la thèse ; pas d'écart narratif.
- Contrôle du premier objet : présence OK ; foyer partagé titre/question/coupe ; signature OK ; intégration OK ; **résolution en échec** (objet illisible sur mobile) ; désirabilité située OK ; vérité de scène OK (bandeau + mentions locales) ; résilience visible en échec (mobile).
- Défaut dominant : la coupe (objet de preuve) n'est pas lisible à petite taille → diagnostic « défaut de résolution, direction intacte ».

## 6. Boucle d'édition et revue créative

Revue créative 1 (après v1, CFT-00) :
- Présent : deux masses, titre à forte présence, coupe codée.
- Spécifique : la profondeur et le repère de taille d'enfant ; les créneaux par âge ; « shorts de bain refusés », bonnet obligatoire.
- Culturellement transformé : signalétique de bord de bassin (marquages de profondeur, carrelage, ligne d'eau) devenue graduation, champ et frise de temps.
- Encore générique : la carte-question (liste de radios) ; l'état vide en pointillés.
- Manque de résolution : libellés SVG qui rétrécissent avec la coupe ; collision « GRAND BAIN » / « 2,00 m ».
- Intervention au meilleur gain : **Texte secondaire / Image intégrée** (SAVOIR/STATE) → sortir les libellés du SVG en calques HTML à taille fixe et resserrer la coupe (1000×330 → 800×352) ; condition : lisible à 390 px sans débordement.

v1 → v2 (CHANGED) : captures `captures/v2/`, `captures/v2-palier2/`. Effet observé : chiffres de profondeur à 15 px (desktop) / 13 px (mobile), lisibles ; coupe plus haute ; la tête de l'enfant au-dessus de la ligne d'eau se lit à 390 px. Régression vérifiée : aucune (débordement PASS). Corrections locales ensuite : label « GRAND BAIN · 2 m partout » débordant à 390 px → raccourci et ancré à droite ; « 5–7 ans » coupé sur 2 lignes par « Complet · liste d'attente » → âge en `nowrap`, statut sur deux lignes.

### B1b — atelier d'édition sur capture (auto-comparaison)
- Décision principale mise à l'épreuve : les repères de taille d'enfant portent la relation « il a pied » (la promesse).
- Édition : **retrait** des pictogrammes et de leur légende (variante `etudes/index-b1b-sans-reperes.html`), rien ajouté.
- Paire : `captures/b1b-avant/capture-1440px.png` → `captures/b1b-apres/capture-1440px.png` (et 390 px) ; comparaison rognée `etudes/b1b-paire.png`, état palier 2 choisi.
- Effet observé : sans repères, la coupe devient un profil de profondeur technique ; « il a pied » n'existe plus que dans le texte ; petit et grand bain ne diffèrent que par un chiffre ; la ligne de flotteurs devient l'élément le plus fort de la surface.
- Résultat : **confirmed** — l'original est conservé. Effet secondaire appris : les flotteurs concurrencent les têtes (→ geste de masse ci-dessous).
- Limite : auto-comparaison par l'auteur du rendu, pas un regard indépendant (B3 absent, déclaré).

Repasse de craft (v3/v4), un geste par défaut :
- **Masse visuelle** : flotteurs réduits (rx 9,5→7, ry 6→4,2, trait 1→0,8) ; réinspecté : les têtes d'enfant redeviennent le premier signal à la surface ; la ligne d'eau reste reconnaissable. Conservé.
- **États / résolution située (C6)** : l'état initial en pointillés ne servait à rien au parent qui hésite → ajout « Vous hésitez entre deux phrases ? Prenez la plus prudente… » + « Réserver un essai sans choisir » ; réinspecté : la colonne droite équilibre la gauche à 1440 px (silhouette) ; l'action existe avant le choix. Conservé.
- **Texte secondaire** : libellés de profondeur non sélectionnés passaient par opacité 45 % (≈ 2,9:1) → couleur `#5b707b` sur blanc (5,19:1). Conservé.
- États vides « aucun créneau » / « hors âge » : ajout du lien d'appel (l'action principale reste fonctionnelle avec valeur d'exemple).
- Nav mobile masquée → rangée de 4 ancres sous la marque (les parents vont aux tarifs) ; supprime aussi le faux RETURN de la recette sur liens masqués.
- Dialogue : contenu dans un `<template>` injecté à l'ouverture, vue de succès créée au succès (pas de contrôles masqués dans le DOM) ; titre du résumé d'erreur exact (« Il manque 2 informations »).

Revue créative 2 (après repasse, sur `captures/final/`) :
- Présent : titre + coupe en deux masses équilibrées ; la coupe se lit avant le texte.
- Spécifique : profondeur à l'échelle, repères de taille, créneaux par âge et état complet, séance minute par minute, détails du sac.
- Culturellement transformé : signalétique de piscine → graduation exacte, ligne d'eau → frise (1 flotteur = 5 min), frite jaune → sélection.
- Encore générique : sections tarifs et infos pratiques (cartes) — convention de genre gardée volontairement (comparaison rapide), contenu propre.
- Manque de résolution : coupe petite en mobile, sous la question ; repères estompés peu contrastés (non textuels, non mesurés).
- Prochaine intervention : vue mobile recadrée sur le palier choisi, à comparer avec la coupe entière (test parents) ; sinon STOP.

## 7. Gates

Gate A (profil « page vitrine » + formulaire → contrôles d'office + états, motion réduite, focus non masqué). MEDIUM : web, Chromium sans tête. SCOPE : page, états initial/palier/hors âge/aucun créneau/dialogue erreur/succès. CONFORMANCE-TARGET : WCAG 2.2 AA. METHOD : AUTOMATED (check_render, `--allow-external` : polices Google chargées) + MANUAL scripté (`etudes/parcours.py`). COVERAGE-LIMIT : pas de lecteur d'écran, contraste non textuel non mesuré.
- Débordement, erreurs JS, cibles, structure, h1 unique, mouvement réduit : PASS (`captures/final-check.json`, version c272153ea68a).
- Contraste : PASS-WITH-RESERVATION (aucun texte évalué sous AA ; réserves : texte natif de `select`, `::after` des FAQ, `span.ex` en opacité). Calcul complémentaire : texte #0d2a3a/#f1f6f5 13,65:1 ; secondaire #3d5664/#f1f6f5 7,09:1 ; bouton #fff/#0d2a3a 14,9:1 ; erreur #a8231a/#fdeceb 6,29:1 ; « complet » #7a3b12/#f1f6f5 7,82:1 ; « places » #1d6b45/#f1f6f5 5,94:1 ; sélection #0d2a3a/#f5c22e 8,97:1 ; profondeur non choisie #5b707b/#fff 5,19:1 ; zones #0d2a3a/#e4eeed 12,6:1. `span.ex` (opacité 0,8 sur bouton) : NOT-VERIFIED.
- Nom accessible : PASS-WITH-RESERVATION (24 à 36 contrôles, candidats DOM ; AccName non calculé). Le RETURN v1–v3 venait de contrôles masqués (dialogue fermé, nav mobile `display:none`) ; résolu en ne gardant aucun contrôle masqué dans le DOM.
- Clavier : PASS-WITH-RESERVATION (radios non atteintes une à une = groupe radio, flèches vérifiées) ; dialogue modal : PASS (9 arrêts, piège de focus natif, Échap et Fermer rendent le focus à « Réserver »).
- États : erreur près du champ + résumé focalisé + liens vers champs + saisie conservée + succès explicite et honnête (« maquette : rien n'a été envoyé ») — OBSERVED (`captures/v4-etats/parcours.log`, captures erreur/succès).
- Information non chromatique : sélection = bordure + étiquette « Son palier » + aria-pressed ; complet = texte ; erreur = « ! » + texte.
- Contenu honnête : bandeau global + mentions locales (téléphone, adresse, prix, places, encadrement, température) + succès de formulaire qui dit qu'il n'envoie rien.

Gate B : B1 — pas d'ancre à comparer (absence déclarée). B1b fait (§6). B2 : V (caractère) capturé ; U non testé (pas de parent) ; A/T recette. B3 : aucun regard externe ; absence déclarée. B5 : aucun asset directeur externe (CODE-NATIVE) ; polices Google Fonts OFL. B6 : réponse compacte.

Gate C (sur `captures/final/`, 1440 et 390, état initial et palier 2) :
- C1 surface : carrelage + eau codée par profondeur, issus du produit — présent.
- C2 typographie : Barlow Condensed (titre, chiffres) / Barlow (texte), comparée à Fraunces, Baloo 2, Rubik sur le vrai titre — présent.
- C3 composition : deux masses, ordre titre → question/coupe → fiche — présent.
- C4 densité : groupes par proximité ; fiche dense mais séparée par filets — présent.
- C5 profondeur : planéité assumée (pas d'ombres portées, filets 1 px) — présent / cohérent.
- C6 résolution située : « Vous hésitez entre deux phrases ? », aucun créneau pour l'âge → appel, complet → liste d'attente — présent.
Tests BIBLIOTHEQUE/GATE (non-généricité, silhouette) : à faible détail, la coupe reste reconnaissable ; non générique si le nom disparaît (le bassin gradué reste).

Axes : V PASS-WITH-RESERVATION (auto-comparaison, sans ancre) ; U NOT-VERIFIED (pas de tâche parent) ; A PASS-WITH-RESERVATION (recette + parcours scripté, sans lecteur d'écran) ; T PASS (débordement, JS, mouvement réduit aux 3 largeurs).

## 8. Matière, assets, vérité

- Route : CODE-NATIVE (coupe SVG + calques HTML, pictogrammes de signalétique assumés comme repères abstraits, jamais présentés comme photo). Contre-épreuve : photo d'enfant dans le petit bain — refusée sans photo réelle consentie (droit à l'image de mineurs, faux asset). Polices : Google Fonts, OFL, chargées et vues sur capture.
- TRUTH : coupe et fiche = ILLUSTRATIVE + MECHANISM ; profondeurs, ratios, créneaux, places, prix, température, nom, adresse, tel = ILLUSTRATIVE (marqués dans l'interface en langage produit) ; « test d'aisance aquatique », « Pass'Sport » = MODEL-KNOWLEDGE-NOT-RECHECKED, à confirmer par l'école ; tailles moyennes d'enfant (1,07/1,15/1,22 m) = repère indicatif, connaissance non revérifiée.
- Données cohérentes : 30 séances × 7 € = 210 € ; × 9,50 € = 285 € ; × 11 € = 330 € ; paliers et tranches d'âge des créneaux inclus dans la tranche du palier ; frise 5+5+20+10+5 = 45 min.

## 9. Intégrité (avant verdict)

- Ancre/spec : aucune ancre observée/fournie ; spec = §3 (observée contre le rendu). → pas d'acceptation.
- Décision perceptible : la profondeur comme axe de lecture, visible sur capture.
- Alternative : photo-led (§3), non matérialisée faute d'asset.
- Écart spec/rendu restant : sur mobile la coupe passe sous la question (accepté : le geste précède la preuve) et reste petite.
- Preuve manquante : tâche parent, lecteur d'écran, contraste non textuel.
- Hypothèse incertaine : que les parents se reconnaissent dans les 5 phrases (owner : école ; preuve : 3 parents).
- Décision changée par la procédure : lisibilité de l'objet (v1→v2), repères confirmés (B1b), état initial actionnable.
- Règle satisfaite dans la lettre seulement : risque sur « culture visuelle » (aucune référence observée) — déclaré.

## 10. Handoff / clôture

MODE DIRECTION — DECISION objet de placement en hero — RISK site interchangeable / objet illisible — SCOPE page entière, 390/768/1440, états listés — ARTIFACT index.html (c272153ea68a)
OBSERVATION/METHOD check_render AUTOMATED + captures + parcours scripté — PROOF captures/, etudes/, run_card.json — LIMIT pas d'ancre, U et lecteur d'écran NOT-VERIFIED, contenus d'exemple
DECISION-CHANGE CHANGED (lisibilité de la coupe ; repères confirmés) — NEXT-ACTION vue mobile recadrée sur le palier — OWNER propriétaire de l'école — NEXT-PROOF contenu réel + 3 parents sur téléphone + lecteur d'écran — EXIT-CONDITION 3 parents placent leur enfant sans aide et réservent.
State CLOSED (artefact et trace persistés) ; issue EXPLORATORY ; verdict EXPLORATORY ; direction_status HELD dans le rendu, avec la réserve : direction calibrée uniquement de mémoire, sans référence observée ni contrainte réelle.
