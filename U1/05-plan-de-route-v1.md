# Plan de route de la refonte Design Governance

**Version :** 1 · **Date :** 2026-10-07 · **Base :** commit `d90869c` (branche `claude/repo-analysis-g87gag`, paquet V1.0.0, révision `R2026-10-04-AUDIT2-FIXES`).
**Sources consolidées :** plan DG-REFONTE-2026-10-05-v2 ; unité U1 (registre des 37 constats, matrice de couverture, parcours, vérification de l'analyse externe) ; nos échanges du 7 octobre, dont la décision de **ne rien construire qui ne soit nécessaire**.

Ce document ne remplace pas le plan v2 : il l'**ordonne** et le **réduit** à ce qui est justifié par une preuve. La correspondance avec les étapes du plan v2 figure en section 7.

---

## 1. Mission et critère de jugement (formulés par le propriétaire, 2026-10-07)

**Mission.** Transformer une intention en une réalisation adaptée, distinctive, soignée et utilisable, en rendant les bonnes connaissances et les bons moyens plus faciles à mobiliser. Le système améliore :
- **ce qu'on produit** : compréhension du besoin, direction artistique, composition, contenu, interactions, finition, pour des interfaces, sites, identités, documents ou présentations selon les moyens disponibles ;
- **la manière de le produire** : retrouver une méthode, savoir quand elle convient, sélectionner une ressource (connaissance, asset, police, composant, bibliothèque, outil), l'adapter et vérifier son effet ; l'existence d'un moyen doit déboucher sur une possibilité concrète de fabrication ;
- **le système lui-même** : organisation compréhensible, responsabilités claires, connexions fiables, reprise facile, retours d'expérience qui réduisent les défauts récurrents.

L'utilisateur exprime son besoin sans maîtriser la mécanique. **Règles, audits, traces et contrôles servent cette mission** : ils protègent la qualité, la cohérence, la vérité des affirmations et la continuité.

**Critère de jugement.** *Le système permet-il d'obtenir de meilleures réalisations, avec moins d'effort total, de défauts évitables et de reprises, tout en préservant diversité et adaptation ?*

| Partie du critère | Indicateur mesuré (U2, puis U5) |
|---|---|
| Meilleures réalisations | Lecture à l'aveugle (foyer, spécificité, finition, défaut dominant) ; objet de preuve présent et crédible |
| Moins d'effort total | Tours jusqu'au premier artefact ; octets lus ; questions posées ; attente ou non d'une réponse avant de construire |
| Moins de défauts évitables | Résultats `check_render` ; affirmations inventées non marquées ; actions principales non fonctionnelles |
| Moins de reprises | Nombre de corrections nécessaires après le premier rendu, et leur nature (locale ou structurelle) |
| Diversité | Deux runs indépendants du même brief : reprise de la même palette, police, ossature ou objet de preuve |
| Adaptation | Les trois briefs donnent-ils des expressions différentes et justifiées par leur contexte ? |
| Moyens mobilisés | Polices, icônes, images et composants réellement intégrés, chargés et autorisés, ou repli honnête déclaré |
| Sans maîtriser la mécanique | Jargon interne dans la réponse visible ; clarté des quatre rubriques |

## 2. Règles de conduite (valables pour toute la refonte)

1. **Mesurer avant de changer.** Aucune modification du paquet tant que l'état actuel n'est pas mesuré (U2).
2. **Rien sans justification.** Chaque changement cite son constat (C01 à C37). Chaque mécanisme nouveau nomme ce qu'il remplace et la mesure qui le justifie ; sinon il n'est pas construit.
3. **Le plus simple d'abord.** Éditer avant de scripter, retirer avant d'ajouter. Une règle ajoutée en remplace une.
4. **Lire avant de modifier.** Relire en entier les sections touchées et chercher leurs reprises (sources, noyau, guides, README, références de la skill, validateurs).
5. **Valider après chaque changement.** `python3 scripts/validate_all.py` doit passer ; si une garde bloque un changement voulu, la garde est adaptée **explicitement**, et c'est noté.
6. **Une unité à la fois.** Chaque unité se termine par un livrable, ses preuves, un bilan et **un point de décision avec vous**. Aucune unité ne démarre sans votre accord.
7. **Honnêteté des preuves.** Distinguer le testé, le lu et l'estimé ; une auto-évaluation n'est jamais présentée comme un regard indépendant.
8. **Réversibilité.** Chaque unité est un commit (ou une PR) séparé, qu'on peut annuler seul.

## 3. Où en est-on (acquis)

| Acquis | Preuve |
|---|---|
| Le dépôt contient le paquet source (69 fichiers) ; la CI s'y exécute | Commit `d90869c` ; `validate_all` passe |
| Les identités du plan v2 sont confirmées (copie, archives GitHub et Local) | Empreintes recalculées, identiques |
| 37 constats documentés avec leur preuve et leur disposition | `01-registre-constats.md` |
| Couverture des cinq absolus et de l'intégrité | `02-matrice-couverture.md` |
| Trois parcours préparés ; P1 et P3 réellement testés | `03-parcours.md` |
| Analyse externe vérifiée (≈ 60 affirmations) ; 12 constats ajoutés | `04-verification-analyse-externe.md` |
| 17 tests rejouables sans modifier le dépôt | `preuves/reproduire_U1.py` |

## 4. Décisions à prendre avant U2

| # | Question | Recommandation | Pourquoi maintenant |
|---|---|---|---|
| **D1** | Où ranger les documents de refonte (plan, registre, mesures) ? Le paquet refuse tout fichier hors inventaire (C20). | Une branche `refonte` séparée, qui ne contient que ces documents | Sans cela, rien n'est versionné |
| **D2** | Une seule liste de chargement : la table `CHARGE` de DIRECTION, complétée ; la carte d'ACTION devient un renvoi (C13). | Garder `CHARGE` | Conditionne U4 |
| **D3** | Lancer des agents neufs pour la mesure (environ 6 : 3 qui produisent, 3 qui relisent à l'aveugle). | Oui | Sans eux, pas de mesure sans biais d'ancrage |

---

## 5. Les unités

### U2 — Mesurer l'état actuel (baseline)

- **Entrée :** D1, D2, D3 tranchées. Base figée : `d90869c`.
- **Travail :**
  1. Trois briefs fixes, écrits avant les essais : **B1** retouche de contraste (page fournie `preuves/p1/avant.html`) ; **B2** landing d'un SaaS de facturation, peu de contenu ; **B3** « un site pour mon atelier de réparation de vélos », rien d'autre.
  2. Pour chaque brief, un agent **neuf**, avec le paquet seul. **B2 est lancé deux fois**, avec deux agents indépendants, pour mesurer la diversité. Option : un **B4 hors Web** (par exemple un document d'une page) pour voir où le système et ses outils s'arrêtent ; ses contrôles automatiques seront déclarés `NOT-VERIFIED`.
  3. On relève :
     - les routes ouvertes et les octets lus ;
     - les questions posées, et s'il attend la réponse avant de construire ;
     - le nombre de tours jusqu'au premier artefact ;
     - le résultat de `check_render` ;
     - les affirmations non marquées comme exemple ;
     - la trace produite ;
     - les **moyens réellement mobilisés** (polices, icônes, images, composants), s'ils sont chargés, et leur licence ;
     - le jargon interne dans la réponse visible.

     Tous les indicateurs du tableau de la section 1 sont relevés.
  4. Chaque rendu est lu à l'aveugle par une instance neuve, sans trace ni corpus, avec une grille courte fixée à l'avance : foyer, spécificité, finition, défaut dominant. Cette lecture est déclarée comme un substitut, jamais comme un regard humain.
- **Livrable :** dossier `baseline-d90869c` (briefs, rendus, mesures, lectures) et un bilan.
- **Fin quand :** les trois briefs ont leurs mesures complètes, et les **seuils de réussite** des unités suivantes sont écrits **avant** toute correction, puis ne sont plus modifiés après observation.
- **Hors périmètre :** toute modification du paquet.
- **Limite connue :** trois briefs forment un pilote, pas une preuve générale ; même famille de modèle.

### U3 — Corrections sûres (cohérence, sans changer ce que fait l'agent)

- **Entrée :** U2 terminée.
- **Constats traités :**
  - C07 READING_MAP « pour les humains » ;
  - C08 registre tu / infinitif ;
  - C12 renvoi « §6 » faux dans GATE-C ;
  - C22 deux FAST-PATH ;
  - C23 compteur 27 → 30 ;
  - C30 « premium » défini deux fois ;
  - C31 marqueurs de vague et carte des moyens en double ;
  - C32 section vide ;
  - C36 exemple `decision` = `decision_intent` ;
  - C25 étendre `--trouver --guides` au README et aux références de la skill ;
  - C10 restauration : refuser les liens symboliques et les destinations non vides (version minimale, sans staging) ;
  - C21 déclarer la limite de `check_render` sur le contraste non textuel.
- **Méthode :** pour chaque constat, relire la section entière, chercher ses reprises, modifier, puis lancer `validate_all`. Un commit par groupe cohérent.
- **Fin quand :** chaque constat traité est marqué « corrigé » dans le registre avec son commit ; `validate_all` passe ; le noyau ne bouge pas, ou seulement par déduplication (à vérifier par diff).
- **Hors périmètre :** prise de brief, table `CHARGE`, contenu du noyau.

### U3b — État réel des moyens (connaissances, assets, polices, composants, outils)

- **Entrée :** U2 terminée. Peut avancer en parallèle de U3.
- **Pourquoi :** la mission exige qu'un moyen débouche sur une fabrication concrète. Aujourd'hui, la carte des moyens (`SAVOIR/TOOLS/MOYENS`, 2,2 Ko) ne donne que des noms de sources, et le paquet ne fournit aucun asset (C38). La recette d'observation bloque les ressources externes : une police chargée depuis un service tiers est jugée avec la police de repli (C39). Ce travail correspond au premier alinéa de l'étape 4 du plan v2, qui s'exécute sans condition.
- **Travail :**
  - classer chaque moyen cité selon son statut réel : **décrit** (un nom), **accessible** (atteignable dans l'environnement du run), **intégrable** (une recette d'intégration courte existe), **éprouvé** (utilisé dans un run mesuré) ;
  - pour chaque couche, nommer le **repli honnête** quand le moyen manque ;
  - s'appuyer sur ce que U2 a observé : moyens réellement utilisés, échecs de chargement.
- **Livrable :** une table de statuts dans la source propriétaire (`SAVOIR/TOOLS/MOYENS`), sans catalogue ni nouveau mécanisme ; décision sur C39 (autoriser les polices dans `check_render`, ou déclarer la limite).
- **Fin quand :** chaque moyen cité a un statut et un repli ; aucun moyen « décrit » n'est présenté comme disponible.
- **Hors périmètre :** embarquer des assets dans le paquet ; construire une bibliothèque de composants (à reconsidérer seulement si U2 ou U5 montre que l'absence de moyens limite la qualité).

### U4 — Corrections de comportement (ce que l'agent lit et fait)

- **Entrée :** U3 terminée, seuils de U2 écrits.
- **Constats traités, par lot :**
  - **Lot 1, prise de brief :** C01, C02, C03. Appliquer la décision §9.2 dans DIRECTION, puis recompiler le noyau ; aligner QUICKSTART, README (et README Local), `examples.md` ; adapter la garde `validate_structure.py:227`.
  - **Lot 2, chargement :** C13, C15. Compléter la table `CHARGE` (STANDARD et DIRECTION) et citer les sous-routes (`GATE-B/B2`, `B6`…). La carte d'ACTION devient un renvoi (D2).
  - **Lot 3, classement :** C14. Aligner FAST-PATH sur la Protection de niveau.
  - **Lot 4, protections dans le noyau :** C04, C17, C18, C19. Les cinq absolus en une ligne chacun (clause santé incluse), le piège de conformité et la déclaration « avant de construire », avec un énoncé unique de l'absolu 4.
  - **Lot 5, lisibilité du noyau :** C26, C27, C05, C06. Réordonner (classer, absolus, brief et vérité, structure, composition, boucle, sortie), sous-titrer la section 5, définir les tags et jetons au premier usage, retirer les répétitions de la boucle.
- **Contraintes :** le budget du noyau (46 000 octets) est tenu ; chaque ajout s'accompagne d'un retrait équivalent quand c'est possible ; aucun nouveau mécanisme.
- **Fin quand :**
  - les constats du lot sont « corrigés » ;
  - `validate_all` passe ;
  - les charges par mode sont remesurées (objectif indicatif : LITE ≤ 62 Ko, à confirmer par le seuil fixé en U2) ;
  - un diff lisible du noyau avant et après est fourni.

### U5 — Remesurer et décider

- **Entrée :** U4 terminée.
- **Travail :** même protocole que U2, mêmes briefs, agents neufs, sur la nouvelle version ; comparaison aux seuils.
- **Livrable :** bilan comparatif avant/après, par mesure et par lot.
- **Décision :** chaque lot de U4 est **gardé, ajusté ou annulé** selon les mesures. Un lot qui n'améliore rien et ne protège rien de plus est annulé.

### U6 — Une seule expérience nouvelle : les vues de perception (optionnelle)

- **Entrée :** U5 terminée, et uniquement si U5 montre une faiblesse perceptuelle (foyer, hiérarchie, finition).
- **Travail :** `check_render` produit en plus une capture floue, une en niveaux de gris, une sans texte et une mobile ; on compare avec et sans ces vues, sur les mêmes briefs.
- **Décision :** gardé seulement si la lecture à l'aveugle s'améliore.

### U7 — Questions tranchées par la preuve (au cas par cas)

Chaque point ci-dessous n'est ouvert que si U2 ou U5 montrent le problème :

| Constat | Question | Ce qui la déclenche |
|---|---|---|
| C11, C33 | Contrôle de contenu vide sur `proof.observed`, `method` et `creative_close` ? | Des traces creuses observées dans les runs |
| C16 | Alléger les routes DIRECTION ? | Charge DIRECTION jugée excessive face aux seuils |
| C28 | Table de craft à 3 colonnes ? | A/B neutre ou positif |
| C29 | Budget par mode en test automatique ? | Dérive de charge constatée après U4 |
| C34, C35 | Exemple vélo, profils STYLE, matrice COMPAT : effet de preset ? | Reprise des mêmes objets ou noms entre les rendus |
| C37 | Une grille de qualité de référence ? | Confusion observée chez l'agent ou le relecteur |
| C09 | Contrôle d'échéance des `[VEILLE]` ? | À faire avant 2027-03 |
| C03 (approche générale) | Contrôle de cohérence des reprises de règles ? | Un second changement canonique qui laisse des reprises en retard |

### U8 — Intégrer et livrer

- **Travail :**
  - mettre à jour CHANGELOG et RELEASE_NOTES (ce qui a changé, ce qui est prouvé, les limites) ;
  - reconstruire les distributions GitHub et Local, et vérifier leurs chemins ;
  - ouvrir une PR avec tous les résultats attribués à la version.
- **Fin quand :** CI verte, distributions reproductibles, notes de version honnêtes, retour arrière possible (la version précédente est conservée).

---

## 6. Ce qu'on ne fait pas, et pourquoi

| Idée écartée ou reportée | Raison | Condition de réouverture |
|---|---|---|
| Fichier unique de relations (refonte des 55 listes des scripts) | Coût supérieur au problème constaté (une seule règle et ses reprises) | Plusieurs changements réels montrent des reprises oubliées |
| Compilateur de paquets de contexte | Les sous-routes dans `CHARGE` donnent l'essentiel du gain | La charge reste au-dessus des seuils après U4 |
| Mémoire anti-convergence entre runs | Signal faible (veille sur peu de rendus) | Convergence mesurée en U2 ou U5 |
| Navigation par symptôme (synonymes) | Besoin non observé | Échecs de recherche observés chez un agent |
| Scission de BIBLIOTHEQUE, fusion QUICKSTART et READING_MAP | Gros chantier, effet sur les rendus non démontré | Après U5, si la charge des guides est en cause |
| IA dans les scripts (routage ou jugement automatique) | Non reproductible, non vérifiable | — |
| Staging et récupération pour la restauration | Git est la source ; la copie Markdown est secondaire | — |

## 7. Correspondance avec le plan v2

| Plan v2 | Ici |
|---|---|
| Étape 0 (base et constats) et 0 bis (audit) | U1, faite pour le noyau, DIRECTION, ACTION et INTEGRITY. Les autres fichiers sont lus **au moment où une unité les touche** (règle 4) |
| Étape 1 (protections, preuves, restauration) | Matrice faite en U1 ; restauration minimale en U3 ; protections du noyau en U4 |
| Étape 2 (sources, grilles, parcours) | U3 et U4 |
| Étape 3 (index des relations) | Reportée (section 6) |
| Étape 4, premier alinéa (statuts des ressources et replis honnêtes) | **U3b**, sans condition, comme le prévoit le plan v2 |
| Reste des étapes 4 et 5 (mobilisation assistée) | Derrière la porte de mesure : U6 et U7 seulement si U5 le justifie |
| Étape 6 (évaluation) | **Avancée** : U2 (avant) et U5 (après) |
| Étape 7 (intégration) | U8 |
| §9.1 (lecture de substitution) | Appliqué en U2 et U5 |
| §9.2 (construire dans le même tour) | U4, lot 1, **après** la baseline |

## 8. Les 39 constats ont chacun leur place

| Unité | Constats |
|---|---|
| Décision D1 | C20 |
| U3 | C07, C08, C10, C12, C21 (limite), C22, C23, C25, C30, C31, C32, C36 |
| U4 | C01, C02, C03 (garde concernée), C04, C05, C06, C13, C14, C15, C17, C18, C19, C26, C27 |
| U3b | C38, C39 |
| U6 | C21 (amélioration éventuelle de la recette) |
| U7 | C03 (approche générale), C09, C11, C16, C28, C29, C33, C34, C35, C37 |
| Sans suite | C24 (aucun texte ne cite `GATE-A/A1`) |

## 9. Risques du plan lui-même

| Risque | Parade |
|---|---|
| Trop de documentation autour du travail | Un registre, un plan, un bilan par unité ; rien d'autre |
| Mesure biaisée (même modèle, peu de briefs) | Briefs et seuils fixés avant ; limites déclarées ; jamais présentés comme preuve générale |
| Une correction en casse une autre | `validate_all` après chaque changement ; un commit par lot ; U5 compare |
| Le noyau dépasse son budget en U4 | Chaque ajout s'accompagne d'un retrait ; le budget est contrôlé à la compilation |
| Glissement vers « tout implémenter » | Règle 2 et section 6 : rien sans constat et sans mesure |
