# U1b — Fiche d'inventaire n°1 : `V1/official/SAVOIR.md`

**Base :** commit `d90869c`. **Lecture :** intégrale, lignes 1 à 1052, section par section (INTEGRITY, lignes 950 à 1052, lue plus tôt dans la journée par sa route complète). **Mesures :** tailles servies par `read_route.py`, recherches littérales. Chaque affirmation cite sa ligne. **Angle :** ce que le fichier *possède* et ce que cela permet de fabriquer. Pas de propositions d'ajout.

## 1. Identité

| Élément | Valeur |
|---|---|
| Taille | 118 858 o, 1 052 lignes |
| Routes | 12 : FRAME 11,6 Ko · CRAFT 21,6 · TYPE 3,2 · STATE 13,8 · SOURCE 6,7 · DESIGN-ATLAS 7,5 · STYLE 15,8 · SYSTEM 2,0 · CONTEXT 3,1 · TECH 6,8 · TOOLS 8,1 · INTEGRITY 8,6 |
| Part compilée dans le noyau | 18 blocs, 17,9 Ko : **15 % du fichier, 41 % du noyau** |
| Concepts protégés par le validateur | 7 (TXI-01, TIT-01, FIN-01, RCV-01, ANT-01, MOY-01, HON-02) |

## 2. Rôle

- **Déclaré** (l. 7-9) : « comment exercer le jugement » ; transformer une impression visuelle en décision située.
- **Réel :** c'est **le savoir de design du système**. Presque tout ce que l'agent sait de composition, de typographie, de couleur, d'états et de craft vient d'ici. Le reste du fichier est de l'outillage de jugement (grilles, gabarits, tests) et de la veille.

## 3. Ce qu'il possède, par couche de travail

**Niveaux de concrétude :**
- **A, actionnable** : un geste, une formule, une décision directe ;
- **O, orientant** : une question ou une grille de regard ;
- **N, seulement nommé** : une source ou une référence sans moyen d'usage.

**Accès :** **Noyau** (toujours lu) ou **Route** (seulement si chargée).

### Comprendre le besoin

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| FND-03 : cinq questions de cadrage (Qui, Pourquoi avec la formule JTBD « Quand…, je veux…, afin de… », Quelle décision, Quelle preuve, Quelles contraintes) | 168-178 | A | Route |
| Fiche d'hypothèse (nature et confiance, source et coût d'erreur, owner, besoin d'avis utilisateur) | 180-191 | A (gabarit) | Route |
| Architecture par tâche et vocabulaire utilisateur ; cas à prévoir : vide, erreur, permission, données longues, succès partiel, localisation | 195 | A | Route |
| Méthode comprendre / ouvrir / converger / prouver | 110-112 | O | Route |
| FND-02 : format de compromis en 4 lignes (décision, risque résiduel, signal de retour, owner) | 157-166 | A (gabarit) | Route |

### Direction artistique

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| FND-01 : trois lois (intention avant décoration, retenue avant accumulation, cohérence systémique avant créativité locale) | 94-100 | O | Route |
| Test de singularité (« si le logo et le nom disparaissent… ») | 117 | A | **Noyau** |
| Convergence de genre légitime ; ordre de décision JTBD → structure → hiérarchie → lisibilité → accessibilité → système visuel → polish | 120-126 | O | Route |
| Pluralité esthétique : trois questions pour ne pas imposer un canon | 147-153 | O | Route |
| CFT-00 : 8 dimensions de qualité créative avec un « signal observable attendu » pour chacune | 217-230 | O, avec signaux | Route |
| CFT-02 : 6 axes de position (structure, matière, voix, temporalité, densité, texte/image) avec leurs pôles et une question | 293-300 | A, pour générer une alternative | Route |
| Varier un axe à la fois ; 5 champs par alternative | 307-313 | A | **Noyau** |
| CFT-04 : design émotionnel en 3 niveaux (viscéral, comportemental, réflexif) et une table de 5 intentions (calme, énergie, confiance, luxe, sérieux) avec leurs leviers et contre-indications | 349-369 | A, comme points de départ | Route |
| CFT-04a : faut-il montrer l'objet de preuve ou le geste en premier ? Table de 4 questions ; « aucun des deux ne gagne par défaut » | 373-384 | A | Route |
| STYLE : 8 profils nommés (intention, expression, contre-indications), 7 dimensions de taxonomie, 9 dials, « test de style » (masquer couleurs, image et logo) | 643-713 | O, avec un test A | Route |
| Vocabulaire à rendre observable : 7 familles de mots faibles (« premium », « moderne », « intuitif »…) avec ce qu'il faut préciser | 737-749 | A, traduit les mots de la personne | Route |

### Composition

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Grammaire : intention → tension → foyer → masse → rythme → matière et type → contenu → états → résolution → retenue | 131-142 | A, par séquence | **Noyau** |
| Forme située : formule et 5 tests (tâche, donnée, état, preuve, retrait) | 272-283 | A | Formule au **noyau**, tests en route |
| Contrôles principaux (alignement, compensation optique, proximité, priorités, responsive pensé comme recomposition) | 327 | A | **Noyau** |
| Texte sur image (zone calme, voile local, mesure aux points défavorables) | 334 | A | **Noyau** |
| Cohérence et harmonie ; paires à inspecter sur capture (typo ↔ espace, densité ↔ usage…) | 339-345 | O | Route |
| Matrice motivation × construction (CFT-01) | 252-257 | A, table de décision | Route |

### Typographie

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Critères de choix (langues, chiffres, licence, performance, fallback, ton) | 411 | A | **Noyau** |
| Équilibre d'un titre (coupes, mot isolé, `text-wrap: balance`, écart d'échelle, lisible au flou) | 426 | A | **Noyau** |
| Comparer au moins deux voix sur le vrai titre (question de convergence) | 393 | A | **Noyau** |
| Une ou deux voix expressives ; polices variables comme système adaptatif | 416-420 | O / A | Route |
| Preuve typographique en 5 axes et 4 cas | 433-447 | A (gabarit) | Route |

### Couleur

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Palette par rôles (surfaces, textes, actions, états, frontières) ; répartition neutres / couleurs comme décision | 389 | A | **Noyau** |
| Question de convergence (neutres et un accent, sombre et doré, dégradé froid) | 393 | A | **Noyau** |
| OKLCH comme espace de conception ; dark mode recomposé et non inversé ; gamut élargi jamais porteur d'une information | 398-400 | A | Route |

### Craft, états, finition

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| **Table du vocabulaire perceptuel** : 13 lignes signal → geste conditionné → réinspection | 494-512 | **A**, l'objet le plus concret du corpus | **Noyau** |
| Jugement visuel situé : 6 lentilles et 3 niveaux (Correction, Précision, Intention), avec la question du niveau 3 | 457-486 | O | Route |
| États pertinents (focus, vide, erreur, overflow, chargement, permission refusée, image absente, valeur extrême) | 519-521 | A, liste | Route |
| **RCV-01 : récupération après erreur** (message près du champ, saisie conservée, gestion du focus selon le moment, parcours jusqu'au succès) | 524 | **A** | **Route seulement** |

### Assets, sources, moyens

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Test d'utilité d'une ancre (3 conditions) ; pièges du sourcing | 538-548 | A | Route |
| Fiche source en 12 champs | 556-569 | A (gabarit) | Route |
| Déclencheurs de profondeur de recherche | 573 | O | Route |
| Calibrations par domaine (cinéma, édition, affichage, architecture…) | 580 | O | **Noyau** |
| Contre-épreuve avant un asset directeur | 585 | A | Route |
| Traitement des assets moyens (recadrage, étalonnage, duotone, grain, trame) | 618 | A | **Noyau** |
| 11 rôles d'asset ; 11 médiums | 623, 627 | N (index) | Route |
| **Carte des moyens** : noms de sources par couche (Google Fonts, Fontshare, Lucide, Phosphor, shadcn, Radix, Wikimedia, Unsplash, Figma) | 923-933 | **N** | Résumé au noyau, liste en route |

### Contexte, technique, médiums

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Contextes à fort enjeu (3 catégories et leurs priorités) | 781-789 | O | Route |
| Responsive : recomposer plutôt que comprimer ; motion comme système d'états | 793-803 | A | Route |
| Preuve adaptée par question technique (5 lignes) | 813-819 | A | Route |
| Ordre P0 à P3 | 823 | O | Route (absent du noyau) |
| **Traduire production et observation par médium** : web et natif, image et identité, **print, document ou présentation**, motion, son, spatial | 831-840 | O, avec des limites précises | Route |
| Cinq responsabilités de preuve hors web | 844-852 | A (grille) | Route |

### Vérité, claims, convergence, intégrité

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Fiche claim en 10 champs ; séparation claim, source, asset, observation | 866-892 | A (gabarit) | Route |
| Goût défini comme « capacité à reconnaître une solution proportionnée » ; trois rôles du sourcing (direction, production, vérification) | 896-902 | O | Route |
| Marqueurs de vague (3 vagues datées, signaux à confirmer) ; écran d'accueil d'app | 908-914 | O (veille datée) | Résumé au noyau, détail en route |
| Test anti-slop procédural : « qu'est-ce qui change si cette ligne est vraie, fausse ou absente ? » | 729-733 | A | Route |
| INTEGRITY : modes d'échec, table « Bloque si… », contrôle d'intégrité, délégation | 950-1015 | A | Route |
| Niveaux d'autorité : légende des 7 tags | 48-62 | — | Route (la légende n'est pas au noyau, C27) |

## 4. Ce que le fichier ne possède pas

Constats de lecture, sans proposition :

1. **Presque aucune valeur chiffrée.** Hors du « 1 px » (3 fois), aucune échelle typographique, longueur de ligne, interligne, espacement, durée de motion ni seuil de contraste. Les seuils WCAG sont dans ACTION/GATE-A. Le savoir est relationnel par choix : « les valeurs chiffrées sont des points de départ » (DIRECTION). Mais ces points de départ ne sont pas ici. Ils sont peut-être dans `BIBLIOTHEQUE/CONTRACTS` (calibration locale), à vérifier dans la fiche n°2.
2. **Aucune ressource utilisable directement** (C38) : des noms de sources, sans statut, sans recette d'intégration, sans exemple de paire typographique ni de palette.
3. **Aucun exemple visuel** : tout est décrit en texte. Aucune image de référence, avant/après ou spécimen n'est archivé (l. 914 : « sélection et fichiers images non archivés »).
4. **Les médiums hors web** (documents, présentations, print) ont une table de traduction (l. 831-840) et une grille de preuve, mais aucune méthode de composition propre : la composition et la typographie sont pensées pour l'écran.

## 5. Potentiel présent mais peu exploité

Des éléments qui existent, sont concrets, et que l'agent ne voit que s'il charge la bonne route :

| Élément | Pourquoi il compte au regard de la mission | Accès actuel |
|---|---|---|
| **Vocabulaire à rendre observable** (l. 737-749) | Traduit directement les mots de la personne (« moderne », « premium », « intuitif ») en décisions observables. C'est le cœur de « exprimer son besoin sans maîtriser la mécanique ». | Route STYLE uniquement |
| **CFT-04, design émotionnel** (l. 359-365) | Répond aux retours du type « trop froid », « pas assez sérieux » avec des leviers et des contre-indications. | Route CRAFT |
| **CFT-04a, objet ou geste d'abord** (l. 373-384) | Nuance que le noyau ne porte pas : le noyau dit « l'objet arrive avant les bénéfices » ; ici, « aucun des deux ne gagne par défaut », et trois cartes égales peuvent être justes. | Route CRAFT |
| **RCV-01, récupération après erreur** (l. 524) | Recette complète et précise, concept protégé, mais le noyau n'en garde qu'une phrase (ligne « États »). | Route STATE |
| **Test de style** (l. 695) et **test anti-slop procédural** (l. 731) | Deux tests rapides et décisifs, l'un sur le rendu, l'autre sur la trace. | Routes STYLE |
| **Table par médium** (l. 831-840) | Seule base existante pour vos documents et présentations. | Route TECH |
| **CFT-02, axes de position** (l. 293-300) | Outil le plus direct pour produire une vraie alternative. | Route CRAFT (et doublon dans DIRECTION l. 766-773) |

## 6. Connexions

- **Vers DIRECTION :** absolus (l. 532), START et TREE (l. 757), VISUAL_TARGET (rôles et routes d'asset), CREATIVE-BOOT (MODAL).
- **Vers ACTION :** GATE-A (contraste, l. 400), STATUS (valeurs de repli), STRUCTURED-PROOF (preuve typographique), POLICIES (ressources techniques), ANTI-SLOP (matrice CFT-01, l. 261).
- **Vers BIBLIOTHEQUE :** SELECT et CONTRACTS (l. 490), COMPONENTS (l. 767).
- **Vers CHANGELOG :** promotion des claims (l. 881), migration des anciens identifiants (l. 64).

## 7. Observations faites en passant (à verser au registre)

| Observation | Lignes | Lien |
|---|---|---|
| Un **troisième** bloc FAST-PATH existe (`SAVOIR/FAST-PATH`) | 42-46 | Étend C22 |
| La grille « Jugement visuel situé » existe bien (6 lentilles) | 457-470 | Confirme C37 |
| Les axes de CFT-02 (l. 293-300) sont presque identiques à ceux de DIRECTION « Direction divergente » (l. 766-773) | — | Doublon de contenu |
| La nuance de CFT-04a manque au noyau, qui ne porte qu'un côté (l'objet d'abord) | 373 | Nouveau, à confirmer par la mesure |
| La légende des tags existe (l. 48), mais pas dans le noyau | 48-62 | Précise C27 |
| Doublons et section vide déjà connus | 908 et 913, 918 et 923, 825 | C31, C32 |

## 8. En une phrase

SAVOIR possède un **savoir de jugement riche, nuancé et souvent actionnable** : grammaire de composition, table de craft, émotions, axes de position, traduction des mots vagues, récupération d'erreur. Mais il est **presque sans valeurs chiffrées, sans ressources concrètes et sans exemples visuels**, et plusieurs de ses meilleurs outils ne sont visibles que si l'agent sait qu'il doit charger la route qui les contient.
