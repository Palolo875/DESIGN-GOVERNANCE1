# Architecture cible du système

**Statut :** architecture validée, rangement réalisé ; exigences actualisées pour la suite de la phase 5.
**Documents liés :**
- [`vocabulaire.md`](vocabulaire.md) : des codes aux noms clairs ;
- [`correspondance.md`](correspondance.md) et `correspondance.csv` : la table historique des 388 sections ; [complément de phase 5](correspondance-phase5.csv) pour les blocs désormais activés à la demande ;
- [charte](../PLAN/charte.md) ;
- [synthèse de l’audit](../AUDIT2/synthese.md).

---

## 0. Décisions de la phase 1 (tu m’as laissé le choix)

| # | Question | Choix | Pourquoi |
|---|---|---|---|
| 1 | Séparer design et gouvernance | **Oui**, dans DIRECTION, ACTION, BIBLIOTHEQUE et la part concernée de SAVOIR | C’est la condition pour que le design soit au cœur et la gouvernance adaptée au travail (charte 2) |
| 2 | Deux distributions ou une | **Une seule arborescence**, identique dans le dépôt et les exports. Le Local retire la configuration Git/CI et les outils de préparation : 103 fichiers contre 108 pour GitHub | Deux arborescences imposaient de réécrire les chemins et rendaient les outils conditionnels. Le manifest déclare les cinq différences de distribution |
| 3 | Connexions C01 à C09 | **Ce sont du savoir.** Elles deviennent un chapitre du savoir (« quand plusieurs domaines se croisent »), gardé entier et consultable avec `--connexions` | Les répartir entre propriétaires romprait leur nature transversale ; les laisser dans une « carte » les cache |
| 4 | Copie Markdown de l’outil de livraison | **Retirée.** En phase 8, une version en un seul fichier, générée et lisible, pourra la remplacer pour les agents sans accès aux fichiers | Elle embarque un script de restauration complexe et double la maintenance |
| 5 | Corrections de fond en phase 5 | **Oui**, sans exception : convergence, exemples, valeurs recopiables, et mon ajout récent des « signaux de page » (examiné en premier) | La charte interdit de changer le fond pendant le rangement |

## 1. L’arborescence livrée

Cet arbre décrit `R2026-10-10-PHASE5`. Les fichiers de la cible initiale qui n’ont pas été créés séparément ne sont pas présentés comme existants ; leur matière reste accessible par les routes propriétaires et les sections conservées.

```text
README.md                      Accueil : ce que c’est, les quatre portes, installer, limites (court)
guides/                        Les portes humaines
  commencer.md                   débutant : quoi demander, quoi fournir, ce qu’on reçoit, comment poursuivre
  designer.md                    designer : lire le savoir par sujet, combiner, connexions
  equipe.md                      équipe : travailler à plusieurs, activer la gouvernance, livrer
  glossaire.md
design/                        LE CŒUR
  README.md                      comment le design est organisé ; la boucle créer puis apprendre (schéma)
  direction/                     décider ce que la page doit être
    cadrer.md                      demande vague, cadrage du domaine
    diriger.md                     rôle, posture, lancement créatif, cible visuelle, atelier, direction divergente
    premier-objet.md               construire le premier objet complet, réutilisation située
    boucle.md                      créer puis apprendre : défaut principal, correction, réobservation
    standard.md                    standard de qualité visuelle, les cinq règles essentielles, invariants de jugement
  savoir/                        le livre de référence
    README.md                      préface, règles d’or, comment lire
    fondements.md  qualite-creative.md  composition.md  typographie.md
    images-et-sources.md  styles.md  systeme-de-design.md  contexte.md  techniques.md
    gout-et-tendances.md  connexions.md
  formes/                        les structures
    README.md
    choisir.md                     lire une structure, tension, signature, sélection, dérivation, signaux de convergence
    catalogue.md                   supports, grilles, scènes, séquence, objets, micro, modificateurs, composants, compatibilité
  produit/                       ce qui fait un vrai produit
    README.md
    premier-rendu.md               qualité attendue dès le premier rendu
    interface.md                   interface réelle, états, médium et capacité
    plancher.md                    plancher produit : accessibilité, contraste, contrôles applicables
    finition.md                    finition sur rendu, comparaison, atelier sur capture, passe créative, arrêt du polish
    preuve-visuelle.md             rendre la direction vérifiable, preuve dégradée sans navigateur
agent/                         Pour l’agent
  skill/                         la skill (SKILL.md compilé + références), à copier dans .claude/skills/
  chemins.md                     classer, choisir le chemin, quoi lire
  repondre.md                    la réponse à la personne, trace courte, checkpoint, droits et confidentialité
gouvernance/                   CONTRÔLES ET TRACE ADAPTÉS AU RISQUE ET AU TRAVAIL
  README.md                      quand l’activer et ce qu’il apporte
  principes.md  statuts.md  travail.md  verification.md  cloture.md  structure.md
  schemas/                       schémas, exemples et fichiers de test
  outils/                        validation des fiches et des contrats
maintenance/                   Faire évoluer le système
  README.md                      source de vérité, validation, distributions
  evolution.md                   règles d’évolution, cycle de vie des routes, budget
  versions.md                    journal des versions, court
V1/sections/                   sections conservées et carte dérivée ; même autorité que les sections déplacées
  DIRECTION.md  ACTION.md  SAVOIR.md  BIBLIOTHEQUE.md  READING_MAP.md  README.md
scripts/                       lecteur, vérification du rendu, construction de la skill, contrôles, tests
```

**Pourquoi cette forme.**
- **Cinq parties visibles à la racine, dans l’ordre d’importance.** Les guides et le design viennent d’abord. L’agent, la gouvernance et la maintenance suivent.
- **Le design est un dossier et non un fichier.** On voit tout de suite ses quatre familles : direction, savoir, formes, produit.
- **La gouvernance se charge selon le besoin.** Les vérifications applicables restent dues ; la trace complète est chargée pour un travail persistant, partagé, audité ou soumis à acceptation. Une exploration conserve une trace légère (critère S9).
- **Des fichiers découpés par usage.** Les gros fichiers restent servis section par section. Le chemin de l’agent fait 42 570 caractères ; il n’est pas chargé intégralement. La skill commune fait 18 241 caractères. Le rangement augmente le nombre de fichiers et réduit ce qu’il faut lire d’un coup ; le lecteur n’exige pas de connaître leur emplacement.

**Estimation historique de la répartition après rangement**, d’après la table de correspondance initiale ; ce tableau n’est pas une mesure de la révision actuelle :

| Partie | Caractères |
|---|---|
| Design | ~267 000 |
| Gouvernance | ~117 000 |
| Agent, dont la skill (43 000) | ~93 000 |
| Guides | ~54 000 |
| Maintenance | ~43 000 |
| Hors produit (historique) | ~13 000 |
| Retiré pour redite | ~10 000 |

La phase 4 réduite a clarifié les portes et les guides ; le bilan de phase 5 donne la mesure actuelle de la skill et des recettes de lecture.

## 2. Les quatre portes

| Porte | Fichier | Ce qu’on y trouve d’abord | Ensuite |
|---|---|---|---|
| Débutant | `guides/commencer.md` | Une page sans jargon : quoi demander, quoi fournir, ce qu’on recevra, comment poursuivre. Elle reprend la section « Commencer » actuelle, qui est déjà bonne | Rien d’obligatoire |
| Designer | `guides/designer.md` | La carte des sujets en clair (« couleur → `savoir/couleur` »), comment combiner selon le résultat cherché, les connexions | Le savoir, les formes, le produit |
| Équipe | `guides/equipe.md` | Quand activer la gouvernance, qui décide, ce qui est tracé, comment livrer | `gouvernance/` |
| Agent | `agent/skill/SKILL.md` | Le noyau, puis « quoi lire » selon le chemin | `agent/chemins.md`, puis les routes |

Le README de la racine présente les quatre portes, l’installation et les limites. La révision livrée compte 7 774 caractères ; l’objectif initial d’environ 4 000 n’est pas déclaré atteint.

## 3. Les chemins selon l’effort

Les noms en clair remplacent les modes, qui restent internes à l’agent. Les cibles sont **provisoires** et portent sur la lecture avant production. Les chiffres de départ ci-dessous sont historiques ; les recettes mesurées après la suite de phase 5 sont décrites dans [le bilan](../PLAN/phase5-suite.md).

| Chemin | Modes actuels | Ce que l’agent lit avant de produire | Aujourd’hui | Cible provisoire |
|---|---|---|---|---|
| Retouche | `LITE`, `ITER` | la skill, plus la section du plancher ou de la finition concernée | ~59 000 à 65 000, dont 0 de design ou de produit | ≤ 35 000, dont 100 % design et produit |
| Page ou écran | `STANDARD`, `DIRECTION` | la skill, plus direction, typographie, premier rendu, interface, finition ; le reste seulement si ça change une décision | ~103 000, dont 23 % de design | ≤ 75 000, dont ≥ 85 % design et produit |
| Produit livré | `DIRECTION` en trace complète | la page, plus les parties utiles du module | ~138 000 | ≤ 110 000 |
| Système de design | `SYSTÈME` | la skill, plus système de design et composants | à mesurer | à fixer après mesure |

**Pendant le rangement, le chemin réel de l’agent est resté identique.** La suite de phase 5 compile désormais vingt blocs communs et active les vingt-trois autres dans leurs routes propriétaires. La table reste unique ; le lecteur sert seulement la ligne du mode classé. Les cibles initiales ne sont pas déclarées atteintes à partir d’une mesure qui inclut aussi les contrôles après production. On ne retire pas une protection pour atteindre un nombre.

## 4. Le module de gouvernance

**Ce qu’il contient :**
- statuts et verdicts formels ;
- conditions de départ ;
- fiche de travail ;
- clôture et test de sortie ;
- vérification en contexte (familles de preuve, regard extérieur) ;
- dérogation ;
- contrats de structure ;
- intégrité (contrôle, délégation) ;
- projection machine ;
- schémas, et les outils qui les valident.

**Ce qui reste hors module, parce que c’est du produit ou de l’honnêteté de base :**
- le plancher produit et la finition ;
- la réponse à la personne et la trace courte ;
- le principe « dire ce qu’on n’a pas pu vérifier » ;
- l’accord avant toute action irréversible ;
- les droits et la confidentialité en version courte ;
- la preuve dégradée sans navigateur.

**La règle de séparation, vérifiée par un contrôle :**
- les fichiers de `design/`, `agent/` et `guides/` (sauf `equipe.md`) peuvent citer le module (« pour aller plus loin ») ;
- ils exigent seulement les parties nécessaires au risque, à la décision, à la reprise ou à l’acceptation ;
- la table de chargement distingue la preuve applicable, la trace légère et la trace complète, quel que soit le mode.

**Le paquet entier reste nécessaire aux routes qu’il active.** Une dépendance requise absente devient une limite explicite ; elle n’est jamais remplacée par une promesse de conformité. Le rangement séparé des dossiers n’implique pas que l’on puisse retirer physiquement le module sans vérifier les dépendances.

## 5. Le modèle de section

Chaque route suit la même ouverture courte, puis son contenu :

```text
## <Titre en clair>
<!-- adresse : savoir/couleur ; ancien : SAVOIR/CRAFT/CFT-05 -->
À quoi ça sert, en une phrase. Quand l’ouvrir, en une phrase.

<le contenu, inchangé sur le fond>

(si utile) **Pièges.** … **Ce qui montre que c’est réussi.** …
```

Les rubriques « Pièges » et « Ce qui montre que c’est réussi » ne sont pas obligatoires. On les écrit seulement quand le contenu existe déjà quelque part ; on n’invente rien pour remplir le modèle, ce qui éviterait aussi le slop procédural que le savoir dénonce lui-même.

Chaque fichier commence par une phrase sur son rôle et son public, puis par un sommaire si le fichier compte plus de trois sections.

## 6. Adresses, lecteur et skill

- **Adresses.** `dossier/fichier` ou `dossier/fichier#section`, en français et en minuscules (`savoir/couleur`, `produit/plancher`, `formes/catalogue#grilles`). Le lecteur accepte aussi les anciennes adresses comme alias, avec un message « ancienne adresse → nouvelle ». Il les accepte pendant toute la V1 et les retire seulement en V2.
- **Lecteur.**
  - Il cherche aussi les phrases : chaque mot significatif, avec ses synonymes, classé par le nombre de mots trouvés dans une même section.
  - Son sommaire suit la nouvelle arborescence.
  - Son option `--connexions` lit `design/savoir/connexions.md`.
- **Skill.**
  - Les blocs du noyau gardent leurs noms internes.
  - `build_core.py` les lit à leur nouvelle place.
  - Pendant les phases 3 et 4, un contrôle vérifie que la skill compilée reste **identique à l’octet près**. Le rangement ne change donc rien pour l’agent.
  - La skill ne change qu’en phase 5.

## 7. Les langues

- **Le français est la source.** Les adresses sont les mêmes dans toutes les langues (`savoir/couleur`) ; seuls les titres et le texte sont traduits.
- **L’anglais vit dans `en/`**, qui reprend `guides/`, `design/` et le README. La phase 7 dira s’il faut aussi traduire `gouvernance/` et `maintenance/`.
- **Un contrôle de parité** vérifie que les deux langues ont les mêmes sections, les mêmes adresses et les mêmes liens.
- **La skill demande à l’agent de répondre dans la langue de la personne** (phase 5).

## 8. Les contrôles cibles

| Groupe | Aujourd’hui | Cible | Contrôles |
|---|---|---|---|
| Structure utile | ~112 | gardés, adaptés aux nouveaux chemins | liens ; skill compilée (identique à l’octet près en phases 3 et 4) ; budget de la skill ; adresses et alias résolvables ; lecteur ; vérification du rendu |
| Phrases verrouillées | ~252 à l’audit initial | protéger le sens sans figer la formulation | Chaque règle importante garde un propriétaire et un contrôle avec une mutation rouge. Les verrous qui ne protègent qu’une formulation peuvent être retirés avec une raison ; aucun quota de retrait |
| Gouvernance | ~122 à l’audit initial | conserver les invariants utiles, réduire les doublons prouvés | schémas, fiches, contrats ; leur validation protège le paquet livré, leur activation dans un run dépend du besoin |
| Nouveaux | — | ~6 | correspondance complète ; rien de perdu (chaque paragraphe ancien retrouvé ou retiré avec sa raison) ; séparation du module ; parité des langues (phase 7) ; mode lecture seule ; installation depuis le zip |

L’ancienne estimation de 490 à 300 contrôles n’est plus une cible. Le nombre de fichiers de test n’établit pas une redondance. Chaque contrôle gardé ou adapté protège un défaut identifié ; une mutation doit faire échouer la protection correspondante. Le coût se mesure séparément.

## 9. Le rangement (phase 3), précisé par l’audit

Chaque lot est un commit annulable.

| Lot | Contenu | Garde-fou |
|---|---|---|
| 0 | **Outils de sécurité.** Contrôle « rien de perdu » au niveau du paragraphe (empreinte de chaque paragraphe actuel, retrouvée dans le nouvel arbre ou listée comme retirée avec sa raison) ; contrôle d’identité de la skill ; mode de validation en lecture seule | mutation rouge de chaque nouveau contrôle |
| 1 | **Indépendance d’emplacement et registre des verrous.** Une seule table (`LIEUX`, dans le lecteur) dit quels fichiers portent aujourd’hui le contenu de chaque ancien fichier ; lecteur, compilation du noyau et validateurs passent par elle. Registre des ~270 chaînes verrouillées (`RANGEMENT/verrous.csv`). La conversion des verrous de formulation en règles protégées se fait fichier par fichier en phase 4, texte en main, car c’est la réécriture, pas le déplacement, qui les casse *(précisé le 9 octobre, au lot 1)* | test de déplacement simulé ; tous les contrôles verts ; skill identique |
| 2 | **Outils.** Adresses et alias dans le lecteur, recherche par phrases, une seule liste de fichiers, correction de l’installation | tests du lecteur ; second jeu de recherche (3 sur 150 aujourd’hui) |
| 3 | **Vestiges et historique.** On retire le fichier-pointeur, on sort le journal de décisions du produit, on réduit les notes de version | rien de perdu ; liens |
| 4 | **Gouvernance vers le module** | skill identique à l’octet près ; séparation |
| 5 | **Design** : direction, savoir, formes, produit, et application du modèle de section (ouvertures seulement) | rien de perdu ; skill identique |
| 6 | **Agent** : chemins et réponse ; la table de chargement pointe vers les nouvelles adresses | skill identique ; lecteur |
| 7 | **Portes** : README, guides, glossaire | lecture débutant en moins de cinq minutes (S3) |

**Ordre.** Les lots 0 à 2 rendent le rangement sûr et bon marché. Les lots 3 à 7 déplacent sans réécrire. La réécriture en clair viendra en phase 4.

**Précision du 9 octobre (lot 4).** Le rangement ne déplace que des sections entières dont le déplacement laisse identique le texte que sert chaque route (contrôle `RANGEMENT/servi.py`). Les dispositions « scinder » de la table de correspondance — sections qui mêlent design, produit et gouvernance — changent ce que lit l’agent : elles passent en phase 5, avec la skill et la table de chargement. Un fichier qui reçoit plusieurs sources marque l’origine de chaque section (`<!-- origine:… -->`).
## 10. Risques propres à cette architecture

| Risque | Parade |
|---|---|
| Trop de fichiers | Un sommaire par dossier ; le lecteur sert par adresse ; aucun fichier sous ~2 000 caractères sans raison. Les plus petits (couleur, système de design) sont des sujets majeurs pour un designer et grossiront peut-être en phase 5 |
| Les anciennes adresses cassent des usages (skills installées, notes) | Alias acceptés pendant toute la V1, avec un message de redirection |
| Le module devient un fourre-tout | Son README dit ce qu’il contient et quand l’activer ; sa taille est suivie |
| Une section scindée perd sa cohérence | Le lot qui la scinde relit la section entière et garde un renvoi entre les deux moitiés |
| Le chemin « quoi lire » (~34 000 caractères) reste lourd | C’est un sujet de la phase 5 ; le rangement ne le touche pas |

## 11. Ce qui vient ensuite

L’architecture et le rangement sont réalisés. La suite de phase 5 a son [bilan et ses limites](../PLAN/phase5-suite.md). La comparaison indépendante de qualité et de variété reste ouverte ; elle doit conserver les mêmes briefs, capacités et critères, puis faire juger les rendus sans révéler la version du système. La phase 6 conserve son périmètre minimal et l’anglais reste reporté. La PR du produit attend sa fusion vers `main`.
