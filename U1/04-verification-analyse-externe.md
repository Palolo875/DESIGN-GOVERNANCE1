# Vérification de l'analyse « fichier par fichier » (SKILL, DIRECTION, ACTION, SAVOIR, BIBLIOTHEQUE, guides, schémas, scripts)

**Base :** commit `d90869c`, 2026-10-07. **Méthode :** chaque affirmation chiffrée ou vérifiable est recalculée par script sur le dépôt, ou lue à l'endroit cité. Les comptages stylistiques (négations, conditions, longueur des phrases) dépendent de la méthode : quand la mienne diffère, je donne les deux chiffres sans trancher.

**Verdicts :** ✅ confirmé · ≈ ordre de grandeur juste, chiffre ou formulation inexacts · ❌ faux · ◻ non vérifié.

## Synthèse

- **Environ 60 affirmations vérifiées.** Une large majorité est confirmée ou juste en ordre de grandeur. Cinq sont fausses et changent une piste : voir « Corrections qui changent les pistes ».
- **L'analyse rejoint le registre U1 sur l'essentiel** : charge par mode (C15, C16), absolus et piège de conformité absents du noyau (C17 à C19), limites du validateur (C11), compteur 27/30 (C23, désormais vérifié).
- **Elle apporte une douzaine de constats nouveaux et confirmés**, ajoutés au registre sous les numéros C26 à C37.
- **Elle n'a pas vu deux points du registre :** l'incomplétude de `CHARGE` (C13), qui fausse son tableau STANDARD, et le fait que les validateurs figent la formulation d'une règle sans contrôler les fichiers qui la reprennent (C03).

## Corrections qui changent les pistes

| # | Affirmation | Ce que montre la vérification | Conséquence pour la piste |
|---|---|---|---|
| 1 | « `GATE-A` ne se découpe pas : les sous-locators reposent sur des sous-titres, et `GATE-A` n'en a pas. » | ❌ `GATE-A` a quatre sous-titres `###`. `ACTION/GATE-A/Contrat` (1 521 o) et `ACTION/GATE-A/Contrôles` (7 536 o) se résolvent. Seul le découpage **par profil de surface** est impossible, car les profils sont des lignes de table. | Le découpage de GATE-A ne demande que des sous-titres de profil. Pour GATE-B, le découpage existe déjà. |
| 2 | « LITE charge plus que STANDARD » (71 Ko contre 67 Ko). | ≈ Chiffres justes (70,2 et 66,9 Ko), mais conclusion trompeuse. La ligne STANDARD de `CHARGE` ne cite aucune gate, alors que `RUN-STANDARD` exige « les Gates A et B ciblés » (C13). Avec ces gates, STANDARD lit **88,8 Ko**. | Le problème n'est pas que LITE soit trop lourd *par rapport à* STANDARD : `CHARGE` est incomplète. À corriger d'abord (décision D2). |
| 3 | Environ 37 Ko (35 %) de `DIRECTION` sont des « vues dérivées » à réduire à des pointeurs, dont `CHARGE` et `EXTERNAL-START`. | ❌ Mesuré : 26,5 Ko (25 %) pour la même liste de sections. Surtout, `CHARGE` contient trois blocs compilés dans le noyau (la table de chargement elle-même), et `EXTERNAL-START` contient les blocs noyau BRIEF et CONTENU (1,7 Ko normatifs). | Réduire ces sections à des pointeurs **casserait le noyau**. La piste ne vaut que pour le récapitulatif, l'architecture, la carte, la section 0 et le routage (≈ 11 Ko). |
| 4 | Piste « rendre le mode strict obligatoire pour tout verdict accepté ». | ❌ Le strict ne repère pas le contenu creux. Une carte dont les **42 champs libres valent « ok1…ok42 »** (thèse « ok9 », preuve « ok24 ») passe `--strict`, comme une ancre observée à URL inventée. Le strict ne refuse que les placeholders connus et les hôtes de démonstration. | Rendre le strict obligatoire est utile, mais il faut un contrôle de non-vacuité en plus (la piste 5 des scripts). Aucun contrôle textuel ne prouvera qu'une observation a eu lieu. |
| 5 | « L'absolu 1 se vérifie par déclaration, non par perception. » | ≈ À moitié. GATE-C C1, C2 et C3 correspondent exactement aux trois décisions de l'absolu 1, et « une capture réelle est nécessaire pour un jugement C » (`ACTION.md:921`). C'est donc une perception, mais une **auto-évaluation** par l'agent producteur, qui est le vrai problème. | La proposition de faire remonter la lecture légère sans le texte, idéalement par un second passage, reste juste. |

## Vérification détaillée

### SKILL.md

| Affirmation | Mesure | Verdict |
|---|---|---|
| Charges LITE 71, ITER 75, STANDARD 67, SYSTÈME 57, DIRECTION légère 100 Ko | 70,2 · 74,8 · 66,9 · 56,2 · 98,4 Ko | ✅ |
| DIRECTION, trace complète : 142 Ko | 134,5 Ko | ≈ (+5,5 %) |
| Noyau 43 Ko, environ 11 à 13k tokens | 43 201 o ; tokens non mesurés | ✅ / ◻ |
| Section 5 « Composition » : 13,8 Ko, 32 % | 13 833 o, 32,0 % de SKILL.md (33,6 % du bloc compilé) | ✅ |
| Le marquage de vérité (§6) arrive après la composition ; la sortie vient en dernier | Vrai. Mais §3 (PREMIER-OBJET) impose déjà `TRUTH/ILLUSTRATIVE` avant la composition. | ≈ |
| Les cinq absolus sont absents ; seul l'absolu 2 est cité | « absolu » : 1 occurrence ; « santé », « P0 », « Piège de conformité » : 0 | ✅ (le **contenu** de l'absolu 5 est pourtant largement présent : CNT-01, vérité ; voir la matrice U1) |
| Tags `[REQUIS PAR LE MODULE]`, `[VEILLE]` et `[MÉTHODE]` sans légende | 2, 2 et 1 occurrences ; aucune légende | ✅ |
| Le seul sous-locator essayé, `GATE-A/A1`, échoue | « locator inconnu » | ✅ (mais voir correction n°1) |
| Table de craft : 13 lignes de 70 à 130 mots, geste de 29 à 53 mots, « Surface » la plus dense | 13 lignes ; 62 à 104 mots ; geste 29 à 53 ; Surface = 53 | ✅ sauf la longueur des lignes (≈) |
| Sans la table, le noyau passerait sous 36 Ko | 36 436 o | ≈ (« environ 36 Ko ») |
| Phrases : médiane 12 mots, 90 % sous 24 | Ma méthode : médiane 14, 90e centile 31 | ◻ méthode différente |
| 48 routes distinctes, 73 codes en backticks | Même chiffre que ma pré-passe U1 (48 locators + 25 codes) | ✅ |
| Environ 60 conditions, 29 « ne…pas », 12 « jamais » | 77 à 88 conditions selon les mots retenus ; 32 « ne…pas » ; **12 « jamais »** | ≈ / ✅ |
| « Les notes de version disent qu'aucune mesure de ce coût n'existe » | Non retrouvé tel quel. `DIRECTION.md:865` dit que la règle de lecture « ne constitue pas une mesure de […] volume, de charge cognitive » | ≈ |

### DIRECTION

| Affirmation | Mesure | Verdict |
|---|---|---|
| 105 Ko, 868 lignes | 104 836 o, 867 lignes | ✅ |
| 15 blocs au noyau, 14 Ko, 32 % du noyau | 15 blocs, 13 954 o, 32,3 % de SKILL.md | ✅ |
| Absolus à 75 % du fichier (l. 631) | l. 631 / 867 = 73 % | ✅ |
| Seul l'absolu 2 est compilé ; manquent l'absolu 1 et la clause santé de l'absolu 5 | Confirmé | ✅ |
| Piège de conformité et P0 à P3 hors noyau | `DIRECTION.md:26` et `:108`, hors des blocs noyau | ✅ |
| Deux schémas d'organisation : routes nommées, puis sections 0 à 3 | `## 0.` à `## 3.` à partir de la ligne 721 | ✅ |
| `START/TREE` (3,5 Ko) contient la Protection de niveau | 3 429 o, contient la Protection de niveau | ✅ |
| ≈ 37 Ko (35 %) de vues dérivées | 26,5 Ko (25 %), dont des blocs noyau normatifs | ❌ (correction n°3) |
| 40 « ni…ni », 39 « ne crée… », 42 « jamais » | 47 · 29 · **42** | ≈ / ✅ |
| Creative Boot 12 champs, `DOMAIN-FRAME` 16, `VISUAL_TARGET` 11, premier objet 8 | 12 · 16 · 11 · 8 | ✅ |
| 14 codes de statut cités | 14 | ✅ |
| Question 3 de l'arbre : 55 mots | 38 mots | ❌ (le constat de négations imbriquées reste vrai) |

### ACTION

| Affirmation | Mesure | Verdict |
|---|---|---|
| 120 Ko, 1 085 lignes ; 5 Ko au noyau (4 blocs, 12 %) | 120 008 o, 1 084 lignes ; 4 blocs, 5 063 o, 11,7 % | ✅ |
| `GATE-B` découpable (B1 à B6, B1b) de 0,5 à 4,9 Ko | B1b avec l'atelier : 4,7 Ko ; B6 : 0,4 Ko | ✅ |
| `STATUS` à la ligne 146, après son premier usage | l. 146 | ✅ |
| `RUN_CARD` 18,7 Ko (16 %) | 18 711 o, 16 % | ✅ |
| 34 chemins JSON, une cinquantaine de mentions de validateur ou de schéma | 26 chemins pointés distincts ; 11 mentions dans la section | ≈ |
| 3,6 Ko de documentation de `check_render` | 3,8 Ko | ✅ |
| Cinq vues de l'enregistrement de run | Ligne de run, entrée minimale, HANDOFF, EXECUTION-SNAPSHOT, RUN_CARD | ✅ |
| ~155 codes, 12 gabarits, 24 tables | 150 codes distincts, 12 gabarits, 24 tables | ✅ |
| 38 « ne crée… », 34 « ni…ni », 33 « jamais » | 30 · 41 · **33** | ≈ / ✅ |
| 7,4 Ko de `GATE-B` ne concernent que DIRECTION en trace complète (B1b, atelier, B3, B5) | 7 363 o | ✅ |
| `RUN_CARD` avec snapshot ≈ 19 Ko ; pipeline avec preuves structurées ≈ 22 Ko | 18,7 Ko (le snapshot est dans la section) ; 19,8 Ko | ✅ / ≈ |

### SAVOIR

| Affirmation | Mesure | Verdict |
|---|---|---|
| 18 blocs au noyau, 17,9 Ko : 41 % du noyau pour 15 % du fichier | 18 blocs, 17 896 o, 41,4 % ; 15,1 % du fichier | ✅ |
| `SAVOIR/STATE` 13,9 Ko, dont 8,4 Ko (60 %) déjà dans le noyau ; `CRAFT` 18 % | 13 816 o, 8 386 o (61 %) ; CRAFT 18 % | ✅ |
| Phrases d'INTEGRITY absentes du noyau (« slop procédural », « théâtre », « modes d'échec », « non-récitation ») | 0 occurrence pour chacune | ✅ |
| INTEGRITY chargé seulement avant un verdict DIRECTION en trace complète | Aussi `[FORCÉ]` sur « Doute sur l'application d'une règle » (`DIRECTION.md:801`) | ≈ |
| « Premium » défini deux fois (5 termes, puis 6 avec la désirabilité) | `SAVOIR.md:104` (5 termes) et `:232` (6) | ✅ |
| « Marqueurs de vague » et « Carte des moyens » écrits deux fois, avec deux dates `[VEILLE]` | Marqueurs : l. 908 `[VEILLE 2026-10]` et l. 913 `[VEILLE 2026-09]` ✅. Carte : l. 918 et l. 923, **même date** 2026-09 | ≈ |
| `STYLE` 15,9 Ko, 8 profils en capitales | 15 788 o ; 8 profils (`RAW_BRUTALISM`, `QUIET_SYSTEM`…) | ✅ |
| Section vide `Preuve par médium` (l. 825) | Le titre est suivi d'une ligne vide puis d'un autre `###` | ✅ |
| « 6 rendus sur 6, même auteur » | « 6 rendus sur 6 » ✅ ; « même auteur » se rapporte au signal « 3 rendus sur 3 » | ≈ |
| Huit grilles de qualité parallèles | Existence vérifiée pour CFT-00, FIRST-OBJECT, Correction/Précision/Intention, Creative Quality Review, `creative_close` (5 champs, 4 questions), GATE-C et CFT-TARGETS ; « Jugement visuel situé » non vérifié | ✅ / ◻ |

### BIBLIOTHEQUE

| Affirmation | Mesure | Verdict |
|---|---|---|
| 76 Ko, 4,3 Ko au noyau (10 %) | 76 460 o ; 5 blocs, 4 289 o, 9,9 % | ✅ |
| 44 routes nommées | 41 identifiants structurels distincts | ≈ |
| Première route après ≈ 39 Ko | l. 328, à 38 979 o | ✅ |
| `SELECT` 11,5 Ko | 11 389 o (route servie) | ✅ |
| 8 gabarits ; `N/A-JUSTIFIED` 13 fois, dont 6 avec « pas une sortie de confort » | 8 · 13 · **1** occurrence littérale | ✅ / ≈ |
| Gouvernance 18 Ko (24 %) | EVOLUTION, COMPAT et GATE : 13,5 Ko, plus une partie de COMPONENTS | ≈ |
| « Non vérifié combien de routes sont adoptées » | `CHANGELOG.md:66` : toutes sont `SEED`, sans gain mesuré | ✅ (réponse : aucune) |

### Guides

| Affirmation | Mesure | Verdict |
|---|---|---|
| 48 routes citées dans READING_MAP, 0 échec | 48, 0 échec | ✅ |
| 110 tests de scripts (30 + 50 + 20 + 10), 26 cas navigateur | 30 · 50 · 20 · 10 ; 26 (vérifié en U1) | ✅ |
| Le README annonce 27 régressions, il y en a 30 | `README.md:177` : « 27 » ; 30 tests | ✅ **(C23 vérifié)** |
| QUICKSTART 26 Ko, 12 sections | 26 133 o, 14 titres `##` | ✅ / ≈ |
| READING_MAP 29 Ko ; 9 combinaisons ; C01 à C09 ≈ 10 Ko ; table des locators 25 lignes, 3,5 Ko lue par `read_route` | 29 138 o ; 9 ; 9 connexions, 12,5 Ko ; 25 lignes, 3 468 o, lue par `parse_route_rows` | ✅ / ≈ |
| CHANGELOG : 48 % de journal de révisions d'audit | « Autorité et maintenance » : 7 919 o (48 %), décisions F01 à F10 et R01 à R04 | ✅ |
| GLOSSAIRE : 57 termes, 16 contrôlés | 57 termes dans la table principale (mon premier comptage, 63, incluait la table d'exemples ; corrigé lors de la fiche U1b n°7) ; 16 dans `GLOSSARY_TERMS` | ✅ |
| `ORCHESTRATION_MAP` : 385 octets | 385 | ✅ |
| Le « tableau des réparations du jour » de l'exemple vélo ressemble à « fournées du jour », signalé en convergence | `SAVOIR.md:913` : « même objet central par brief (fournées du jour ; facture tamponnée) » ; `examples.md:36`, `:42` | ✅ (le risque reste une hypothèse) |
| À garder : « trois questions maximum posées **avant de construire** » | Contredit la décision §9.2 du plan (C01, C02) | ⚠ à arbitrer |

### Schémas

| Affirmation | Mesure | Verdict |
|---|---|---|
| `run_card.schema` : 138 propriétés, 26 énumérations, profondeur 5 | 143 · 27 · 5 | ≈ |
| Carte DIRECTION acceptée = 81 valeurs | 81 valeurs dans l'exemple | ✅ |
| L'exemple duplique `decision` et `decision_intent` | Identiques | ✅ |
| Écosystème RUN_CARD ≈ 180 Ko | 178 Ko (route, schéma, exemple, projection, validateur, fixtures de 66 Ko) | ✅ |
| 22 fixtures négatives, aucune sur le contenu creux | 22 ✅. Mais `invalid_critical_placeholder_protection` porte sur un placeholder, ce qui est un début de contrôle de contenu | ≈ |
| `domain_frame` impose 16 champs non vides | 16 requis, dont 8 listes avec `minItems` | ✅ |
| `research_brief` admet `depth: none` sans entrée | Énumération `none/targeted/deep` ; `entries` `minItems` 0 | ✅ |
| Le schéma `production_contracts` accepte `{}` mais le validateur le refuse | Pas de `required` ; validateur : « type indéterminé : document vide » | ✅ |
| Non strict : textes libres « ok1, ok2… » acceptés | 42 champs « okN » : **acceptés**, en non strict comme en strict | ✅ (et pire qu'annoncé) |
| `ACCEPTED` avec U et A en PASS et `observed: ["ok"]` accepté | Accepté (non strict) | ✅ |
| Ancre observée à URL inventée acceptée ; strict non testé | Strict testé : accepté | ✅ |
| `creative_direction_set` exige deux directions, alors que SAVOIR admet de ne pas matérialiser d'alternative | Pas de contradiction : le contrat est conditionnel ; sans alternative utile, il n'est pas produit (`ACTION.md:551`, `:626`) | ❌ |

### Scripts

| Affirmation | Mesure | Verdict |
|---|---|---|
| 392 Ko, soit 93 % des quatre sources | 392 016 o ; 93 % | ✅ |
| Outils 82 Ko, validateurs 210 Ko, tests 77 Ko, distribution 22 Ko | 82,1 · 210,4 · 77,0 · 22,3 Ko | ✅ |
| `validate_all` : code 0, 75 lignes `PASSED`, 135 s | 75 lignes `PASSED` ; durée non chronométrée | ✅ / ◻ |
| `check_render` : dix contrôles | 11 lignes de contrôle (dont « défilement horizontal interne ») | ≈ |
| 125 cas de test de la recette (48 + 51 + 26) | 125 | ✅ |
| L'ordre du noyau est une liste de 8 entrées dans `build_core.py` | `build_core.py:35-58` | ✅ |
| La projection de colonnes existe et n'est jamais utilisée | 42 blocs, colonnes toutes `None` ; `project()` l. 101 | ✅ |
| Garder trois colonnes de la table de craft fait gagner 2,2 Ko | 4e colonne : 2 162 o | ✅ |
| Le budget ne couvre que le noyau | `test_core_budget.py` et `check_budget` ; aucun budget par mode | ✅ |
| `validate_structure` : 52 Ko, 28 fonctions, 26 concepts, 9 renvois, 37 expressions retirées dont 34 exemptées seulement dans le CHANGELOG, 22 % de registres | 52 Ko, 27 fonctions, 26, 9 ; par ma regex 32 expressions dont 30 exemptées seulement dans le CHANGELOG ; registres 22 % | ✅ / ≈ |
| `GATE-A` ne se découpe pas | Faux | ❌ (correction n°1) |

## Avis sur les pistes

**À faire tôt (sûres, petites, vérifiables par les validateurs existants)**
1. Citer les sous-routes de GATE-B dans `CHARGE` (LITE : B2 et B6) **et** compléter les lignes STANDARD et DIRECTION (C13). LITE passe de 70,2 à 61,4 Ko.
2. Ajouter au noyau le piège de conformité, l'énoncé court des cinq absolus (avec la clause santé) et P0 à P3 (≈ +1,5 Ko). Le noyau a 2,8 Ko de marge (43 201 / 46 000).
3. Réordonner le noyau dans `build_core.py` (liste de 8 entrées) : classer, absolus, brief et vérité, structure, composition, boucle, sortie.
4. Dédupliquer « Marqueurs de vague » et « Carte des moyens » dans SAVOIR, combler ou retirer la section vide `Preuve par médium`, corriger 27 → 30.
5. Ajouter un budget par mode à `test_core_budget` (somme du noyau et des routes de chaque ligne de `CHARGE`), qui rend la charge visible et contrôlée.

**À tester dans l'A/B, et non à décider sur papier**
- Table de craft à 3 colonnes (−2,2 Ko) ou sortie du noyau (−6,8 Ko).
- `STYLE` avec ou sans les 8 profils nommés ; `COMPAT` avec ou sans matrice ; mesurer la reprise des noms de scène et de l'objet « … du jour ».
- Changer l'objet de l'exemple vélo : à décider après mesure, car l'effet n'est pas démontré.

**À reformuler**
- « Réduire les vues dérivées de DIRECTION à des pointeurs » : seulement le récapitulatif, l'architecture, la carte, la section 0 et le routage (≈ 11 Ko). `CHARGE` et `EXTERNAL-START` portent des blocs du noyau.
- « Strict obligatoire » : oui, mais avec un contrôle de non-vacuité ciblé sur `proof.observed`, `method` et `creative_close` (longueur minimale, refus de « ok », de « okN » et de répétitions), en sachant qu'il ne prouvera jamais l'observation.
- « Fusionner QUICKSTART et READING_MAP » : d'abord sortir la table des locators dans un fichier machine. L'auteur le dit lui-même.

**À écarter**
- La contradiction supposée sur `creative_direction_set` : le contrat est conditionnel.
