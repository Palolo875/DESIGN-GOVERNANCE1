# Fiche — scripts/ (17 fichiers), .github/workflows/validate.yml, schemas/ (8 fichiers + 25 fixtures)

Commit audité : `9681d4e`. Lecture seule : rien n'a été modifié dans le dépôt (voir « Méthode » en fin de fiche, y compris ce qui n'a pas été lancé).
Les lignes citées sont celles du commit audité. Les grilles de la charte s'appliquent avec le remplacement demandé : F5, F6 et F10 deviennent **utilité, simplicité, messages**.

## Identité

**Rôle actuel.** Les scripts font cinq métiers mêlés : lire le savoir par route (`read_route.py`), vérifier un rendu HTML (`check_render.py`), construire la skill à partir des sources (`build_core.py`), contrôler les textes et les cartes de run (six validateurs), fabriquer et livrer les archives (`build_distributions.sh`, `preparer_livraison.py`, manifeste). `schemas/` sert la sérialisation machine des artefacts de gouvernance. La CI ne lance qu'une commande : `validate_all.py --require-browser`.

**Public réel.** Sur 17 fichiers de scripts, deux servent un public de la charte : `read_route.py` (agent, puis designer et équipe via `--sommaire`) et `check_render.py` (agent, designer, équipe). `build_core.py` sert l'agent sans qu'il le voie : il fabrique la skill. Tout le reste sert le mainteneur du système, c'est-à-dire le propriétaire. Aucun script n'est destiné au débutant.

**Public visé par la charte.** Agent (lecture par route, vérification du rendu), équipe (traces, contrats), mainteneur. Le débutant et le designer n'ont pas à ouvrir un seul script.

**Taille (mesures.md).** `scripts/` = 7 334 lignes. Répartition par fonction, calculée sur les `wc -l` :

| Bloc | Fichiers | Lignes | Part |
|---|---|---:|---:|
| Chemin design et produit à garder | read_route, check_render, build_core + leurs 3 tests | 2 488 | 34 % |
| Validation des textes (structure et verrous de phrases) | validate_structure, validate_reading_map, validate_design_governance, validate_all, test_audit_regressions | 2 325 | 32 % |
| Gouvernance | validate_run_card, validate_contracts | 1 570 | 21 % |
| Livraison | build_distributions.sh, preparer_livraison + test, package_manifest.json | 951 | 13 % |

`schemas/` = 105 840 octets : 5 schémas (15 460 + 3 359 + 2 724 + 2 178 octets, plus l'exemple de carte 5 457), 3 exemples (3 026 + 5 647 + 1 819), 25 fixtures (66 170 octets, soit 63 % du dossier).

## Verdicts de la grille

| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger (mineur) | `validate_design_governance.py:1-5` se décrit en une ligne (« validation légère ») alors qu'il porte 11 familles de contrôles et un nom trompeur (il valide le paquet, pas la gouvernance) ; `test_audit_regressions.py:2` se définit par un audit passé (« témoins de l'audit simulé ») et mélange liens, capacités, façades, hôtes stricts. Les autres docstrings sont précises. |
| F2 Public | à corriger | Aucun script ne nomme son public. Seuls 2 fichiers sur 17 servent un public de la charte (voir Identité). Les messages ne distinguent pas l'agent, le designer et le mainteneur. |
| F3 Structure | à corriger | `validate_run_card.py` : 1 084 lignes, dont environ 170 lignes de données de test (`FIXTURE_TABLE` l.688, 87 `UNIT_CASES` l.747-842, `STRICT_ADMITTED` l.844) mêlées au validateur. `validate_structure.py` : 811 lignes, dont environ 230 lignes de tables de verrous (l.55-286). `check_render.py` : environ 230 lignes de JavaScript dans des chaînes Python (l.46-275, 38 % du fichier). |
| F4 Une seule fois | à corriger (important) | Moteur « sous-ensemble de JSON Schema » écrit deux fois : `validate_contracts.py:33,79,102,189,350` et `validate_run_card.py:52,142,212,858,980` (plus `_unique_keys` en troisième copie, `validate_design_governance.py:24`). Liste des fichiers du paquet en trois lieux : `package_manifest.json` (deux listes presque identiques), 41 `cp -a` de `build_distributions.sh:52-97`, `FIXTURE_TABLE` de `validate_run_card.py:~690`. README Local écrit en dur dans un script shell (`build_distributions.sh:98-151`). |
| Utilité | à corriger (bloquant pour les phases de langue) | Environ la moitié des contrôles des validateurs exigent une formulation exacte du texte (voir plus bas). Une synonymie suffit à casser : remplacer « irréversible ou coûteuse » par « irréversible ou onéreuse » dans une copie fait échouer `validate_structure.py` deux fois (ACTION.md et SKILL.md, règle `validate_structure.py:203`). Tant que ces verrous existent, la phase de langue ne peut pas réécrire le texte. |
| Simplicité | à corriger | Un contrôle de phrase ne protège pas ce qu'il nomme, il protège une chaîne. Les mêmes faits sont vérifiés plusieurs fois : par un validateur de structure, par une façade LCF, par un test de mutation (`test_audit_regressions.py`), parfois par `check_craft_regressions` (`validate_all.py:45-100`). La validation complète lance `test_check_render.py` jusqu'à trois fois (une fois en direct, une fois dans chaque `validate_all.py` de Local appelé par `build_distributions.sh:230`, qui est lancé deux fois par `validate_all.py:186,190`). Durée complète non mesurée (voir Méthode). |
| Messages | à corriger (important) | Bannières en anglais, détail en français (`READING MAP VALIDATION FAILED`, `CORE BUDGET PASSED`, `ROUTE READ FAILED`) ; docstrings de `read_route.py:2` et `validate_contracts.py:2` en anglais, les autres en français. Voir défauts 8 et 9. |
| F7 Liens | conforme | `validate_design_governance.check_links` (l.177) contrôle liens, fichiers hors paquet et fragments d'ancres, hors blocs de code ; testé par 11 cas (`test_audit_regressions.py`). Le build Local refait un contrôle de liens et de chemins entre accents graves (`build_distributions.sh:~205-225`). |
| F8 Longueur | à corriger (mineur) | Quatre fichiers dépassent 750 lignes (run_card 1 084, structure 811, read_route 770, reading_map 750). Aucun n'est découpé par rôle. |
| F9 Limites | conforme, sauf une redite | `check_render.py:569` imprime à chaque exécution un paragraphe de limites d'environ 1 100 caractères, déjà dit dans la docstring (l.2-20), `ACTION.md:805` et `README.md:175`. Les autres scripts disent leurs limites une fois (« ne prouve pas l'absence du savoir », `read_route.py`). |
| F11 Vestiges | à corriger (mineur) | Environ 90 codes d'audits passés dans le code et les messages (`C11`, `C8 O-1`, `E1 O-1`, `INV-C1-1`, `F-RRT-001`) : `read_route.py:108,238`, `build_distributions.sh:175,237,247`, `validate_reading_map.py:645` (« DIRECTION 72 », « DIRECTION 55 » : numéros de ligne périmés dans un libellé), `validate_run_card.py:910` (« témoin C13 »). Les 112 cas de test portent des identifiants opaques (`C19-2`, `B2-9b`). |
| F12 Dépendances | à corriger | Le couplage texte-script n'est lisible nulle part : les verrous citent des chaînes, pas la règle qu'ils protègent. Seuls `mesures.json` et ce rapport en donnent la carte (voir plus bas). |

## Sections

### Les scripts, un par ligne

| Fichier (lignes) | Ce qu'il fait | Appelé par | Public | Famille | Disposition proposée |
|---|---|---|---|---|---|
| `read_route.py` (770) | Résout un identifiant de route (`DIRECTION/START`) et n'affiche que son bloc ; `--trouver` cherche un terme (mots entiers, alias, partiel) et classe les routes ; `--sommaire` liste les routes ; `--connexions` expose l'index de connexions ; replie les blocs déjà compilés dans le noyau. | Agent (`SKILL.md:29-31`), humain, les validateurs (import), `build_core` (import), `validate_all` (test de repérage `validate_all.py:130`) | Agent ; designer et équipe via `--sommaire` | méta (lecture), indispensable au chemin design | **Garder.** Détacher `--connexions` et le lien à la révision du CHANGELOG (l.142-222, environ 80 lignes) vers le module de maintenance, ou le retirer avec les connexions de READING_MAP (décision liée à cette fiche). Sortir `ALIAS_GROUPS` (l.434-474, 38 groupes) en fichier de données. Voir « À garder absolument ». |
| `check_render.py` (607) | Ouvre une page HTML dans Chromium aux largeurs 390, 768 et 1440 px et rend onze contrôles objectivables (débordement, contraste, nom accessible, cibles, alt/lang/titre, h1, clavier et focus, mouvement réduit, objet de preuve) ; écrit captures et JSON de provenance. | Agent (`ACTION.md:725,805`, `SKILL.md`), humain, `test_check_render.py` | Agent, designer, équipe | produit (vérification visuelle) | **Garder** (charte §4). Réécrire les messages en langage clair (statuts, bannière), extraire le JavaScript dans un fichier. Voir « À garder absolument ». |
| `build_core.py` (170) | Compile 42 blocs « noyau » des sources (SAVOIR 18, DIRECTION 15, BIBLIOTHEQUE 5, ACTION 4) dans `SKILL.md` et refuse un fichier de plus de 46 000 octets. | Humain, `validate_all`, `build_distributions`, `preparer_livraison`, `validate_structure` (import) | Mainteneur ; l'agent en reçoit le résultat | méta (construction), protège la charge de l'agent | **Garder** (charte §4). Le registre `NOYAU` (l.38-70) sera réécrit en phase 5. Marge actuelle : 44 559 sur 46 000 octets (96,9 %), à surveiller avant toute réécriture qui allonge. |
| `test_core_budget.py` (90) | 10 tests sur le budget d'octets de `build_core`. | `validate_all` | Mainteneur | méta | **Fusionner** avec un fichier de tests du build et réduire : trois des dix tests vérifient la même comparaison (45 999, 46 000, 46 001). |
| `validate_structure.py` (811) | « Gardes de propriété » : 26 concepts balisés à un seul lieu, 9 renvois atteignables, 37 vocabulaires retirés, 65 résumés fidèles, glossaire, entrée humaine, noyau compilé, chargement, en-tête YAML de la skill, façades. | `validate_all`, `build_distributions`, CI | Mainteneur | méta ; 78 % de verrous de phrases | **Simplifier** fortement : garder les 51 contrôles de structure (voir plus bas), retirer les verrous de phrases à mesure que les textes sont réécrits, après leur entrée dans la table de correspondance (voir « Savoir à protéger »). |
| `validate_reading_map.py` (750) | Contrôle la carte de lecture (locators, propriétaires, liens, sujets, connexions) et 56 « conditions de façade » (LCF-01 à LCF-56). | `validate_all`, `build_distributions`, `test_audit_regressions` | Mainteneur | méta ; 24 LCF touchent la gouvernance | **Simplifier et scinder.** Les 16 contrôles de carte rejoignent le validateur de structure. Les 24 LCF de gouvernance partent dans le module. Les 32 LCF de phrases et les 15 en-têtes exigés par `REQUIRED` (l.29) sont retirés progressivement. |
| `validate_all.py` (198) | Chaîne tout : compilation, 6 validateurs, 5 suites de tests, régressions de mutation, test de repérage, scénarios de la CLI, double build et reproductibilité. | CI (`validate.yml:28`), humain, `preparer_livraison`, `build_distributions` (copie Local) | Mainteneur, CI | méta | **Simplifier.** Ne garder que l'orchestration : sortir `check_craft_regressions` (l.45-100) et les 11 scénarios CLI de gouvernance (l.139-178) vers leurs propriétaires ; ne plus lancer le build deux fois dans la CI. Ne pas le lancer « en lecture » : il écrit `dist/`, `.build/` et les deux zip (l.186-190). |
| `validate_design_governance.py` (353) | Contrôle l'inventaire du paquet (manifeste, version, fichiers inattendus, liens symboliques), les liens et ancres, les valeurs structurées (`STATE`, `VERDICT`…), le contrat de cycle de vie, la mention « expérimentation maintenue ». | `validate_all`, `build_distributions`, humain (`README.md:~178`) | Mainteneur | méta ; 11 contrôles de structure, 25 de phrases, 6 de gouvernance | **Renommer** (`validate_package`) et **simplifier** : garder manifeste, fichiers, liens et ancres ; retirer les 25 contrôles de phrases (l.242-310). |
| `validate_run_card.py` (1 084) | Valide la carte de run (RUN_CARD) contre son schéma et ses invariants métier (verdicts, axes, réserves, ancres, B1b, système) ; profil `--strict` ; suite de 87 cas et 25 fixtures. | Humain et agent (`--strict chemin`), `validate_all`, `build_distributions`, tests | Équipe, auditeur ; agent producteur | gouvernance | **Déplacer** vers le module de gouvernance. Séparer en trois : moteur de schéma (partagé), invariants, cas de test. |
| `validate_contracts.py` (486) | Valide `DOMAIN_FRAME`, `RESEARCH_BRIEF` et les contrats de production ; 25 cas unitaires. | Humain (`QUICKSTART.md:108`, `README.md:184`), `validate_all`, `build_distributions` | Équipe | gouvernance | **Déplacer** vers le module et **fusionner** son moteur de schéma avec celui de `validate_run_card`. |
| `test_read_route.py` (444) | 66 tests du lecteur : blocs de code, recherche, alias, identifiants structurels, connexions, CLI. | `validate_all` | Mainteneur | méta | **Garder.** Réduire la dépendance au vrai corpus (`every_alias_group_reaches_sources`, `ActivationTests`). |
| `test_check_render.py` (407) | 129 cas : A (50, interprétation sans navigateur), B (28, pages piège dans Chromium), C (51, JavaScript sur DOM simulés avec Node). | `validate_all` | Mainteneur | produit | **Garder.** `--skip-browser` existe déjà. |
| `test_audit_regressions.py` (213) | 30 tests de natures différentes : 10 mutations de façade (LCF-51 à 56), 11 de liens, 6 de capacités, 1 d'hôtes stricts, 2 de relais du noyau. | `validate_all` | Mainteneur | méta | **Retirer en tant que fichier** : répartir chaque classe chez son propriétaire (liens, run_card, structure) ; les 10 tests de façade disparaissent avec les LCF. |
| `test_preparer_livraison.py` (282) | 21 tests de la préparation de livraison et de la restauration à l'octet près. | `validate_all` (si présent) | Mainteneur | méta | Suit le sort de `preparer_livraison.py`. |
| `preparer_livraison.py` (212) | Compile le noyau, lance `validate_all`, option `--markdown` : deux copies de lecture en un seul `.md` avec script de restauration et vérification à l'octet. | Humain (README, CHANGELOG) | Mainteneur, équipe | méta | **Simplifier** : le cœur tient en deux commandes (compiler, valider). La copie Markdown (l.40-80, 100-155) est une fonction à part : la garder en option ou la retirer, décision du propriétaire. |
| `build_distributions.sh` (318) | Assemble les distributions GitHub et Local, réécrit les chemins du Local, vérifie le manifeste, archive de façon déterministe, publie de façon transactionnelle. | `validate_all` (deux fois), humain | Mainteneur | méta | **Simplifier**, en fonction de la décision sur l'export Local (défaut 12). Sortir le README Local en fichier source ; générer la liste de fichiers depuis le manifeste. Ne pas lancer. |
| `package_manifest.json` (139) | Deux listes de chemins (GitHub 69, Local 63) et la version. | `validate_design_governance`, `build_distributions` | Mainteneur | méta | **Fusionner** en une liste et une règle de renommage pour Local, ou la générer. |
| `.github/workflows/validate.yml` (30) | Sur chaque push et chaque PR : installe Python 3.11, Playwright 1.56.0 et Chromium, lance `validate_all.py --require-browser`. Actions épinglées par SHA. | GitHub | Mainteneur, équipe | méta | **Garder, simplifier** : un seul job fait échouer tout si Chromium manque ; séparer un job documents (Python seul) d'un job navigateur ; filtrer par chemin. |

### schemas/

| Fichier (taille) | Ce qu'il apporte | Public | Famille | Disposition |
|---|---|---|---|---|
| `run_card.schema.json` (15 460 o) | Format JSON de la carte de run : mode, risque, direction, ancres, preuve, clôture (état, verdict, axes V/U/A/T, réserves, B1b). | Équipe, auditeur ; agent producteur en trace complète | gouvernance | Module de gouvernance |
| `run_card.example.json` (5 457 o) | Modèle canonique d'une carte `DIRECTION` close, et base de 87 cas de test. Cité par `ACTION.md`, `examples.md`, `machine_projection.md`, `validate_reading_map.py` (LCF-31). | Équipe, agent | gouvernance | Module de gouvernance |
| `domain_frame.schema.json` (2 724 o) + exemple (3 026 o) | Cadre de domaine avant de concevoir : public, tâches, risques, plan de preuve. | Agent producteur, équipe | design en amont, forme de gouvernance | Module de gouvernance ; garder le gabarit lisible dans `DIRECTION.md:246` (qui dit « reprend exactement » le schéma) |
| `research_brief.schema.json` (2 178 o) + exemple (1 819 o) | Trace d'une recherche (question, sources, ce qui a changé). `SAVOIR.md:586` la dit déjà « facultative ». | Équipe | gouvernance | Module de gouvernance |
| `production_contracts.schema.json` (3 359 o) + exemple (5 647 o) | Trois contrats au choix : comparaison de directions, pack de réalité UI/UX, cas d'évaluation. | Équipe | mixte : direction (design), UI/UX (produit), évaluation (méta) | Module de gouvernance ; si le propriétaire veut un contrôle de la comparaison de directions dans le chemin design, c'est le seul contrat candidat à rester |
| `fixtures/` (25 fichiers, 66 170 o) | 3 cartes valides, 22 invalides. | Mainteneur | gouvernance (test) | Voir défaut 5 : réduire à 7 |

## Les six validateurs : trois groupes de contrôles

**Méthode de comptage.** Je compte les contrôles déclarés dans le code (une entrée de table ou un `raise` sur une règle distincte), pas les occurrences de `mesures.json`. Cette mesure compte « chaîne littérale × document » : elle compte une fois par document qui contient la chaîne. J'ai refait le calcul (`ast`, chaînes de 24 caractères et plus présentes dans un document) : elle donne bien 155, 109 et 84, mais :

- `validate_structure.py` = **90** chaînes distinctes pour 155 occurrences ;
- `validate_reading_map.py` = **70** pour 109 ;
- `validate_all.py` = **26** pour 84, dont **24 sont des chemins de fichier ou de commande** (`scripts/validate_run_card.py` compté 6 fois, `schemas/run_card.example.json` 3 fois…). Seules **deux** chaînes sont des phrases du texte : `validate_all.py:76` (« vocabulaire perceptuel de `SAVOIR/STATE` ») et `:82` (« Les gestes proposés sont des points de départ, pas une liste fermée »), plus le terme de repérage « Cohérence de rayon » (l.130). La ligne « 84 » surestime donc fortement `validate_all` ; le total de 499 de la mesure tous scripts confondus sur-compte aussi.

**Mon décompte (estimation par lecture, à ±10 %).**

| Validateur | Structure | Phrases verrouillées | Gouvernance | Total |
|---|---:|---:|---:|---:|
| `validate_structure.py` | 51 | 176 | 0 | 227 |
| `validate_reading_map.py` | 16 | 48 | 24 | 88 |
| `validate_all.py` | 16 | 3 | 11 | 30 |
| `validate_design_governance.py` | 11 | 25 | 6 | 42 |
| `validate_run_card.py` | 10 | 0 | 60 invariants (+ 87 cas, 25 fixtures) | 70 |
| `validate_contracts.py` | 8 | 0 | 21 (+ 25 cas) | 29 |
| **Ensemble** | **112 (≈ 23 %)** | **252 (≈ 51 %)** | **122 (≈ 25 %)** | **≈ 490** |

La moitié des contrôles déclarés exigent donc une formulation exacte. Cela correspond à l'ordre de grandeur de la mesure (environ 500), mais pas à la même quantité.

### Groupe 1 : structure (protège quelque chose d'utile)

- Concepts à un seul lieu, balisés d'une balise invisible, avec un bloc d'au moins 12 mots (26 entrées, `validate_structure.py:55-83`, contrôle `check_concepts:404`). Une reformulation ne les casse pas. C'est le bon mécanisme, mais le registre est à réduire.
- Renvois atteignables : une route cite un locator dont le bloc contient le concept (9 entrées, `validate_structure.py:85-95`, `check_references:441`).
- Noyau : balises appariées, uniques, dans les sources ; la skill est identique à sa compilation ; budget en octets (`check_noyau:522-560`, `build_core.py:49`).
- En-tête YAML de la skill lisible, `name` exact (`check_skill_header:680-698`).
- Carte de lecture : locators uniques, propriétaires cohérents, titres résolus, locators cités atteignables (`validate_reading_map.py:55-104`), sujets traités par leur route (`:133`).
- Inventaire du paquet et liens (`validate_design_governance.py:75-143,177-197`) : fichier attendu ou inattendu, liens symboliques, lien cassé, fragment introuvable.
- Pas de numéro de ligne dans un message du validateur (`validate_structure.py:352`).
- Lignes de table dupliquées (`:499`), ordre rôle > posture > récapitulatif dans DIRECTION (`:606`, 3 entrées).
- Pour `validate_run_card` et `validate_contracts` : le moteur de schéma, la clé répétée, le mot-clé non géré, les témoins négatifs (`validate_run_card.py:52-125,142,980,1002`).

### Groupe 2 : phrases verrouillées (exigent une formulation exacte)

- **Résumés fidèles** (`FIDELITY`, 65 entrées, `validate_structure.py:201-284`). Exemple l.203 : tout paragraphe qui parle de checkpoint avant le build doit contenir « irréversible ou coûteuse ».
- **Vocabulaire retiré** (`RETIRED`, 37 entrées, `:98-172`). Exemple l.107 : le motif `anti-directions?` est interdit partout hors CHANGELOG.
- **Entrée humaine** (`QUESTIONS`, `:286`) : les quatre intertitres exacts « **1. Que demander ?** » à « **4. Comment poursuivre ?** ». Je l'ai vérifié sur une copie : renommer le quatrième intertitre en « Et ensuite ? » produit `[ENT-01] question absente`. Cela gèle la page d'entrée que la charte veut réécrire (S1, S3).
- **Plancher du noyau** (`CORE_FLOOR`, `:616-628`, 12 entrées). Exemple l.621 : la skill compilée doit contenir « Conçois une palette par rôles ».
- **Lignes de façade** (`ROW_NEEDLES`, `:718-729`, 10 entrées) et glossaire (16 termes, `:361`), préambule de BIBLIOTHEQUE, chargement (CHG-01 à 08), déclencheur UI/UX.
- **Conditions de façade** (LCF non-gouvernance, 32 entrées, `validate_reading_map.py:620-705`). Exemple LCF-44 (`:490,510`) : l'ordre « contenu réel … marque … asset principal … destination » dans trois textes. LCF-46 (`:491-540`) interdit dix-sept mots de tendance (violet, Inter, beige, crème, halo, ASCII…) hors des lignes `[VEILLE 20…]`.
- **Positions de paquet** (`validate_design_governance.py:242-310`) : « Les cinq fichiers suivants sont les **seules sources normatives** de V1 » (l.245) et « expérimentation maintenue » dans neuf fichiers (l.295).
- **Mutations de `validate_all`** (`validate_all.py:76,82`).

### Groupe 3 : gouvernance (valide le format des cartes et des contrats)

- Carte de run : verdict accepté exige preuve observée, provenance, limitation, capacité attestée (`validate_run_card.py:297-348`) ; risque critique exige protection structurée et exclut LITE et ITER (`:230-266`) ; FAIL-ASSUMED exige exception et preuve d'échec (`:268`) ; B1b (`:388`) ; DIRECTION exige ancre, calibration, `creative_close` (`:413-486`) ; SYSTÈME exige paquet (`:368`).
- Contrats : couverture risque-contrôle (`validate_contracts.py:193`), dates ISO de sources (`:125,219`), directions distinctes (`:240`), couverture UI/UX (`:261`).
- Façades de gouvernance : 24 LCF qui vérifient que les textes disent la même chose du statut, du verdict, du `DECISION-CHANGE`, de la réserve, de la clôture (LCF-11, 12, 13, 14, 20, 22, 23, 26, 28, 32 à 38, 40 à 42, 52, 53, 56, C1, C2). **Les meilleurs de la liste** : LCF-26 (`:334`) et LCF-41 (`:457`) comparent les documents au schéma, qui est la vraie source de vérité.
- Valeurs structurées autorisées dans les `.md` (`STATE`, `ISSUE`, `VERDICT`, `DIRECTION-STATUS`) : `validate_design_governance.py:215-240`.

## Schémas : à quoi ils servent, pour qui, et que deviennent-ils

**À quoi.** Ils donnent un format vérifiable par machine à cinq documents que l'agent écrit : la carte de run (`ACTION/RUN_CARD`), le cadre de domaine, le brief de recherche et les contrats de production. Ils ne contrôlent que la forme et quelques invariants : `ACTION.md:404` le dit (« la projection … respecte les contrôles exécutés »). Ils n'attestent ni l'usage ni la qualité visuelle.

**Pour qui.** L'équipe qui veut une trace persistante, partagée ou auditée, et l'agent qui la produit. Le débutant et le designer ne les lisent pas ; l'agent n'en produit pas en trace légère (`ACTION.md:53`), c'est-à-dire pour la petite correction et la page ordinaire.

**Si la gouvernance devient facultative.**

1. Les 8 fichiers de schémas et d'exemples, les 25 fixtures, `validate_run_card.py`, `validate_contracts.py` et les 24 LCF de gouvernance sortent du cœur et vivent dans un module (par exemple `gouvernance/`), livré à part ou activé à la demande.
2. Le cœur ne perd rien du chemin design. Mais **six endroits supposent aujourd'hui que le module est là** et casseraient : `validate_reading_map.py` (`SCHEMA`, LCF-26 et LCF-41), `test_audit_regressions.py` (imports de `validate_run_card` en tête de fichier), `validate_all.py:139-178` (11 scénarios CLI), `validate_design_governance.py` (le manifeste liste les 25 fixtures), `README.md:106,182-184`, `QUICKSTART.md:108`. Les règles qui y renvoient dans les documents (`DIRECTION.md:246`, `SAVOIR.md:586`, `ACTION.md:404,543,618`, `examples.md`, `machine_projection.md`) doivent devenir conditionnelles.
3. Le gabarit du cadre de domaine doit rester lisible dans le texte (`DIRECTION.md:246`), pour l'agent sans module. À décider : `domain_frame` est une préparation de design écrite sous forme de gouvernance ; la comparaison de directions de `production_contracts` est du design. Je recommande de tout déplacer et de ne garder dans le cœur que les gabarits en prose.

## À garder absolument

### `read_route.py`

- **Résoudre un locator vers son seul bloc** : `resolve` (l.224-292), `served_lines`/`extract` (l.311-338) qui excluent les sous-blocs porteurs de leur propre locator. C'est le contrat qui borne la charge de l'agent (S2) et que tout valideur réutilise comme seul résolveur.
- **Ignorer les titres dans les blocs de code** : `non_code_lines` (l.92) et `headings` (l.107) ; 8 tests (`test_read_route.py:18-48`).
- **Refuser sans deviner** : locator inconnu, ambigu, dupliqué, absent, identifiant structurel dans un bloc de code (`_unique` l.135, `resolve`), avec code de sortie non nul.
- **Rechercher un terme sans fausse certitude** : mots entiers puis alias puis partiel puis mots séparés (`search` l.494), classement des routes (`rank_routes` l.539), `ALIAS_GROUPS` (l.434-474), et la phrase « ce résultat ne prouve pas l’absence du savoir » (l.719). Ce sont les supports de la trouvabilité (S4).
- **`--sommaire`** (`summary_rows` l.560, `outline` l.594) : la navigation (S5).
- **Replier ce que le noyau contient déjà** : `fold_core` (l.368), `--complet`. À adapter en phase 5 avec le registre `NOYAU`.
- **Garde UTF-8 nommée** avant lecture (`non_utf8` l.295).
- **Les identifiants structurels** (`SUPPORT`, `GRID`, `SCENE`, `OBJECT`, `MICRO`, `MODIFIER`, `LAYER` → BIBLIOTHEQUE, l.39-41) : route vers le savoir de formes.
- À adapter, pas à perdre : `PREFIXES` en dur (l.38), la table « Locators principaux » (l.56), « Carte des sujets » (l.517) et la forme `## DIRECTION/START` des titres. Si ces conventions changent, `read_route.py` change dans le même lot.

### `check_render.py`

- **Ne jamais simuler une preuve** : sans Playwright ou sans Chromium, sortie `NOT-VERIFIED` et code 2 (l.536-566) ; un contrôle qui ne peut pas conclure rend une réserve, jamais un succès.
- **Rendu réel, ordinateur et mobile** : largeurs 390, 768 et 1440 px par défaut (l.590), défilement complet pour révéler le contenu chargé au défilement (l.318-324), état initial puis états cliqués (`--click`).
- **Les contrôles objectivables** (`interpret` l.383-530) : débordement horizontal et défilement interne, erreurs JavaScript, contraste de texte sur fond uni (seuils WCAG 2.2 AA, textes non mesurables déclarés en réserve), nom accessible (candidats DOM), cibles de 24 px avec règle d'espacement, alt/lang/titre, un seul h1, parcours clavier et changement de style au focus, mouvement réduit, objet de preuve au premier écran.
- **Requêtes externes bloquées par défaut** (`--allow-external`) : le contrôle reste local et reproductible, et la sortie le dit (compteur de requêtes bloquées).
- **Captures pleines pages, une par largeur, sans écraser** (`capture_paths` l.532, refus l.546) : c'est ce qui garde la paire avant/après.
- **Provenance** (`artifact_locator`, `artifact_version`, `method`, `observed_at`, l.559-561) et JSON (`--json`) : utile à l'équipe ; à rendre facultative dans l'affichage.
- **Aucun verdict global** : la recette « ne valide ni la direction visuelle, ni l'utilisabilité » (docstring l.2-8). À conserver, mais à dire une fois, pas à chaque exécution.
- **Ses tests** (`test_check_render.py`, 129 cas) : ils sont la preuve que la recette dit vrai sur des cas connus.
- À réécrire (forme) : la bannière `Recette AUTOMATED (GATE-A)` et les statuts `[RETURN]`, `[PASS-WITH-RESERVATION]`, `[NOT-VERIFIED]` sont des codes internes ; un designer ou une équipe a besoin de « À corriger », « À vérifier à la main », « Conforme », « Non vérifié ».

## Défauts

| N° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| 1 | convergence (verrous de phrases) | bloquant pour les phases de langue | ≈ 252 contrôles exigent une formulation exacte. Synonyme testé sur copie : « irréversible ou coûteuse » → « irréversible ou onéreuse » donne 2 échecs (`validate_structure.py:203`). Le quatrième intertitre de l'entrée est verrouillé (`:286`). | Entrer chaque verrou dans la table de correspondance (S7), puis le retirer dans le lot qui réécrit sa phrase ; garder seulement les verrous de structure. Ne rien supprimer avant : chaque verrou date d'une décision. |
| 2 | répétition | important | Même fait vérifié trois fois : `FIDELITY` (`validate_structure.py:203`), `ROW_NEEDLES`/`CORE_FLOOR`, LCF correspondante, test de mutation (`test_audit_regressions.py`). Un échec peut apparaître deux fois pour une seule cause (ACTION.md et SKILL.md, copie compilée). | Un seul contrôle par règle, au propriétaire ; la copie compilée se vérifie par la comparaison à la compilation, pas par la phrase. |
| 3 | répétition | important | Moteur JSON Schema dupliqué : `validate_contracts.py:33,79,102,189,350` ; `validate_run_card.py:52,142,212,858,980` ; `validate_design_governance.py:24`. Deux listes `PLACEHOLDERS` (`validate_contracts.py:120` ; `validate_run_card.py:203`). | Un module partagé de moteur de schéma. |
| 4 | structure | mineur | `validate_run_card.py` : 1 084 lignes, 87 cas de test et 25 entrées de fixtures intégrés (l.688-860) ; `validate_contracts.py` : 25 cas (l.308) ; `validate_structure.py` : tables de verrous (l.55-286). | Séparer données de test et code ; viser moins de 400 lignes par fichier. |
| 5 | répétition | important | Les 22 fixtures invalides (40 335 o) ont toutes un message déjà couvert par un cas unitaire : 22 sur 22 messages de `FIXTURE_TABLE` figurent dans `UNIT_CASES` (vérifié par programme). Elles sont nommées trois fois (`package_manifest.json` ×2, `FIXTURE_TABLE`). | Garder 3 valides (9 624 o) et les 4 invalides appelées par la CLI de `validate_all.py:145-163` (16 211 o), soit 7 fichiers. Retirer ou générer les 18 autres (≈ 40 ko) après décision. |
| 6 | répétition | important | Chaque déplacement de fichier se paie quatre fois : `package_manifest.json` (deux listes), 41 `cp -a` (`build_distributions.sh:52-97`), `validate_design_governance.check_expected_files` (l.103), plus la règle de réécriture des chemins du Local (l.172-185). | Une seule liste dérivée de `git ls-files` ou du manifeste ; le Local en est une projection. |
| 7 | obsolète | mineur | ≈ 90 codes d'audits passés, libellés à numéros de ligne périmés : `validate_reading_map.py:645` (« DIRECTION 72 », « DIRECTION 55 »), `read_route.py:108,238`, `build_distributions.sh:175,237,247`, `validate_run_card.py:910`. | Retirer les codes des commentaires et des messages ; renommer les cas de test par ce qu'ils protègent. |
| 8 | langue (messages) | important pour `check_render`, mineur ailleurs | `check_render.py:565` : « Recette AUTOMATED (GATE-A) » ; statuts `RETURN`, `PASS-WITH-RESERVATION`, `NOT-VERIFIED` (l.14-15) ; bannières anglaises `READING MAP VALIDATION FAILED`, `CORE BUDGET PASSED` à côté de détails en français ; docstrings anglaises `read_route.py:2`, `validate_contracts.py:2`. | Une langue par script (le français, source de la charte §9) ; statuts en mots du métier pour ce qu'un designer lit. |
| 9 | langue (messages) | important | `validate_reading_map.py:~700` : « LCF-51 : condition de façade non tenue — BIBLIOTHEQUE, entrée et résumés locaux (propriétaire : …) » ne dit ni la chaîne attendue ni le fichier à toucher. `read_route.py` : « locator inconnu : DIRECTION/UNKNOWN » sans piste vers `--sommaire` ni `--trouver` (vérifié). Contre-exemple utile : `résumé infidèle` (`validate_structure.py:473`) nomme le fichier, le début du paragraphe et la chaîne manquante. | Format unique : quoi, où, comment corriger. Ajouter la piste de reprise à l'erreur de `read_route`. |
| 10 | coût de lecture et de calcul | important | La validation complète relance `test_check_render.py` (≈ 60 s avec navigateur, mesuré) à chaque `validate_all.py` de Local appelé par le build (`build_distributions.sh:230`), lui-même lancé deux fois (`validate_all.py:186,190`) ; la CI installe Chromium à chaque push (`validate.yml:21-26`). Durée totale à vérifier. | Un build, un seul passage des tests de rendu ; deux jobs CI. |
| 11 | risque | important | `validate_all.py` est la seule commande « complète » et elle écrit `dist/`, `.build/` et les zip (`:186-190`). Impossible de l'exécuter pour lire sans modifier le dépôt. | Séparer `check` (lecture seule) de `build` (écriture). |
| 12 | convergence (architecture) | important | Deux dispositions du paquet imposent des chemins doubles dans six scripts : `read_route.py:36,357,543`, `build_core.py:25-26`, `validate_design_governance.py:19`, `validate_structure.py:49`, `validate_reading_map.py:28` ; plus README Local de 54 lignes en dur dans un script (`build_distributions.sh:98-151`) qui répète des paragraphes du README. | Décider si l'export Local survit. S'il reste, le générer depuis des sources, pas depuis un heredoc. |
| 13 | convergence (tendances dans le code) | important | Les dix-sept marqueurs de vague (`violet`, `Inter`, `beige`, `crème`, `halo`…) vivent dans un validateur (`validate_reading_map.py:491`), interdits dans onze textes hors lignes `[VEILLE 20…]` datées. Mettre à jour une tendance revient à modifier du code. | Garder la règle (charte : tendances datées, jamais en règle) mais la porter par le format de la veille datée, pas par une liste de mots dans un script. |
| 14 | structure | mineur | `test_audit_regressions.py` rassemble cinq sujets sans lien (façades, liens, capacités, hôtes stricts, noyau). | Répartir chez les propriétaires (voir tableau). |
| 15 | structure | mineur | 230 lignes de JavaScript dans des chaînes Python (`check_render.py:46-275`) : pas de coloration, pas de test unitaire direct hors Node (partie C). | Extraire en fichier `.js` lu par le script. |
| 16 | répétition (limites) | mineur | Paragraphe de limites d'environ 1 100 caractères imprimé à chaque exécution (`check_render.py:569-584`) et déjà dit en docstring, `ACTION.md:805`, `README.md:175`. | Une fois dans la docstring ; la sortie ne rappelle que les limites propres à l'exécution (requêtes bloquées, textes non évalués). |
| 17 | risque | mineur | Budget `SKILL.md` : 44 559 sur 46 000 octets (`build_core.py:30`, vérifié par `--check`). Marge de 1 441 octets. | À garder en tête pour tout lot qui allonge le noyau. |

## Savoir à protéger

Les scripts ne contiennent pas de savoir de design, mais leurs tables de verrous sont **un inventaire de règles et de décisions** à faire entrer dans la table de correspondance avant tout retrait.

- `FIDELITY` (`validate_structure.py:201-284`, 65 règles) : chaque ligne est une règle à condition canonique (déclencheur + condition). Exemples : checkpoint non applicable aux actions irréversibles ou coûteuses (l.203) ; Gate B chargée en trace complète seulement ; question de convergence ; équilibre d'un titre ; récupération après erreur ; contenu marqué conserve l'action principale.
- `RETIRED` (`:98-172`, 37 décisions de vocabulaire) : trace des décisions passées (ex. « anti-direction » remplacé par MODAL/PARTI, l.107). Doit être croisé avec le CHANGELOG.
- `CONCEPTS` (`:55-83`, 26 propriétés à un seul lieu : HON-01 à HON-08 honnêteté, ANT-01 vagues datées, TRA-01 trace légère, CHK-01 première proposition = checkpoint, ROL-01 rôle, TXI-01 texte sur image, FIN-01 activation du craft…).
- 56 LCF (`validate_reading_map.py:620-705`) : cohérence d'une même règle entre façades.
- Invariants de carte (`validate_run_card.py:230-486`) et de contrats (`validate_contracts.py:193-290`).
- Logique de recherche et de classement (`read_route.py:392-560`), alias (`:434-474`).
- Seuils d'accessibilité et règles de mesure (`check_render.py:88-275`).
- Vocabulaire des schémas (`run_card.schema.json` : états, verdicts, axes, bases de capacité).

## Ce qui fige ou pousse à la convergence

- Exemples de contrats : `production_contracts.example.json` et `domain_frame.example.json` décrivent le même scénario (tableau de pilotage d'incidents B2B) avec des étendues fixes (« desktop 1440, tablette 834 », lignes 20-21, 28-33). Un agent qui remplit un autre domaine peut en recopier la grille d'états et d'étendues. Risque faible : aucune valeur de couleur, de police ni de mise en page (recherche des couleurs et polices dans `schemas/` : aucun relevé).
- `run_card.example.json` : carte `DIRECTION` complète avec un `id` (`DIRECTION-PREMIUM-001`), une thèse et des ancres rédigées ; les gabarits `chemin-ou-url-local` sont refusés par le mode strict, ce qui limite la recopie.
- `check_render.py:590` : largeurs par défaut 390, 768 et 1440. Valeurs raisonnables ; elles deviennent la grille de vérification par défaut.
- Liste de dix-sept mots de tendance dans un validateur (`validate_reading_map.py:491`) : voir défaut 13.
- Autrement : aucun relevé.

## Dépendances et risques de déplacement

- **`read_route.py` est la racine du graphe** : importé par `validate_structure`, `validate_reading_map`, `validate_design_governance` (`headings`, `non_code_lines`), `build_core` (`main`), les tests. Toute modification de ses conventions (préfixes, table « Locators principaux », titres `## X/Y`) casse tout d'un coup.
- **`validate_structure.py` importe `read_route` et `build_core`** et lit `validate_run_card.py` (`check_numeric_locators:352`, qui sort sans erreur si le fichier est absent).
- **Chaînes verrouillées sur les documents** (mesures.json, par fichier, en occurrences littéral × document ; à lire avec la remarque sur le sur-comptage) : `validate_structure` 155 (SKILL.md 30, DIRECTION.md 25, ACTION.md 23, QUICKSTART.md 14, SAVOIR.md 14, README.md 9…) ; `validate_reading_map` 109 (DIRECTION.md 26, ACTION.md 18, READING_MAP.md 14…) ; `validate_design_governance` 26 ; `read_route` 22 ; `test_audit_regressions` 28 ; `test_read_route` 20. Déplacer ou renommer README.md, SKILL.md, DIRECTION.md, ACTION.md ou QUICKSTART.md casse d'abord ces contrôles.
- **Phase 5 (`SKILL.md`, chargement, chemins)** : `CORE_FLOOR`, `check_load` (CHG-01 à 08), `check_ui_trigger` (UIX-01), `build_core.NOYAU` et `read_route.fold_core` doivent changer dans le même lot que la skill.
- **Entrée humaine** : `check_entry` (ENT-01, CST-01) verrouille quatre intertitres, le vouvoiement, l'absence de mode demandé et la signature « le réel et le beau sont cadrés ensemble » (`validate_structure.py:288`). La nouvelle entrée de la charte ne passera pas ce contrôle sans le modifier d'abord.
- **Ordre des lots recommandé** : (1) extraire le moteur de schéma et séparer données de test ; (2) introduire un mode `check` en lecture seule ; (3) à chaque lot de réécriture, retirer ses verrous de phrases avec leur entrée dans la table de correspondance ; (4) isoler le module de gouvernance avec une exécution conditionnelle dans `validate_all` ; (5) seulement alors toucher au build et à l'export Local.

## Méthode et limites de cet audit

- **Lu en entier** : les 17 fichiers de `scripts/` (les trois tests de rendu, de route et de livraison ont été lus par leurs en-têtes, la liste de tous leurs cas et leurs parties significatives, pas ligne à ligne), `validate.yml`, les cinq schémas, les trois exemples, l'exemple de carte. Les 25 fixtures ont été comparées par programme (écart structurel avec les cartes valides, couverture des messages par les cas unitaires), pas relues une par une.
- **Lancé, en lecture seule** : `build_core.py --check`, `validate_design_governance.py`, `validate_run_card.py` (suite et `--strict`), `validate_contracts.py`, `validate_reading_map.py`, `validate_structure.py`, `test_core_budget.py`, `test_audit_regressions.py`, `test_read_route.py`, `test_check_render.py`, `read_route.py` (erreurs et recherche vide), `check_render.py` sur une page d'essai placée hors du dépôt. Tout passe : 87 cas run_card sur 87, 25 sur 25 contrats, 66 tests de route, 30 régressions, 129 cas de rendu avec navigateur et Node présents.
- **Non lancé** : `validate_all.py` (il exécute `build_distributions.sh`, qui réécrit `dist/`, `.build/` et les deux zip), `build_distributions.sh`, `preparer_livraison.py`. La durée complète de `validate_all.py` est donc **à vérifier**. Les mutations de texte ont été faites sur une copie dans le dossier de travail, jamais dans le dépôt.
- Le dossier `scripts/__pycache__` (ignoré par git) a été supprimé par erreur puis recréé en partie par les tests ; `git status` reste propre.
- Les décomptes de la section des trois groupes sont des estimations par lecture (±10 %) ; le décompte de la mesure automatique a été recalculé et conservé comme preuve.

## Synthèse

1. Seuls `read_route.py`, `check_render.py` et `build_core.py` (avec leurs tests, 34 % des lignes) servent le chemin design ; ils sont à garder, avec une réécriture de forme pour les messages de `check_render` et la conservation de leurs règles d'honnêteté (pas de faux succès, rendu réel, blocage externe, captures sans écrasement).
2. Environ la moitié des ≈ 490 contrôles des validateurs sont des verrous de phrases (≈ 252), un quart de la structure utile (≈ 112), un quart de la gouvernance (≈ 122). Les verrous bloquent la phase de langue ; ils sont aussi un inventaire de règles à faire entrer dans la table de correspondance avant retrait. La mesure « 84 » de `validate_all` est surtout des chemins de fichiers : deux phrases seulement.
3. Gouvernance facultative : `schemas/` (8 fichiers + 25 fixtures), `validate_run_card.py`, `validate_contracts.py` et 24 conditions de façade forment un bloc à déplacer ; six points du cœur le supposent présent et deviennent conditionnels. Les 22 fixtures invalides doublent des cas unitaires (22 sur 22) : réduire à 7 fichiers.
4. À simplifier avant de toucher au contenu : un seul moteur de schéma (copié trois fois), une seule liste de fichiers (quatre lieux), un mode de contrôle en lecture seule distinct du build, un seul passage des tests de rendu dans la CI.
5. À décider par le propriétaire : sort de l'export Local (conditionne six scripts et le build), sort de la copie Markdown de `preparer_livraison.py`, sort des connexions situées dans `read_route.py --connexions`, et place des gabarits de cadre de domaine.
