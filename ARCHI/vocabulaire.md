# Vocabulaire — des codes internes aux noms clairs

**Statut :** proposition, phase 2, le 9 octobre 2026. Ce vocabulaire est appliqué en phase 4 (langue). Les blocs copiés dans la skill attendent la phase 5.

## Règles

1. **Ce que lit un humain ne contient aucun code.** Une route se nomme par son titre en clair (« la couleur », « le plancher produit »). Son adresse sert au lecteur et à l’agent : elle est écrite entre accents graves, jamais au milieu d’une phrase.
2. **Les adresses deviennent des chemins lisibles.** `dossier/fichier` ou `dossier/fichier#section`, en minuscules et en français. Exemple de forme : `savoir/couleur`. Les anciennes adresses (`SAVOIR/CRAFT/CFT-05`) restent acceptées par le lecteur comme alias, le temps de la transition. La table complète des alias se déduit de `correspondance.csv`.
3. **Les valeurs machine ne changent pas.** Les valeurs des schémas (`NOT-VERIFIED`, `ACCEPTED`, `EXPLORATORY`…) restent identiques dans `gouvernance/schemas/`, pour ne pas casser les fiches existantes. Le texte humain emploie le nom clair et cite la valeur machine une seule fois, dans le module de gouvernance.
4. **Les identifiants de règle deviennent invisibles.** Ils passent dans des commentaires (`<!-- règle:… -->`), où les contrôles les retrouvent sans qu’un lecteur les voie.
5. **Un terme garde un seul sens, et une notion un seul terme.** Un terme de métier (grille, hiérarchie, contraste, ancre) est gardé et défini à sa première apparition dans le glossaire.
6. **On ne traduit pas ce qui est un usage établi du métier** : *slop* (production générique d’IA), *responsive*, *token*, *mockup*. Ces termes sont définis une fois.

## Fichiers et grandes parties

| Ancien | Nouveau nom | Nouvelle place |
|---|---|---|
| `DIRECTION.md` (partie design) | La direction | `design/direction/` |
| `DIRECTION.md` (classement, chargement) | Les chemins de l’agent | `agent/chemins.md` |
| `SAVOIR.md` | Le savoir | `design/savoir/` |
| `BIBLIOTHEQUE.md` | Les formes | `design/formes/` |
| `ACTION.md` (qualité du rendu) | La qualité du produit | `design/produit/` |
| `ACTION.md` (fiche, statuts, clôture) | La gouvernance | `gouvernance/` |
| `READING_MAP.md` | Guide du designer, connexions | `guides/designer.md`, `design/savoir/connexions.md` |
| `QUICKSTART.md` | Guide d’équipe | `guides/equipe.md` |
| `GLOSSAIRE.md` | Glossaire | `guides/glossaire.md` |
| `CHANGELOG.md`, `RELEASE_NOTES.md` | Évolution, versions | `maintenance/` |
| `skills/design-governance-practice/` | La skill | `agent/skill/` |
| `scripts/` | Outils | `outils/`, et `gouvernance/outils/` pour ceux du module |

## Chemins et modes

| Code | Nom clair | Note |
|---|---|---|
| `LITE` | retouche | une correction locale |
| `ITER` | itération | sur une direction existante |
| `STANDARD` | écran cadré | structure ouverte, direction donnée |
| `DIRECTION` (mode) | direction ouverte | page ou identité à diriger |
| `SYSTÈME` | système de design | composants et tokens partagés |
| trace légère / complète | trace courte / trace complète | |
| `FAST-PATH` | chemin court | |
| `START` | classer avant d’agir | |
| `CHARGE` | quoi lire | |
| `ROUTING` | prérequis | fusionné avec « quoi lire » |

## Direction

| Code | Nom clair |
|---|---|
| `EXTERNAL-START` | partir d’une demande vague |
| `CREATIVE-BOOT` | lancement créatif |
| `DOMAIN-FRAME` | cadrer le domaine |
| `VISUAL_TARGET` | cible visuelle |
| `FIRST-OBJECT` | premier objet |
| `DIRECTION-ATELIER` | atelier de direction |
| `DOUBLE-LOOP` | créer puis apprendre (la boucle) |
| `SERVICE-BOUNDARY` | relation ou contrat |
| `ABSOLU 1` à `5` | les cinq règles essentielles, chacune nommée par son contenu |
| `REUSE-CHALLENGE` | test de réutilisation |
| `JTBD` | tâche visée (*job to be done*) |
| `ANCHOR` ; `-PROVIDED`, `-OBSERVED`, `-GENERATED` | ancre (référence visuelle) ; fournie, observée, générée |

**Champs du lancement créatif :**

| Code | Nom clair |
|---|---|
| `DECISION` | décision |
| `PROMISE` | promesse |
| `PROOF-OBJECT` | objet de preuve |
| `GESTURE` | geste |
| `MODAL` | le choix attendu (ce que tout le monde ferait ici) |
| `PARTI` | parti pris |
| `STRUCTURAL-TENSION` | tension de structure |
| `STRUCTURAL-SIGNATURE` | signature de structure |
| `CFT-TARGETS` | qualités visées |
| `FABRICATION` | moyens et plafond |
| `DOMINANT-DEFECT` | défaut principal |
| `NEXT-PROOF` | prochaine preuve |
| `OWNER` | responsable |
| `SCOPE` | périmètre |
| `RISK` | risque |
| `CONSTRAINT` | contrainte |

## Savoir

| Code | Nom clair |
|---|---|
| `FRAME`, `FND-01` | fondements ; principe fondateur |
| `FND-02` | compromis |
| `FND-03` | cadrer le contexte |
| `CRAFT`, `CFT-00` | qualité créative et ambition |
| `CFT-01` | forme située |
| `CFT-02` | registres |
| `CFT-03` | composition, densité, harmonie |
| `CFT-04` | émotion |
| `CFT-04a` | premier contact |
| `CFT-05` | couleur et contraste |
| `TYPE` | typographie |
| `STATE` | composition et détails ; états (côté produit) |
| `SOURCE` | images et sources |
| `DESIGN-ATLAS` | familles visuelles |
| `STYLE` | styles |
| `SYSTEM` | système de design |
| `CONTEXT` | contexte et accessibilité |
| `TECH` | techniques par médium |
| `TOOLS` | goût et tendances |
| `VEILLE`, `CONVERGENCE` | tendances datées |
| `MOYENS` | ressources |
| `INTEGRITY` | intégrité (module) ; pièges (savoir) |
| `JUGEMENT-COURT` | jugement rapide |

## Qualité du produit et contrôles

| Code | Nom clair | Place |
|---|---|---|
| `FIRST-RENDER` | premier rendu | produit |
| `UI-UX-REALITY` | interface réelle | produit |
| `GATE-A` | plancher produit | produit (procédure au module) |
| `GATE-C` | finition sur rendu | produit |
| `ANTI-SLOP` | contre le générique | produit, fusionné avec la finition |
| `VISUAL_PROOF` | preuve visuelle | produit |
| `STRUCTURED-PROOF` | contrats de décision | produit (gabarits), module (déclencheurs) |
| `B1` | comparaison | produit |
| `B1b` | comparaison sur capture (atelier d’édition) | produit ; formalités au module |
| `B4` | corrections ancrées | produit |
| `GATE-B` | vérification en contexte | module |
| `B2`, `B3`, `B5`, `B6` | familles de preuve, regard extérieur, trace des assets, sortie compacte | module |
| `V/U/A/T` | caractère, usage, accessibilité, robustesse | produit (les questions), module (les verdicts) |
| `POLICIES` | contraste (produit) ; inspection et ressources (module) | |

## Gouvernance (module)

| Code | Nom clair |
|---|---|
| `RUN`, `RUN_CARD` | travail, fiche de travail |
| `HANDOFF` | réponse et trace |
| `PRECONDITION` | conditions de départ |
| `STATUS` | statuts |
| `CLOSE-PACKAGE` | dossier de clôture |
| `CLOSE-EXIT-CHECK` | test de sortie |
| `PIPELINE-DIRECTION` | déroulé de la direction |
| `OVERRIDE`, `FAIL-ASSUMED` | dérogation, défaut assumé |
| `AUTHORITY` | portée d’action |
| `MAINTENANCE` | maintenance (déplacée dans `maintenance/`) |

**Valeurs machine**, qui restent identiques dans les schémas ; leur nom clair est employé dans le texte :

| Valeur machine | Nom clair |
|---|---|
| `NOT-VERIFIED` | non vérifié |
| `NOT-OBSERVED` | non observé |
| `N/A-JUSTIFIED` | sans objet (justifié) |
| `PASS`, `PASS-WITH-RESERVATION` | conforme, conforme avec réserve |
| `FAIL` | non conforme |
| `ACCEPTED`, `ACCEPTED-WITH-RESERVATION` | accepté, accepté avec réserve |
| `RETURN`, `RETURNED` | renvoyé |
| `HELD`, `HELD-WITH-ACCEPTED-DIFFERENCE` | retenu, retenu avec écart accepté |
| `ESCALATED`, `BLOCKED`, `ABANDONED` | remonté, bloqué, abandonné |
| `CLOSED`, `STATE: CLOSED` | clos, trace close |
| `EXPLORATORY` | exploratoire |
| `DECISION-CHANGE`, `DECISION-INTENT` | décision changée, décision visée |
| `TRACE-LOCATOR` | emplacement de la trace |
| `EXIT-CONDITION` | condition de sortie |
| `PROOF-LIMIT` | limite de la preuve |

## Formes (catalogue)

Les identifiants du catalogue reçoivent un nom français. L’identifiant reste en commentaire, pour les contrôles et les anciens renvois.

| Code | Nom clair |
|---|---|
| `SUPPORT/FREE_FIELD` | champ libre |
| `SUPPORT/ARCHITECTED_FRAME` | cadre construit |
| `SUPPORT/OPERATIONAL_CANVAS` | toile d’opération |
| `SUPPORT/COLLECTION_PLINTH` | socle de collection |
| `GRID/MODULAR` | grille modulaire |
| `GRID/COLUMN` | grille en colonnes |
| `GRID/RADIAL` | grille radiale |
| `GRID/HIERARCHICAL` | grille hiérarchique |
| `GRID/BASELINE` | grille de ligne de base |
| `GRID/AXIAL` | grille axiale |
| `SCENE/INSTRUMENT` | scène instrument |
| `SCENE/EDITORIAL_FIELD` | champ éditorial |
| `SCENE/FRAMED_PRODUCT` | produit encadré |
| `SCENE/OPERATING_GRID` | grille d’opération |
| `SCENE/SPLIT_PROOF` | preuve partagée |
| `SCENE/PRODUCT_NARRATIVE` | récit du produit |
| `MODIFIER/FIELD_SWITCH` | bascule de champ |
| `MODIFIER/NAVIGATION_SHELL` | coque de navigation |
| `MODIFIER/PRINT_FIELD` | champ imprimé |
| `LAYER` | couche |
| axes de tension (`PROOF-POSITION`, `TEMPORALITY`…) | position de la preuve, temporalité… (liste complète au rangement) |
| routes d’objet et de micro (`USAGE_LEDGER`, `CONTROL_VALUE_TILE`, `MEDIA_ARCHIVE`…) | nommées au rangement, une par une |

## Reste à nommer

L’annexe générée ci-dessous liste les autres codes visibles qui reviennent au moins trois fois. Ils sont à nommer en phase 4, au moment de réécrire leur fichier.

<!-- annexe générée -->
### Annexe générée — codes restants (au moins 3 occurrences)

Produite par `ARCHI/outils/reste_a_nommer.py`. Les mots en capitales qui sont du texte ordinaire mis en relief (REQUIS, MODULE…) seront simplement écrits en minuscules.

`MODE` (25), `MICRO` (21), `REQUIS` (21), `PAR` (21), `MODULE` (21), `USER` (17), `TASK` (15), `EXPERT` (15), `ANCHOR-GENERATED` (12), `TRUTH` (12), `ARTIFACT` (11), `VERDICT` (11), `ISSUE` (10), `REFERENCES` (10), `ILLUSTRATIVE` (9), `METHOD` (8), `DECIDED` (8), `ANCHOR-OBSERVED` (8), `ANCHOR-PROVIDED` (8), `PERCEPTUAL` (8), `PROOF_PRODUCT_STAGE` (8), `ADOPTED` (8), `OBSERVATION` (7), `NEXT-ACTION` (7), `CHANGED` (7), `NAME` (7), `PILOT` (7), `DEPRECATED` (7), `ADAPTER` (7), `DURABLE` (7), `RETURN-DIRECTION` (6), `DIRECTION-STATUS` (6), `TECHNICAL` (6), `EDITORIAL_SELECTION` (6), `SYSTEM_DATA_MODULE` (6), `MECHANISM` (6), `PROFILE-DECISION` (6), `DOSSIER` (5), `SPECCED` (5), `CHECKING` (5), `COUNTERINDICATION` (5), `VERSION` (5), `CODE-NATIVE` (5), `CONFORMANCE-TARGET` (5), `PROOF-TYPE` (5), `QUERY_HEALTH` (5), `SEED` (5), `R2026-10-08-ACCES-MATIERE` (4), `SYSTEM-ESCALATION` (4), `LOST-IN-BUILD` (4), `PARTIALLY-HELD` (4), `DECISION-MODIFIED` (4), `DATE` (4), `AXES` (4), `ISO` (4), `AUTOMATED` (4), `FOCUS` (4), `COMPARISON_SPLIT` (4), `NAV_CONTEXT_CAPSULE` (4), `SANS-ASSET` (4), `DIGITAL_MEMORY` (4), `RESEARCH_BRIEF` (3), `EVALUATION_CASE` (3), `SELECT` (3), `CHEMIN` (3), `ORCHESTRATION_MAP` (3), `INTAKE` (3), `BUILDING` (3), `RECLASSIFIED` (3), `WHEN-USEFUL` (3), `WHY-NOW` (3), `BASIS` (3), `CAPABILITY-BASIS` (3), `REVIEW-DATE` (3), `REMAINING-RISK` (3), `FOURNI` (3), `HYBRIDE` (3), `MANUAL` (3), `OBSERVABLE-CONSEQUENCE` (3), `PRIMITIVES` (3), `TOKENS` (3), `NEXT-REVIEW` (3), `ENTITY_STATUS_RAIL` (3), `BRAND_GRAMMAR` (3), `PREUVE` (3), `YES` (3), `KEEP-IF` (3), `DIALS` (3), `EVIDENCE` (3), `TACTILE_VOLUME` (3)
