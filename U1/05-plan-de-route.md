# Plan de route de la refonte Design Governance

**Version 2.** Date : 2026-10-07. Base : commit `d90869c`, sur la branche `claude/repo-analysis-g87gag` (paquet V1.0.0, révision `R2026-10-04-AUDIT2-FIXES`). La version 1 reste disponible : `05-plan-de-route-v1.md`.

**Sources :**
- le registre des constats C01 à C60 (`01-registre-constats.md`) ;
- l'inventaire U1b (10 fiches et leur synthèse) ;
- la note de discussion `U1b/12-discussion-creation-gouvernance.md`, avec trois recherches extérieures ;
- nos échanges du 7 octobre.

**Ce qui change par rapport à la version 1 (décision du propriétaire, 2026-10-07) :** on **corrige d'abord ce qui peut l'être sans run**, parce que l'état actuel fausserait la mesure. On **ne mesure qu'ensuite**, puis on ne fait de **paris** qu'à partir de ce que la mesure montre. L'état d'avant reste mesurable à tout moment : le commit `d90869c` est conservé.

---

## 1. Mission et critère

Inchangés par rapport à la version 1, §1.

**Mission.** Transformer une intention en une réalisation adaptée, distinctive, soignée et utilisable, en rendant les bonnes connaissances et les bons moyens plus faciles à mobiliser. Cela vaut pour ce qu'on produit, pour la manière de le produire, et pour le système lui-même.

**Critère.** *Le système permet-il d'obtenir de meilleures réalisations, avec moins d'effort total, moins de défauts évitables et moins de reprises, tout en préservant diversité et adaptation ?* Les indicateurs sont ceux de la version 1, §1. Ils sont relevés en U3 (référence) et en U5 (remesure).

## 2. Règles de conduite

| # | Règle |
|---|---|
| 1 | **Corriger avant de mesurer, mesurer avant de parier.** Les corrections objectives (type A) et les décisions tranchées par le propriétaire (type D) se font sans run. Tout changement dont l'effet est incertain (type M) attend la mesure |
| 2 | **Rien sans justification.** Chaque changement cite son constat (C01 à C60). Un mécanisme nouveau nomme ce qu'il remplace |
| 3 | **Le plus simple d'abord.** Éditer avant de scripter, retirer avant d'ajouter. Une règle ajoutée en remplace une |
| 4 | **Lire avant de modifier.** Relire en entier les sections touchées, puis chercher leurs reprises : sources, noyau, guides, README, références de la skill, validateurs |
| 5 | **Valider après chaque changement.** `validate_all` passe ; une garde qui bloque un changement voulu est adaptée **explicitement**, et c'est noté |
| 6 | **Une unité à la fois**, chacune terminée par un livrable, ses preuves, un bilan et ta décision |
| 7 | **Honnêteté des preuves.** Distinguer le testé, le lu et l'estimé. Une auto-évaluation n'est jamais présentée comme un regard indépendant |
| 8 | **Réversibilité.** Un commit par lot, annulable seul |
| 9 | **Aucun exemple, gabarit ni code à visée esthétique sans mesure de diversité avant et après.** Les exemples de trace (forme d'une décision) et le code d'observation restent permis *(validée le 2026-10-07)* |
| 10 | **Fiche de changement.** Chaque lot porte, dans son commit, les 8 éléments de la règle d'évolution du CHANGELOG : source, propriétaire, périmètre, compatibilité, preuve, limite, revue, retour. Toute règle nouvelle passe le test « utile (un échec observé), unique, polyvalent » *(validée)* |
| 11 | **Pas de hausse nette des verrous.** Chaque lot liste les verrous des validateurs qu'il touche (C57) et les adapte avec leur mutation rouge. Une phrase retirée emporte son verrou *(validée)* |
| 12 | **Ménager l'usage.** Pas d'agents en parallèle sans nécessité ; runs l'un après l'autre ; point d'étape après chaque groupe ; arrêt propre si la limite approche *(demande du propriétaire)* |
| 13 | **L'ancien dépôt `Palolo875/design-governance` est obsolète.** Il n'est ni une source ni une référence ; au plus un contexte cité comme tel |

## 3. Acquis

| Acquis | Preuve |
|---|---|
| Le dépôt contient le paquet source (69 fichiers) ; CI verte sur `d90869c` (sans navigateur, C56) | Commit `d90869c` ; run 37603355045 |
| Registre de 60 constats, chacun typé A, D, M ou S | `U1/01-registre-constats.md` |
| Couverture des cinq absolus ; trois parcours, dont P1 et P3 testés | `U1/02`, `U1/03` |
| Inventaire complet du paquet : 10 fiches, lecture intégrale, synthèse par couche | `U1b/01` à `U1b/11` |
| 23 tests rejouables sans modifier le dépôt (T-01 à T-23) | `U1/preuves/`, `U1b/preuves/` |
| Recherches : fixation et uniformisation, retour visuel et évaluation, skills et gouvernance | `U1b/12`, annexe |
| `validate_all` complet : 125 s, succès | `U1b/preuves/validate_all.log` |

## 4. Décisions

### 4.1 Prises le 2026-10-07

| # | Décision |
|---|---|
| D1 | Documents de refonte sur une branche dédiée `refonte`, créée au début de l'implémentation (C20) |
| D2 | `DIRECTION/CHARGE` reste la seule liste de chargement ; la carte d'ACTION devient un renvoi (C13). Elle passe en type A, puisque la décision est prise |
| D3 | Mesure avec des agents neufs. **Juges : Sonnet 5.5 (principal) et Haiku 5.5 (second avis)**, sur captures seules, par paires, ordre inversé ; **le propriétaire juge en dernier**, sur planche anonymisée |
| D4 | La mesure inclut une **condition « sans le système »** |
| D5 | Règles 9 à 11 ; grille d'audit en quatre axes (§5) |
| D6 | On corrige d'abord sans run (règle 1) |
| D7 | Capture simple, desktop et mobile en pleine page, ajoutée à `check_render` (décision du 2026-10-07) |
| D8 | Premier contact : le noyau reprend la nuance de SAVOIR/CFT-04a, aucun ordre ne gagne par défaut (décision du 2026-10-07) |
| D9 | Absolu 4 et piège de conformité : une ligne chacun dans le noyau, compensée en L2 (décision du 2026-10-07) |
| D10 | Blocage externe gardé par défaut dans `check_render`, documenté (appliqué en L4) |
| D11 | Navigateur ajouté à la CI (décision du 2026-10-07) |
| D12 | Modèle producteur des rendus : Opus 5.5, dans les deux conditions ; juges Sonnet 5.5 (principal) et Haiku 5.5, puis le propriétaire (décision du 2026-10-08) |
| D13 | Volume de U3 : 7 runs (décision du 2026-10-08) |
| D14 | Brief B3 remplacé, domaine choisi hors des exemples et des signaux : « Il me faut un site pour mon école de natation pour enfants. » Rien d'autre (décision déléguée, 2026-10-08) |

### 4.2 À prendre (chacune bloque un lot précis, pas tout le plan)

| # | Question | Recommandation | Constat | Lot bloqué |
|---|---|---|---|---|

## 5. Grille d'audit en quatre axes

Elle sert deux fois avec les mêmes rubriques : avant chaque lot (constats) et après (effets et régressions).

| Axe | Avant le lot : ce qu'on vérifie | Après le lot : comment on contrôle |
|---|---|---|
| **Organisation et lecture** (hiérarchie, vocabulaire, répétitions, parcours, charge) | Reprises de la règle touchée ; vocabulaire ; doublons | Charge par mode remesurée en octets (script U1, T-15) ; recherche des anciennes formulations |
| **Capacités et ressources** (disponibilité, adaptation, qualité esthétique, mobilisation effective) | Le lot rend-il un moyen plus accessible ou plus honnête ? | La qualité esthétique et la mobilisation ne se contrôlent qu'en U3 et U5 ; aucun lot ne les revendique |
| **Fiabilité** (protections, contrats, preuves, clôtures, transmissions, restauration) | Protections et contrats touchés ; tests existants | `validate_all` ; tests T-01 à T-23 rejoués ; nouveaux cas rouges, puis verts |
| **Relations entre fichiers** (dépendances, consommateurs, compilation, guides, distributions) | Consommateurs de chaque texte touché ; verrous (C57) | `build_core --check` ; deux builds identiques ; liens ; distributions GitHub et Local |

---

## 6. Les unités

### U2 — Corrections sans run (types A et D)

**Entrée :** ton accord sur ce plan, et D1 (création de la branche `refonte` pour les documents).

**Méthode, pour chaque lot :**
1. relire les sections entières et chercher leurs reprises ;
2. lister les verrous touchés ;
3. appliquer la grille « avant » ;
4. modifier ;
5. recompiler le noyau si besoin ;
6. lancer `validate_all` ;
7. remesurer la charge ;
8. remplir la fiche de changement ;
9. faire un commit ;
10. faire un point avec toi.

| Lot | Contenu | Constats | Touche le noyau ? |
|---|---|---|---|
| **L1 — Faits et hygiène** | Renvoi « §6 » faux ; compteur 27 ; « premium » défini deux fois ; marqueurs de vague et carte des moyens en double ; section vide ; exemple `decision` = `decision_intent` ; illustrations vides ; chiffres d'exemple non marqués ; limite de contraste non textuel déclarée ; READING_MAP « pour les humains » ; registre tu/infinitif | C07, C08, C12, C21, C23, C30, C31, C32, C36, C44, C46 | Peu (C07, C08) |
| **L2 — Doublons et nommage** | Un nom par FAST-PATH ; un seul jeu d'axes de position ; boucle d'édition dédupliquée ; légende des tags ; codes définis ou retirés ; noyau réordonné et sous-titré | C05, C06, C22, C26, C27, C41 | Oui ; charge mesurée avant et après, pour un noyau **plus léger ou égal** |
| **L3 — Cohérence des règles** | Prise de brief (décision §9.2 du plan v2, construire dans le même tour) ; FAST-PATH aligné sur la Protection de niveau ; un seul énoncé de l'absolu 4 ; ancre générée en enjeu élevé ; CHARGE unique et complète, avec les sous-routes LITE | C01, C04, C13, C14, C15, C17 | Oui |
| **L4 — Outils et accès** | `--trouver --guides` étendu au README et à la skill ; options de `check_render` documentées là où l'agent les lit, et outil cité au noyau ; installation de la skill documentée ; profil strict étendu aux captures B1b ; restauration sans lien symbolique ni destination non vide ; RESEARCH_BRIEF relié ; statuts des moyens (décrit, accessible, intégrable) | C10, C25, C38, C39, C43, C45, C47 | Une ligne (`check_render`) |
| **L5 — Exemples** | Retirer de l'exemple vélo l'objet convergent, sans ajouter de choix esthétique (règle 9) | C34 | Non |
| **L6 — Décisions D** | Selon tes réponses à D7, D8, D9, D11 | C18, C19, C40, C42, C56 | Selon les décisions |
| *(optionnel)* | Contrôle d'échéance des `[VEILLE]` (avant 2027-03) | C09 | Non |

**Fin quand :**
- chaque constat de type A est « corrigé » dans le registre, avec son commit ;
- chaque décision D est appliquée ou reportée par écrit ;
- `validate_all` passe ;
- le noyau n'a pas grossi ;
- les deux distributions sont reproductibles.

**Hors périmètre :** tout constat de type M ; tout ajout de matière esthétique.

### U3 — Mesure de référence, sur la version corrigée

**Entrée :** U2 terminée (révision `R2026-10-08-CORRECTIONS`, commit `01be58d`), D12 à D14 tranchées. Base figée : ce commit.

**Protocole frugal (règle 12) :**

| Brief | Avec le système | Sans le système |
|---|---|---|
| B2 — landing d'un SaaS de facturation, peu de contenu | 2 runs | 2 runs |
| B3 — « Il me faut un site pour mon école de natation pour enfants. » (D14) | 1 | 1 |
| B1 — retouche de contraste (page fournie) | 1 (mesure de proportion) | — |

Cela fait **7 runs**, un à la fois. Les deux conditions ont les **mêmes outils**, la même consigne, le même réseau (polices externes autorisées pour les deux) ; seule la skill diffère.

**Relevés :** les indicateurs de la version 1, §1 ; les routes ouvertes (H1) ; la diversité entre les deux runs de B2 (palette, police, ossature, objet de preuve), dans chaque condition.

**Jugement :**
1. Je fais les captures, déterministes, desktop et mobile.
2. Sonnet 5.5 et Haiku 5.5, en contexte frais, comparent par paires, à l'aveugle, ordre inversé, avec une grille courte : présence, spécificité, finition, vérité, défaut dominant.
3. Tu juges en dernier, sur planche anonymisée ; la clé n'est révélée qu'après ton classement.

Avant l'usage, je vérifie que l'alias « haiku » de l'outil désigne bien Haiku 5.5. Sinon, je le déclare.

**Livrable :** dossier `mesure-<commit>` avec briefs, rendus, captures, relevés, jugements et bilan. Les **seuils** des paris (U4) sont écrits **avant** de les tenter.

**Limite :** un pilote, pas une preuve générale ; juges de la même famille que le producteur ; ton regard fait référence.

### U4 — Paris mesurés (type M), choisis d'après U3

Ne sont ouverts que ceux que U3 justifie. Candidats :
- allègement du noyau au-delà des doublons (C53) ;
- promotion d'outils de route au noyau, si H1 montre qu'ils ne sont pas ouverts (C54) ;
- divergence par défaut en DIRECTION ;
- juge en contexte frais comme étape de méthode (C55) ;
- matière ou ressources (C38, C51, C52, sous la règle 9) ;
- mémoire entre runs (C59).

**Un pari à la fois, avec son seuil écrit avant.**

### U5 — Remesure

Même protocole que U3, sur la version issue de U4. Chaque pari est gardé, ajusté ou annulé.

### U6 — Vues de perception (optionnelle)

Captures floue, en gris et sans texte. Seulement si U3 ou U5 montrent une faiblesse de hiérarchie ou de foyer.

### U7 — Questions déclenchées par la preuve

C03, C11, C16, C28, C29, C33, C35, C37, C48, C49 : chacune n'est ouverte que si la mesure montre le problème.

### U8 — Intégrer et livrer

- CHANGELOG et RELEASE_NOTES selon la règle d'évolution ;
- distributions reconstruites ;
- PR vers la branche principale ;
- CI verte.

---

## 7. Ce qu'on ne fait pas

| Écarté ou reporté | Raison | Réouverture |
|---|---|---|
| Exemples, gabarits ou code esthétiques « pour aider » | Risque de figer ou de produire du slop (recherche ; règle 9) | Mesure de diversité favorable |
| Listes de polices ou de couleurs « recommandées » | Deviennent le nouveau défaut (Anthropic, Space Grotesk) | Idem |
| Fichier unique de relations, compilateur de contexte | Coût supérieur au problème constaté | Après U5, si la charge reste en cause |
| Fusion des guides, scission de BIBLIOTHEQUE | Gros chantier, effet non démontré | U7, après mesure (C49) |
| IA dans les scripts | Non reproductible | — |
| S'appuyer sur l'ancien dépôt | Obsolète (règle 13) | — |

## 8. Les 60 constats ont chacun leur place

| Où | Constats |
|---|---|
| **U2 L1** | C07, C08, C12, C21, C23, C30, C31, C32, C36, C44, C46 |
| **U2 L2** | C05, C06, C22, C26, C27, C41 |
| **U2 L3** | C01, C04, C13, C14, C15, C17 |
| **U2 L4** | C10, C25, C38, C39, C43, C45, C47 |
| **U2 L5** | C34 |
| **U2 L6** (décisions) | C18, C19, C40, C42, C56 |
| U2, optionnel | C09 |
| **U4** (paris mesurés) | C51, C52, C53, C54, C55, C59 |
| **U7** (déclenchés) | C03, C11, C16, C28, C29, C33, C35, C37, C48, C49 |
| Déjà traités | C02 (plan v1), C20 (décision D1) |
| Sans suite ou contrainte de méthode | C24, C50, C57 (règle 11), C58, C60 |

## 9. Risques du plan

| Risque | Parade |
|---|---|
| Corriger avant de mesurer fait perdre l'état « avant » | `d90869c` reste mesurable à tout moment si besoin |
| Une correction de type A change en fait le comportement | Charge et diff du noyau mesurés à chaque lot ; ce qui est incertain passe en M |
| Les verrous ralentissent chaque lot | Règle 11 ; verrous listés avant de commencer |
| Usage et limites | Règle 12 ; lots courts ; mesure frugale |
| Glissement vers « tout implémenter » | Règles 1, 2 et 9 ; §7 |
| Mesure biaisée (même famille de modèles, peu de briefs) | Condition sans système ; juges en contexte frais ; ton regard final ; limites déclarées |

## 10. Correspondance avec la version 1

| v1 | v2 |
|---|---|
| U2 baseline (avant correction) | **U3**, après les corrections sans run |
| U3 corrections sûres | **U2**, lots L1, L2 et L4 |
| U3b moyens | **U2 L4**, pour les statuts ; matière en U4 |
| U4 corrections de comportement | **U2 L3** (cohérence) et **L6** (décisions) ; le reste en U4 |
| U5 remesure, U6, U7, U8 | Inchangés |
| Décisions D1 à D3 | Prises (§4.1) |
