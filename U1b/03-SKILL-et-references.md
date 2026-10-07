# U1b — Fiche d'inventaire n°3 : `SKILL.md` et ses 4 références

**Base :** commit `d90869c`. **Lecture :** intégrale de `SKILL.md` (226 lignes, lu en U1 puis relu pour l'inventaire), `examples.md` (119 lignes), `flow.md` (26), `canonical_minimum.md` (25), `machine_projection.md` (129). Contenu de l'archive Local vérifié. **Angle :** ce que l'agent a réellement entre les mains.

## 1. Identité

| Fichier | Taille | Rôle |
|---|---|---|
| `SKILL.md` | 43 201 o (noyau compilé : 41 217 o, 8 sections ; budget 46 000 o) | Lu à chaque run |
| `references/examples.md` | 9,9 Ko | 5 exemples de traces |
| `references/flow.md` | 2,1 Ko | Le parcours en 7 étapes (diagramme et texte) |
| `references/canonical_minimum.md` | 1,8 Ko | Aide-mémoire si les sources sont absentes |
| `references/machine_projection.md` | 7,4 Ko | Carte de run en YAML et règles de sérialisation |

## 2. Rôle

- **Déclaré** (l. 8) : « couche d'activation » ; le noyau est compilé depuis les sources, qui font foi.
- **Réel :** c'est **le seul texte dont l'agent est sûr de disposer**. Le reste du système n'existe pour lui que s'il ouvre une route avec `read_route.py`, donc s'il sait qu'il doit le faire et si les scripts sont accessibles (section 6).

## 3. Ce que l'agent possède en lisant seulement `SKILL.md`

Niveaux : **A** actionnable · **O** orientant.

| Couche de travail | Contenu du noyau (§) | Concr. |
|---|---|---|
| **Posture** | Rôle de directeur artistique senior ; « première idée = hypothèse à tester contre la convergence » (§1) | O |
| **Classer et charger** | Règle de vitesse, recherche `--trouver`, connexions, table de chargement par mode (§2) | A, mais renvoie à 48 routes |
| **Comprendre le besoin** | Prise de brief (3 demandes au plus, par gain de plafond) ; contenu d'exemple **marqué** et action principale fonctionnelle ; données d'exemple cohérentes (§3) | A |
| **Direction artistique** | Promesse → objet de preuve → geste ; marquage `TRUTH/*` (§3) ; question de convergence palette et police, comparer deux voix sur le vrai titre (§5) ; marqueurs de vague datés (§5) | A |
| **Structure** | Où elle vit, comment le regard circule… ; 6 polarités ; 7 axes de tension ; activer la bibliothèque (intention → niveau → levier → effet) ; 7 signaux de convergence ; test de trame (§4) | A |
| **Composition** | Grammaire intention → retenue ; test de singularité ; forme située ; contrôles d'alignement et de responsive (§5) | A |
| **Typographie** | Critères de choix ; équilibre d'un titre (§5) | A |
| **Couleur** | Palette par rôles ; question de convergence (§5) | A |
| **Craft et finition** | Table de 13 gestes, choix et contrôle (§5) | **A**, le cœur concret |
| **Assets et moyens** | Plafond de fabrication ; ancre (explorer, accepter, diffuser) ; carte des moyens en résumé ; traitement des assets moyens ; calibrations par domaine ; pas de faux asset (§6) | A, mais moyens = noms (C38) |
| **Observer et corriger** | Boucle d'édition ; table de diagnostic ; atelier B1b ; revue créative ; 6 questions ; repasse ; varier un axe à la fois (§7) | A |
| **Répondre** | La première proposition vaut checkpoint ; 4 rubriques en langage produit ; système activé en silence ; trace légère en 6 lignes (§8) | A |

**Constat d'ensemble :** le noyau couvre **toutes les couches de la mission**, de façon le plus souvent actionnable. C'est un texte de fabrication, pas seulement de gouvernance.

## 4. Ce que l'agent ne possède pas en lisant seulement `SKILL.md`

| Absent du noyau | Où cela existe | Effet probable |
|---|---|---|
| Les cinq absolus, le piège de conformité, l'ordre P0 à P3 | DIRECTION | Protections fondamentales hors du texte toujours lu (C17 à C19) |
| La traduction des mots vagues (« moderne », « premium », « intuitif ») | SAVOIR/STYLE | Les mots de la personne ne sont pas convertis systématiquement |
| La table des émotions (calme, énergie, confiance, luxe, sérieux) | SAVOIR/CRAFT, CFT-04 | Les retours du type « trop froid » sont traités sans leviers de référence |
| La nuance « objet ou geste d'abord » | SAVOIR/CRAFT, CFT-04a | Le noyau pousse toujours l'objet de preuve en premier |
| La table intention → construction | BIBLIOTHEQUE/SELECT | L'activation y renvoie, sans le contenu |
| La recette complète de récupération d'erreur | SAVOIR/STATE, RCV-01 | Une seule phrase au noyau |
| « Premier objet habitable » et thèse structurelle | BIBLIOTHEQUE | — |
| Valeurs de départ, ressources concrètes, exemples visuels | **Nulle part** (fiches n°1 et 2) | L'agent fabrique tout de mémoire |

## 5. Les quatre références

| Fichier | Ce qu'il possède | Ce qu'il ne possède pas |
|---|---|---|
| **examples.md** | 5 exemples : LITE (contraste), DIRECTION avec brief flou (atelier vélo, trace légère), DIRECTION identitaire (hero de cartographie sonore, trace complète), DIRECTION + STYLE (archive, `DIGITAL_MEMORY`), SYSTÈME (Select partagé). Ils montrent la **séquence** et la **trace**, avec des `DECISION-CHANGE` crédibles (CONFIRMED, CHANGED, ABANDONED). | **Aucun rendu** : ce sont des traces, toutes `ILLUSTRATIVE` et `SIMULATED` (l. 3). **Aucun exemple de landing SaaS**, la demande la plus fréquente et votre propre exemple. L'exemple vélo attend la réponse avant de construire (C01) et a un objet « … du jour » (C34). |
| **flow.md** | Le parcours en 7 étapes (classer, protéger, cultiver et diriger, composer et construire, polir et observer, vérifier et corriger, proposer ou fermer) et un diagramme Mermaid | Une troisième formulation du parcours (avec QUICKSTART et le README) ; dit « charger `DIRECTION/START` avant un build », alors que le noyau dit qu'en LITE l'arbre suffit |
| **canonical_minimum.md** | Si les sources manquent : ne pas inventer ; les séparations entre statuts | Aucun savoir de design, mais le noyau le porte déjà |
| **machine_projection.md** | La carte de run complète en YAML, commentée ; règles de sérialisation | Copie en YAML de `schemas/run_card.example.json` (un exemplaire de plus à maintenir) ; identifiant d'exemple `DIRECTION-PREMIUM-001` ; décision et intention de décision présentées comme deux placeholders voisins |

## 6. Accès réel : la skill n'est pas autonome

1. **Les chemins sont relatifs à la racine du paquet.** Le noyau demande `python3 scripts/read_route.py …`, et l'export Local cite `official/…` ; ces fichiers sont dans le paquet, pas dans le dossier de la skill. *Vérifié* sur l'archive Local (63 fichiers, skill dans `skill/`).
2. **Aucune instruction d'installation dans un agent.** Ni le README GitHub ni le README Local n'expliquent comment brancher la skill sur Claude Code ou un autre agent. *Vérifié* par lecture.
3. **Conséquence déduite, non testée.** Si la skill est installée seule, comme on le fait d'habitude avec une skill, l'agent garde le noyau et `canonical_minimum`, mais perd les routes, la recherche et `check_render`. La skill prévoit ce cas (l. 8 : « le dire et s'appuyer sur canonical_minimum ; une proposition reste alors une hypothèse »), mais tout ce qui est hors du noyau devient alors inaccessible.
4. **Le déclenchement est large.** La description (frontmatter) dit : « Utiliser pour toute demande de design à construire, corriger ou juger. »

## 7. Observations faites en passant (à verser au registre)

| Observation | Où | Lien |
|---|---|---|
| Skill non autonome ; pas d'instruction d'installation | Section 6 | Nouveau, à confirmer par un essai d'installation |
| Aucun exemple ne montre un rendu ; aucun exemple de landing SaaS | `examples.md` | Nouveau |
| Copie YAML de la carte de run | `machine_projection.md` | Doublon (C36 voisin) |
| Troisième formulation du parcours | `flow.md` | Déjà relevé par l'analyse externe |

## 8. En une phrase

Le noyau de `SKILL.md` est **un bon texte de fabrication qui couvre toutes les couches du travail**, mais il est **le seul accès garanti** au système. Les outils les plus utiles des sources et tous les scripts n'existent pour l'agent que s'il travaille depuis la racine du paquet et pense à les ouvrir. Les exemples montrent des traces, jamais des rendus.
