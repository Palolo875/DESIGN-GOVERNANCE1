# Fiche — guides, portes d'entrée et historique (8 fichiers)

Commit audité : `9681d4e`. Lecture seule ; les huit fichiers ont été lus en entier. Les lignes de `CHANGELOG.md` et de `ORCHESTRATION_MAP.md` sont celles du fichier lui-même. Les mesures viennent de `mesures.md` ; les répétitions ont été relocalisées par un recoupement de fenêtres de 14 mots (mêmes lignes que `mesures.md`).

Fichiers : `README.md` (A), `RELEASE_NOTES.md` (B), `V1/official/README.md` (C), `V1/official/QUICKSTART.md` (D), `V1/official/GLOSSAIRE.md` (E), `V1/official/READING_MAP.md` (F), `V1/official/ORCHESTRATION_MAP.md` (G), `V1/official/CHANGELOG.md` (H).

---

## 0. Vue transversale

### 0.1 Les portes d'entrée, évaluées par public

| Public | Porte actuelle | « Comprend-il en cinq minutes quoi faire ? » | Verdict |
|---|---|---|---|
| **Débutant** | `README.md` section « Commencer » (A:9-23) : 2 262 caractères, 342 mots, aucun code entre apostrophes inverses, quatre questions Que demander / fournir / recevoir / poursuivre. | Il comprend quoi décrire, quoi apporter, ce qu'il recevra, comment corriger (A:14-20). Il ne sait pas **où** taper sa demande ni comment l'agent est mis en place : l'installation est dans la zone technique (A:56-64), après Fiche de version, Mission et tableau des lecteurs. Et il lit d'abord un paragraphe de jargon (A:3 : « mode `DIRECTION` », « lecteur », « carte des sujets », nom de révision), 1 067 caractères avant « Commencer ». | à corriger |
| **Designer** | Aucune porte propre. A:52 le renvoie à `QUICKSTART.md`, qui est un guide de pilotage de run (modes, ligne de run, `RUN_CARD`). Le seul index par sujet est la carte des sujets de F (F:40-67), écrite en codes de route (236 codes/1000 mots), pensée pour `read_route.py --trouver`. | Non. Il ne trouve pas « le savoir parcourable par sujet, utilisable sans agent » que demande la charte. | à corriger (S1) |
| **Équipe** | Aucune porte propre. A:53 : « Reviewer ou lead » vers `READING_MAP.md` puis `ACTION.md` ; A:54 : mainteneur vers `CHANGELOG.md`. Rien en langage clair sur qui décide, ce qui est vérifié, ce qui reste ouvert (les pièces sont dans D:180-195, D:265-279, éparses). | Non. | à corriger (S1) |
| **Agent** | `SKILL.md` via A:51, C:5. Une ligne, claire. D:7 invite aussi « l'agent » à lire le guide, alors que `SKILL.md:224` dit qu'il ne l'ouvre que si une personne le demande. | Oui pour l'entrée ; deux discours sur le rôle du guide. | conforme (incohérence mineure) |

Autres constats sur les portes : `V1/official/README.md` (C) est une seconde porte qui renvoie vers la première (C:5) ; le README du dépôt est doublé d'un **README Local fabriqué dans un script** (`scripts/build_distributions.sh:98-150`, avec l'entrée et la constitution reprises par balises) : trois textes d'accueil à tenir ensemble.

### 0.2 Répétitions entre ces fichiers

| Paire | Fenêtres (mesures) | Lignes | Nature | Proposition |
|---|---:|---|---|---|
| A ↔ D | 27 | A:204 ↔ D:259, D:279 | « Une capture prouve un rendu… » et « slop procédural » dits trois fois dans ces deux fichiers, plus A:206-208 | Un seul propriétaire (à vérifier : ACTION) ; les guides renvoient |
| A ↔ `machine_projection.md` | 29 | A:200 ↔ MP:128 ; aussi B:141 | « Une `RUN_CARD` validée atteste la forme… ; la liste exacte vit en un seul lieu » : la phrase qui dit « un seul lieu » est copiée dans A:200, B:141, MP:128 et en variante C:21, D:246 | Un seul énoncé (frontière d'`ACTION/RUN_CARD`) ; liens ailleurs |
| B ↔ H | 14 | B:1-5 ↔ H:3-8 ; B:13, 23, 33 ↔ H:32-38 ; B:129 ↔ H:88 | En-tête de statut ; formule de compatibilité (« V1.0.0, 69 fichiers GitHub et 63 Local ; aucun nouveau mode, gate, statut ni champ RUN_CARD ») ; limites | Voir B et H : la répétition est surtout de fond (mêmes révisions racontées deux fois, hors fenêtres) |
| A ↔ H | 10 | A:5 ↔ H:12 ; A:73 ↔ H:19 ; A:198 ↔ H:88 ; A:208 ↔ H:90 | Définition du cadre, ancre graduée, limites du validateur | Idem |
| A ↔ C | 9 | A:45 ↔ C:21 ; aussi A:21-22 ↔ C:5 | Phrase `RUN_CARD`/trace ; « pour commencer » | Fusionner C dans A ou D |
| A ↔ B ↔ H | 6 | A:198, B:129, H:88 | « Ces contrôles ne remplacent ni observation, ni test utilisateur, ni accessibilité, ni performance, ni adoption » : cinq formulations (A:198, B:129, C:21, D:259, H:88) | Dire une fois par sujet (F9) |
| D ↔ H | 1 | D:29 ↔ H:17 | Trace légère / complète | Négligeable |

Répétitions de fond que les fenêtres ne voient pas :
- **Le même parcours « classer → charger → construire → observer → persister »** est reformulé en A:66, B:111-114, D:79 et D:193, E:86-89, F:13-18 (et `flow.md`). Sept fois.
- **L'histoire des révisions** : `RELEASE_NOTES.md` (B:7-77, 13 100 caractères) et `CHANGELOG.md` (H:32-48, 10 800 caractères) racontent les mêmes six révisions (accès, corrections, second audit, audit interne, mobilisation, activation), à deux niveaux de détail ; A:3 en donne un troisième résumé.
- **La description du cadre** : A:5, A:12, A:39-45, B:81-92 (Présentation, Points clés), H:12-28, C:3, D:3-9 : sept présentations de ce qu'est le système.
- **Le statut expérimental** : A:7, B:3, H:4, D:3, C:3.
- **Trois formats « ligne de run » et deux « handoff »** : D:16, D:68, D:202-209 (champs différents) ; D:185-190 (opérateur vers agent) et F:265-278 (agent vers suivant).

### 0.3 Vestiges et historique de travail livrés avec le produit

| Où | Vestige | Preuve |
|---|---|---|
| A:3 | Nom de révision de travail en tête de la page d'accueil, avec renvoi à un historique « tenu hors distribution » | `R2026-10-08-ACCES-MATIERE` ; « protections des révisions précédentes » |
| B entier | Quatre révisions racontées avec identifiants d'audit internes (`F01–F06`, `F07–F10`, `R01–R04`, `LCF-51…56`), nom de mesure `U5`, « paris P1 et P3 » | B:9, B:27, B:31, B:43, B:51 |
| B:77, H:56, A:3 | Le produit affirme que l'historique n'est pas livré, tout en livrant ses résumés | B:77 « tenu hors distribution » contre B:7-77 |
| H:32-48 | Chaque décision se termine par « Retour : restaurer `<révision>` depuis l'historique » alors que l'historique n'est pas livré : consigne inexécutable pour un lecteur de la distribution | H:32, 34, 36, 40, 42, 44, 48 ; H:56 |
| F:109 | « Base de sources : `R2026-10-08-ACCES-MATIERE` » | F:109 (verrouillé par `read_route.py:152,215`) |
| G entier | Fichier-pointeur, « ne porte plus de contenu propre » | G:3 |
| C:19 | Mention d'un fichier qui « n'est plus qu'un pointeur » | C:19 |
| A:94 | « désormais » : mention d'un état passé | mesures (vestiges A : 3) |
| H:10-28 | Titre « Version initiale… (2026-10-01) » qui contient en fait la description courante du produit | H:10 |
| B:17, 25, 37 | Titres positionnels « Révision précédente » : faux à la révision suivante | B:17, 25, 37 |

---

# Partie A — `README.md` (racine)

## Identité
Rôle actuel : page d'accueil du dépôt, qui cumule entrée humaine, fiche de version, présentation de la méthode, installation, structure du dépôt, procédures de distribution et de reprise, commandes de validation et limites. Public réel : débutant (A:9-23), opérateur, mainteneur. Public visé par la charte : débutant en premier ; les autres par portes distinctes. Taille : 21 970 caractères, 3 141 mots, 10 sections de niveau 2 + 2 de niveau 3, 65 codes (21/1000 mots), phrases moyenne 19 / p90 32 / 2 % > 40 mots, 5 « non vérifié », 3 vestiges. Plus grosse section : « Source de vérité et distributions » (3 870). L'entrée « Commencer » pèse 2 281 caractères, soit 10 % du fichier.

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | Au moins six rôles ; les premières lignes (A:3, A:5, A:7) sont une révision, une définition et un statut, pas l'entrée |
| F2 Public | à corriger | Tout est dans un seul fichier : A:9-23 pour le débutant, A:171-200 pour le mainteneur |
| F3 Structure | à corriger | Titres de niveau 2 clairs, mais l'ordre mêle entrée et maintenance : « Fiche de version » (A:25) et « Mission » (A:39) précèdent l'accès aux lecteurs (A:47) |
| F4 Une seule fois | à corriger | Voir 0.2 : A↔D 27, A↔MP 29, A↔H 10, A↔C 9 ; limites dites en A:7, 30, 32, 142, 146, 173, 175, 198, 200, 202-208 |
| F5 Langue | à corriger | Entrée A:9-23 : conforme (0 code). Hors entrée : `RUN_CARD`, `DIRECTION/CHARGE`, `NOT-VERIFIED`, `DOMAIN_FRAME`… (A:45, A:51, A:177) sans définition à la première apparition |
| F8 Longueur | à corriger | Entrée 2 262 car. (cible S3 : environ 6 000, atteinte) ; le fichier entier 21 970 pour une « porte » |
| F9 Limites | à corriger | Voir F4 : cinq endroits pour la même limite des validateurs |
| F10 Exemples | conforme (mineur) | Aucune valeur de couleur ni police. A:20 « trop froid pour une boulangerie » : exemple de retour, domaine déjà évité dans `examples.md` (`validate_structure.py:746`) ; à vérifier |
| F11 Vestiges | à corriger | A:3 révision de travail ; « désormais » (A:94) |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition proposée |
|---|---|---|---|---|---|
| Titre + révision + statut (1-7) | Nom, révision, avertissement d'expérimentation | méta | tous | Le jargon (A:3) précède l'entrée ; le statut est utile et court | réécrire (forme) : titre et deux lignes de promesse en langage clair ; déplacer la révision vers l'état de version (B) ; garder le statut (A:7) |
| Commencer (9-23) | Les quatre questions pour la personne sans expérience | design (usage) | débutant | Très bon cœur, verrouillé (`ENT-01`) ; manque « où écrire / comment démarrer » ; lien final vers 4 documents d'un coup | garder ; compléter la forme (une phrase sur la mise en place) ; placer en première position |
| Fiche de version (25-37) | État de la version, NOT-VERIFIED, rappel des cartes | méta | équipe, mainteneur | Mélange état et pédagogie ; A:35-37 décrit la carte de lecture dans un tableau d'état | déplacer vers l'état de version (B ou H) ; A:35-37 vers la porte de F |
| Mission (39-45) | Mission et vocabulaire d'ambition ; liste des contrats | méta / gouvernance | designer, équipe | Cinquième présentation du cadre ; A:45 énumère cinq contrats en codes | fusionner avec l'entrée (une phrase) ; contrats déplacés vers une porte équipe |
| Pour les agents et les opérateurs (47-54) | Tableau des portes par lecteur | méta | tous | Bon principe, mais quatre lecteurs qui ne sont pas les quatre publics de la charte | réécrire (forme) : un tableau par public |
| Installer la skill (56-64) | Trois étapes d'installation, prérequis Python | gouvernance (opérations) | agent, opérateur | Indispensable au débutant mais enterré | déplacer vers la porte « mise en place » ; le débutant y est renvoyé depuis l'entrée |
| Mode choisi par l'agent + parcours (66-68) | Le mode n'est jamais demandé à la personne ; parcours complet | gouvernance | agent | Une des sept formulations du parcours | fusionner avec D:75-91 ; garder une phrase |
| Constitution minimale (70-76) | Les cinq absolus résumés, piège de conformité | gouvernance | équipe, agent | Seule copie autorisée (`CST-01`, balises) | garder (déplacement exige de changer `validate_structure.py:285,313` et `build_distributions.sh:163`) |
| Modèle à double boucle (78-98) | Boucle de création / de gouvernance ; boucle d'édition ; finesse ; traduction BIBLIOTHEQUE | design + gouvernance | designer | De la méthode de design dans l'accueil ; A:94, A:96 sont des annonces de capacité (« désormais ») | déplacer vers le savoir de design (à décider par la phase 2) ; retirer les phrases d'annonce |
| Structure du dépôt (100-121) | Quatre couches, cinq sources, commandes du lecteur | méta | mainteneur, designer | A:121 est un paragraphe de 1 050 caractères qui contient les trois commandes du lecteur et `--strict` | déplacer vers un document mainteneur / de lecteur ; garder le tableau des sources dans C |
| Source de vérité et distributions (123-146) | Construction des archives, options, budget | gouvernance | mainteneur | Aucun intérêt pour les autres publics ; verrouillé (`preparer_livraison.py` 8 phrases, test 8) | déplacer vers un document mainteneur |
| Reprendre une préparation interrompue (148-154) | Procédure sûre de reprise (verrou, sauvegardes) | gouvernance | mainteneur | 2 155 caractères de procédure ; renvoyée par `build_distributions.sh:16` | déplacer vers un document mainteneur ; mettre à jour le message du script |
| Validation (171-200) | Prérequis, commandes, limites des validateurs | gouvernance | mainteneur | A:198-200 doublonnent B:141, MP:128 | déplacer ; réduire les limites à un renvoi |
| Limites et discipline d'usage (202-208) | Limites d'une capture, slop procédural, qualité créative située | méta | tous | Le texte utile de F9 ; A:206-208 bien écrit | garder une fois, ici ou dans B (une seule place) |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| A1 | structure | important | A:3-7 avant A:9 ; entrée à 10 % du fichier | Mettre l'entrée en tête ; reléguer le reste |
| A2 | convergence (portes) | important | A:47-54 ne donne ni porte designer ni porte équipe | Quatre portes (voir 0.1) |
| A3 | coût de lecture | important | 21 970 car. pour une page d'accueil ; A:121 (1 050 car. d'un bloc) | Scinder en entrée + document mainteneur |
| A4 | langue | important | A:45 : `DOMAIN_FRAME`, `RESEARCH_BRIEF`, `CREATIVE_DIRECTION_SET`, `UI_UX_REALITY_PACK`, `EVALUATION_CASE` | Sortir de la page d'accueil |
| A5 | répétition | important | Voir 0.2 | Un propriétaire par énoncé |
| A6 | obsolète | important | A:3 « L'historique… hors distribution » et nom de révision | Retirer de l'accueil |
| A7 | risque | mineur | Le README Local est écrit dans `build_distributions.sh:98-150` : deux sources d'accueil | Décider d'une seule source en phase 5 |
| A8 | langue | mineur | A:7 « ne promet ni beauté automatique… » : honnête mais en tête, avant l'invitation | Le garder court après l'entrée |
| A9 | visuel | mineur | Aucun repère visuel (pas de schéma, pas d'identité) | Phase 8 de la charte, non traitée ici |

## Savoir à protéger
- Les quatre questions et leur contenu, dont « au plus trois questions », « construit quand même une première proposition », « accord avant toute action irréversible ou coûteuse » : A:12-20.
- Statut expérimental et non-promesse : A:7.
- Installation de la skill, prérequis, vérification, « sans accès au paquet l'agent n'a que le noyau » : A:58-64.
- Le mode est choisi par l'agent, jamais demandé : A:66.
- Cinq absolus, piège de conformité : A:73-75.
- Boucle d'édition, finesse (bord éclairé, alignement optique, chiffres stables), traduction intention vers levier, « ni catalogue ni garantie » : A:80-98.
- Quatre couches du dépôt, cinq sources et leurs décisions : A:102-119.
- Commandes du lecteur et mises en garde (`--trouver`, `--sommaire`, `--guides`, « l'absence de résultat ne prouve pas… ») : A:121.
- Distribution : source de vérité, `preparer_livraison.py`, options `--markdown`, `--empreintes`, `--log`/`--journal`, `--require-browser`, budget SKILL en octets UTF-8 : A:125-146.
- Reprise d'une préparation interrompue (verrou, `owner.txt`, ordre des actions, « aucune purge selon l'âge ») : A:150-154.
- Archives produites et règle « modifier les sources, pas les archives » : A:162-169.
- Prérequis Python 3.10, Playwright/Chromium, Bash/zip, Node pour DOM simulés : A:173-175.
- Tableau des commandes de validation et leur portée : A:179-188.
- Limites des validateurs, de la capture, du slop procédural, de la qualité créative située : A:198-208.

## Ce qui fige ou pousse à la convergence
Aucun relevé de valeur. Seul point : l'exemple de retour A:20 (« trop froid pour une boulangerie »), mineur et lu par des humains.

## Dépendances et risques de déplacement
- Cité par : C:5 et D:7 (lien `../../README.md#commencer`), E:84, `SKILL.md` (accès humain, `SKILL.md:224`), `FAC-01` (titre `## Commencer` obligatoire, `validate_structure.py:751-753`).
- Verrous : 56 phrases verrouillées, dont `validate_all.py` 19, `preparer_livraison.py` 8, `test_preparer_livraison.py` 8, `validate_structure.py` 9, `validate_reading_map.py` 3, `validate_design_governance.py` 3. Balises `entree:`/`constitution:` (`ENT-01`, `CST-01`) ; tests sur les quatre questions, l'absence de mode demandé, le vouvoiement, une seule mention de « retenir cette direction pour ».
- `build_distributions.sh:155-170` extrait les deux blocs balisés pour fabriquer le README Local ; `build_distributions.sh:16` renvoie à la section « Reprendre une préparation interrompue ».
- Déplacer les sections de maintenance casse : les verrous de `preparer_livraison.py`, de `validate_all.py`, et le message d'erreur du script de build. Déplacer l'entrée ou la constitution sans toucher aux balises casse `ENT-01`, `CST-01` et le README Local.

## Synthèse
Le cœur « Commencer » est bon (2,3 k caractères, sans code) et doit rester la porte du débutant, mais il est précédé de jargon et suivi de 19 k caractères de maintenance. La page cumule six rôles ; elle gagne à être scindée en entrée courte et document mainteneur. Il manque les portes designer et équipe, et la mise en place concrète. La constitution minimale et les balises sont verrouillées : elles se déplacent avec leurs contrôles.

---

# Partie B — `RELEASE_NOTES.md`

## Identité
Rôle actuel : notes de la version et de quatre révisions, plus un résumé du produit, une liste de contrôles et les limites. Public réel : mainteneur, relecteur (GitHub uniquement : le fichier n'existe pas dans l'export Local, `package_manifest.json`). Public visé par la charte : équipe, après la mise de l'historique hors des portes. Taille : 18 111 car., 2 606 mots, 11 sections de niveau 2 + 1 de niveau 3, 67 codes (26/1000), 8 « non vérifié », 7 vestiges. Plus grosse section : « Révision précédente R2026-10-04-AUDIT-FIXES » (8 034).

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | B:1-5 annonce des notes de version ; B:79-158 est un second README (Présentation, Contenu, Parcours, Contrôles) |
| F2 Public | à corriger | Aucun public déclaré ; contenu pour mainteneur |
| F3 Structure | à corriger | B:45 se termine par « : » puis un paragraphe, pas une liste ; B:59 « Contrôles et capacités conservés » (niveau 3) contient les révisions MOBILISATION et ACTIVATION (B:47-75) sans titre propre |
| F4 Une seule fois | à corriger | B↔H 14 fenêtres ; B:79-92 ↔ H:12-28 ; B:96-103 ↔ A:100-107 ; B:119-150 ↔ A:171-200 |
| F5 Langue | à corriger | `LCF-55`, `LCF-56`, `F07–F10`, `R01–R04`, `RETURN`, `U5`, `P1`/`P3` sans définition (B:9, 27, 31, 43, 51) |
| F8 Longueur | à corriger | 66 % du fichier (12 100 car.) est l'histoire des révisions B:17-77 ; la « section de référence » B:37-77 fait 8 034 car. |
| F9 Limites | à corriger | 8 mentions ; B:152-158 est le bon endroit, B:15, 23, 35, 61, 63, 77, 129, 137 répètent |
| F10 Exemples | conforme | Aucune valeur recopiable |
| F11 Vestiges | à corriger (le plus lourd du lot) | Le fichier est quasi entièrement un état passé : B:17, 25, 37, noms de révision, `U5`, nombre de fichiers par distribution (B:23, 33) |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition proposée |
|---|---|---|---|---|---|
| En-tête (1-5) | Statut, date, usage | méta | équipe | Doublon de H:3-8 ; le `\` final de B:4 est un saut de ligne mal écrit | fusionner avec H (source de version) ; corriger la forme |
| Révision R2026-10-08-ACCES-MATIERE (7-15) | Ce que la révision courante change pour l'utilisateur | méta | équipe | Seule section réellement « notes de version » ; lisible (1 121 car.) | garder (réécrire en langage clair) |
| Révision précédente CORRECTIONS (17-23) | Corrections avant mesure ; renommages `SAVOIR/JUGEMENT-COURT`, `BIBLIOTHEQUE/AVANT-SELECTION` | méta | mainteneur | Double H:34 | déplacer vers l'historique ; conserver les renommages dans H (migration) |
| Révision précédente AUDIT2-FIXES (25-35) | Contraste, objet de preuve, profil strict, restauration | méta | mainteneur | Double H:36-40 ; contient les clés JSON `contrast_coverage`, `proof_observations` (B:33) | déplacer vers l'historique ; conserver la compatibilité JSON dans H |
| Révision précédente AUDIT-FIXES (37-77) | Six constats F01-F06, mobilisation, activation, compatibilité `creative_direction_set` | méta | mainteneur | Regroupe au moins trois révisions ; B:59 mal titré ; B:65 contient la seule note sur l'ancien validateur et `maxItems: 3` | déplacer vers l'historique ; protéger B:65 (compatibilité) |
| Présentation (79-83) | Description du système et de la trace | méta | débutant | Doublon A:12, H:12 | retirer (déjà dit) |
| Points clés (85-94) | Six idées du produit | méta | équipe | Doublon H:16-22 | retirer après vérification de correspondance |
| Contenu (96-103) | Table des dossiers | méta | mainteneur | Doublon A:100-107 ; B:100 mentionne `ORCHESTRATION_MAP.md` pointeur | retirer |
| Parcours (105-117) | Trois parcours (personne, agent, opérateur) | méta | tous | Doublon A:66, D:193 | retirer |
| Contrôles inclus (119-137) | Ce que le package contrôle, configuration CI | gouvernance | mainteneur | B:137 : seule description de la CI (Ubuntu, Python 3.11, Playwright 1.56.0) | déplacer vers le document mainteneur |
| Ce que le validateur atteste (139-150) | Ce que `RUN_CARD` validée atteste ou non | gouvernance | équipe | Verrouillé (`FAC-01`) ; doublon A:200, MP:128 | garder le titre ; ramener à un renvoi |
| Limites déclarées (152-158) | Efficacité, convergence, taille et coût, plateformes, champs libres | méta | équipe | Seule source de B:155-158 ; verrouillée (`FAC-01`) | garder (c'est la vraie fonction du fichier) |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| B1 | obsolète | important | B:17-77 | Séparer l'historique du produit livré ; garder la révision courante |
| B2 | répétition | important | B:7-77 ↔ H:32-48 ; B:79-150 ↔ A, H | Un seul récit par révision |
| B3 | contradiction interne | important | B:77 « L'historique… est tenu hors distribution » contre B:7-77 | Aligner le discours avec ce qui est livré |
| B4 | structure | important | B:45 phrase finissant par « : » ; B:59 niveau 3 portant plusieurs révisions | Reconstruire un titre par révision |
| B5 | langue | important | Identifiants d'audit non définis (B:27, 31, 43, 51) | Retirer des textes pour humains |
| B6 | obsolète | mineur | Titres « précédente » (B:17, 25, 37) ; « 69 fichiers GitHub et 63 Local » (B:23, 33) à comparer à `package_manifest.json` (69 et 63 : exact aujourd'hui) | Titres datés ; chiffres calculés ou supprimés |
| B7 | visuel | mineur | B:3-5 sauts de ligne par `\` et deux espaces | Corriger |

## Savoir à protéger
- Notes de la révision courante : B:9-15 (typographie chargée d'office, routes tranchées, `--sommaire`, `BIBLIOTHEQUE/SEQUENCE`, retrait de P1/P3, efficacité NOT-VERIFIED).
- Renommages `ACTION/FAST-PATH`, `SAVOIR/JUGEMENT-COURT`, `BIBLIOTHEQUE/AVANT-SELECTION`, refus d'une carte stricte sans capture B1b : B:19-23.
- Profil strict (familles `example.com/.org/.net`, `.invalid`), restauration Markdown (refus de chemins non canoniques, collisions) : B:29.
- Clés de sortie `contrast_coverage`, `proof_observations`, `keyboard_coverage` et leur tolérance côté consommateurs : B:33, B:41.
- Six parcours simulés, « ni aveugle ni étude utilisateur » : B:61.
- Compatibilité `creative_direction_set` (retrait de `maxItems: 3`, ancien validateur à mettre à jour) : B:65.
- Verrou et sauvegardes jamais effacés selon l'âge : B:31, B:69.
- CI livrée distincte de son exécution (`NOT-VERIFIED`) : B:35, B:137.
- Limites : efficacité, convergence, taille et coût, plateformes (macOS/Windows non observés), champs libres sans filtre de placeholders : B:154-158.

## Ce qui fige ou pousse à la convergence
Aucun relevé.

## Dépendances et risques de déplacement
- Présent seulement dans la distribution GitHub (`package_manifest.json`) ; `validate_design_governance.py:94-97` ignore son absence en Local.
- Verrous : 14 phrases (dont `validate_structure.py` 6, `preparer_livraison.py` 2, `read_route.py` 2). `FAC-01` exige `**Efficacité : \`NOT-VERIFIED\`.**`, « Aucune mesure comparative » et le titre `## Ce que le validateur atteste` (`validate_structure.py:762-765`) ; `LCF-21`, `LCF-27` (`validate_reading_map.py:668,674`) ; contrôle de titre de version (`validate_design_governance.py:94`).
- Cité par : H n'y renvoie pas ; A:3 y renvoie pour les limites.
- Mentionné dans `build_distributions.sh:53` (copie GitHub seulement).

## Synthèse
Un tiers du fichier seulement est de la note de version ; deux tiers sont de l'historique de travail avec des identifiants internes, et un tiers est un second README. L'historique doit rester conservé (traçabilité), mais plus dans la porte du produit. Les limites B:152-158 sont le contenu à garder. Les verrous `FAC-01` imposent de garder deux titres/phrases.

---

# Partie C — `V1/official/README.md`

## Identité
Rôle actuel : index du dossier des sources : liste les cinq sources normatives et déclare les guides non normatifs. Public réel : lecteur qui ouvre le dossier. Public visé : équipe et agent, après fusion. Taille : 2 054 car., 282 mots, 1 section de niveau 2, 23 codes (82/1000), 0 vestige, 0 « non vérifié ».

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | conforme | C:3-5 : dossier des sources officielles |
| F2 Public | à corriger | C:5 renvoie le débutant vers A, l'opérateur vers D, l'agent vers la skill : trois publics en un paragraphe |
| F3 Structure | conforme | Un titre de section clair (C:7) |
| F4 Une seule fois | à corriger | A↔C 9 fenêtres (A:45 ↔ C:21) ; tableau C:11-17 = A:111-117 ; C:19 = A:119 |
| F5 Langue | à corriger | `RUN_CARD`, `DESIGN-ATLAS` non définis (C:19, 21) |
| F8 Longueur | conforme | 2 054 car. |
| F9 Limites | conforme | Une seule phrase (C:21) |
| F10 Exemples | conforme | Aucun |
| F11 Vestiges | à corriger | C:19 « `ORCHESTRATION_MAP.md` n'est plus qu'un pointeur » |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Introduction (1-5) | Définition du dossier et trois renvois | méta | tous | Renvoi circulaire vers A | fusionner avec A (porte) |
| Sources normatives (7-21) | Tableau des cinq sources, statut non normatif des guides, `DESIGN-ATLAS` appartient à `SAVOIR.md`, carte dérivée | méta | équipe, agent | Même tableau qu'en A:109-119 ; C:19 est la seule déclaration complète de ce qui est (non) normatif | garder la déclaration normatif/non normatif en un seul lieu (A ou H) ; retirer le doublon |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| C1 | répétition | important | C:11-19 ↔ A:111-119 ; H:14 ; H:50 : quatre listes des cinq sources | Un seul tableau |
| C2 | obsolète | mineur | C:19 | Retirer la mention du pointeur avec G |
| C3 | convergence (portes) | mineur | C:5 est une seconde porte | Supprimer la porte |

## Savoir à protéger
- Les cinq sources et leur responsabilité : C:9-17.
- Guides d'entrée non normatifs, aucune route/gate/statut/score/autorité créés : C:19.
- `DESIGN-ATLAS` appartient à `SAVOIR.md` : C:19.
- READING_MAP dérivée et non normative : C:19.
- Une validation confirme seulement les contrôles exécutés : C:21.

## Ce qui fige ou pousse à la convergence
Aucun relevé.

## Dépendances et risques de déplacement
- Verrous : 8 phrases (`validate_structure.py` 2, `validate_design_governance.py` 2, `read_route.py` 2, `validate_reading_map.py` 1, `build_core.py` 1). `FAC-01` exige le lien vers « Commencer » (`validate_structure.py:748-750`). Titre vérifié (`validate_design_governance.py:94`). Réécrit par `build_distributions.sh:186` pour le chemin Local.
- Cité par : `package_manifest.json`, `read_route.py` (`--guides`). Déplacer demande de mettre à jour le manifeste, le README Local et les verrous.

## Synthèse
Petit fichier utile à peu près comme index de dossier ; sa seule contribution propre est la phrase qui dit ce qui est normatif ou non (C:19). Candidat à la fusion dans l'entrée ou dans un en-tête de dossier, après report de cette phrase.

---

# Partie D — `V1/official/QUICKSTART.md`

## Identité
Rôle actuel (D:5) : « interface d'activation rapide » du pilote de run, qui résume modes, ligne de run, parcours, handoff, exemple, clôture. Public réel : opérateur ou agent qui connaît déjà le système ; D:7 le dit. Public visé par la charte : équipe (module de gouvernance) et, pour la partie lecture de routes, agent. Taille : 26 035 car., 3 707 mots, 14 sections de niveau 2 + 3 de niveau 3, 136 codes (37/1000), phrases moyenne 18,4 / p90 31 / 5 % > 40, 1 « non vérifié », 0 vestige. Plus grosse section : « 3. Le parcours complet » (4 019). Lecture : 18 minutes environ.

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | D:5 « n'ajoute aucune règle » mais le guide en reformule plusieurs sous forme d'impératifs : D:71, D:136, D:142, D:195 |
| F2 Public | à corriger | D:7 : « opérateur, designer ou agent » ; contenu pour qui connaît déjà `DIRECTION/START` et la `RUN_CARD` |
| F3 Structure | à corriger | « Parcours commun » (D:11) et « Carte de résolution » (D:31) non numérotés, puis 1 à 12 ; D:132-134 trois lignes orphelines ; D:138 section de 401 car. |
| F4 Une seule fois | à corriger | A↔D 27 ; D↔`DIRECTION.md` 6 (D:47) ; trois formats de ligne de run (D:16, 68, 202-209) ; parcours (D:79) = A:66, E:86-89, F:13-18 |
| F5 Langue | à corriger | 136 codes ; `MODE — DECISION — RISK — NEXT-PROOF — OWNER` (D:16) dès la deuxième page ; D:47 : `MODAL`/`PARTI`, `FABRICATION`, `CFT`, `TENSION` en un paragraphe de 1 000 car. |
| F8 Longueur | à corriger | 26 k pour un « quickstart » ; D:41-47 : 2 629 car. dans « Façade d'activation » |
| F9 Limites | conforme | Un seul « non vérifié » ; mais limites rappelées en D:9, 71, 111, 246, 259, 277 |
| F10 Exemples | à corriger | D:197-244 exemple `home-042` : thèse, modal et parti concrets |
| F11 Vestiges | conforme | Aucun nom de révision |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Intro + rôle + pour qui (1-9) | Ce qu'est le package, avertissement | méta | opérateur | Quatrième présentation du cadre ; D:7 renvoie le débutant à A | réécrire (forme) : une phrase de rôle |
| Parcours commun (11-29) | Ligne de run et cinq questions, une suite parmi six | gouvernance | opérateur | Une des trois lignes de run ; D:29 mêle trace légère et complète | garder (cœur du guide) ; unifier avec D:61-73 |
| Carte de résolution rapide (31-35) | Renvoi à F, deux formes de sortie, trace légère en six lignes | méta | opérateur | Mélange renvoi et règle de trace (D:35) | fusionner avec D:11-29 |
| 1. Choisir la profondeur de lecture (37-59) | Façade, bénéfice attendu par source, Creative Boot, prise de brief, constitution | gouvernance + design | opérateur | D:47 : un paragraphe de 1 000 car. qui résume Creative Boot et prise de brief ; doublon DIRECTION (D↔DIRECTION 6 fenêtres) | réécrire (forme) ; renvoyer vers DIRECTION |
| 2. La ligne de run (61-73) | Ligne de run avec `ID` et `STATE` ; `DECISION-INTENT` ; ne jamais prétendre avoir vérifié | gouvernance | opérateur | Seconde ligne de run ; D:71 règle de véracité utile | fusionner avec D:11-29 ; protéger D:71-73 |
| 3. Le parcours complet (75-111) | Parcours, deux boucles, charger une route, `--trouver`, mode strict | gouvernance + méta | opérateur, agent | D:102 : un paragraphe de 1 160 car. sur le lecteur ; double A:121 | déplacer le lecteur vers le document mainteneur / de lecteur ; garder le parcours |
| 4. Choisir le mode (113-136) | Ordre canonique des cinq modes, table situation / mode, mode = hypothèse | gouvernance | opérateur | L'ordre canonique (D:117-121) ne suit pas l'ordre de la table (D:123-130) ; D:132-134 orphelines | réécrire (forme) |
| 5. Charger seulement ce qui peut changer (138-142) | `DIRECTION/CHARGE` unique | gouvernance | agent | 401 car., redit D:47, F | fusionner avec 4 |
| 6. Qualité positive dès le premier rendu (144-163) | Huit dimensions du premier rendu avec « retour si… » | design + produit | designer | Contenu de design (présence, foyer, signature, intégration, résolution, désirabilité, vérité, résilience), projection de `DIRECTION/FIRST-OBJECT` (D:146) | garder, déplacer vers la porte designer (à décider) ; savoir à protéger |
| 7. One-shot (165-178) | Compression sans dispense, six conservations | gouvernance | opérateur | Aucun code ; clair | garder |
| 8. Handoff agentique (180-195) | Modèle de brief à l'agent (six champs) ; confirmation avant action externe | gouvernance | opérateur, équipe | Bon contenu pour la porte équipe | garder ; déplacer vers la porte équipe |
| 9. Exemple complet minimal (197-246) | Exemple de ligne de run et de `RUN_CARD` `DIRECTION` | gouvernance | opérateur | Exemple à valeurs concrètes (voir « fige ») | réécrire (forme) : exemple neutre ou retirer |
| 10. Observer, interpréter et améliorer (248-263) | Quatre questions de preuve ; polish ≠ gradients/ombres | produit + design | designer, équipe | D:259 doublon A:204 | garder une fois ; doublon retiré |
| 11. Persister et fermer (265-279) | Cinq vérifications avant fermeture ; CLOSED ≠ réussi ; slop procédural | gouvernance | équipe | D:277 un paragraphe de 560 car. ; D:279 doublon A:204 | garder ; réduire |
| 12. Sources propriétaires (281-291) | Table des cinq sources + références de la skill | méta | tous | Quatrième liste des cinq sources | fusionner avec la liste unique |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| D1 | coût de lecture | important | 26 035 car., 18 min ; pas de chemin court pour un débutant | Couper en guide équipe (court) + référence |
| D2 | langue | important | 136 codes ; D:16, 47, 102 | Introduire chaque terme à sa place ; sortir `read_route` |
| D3 | convergence (formats) | important | Trois lignes de run D:16, 68, 202-209 | Un seul format |
| D4 | répétition | important | A↔D 27 ; D:79 / A:66 / E:86 / F:13 | Un propriétaire |
| D5 | structure | mineur | Numérotation incohérente (D:11, 31 non numérotées, D:37 « 1. ») ; orphelines D:132-134 | Remettre en ordre |
| D6 | risque (rôle) | important | D:5 « n'ajoute aucune règle » contre D:71, 136, 142, 195 qui prescrivent | Renvoyer vers les propriétaires ou assumer la règle |
| D7 | convergence | important | D:216-221 (voir ci-dessous) | Exemple neutre |
| D8 | incohérence | mineur | D:7 invite l'agent ; `SKILL.md:224` dit le contraire | Aligner |
| D9 | langue | mineur | D:9, D:43-45 : « lorsque la décision visuelle est ouverte et que les capacités sont disponibles… » (phrases longues, p90 31) | Phrases courtes |

## Savoir à protéger
- Les cinq questions de cadrage et la suite parmi six : D:19-29.
- Deux formes de sortie ; niveau de trace indépendant du mode ; `N/A-JUSTIFIED` : D:35.
- Rôle des cinq sources dans la façade d'activation ; « si aucun gain ne peut modifier la décision, chemin court » ; risque critique ≠ chemin court : D:43-45.
- Creative Boot et prise de brief (au plus trois intrants, première proposition construite dans le même tour) : D:47.
- Déclencheurs de `DOMAIN-FRAME`, `SAVOIR/SOURCE`, contrat de réalité UI/UX : D:49.
- Constitution et table « Pour… faites d'abord… » : D:53-59.
- Règle de véracité : ne jamais prétendre avoir construit/observé ce qui ne l'était pas ; capacité manquante limite le claim, pas la protection ; package V1 indisponible : proposition hypothétique : D:71-73.
- Parcours complet, deux boucles, rationale ≠ correction, note d'invalidation d'hypothèse : D:77-90.
- Lecteur de routes (`--trouver`, `--sommaire`, `--complet`, `--guides`, blocs « (noyau) ») et mode strict : D:94-111.
- Ordre canonique des modes, table situation/mode, « le mode est une hypothèse de routage » : D:115-136.
- `DIRECTION/CHARGE` unique ; « non chargé par défaut » n'interdit rien : D:140-142.
- Les huit dimensions du premier rendu avec leur « retour si… », « jamais un style, une palette, un score » : D:146-163.
- One-shot : six éléments non supprimés, sortie selon le niveau de trace : D:167-178.
- Brief agentique à six champs et confirmation avant action externe/irréversible : D:182-195.
- Exemple de sérialisation `RUN_CARD` `DIRECTION` (`sources`, `direction`, `anchors`, `artifact`, `trace_locator`, `proof`, `next_proof`, `capability_profile`, `closure`, `direction_status`, `creative_close` à cinq champs) : D:246.
- Quatre questions de preuve ; capture ≠ tâche utilisateur ; polish ≠ gradients : D:250-263.
- Cinq contrôles avant fermeture ; `CLOSED` ≠ réussi ; conditions de fermeture par issue ; slop procédural : D:269-279.

## Ce qui fige ou pousse à la convergence
- D:197-244, exemple `home-042` : `Modal : titre centré, sous-titre, deux boutons, trois cartes de bénéfices` (D:218) ; `Thèse : la preuve du produit porte la première scène` (D:216) ; `Parti : … la preuve remplace le titre` (D:219) ; viewports `desktop 1440, mobile 390` (D:206) ; `OWNER: design-lead` (D:208). Une page d'accueil dont la thèse et le parti sont déjà écrits est un gabarit que l'agent peut recopier. B:21 dit qu'une révision a retiré un tel objet de l'exemple de brief flou : cette réserve n'a pas été appliquée ici. Atténuant : `SKILL.md:224` dit que l'agent n'ouvre pas ce guide d'office.
- Les trois formats de ligne de run (D:16, 68, 202) : un agent copie le premier rencontré.
- D:127 « craft exigeant : Gate C ciblé » : règle courte, pas une valeur.

## Dépendances et risques de déplacement
- Cité par : A:22, A:52, C:5, F:14, `SKILL.md:224`.
- Verrous : 39 phrases (`validate_structure.py` 14, `validate_all.py` 10, `validate_reading_map.py` 7, `read_route.py` 3, `test_read_route.py` 2, `test_audit_regressions.py` 1, `test_preparer_livraison.py` 1, `build_core.py` 1). `FAC-01` : lien vers « Commencer » obligatoire. Titre `V1.0.0` vérifié (`validate_design_governance.py:94`). Réécriture de chemin dans `build_distributions.sh:186`. `test_read_route.py` ouvre `QUICKSTART.md` pour tester `--guides`.
- Découper D casse au moins 14 phrases verrouillées par `validate_structure.py` et 10 par `validate_all.py` : leurs places devront être déplacées avec elles.

## Synthèse
Un bon guide opérateur, mais trop long et trop codé pour être une entrée, et mal placé entre règles et guide. Les sections 6, 8, 10 et 11 sont des savoirs que les publics designer et équipe attendent. L'exemple de la section 9 donne une thèse et un parti à recopier. Le lecteur de routes (D:94-111) appartient à un document de lecteur ou de mainteneur.

---

# Partie E — `V1/official/GLOSSAIRE.md`

## Identité
Rôle actuel : définit 61 termes (mots du design et codes de gouvernance mêlés), six exemples et quatre étapes pour commencer. Public réel : opérateur et agent. Public visé : designer pour les mots du design, équipe pour les codes. Taille : 13 447 car., 1 895 mots, 2 sections de niveau 2, 82 codes (43/1000), 5 « non vérifié », 0 vestige, phrases moyenne 17,8.

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | E:3 « mots nécessaires pour commencer » ; le dernier bloc (E:82-93) est une procédure de run |
| F2 Public | à corriger | E:84 : « s'adresse à l'opérateur ou à l'agent » ; le débutant est écarté dès E:3-5 |
| F3 Structure | à corriger | Un tableau plat de 61 lignes sans ordre (ni alphabétique ni thématique) ; E:69-80 « Exemples express » séparés de leurs termes |
| F4 Une seule fois | à corriger | E:86-89 ↔ D:19-29, F:13-18 ; E:39-40 ↔ D:35 ; E:46-49 ↔ ACTION |
| F5 Langue | à corriger | 25 des 61 termes sont des codes (`MODAL`, `PARTI`, `FABRICATION`, `B1b`, `SPECCED`, `TRUTH/*`, `ANCHOR-*`) ; « handoff », « noyau », « checkpoint » utilisés mais sans ligne (E:40, 41, 42) |
| F8 Longueur | à corriger | 13 k pour un glossaire « pour commencer » |
| F9 Limites | conforme | Limites dans les définitions (E:21, 48, 62-64) |
| F10 Exemples | conforme (mineur) | E:75, E:78 (« 390 px », « deux CTA de même poids ») : exemples de définition, pas de modèle de design |
| F11 Vestiges | conforme | Aucun |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Intro (1-3) | Rôle non normatif | méta | tous | Court | garder |
| Tableau des termes (5-67) | 61 définitions | méta, design, gouvernance | tous | Lignes de design : Direction, DA, Craft, Polish, Créativité située, Goût situé, Spécificité, Thèse, Ancre, Slop (E:22-30, 49) ; lignes de gouvernance : Mode, Run, RUN_CARD, Owner, Scope, Gate, STATE, VERDICT… ; verrouillé ligne à ligne | scinder : mots du design (portail designer), codes de gouvernance (module équipe) ; garder le contrôle `check_glossary` |
| Exemples express (69-80) | Six exemples de termes | méta | opérateur | E:80 : un exemple de 600 car. pour `CLOSED` qui règle des verdicts | fusionner avec les définitions ; raccourcir E:80 |
| Pour commencer sans vocabulaire préalable (82-93) | Quatre étapes d'un run ; distinction direction / DA / craft / polish / spécificité ; clarifier le désaccord de mode | méta + gouvernance | opérateur | Ne correspond pas au titre du fichier ; doublon D, F | déplacer E:86-89 vers D ; E:91 vers le tableau (termes du design) ; garder E:93 |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| E1 | structure | important | Mélange design et gouvernance en un tableau plat | Deux tableaux |
| E2 | langue | important | 25/61 termes sont des codes ; débutant exclu (E:84) | Mots du design définis sans code |
| E3 | répétition | mineur | E:86-89 | Retirer |
| E4 | langue | mineur | « handoff », « noyau », « checkpoint », « consumer » non définis | Ajouter ou reformuler |
| E5 | risque | mineur | Chaque terme du vocabulaire de fabrication doit avoir sa ligne (`validate_structure.py:360,487`) : supprimer un terme sans toucher au contrôle casse la validation | Prévoir l'adaptation |
| E6 | incohérence | mineur | E:78 `CHANGED` ; D:237 `ABANDONED` : les deux valeurs existent (`run_card.schema.json:179`) | Aucune correction nécessaire |

## Savoir à protéger
- Définitions de décision, risque, preuve, mode (niveau de protection distinct du niveau de trace) : E:7-12.
- `FAST-PATH`, façade d'activation, source propriétaire, run, `RUN_CARD` (exigence selon trace et mode), artefact, owner, scope, limite : E:13-21.
- Direction, DA, craft, polish (geste conditionné, réinspecté, sans accumulation d'effets), créativité située, goût situé, spécificité, thèse : E:22-29.
- Ancre et ses trois voies, Creative Boot, `MODAL`, `PARTI`, `FABRICATION`, plafond, objet de preuve, défaut dominant : E:30-38.
- Trace légère (six lignes), trace complète (distincte de la forme courte LITE), première proposition, livraison, trame modale, profil de surface, vérité de scène, marquage de vérité : E:39-46.
- `B1b`, `FAIL-ASSUMED`, slop (dont procédural), premier objet, boucle d'amélioration : E:47-51.
- Gate A/B/C, axes V/U/A/T, `STATE`, `ISSUE`, `VERDICT` (six valeurs), statut de direction, `DECISION-INTENT`, `DECISION-CHANGE` (triade et valeurs de repli), `TRACE-LOCATOR`, `CLOSED`, `NOT-VERIFIED`, `NOT-OBSERVED`, `N/A-JUSTIFIED`, `SPECCED`, `READING_MAP`, locator : E:52-67.
- Six exemples, dont l'exemple complet de `CLOSED` (verdict, réserve complète, `FAIL` exclut tout verdict accepté) : E:75-80.
- Le distinguo direction / DA / craft / polish / spécificité et la règle « clarifier le périmètre plutôt que masquer le désaccord de mode » : E:91-93.

## Ce qui fige ou pousse à la convergence
Aucun relevé de valeur de design. Exemples de définition E:75-80 (390 px, deux CTA) : mineurs, à ne pas déplacer dans un fichier lu par l'agent sans les neutraliser.

## Dépendances et risques de déplacement
- Verrous : 16 phrases (`validate_reading_map.py` 5, `validate_run_card.py` 4, `validate_structure.py` 3, `test_audit_regressions.py` 2, `validate_design_governance.py` 2). `validate_structure.py:719-722` verrouille quatre lignes du tableau (Mode, Run, Trace légère, Livraison) ; `check_glossary` (`validate_structure.py:360,487`) exige qu'un terme du vocabulaire de fabrication y figure en première cellule de ligne de table.
- Cité par : A:119, C:5, C:19, `build_distributions.sh:127`.
- Scinder le fichier ou changer la première cellule d'une ligne casse `check_glossary` et ces quatre verrous.

## Synthèse
Contenu solide et verrouillé, mais c'est un référentiel d'opérateur plutôt qu'un glossaire pour commencer. Il mélange les mots que le designer doit connaître et les codes que seul le module de gouvernance utilise ; la scission est la décision principale. Les étapes finales (E:86-89) doublonnent D et F.

---

# Partie F — `V1/official/READING_MAP.md`

## Identité
Rôle actuel : carte dérivée de lecture et d'activation : démarrage, routage, sujets, combinaisons par résultat, connexions situées, perspectives, handoff, résolution des routes, locators. Public réel : agent (via `read_route.py`) et relecteur ; pas un humain. Public visé : agent et designer (par sujet), équipe (combinaisons). Taille : 29 625 car., 3 763 mots, 12 sections de niveau 2 + 11 de niveau 3, **336 codes (89/1000, le plus dense)**, phrases moyenne 16,1 / p90 24 / 0 % > 40, 2 « non vérifié », 1 vestige (F:109). Plus grosse section : « Connexions situées » (11 579).

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | F:7 « réduit la recomposition mentale » ; en fait cinq fonctions : navigation, savoir de situation (C01-C09), orchestration, annexes de lecture (handoff), table machine (locators) |
| F2 Public | à corriger | Aucun humain ne peut lire 222 codes de route (F:1-334) sans le lecteur |
| F3 Structure | à corriger | Treize sections de niveau 2 sans regroupement ; « Constitution minimale » (F:22-24, 236 car.) est un pointeur ; deux conditions d'arrêt (F:105, F:332) |
| F4 Une seule fois | à corriger | F:13-18 / A:66 / D:79 ; F:26-36 / D:123-130 ; F:105 / F:332 ; F:265-278 / `ACTION/HANDOFF` (copie déclarée en F:263) |
| F5 Langue | à corriger | 336 codes ; F:40-67 carte des sujets : chaque cellule est un code (`SAVOIR/CRAFT/CFT-03`) sans phrase |
| F8 Longueur | à corriger | 29 625 car. ; « Connexions situées » 11 579 ; mais chaque connexion est ouverte seule (≈ 1 000 car.) : conforme à la règle « se comprend ouverte seule » |
| F9 Limites | conforme | Un seul « non vérifié » ; limites par connexion (« Moyens et limites ») |
| F10 Exemples | conforme | Aucune valeur de design ; tables de routes |
| F11 Vestiges | à corriger | F:109 base de sources par nom de révision de travail |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Utilisation (5-9) | Rôle de la carte ; renvoi aux combinaisons | méta | agent | Court | garder |
| Chemin canonique de démarrage (11-20) | Six étapes de lecture | méta | agent | Sixième formulation du parcours | fusionner avec D:75-91 |
| Constitution minimale (22-24) | Pointeur vers A et `DIRECTION.md` | méta | tous | Pointeur de 236 car. (autorisé par `CST-01`) | retirer ou garder en une ligne |
| **Carte des sujets** (40-67 ; avec « Routage minimal par décision » 26-38) | Pour 21 sujets, la route propriétaire et les renvois | méta (navigation) | designer, agent | Contrôlée par `SUJ-01` ; lue par `read_route --trouver` ; sans phrase explicative | garder ; ajouter un libellé humain par ligne ; candidate à la porte designer |
| Routage minimal par décision (26-38) | Pour sept décisions, première lecture et ajouts | méta (navigation) | agent, opérateur | Recoupe D:123-130 (décision vs situation) | fusionner avec la carte des sujets ou D |
| **Combinaisons par résultat recherché** (69-105) | Neuf résultats × noyau × renforts × preuve ; principe « composer la contribution, pas charger le maximum » ; garde-fous | gouvernance (orchestration) | équipe, agent | Ancien contenu de G ; une seule section autorisée (`MAP-01`) ; F:105 redit F:332 | garder ; mettre dans le module équipe ; fusionner F:105 et F:332 |
| **Connexions situées** (107-241) | Neuf entrées C01-C09, chacune avec condition, sources, intervention, contre-indication, moyens, observation | design + produit + gouvernance | agent, designer | De fait du **savoir d'intervention** (C04 récupération après erreur, C08 raccords image/texte, C02 typographie, C03 asset) ; déclaré « dérivé » ; le contenu exact n'est pas toujours retrouvé dans les propriétaires (à vérifier : ex. F:153 « Un crop… ne corrige pas un sujet inadéquat », non trouvé par recherche littérale dans les quatre sources) | garder ; vérifier chaque entrée contre ses propriétaires avant tout déplacement ; candidate au savoir de design |
| Activation multi-perspective (243-259) | Onze perspectives, déclencheur, lecture, sortie, non-chargement | gouvernance | agent | Troisième table d'orientation (avec F:26 et F:69) ; non citée dans F:5-9 | garder ; reclasser sous « équipe/agent » ; à fusionner avec les combinaisons (à décider) |
| Handoff minimal commun (261-281) | Treize champs du handoff, `N/A-JUSTIFIED` | gouvernance | agent | Copie déclarée de `ACTION/HANDOFF` (F:263) | retirer la copie, garder un renvoi (à vérifier : `ACTION/HANDOFF` porte les treize champs) |
| Résolution des routes (283-296) | Préfixe → propriétaire ; `RUN_CARD` n'est pas une route | méta | agent | Verrouillé par `read_route.py` | garder |
| Locators principaux (298-330) | Raccourcis et sous-locators (25 lignes) ; trois étapes de résolution | méta (table machine) | agent, outil | 78 codes ; lue par `read_route.py` comme étape 1 de résolution | garder tel quel ; déplacer vers un fichier de données si la phase 5 le décide |
| Condition d'arrêt (332-334) | Quand arrêter la lecture | méta | agent | Doublon F:105 | fusionner avec F:105 |

### Les trois cartes, distinguées
| Carte | Ce qu'elle répond | Lignes | Mode d'usage | Famille |
|---|---|---|---|---|
| **Carte des sujets** | « Où est le sujet X ? » : un mot de métier donne une route propriétaire | F:40-67 (et routage F:26-38) | `read_route.py --trouver` l'affiche en tête ; contrôle `SUJ-01` | navigation (méta) |
| **Connexions** | « Dans cette situation, quelles contributions rapprocher et que faire ? » | F:107-241 | `read_route.py --connexions [Cxx]` ; refuse un index périmé (`read_route.py:215`) | savoir d'intervention |
| **Combinaisons** | « Pour ce résultat, quelles capacités composer et quelle preuve ? » | F:69-105 (et F:243-259) | Lue à la main ; renvoi depuis `flow.md:24` et A:37 | orchestration (gouvernance) |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| F-1 | langue | important | 336 codes ; F:40-67 cellules en codes seuls | Libellé humain par sujet |
| F-2 | risque | important | Savoir d'intervention (C01-C09) déclaré dérivé : un déplacement ou une fusion peut le perdre | Table de correspondance entrée par entrée |
| F-3 | convergence | mineur | F:11-20 / F:26-36 / D:123-130 / E:86-89 : quatre routages | Un seul |
| F-4 | répétition | mineur | F:105 / F:332 ; F:265-278 / `ACTION/HANDOFF` | Fusion, renvoi |
| F-5 | obsolète | important | F:109 : « Base de sources : `R2026-10-08-ACCES-MATIERE` », verrou `read_route.py:152,215` | Remplacer par une version calculée, sans nom de révision de travail |
| F-6 | structure | mineur | F:243-259 et F:69-105 : deux tables d'orientation voisines | Les rapprocher |
| F-7 | structure | mineur | F:22-24 pointeur ; titre du fichier long | Retirer le pointeur |
| F-8 | risque | important | Absente des portes : F:5-9 et A:35-37 la décrivent ; aucune porte designer ne l'indique | Voir 0.1 |

## Savoir à protéger
- Chemin canonique et « `DIRECTION/START` reste la seule classification » : F:13-20.
- Routage minimal par décision dominante (sept lignes) : F:28-36 ; sortie par défaut : F:38.
- Carte des sujets (21 sujets) et règle « elle ne crée ni route ni autorité » : F:42-67.
- Principe « ne pas charger le maximum de routes ; composer le maximum de contribution pertinente » ; neuf résultats recherchés et leurs combinaisons et preuves : F:71-89.
- Variation créative (un axe situé à la fois, `CFT-02`) : F:93-95.
- Garde-fous de la combinaison et arrêt de l'orchestration : F:99-105.
- Index des connexions et règle d'usage (condition établie / fausse / inconnue ; aucun quota) : F:109-115.
- **C01 à C09, chacune de ses six rubriques** : F:117-241 (C01 contexte incertain 117-129 ; C02 typographie 131-143 ; C03 asset 145-157 ; C04 récupération après erreur 159-171 ; C05 réemploi 173-185 ; C06 changement partagé 187-199 ; C07 ambition vers construction 201-213 ; C08 élément vers ensemble 215-227 ; C09 intention vers médium 229-241).
- Onze perspectives avec déclencheur, lecture minimale, sortie, non-chargement ; `N/A-JUSTIFIED` valide ; non-chargement ne rend jamais `N/A` un contrôle applicable : F:245-259.
- Treize champs du handoff : F:265-281.
- Préfixes de propriétaire et statut de `RUN_CARD` comme adaptateur machine : F:287-296.
- Trois étapes de résolution des locators et 25 raccourcis : F:300-330.
- Condition d'arrêt : F:334.

## Ce qui fige ou pousse à la convergence
Aucun relevé de valeur. Risque de lecture : les colonnes « Noyau possible » et « Renforcement » (F:79-87) peuvent être lues comme une liste à charger malgré F:73 ; l'ancre en est le principe écrit en F:73.

## Dépendances et risques de déplacement
- Verrous : 48 phrases (`validate_reading_map.py` 14, `test_read_route.py` 10, `validate_all.py` 8, `validate_structure.py` 8, `test_audit_regressions.py` 6, `read_route.py` 2). `SUJ-01` (carte des sujets), `MAP-01` (une seule section « Combinaisons par résultat recherché »), 9 connexions résolues et index daté de la révision (`read_route.py:152,215`). `read_route.py` lit la table des locators (F:304-330) comme étape 1 et la carte des sujets pour `--trouver`.
- Cité par : A:35-37, C:19, D:33, `SKILL.md:31,224`, `flow.md:24`, G:3.
- Déplacer F:107-241 ou F:298-330 casse `read_route.py --connexions`, la résolution des routes et les tests `test_read_route.py` ; renommer le titre « Combinaisons par résultat recherché » casse `MAP-01`, G:3 et A:37.

## Synthèse
Le fichier remplit trois cartes différentes sous un titre unique ; elles se distinguent bien (sujets, situations, résultats) et chacune a un verrou propre. Les connexions C01-C09 sont du savoir d'intervention déguisé en carte dérivée : à protéger entrée par entrée. Les locators sont une table machine. Aucun humain ne le lit tel quel ; la carte des sujets pourrait servir le designer avec des libellés.

---

# Partie G — `V1/official/ORCHESTRATION_MAP.md`

## Identité
Rôle actuel : fichier-pointeur vers la section « Combinaisons par résultat recherché » de F. Public réel : personne (compatibilité). Public visé : aucun. Taille : 367 car., 41 mots, 3 lignes, 3 vestiges.

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | conforme | G:3 dit ce qu'il est |
| F2 Public | à corriger | Aucun lecteur |
| F3 Structure | conforme | Un titre, un paragraphe |
| F4 Une seule fois | conforme | Ne répète rien, mais est cité trois fois ailleurs |
| F5 Langue | conforme | Un code |
| F8 Longueur | conforme | — |
| F9 Limites | conforme | — |
| F10 Exemples | conforme | — |
| F11 Vestiges | à corriger (fichier-pointeur) | G:3 « pointeur de compatibilité… ne porte plus de contenu propre » |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| Titre + statut (1-3) | Renvoi vers F:69 | méta | aucun | Le lien `READING_MAP.md#combinaisons-par-résultat-recherché` est le seul contenu | retirer (après décision sur `MAP-01`) |

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| G1 | obsolète | important | G:3 | Retirer le fichier ; adapter 6 endroits |
| G2 | risque | important | `MAP-01` (`validate_structure.py:336-345`) échoue si G porte du contenu ; `package_manifest.json:16,84`, `validate_reading_map.py:220` le déclarent | Modifier validateurs et manifeste dans le même lot |
| G3 | incohérence | mineur | G:1 le titre promet « combinaisons dérivées par résultat » | Sans objet si retiré |

## Savoir à protéger
Aucun savoir propre. Seul le renvoi : G:3.

## Ce qui fige ou pousse à la convergence
Aucun relevé.

## Dépendances et risques de déplacement
- Cité par : C:19, B:100, `package_manifest.json` (GitHub ligne 16, Local ligne 84), `validate_structure.py:341-345` (`MAP-01`), `validate_reading_map.py:220` (clé `OM`).
- Retirer G sans toucher à ces cinq endroits fait échouer `validate_structure.py`, `validate_reading_map.py` et le build. Les archives `Design_Governance_V1_*.zip` et `dist/` contiennent aussi G (copies générées).

## Synthèse
Fichier-pointeur sans savoir propre. Il se retire sans perte de fond, mais seulement avec le manifeste, `MAP-01`, `validate_reading_map.py`, C:19 et B:100.

---

# Partie H — `V1/official/CHANGELOG.md`

## Identité
Rôle actuel : cinquième source normative : version et révision, résumé du produit, décisions de révision, cycle de vie des routes, migration des alias, limites. Public réel : mainteneur. Public visé : équipe (module de gouvernance). Taille : 20 277 car., 2 859 mots, 5 sections de niveau 2, 128 codes (45/1000), 4 « non vérifié », 5 vestiges, phrases moyenne 18,2 / p90 30 / 4 % > 40. Plus grosse section : « Autorité et maintenance » (11 948, soit 59 % du fichier).

## Verdicts de la grille
| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | H:38 « version, cycle de vie, migration » : en fait quatre rôles (métadonnées de version, description du produit, règles de maintenance, journal de décisions) |
| F2 Public | conforme | Mainteneur ; mais H:36-48 écrit à la première personne de l'historique |
| F3 Structure | à corriger | Deux niveaux seulement (conforme) ; « Autorité et maintenance » (H:30) contient neuf paragraphes de décisions non titrés, deux sans date (H:44, 48) ; sous-titrage par gras en tête de paragraphe |
| F4 Une seule fois | à corriger | H↔B 14 ; H:14-28 ↔ B:85-92 ↔ A:12 ; H:50 ↔ A:109-119 ↔ C:9-17 |
| F5 Langue | à corriger | 128 codes ; H:32 contient `check_render`, `SAVOIR/CRAFT`, `SUJ-01` ; paragraphes jusqu'à 2 200 car. |
| F8 Longueur | à corriger | Un paragraphe de décision = 560 à 2 200 car. ; section de 11 948 car. en 13 paragraphes |
| F9 Limites | conforme | 4 mentions, sans excès |
| F10 Exemples | conforme | H:16 `[VEILLE 2026-09]` : marqueur de tendance datée, autorisé |
| F11 Vestiges | à corriger | H:6 révision ; H:32-48 « Retour : restaurer `<révision>` depuis l'historique » ; H:56 |

## Sections
| Section (ligne) | Apporte | Famille | Public | Observation | Disposition |
|---|---|---|---|---|---|
| En-tête (1-8) | Version, statut, date, **révision** | méta | tous, outils | `Version expérimentale` est la source unique de version (`validate_design_governance.py:85`) ; **Révision** est lue par `read_route.py:215` | garder (règle normative : source de version) |
| V1.0.0 — Version initiale (10-28) | Description du produit en 14 puces + budget de 46 000 octets + préparation | méta / gouvernance | équipe | Titre faux : c'est la description courante (ex. H:24 budget, H:26 `preparer_livraison.py`) ; doublon B:85-92, A:12-20 | scinder : règles de maintenance (H:24 budget, H:23 contrôles) restent normatives ; description du produit déplacée vers la porte équipe |
| Autorité et maintenance (30-56) | Treize paragraphes | mixte | mainteneur | Voir « Normatif et historique » ci-dessous | scinder |
| Cycle de vie des routes (58-70) | Cinq statuts, transitions, règle de dépréciation | gouvernance | mainteneur | Pur normatif ; table verrouillée en partie | garder |
| Migration des anciens aliases (72-84) | Cinq alias vers leur reclassification | gouvernance | mainteneur | Normatif de compatibilité | garder |
| Limites de la version (86-90) | Une validation confirme seulement les contrôles exécutés ; la version reste expérimentale | méta | tous | Quatrième énoncé de cette limite (A:198, B:129, C:21) | garder une fois (propriétaire de la version) |

### Dans « Autorité et maintenance » : normatif contre historique
| Lignes | Contenu | Nature | Preuve |
|---|---|---|---|
| H:32 | Décision de la révision d'accès et de matière (2026-10-08) | **historique** (journal de décision) | « Décision de la révision… À la demande du propriétaire… Retour : restaurer… » |
| H:34 | Décision de la révision de corrections (2026-10-08) | historique | idem |
| H:36-40 | Décision du second audit (2026-10-04), périmètre, maintenance et preuve | historique | idem |
| H:42 | Décision de la révision d'audit interne (2026-10-04) | historique | idem |
| H:44-46 | Décision de la révision de mobilisation (sans date) | historique | idem |
| H:48 | Décision de la révision d'activation (sans date) | historique | idem |
| H:50 | Les cinq sources normatives ; guides et cartes sans règle concurrente ; `RUN_CARD` et validateurs pour la projection machine | **normatif** (autorité) | « Les cinq sources normatives sont… » |
| H:52 | Comportement du lecteur : identifiants structurels, `LAYER/*`, refus d'un nom absent ou ambigu | description d'outil (ni règle ni histoire) ; à placer avec F:300 / `read_route.py` | « Le lecteur projette… » |
| H:54 | **Règle d'évolution** : source unique, propriétaire, périmètre, compatibilité, preuve, limite, prochaine revue, retour ; transversalité sur décision du propriétaire | **normatif** (maintenance) | « Toute évolution doit identifier… » |
| H:56 | L'historique n'est pas livré et n'est pas requis | normatif (déclaration) | « L'historique de conception… n'est pas livré » |
| H:24 | Budget de `SKILL.md` : 46 000 octets UTF-8, procédure de dépassement | **normatif** (maintenance) | « borné à 46 000 octets UTF-8 » |
| H:58-70 | Cycle de vie des routes : statuts, transitions, dépréciation | **normatif** | tableau H:62-68 |
| H:72-84 | Migration des alias | **normatif** (compatibilité) | tableau H:76-82 |
| H:14-23, H:25-28 | Description des sources, du noyau, de la direction avant fabrication, de la trace, etc. | **mixte** : résumé du produit courant (double les sources propriétaires) ; contient quelques règles propres (H:20 `OBSERVED`/`NOT-VERIFIED`/`N/A-JUSTIFIED`) | « Direction avant fabrication… » |

Mesure (longueurs de lignes) : environ 10 800 des 11 948 car. de la section sont de l'historique de décision (H:32-48) ; la déclaration d'autorité et la règle d'évolution (H:50-56) tiennent en 1 100 car.

## Défauts
| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| H1 | structure | important | Un fichier normatif dont 60 % est un journal | Séparer règles et journal |
| H2 | obsolète | important | H:32, 34, 36, 40, 42, 44, 48 « Retour : restaurer … depuis l'historique » ; H:56 | Le journal vit hors distribution ou la consigne est reformulée |
| H3 | répétition | important | H:32-48 ↔ B:7-77 ; H:14-28 ↔ B:85-92 | Un seul journal |
| H4 | structure | mineur | H:44 et H:48 sans date ; ordre non chronologique (10-08, 10-08, 10-04, 10-04, ?, ?) | Dater et ordonner |
| H5 | langue | important | H:32 : un paragraphe de 2 200 car. de codes et de noms de scripts | Découper en rubriques (décision, périmètre, compatibilité, preuve, limite, retour) |
| H6 | risque | important | Exemption : `validate_structure.py:10,100-125` autorise 30 termes retirés « dans l'historique (CHANGELOG) » | Déplacer l'historique oblige à déplacer l'exemption |
| H7 | risque | important | Source de la version et de la révision : `validate_design_governance.py:85`, `read_route.py:215`, F:109 | Garder l'en-tête (H:1-8) tel quel |
| H8 | incohérence | mineur | H:38 cinq sources « ce fichier (version, cycle de vie, migration) » : n'annonce pas le journal | Aligner |
| H9 | visuel | mineur | `\` de fin de ligne H:5 | Corriger |

## Savoir à protéger
- Version, statut expérimental, date, révision, usage recommandé : H:3-8.
- Description de V1 : sources, noyau compilé, `DIRECTION/CHARGE` seule liste, prise de brief (trois demandes au plus), Creative Boot `MODAL`/`PARTI`, marqueurs de vague, proposition et trace graduée, vérité du contenu, ancre graduée, interfaces, entrées, projection machine, contrôles (liste close), recherche, préparation, recette de rendu, efficacité `NOT-VERIFIED` : H:12-28.
- Budget 46 000 octets UTF-8 et procédure de dépassement : H:24.
- Décisions de révision (chacune avec propriétaires, périmètre, compatibilité, mainteneur, preuve, limite, revue, retour) : H:32 (accès), H:34 (corrections), H:36-40 (second audit), H:42 (audit interne), H:44-46 (mobilisation), H:48 (activation).
- Cinq sources et rôle des guides et cartes : H:50.
- Comportement du lecteur sur identifiants structurels : H:52.
- Règle d'évolution (huit éléments requis) : H:54.
- L'historique n'est pas livré ni requis : H:56.
- Statuts de route (`SEED`, `PILOT`, `ADOPTED`, `DEPRECATED`, `ABANDONED`), transitions, conditions de dépréciation, informations requises à toute nouvelle route : H:60-70.
- Alias `REFERENCES/*` et leur reclassification ; reclassification ambiguë reste `NOT-VERIFIED`/`EXPLORATORY` : H:74-84.
- Limites de la version : H:88-90.

## Ce qui fige ou pousse à la convergence
Aucun relevé de valeur de design. H:16 `[VEILLE 2026-09]` est un marqueur de tendance datée (autorisé par la charte).

## Dépendances et risques de déplacement
- Cité par : A:54, A:117, A:146, B:94, C:17, D:289, F:293 (préfixe `CHANGELOG/*`), `validate_*`.
- Verrous : 18 phrases (`validate_structure.py` 7, `validate_reading_map.py` 4, `validate_design_governance.py` 3, `read_route.py` 2, `build_core.py` 1, `validate_all.py` 1). Le contrôle de version (`validate_design_governance.py:85-100`) lit « **Version expérimentale :** `Vx.y.z` » ; `read_route.py:215` lit « **Révision :** » et le compare à F:109 (`connections()`). `validate_structure.py` autorise ~30 vocabulaires retirés dans CHANGELOG (« historique »).
- Exceptions de vocabulaire retiré : `validate_structure.py:100-125` liste `{"CHANGELOG.md"}` comme seul fichier où un terme remplacé peut subsister (« l'historique », `validate_structure.py:10`). Si le journal quitte H, cette tolérance doit suivre ; à vérifier par un essai de validation.
- Déplacer le journal vers un fichier hors distribution : rien ne casse à ma connaissance, mais l'inventaire (`package_manifest.json`) et la table de correspondance doivent le noter.

## Synthèse
La partie normative du CHANGELOG est petite et nette : en-tête de version, budget, règle d'évolution, cycle de vie, alias, limites (H:50-56 ≈ 1 100 car., cycle de vie et alias H:58-84 ≈ 2 500 car., budget H:24, limites H:86-90 ; H:12-28 à trier). Le reste est un journal de décisions qui double `RELEASE_NOTES.md` et dont les consignes de retour renvoient à un historique non livré. Séparer la règle de l'historique est la décision principale, avec trois verrous à emporter : version, révision, exemptions de vocabulaire retiré.

---

# Résumé des décisions à prendre (pour la table de correspondance)

| Décision | Fichiers | Gravité |
|---|---|---|
| Une seule porte débutant, en tête, avec « où commencer » ; portes designer et équipe à créer | A, C, D, F | important |
| Scinder A en entrée et document mainteneur (A:123-200) | A | important |
| Séparer l'historique de B et de H ; garder la révision courante et les limites | B, H | important |
| Retirer G, C ou les fusionner, avec manifeste, `MAP-01`, `validate_reading_map.py` | C, G | important |
| Scinder E : mots du design / codes de gouvernance | E | important |
| D : couper (équipe, designer, lecteur) ; neutraliser l'exemple D:197-244 | D | important |
| F : distinguer sujets, connexions, combinaisons ; vérifier C01-C09 contre leurs propriétaires avant déplacement | F | important |
| Un énoncé par limite, une formule de parcours, une liste des cinq sources | A, B, C, D, E, F, H | important |
