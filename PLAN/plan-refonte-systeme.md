# Plan de refonte du système — nettoyer, structurer, rendre pro

**Statut :** plan validé, en cours d’exécution. Mis à jour le 9 octobre 2026, après le lot 6 du rangement. Aucun run n’est prévu sans ton accord explicite.
**Point de départ :** commit `9681d4e` sur `claude/repo-analysis-g87gag` (révision `R2026-10-08-ACCES-MATIERE`). **Dernier commit :** `f665c81`.

---

## 0. État d’avancement

| Phase | État | Ce qui est fait |
|---|---|---|
| 0 — Charte et grilles | **faite** | Charte en 10 principes, grilles fichier, système et résultat (`PLAN/charte.md`, `PLAN/grilles.md`) |
| 1 — Audit | **faite** | 8 fiches, mesures, second jeu de recherche, synthèse et dispositions (`AUDIT2/`) |
| 2 — Architecture | **faite** | Arborescence, quatre portes, module de gouvernance, vocabulaire, table de 388 sections, carte visuelle (`ARCHI/`) |
| 3 — Rangement | **en cours : lots 0 à 6 faits** | Voir le détail ci-dessous |
| 4 à 8 | à venir | |

**Rangement, lot par lot :**

| Lot | État | Commit | Résultat |
|---|---|---|---|
| 0 — Outils de sécurité | fait | `950f664` | Validation en lecture seule ; contrôle « rien de perdu » (2 720 blocs relevés) |
| 1 — Indépendance d’emplacement | fait | `daf1db2` | Une seule table (`LIEUX`) dit où vit le contenu ; test de déplacement simulé ; registre des 270 phrases verrouillées |
| 2 — Outils | fait | `02b56d5` | Recherche par phrases (témoin : 26/75 dans les 3 premiers, contre 1 ou 2) ; 74 adresses lisibles ; installation corrigée |
| 3 — Vestiges et historique | fait | `8653161` | Journal de décisions et historique des versions hors produit ; fichier-renvoi retiré ; 44 retraits justifiés, conservés sur `refonte` |
| 4 — Gouvernance en module | fait | `4077ae3` | 15 sections (~80 000 caractères) dans `gouvernance/` ; texte servi identique pour les 110 routes |
| 4b — Schémas et outils de gouvernance | fait | `a92a47c` | `gouvernance/schemas/` et `gouvernance/outils/` ; seuls les chemins changent dans la documentation (23 lignes), renommages déclarés |
| 5 — Cœur du design | fait | `8e2b23d` | 37 sections dans `design/` (direction, savoir, formes, produit), un README par dossier ; texte servi identique pour les 110 routes |
| 6 — Agent | fait | `f665c81` | 9 sections dans `agent/chemins.md` et `agent/repondre.md` ; la skill dans `agent/skill/`, identique ; consigne d’installation corrigée (la skill garde son nom) |
| 7 — Portes et maintenance | à faire | | README court, guides par public, glossaire, `maintenance/` |

**Garanties vérifiées à chaque lot :** rien de perdu (chaque bloc retrouvé ou retiré avec sa raison) ; texte servi identique pour chaque route ; skill identique à l’octet près ; validation complète verte, archives comprises ; un commit annulable avec sa fiche.

**Ce qui a changé au plan en cours de route, et pourquoi :**
1. **Lot 1.** Les phrases exigées mot pour mot par les contrôles ne gênent que la réécriture, pas le déplacement. Elles seront converties en règles protégées **fichier par fichier en phase 4**, texte en main, plutôt que toutes d’un coup.
2. **Lot 4.** Le rangement ne déplace que des **sections entières** dont le déplacement ne change pas ce que lit l’agent. Les sections qui mêlent design, produit et gouvernance doivent être **découpées**, ce qui change ce que lit l’agent : ce découpage passe **en phase 5**, avec la skill et la table de lecture.
3. **Lot 4.** Un fichier qui reçoit des sections de plusieurs sources marque l’origine de chacune, de façon invisible à la lecture, pour que les contrôles retrouvent la part de chaque source.
4. **Lot 4b ajouté.** Déplacer les schémas et leurs outils touche de nombreux chemins (scripts, CI, documentation) : c’est un lot à part.
5. **Lot 6.** Renommer le dossier de la skill aurait fait installer la skill sous le nom « skill » : la consigne d’installation dit désormais sous quel nom la copier.
6. **Phase 5.** Les mesures de l’audit y ajoutent deux priorités : la convergence des résultats (même police, même concept d’un run à l’autre) et l’effet possible de mon ajout récent « signaux de page ».

---

## 1. Ce que l’on veut obtenir

Un système de design :

- **centré sur le design.** Le savoir, la direction et les formes sont le cœur ; la gouvernance aide ou renforce ;
- **qui produit des résultats beaux, variés, créatifs et de qualité pro.** Un produit qu’on pourrait mettre en ligne, pas une démo ;
- **flexible et proportionné.** L’effort suit la demande, ce qui réduit le coût et la complexité ;
- **utilisable par tous.** Un débutant, un designer, une équipe ou un agent ;
- **clair, bien structuré, facile à parcourir, peu chargé.** Dans l’ensemble comme dans chaque fichier ;
- **beau lui-même** : la carte, les schémas et les supports visuels ;
- **en français et en anglais ;**
- **opérable partout.** Avec ou sans navigateur, avec Claude Code ou un autre agent ;
- **propre et présentable.**

## 2. Charte : les dix principes qui guident chaque décision

1. **Le design au cœur.** La gouvernance est un module qu’on active quand il sert : livraison client, audit, travail en équipe.
2. **Beau, varié, pro.** La variété vient de ce qui est propre à chaque demande, pas du hasard. La qualité vient du métier : finition, typographie, rendu vérifié.
3. **L’effort proportionné.** On dépense là où ça change le résultat et on coupe ailleurs. L’agent choisit le chemin ; personne n’a à comprendre les modes.
4. **Une porte par public.** Un seul contenu, des entrées différentes, et d’abord seulement ce qui sert.
5. **Clair et en deux langues.** Aucun code interne visible. Le français est la source, l’anglais une traduction contrôlée, et l’agent répond dans la langue de la personne.
6. **Beau lui-même.** Le système a une identité visuelle propre, et chaque schéma garde un équivalent écrit.
7. **Structuré et léger.** Chaque fichier a un rôle et un public, une structure prévisible, et aucune répétition.
8. **Opérable partout.** Le système dit ce qu’il n’a pas pu vérifier, sans s’arrêter pour autant.
9. **Prudent et rigoureux.** Rien ne se perd sans décision écrite. Chaque changement passe par un diagnostic, une proposition, ton accord, puis un commit annulable.
10. **Honnête sans encombrer.** Les limites sont dites une fois, au bon endroit, et non répétées à chaque page.

## 3. Les publics et ce dont chacun a besoin

| Public | Ce qu’il veut | Sa porte d’entrée | Ce qu’il ne doit pas voir d’abord |
|---|---|---|---|
| Débutant ou personne sans expérience | Obtenir un bon résultat sans apprendre le système | Une page : quoi demander, quoi fournir, ce qu’on reçoit, comment poursuivre | Modes, routes, gouvernance, vocabulaire interne |
| Designer | Un savoir de référence pour juger et fabriquer | Le savoir et les formes, parcourables par sujet, comme un livre | Mécanique d’agent, traces, schémas de données |
| Équipe | Travailler à plusieurs, livrer, garder une trace | Le même contenu, plus le module de gouvernance | Détails d’outillage interne |
| Agent | Savoir quoi lire, quand, et quoi produire | La skill, courte, avec des renvois clairs | Historique, explications destinées aux humains |

## 4. État de départ : ce que l’on sait déjà

**Taille.**
- Environ 630 000 caractères de texte au total.
- **Design**, SAVOIR et BIBLIOTHEQUE : environ 200 000.
- **Gouvernance**, ACTION : environ 121 000.
- **DIRECTION**, qui mêle direction et gouvernance : environ 106 000.
- **Guides et cartes** : environ 120 000.
- **Historique** : environ 40 000.
- **Skill** : environ 44 600 octets, pour un plafond de 46 000.
- **Outillage** : 17 scripts, environ 6 900 lignes, et 25 fichiers de test pour les schémas.

**Navigation.** 71 routes. Le lecteur trouve la bonne route pour 98 termes sur 121 (rang médian : 1). En mode DIRECTION, la lecture de départ fait environ 80 000 caractères.

**Langue.**
- Des codes internes partout (CFT-04a, B1b, FAST-PATH, RETURN, LCF-46…).
- `NOT-VERIFIED` plus de 70 fois.
- Des noms de révision dans le README.
- Un glossaire de 14 000 caractères, rendu nécessaire par ce jargon.

**Vestiges.**
- `ORCHESTRATION_MAP.md` n’est plus qu’un renvoi.
- L’historique de travail est livré avec le produit.
- Le guide QUICKSTART fait 27 000 caractères.

**Visuel.**
- Un seul schéma dans le système : un diagramme Mermaid dans `references/flow.md`.
- Des gabarits en texte brut (Creative Boot, cadrage de domaine).
- La carte du système est un artifact externe, non livré.

**Ce qu’ont appris les mesures U3 et U5.**
- Le savoir est présent, mais l’agent ne le mobilise pas assez.
- Les runs qui mobilisent tout sont meilleurs, pour 40 à 60 % de jetons en plus.
- Ce qui change le résultat : l’atelier de direction, le choix typographique, le style, la palette et les retouches sur capture.
- **Les résultats convergent.** Trois pages de facturation se ressemblent ; deux pages de natation ont le même concept.

## 5. Règles de travail pendant la refonte

1. **Une table de correspondance tenue à jour.** Chaque section, règle ou élément de savoir de l’ancien système reçoit une nouvelle adresse, ou une raison de retrait que tu as validée. Un contrôle automatique vérifie que rien ne manque.
2. **Le fond n’est pas touché pendant le rangement.** Les phases 3 et 4 changent la place, la forme et la langue. Elles ne changent pas ce que le savoir enseigne. Un changement de fond est un lot à part, annoncé comme tel.
3. **Un cycle fixe pour chaque lot.** Diagnostic écrit, proposition, ton accord, application, contrôles, commit annulable avec sa fiche de changement.
4. **Ce qui pilote l’agent passe en dernier.** La skill, la liste de chargement et les chemins changent son comportement : on les retouche en phase 5 seulement, avec une petite mesure si tu l’acceptes.
5. **Moins de contrôles, mais solides.** Chaque contrôle conservé garde sa preuve d’efficacité : on le casse volontairement et il doit échouer. Chaque contrôle retiré est noté avec sa raison. Le total doit baisser.
6. **Ce que l’on garde.** Les décisions déjà prises (gouvernance proportionnée, honnêteté sur la preuve, pas d’exemples qui figent), le lecteur de routes, la construction de la skill depuis les sources, la vérification du rendu.
7. **Le travail reste séparé du produit.** Les documents de travail vont sur `refonte` ; le système, sur la branche de développement.

## 6. Les phases

Chaque phase indique son but, son contenu, ce qu’elle produit, la condition pour la considérer finie, ce que tu valides, et ses risques.

### Phase 0 — Charte et grille de qualité

- **But :** fixer le cap et les critères avant de toucher quoi que ce soit.
- **Contenu :**
  - finaliser la charte (§2) et les publics (§3) ;
  - écrire une **grille de qualité d’un fichier**, appliquée ensuite partout : rôle unique, public nommé, ouverture qui dit à quoi sert le fichier, structure prévisible, longueur adaptée à l’usage, absence de répétition et de jargon non expliqué, liens valides, risques et limites au bon endroit ;
  - écrire une **grille de qualité du système** : portes d’entrée, charge de lecture par chemin, trouvabilité, cohérence du vocabulaire, beauté des supports.
- **Livrables :** `charte.md` et `grilles.md` sur `refonte`.
- **Fin :** charte et grilles validées par toi.
- **Risque :** des grilles trop abstraites. Parade : chaque critère dit comment on le vérifie.

### Phase 1 — Audit fichier par fichier, sans rien changer

- **But :** savoir précisément quoi faire de chaque fichier.
- **Contenu :**
  - une fiche par fichier, en appliquant la grille de la phase 0 : 17 documents, 17 scripts, les schémas et les fichiers de test ;
  - un **registre des défauts**, classés par type : structure, langue et jargon, répétition, obsolète, risque, visuel, coût de lecture ;
  - une **carte des dépendances** : quel fichier cite quoi, quel contrôle protège quoi, ce qui casse si on déplace ;
  - un **audit des chemins de l’agent** : ce qu’il lit pour une petite correction, pour une page, pour un produit livré, combien ça coûte, et ce qui ne sert à rien ;
  - un **audit de la créativité et de la variété** : où le système pousse à la variété, où il pousse à la convergence (choix par défaut, gabarits, exemples), à partir des pages U3 et U5 ;
  - l’**inventaire des contrôles** : pour chacun, ce qu’il protège, s’il reste utile, et s’il fige du texte.
- **Livrables :** `AUDIT2/` sur `refonte`, avec les fiches, le registre, les dépendances et la synthèse. On réutilise l’audit et l’inventaire U1b déjà faits.
- **Fin :** chaque fichier a une fiche et une disposition proposée (garder, déplacer, fusionner, réécrire, retirer).
- **Tu valides :** les dispositions.
- **Risque :** un audit trop long. Parade : une fiche courte par fichier, et le détail seulement là où il y a un défaut.

### Phase 2 — Architecture cible

- **But :** dessiner le système final avant de le construire.
- **Contenu :**
  - l’**arborescence cible** : la place de chaque fichier, les quatre portes d’entrée, le module de gouvernance bien délimité ;
  - les **chemins par effort** : petite correction, page ou écran, produit livré. Pour chacun : ce que l’agent lit, ce qu’il produit, ce qu’il vérifie ;
  - le **vocabulaire** : la table qui remplace chaque code interne par un nom clair, et les termes conservés avec leur définition ;
  - le **modèle de section**, une structure type commune à toutes les routes : à quoi elle sert, quand l’ouvrir, comment l’appliquer, les pièges, ce qui prouve que c’est réussi ;
  - la **première version de la table de correspondance**, de l’ancien vers le nouveau ;
  - la **liste des contrôles cibles**, avec ceux qu’on garde, ceux qu’on adapte et ceux qu’on retire.
- **Livrables :** `architecture.md`, `vocabulaire.md`, `correspondance.csv` sur `refonte`, et une carte visuelle de l’architecture cible pour en juger.
- **Fin :** architecture validée par toi.
- **Risque :** une architecture élégante sur le papier mais coûteuse à migrer. Parade : chaque déplacement est chiffré et justifié par un défaut de l’audit.

### Phase 3 — Rangement par lots (forme et place, pas le fond)

- **But :** passer à l’architecture cible sans rien perdre.
- **Lots, dans cet ordre** (détail et état au §0) :
  0. **Outils de sécurité** : validation en lecture seule, contrôle « rien de perdu ». *Fait.*
  1. **Indépendance d’emplacement** : table `LIEUX`, registre des verrous. *Fait.*
  2. **Outils** : recherche par phrases, adresses lisibles, installation. *Fait.*
  3. **Vestiges et historique** hors produit. *Fait.*
  4. **Gouvernance en module** : sections entières de gouvernance formelle. *Fait.* 4b : schémas et outils de gouvernance.
  5. **Cœur du design** : sections entières de direction, savoir, formes et produit vers `design/` ; ouverture de chaque fichier (rôle, public).
  6. **Agent** : chemins et réponse ; la skill sous `agent/skill/`.
  7. **Portes et maintenance** : README court, guides par public, glossaire, `maintenance/`.
- **Règle des déplacements :** seulement des sections entières, et seulement si chaque route sert ensuite exactement le même texte. Le découpage des sections mêlées attend la phase 5.
- **Pour chaque lot :** rien de perdu, texte servi identique, skill identique, contrôles verts, commit annulable.
- **Fin :** architecture en place, table complète, contrôles verts.
- **Risque :** casser les renvois internes. Parade : la carte des dépendances de la phase 1, et un contrôle des liens à chaque lot.

### Phase 4 — Langue claire en français

- **But :** que chaque public comprenne sans glossaire.
- **Contenu :**
  - réécrire fichier par fichier avec le vocabulaire de la phase 2 ;
  - des phrases courtes, un exemple de mécanisme quand il éclaire, jamais un exemple qui fige ;
  - les limites (`NOT-VERIFIED`) dites une fois au bon endroit ;
  - un glossaire réduit aux vrais termes du métier.
- **Verrous :** les phrases exigées mot pour mot par les contrôles qui touchent le fichier réécrit sont converties en règles protégées (présence de la règle et de quelques termes clés), avec une mutation rouge chacune ; le registre `RANGEMENT/verrous.csv` sert de liste de travail.
- **Contrôle du sens :** on garde un échantillon avant/après par fichier, que tu relis, et la table de correspondance vérifie qu’aucune règle n’a disparu. Les blocs du noyau attendent la phase 5 (skill identique jusque-là).
- **Fin :** tous les fichiers passent la grille de la phase 0 sur la langue.
- **Risque :** perdre une nuance en simplifiant. Parade : la relecture d’échantillons, et les règles à forte conséquence relues une à une.

### Phase 5 — Chemin de l’agent : variété, qualité et coût

C’est la seule phase qui change le comportement de l’agent.

- **But :** produire des résultats plus variés et plus pro, pour moins cher.
- **Contenu :**
  - **découper les sections mêlées** (design, produit, gouvernance) relevées par la table de correspondance (« scinder »), pour que le chemin de design ne lise plus la gouvernance ; mettre à jour la table de lecture en conséquence ;
  - **traiter la convergence des résultats** en premier : usage de la liste des tendances (effet de liste noire), mots et valeurs d’exemple recopiés, exemples recopiables ; examiner d’abord l’effet de mon ajout « signaux de page » ;
  - réécrire la skill : plus courte, organisée par chemin d’effort, avec la consigne « réponds dans la langue de la demande » ;
  - rendre systématiques et légères les étapes qui changent le résultat : direction, typographie, style, palette, retouche sur capture ;
  - ajouter les **mécanismes de variété** : envisager plusieurs directions distinctes avant de choisir, repérer ses propres choix par défaut, et remonter à ce que la demande a de propre ;
  - intégrer la **barre produit** dans le chemin par défaut : rendu vérifié sur ordinateur et sur mobile, états, interactions, contenu crédible, accessibilité de base, composants cohérents ;
  - ajouter un mode dégradé explicite : sans navigateur, sans assets, avec un autre agent.
- **Mesure, si tu l’acceptes :** un run par demande (facturation, natation) pour la qualité, et deux runs sur une même demande pour la variété. Soit trois ou quatre runs, au lieu des quatre runs plus juges qu’on avait envisagés.
- **Fin :** skill réécrite, contrôles verts, et mesure faite ou explicitement reportée.
- **Risque :** une skill plus courte qui active moins. Parade : la mesure, et le retour arrière possible en un commit.

### Phase 6 — Identité visuelle et supports

Cette phase peut avancer en parallèle des phases 3 à 5, une fois la phase 2 validée.

- **But :** que le système soit beau et que ses schémas aident vraiment.
- **Contenu :**
  - **Une identité visuelle du système :** typographie, couleurs, style de schéma, clair et sombre.
  - **Les schémas refaits avec cette identité :**
    - la carte du système ;
    - le parcours d’un travail, de la demande à la livraison ;
    - la boucle « créer puis apprendre » ;
    - l’architecture des fichiers ;
    - les chemins par effort.
  - **Les gabarits présentés proprement :** Creative Boot, cadrage de domaine.
  - **Une version consultable** du système pour les humains, si tu la veux : un petit site généré à partir des sources, jamais tenu à la main.
- **Règle :** chaque schéma garde son équivalent écrit, pour les agents et pour l’accessibilité.
- **Livrables :** schémas en SVG livrés avec le système, carte mise à jour, et éventuellement la version consultable.
- **Fin :** chaque support respecte l’identité, est lisible en clair et en sombre, et a son équivalent écrit.
- **Risque :** de la décoration qui alourdit. Parade : un schéma n’existe que s’il explique mieux que le texte.

### Phase 7 — Anglais

- **But :** rendre le système accessible en anglais sans double maintenance fragile.
- **Contenu :**
  - traduire d’abord les portes d’entrée et les guides, puis le reste ;
  - un contrôle de parité vérifie que les deux langues ont les mêmes sections, les mêmes adresses de route et les mêmes liens ;
  - le lecteur de routes fonctionne dans les deux langues.
- **Fin :** la parité est contrôlée et verte.
- **Décision pour toi :** tout traduire, ou seulement les entrées et le savoir.
- **Risque :** les deux versions divergent avec le temps. Parade : le contrôle de parité, et le français déclaré source.

### Phase 8 — Emballage et version

- **But :** un produit propre, présentable et installable.
- **Contenu :**
  - choisir le nom de version (1.1 ou 2.0) ;
  - écrire l’installation par public ;
  - refaire le README et un journal des versions court ;
  - livrer un zip propre ;
  - faire une vérification finale avec la grille du système.
- **Fin :** le zip passe tous les contrôles et la grille du système.

## 7. Ordre et dépendances

```text
0 Charte ─▶ 1 Audit ─▶ 2 Architecture ─┬─▶ 3 Rangement ─▶ 4 Langue FR ─▶ 5 Chemin de l’agent ─▶ 7 Anglais ─▶ 8 Emballage
                                        └─▶ 6 Visuel (en parallèle, une fois l’architecture validée) ───────────────┘
```

**Pourquoi cet ordre :**
- on range avant de réécrire, pour ne pas réécrire ce qui va bouger ;
- on écrit en français clair avant de traduire, pour ne pas traduire deux fois ;
- on touche à la skill en dernier, parce qu’elle change le comportement de l’agent ;
- le visuel dépend de l’architecture, pas de la langue.

## 8. Les décisions qui te reviennent

| Quand | Décision |
|---|---|
| Phase 0 | Charte, publics, grilles |
| Phase 1 | Disposition de chaque fichier |
| Phase 2 | Architecture, vocabulaire, contrôles retirés, gouvernance en module dans le même paquet ou en paquet séparé |
| Phase 5 | Faire ou non la petite mesure (trois ou quatre runs) |
| Phase 6 | Identité visuelle ; version consultable ou non |
| Phase 7 | Étendue de la traduction |
| Phase 8 | Nom de version |

## 9. Risques et parades

| Risque | Parade |
|---|---|
| Perdre du savoir en rangeant | Table de correspondance, contrôle « rien ne manque », fond intouché en phases 3 et 4 |
| Changer le comportement sans le voir | Comportement touché seulement en phase 5, mesure légère, retour arrière en un commit |
| Refonte trop longue, jamais finie | Chaque phase livre un système utilisable ; on peut s’arrêter après n’importe quel lot |
| Trop de contrôles retirés, régressions | Contrôles structurels gardés (liens, construction de la skill, routes, lecteur, rendu), preuve d’efficacité pour chacun |
| Beau mais lourd | Un schéma ou un support n’existe que s’il explique mieux, avec un équivalent écrit |
| Deux langues qui divergent | Français source, contrôle de parité |
| Coût en jetons | Pas de run hors phase 5 ; audits faits par lecture et outils, pas par production |

## 10. Effort estimé

Ce sont des ordres de grandeur, sans run.

| Phase | Volume de travail | Commits sur la branche |
|---|---|---|
| 0 | Court | 0 (documents sur `refonte`) |
| 1 | Moyen | 0 |
| 2 | Moyen | 0 |
| 3 | Important : le plus gros | 5 à 8 |
| 4 | Important | Un par fichier ou groupe de fichiers |
| 5 | Moyen, plus la mesure éventuelle | 2 à 4 |
| 6 | Moyen | 2 à 4 |
| 7 | Important si tout est traduit | 2 à 5 |
| 8 | Court | 1 à 2 |

## 11. Hors de ce plan

- Les mesures larges avec juges : seule la petite mesure de la phase 5 reste possible.
- Les ajouts de savoir nouveau, sauf ce qui est déjà décidé. Les points reportés (registre et chaleur sans photo, échéance des marqueurs de tendance, texte tronqué dans la vérification du rendu, second test de trouvabilité) sont rangés dans l’audit de la phase 1 et traités s’ils relèvent du nettoyage.
- Toute publication ou PR sans ta demande.
