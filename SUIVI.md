# Suivi des travaux

Ce fichier suit le cap du système, les constats relevés, les actions ouvertes et les décisions prises. Il n’est pas normatif : une règle fait foi dans sa section propriétaire. Il vit seul sur la branche `suivi`, séparée du paquet : ni la validation ni les distributions n’y touchent.

Mettre à jour une ligne quand son statut change ; ajouter une entrée datée sous « Décisions » quand un choix est fait.

## Cap

Retenu comme cap de travail le 2026-10-22 ; son inscription dans le README reste à faire (A7).

| Niveau | Contenu |
|---|---|
| **Utilité** | Aider une personne ou un agent à transformer une demande en réalisation de design pertinente, avec une vraie direction, construite et soignée dès la première proposition, puis améliorée à partir du rendu réel ; analyser et corriger un existant. |
| **Objectif** | Obtenir un niveau élevé plus régulièrement, avec moins d’oublis, de tâtonnements et de reprises inutiles : esthétique, identité, usage et solidité de l’exécution. |
| **Hypothèse à éprouver** | Q1 : le système oriente-t-il les choix ? Q2 : mobilise-t-il les bons moyens ? Q3 : conduit-il au niveau visé ? Chaque question se juge par comparaison avec un travail fait sans lui, sur des demandes comparables. |

Filtre pour toute évolution : quelle question sert-elle, et comment le saura-t-on ? La capitalisation des enseignements d’un run à l’autre est une direction de travail, pas une capacité acquise.

## Constats

Relevés le 2026-10-22 sur `main` au commit `c77a8bc`.

| ID | Constat | Mesure ou source |
|---|---|---|
| C1 | Le tronc DIRECTION est presque plein : 34 331 caractères sur 35 000 (98 %), marge 669. `DIRECTION/VISUAL_TARGET` en occupe 9 209. | `read_route.py --tronc DIRECTION` |
| C2 | `ACTION/GATE-A` (8 073 caractères) est lue par quatre modes sur cinq et occupe 23 % de chaque budget de tronc. | `read_route.py --tronc MODE` |
| C3 | Le sommaire annonce « 110 routes » pour 74 routes distinctes : un fichier qui héberge plusieurs responsabilités y est listé plusieurs fois. | `read_route.py --sommaire`, lignes dédoublonnées |
| C4 | 25 routes ne sont citées ni par le noyau ni par `DIRECTION/CHARGE`. La plupart le sont à dessein (catalogue des formes, atteint par `BIBLIOTHEQUE/SELECT`). À examiner : `ACTION/STRUCTURED-PROOF`, `ACTION/RECETTE-RENDU`, `SAVOIR/CONTEXT`. Cause en partie expliquée par l’audit (L1-01, L1-02). `ACTION/RECETTE-RENDU` est en fait atteinte par un renvoi explicite de `GATE-A`, dans le tronc (L2, « Ce qui tient »). | Recherche des codes dans `SKILL.md` et la ligne de `CHARGE` |
| C5 | La mobilisation est presque entièrement tirée : une route n’est lue que si l’agent reconnaît son signal. Les signaux les plus importants (« motif générique », « finesse sans geste concret », « direction faible ») décrivent des défauts que l’agent voit mal en lui-même. | Tableau des signaux du noyau, section 10 |
| C6 | Le journal de mobilisation voit les lectures et les appels, pas un problème non reconnu. Il ne voit que `read_route.py` et les recettes : un fichier ouvert directement n’y apparaît pas. | `scripts/journal_mobilisation.py` |
| C7 | `check_caractere.py` nomme les routes à lire pour chaque signal ; `check_render.py` ne renvoie qu’à `ACTION/GATE-A`. | Codes de route cités dans les deux scripts |
| C8 | Onze éléments sont à l’essai, aucun adopté ni éprouvé sur un run de design complet. Revue avant 2027-04. | `maintenance/versions.md`, « Sections à l’essai » |
| C9 | Efficacité `NOT-VERIFIED`. Seules comparaisons avec et sans le système dans le corpus : quelques rendus internes en septembre 2026, où palette et police par défaut reviennent avec ou sans lui (L4-04). | `maintenance/versions.md` |
| C10 | Le paquet pèse environ 700 k de texte pour 660 k de code et 140 k de JSON (octets, hors images, cartes et polices). | Taille des fichiers par dossier |

## Actions

Statuts : `À FAIRE`, `EN COURS`, `FAIT`, `À DÉCIDER`, `ABANDONNÉ`.

| ID | Action | Sert | Statut | Fin quand |
|---|---|---|---|---|
| A1 | Faire pousser les routes par `check_render.py`, sur le modèle du gate C qui le fait déjà (`finition.md:16-23`) : chaque défaut relevé nomme la route qui le traite (contraste vers `SAVOIR/CRAFT/CFT-05`, texte sur image vers `SAVOIR/CRAFT/CFT-03`, textes tronqués ou titre déséquilibré vers `SAVOIR/TYPE`). | Q2 (C5, C7) | `À FAIRE` | La sortie et le journal portent la route proposée ; tests du paquet verts. |
| A2 | Mesurer la reconnaissance des signaux : sur chaque run de la campagne, une personne note les signaux présents ; on les compare aux routes lues. | Q2 (C5, C6) | `À FAIRE` | Un taux de signaux manqués par signal, sur au moins cinq runs. |
| A3 | Rattacher certaines lectures à un moment plutôt qu’à un signal, par exemple `SAVOIR/CRAFT/CFT-00` après le premier rendu en DIRECTION. | Q1, Q3 (C5) | `À DÉCIDER` | Arbitrage avec le budget du tronc DIRECTION (C1). |
| A4 | Corriger le décompte du sommaire pour annoncer les routes distinctes. | Cohérence (C3) | `À FAIRE` | Le sommaire annonce 74 routes ; test du lecteur ajouté. |
| A5 | Campagne d’évaluation : cinq à dix briefs contrastés, runs avec et sans le système, journal activé (`DG_JOURNAL`), rendus jugés par des personnes ; reprendre les signaux d’apprentissage de `boucle.md:78-80`, les mesures de série de `gouvernance/cloture.md:78-80` et le contrat `EVALUATION_CASE`. | Q1, Q2, Q3 (C8, C9) | `À FAIRE` | Protocole écrit, puis résultats avec point de départ, observation et limite (contrat de gain réel). |
| A6 | Redonner de la marge au tronc DIRECTION, par exemple en séparant dans `DIRECTION/VISUAL_TARGET` ce qui doit être lu à chaque run de ce qui peut l’être sur signal. Voie chiffrée : L2-06 (jusqu’à environ 6 800 caractères). | Q1 (C1, L2-06) | `À DÉCIDER` | Marge rendue sans retirer de contrainte bloquante du tronc. |
| A7 | Inscrire le cap : version courte en tête du README, texte complet relié depuis le README et la fiche de version. | Cap | `À FAIRE` | README et fiche à jour ; validation verte. |
| A8 | Examiner les routes atteintes seulement en cascade (C4) : faut-il un signal, un renvoi plus direct, ou rien ? `ACTION/RECETTE-RENDU` est réglée (renvoi de `GATE-A`) ; `ACTION/STRUCTURED-PROOF` est atteinte par `SAVOIR/TYPE` et `GATE-B/B2` (L3-02) ; reste `SAVOIR/CONTEXT`, pour laquelle L5-02 propose un signal dans le noyau (« Mouvement, responsive ou contexte à fort enjeu »). | Q2 (C4, L5-02) | `À DÉCIDER` | Décision notée pour chacune. |
| A9 | Rattacher à une route ou supprimer tout contenu normatif hors route : `agent/chemins.md:217-272`, les cinq absolus (`standard.md`, dont un énoncé court à compiler dans le noyau), « Direction divergente » (`diriger.md:119-134`), `interface.md`, `principes.md:6-31`, `cloture.md:85-102`, `structure.md:6-18` et `:71-85` (dont des doublons à supprimer plutôt qu’à rattacher, comme l’ordre de preuve de `principes.md:19`, L5-05), `sections/DIRECTION.md:37-152` et les introductions de `sections/ACTION.md`, `BIBLIOTHEQUE.md` et `SAVOIR.md` ; passer tout le corpus au relevé de couverture ; ajouter ce contrôle au validateur. | Q2 (L1-01, L2-01, L2-02, L3-01, L6-01) | `À FAIRE` | Le contrôle ne trouve plus de ligne normative hors route. |
| A10 | Une seule table de signaux de routage, celle du noyau, enrichie ; supprimer ou générer les autres, dont `SAVOIR/ROUTING`. | Q2 (L1-02, L6-03) | `À FAIRE` | Une table source ; les correspondances manquantes (`SAVOIR/CONTEXT`, `ACTION/ANTI-SLOP`, `SAVOIR/INTEGRITY`) y figurent. |
| A11 | Première étape : compiler dans le noyau la règle de réconciliation de `sections/DIRECTION.md:127` (une information vit dans la vue qui la rend décisionnelle). Puis une seule déclaration de lancement, un vocabulaire de cadrage unique, une liste d’axes, un ordre de construction et une cible (`VISUAL_TARGET`) dont boot et atelier sont des sous-ensembles, une grille de revue (celle du noyau) à laquelle les autres se rattachent, une liste d’axes qui absorbe les dials de style (L5-04) ; les autres formats deviennent des projections de la trace complète ; lever l’ambiguïté de « trame ». | Q1, Q2 (L1-03, L1-04, L2-03, L4-02, L4-07, L5-04, L6-01) | `À DÉCIDER` | Trace légère sans obligation concurrente ; correspondance des cadres écrite une fois. |
| A12 | Corrections locales : renvois périmés (L1-06), signal vers `ACTION/RECETTE-RENDU` (L1-07), définitions dans le noyau (L1-08), lien entre proposition légère et `EXPLORATORY` (L1-05), notice de la recette en listes (L2-07), adresses lisibles (L1-09, L2-08), bloc `BRIEF` dans le noyau (L2-09), mention FTC précisée (L2-10), une seule notice de la recette de rendu (L3-04), renvoi de `cloture.md:100` (L3-05), repères OKLCH sur fond sombre (L4-05), source du modèle émotionnel (L4-06), doublons et classement de l’atlas (L5-05), échéance de l’AI Act revérifiée (L5-06), locators de la carte de lecture (L6-06). | Cohérence | `À FAIRE` | Renvois corrigés ; validation verte. |
| A13 | Faire de l’atelier sur capture une étape énoncée dans `ACTION/RUN-DIRECTION` ou dans la boucle du noyau, et non un signal. | Q2, Q3 (L2-04) | `À FAIRE` | L’étape figure dans le tronc DIRECTION ; elle sort du tableau des signaux. |
| A14 | Donner à `SAVOIR/TYPE` une méthode courte pour trouver, apparier et comparer des voix typographiques. | Q1, Q3 (L2-05, confirmé aux lots 4 et 5) | `À FAIRE` | Méthode écrite et citée par la question de convergence du noyau. |
| A15 | Dire ce que deviennent en trace légère les contrats de `ACTION/STRUCTURED-PROOF` (carte de hiérarchie, partition typographique…) l’enregistrement par hypothèse de `FND-03` et les formulaires structurels de `BIBLIOTHEQUE` (tension, signature, dérivation, grille, objet), sur le modèle du gate C ; compiler dans le noyau les cinq questions de cadrage de `FND-03`. | Q2 (L3-02, L4-03, L6-05) | `À FAIRE` | Plus d’obligation écrite concurrente de la trace légère. |
| A16 | Mesurer l’usage des statuts dans la campagne (A5), puis décider s’il faut fusionner les homonymes entre issue et verdict. | Cohérence (L3-03) | `À DÉCIDER` | Après A5. |
| A17 | Mobiliser l’inventaire du sujet et la phrase d’idée au moment du premier objet, et ajouter le déclencheur de `CFT-06` (écriture) au tableau des signaux, et les citer dans la connexion C07. | Q1, Q3 (L4-01, L5-03) | `À DÉCIDER` | Avec A6 (place dans le tronc DIRECTION) ; mesuré par A5. |
| A18 | Verser à la fiche de version les observations de convergence avec et sans le système, avec leurs limites, et en faire le point de départ de A5. | Q1 (L4-04) | `À FAIRE` | Fiche de version à jour ; question de départ de la campagne écrite. |
| A19 | Ajouter `SAVOIR/SYSTEM` au tronc SYSTÈME, et un contrôle au validateur : chaque tag `[REQUIS]` a son plancher dans le noyau ou sa route dans le tronc des modes qu’il vise. | Q2 (L5-01) | `À FAIRE` | Contrôle vert sur le corpus. |
| A20 | Compiler le test de trame dans le noyau (section 4), pour que la ligne « modal, trame et parti » de la trace légère repose sur un test lu à chaque run. | Q1 (L6-02, L1-04) | `À FAIRE` | Test présent dans `SKILL.md` ; budget du noyau respecté. |
| A21 | Combler ou déclarer le biais logiciel du catalogue des formes (commerce local, commerce en ligne, lecture, événement). | Q1 (L6-04) | `À DÉCIDER` | Routes ou exemples ajoutés, ou biais déclaré. |

## Décisions

- **2026-10-22.** Création de ce fichier de suivi, sur une branche à part (`suivi`) pour ne pas entrer dans le paquet ; une copie de travail reste dans la session.
- **2026-10-22.** Le texte de mission est retenu comme cap de travail, en trois niveaux : utilité, objectif, hypothèse à éprouver (voir « Cap »).
- **2026-10-22.** Audit lancé : sept perspectives (MIS à VER, plus LIS pour les fichiers destinés aux personnes), quatre gravités, lecture intégrale par lots. Constats dans `AUDIT.md`. Lot 1 (`SKILL.md`, `agent/chemins.md`) terminé : un bloquant, trois importants.
- **2026-10-22.** Lot 2 de l’audit (tronc DIRECTION, 9 fichiers) terminé : un bloquant (les cinq absolus hors route), quatre importants. Actions A13 et A14 ajoutées ; A6, A8, A9, A11 et A12 complétées.
- **2026-10-22.** Codes de perspective de l’audit renommés (MIS, MOB, SAV, COH, EXE, PRO, VER, LIS) pour éviter la confusion avec l’ordre de preuve `P0` à `P3` du système. Lot 3 (production, réponse, gouvernance ; 13 fichiers) terminé : trois importants. A15 et A16 ajoutées.
- **2026-10-22.** Lot 4 de l’audit (savoir, première partie ; 5 fichiers) terminé : quatre importants, dont un premier indice sur Q1 (L4-04). A17 et A18 ajoutées.
- **2026-10-22.** Lot 5 de l’audit (savoir, seconde partie ; 6 fichiers) terminé : un important (L5-01, qui nuance L4-03). L2-05 confirmé. A19 ajoutée ; A8 passe à « à décider ».
- **2026-10-22.** Lot 6 de l’audit (formes et sections de référence ; 9 fichiers) terminé : deux importants (règle de réconciliation hors route, test de trame non compilé). A20 et A21 ajoutées ; A9, A10, A11, A12 et A15 complétées.
