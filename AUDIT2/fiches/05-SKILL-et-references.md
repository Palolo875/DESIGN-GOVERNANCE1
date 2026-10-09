# Fiche — SKILL.md et references/ (canonical_minimum, examples, flow, machine_projection)

Commit audité : `9681d4e`. Chemins relatifs à `skills/design-governance-practice/` sauf mention. Lecture intégrale des cinq fichiers, du script `scripts/build_core.py` et des sources des blocs du noyau. Mesures reprises de `mesures.md` / `mesures.json` ; deux mesures propres (poids des blocs, positions dans le fichier) sont calculées depuis `build_core.py` et le texte, et marquées « calcul de l'auditeur ».

Plan : A. SKILL.md (analyse détaillée) · B. canonical_minimum.md · C. examples.md · D. flow.md · E. machine_projection.md · F. Synthèse commune.

---

# A. SKILL.md

## A1. Identité

- **Rôle actuel.** « Couche d'activation » de Design Governance (`SKILL.md:8`) : un en-tête, un paragraphe d'accroche, un « noyau de fabrication » de 41 062 caractères compilé depuis quatre sources, et cinq renvois (`SKILL.md:218-224`). Il mêle quatre rôles : posture, table de routage, savoir de fabrication, règles de sortie et de trace.
- **Public réel** : l'agent (tutoiement impératif, `SKILL.md:17`). **Public visé par la charte** : l'agent, avec « une skill courte, des chemins selon l'effort, des renvois précis, aucune lecture inutile » (charte §2). Ni le débutant ni l'équipe ne sont servis ici (`SKILL.md:224` les renvoie à README, QUICKSTART, READING_MAP).
- **Taille** : 42 978 caractères, 44 559 octets, 224 lignes, 6 296 mots. Plafond `CORE_BUDGET_BYTES = 46_000` (`scripts/build_core.py:31`) : marge de 1 441 octets (3 %). Titres : {1:1, 2:2, 3:10}. Codes : 202, soit 32 pour 1000 mots. Phrases : moyenne 21,1, p90 35, 8 % au-delà de 40 mots. Non vérifié : 2. Vestiges : 0.
- **Sources du noyau** (calcul de l'auditeur, `build_core.py:NOYAU`, sans les sauts de ligne) : SAVOIR 16 264, DIRECTION 15 457, ACTION 4 686, BIBLIOTHEQUE 4 087, soit 40 494. Plus gros bloc : `COMP-VOCABULAIRE` (SAVOIR) 7 859, soit 18 % du fichier. Suivent `CHARGE-TABLE` 3 679, `CHARGE-REGLE` 2 350, `STRUCT-SIGNAUX` 1 866, `SORTIE` 1 356, `PREMIER-OBJET` 1 355, `TRACE` 1 265, `BOUCLE-ATELIER` 1 209.

## A2. Verdicts de la grille

| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | Les premières lignes (`SKILL.md:6-8`) disent « couche d'activation », « sources normatives », « gates, statuts et preuves » : le rôle est décrit par la gouvernance, pas par le design. Quatre rôles dans un seul fichier. |
| F2 Public | conforme (agent) / à corriger (lisibilité humaine) | Registre impératif adapté à l'agent. Mais le fichier est aussi le premier que lit toute personne qui ouvre le dossier ; rien ne le dit. |
| F3 Structure | à corriger | Trois niveaux au plus (conforme). Mais une seule section de niveau 2 pèse 41 062 caractères ; ses dix sous-sections vont de 1 259 à 7 887 caractères (`mesures.json`, lignes 15-200). Deux « sections » sont en fait un seul tableau (`SKILL.md:33-39`, 3 679 car. ; `SKILL.md:139-153`, 6 611 car.). |
| F4 Une seule fois | à corriger | Doublons internes (voir A5, défaut SK-5) ; en plus, tout le noyau est une copie générée des sources (voir A6). |
| F5 Langue | à corriger | 202 codes ; §2 « Classer, puis charger » à 100 codes pour 1000 mots (`mesures.json`, ligne 25). Termes non définis dans le fichier : `NOT-VERIFIED`, `N/A-JUSTIFIED` (`SKILL.md:45`), `EXPLORATORY` (`SKILL.md:57`), `MODAL`/`PARTI` (`SKILL.md:8`), « absolu 4 / absolus 1 et 5 / absolu 2 » (`SKILL.md:23, 27, 202`), « B1b » (`SKILL.md:180`). Point fort : la réponse visible est protégée du jargon (`SKILL.md:213`). |
| F8 Longueur | à corriger | La charte attend « une skill courte ». 43 000 caractères sont lus à chaque run, quel que soit le mode (voir A4). |
| F9 Limites | conforme | 2 mentions « non vérifié ». Les limites sont dites une fois par sujet : recherche littérale (`SKILL.md:29`), rendu (`SKILL.md:155, 167`), sources absentes (`SKILL.md:8`). |
| F10 Exemples | à corriger (mineur) | Valeurs et recettes chiffrées qui risquent de devenir des réglages par défaut (voir A7). Pas de couleur, police ni mise en page type imposées. |
| F11 Vestiges | conforme | 0 vestige mesuré ; aucun renvoi vide ni nom de révision. |

## A3. Évaluations demandées

### Ordre de lecture (calcul de l'auditeur, positions en caractères)

| Position | Ce que l'agent apprend | Famille |
|---|---|---|
| 0-1 139 | En-tête + accroche : « couche d'activation », gates, statuts, sources qui font foi (`SKILL.md:1-8`) | méta |
| 1 308 | §1 Rôle et posture (1 259) : directeur·rice artistique, première idée = hypothèse (`SKILL.md:15-23`) | design |
| 2 568 | §2 Classer, puis charger (6 608) : règle de vitesse, mode d’emploi du lecteur de routes, table de 5 modes (`SKILL.md:25-41`) | gouvernance/méta |
| 9 177 | §3 Brief et premier objet (3 413) | design |
| 12 591 | §4 Moyens et vérité (3 890) | produit + gouvernance |
| **16 482 (38 %)** | §5 Structure : premier contenu de composition (`SKILL.md:71`) | design |
| 20 597 | §6 Composition | design |
| **24 141 (56 %)** | §7 Gestes de finition : premier savoir de finition (`SKILL.md:135`) | design/produit |
| 32 029 | §8 Couleur et convergence | design |
| 33 587 | §9 Boucle d'édition | design + produit + gouvernance |
| 38 654 | §10 Proposition, sortie et trace | produit + gouvernance |

Constat : après la posture, l'agent lit 6 600 caractères de routage et 7 300 de brief et de vérité avant la première ligne de composition. Le plus dense en codes (§2) passe avant tout savoir de forme. Le fond est cohérent (poser le problème, puis fabriquer, puis boucler, puis rendre compte) ; c'est le **poids du routage en position 2** qui renverse la priorité « le design au cœur » (charte §3, principe 2).

### Ce qui aide vraiment à produire un bon design (estimation par section, à affiner)

- **Valeur de conception directe, environ 25 000 caractères (58 %)** : §1 (1,3k), §3 (3,4k), §5 (4,1k), §6 (3,5k), §7 (7,9k), §8 (1,6k) et la partie « seconde boucle / variation d'un axe / revue courte » du §9 (environ 3,5k).
- **Ce qui est le plus actionnable** : `SKILL.md:21` (première idée testée contre la convergence), `SKILL.md:49` (promesse → objet de preuve → geste), `SKILL.md:101-105` (signaux de convergence, test de trame), `SKILL.md:121-125` (test de singularité, forme située), `SKILL.md:131` (équilibre d'un titre), `SKILL.md:139-153` (13 gestes de finition avec condition), `SKILL.md:161` (question de convergence), `SKILL.md:182-184` (éditer par retrait, réduction ou transformation).
- **Observation de fond (à vérifier par le propriétaire)** : le noyau est surtout correctif (signaux, questions de reprise, tests de convergence). Le savoir génératif (comment démarrer une composition forte) se limite à `SKILL.md:109-125` ; le reste est renvoyé à des routes.

### Ce qui relève de la gouvernance (environ 13 000 à 14 000 caractères, 31 %)

- §2 en entier (6 608) : mode d'emploi du lecteur de routes, table de chargement par mode avec gates A/B/C, `RUN_CARD`, `CLOSE-PACKAGE`, `HANDOFF` (`SKILL.md:25-41`).
- `SKILL.md:57` « Explorer, accepter, diffuser » (1 146) : ancres, `EXPLORATORY`, `FAIL-ASSUMED` ; c'est une règle de statut, pas de forme.
- `SKILL.md:180` (portée B1b, deux motifs `N/A-JUSTIFIED`) et le paragraphe de trace complète (`SKILL.md:215`, 1 292).
- `SKILL.md:213` (exposition des codes sur demande) et `SKILL.md:23` (« passer le gate »).

### Charge pour l'agent

- **Coût fixe** : 44 559 octets lus à tout run. `mesures.md` ne fournit pas de cible par chemin ; la grille S2 donne environ 80 000 caractères pour « une page en direction ». Le noyau seul en représente donc plus de la moitié.
- **Le coût ne dépend pas du mode.** La table `SKILL.md:35` prévoit pour LITE un chemin court (`ACTION/RUN-LITE`, `FAST-PATH`, `GATE-A`, `GATE-B/B2`, `B6`), mais l'agent a déjà lu 43 000 caractères dont la moitié ne concerne pas une retouche (§3, §5, §6, §8, §9 seconde boucle, §10 trace complète). Avec `DIRECTION/START` (13 978) et `GATE-A` (11 935), une retouche de contraste dépasse 60 000 caractères (estimation, à vérifier lecture par lecture ; `read_route.py` permet des lectures de sous-sections).
- **Plafond comme aimant.** Le budget de 46 000 octets est un plafond de santé, pas une cible (`build_core.py:31`), mais il laisse 3 % de marge : tout ajout futur passe par un arbitrage serré ; à l'inverse, rien ne force un allègement.
- **Plus gros blocs** : `COMP-VOCABULAIRE` 7 859 (tableau de 13 gestes), dont `SKILL.md:155` dit : « utilise une ligne pertinente ; ne déroule pas toutes les lignes » (`SKILL.md:137`). Le noyau paie donc 13 lignes pour en lire une. Même remarque pour `CHARGE-TABLE` (3 679) : un agent lit une ligne sur cinq.
- **Cellules trop lourdes** : la ligne DIRECTION de la table de chargement (`SKILL.md:38`) compte une trentaine de routes entre ses deux colonnes ; la colonne « Ajouter seulement si » répète deux fois la condition `DIRECTION/DOMAIN-FRAME` (`SKILL.md:37` et `38`).

### Codes visibles

- 147 codes entre accents graves dans le noyau, 78 distincts. Les plus fréquents : `SAVOIR/STATE` ×9, `ACTION/GATE-A` ×7, `DIRECTION` ×6, `SAVOIR/CRAFT/CFT-03` ×6, `DIRECTION/START` ×5 (calcul de l'auditeur).
- Termes anglais non définis dans le fichier : gate, scope, owner, blast radius, handoff, run, checkpoint, JTBD, claim (`SKILL.md:35, 45, 89, 213`).
- Renvois à des règles numérotées d'un autre fichier sans les nommer : « absolu 4 » (`SKILL.md:27`), « ABSOLUS 1 et 5 » (`SKILL.md:23`), « absolu 2 de `DIRECTION` » (`SKILL.md:202`).
- Pour un lecteur humain, la lecture du noyau n'est pas possible sans les sources. Pour l'agent, la densité est tolérable en §2 (c'est une table d'adresses) mais elle imprègne aussi le savoir de design (`SKILL.md:35-38`, `45`, `49`).

## A4. Sections

| Section (ligne) | Ce qu'elle apporte | Famille | Public | Observation principale | Disposition proposée |
|---|---|---|---|---|---|
| En-tête (1-4) | Nom et déclencheur (429 caractères) | méta | agent | « plafond déclaré », « trace proportionnée au risque », « charger les sources progressivement » : la description parle gouvernance | réécrire (forme) : décrire ce que la skill fait pour la personne |
| Accroche (6-8) | Dit que la skill est une couche d'activation et que les sources font foi | méta | agent | Jargon dès la première phrase (Creative Boot, `MODAL`/`PARTI`, `FABRICATION`) ; contient la règle « sources absentes » dupliquée en `SKILL.md:223` et `canonical_minimum.md:7,24` | réécrire (forme) ; déplacer la règle « sources absentes » vers Références |
| §1 Rôle et posture (15-23) | Posture, première idée, piège de conformité | design | agent | Meilleure ouverture possible ; `SKILL.md:23` introduit le mot « gate » avant sa définition | garder (tête de fichier) |
| §2 Classer, puis charger (25-41) | Règle de vitesse, outil de recherche, table de 5 modes, clôture | gouvernance/méta | agent | 6 608 caractères, 93 codes, position 2 ; mélange vitesse, manuel d'outil et routage ; `SKILL.md:41` fourre-tout (clôture, tags, qui lit README) | scinder : (a) règle de vitesse et table de chargement ; (b) manuel de `read_route.py` (`SKILL.md:29-31`) ; (c) clôture et tags (`SKILL.md:41`) |
| §3 Brief et premier objet (43-51) | Prise de brief minimale, contenu d'exemple marqué, chaîne promesse → objet → geste, cohérence des données | design | agent | Dense mais utile. `SKILL.md:49` empile sept notions codées (situation, tension, geste produit, objet de preuve, marquage de vérité, position/exclusion, contre-choix) | garder ; réécrire (forme) `SKILL.md:49` |
| §4 Moyens et vérité (53-69) | Artefact complet avant rendu, ancre, moyens, assets moyens, calibrations, faux assets, marquage de vérité | produit + gouvernance | agent | Trois sujets : fabrication (`55, 61, 63`), vérité (`65, 67, 69`) et statut de direction (`57`). Le marquage de vérité est dit en trois endroits (`47`, `49`, `67-69`) | scinder : `SKILL.md:57` vers le module de gouvernance ; fusionner `47`, `49`, `67-69` en un seul passage de vérité |
| §5 Structure (71-105) | Où vit l'interface, caractère perceptuel, 7 axes de tension, activation de la bibliothèque, signaux, test de trame | design | agent | Premier vrai contenu de composition, mais à 38 % du fichier. Les 7 axes (`SKILL.md:79-87`) sont un lexique fixe | garder ; déplacer plus haut |
| §6 Composition (107-133) | Séquence de décision, singularité, forme située, contrôles, typographie, titre, texte sur image | design | agent | Section la plus propre : peu de codes (3, soit 6 pour 1000 mots) ; `SKILL.md:129` porte la seule consigne de typographie du noyau | garder |
| §7 Gestes de finition (135-155) | Activation du craft ; 13 gestes avec signal, geste, condition, réinspection | design/produit | agent | 7 887 caractères (18 %) ; le seul tableau à quatre colonnes ; une ligne utile par run (`SKILL.md:137`) ; valeurs chiffrées (voir A7) | garder le savoir ; **décision à prendre** : noyau ou route lue à la demande (le contenu vit déjà dans `SAVOIR.md:503-524`) |
| §8 Couleur et convergence (157-163) | Palette par rôles, question de convergence, marqueurs de vague | design | agent | Court, net. Cite une liste de palettes et de polices « par réflexe » (`SKILL.md:161`), à contexte daté dans `SAVOIR/TOOLS/CONVERGENCE` | garder |
| §9 Boucle d'édition (165-198) | Boucle commune, `check_render`, tableau de diagnostic, atelier B1b, lecture légère, revue courte, repasse, variation d'un axe | design + produit + gouvernance | agent | Trois familles dans un seul bloc ; `SKILL.md:167` mêle boucle de design et manuel de `check_render` (options, `--allow-external`) ; `SKILL.md:180` est une règle de gate | scinder : check_render vers un manuel d'outils ; B1b vers gouvernance ; garder le reste |
| §10 Proposition, sortie et trace (200-215) | Première proposition = checkpoint, 4 rubriques de réponse, silence des codes, trace légère/complète | produit + gouvernance | agent | Les 4 rubriques et la règle « pas de jargon » sont du produit ; la trace légère/complète est de la gouvernance | scinder : réponse visible (garder) ; trace (déplacer vers gouvernance, laisser un renvoi) |
| Références conditionnelles (218-224) | Cinq renvois | méta | agent | « Aide-mémoire : seulement si les sources V1 sont absentes » répète `SKILL.md:8` ; `flow.md` décrit comme « la vue courte du chemin » | réécrire (forme) |

## A5. Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| SK-1 | coût de lecture | important | 44 559 octets lus à chaque run ; §3, §5, §6, §8 et la moitié de §9-§10 ne servent pas une retouche LITE | Décrire des tranches « toujours lu » et « à la demande » ; décision de la phase 2 (cibles par chemin) |
| SK-2 | structure | important | §2 (6,6k) en position 2 ; première composition à 38 %, premiers gestes de finition à 56 % (`mesures.json` ligne 25 ; calcul de l'auditeur) | Faire passer le savoir de design avant le routage, ou rendre le routage plus court |
| SK-3 | convergence (gouvernance mêlée au design) | important | `SKILL.md:25-41` ; `57` ; `180` ; `215` ; grille S9 : « non : les deux sont mêlés » | Isoler les passages gouvernance (A3) pour que le chemin de design se lise sans eux |
| SK-4 | coût de lecture | important | `COMP-VOCABULAIRE` 7 859 caractères, 13 lignes dont une seule sert (`SKILL.md:137`) | Poser la question noyau ou route (A4, §7) |
| SK-5 | répétition | important | (a) condition `DIRECTION/DOMAIN-FRAME` répétée `SKILL.md:37` et `38` ; (b) « Sans risque critique touché — voir Protection de niveau » deux fois (`35`, `36`) ; (c) `ACTION/UI-UX-REALITY si la surface UI/UX est nouvelle…` deux fois (`37`, `38`) ; (d) marquage de vérité en trois endroits (`47`, `49`, `67-69`) ; (e) première proposition = checkpoint (`55`, `202`) ; (f) retour à `DIRECTION/START` (`35`, `36`, `176`) | Fusionner chaque doublon dans son meilleur lieu ; attention au contrôle `UIX-01` qui exige la phrase dans les lignes STANDARD et DIRECTION |
| SK-6 | langue | important | Voir F5 ; « absolu 4 », « B1b », `EXPLORATORY`, `MODAL` non définis | Définir ou remplacer à la première occurrence |
| SK-7 | structure | mineur | Manuel d'outil dans le récit : `SKILL.md:29` (1 472 car., trois options de `read_route.py`) ; `167` (cinq options de `check_render.py`) | Grouper les deux manuels hors du savoir de design |
| SK-8 | risque | mineur | Plafond de 46 000 octets : marge de 3 % (`test_core_budget.py`) | Remplacer par des cibles par chemin en phase 2 ; garder un plafond de sécurité |
| SK-9 | risque | mineur | `scripts/read_route.py` et `scripts/check_render.py` cités en chemin relatif (`SKILL.md:29, 167`), mais le dossier de la skill ne contient que `SKILL.md` et `references/` ; `package_manifest.json` place les scripts à la racine | À vérifier : comment la skill est installée seule (grille S10) ; le texte gère l'absence des sources (`SKILL.md:8`) mais pas celle des scripts |
| SK-10 | coût de lecture | mineur | Phrases : 8 % au-delà de 40 mots, la valeur la plus haute des fichiers de savoir (`mesures.md`) ; paragraphes de 1 100 à 1 500 caractères (`29`, `49`, `57`, `215`) | Couper à la réécriture de forme |
| SK-11 | convergence | mineur | Gabarit de réponse fixe à quatre rubriques (`SKILL.md:206-211`), repris tel quel par l'exemple (`examples.md:38`) | À garder (verrouillé par LCF-C2) ; ne pas laisser l'exemple figer la voix |
| SK-12 | produit | mineur, à vérifier | La vérification du rendu sur ordinateur et mobile n'est pas énoncée comme plancher dans le noyau : « mobile » n'apparaît qu'en `SKILL.md:131, 149, 152` ; le plancher repose sur `ACTION/GATE-A` (`ACTION.md:683, 719`) | Vérifier que l'invariant de la charte (§4) est bien porté par la route chargée dans tous les modes |

## A6. Mécanisme du noyau (compilation)

- Les blocs `<!-- noyau:début X -->` vivent dans quatre sources : DIRECTION (ROLE, POSTURE, MOY-PLAFOND, CHARGE-REGLE/TABLE/FIN, BRIEF, CONTENU, PREMIER-OBJET, VER-SCENE, VER-AUDIENCE, BOUCLE, BOUCLE-DIAGNOSTIC, BOUCLE-QUESTIONS, ANCRE), SAVOIR (17 blocs), ACTION (SORTIE, TRACE, CHECKPOINT, BOUCLE-ATELIER), BIBLIOTHEQUE (5 blocs STRUCT-*).
- Les titres des 10 sections et leur ordre sont fixés dans `build_core.py:NOYAU` (lignes 34-61), **pas** dans `SKILL.md`. Toute réorganisation de l'ordre de lecture passe par ce registre, par `CORE_FLOOR` (12 phrases exigées, `validate_structure.py:616-627`) et par les contrôles `UIX-01`, `NOY-02`.
- Les marqueurs `<!-- concept:… -->` sont retirés à la compilation (`build_core.py:CONCEPT`).
- Les mesures de répétition excluent « la copie compilée du noyau » (`mesures.md`) : le noyau est donc, par construction, **dupliqué à 100 %** entre `SKILL.md` et les quatre sources. C'est un choix d'architecture (charte §4 : « la construction de la skill à partir des sources » est conservée), mais il double le poids du dépôt (environ 40 000 caractères) et fait que le lecteur de routes remplace à la lecture les blocs déjà présents (`SKILL.md:29`, « remplacés par un renvoi à leur section »).

## A7. Ce qui fige ou pousse à la convergence

Valeurs et recettes chiffrées que l'agent risque de recopier systématiquement :
- « liseré clair de **1 px CSS** » sur le bord supérieur d'une surface (`SKILL.md:145`) et « décalage local de **1 px CSS** » pour l'alignement optique (`SKILL.md:151`) : conditionnels dans le texte, mais le chiffre est ce qui se retient.
- Formule `rayon intérieur = max(0, rayon extérieur − inset)` (`SKILL.md:141`) ; `font-variant-numeric: tabular-nums` (`146`) ; `text-wrap: balance` (`131`) : recettes valables, mais appliquées sans condition elles donnent le même détail à toutes les pages.
- Liste fermée de sept axes de tension nommés `DENSITY`, `FOCUS`, `PROOF-POSITION`, `TEMPORALITY`, `FIELD-MATERIAL`, `NAVIGATION`, `ACTION` (`SKILL.md:79-87`) et six paires de caractère (`75`) : l'agent choisira dans ce lexique, pas hors de lui.
- Voix typographiques proposées (« grotesque, serif, mécane, manuscrite ou vernaculaire du lieu », `SKILL.md:161`) et palettes « par réflexe » (« sombre et doré, dégradé froid », `161`) : l'énumération des voix à comparer devient la liste des voix choisies. Les palettes sont des contre-exemples, mais ne sont pas marquées datées dans le fichier.
- Trame modale d'un SaaS « promesse, logos, trois bénéfices, tarifs, FAQ » (`SKILL.md:103`) : contre-exemple, donc risque faible.
- Le système connaît le risque : `SKILL.md:101` signale le grain repris « d'un brief à l'autre » comme signal de convergence.

## A8. Savoir à protéger

- Posture d'un·e DA et product designer ; pas d'imitation d'un canon « premium » : `SKILL.md:17-19`
- Première idée = hypothèse ; ne pas remplacer le biais de conformité par une obligation de nouveauté : `21`
- Piège de conformité (passer le gate plutôt que concevoir) : `23`
- Règle de vitesse : déclarer mode, décision, risque, preuve, arrêt avant de construire : `27`
- Retrouver un savoir : `--trouver`, limites de la recherche, lecture de la route en entier, blocs remplacés par un renvoi : `29`
- Connexions situées par `--connexions` : `31`
- Table des 5 modes, colonnes « charger d'abord » et « ajouter seulement si » : `33-39`
- Clôture par mode ; tags `[REQUIS PAR LE MODULE]` et `[MÉTHODE]` ; rôle de README, QUICKSTART, READING_MAP : `41`
- Prise de brief : au plus trois demandes, build dans le même tour, hypothèses nommées : `45`
- Destination réelle sans contenu : contenu d'exemple marqué, action principale fonctionnelle, signes de preuve jamais inventés : `47`
- Chaîne promesse → objet de preuve → geste ; objet de préférence codé ; marquage `TRUTH/*` près de l'objet : `49`
- Cohérence des données d'exemple : `51`
- Artefact complet avant premier rendu ; plafond déclaré ; un défaut dominant : `55`
- Explorer, accepter, diffuser ; ancres ; `FAIL-ASSUMED` réservé aux échecs observés : `57`
- Carte des moyens par couche, licence et disponibilité : `59`
- Traitement des assets moyens : `61`
- Calibrations par domaines : `63`
- Pas de faux asset de marque : `65`
- Marquage local de vérité à deux axes ; `TRUTH/*` jamais dans l'interface : `67-69`
- Structure : où elle vit, circulation du regard, preuve tangible, action : `73`
- Caractère perceptuel et traduction en relations observables : `75`
- Axes de tension : `77-87`
- Activer la bibliothèque : intention → niveau → levier → effet : `89`
- Sept signaux d'enquête et leurs questions de reprise : `91-101`
- Test de trame (romps l'ordre, le foyer ou l'objet) ; signal ≠ ajout mécanique de scène : `103-105`
- Séquence de composition et six questions : `109-119`
- Test de singularité ; formule de la forme située : `121-125`
- Contrôles principaux et responsive comme recomposition : `127`
- Plancher typographique : `129`
- Équilibre d'un titre (sens, forme, hiérarchie ; capture desktop et mobile) : `131`
- Texte sur image : `133`
- Activation du craft ; 13 gestes de finition : `137-153`
- Choix et contrôle des gestes : `155`
- Palette par rôles ; question de convergence (≥ 2 voix typographiques) ; marqueurs de vague : `159-163`
- Boucle d'édition et `check_render` : `167`
- Tableau de diagnostic de la seconde boucle : `169-178`
- Portée B1b : `180`
- Lecture légère, retrait/réduction/transformation, comparaison de captures : `182-184`
- Revue courte en six points : `186` ; note de ce qui a changé : `188`
- Repasse complète selon le mode : `190`
- Variation d'un axe situé à la fois, cinq éléments à préciser : `192-198`
- Première proposition = checkpoint ; validation ≠ acceptation : `202`
- Quatre rubriques de la réponse visible : `204-211`
- Activation silencieuse ; codes cachés sauf demande ; limites visibles : `213`
- Trace légère de six lignes ; trace complète : `215`
- Références conditionnelles : `218-224`

## A9. Dépendances et risques de déplacement

- **Cité par** : README, QUICKSTART, READING_MAP, CHANGELOG, RELEASE_NOTES, `package_manifest.json`, `build_distributions.sh`, `build_core.py`, `read_route.py`, `validate_structure.py`, `validate_reading_map.py` (`mesures.json`, `fichiers_cites`).
- **Cite** : `QUICKSTART.md`, `READING_MAP.md`, `README.md`, les quatre références, `scripts/build_core.py`, `scripts/check_render.py`, `scripts/read_route.py` ; les sources via 78 codes distincts.
- **Contrôles qui verrouillent ses phrases** (`mesures.json`, `controles`) : `validate_structure.py` 30 phrases (dont `CORE_FLOOR` ×12, `UIX-01`, `NOY-02`, `SKL-01` pour l'en-tête YAML) ; `validate_reading_map.py` 7 (dont LCF-24, LCF-43, LCF-44, LCF-45, LCF-54, LCF-C2) ; `build_core.py` 6 ; `read_route.py` 5 ; `test_audit_regressions.py` 4 ; `test_read_route.py` 3 ; `validate_all.py` 2 ; `test_core_budget.py` (budget en octets).
- **Si on déplace une phrase du noyau** : la déplacer dans sa **source** et éditer `NOYAU` (titres, ordre) ; sinon `NOY-02` échoue. Si on la retire du noyau, ajuster `CORE_FLOOR` et les LCF ci-dessus. Ne jamais éditer la section compilée à la main (`SKILL.md:13`).
- **Piège particulier** : `UIX-01` exige que `ACTION/UI-UX-REALITY si la surface UI/UX est nouvelle ou substantiellement modifiée` figure dans les lignes STANDARD et DIRECTION, et pas dans LITE (`validate_structure.py:700-720`) : la répétition SK-5(c) est donc protégée par un contrôle.
- **Phase 5** : la charte (§5) interdit de toucher à la skill avant la phase 5.

## A10. Synthèse de la partie SKILL.md

Un noyau très riche en savoir de design (environ 58 % du fichier) mais lu en entier à tout run, avec le routage et les règles de statut en position 2 et 4. L'enjeu principal n'est pas de perdre du fond, c'est de **changer l'ordre et la tranche** : savoir de design d'abord, routage court, gouvernance isolée, manuels d'outils groupés. Tout changement passe par le registre `NOYAU` de `build_core.py` et par une trentaine de verrous de phrases.

---

# B. references/canonical_minimum.md

## B1. Identité
Aide-mémoire de repli quand les sources V1 sont absentes : liste des séparations à ne pas inventer. Public réel : l'agent sans sources. Public visé : agent. 1 732 caractères, 25 lignes, 48 codes pour 1000 mots (12 codes), phrases moyenne 13,4, p90 21, 0 % au-delà de 40 mots, non vérifié : 1, vestiges : 0.

## B2. Verdicts

| Critère | Verdict | Preuve |
|---|---|---|
| F1 | conforme | Les trois premières lignes (`canonical_minimum.md:1-3`) disent rôle et limite. |
| F2 | conforme | Agent sans sources ; le contenu correspond. |
| F3 | conforme | H1 + 3 H2 (« Source et limites », « Séparations indispensables », « Priorité »). |
| F4 | à corriger (mineur) | La règle « sources absentes / sources qui font foi » est dite trois fois : `canonical_minimum.md:7`, `:24`, `SKILL.md:8` ; et une fois encore en `SKILL.md:223`. |
| F5 | conforme (agent) | 12 codes, tous sont l'objet du fichier. Mais aucun n'est défini : ils sont listés avec une phrase de séparation (`:11-18`). |
| F8 | conforme | 1 732 caractères. |
| F9 | conforme | Le fichier est lui-même une limite : « une proposition… ne doit pas être présentée comme un run V1 conforme » (`:7`). |
| F10 | conforme | aucun exemple. |
| F11 | conforme | rien. |

## B3. Sections

| Section (ligne) | Apport | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Source et limites (5-7) | Signaler l'absence, ne pas inventer, proposition = hypothèse | méta | agent | Doublon de `SKILL.md:8` | fusionner avec la règle de `SKILL.md:8` (un seul lieu) |
| Séparations indispensables (9-20) | 8 couples de codes à ne pas confondre | gouvernance | agent | Donne les noms sans les sens (ex. `STATE`, `ISSUE`, `VERDICT` : « significations distinctes ») | garder ; **à vérifier** : l'utilité réelle d'une liste de noms sans définition, en l'absence des sources |
| Priorité (22-24) | Les sources font foi | méta | agent | Redit `:7` | fusionner |

## B4. Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| CM-1 | répétition | mineur | `canonical_minimum.md:7, 24` ; `SKILL.md:8, 223` | Un seul passage, au bon endroit |
| CM-2 | risque | mineur | `:11-18` : codes sans sens ; l'agent sans sources ne peut pas les employer correctement | Décider si le repli doit définir ou seulement interdire |
| CM-3 | structure | mineur | Aucun contrôle ne cite ce fichier par nom (grep) ; il est dans le manifeste (`package_manifest.json:69, 134`) | Ne pas le retirer sans ajuster le manifeste |

## B5. Savoir à protéger
- Procédure en l'absence des sources : le signaler, ne rien inventer, proposition = hypothèse : `:7`
- Huit séparations (`MODE`, `STATE`/`ISSUE`/`VERDICT`, `A/B/C` ≠ `V/U/A/T`, `DECISION-INTENT`, `DECISION-CHANGE`, `NOT-VERIFIED`, `NOT-OBSERVED`, `N/A-JUSTIFIED`) : `:11-18`
- Une rationale, une référence, une ancre, un asset ou une capture ne prouvent pas seuls l'implémentation, l'usage ou l'accessibilité : `:20`
- Les sources font foi ; la skill n'est jamais l'autorité : `:24`

## B6. Ce qui fige
aucun relevé.

## B7. Dépendances
Cité par `SKILL.md:8` et `:223` ; manifeste. Aucun verrou nominatif. Le corpus `skills/**/*.md` est parcouru par les contrôles généraux (`validate_structure.py:383`), donc une phrase interdite écrite ici serait détectée.

## B8. Synthèse (partie B)
Petit fichier propre, mais sa raison d'être est étroite (cas « sources absentes ») et la règle est déjà dans `SKILL.md:8`. Candidat à la fusion avec cette règle, sous décision.

---

# C. references/examples.md

## C1. Identité
Cinq exemples de runs sous forme de traces (`LITE`, `DIRECTION` brief flou, `DIRECTION` première scène, `DIRECTION + STYLE`, `SYSTÈME`). Public réel : l'agent qui apprend le format de trace et l'équipe qui audite. Public visé : agent et équipe. 9 706 caractères, 121 lignes, titres {1:1, 2:5}, plus grosse section 2 423 (« première scène identitaire »), **104 codes, soit 77 pour 1000 mots** (le plus élevé des fichiers de la skill), phrases moyenne 19,8, 8 % au-delà de 40 mots, non vérifié : 5.

## C2. Verdicts

| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | Trois citations d'avertissement (`examples.md:3-7`, environ 1 300 caractères) avant le premier exemple ; le rôle (montrer des traces) est noyé dans les restrictions. |
| F2 Public | à corriger | Aucun public nommé ; le contenu est lisible seulement par qui connaît `DECISION-CHANGE`, `RUN_CARD`, `B1b`. |
| F3 Structure | à corriger | Cinq H2 de formes différentes (« LITE — correctif local », « DIRECTION — fabrication… ») ; le chemin par défaut (brief flou) est en position 2, après un exemple de clôture complète. |
| F4 Une seule fois | à corriger | Mêmes avertissements répétés huit fois (`:3, 5, 7, 34, 76, 78, 99, 120`) ; le renvoi à `machine_projection.md` et `schemas/run_card.example.json` redit `machine_projection.md:5-10`. |
| F5 Langue | à corriger (important) | 104 codes ; `SIMULATED` (`:3`) n'est défini dans aucune source (grep sur `V1/official/*.md` : 0 résultat) ; « authored » (`:55`), « blast radius » (`:120`), « dials » (`:91`) non définis. |
| F8 Longueur | conforme | 9 706 caractères, chargé à la demande. |
| F9 Limites | à corriger (mineur) | Huit rappels de non-preuve (`:3, 5, 7, 34, 76, 78, 99, 120`). |
| F10 Exemples | à corriger (important) | Voir C5. |
| F11 Vestiges | à corriger (mineur) | Dates figées : `revue : 2026-10-09` (`:71`), égale à la date du jour de l'audit ; elle deviendra un exemple périmé. |

## C3. Sections

| Section (ligne) | Apport | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Avertissements (3-7) | Dit « reprendre la séquence, pas le style » ; trace ≠ sérialisation ; niveaux de trace | méta | agent | Bon principe, mais l'exemple 3 n'applique pas la règle (valeurs complètes) | réécrire (forme) : une seule consigne |
| LITE — correctif local (9-28) | Trace complète d'une retouche de contraste jusqu'à `CLOSED` | gouvernance | agent/équipe | Montre une **clôture** pour une retouche de bouton ; contredit l'esprit « l'effort proportionné » et « trace légère par défaut » (`SKILL.md:215`) | déplacer vers le module de gouvernance ; **décision à prendre** : montrer la forme légère à la place |
| DIRECTION — fabrication depuis un brief flou (30-49) | Chemin par défaut : brief, hypothèses, réponse visible, trace légère | design + produit | agent | Seul exemple de la sortie par défaut ; le seul à utiliser des crochets pour ne pas figer | garder ; déplacer en tête ; durcir les crochets (voir C5) |
| DIRECTION — première scène identitaire (51-78) | Trace clôturée avec réserve | gouvernance | équipe | Concept complet et concret : thèse, objet, composition, matière | déplacer vers gouvernance ; remplacer le concept par des crochets |
| DIRECTION + STYLE (80-99) | Profil d'expression situé | design/gouvernance | agent | Cas `STYLE/DIGITAL_MEMORY` complet | garder ; remplacer le cas par des crochets |
| SYSTÈME — composant partagé (101-120) | Extension d'un composant, clôture `RETURN` | gouvernance | équipe | Cas technique neutre (Select), pas de style recopiable | déplacer vers gouvernance |

## C4. Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| EX-1 | convergence | important | Voir C5 : concepts concrets complets | Remplacer par des crochets ou par des descriptions de principe |
| EX-2 | convergence | important | Un seul exemple de « alternative écartée » : « la grande photo d'entrée suivie de trois cartes de services » (`:38`) ; `SKILL.md:204-211` exige cette rubrique à chaque run | Remplacer par un crochet ; sinon tous les runs écartent la même alternative |
| EX-3 | structure | important | Quatre exemples sur cinq montrent une clôture (`STATE: CLOSED`, `:25, 73, 117`) ; la trace légère par défaut n'est montrée qu'une fois | Rendre visible le chemin par défaut en premier |
| EX-4 | langue | important | 104 codes (77 pour 1000 mots) ; `SIMULATED` non défini | Définir ou retirer |
| EX-5 | répétition | mineur | Huit avertissements | Un seul |
| EX-6 | obsolète | mineur | `:71` date du 2026-10-09 | Mettre un crochet ou une date relative |
| EX-7 | design | mineur | Aucun exemple ne montre ce qu'est un bon résultat visuel (les exemples décrivent des traces, pas des pages) | À assumer : charte §5 interdit des exemples visuels recopiables |
| EX-8 | structure | mineur | Formats de trace différents d'un exemple à l'autre, assumés (`:3`) | Garder la variation, la dire une seule fois |

## C5. Ce qui fige ou pousse à la convergence

- **Concept complet « cartographie sonore »** : `THESIS: la ville se découvre par couches d'écoute`, `FIRST-OBJECT: topographie sonore interactive`, `PARTI: l'écoute par couches porte la scène` (`:57-65`) et la demande « hero mémorable… sans page SaaS générique » (`:53`). Le titre de l'exemple annonce « première scène identitaire » : le nom de l'exemple lui-même est un parti pris que l'agent peut reprendre.
- **Réponse visible modèle** (`:38`) : « J'ai construit une page d'accueil organisée autour de [...] ; j'ai écarté la grande photo d'entrée suivie de trois cartes de services, que n'importe quel atelier aurait. » Le crochet protège l'objet, pas la structure de phrase ni l'alternative écartée.
- **Ligne `MODAL, TRAME ET PARTI`** (`:45`) : « photo pleine largeur, titre centré, trois cartes… trame héros → services → avis → contact » : décrit la trame d'un atelier, que l'agent pourrait prendre comme trame type.
- **Cas `DIGITAL_MEMORY`** : « traitement pixel/raster », « archive numérique avec fragments, métadonnées et états réels », « densité haute… motion basse… variance modérée » (`:86-96`) : réglages complets.
- **Domaine de l'exemple** : atelier de réparation de vélos (`:32`). Le contrôle `FAC-01` interdit « boulangerie » (`validate_structure.py:746-747`) : signe qu'un domaine d'exemple a déjà été recopié.
- **Dates** : `2026-10-09` (`:71`).
- **Mitigation existante** : `:3` (« Reprendre la séquence, pas le style, les valeurs, les composants ») et `:34` (« l'exemple ne fournit volontairement ni thèse ni objet de preuve, pour qu'ils ne soient pas recopiés ») : le principe est bon mais n'est appliqué qu'à un exemple.

## C6. Savoir à protéger
- Avertissement : exemples non canoniques, reprendre la séquence : `:3`
- Trace ≠ sérialisation ; chemin vers `RUN_CARD` (exemple JSON, `machine_projection.md`, validateur) : `:5`
- Deux niveaux de trace et leur marqueur : `:7`
- Chemin LITE : classer, intention, modifier, vérifier, clôturer ; LITE n'ouvre ni atlas ni style : `:9-28`
- Chemin brief flou : build dans le même tour, hypothèses, trois demandes, réponse en quatre rubriques, trace de six lignes : `:30-49`
- Réserve : cinq champs (owner, scope, impact, prochaine preuve, revue/condition de sortie) : `:71`
- « Une belle capture ne prouve pas l'usage ; une rationale ne prouve pas l'implémentation » : `:76`
- Libellé narratif `CREATIVE-REVIEW` vs champ `creative_close` : `:78`
- Profil de style : refus possible si aucune décision ne change ; `PROFILE-DECISION` n'est ni score ni verdict : `:80-99`
- SYSTÈME : `ABANDONED`/`RETURN` et « le blast radius n'est pas un score » : `:101-120`
- Forme `DECISION-CHANGE: <issue> — … (observation : …)` : `:23, 68, 96, 114`

## C7. Dépendances et risques de déplacement
- **Cité par** `SKILL.md:220`, `QUICKSTART.md:291` ; manifeste.
- **Cite** `machine_projection.md`, `schemas/run_card.example.json`, `scripts/validate_run_card.py`.
- **Contrôles** (lus dans le code, pas seulement les comptes de `mesures.json`) : `FAC-01` (titre exact « ## DIRECTION — fabrication depuis un brief flou », texte « Trace (trace légère », mot `PROCHAINE PREUVE`, absence de « boulangerie », `validate_structure.py:737-747`) ; `LCF-11` (forme des lignes `DECISION-CHANGE:`), `LCF-12` (bloc `RESERVATION:` complet), `LCF-13` (pas de `NOT-OBSERVED:` ; `STATE: CLOSED` exige `VERDICT:`), `LCF-14` (lignes `EVIDENCE:` avec « capture »), `LCF-45` (présence de `MODAL:`), `validate_reading_map.py:391` (l'en-tête doit citer `schemas/run_card.example.json`, `machine_projection.md`, `validate_run_card.py`). `mesures.json` compte 13 phrases pour `validate_all.py` ; à vérifier : la lecture directe ne trouve aucun contrôle nominatif dans ce script.
- **Risque** : renommer le titre du brief flou ou le format des lignes `DECISION-CHANGE:` casse ces contrôles. Remplacer le concept « cartographie sonore » par des crochets reste compatible avec `LCF-11/12/13` tant que les lignes gardent leur forme.

## C8. Synthèse (partie C)
Fichier de gouvernance présenté comme aide générale. Un seul exemple (brief flou) montre le chemin par défaut, et c'est le seul protégé contre la copie. Les trois exemples de clôture portent des concepts ou des réglages complets qu'un agent peut recopier. Les verrous portent sur la forme des lignes, pas sur le contenu des cas, donc le contenu peut changer.

---

# D. references/flow.md

## D1. Identité
Vue de lecture du chemin de décision : un diagramme Mermaid, une phrase qui le répète, trois paragraphes de rappel. Public réel : personne identifiable (l'agent a déjà la table de `SKILL.md:33-39` ; l'humain n'y arrive que par `QUICKSTART.md:291`). Public visé : agent et équipe. 2 086 caractères, 26 lignes, 19 codes pour 1000 mots (6), phrases moyenne 21,4, p90 37, 9 % au-delà de 40 mots, non vérifié : 2.

## D2. Verdicts

| Critère | Verdict | Preuve |
|---|---|---|
| F1 | à corriger (mineur) | La première phrase dit ce que le fichier n'est pas : « une vue de lecture, pas une route supplémentaire » (`flow.md:3`), pas à quoi il sert. |
| F2 | à corriger | Mélange agent (`python3 scripts/read_route.py --connexions`, `:26`) et humain (« si une personne le demande », `:24`). |
| F3 | conforme | un H1, quatre blocs. |
| F4 | à corriger | `:20` redit le diagramme ; `:22` redit `SKILL.md:27` ; `:24` répète `READING_MAP.md:9` (4 fenêtres de 14 mots, `mesures.md`) ; `:26` redit `SKILL.md:31`. |
| F5 | à corriger (mineur) | Libellés de nœuds : `NOT-VERIFIED`, « Protection de niveau », « Owner et prochaine preuve » (`:14, 13, 17`). |
| F8 | conforme | 2 086 caractères. |
| F9 | conforme | 2 mentions. |
| F10 | conforme | aucun relevé. |
| F11 | conforme | rien. |

## D3. Qualité du schéma (Mermaid, `flow.md:5-18`)

**Ce qui est bien** : un équivalent écrit existe (`:20`) ; la syntaxe a l'air valide (`flowchart LR`, flèches pleines et pointillées) ; l'intitulé dit que le schéma n'est pas une route. À vérifier : rendu réel, que je n'ai pas pu obtenir ici.

**Ce qui pose problème (constats vérifiables sur le texte)** :
1. **Valeur ajoutée faible.** Le schéma est une chaîne de sept verbes qui reprend mot pour mot la phrase de `:20` (« classer et protéger… »). Charte §3 principe 8 : « Un schéma n'existe que s'il explique mieux que le texte ». Seules les quatre flèches latérales (`:13-17`) apportent quelque chose, et elles sont mal expliquées.
2. **Ce que le schéma n'affiche pas, alors que c'est le cœur du système** : le **choix du mode** (cinq chemins), la **construction dans le même tour**, la **première proposition qui vaut checkpoint** (le mot « checkpoint » n'apparaît que dans le texte, en parenthèse), la bifurcation **trace légère / trace complète**. Le nœud `G` « Proposer ou fermer » met sur un même plan deux issues opposées.
3. **La gouvernance occupe six nœuds sur dix** (« Protéger », « Vérifier et corriger », « Proposer ou fermer », « Protection de niveau », `NOT-VERIFIED`, « Owner et prochaine preuve ») ; le design en occupe trois (« Cultiver et diriger », « Composer et construire », « Polir et observer »). La charte demande l'inverse comme centre de gravité.
4. **Les trois arêtes en pointillé disent trois choses différentes** (escalade `A→H`, absence de preuve `F→I`, retour créatif `E→C`) sans style distinct, sans légende.
5. **Le retour créatif `E → C`** (`:15`) saute à « Cultiver et diriger ». Or le tableau de diagnostic de la seconde boucle (`SKILL.md:171-178`) distingue six issues : défaut local (retour à l'artefact), défaut de craft (geste), direction faible (rouvrir), risque changé (reclasser), preuve insuffisante, décision établie. Le schéma n'en montre que deux.
6. **Chemin mort** : `I --> J` (`:17`) n'a pas de suite ; `G` n'a pas de sortie. Aucun nœud de fin.
7. **Lisibilité** : sept nœuds en ligne (`LR`) dans une page mobile : réduction probable à une taille illisible (à vérifier en rendu). Aucun `classDef`, aucun thème ni couleur, pas de `accTitle`/`accDescr` : le schéma n'applique aucune identité visuelle (grille S12 : « carte v3 externe ; un diagramme Mermaid » comme valeur de départ) et dépend du thème de l'afficheur en clair et en sombre.
8. **Équivalent écrit trop dense** : une phrase de 1 100 caractères avec parenthèse emboîtée (`:20`) ; 9 % des phrases dépassent 40 mots.

**Verdict sur le schéma** : à corriger (important pour S12, mineur pour l'usage agent). Il faut décider s'il doit survivre : s'il reste, il doit montrer les deux bifurcations qui structurent le système (mode, niveau de trace) et la première proposition.

## D4. Sections

| Section (ligne) | Apport | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Introduction (3) | Statut du schéma | méta | ? | Dit ce qu'il n'est pas | réécrire (forme) |
| Diagramme (5-18) | Chaîne de 7 étapes + 3 exceptions | gouvernance/méta | ? | Voir D3 | réécrire (forme) ou retirer si le schéma refait en phase 5 explique mieux |
| Texte équivalent (20) | Les mêmes étapes en une phrase | méta | agent | Phrase unique, 1 100 caractères | garder l'équivalent (exigé par la charte) ; réécrire (forme) |
| Règle de chargement (22) | Charger `DIRECTION/START` avant d'agir | gouvernance | agent | Redit `SKILL.md:27` | retirer (doublon) |
| Combinaisons (24) | Renvoi à READING_MAP | méta | humain | Répète `READING_MAP.md:9` | retirer (doublon) ou fusionner |
| Connexions (26) | Renvoi à `--connexions` | méta | agent | Répète `SKILL.md:31` | retirer (doublon) |

## D5. Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| FL-1 | visuel | important | Voir D3.1-8 | Décider : refaire ou retirer |
| FL-2 | répétition | mineur | `:22, 24, 26` | Fusionner dans `SKILL.md` |
| FL-3 | structure | mineur | Personne n'est dirigé vers ce fichier ; `SKILL.md:221` le décrit « la vue courte du chemin » | Soit le brancher à une porte, soit le retirer |
| FL-4 | langue | mineur | Libellés avec codes (`:14, 17`) | Libellés en langue claire |

## D6. Savoir à protéger
- Chemin en sept moments : classer, protéger, cultiver/diriger, composer/construire, polir/observer, vérifier/corriger, proposer ou fermer : `:7-12, 20`
- Risque critique ramène au classement : `:13, 16, 20`
- Preuve absente reste `NOT-VERIFIED` avec owner et prochaine preuve : `:14, 17, 20`
- Défaut créatif ramène à la direction : `:15`
- La première proposition vaut checkpoint (trace légère) ; décider et fermer (trace complète) : `:20`
- Boucle créative élève, boucle de gouvernance protège : `:20`
- Charger les routes approfondies seulement si elles changent quelque chose : `:22`
- `READING_MAP` : combinaisons par résultat ; connexions situées par `--connexions` : `:24-26`

## D7. Ce qui fige
aucun relevé.

## D8. Dépendances
Cité par `SKILL.md:221`, `QUICKSTART.md:291`, manifeste. `mesures.json` compte des phrases de `flow.md` dans `validate_structure.py` (2), `validate_reading_map.py` (1), `test_audit_regressions.py` (1) ; **à vérifier** : la lecture directe ne montre aucun contrôle nominatif sur `flow.md`. Les contrôles généraux parcourent `skills/**/*.md` (`validate_structure.py:383`). Un schéma redessiné ne casse donc probablement rien, mais il faut relancer `validate_all.py` pour le confirmer.

## D9. Synthèse (partie D)
Petit fichier dont le schéma n'explique pas mieux que le texte, met la gouvernance au centre, ne montre ni mode ni première proposition, et n'applique aucune identité visuelle. Le texte autour redit trois passages ailleurs. À refaire ou à retirer en phase 5, pas à garder tel quel.

---

# E. references/machine_projection.md

## E1. Identité
Projection structurée d'une `RUN_CARD` en YAML, avec règles de cohérence : transport entre agents, scripts et handoffs. Public réel : l'agent qui sérialise une clôture et les scripts de validation. Public visé : agent et équipe (module de gouvernance). 7 262 caractères, 129 lignes, un seul H1 sans sous-titre, bloc YAML de 3 607 caractères, 51 codes (59 pour 1000 mots), phrases moyenne 15,4, p90 32, 3 % au-delà de 40 mots, non vérifié : 5, vestiges : 0.

## E2. Verdicts

| Critère | Verdict | Preuve |
|---|---|---|
| F1 | conforme | `machine_projection.md:3` dit à quoi sert la projection et qu'elle ne crée pas de contrat concurrent. |
| F2 | conforme (équipe/agent) | Contenu technique cohérent avec le public. |
| F3 | à corriger (mineur) | Un seul H1, aucun H2 : un bloc de 3,6k de YAML suivi de cinq paragraphes denses (`:120-128`) de 500 à 1 000 caractères chacun. |
| F4 | à corriger (important) | (a) Le YAML recopie `schemas/run_card.example.json` (144 lignes), qui en est la version contrôlée ; (b) `:128` est repris de `README.md:200` (29 fenêtres de 14 mots, `mesures.md`) et de `RELEASE_NOTES.md:141` ; (c) la liste de valeurs interdites (`:126`) est aussi en `ACTION.md:399` ; (d) les séparations `STATE/ISSUE/VERDICT/GATE/AXIS/DECISION-CHANGE` (`:120`) répètent `canonical_minimum.md:11-15`. |
| F5 | conforme (public technique) | Codes et clés propres au sujet. |
| F8 | conforme | 7 262 caractères, chargé seulement pour un run persistant. |
| F9 | à corriger (mineur) | Quatre mises en garde « ne prouve pas » (`:122, 124, 126, 128`), dont deux déjà dites en `README.md:200` et `ACTION.md` (frontière de validation). |
| F10 | à corriger (mineur) | Valeurs de remplissage : `id: DIRECTION-PREMIUM-001` (`:14`), `owner: design-owner`, dates `2026-08-29`, `2026-09-12`. |
| F11 | à corriger (mineur) | Dates d'exemple passées (`:16, 49, 74, 106, 109`) avec `date_version: "2026-08-29 / V1"`, antérieures à la révision courante. |

## E3. Sections

| Section (ligne) | Apport | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Introduction (3-10) | Rôle et liste des fichiers de schéma | gouvernance | agent | Bien placée ; renvoie au schéma et au validateur | garder |
| Bloc YAML (12-118) | Forme de référence en lecture | gouvernance | agent/équipe | Doublon de `schemas/run_card.example.json` | **décision à prendre** : garder le YAML pour la lecture et générer la version JSON depuis lui (ou l'inverse) ; un seul lieu |
| Distinctions et valeurs admises (120) | Sépare `STATE`, `ISSUE`, `VERDICT`, etc. ; valeurs de `closure.verdict` et `closure.axes` ; règle sur `null` | gouvernance | agent | Verrouillé par `LCF-26`, `LCF-41` | garder |
| Clôture et preuves (122) | `CLOSED` = persistance ; provenance obligatoire ; `creative_close` ; `profile_decision` | gouvernance | agent | Dense : 1 000 caractères en un paragraphe | réécrire (forme) |
| Risque critique (124) | `critical_protection` structuré | gouvernance | agent | Une phrase de 1 000 caractères | réécrire (forme) |
| Interdits et validation (126-128) | Valeurs jamais introduites ; limite de ce qu'atteste le validateur | gouvernance/méta | agent | Redit `ACTION.md:399` et `README.md:200` | fusionner avec `ACTION/RUN_CARD` (un seul lieu) |

## E4. Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| MP-1 | répétition | important | YAML ≈ `schemas/run_card.example.json` | Un seul lieu, l'autre dérivé ; **attention** : validé par script, ne pas casser |
| MP-2 | répétition | important | `:128` ↔ `README.md:200` ↔ `RELEASE_NOTES.md:141` (29 + 2 fenêtres) | Garder en `ACTION/RUN_CARD`, renvoyer ailleurs |
| MP-3 | répétition | mineur | `:126` ↔ `ACTION.md:399` | idem |
| MP-4 | obsolète | mineur | dates 2026-08-29 et 2026-09-12 | Dates relatives ou crochets |
| MP-5 | convergence | mineur | `DIRECTION-PREMIUM-001` : le mot « premium » contredit `SKILL.md:19` (« jamais l'imitation… d'une esthétique premium ») | Id neutre |
| MP-6 | structure | mineur | Aucun H2 | Découper en sous-titres pour qu'une section se comprenne seule |
| MP-7 | coût de lecture | mineur | Paragraphes de 700 à 1 000 caractères, `:122, 124` | Couper en listes |

## E5. Savoir à protéger
- Rôle : transport, pas de contrat concurrent, `ACTION.md` fait foi : `:3`
- Fichiers de schéma, exemple, fixtures, validateur : `:5-10`
- Forme complète d'une `run_card` (id, owner, mode, risque, sources, direction, anchors, artifact, capability_profile, proof, decision_change, creative_close, profile_decision, closure, b1b) : `:12-118`
- Séparation des états, valeurs de `verdict` (six) et d'`axes` (cinq), `NOT-OBSERVED` jamais sur un axe, `null` seulement où le schéma l'admet : `:120`
- `CLOSED` = persistance ; provenance obligatoire pour `ACCEPTED*` ; `creative_close` obligatoire en `DIRECTION` clôturée ; `profile_decision` : cinq champs : `:122`
- `critical_protection` : objet structuré, `result`, `FAIL-ASSUMED` dans `closure.exception`, cohérence des locators : `:124`
- Valeurs interdites (`SELF-DECLARED`, `ATLAS-PASS`, `POLISHED`, `SLOP-FREE`, score esthétique) : `:126`
- Ce qu'atteste une `RUN_CARD` validée : `:128`

## E6. Ce qui fige
Valeurs de remplissage : `DIRECTION-PREMIUM-001`, `design-owner`, `2026-08-29 / V1`, `ACCEPTED-WITH-RESERVATION`, `HELD` (`:14, 15, 16, 94-95`). Risque faible pour le visuel (aucune valeur de design) mais un id et des dates seront copiés tels quels. Peu d'enjeu pour la convergence de design.

## E7. Dépendances et risques de déplacement
- **Cité par** `SKILL.md:222`, `examples.md:5`, `QUICKSTART.md:291`, manifeste ; son contenu est répété par `README.md:200`.
- **Cite** `ACTION.md` (`ACTION/RUN_CARD`), `schemas/run_card.schema.json`, `schemas/run_card.example.json`, `scripts/validate_run_card.py`.
- **Contrôles** : `LCF-26` (la ligne `closure.axes` et la ligne `profile_decision … champs`, `validate_reading_map.py:341-343`) ; `LCF-41` (« schéma l'admet » et « champ facultatif sans valeur est omis », `:478`) ; `test_audit_regressions.py` (3 phrases, selon `mesures.json`). Déplacer le paragraphe `:120-122` sans conserver ces phrases fait échouer ces contrôles.

## E8. Synthèse (partie E)
Fichier utile mais strictement de gouvernance, doublé par un JSON contrôlé et par trois énoncés de limite répétés ailleurs. Le fond est à garder entier ; la forme (un seul lieu pour l'exemple, des sous-titres, des paragraphes plus courts, des valeurs d'exemple neutres) est à reprendre. Le risque de déplacement est réel : deux contrôles (`LCF-26`, `LCF-41`) lisent ses phrases.

---

# F. Synthèse commune (SKILL.md + references/)

1. **SKILL.md** : savoir de design riche (58 %), mais 43 000 caractères lus à tout run, avec le routage (6,6k) en position 2 et les premières lignes de composition à 38 %. Le fond est à protéger ; ce qui change, c'est l'ordre et la tranche. Une réorganisation passe par `NOYAU` dans `build_core.py`, ses trente verrous et le plafond de 46 000 octets.
2. **Le plus gros bloc, `COMP-VOCABULAIRE` (7 859)**, est lu en entier pour n'en utiliser qu'une ligne ; décision à prendre entre noyau et route à la demande. Le savoir vit déjà dans SAVOIR.
3. **examples.md** : 4 exemples sur 5 montrent une clôture, un seul le chemin par défaut ; les concepts concrets (cartographie sonore, mémoire numérique, alternative écartée « trois cartes ») risquent d'être recopiés ; `SIMULATED` n'est défini nulle part.
4. **flow.md** : le schéma Mermaid n'explique pas mieux que le texte, ne montre ni modes ni première proposition, met la gouvernance au centre, sans identité visuelle ni légende ; à refaire ou retirer.
5. **canonical_minimum.md** et **machine_projection.md** : sains sur le fond ; doublons à fusionner (règle « sources absentes » ×4 ; YAML ≈ JSON ; limite de validation ×3). `machine_projection.md` est verrouillé par `LCF-26`/`LCF-41`.
