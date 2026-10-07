# U1b — Fiche d'inventaire n°7 : les guides

**Base :** commit `d90869c`. **Lecture intégrale :** `README.md` (198 lignes), `V1/official/README.md` (21), `QUICKSTART.md` (291), `READING_MAP.md` (309), `GLOSSAIRE.md` (89), `ORCHESTRATION_MAP.md` (3). **Angle :** ce que les guides possèdent, et pour qui.

## 1. Identité

| Fichier | Taille | Lecteur visé | Lu par l'agent ? |
|---|---|---|---|
| `README.md` (racine) | 21 Ko | La personne qui demande, le mainteneur | Non (le noyau dit : « lectures d'orientation pour les humains ») |
| `V1/official/README.md` | 2 Ko | Index des sources | Non |
| `QUICKSTART.md` | 26 Ko | L'opérateur qui pilote un run (humain ou agent) | Non, sauf demande |
| `READING_MAP.md` | 29 Ko | L'opérateur ; **et les scripts** | **Indirectement** : ses connexions via `--connexions`, sa table de locators via `read_route.py` |
| `GLOSSAIRE.md` | 13 Ko | Toute personne | Non (absent du noyau) |
| `ORCHESTRATION_MAP.md` | 0,4 Ko | — | Pointeur vers READING_MAP |

## 2. Ce qu'ils possèdent

Niveaux : **A** actionnable · **O** orientant.

### README.md

| Élément | Lignes | Concr. | Valeur au regard de la mission |
|---|---|---|---|
| **« Commencer »** : 4 questions pour la personne qui demande (que demander, que fournir, que recevoir, comment poursuivre), sans aucun vocabulaire interne, avec des exemples de retours (« le titre écrase la photo », « trop froid pour une boulangerie ») | 12-22 | **A** | **L'interface utilisateur du système**, très réussie. Une phrase contredit la décision §9.2 du plan (« d'abord […] avant de construire », C02) |
| Fiche de version : efficacité réelle `NOT-VERIFIED`, usage en pilote supervisé | 24-32 | O | Honnêteté |
| Mission et modèle à double boucle (création / gouvernance) | 36-88 | O | Énoncé du but |
| Constitution minimale (les cinq absolus résumés) | 61-67 | O | Résumé qui diverge sur l'absolu 4 (C17) |
| Structure du dépôt, sources normatives | 90-112 | O | Navigation |
| Distributions, préparation, **reprise d'une préparation interrompue** (verrou, sauvegardes) | 114-159 | A | Maintenance, très précise |
| Commandes de validation | 161-190 | A | Maintenance ; compteur « 27 » faux (C23) |
| Limites et discipline d'usage | 192-198 | O | Honnêteté |
| **Comment installer la skill dans un agent** | — | — | **Absent** (fiche n°3) |

### QUICKSTART.md (guide opérateur)

| Élément | Lignes | Concr. | Valeur |
|---|---|---|---|
| Parcours commun : 5 questions et 6 suites possibles (corriger, approfondir, rouvrir, reclassifier, proposer, fermer) | 11-29 | A | Le cœur du pilotage en une page |
| Bénéfice attendu de chaque source (DIRECTION, SAVOIR, BIBLIOTHEQUE, ACTION) | 45 | O | Explique *pourquoi* charger |
| Entrées par besoin (agent, direction ouverte, run à persister) | 55-59 | A | — |
| Ligne de run (deux formats) | 15-16, 67-69 | A | Doublon |
| Les deux boucles (création, amélioration) | 79-90 | O | — |
| Choisir le mode : ordre et table de 6 situations | 113-136 | A | — |
| Qualité positive du premier rendu : les 8 dimensions de DIRECTION, dans le même ordre (« Retour si… ») | 144-163 | A | Projection fidèle (vérifié en U1) |
| One-shot : les 6 étapes qui ne disparaissent jamais | 165-178 | A | — |
| **Handoff agentique** : ce qu'une personne doit donner à un agent (OBJECTIVE, SCOPE, AUTONOMY, CONFIRMATION, CONSTRAINTS, OUTPUT) et ce que l'agent fait ensuite | 180-195 | **A** | **Le seul mode d'emploi pour confier un travail à un agent** |
| Exemple complet minimal : page d'accueil en mode DIRECTION, de la décision à la correction mobile | 197-246 | A (trace) | Le seul exemple proche d'une landing ; une trace, pas un rendu |
| Observer : 4 questions ; fermer : 5 vérifications | 248-279 | A | — |

### READING_MAP.md (carte dérivée)

| Élément | Lignes | Concr. | Valeur |
|---|---|---|---|
| Chemin canonique de démarrage (6 étapes) | 11-20 | O | Une formulation de plus |
| Routage minimal par décision (7 lignes) | 26-38 | A | Une table de routage de plus |
| **Combinaisons par résultat recherché** : 9 résultats (direction forte, beauté et craft, créativité variée, UI/UX habitable, preuve fiable, vitesse, système, domaine sensible, agent contrôlé) → noyau de routes, renforcements, preuve à privilégier ; garde-fous | 40-76 | A | Organise le système **par objectif** plutôt que par fichier |
| **Connexions situées C01 à C09** : contexte incertain, typographie déterminante, asset déterminant, récupération après erreur, réemploi, changement partagé, ambition vers construction, élément vers ensemble, intention vers médium. Chacune avec 6 rubriques : condition, sources, intervention, contre-indication, moyens et limites, observation | 78-212 | **A** | **L'index transversal le plus proche de « la bonne information au bon moment »** : il relie une situation à plusieurs fichiers et à un geste |
| Illustrations de préparation (céramique, comparaison d'usage, affiche de festival, séquence) | 214-216 | Nommées seulement | Quatre briefs cités, sans contenu ni rendu |
| Activation multi-perspective : 11 perspectives (direction, production, usage, contenu, responsive, accessibilité, runtime, preuve, maintenance, coordination, mémoire), avec déclencheur, lecture, sortie et cas de non-chargement | 218-234 | A | — |
| Handoff (copie), résolution des routes | 236-271 | A | Doublon |
| **Table des 25 locators principaux** | 273-305 | — | **Dépendance d'exécution** : `read_route.py` la lit |

### GLOSSAIRE.md

| Élément | Lignes | Concr. | Valeur |
|---|---|---|---|
| **57 termes en langage simple** (décision, JTBD, scope, thèse, ancre, MODAL, PARTI, plafond, objet de preuve, défaut dominant, trace légère…), dont 16 contrôlés par le validateur | 5-63 | A | Définitions claires, utilisables face à une personne |
| 6 exemples express ; un départ en 4 étapes | 65-89 | A | — |

## 3. Ce que les guides ne possèdent pas

1. **Aucune instruction d'installation** de la skill dans un agent (Claude Code ou autre).
2. **Aucun exemple rendu** : l'exemple complet de QUICKSTART et les « illustrations de préparation » sont des traces ou des noms.
3. **Aucune porte d'entrée pour l'agent** : tout ce que les guides offrent de meilleur pour lui (connexions, combinaisons, handoff agentique, glossaire) ne lui parvient que s'il sort du noyau.

## 4. Redondances mesurées dans l'ensemble des documents

| Contenu | Nombre de versions | Où |
|---|---|---|
| Le parcours principal | **au moins 6** | README (double boucle), QUICKSTART (6 étapes et 2 boucles), `flow.md` (7 étapes), READING_MAP (chemin en 6 étapes), GLOSSAIRE (4 étapes), RELEASE_NOTES (l. 93-97, ajouté par la fiche n°9) |
| Ce qu'on écrit avant d'agir | **5** | Ligne de run de DIRECTION, entrée minimale, deux lignes de QUICKSTART, handoff |
| Tables de routage ou de chargement | **au moins 8** | CHARGE, carte d'ACTION, ACTION/ROUTING, SAVOIR/ROUTING, déclencheurs et index de DIRECTION, routage minimal et combinaisons de READING_MAP, table des modes de QUICKSTART |
| Le handoff | **3** | ACTION, READING_MAP (copie déclarée), QUICKSTART (version agentique, différente) |

Chaque copie se déclare « dérivée » ou « non normative ». Elles restent cohérentes entre elles grâce aux validateurs (U1 : aucune incohérence trouvée par lecture, à part C01, C02, C13, C17).

## 5. Potentiel présent mais peu exploité

| Élément | Pourquoi il compte au regard de la mission | Accès actuel |
|---|---|---|
| **« Commencer » du README** | L'interface en langage simple que la mission demande ; déjà écrite et bien faite | Humains seulement |
| **Connexions C01 à C09** | Un index **par situation** qui traverse les fichiers et mène à un geste : c'est la forme la plus aboutie de « mobiliser la bonne connaissance » | Via `--connexions`, si l'agent pense à l'ouvrir |
| **Combinaisons par résultat** | Organise les capacités par objectif (beauté et craft, UI/UX habitable, vitesse…) | Opérateur seulement |
| **Handoff agentique** | Dit comment confier un travail à un agent (autonomie, confirmations, sortie attendue) | Opérateur seulement |
| **Glossaire** | Définitions simples, prêtes pour la réponse visible en langage produit | Non référencé par le noyau |

## 6. Observations à verser au registre

| Observation | Lien |
|---|---|
| Aucune instruction d'installation de la skill | Fiche n°3 (skill non autonome) |
| Au moins 6 formulations du parcours, au moins 8 tables de routage, 3 handoffs | Charge de maintenance ; C13 |
| « Illustrations de préparation » sans contenu | `READING_MAP.md:216` |
| Le glossaire compte bien 57 termes : correction de ma vérification de l'analyse externe, où j'en comptais 63 | `04-verification-analyse-externe.md` |

## 7. En une phrase

Les guides possèdent **les meilleures interfaces du système** : « Commencer » pour la personne qui demande, le handoff agentique pour confier un travail, les connexions et combinaisons pour mobiliser le savoir par situation, et un glossaire clair. Mais ils sont **écrits pour un opérateur humain**, **redondants entre eux** (au moins 6 parcours, au moins 8 tables de routage), et **presque rien n'en parvient à l'agent**.
