# Audit du système

Ce fichier conserve les constats de l’audit de Design Governance, lot par lot. Les actions qui en découlent sont suivies dans `SUIVI.md`. On constate pendant l’audit ; on corrige ensuite, par lots.

## Méthode

**Perspectives.** Les codes de perspective sont des abréviations de trois lettres, pour ne pas les confondre avec l’ordre de preuve `P0` à `P3` du système (`gouvernance/principes.md:19`).

| Code | Perspective | Question |
|---|---|---|
| MIS | Mission | La section sert-elle Q1 (orienter les choix), Q2 (mobiliser les moyens) ou Q3 (atteindre le niveau visé) ? Quelle décision change-t-elle ? |
| MOB | Mobilisation | Est-elle atteinte au bon moment (noyau, tronc, signal, renvoi) et à quel coût de lecture ? |
| SAV | Justesse du savoir | Exacte, à jour, sourcée, de niveau senior, sans dogme ni goût réflexe ? |
| COH | Cohérence | Contradictions, doublons, source unique, vocabulaire stable, renvois valides ? |
| EXE | Exécutabilité | Claire, actionnable, sans ambiguïté pour un agent ; résiste-t-elle à l’agent qui coche sans concevoir ? |
| PRO | Proportionnalité | La règle mérite-t-elle sa place, son poids et son jargon ? |
| VER | Vérité des affirmations | Ce que le système dit de lui-même correspond-il à ce qui est vérifiable ? |
| LIS | Lisibilité humaine | Pour les fichiers destinés aux personnes (niveau 3). |

**Gravités.** `Bloquant` : une promesse essentielle ne tient pas ou une obligation est inapplicable. `Important` : un défaut qui fragilise un run ou induit l’agent en erreur. `Mineur` : un défaut local sans effet probable sur un run. `Question` : un point à trancher, pas forcément un défaut.

**Format d’un constat.** Identifiant (`L<lot>-<n>`), gravité, perspectives, emplacement (`fichier:ligne`), preuve, effet, proposition.

**Couverture.** Chaque fichier lu est inscrit avec le commit, les lignes lues et les perspectives appliquées. Une deuxième passe, transversale par perspective, suivra la lecture fichier par fichier.

## Couverture

| Fichier | Commit | Lignes lues | Lot | Perspectives | Date |
|---|---|---|---|---|---|
| `SKILL.md` | `c77a8bc` | 1–190 (entier) | 1 | toutes | 2026-10-22 |
| `agent/chemins.md` | `c77a8bc` | 1–397 (entier) | 1 | toutes | 2026-10-22 |
| `design/direction/README.md` | `c77a8bc` | 1–11 (entier) | 2 | COH | 2026-10-22 |
| `design/direction/cadrer.md` | `c77a8bc` | 1–50 (entier) | 2 | toutes | 2026-10-22 |
| `design/direction/diriger.md` | `c77a8bc` | 1–134 (entier) | 2 | toutes | 2026-10-22 |
| `design/direction/premier-objet.md` | `c77a8bc` | 1–70 (entier) | 2 | toutes | 2026-10-22 |
| `design/direction/boucle.md` | `c77a8bc` | 1–80 (entier) | 2 | toutes | 2026-10-22 |
| `design/direction/standard.md` | `c77a8bc` | 1–115 (entier) | 2 | toutes | 2026-10-22 |
| `design/savoir/typographie.md` | `c77a8bc` | 1–53 (entier) | 2 | toutes | 2026-10-22 |
| `design/produit/premier-rendu.md` | `c77a8bc` | 1–46 (entier) | 2 | toutes | 2026-10-22 |
| `design/produit/plancher.md` | `c77a8bc` | 1–131 (entier) | 2 | toutes | 2026-10-22 |
| `design/produit/README.md` | `c77a8bc` | 1–12 (entier) | 3 | COH | 2026-10-22 |
| `design/produit/finition.md` | `c77a8bc` | 1–49 (entier) | 3 | toutes | 2026-10-22 |
| `design/produit/interface.md` | `c77a8bc` | 1–27 (entier) | 3 | toutes | 2026-10-22 |
| `design/produit/preuve-visuelle.md` | `c77a8bc` | 1–52 (entier) | 3 | toutes | 2026-10-22 |
| `agent/README.md` | `c77a8bc` | 1–11 (entier) | 3 | COH | 2026-10-22 |
| `agent/repondre.md` | `c77a8bc` | 1–47 (entier) | 3 | toutes | 2026-10-22 |
| `gouvernance/README.md` | `c77a8bc` | 1–25 (entier) | 3 | COH, LIS | 2026-10-22 |
| `gouvernance/principes.md` | `c77a8bc` | 1–44 (entier) | 3 | toutes | 2026-10-22 |
| `gouvernance/statuts.md` | `c77a8bc` | 1–84 (entier) | 3 | toutes | 2026-10-22 |
| `gouvernance/travail.md` | `c77a8bc` | 1–192 (entier) | 3 | toutes | 2026-10-22 |
| `gouvernance/verification.md` | `c77a8bc` | 1–226 (entier) | 3 | toutes | 2026-10-22 |
| `gouvernance/cloture.md` | `c77a8bc` | 1–102 (entier) | 3 | toutes | 2026-10-22 |
| `gouvernance/structure.md` | `c77a8bc` | 1–85 (entier) | 3 | toutes | 2026-10-22 |

## Lot 1 — noyau et chemins de l’agent

**Synthèse.** Le noyau oriente bien les choix (Q1) : la première proposition vaut checkpoint, la question de convergence, le marquage de vérité et la protection de niveau sont clairs et utiles. La mobilisation (Q2) est fragilisée : une partie des règles de routage, dont des obligations `[FORCÉ]`, n’est servie par aucune route, et cinq tables de routage divergent alors que chacune affirme ne pas en être une seconde. La déclaration de lancement est sur-spécifiée : six formats se recouvrent, dont certains contredisent la trace légère de six lignes.

### L1-01 · Bloquant · MOB, COH — Des obligations `[FORCÉ]` hors de toute route

- **Où.** `agent/chemins.md:217-272` : sections « 0. Classification du mode, preuve et capacité » (avec « ITER se souvient ») et « 2. Routage — quoi charger et quand » (« Déclencheurs critiques », « Index à la demande »).
- **Preuve.** Aucune des 74 routes ne sert ces sections ; `read_route.py --trouver "théâtre procédural"` les marque « (hors route) » (lignes 248 et 269). Elles portent pourtant des obligations : ligne 249, « Doute sur l’application d’une règle → `SAVOIR/INTEGRITY` `[FORCÉ]` » ; ligne 252, « Motif possiblement générique → `ACTION/ANTI-SLOP` `[REQUIS PAR LE MODULE]` » ; ligne 229, la condition d’entrée d’`ITER`.
- **Effet.** Un agent qui suit le système (noyau, ligne du mode, tronc) ne lit jamais ces obligations. La règle du noyau « toute contrainte critique est lue avant le choix qu’elle protège » ne tient pas pour elles.
- **Proposition.** Rattacher ce qui reste utile à `DIRECTION/START` ou `DIRECTION/CHARGE`, supprimer ce qui double d’autres tables (voir L1-02), et ajouter au validateur un contrôle qui refuse une obligation `[FORCÉ]` ou `[REQUIS]` hors route.

### L1-02 · Important · MOB, COH — Cinq tables de routage qui divergent

- **Où.** Signaux du noyau (`SKILL.md:158-179`, compilés depuis `agent/chemins.md:177-198`) ; ligne de chargement (`agent/chemins.md:157-163`) ; « Déclencheurs critiques » (`:242-253`) ; « Index à la demande » (`:257-270`) ; `ACTION/ROUTING` (`:349-360`).
- **Preuve.** Chacune déclare ne pas former une seconde liste (lignes 154, 240, 347), mais leurs correspondances diffèrent. Mouvement, responsive, performance : `SAVOIR/CONTEXT` dans l’index et `ACTION/ROUTING`, absent du noyau et de la ligne de chargement. Motif générique : `CFT-01` dans le noyau, `CFT-01` plus `ACTION/ANTI-SLOP` obligatoire dans les déclencheurs. Couleur : `CFT-05` dans le noyau, `SAVOIR/CRAFT`, `SAVOIR/SYSTEM` et la politique de contraste dans `ACTION/ROUTING`. Doute d’application : `SAVOIR/INTEGRITY` `[FORCÉ]` absent du noyau.
- **Effet.** L’agent ne voit que la table du noyau ; les autres correspondances sont invisibles (L1-01) ou ne s’atteignent qu’en lisant une route secondaire. C’est une cause directe du constat C4 du suivi (routes atteintes seulement en cascade).
- **Proposition.** Une seule table de signaux, celle du noyau, enrichie de ce qui manque ; les autres supprimées ou générées à partir d’elle.

### L1-03 · Important · PRO, EXE, COH — Six formats de déclaration au lancement

- **Où.** Absolu 4 en une ligne (`SKILL.md:28`) ; « Entrée minimale », six champs dont `OWNER` et `SCOPE` « jamais omis » (`agent/chemins.md:37-48`) ; Creative Boot, douze champs (`:54-69`) ; ligne `RUN`, six cases, qui « doit exister dès qu’une action de production […] commence » (`:111-115`) ; `DECISION-INTENT` « au lancement » (`:117-119`) ; mémoire de lancement, dix champs, dont la ligne `RUN` « est l’affichage » alors qu’elle n’en montre que cinq plus un état (`:129`) ; trace légère de six lignes au plus (`SKILL.md:152`).
- **Preuve.** La ligne `RUN`, `DECISION-INTENT` et l’entrée minimale ne prévoient aucune exception pour la trace légère, alors que le noyau limite celle-ci à six lignes.
- **Effet.** En trace légère, l’agent ne sait pas ce qu’il doit écrire : soit il écrit tout et alourdit la trace, soit il choisit et laisse d’autres obligations non tenues. `OWNER` n’a pas de sens évident pour un agent seul.
- **Proposition.** Une seule déclaration de lancement, définie une fois (la ligne de l’absolu 4, plus la trace légère) ; les autres formats deviennent des projections réservées à la trace complète, dites comme telles.

### L1-04 · Important · EXE, COH — Plusieurs cadres de pensée sans relation déclarée

- **Où.** `SKILL.md:38` (situation, tension, geste produit, objet de preuve, marquage de vérité, position/exclusion, contre-choix situé) ; `:48` (six paires de caractère) ; `:52-60` (sept axes de tension) ; `:64` (séquence de composition en dix temps) ; `:78` (formule de la forme située) ; `agent/chemins.md:56-69` (champs du boot) ; `SKILL.md:152` (thèse ; modal, trame et parti).
- **Preuve.** Les mêmes notions changent de nom d’un cadre à l’autre (geste produit et `GESTURE`, contre-choix situé et `PARTI`, tension et `STRUCTURAL-TENSION`). « Trame » est une ligne de la trace légère ; le mot désigne tantôt la « trame modale », ordre de sections que n’importe quelle IA produirait (`design/formes/choisir.md:242`), tantôt une matière (`design/direction/diriger.md:18`, `design/formes/choisir.md:194`). La trace ne dit pas lequel (précisé au lot 3 : le terme est défini, mais ambigu).
- **Effet.** L’agent doit deviner quel cadre appliquer et comment ils se correspondent ; un cadre rempli pour lui-même ressemble à l’« échappatoire théâtrale » que le système veut éviter.
- **Proposition.** Un vocabulaire unique de cadrage, défini une fois dans le noyau, et une phrase qui dit comment chaque cadre s’y rattache ; définir « trame » ou la retirer de la trace.

### L1-05 · Mineur · COH — Le sens d’`EXPLORATORY` varie

- **Où.** `agent/chemins.md:212` et `gouvernance/statuts.md:33` : `EXPLORATORY` est « réservé au cas où un rendu observable existe mais qu’une preuve requise manque ». `SKILL.md:100` et `:152` : statut par défaut de toute proposition en trace légère et de toute direction sans ancre.
- **Effet.** Les deux lectures se concilient (une proposition légère manque des preuves d’acceptation), mais le texte ne le dit pas. Le même mot sert aussi d’issue, de verdict et de statut de direction (`gouvernance/statuts.md:24`, `:33`, `:71`).
- **Proposition.** Une phrase dans le noyau qui relie la proposition légère à la définition canonique.

### L1-06 · Mineur · COH — Renvois périmés

- **Où et preuve.**
  - `agent/chemins.md:31`, `:264`, `:358` renvoient à « la section `DESIGN-ATLAS` de `SAVOIR.md` » ; la route vit dans `design/savoir/images-et-sources.md` (`read_route.py SAVOIR/DESIGN-ATLAS`).
  - `agent/chemins.md:397` : « Les routes stables suivantes sont les routes quotidiennes. » Rien ne suit : c’est la dernière ligne du fichier.
  - `agent/chemins.md:10` : un conflit avec `START` « est inscrit dans `maintenance/versions.md` », alors que cette fiche « ne retrace pas son histoire » (`maintenance/versions.md`, introduction).
- **Proposition.** Corriger les trois renvois ; dire où un conflit s’inscrit.

### L1-07 · Mineur · PRO — Mode d’emploi des recettes dans le noyau

- **Où.** `SKILL.md:112` : options de `check_render.py` (`--click`, `--captures`, `--baseline`, `--allow-external`, `--assert`, `--in-frame`) et de `check_caractere.py`, environ 1 200 caractères lus à chaque run.
- **Effet.** La notice complète a été sortie vers `ACTION/RECETTE-RENDU`, mais cette route n’est citée ni par le noyau ni par la ligne de chargement (constat C4) : le noyau reste le seul endroit où l’agent apprend les options. Les retirer couperait l’accès.
- **Proposition.** Garder dans le noyau la règle (preuve à l’état qui compte) et ajouter un signal « recette de rendu → `ACTION/RECETTE-RENDU` » ; alléger ensuite.

### L1-08 · Mineur · EXE, PRO — Codes et anglicismes non définis dans le noyau

- **Où.** `SKILL.md:152` et `:178` (`B1b`), `agent/chemins.md:131` et `:225` (axes V/U/A/T), et passim : *blast radius*, *consumers*, *owner*, *JTBD*, *one-shot*.
- **Effet.** Faible pour un agent, réel pour une personne qui lit la skill ; `B1b` apparaît dans le noyau sans définition.
- **Proposition.** Une définition à la première occurrence dans le noyau, ou un renvoi au glossaire.

### L1-09 · Question · COH — Une route normative dont l’adresse lisible est un guide

- **Où.** `read_route.py SAVOIR/ROUTING` : adresse `guides/2-comprendre#routes`, propriétaire `sections/SAVOIR.md`.
- **Question.** Les guides sont déclarés non normatifs (`README.md`, `sections/README.md`). Une route normative peut-elle avoir pour adresse lisible une section de guide ? À vérifier au lot 8.

### L1-10 · Question · EXE — Demander ou construire ?

- **Où.** `agent/chemins.md:23` : « Si aucune réponse n’est nette, pose une clarification ciblée […] Ne devine pas. » `SKILL.md:137` : « Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition ; elle ne bloque pas le build. »
- **Question.** Les deux règles portent sur des objets différents (le mode, puis le contenu), mais un agent peut lire la première comme une invitation à questionner avant de construire. Faut-il préciser que la clarification ne concerne que le classement ?

### Ce qui tient (vérifié)

- Les clés du gabarit `DOMAIN-FRAME` (`agent/chemins.md:84-101`) sont exactement celles de `gouvernance/schemas/domain_frame.schema.json`, toutes requises.
- La description de la skill fait 429 caractères, sous la limite de 1 024 du format Agent Skills.
- La référence Tuch et al. (2012) du noyau (`SKILL.md:76`) est conforme à ce que j’en connais (première impression en une fraction de seconde, préférence pour une complexité faible et une forme prototypique) ; non revérifiée en ligne.
- Les routes dont la résolution était douteuse se résolvent : `DIRECTION/START/TREE`, `SAVOIR/DESIGN-ATLAS`, `SAVOIR/ROUTING`, `SAVOIR/SYSTEM`, `ACTION/PRECONDITION`, `ACTION/ANTI-SLOP`. Le reste des références est couvert par la validation du paquet.

## Lot 2 — tronc DIRECTION

**Synthèse.** Le contenu du tronc est de bonne qualité : contrat positif du premier objet, routes de production honnêtes, priorité donnée à la vérité, plancher `GATE-A` à jour de WCAG 2.2 avec des profils de surface proportionnés. Deux défauts de mobilisation dominent : les cinq absolus, que le noyau cite, ne sont servis par aucune route, et une étape due en DIRECTION (l’atelier sur capture) n’est atteinte que par un signal. Avant le premier pixel, l’agent fait face à plusieurs listes de champs et d’axes qui se recouvrent (prolonge L1-04). Le savoir typographique du tronc dit quoi vérifier, pas comment choisir.

### L2-01 · Bloquant · MOB, COH, VER — Les cinq absolus sont hors route

- **Où.** `design/direction/standard.md:6-115` (sauf le bloc `ANCRE`, lignes 32-35, compilé dans le noyau) : « Les cinq règles absolues » et « Invariants de jugement ».
- **Preuve.** `read_route.py --trouver "ABSOLU 1"` : « 0 route(s) », ligne marquée « (hors route) » ; `read_route.py direction/standard` : « locator inconnu ». Le noyau y renvoie pourtant : `SKILL.md:24` (« reviens aux ABSOLUS 1 et 5 »), `:28` (« absolu 4 »), `:137` (« absolu 2 de `DIRECTION` »). Le README les présente comme le texte « qui fait foi ».
- **Effet.** La règle supérieure du système n’est pas lisible par le chemin prévu ; l’agent ne dispose que de renvois numérotés sans contenu. Le résumé du README existe, mais la skill dit de ne l’ouvrir qu’à la demande d’une personne (`SKILL.md:190`).
- **Proposition.** Compiler dans le noyau un énoncé court des cinq absolus (le résumé du README fait environ 1 000 caractères ; le noyau a 16 000 octets de marge) et servir le texte complet par une route. Étendre le contrôle de A9 à tout contenu normatif hors route.

### L2-02 · Important · MOB, EXE — « Direction divergente » est hors route

- **Où.** `design/direction/diriger.md:119-134`.
- **Preuve.** Aucune route ne sert ces lignes (relevé de couverture des routes). Elles portent des obligations : ligne 121, « Le mode `DIRECTION` exige une comparaison de positions réellement distinctes lorsque la décision est ouverte » ; ligne 128, la direction retenue « ne l’emporte que si son avantage est formulé en une phrase vérifiable » ; ligne 130, « L’axe matière doit toujours être déclaré ». `standard.md:57` y renvoie (« Direction divergente (déclenchement) »), lui-même hors route (L2-01).
- **Effet.** La règle qui déclenche l’alternative en DIRECTION n’est lue que par fragments, via `ACTION/PIPELINE-DIRECTION`.
- **Proposition.** Rattacher la section à `DIRECTION/VISUAL_TARGET` ou à `ACTION/PIPELINE-DIRECTION`, en la fusionnant avec le contre-choix situé de l’atelier (`diriger.md:95`), qui dit la même chose autrement.

### L2-03 · Important · EXE, COH — Trois listes d’axes, trois ordres de construction, quatre formulaires

- **Où.**
  - Axes : sept axes de tension (`SKILL.md:52-60`) ; six axes de position dont `SAVOIR/CRAFT/CFT-02` serait « le seul propriétaire » (`diriger.md:123`) ; huit axes pour « faire varier un axe situé à la fois » (`SKILL.md:127`).
  - Ordres : séquence de composition en dix temps (`SKILL.md:64`) ; compilation de la première proposition en dix temps, différents (`diriger.md:28`) ; priorités du brief vague en quatre temps (`cadrer.md:13-26`).
  - Formulaires avant le build : cible visuelle, onze champs, « seule représentation canonique » et « prête à construire lorsque chaque champ […] est renseigné ou `N/A-JUSTIFIED` » (`diriger.md:24`, `:71`) ; Creative Boot, douze champs (`agent/chemins.md:56-68`) ; atelier, quatre éléments (`diriger.md:88-93`) ; sept notions du premier objet (`premier-objet.md:9`).
- **Effet.** Prolonge L1-04 : avant le premier pixel en DIRECTION, l’agent dispose de plus de trente champs à renseigner et de trois façons d’ordonner son travail, sans règle qui dise lesquelles priment. Le risque est double : une trace remplie pour elle-même, ou des champs sautés au hasard.
- **Proposition.** Dans A11 : une seule liste d’axes, un seul ordre de construction, une seule cible (celle de `VISUAL_TARGET`), dont le boot et l’atelier deviennent des sous-ensembles nommés.

### L2-04 · Important · MOB, EXE — Une étape due, atteinte seulement par un signal

- **Où.** `design/direction/boucle.md:20` : en DIRECTION, l’arrêt « vient après le tour d’atelier sur capture (`ACTION/ATELIER-EDITION`), dû même en trace légère ».
- **Preuve.** `DIRECTION/DOUBLE-LOOP` n’est pas dans le tronc DIRECTION (chargement conditionnel, `agent/chemins.md:162`). Le noyau présente l’atelier comme un signal (« Comparaison sur capture en `DIRECTION` », `SKILL.md:178`) et non comme une étape.
- **Effet.** Un agent qui ne compare pas spontanément ne rencontre jamais le signal : l’étape due est sautée sans que rien ne le montre.
- **Proposition.** Énoncer l’étape dans `ACTION/RUN-DIRECTION` (tronc) ou dans la boucle du noyau ; la retirer du tableau des signaux.

### L2-05 · Important · SAV, MIS — Le savoir typographique dit quoi vérifier, pas comment choisir

- **Où.** `design/savoir/typographie.md` (53 lignes).
- **Preuve.** Le noyau exige de comparer « au moins deux voix typographiques distinctes sur le vrai titre » (`SKILL.md:94`), et `SAVOIR/TYPE` est dans le tronc DIRECTION précisément pour cela (« voix comparées sur le vrai titre », `agent/chemins.md:162`). La route contient des exigences (langues, chiffres, licence, fallback), l’équilibre d’un titre, le réglage d’un grand texte et la forme de la preuve ; rien sur la manière de trouver des voix candidates, de les apparier ou de les comparer. Une recherche (« deux voix », « paire typographique », « appariement ») ne trouve rien d’autre que la question de convergence et le registre de `SAVOIR/STYLE`.
- **Effet.** Sur la décision où le système redoute le plus le réflexe (la police de titre), il demande une comparaison sans donner de quoi la conduire ; Q1 et Q3 en dépendent directement.
- **Proposition.** Ajouter à `SAVOIR/TYPE` une méthode courte : d’où partir (contenu, langue, registre), deux ou trois familles de voix à opposer, comment comparer sur le vrai titre, et ce qui tranche. À confirmer au lot 4 (`SAVOIR/TOOLS/MOYENS`, `SAVOIR/STYLE`), qui peut contenir une partie de ce savoir.

### L2-06 · Mineur · MOB, PRO — Une voie concrète pour redonner de la marge au tronc DIRECTION

- **Où.** Sous-sections du tronc qui ne servent qu’en trace complète ou sur un signal déjà prévu : « Réserve `ANCHOR-GENERATED` en enjeu identitaire élevé » (1 400 caractères) et le passage à `SPECCED` (`diriger.md:67-73`) ; « Réutilisation située » (2 100) et « Grounding contestable » (600) de `DIRECTION/FIRST-OBJECT`, déjà atteints par le signal « Ancien projet, préférence… » du noyau ; « Décider la route de production » (2 700), utile seulement quand un asset est en jeu.
- **Effet.** Le tronc est à 98 % (C1) en partie à cause de contenu qui n’a pas à être lu à chaque run.
- **Proposition.** Pour A6 : sortir ces sous-sections du tronc en conservant leur activation ; jusqu’à environ 6 800 caractères de marge regagnés.

### L2-07 · Mineur · EXE, LIS — La notice de la recette tient en un paragraphe

- **Où.** `design/produit/plancher.md:88` : environ 4 500 caractères d’un seul tenant (contrôles, statuts, options, limites, `--mesures`).
- **Proposition.** La découper en listes : ce qui est contrôlé, ce que rend chaque statut, options, limites.

### L2-08 · Mineur · COH — Adresse lisible et fichier ne coïncident pas

- **Où.** `read_route.py DIRECTION/CREATIVE-BOOT` : adresse `direction/diriger#lancement`, propriétaire `agent/chemins.md`. `design/direction/README.md:8` annonce un « lancement créatif » dans `diriger.md`, qui n’en contient pas.
- **Proposition.** Même famille que L1-09 : faire coïncider adresse et fichier, ou corriger le README du dossier.

### L2-09 · Mineur · VER — La prise de brief promise n’est pas dans le noyau

- **Où.** La description de la skill promet une « prise de brief minimale » (`SKILL.md:3`) ; la règle (« au plus trois demandes, en un seul échange », build dans le même tour, `cadrer.md:29`) est un bloc de détail servi seulement par `DIRECTION/EXTERNAL-START`, sur le signal « brief vague » (`scripts/build_core.py`, `DETAILS`).
- **Effet.** Limité : le noyau dit déjà qu’une hypothèse nouvelle ne bloque pas le build (`SKILL.md:137`). Le plafond de trois demandes n’est lu que si l’agent reconnaît un brief vague.
- **Proposition.** Compiler le bloc `BRIEF` dans le noyau (environ 900 caractères).

### L2-10 · Question · SAV — La référence FTC contre Amazon

- **Où.** `design/produit/premier-rendu.md:42` : « Ces motifs ont été sanctionnés (FTC contre Amazon, septembre 2025) [VEILLE 2026-10]. »
- **Question.** À ma connaissance, l’affaire s’est conclue en septembre 2025 par un accord d’environ 2,5 milliards de dollars, dont une pénalité civile, sur l’inscription et la résiliation de Prime. « Sanctionnés » se défend ; préciser « accord » et le montant rendrait la mention vérifiable. Non revérifié en ligne.

### Ce qui tient (vérifié)

- `GATE-A` couvre les six critères ajoutés par WCAG 2.2 (focus non masqué, mouvement de glisser, taille des cibles, aide cohérente, saisie redondante, authentification accessible ; `plancher.md:60-67`) et traite WCAG 3.0 comme une veille.
- Les profils de surface de `GATE-A` (`plancher.md:70-77`) rendent le plancher proportionné sans l’affaiblir.
- Le validateur refuse bien une direction acceptée sans ancre, comme l’affirme `standard.md:49` (`gouvernance/outils/validate_run_card.py:437-439`).
- `ACTION/RECETTE-RENDU` est atteinte par un renvoi explicite de `GATE-A` (`plancher.md:79`), qui est dans le tronc de quatre modes : ce n’est pas une route orpheline (C4 corrigé pour elle).
- Le contrat positif du premier objet (`premier-objet.md:21-34`) donne des critères observables et un retour par dimension : un point fort pour Q3.
- `boucle.md:78-80` définit déjà ce qu’un run pilote doit conserver (défaut dominant, cause, correction, gain, régression, capacité manquante) : à reprendre tel quel dans le protocole de la campagne (A5).

## Lot 3 — production, réponse et gouvernance

**Synthèse.** La gouvernance tient sa promesse d’honnêteté : frontière de validation explicite, mode agent seul, distinction nette entre auto-comparaison et regard indépendant, et les affirmations contrôlées sur le validateur sont exactes. Le gate C montre un bon modèle de proportion (en trace légère, contrôle sans verdict écrit) et associe déjà chaque critère manqué à une route à charger. Trois défauts : de nouvelles sections hors route (le motif est systémique), des contrats de preuve dus à chaque run `STANDARD` ou `DIRECTION` sans dire ce qu’ils deviennent en trace légère, et un vocabulaire de statuts lourd, avec des homonymes. La campagne d’évaluation (A5) a déjà l’essentiel de son protocole dans le corpus.

### L3-01 · Important · MOB, COH — D’autres sections normatives hors route

- **Où.** `design/produit/interface.md:6-27` (cadrage de médium et de capacité, dont la règle « médium réel → capacité → preuve propre au médium → fallback » pour un médium non Web) ; `gouvernance/principes.md:6-31` (quatre registres, « Ordre de preuve » `P0` à `P3`, qui fait passer la protection critique avant l’optimisation visuelle, chargement d’ACTION) ; `gouvernance/cloture.md:85-102` (clôture de direction, « Lecture instrumentée et règle de passage », citée par `BIBLIOTHEQUE/EVOLUTION`) ; `gouvernance/structure.md:6-18` (« Entrée prioritaire — à lire avant le catalogue ») et `:71-85` (« Test de sortie BIBLIOTHEQUE »).
- **Preuve.** Relevé de couverture des routes : aucune route ne sert ces lignes. `interface.md` est entièrement hors route.
- **Effet.** Après les lots 1 et 2, le motif est systémique : des règles écrites pour l’agent ne lui parviennent par aucun chemin prévu. L’« entrée prioritaire » qui doit être lue avant le catalogue ne peut pas l’être.
- **Proposition.** Dans A9 : passer tout le corpus normatif au relevé de couverture lors de la passe transversale, puis rattacher, fusionner ou supprimer.

### L3-02 · Important · MOB, PRO — Des contrats dus à chaque run sans portée de trace

- **Où.** `gouvernance/verification.md:8-20` (`ACTION/STRUCTURED-PROOF`).
- **Preuve.** « Chacun n’est dû que si son déclencheur est actif » ; le déclencheur de la carte de hiérarchie (neuf rubriques) est « `STANDARD` ou `DIRECTION` », donc tout run de ces modes ; la partition typographique est requise dès que la famille ou le registre peuvent changer la décision, ce qui est presque toujours le cas en DIRECTION. Rien ne dit ce que ces contrats deviennent en trace légère, alors que le gate C le dit (`design/produit/finition.md:27` : « En trace légère, Gate C sert de contrôle de craft sur la capture […] aucun verdict n’est écrit »).
- **Effet.** Conflit avec la trace légère de six lignes : soit l’agent écrit ces contrats et alourdit chaque proposition, soit il les omet et laisse une obligation non tenue.
- **Proposition.** Aligner `STRUCTURED-PROOF` sur le gate C : en trace légère, les décisions de ces contrats sont tenues dans l’artefact, sans contrat écrit ; le contrat écrit relève de la trace complète. Cela règle aussi A8 pour cette route : elle est atteinte par `SAVOIR/TYPE` (`typographie.md:33`) et `ACTION/GATE-B/B2` (`verification.md:140`) ; le problème est sa portée, pas son accès.

### L3-03 · Important · PRO, EXE — Un vocabulaire de statuts lourd, avec des homonymes

- **Où.** `gouvernance/statuts.md` et voisins.
- **Preuve.** Sept états, six issues, six verdicts globaux, quatre statuts de direction, quatre axes à cinq statuts, cinq conséquences décisionnelles ; s’y ajoutent les statuts de B1b, les quatre dispositions d’une exception, les relations et expositions d’un regard externe (`verification.md:156-165`). Des homonymes : `RETURN` (statut d’axe et verdict global), `RETURNED` (issue), `RETURN-DIRECTION` (verdict) ; `EXPLORATORY` (issue, verdict, et statut de toute proposition légère, voir L1-05) ; `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED`. Le corpus doit répéter qu’il ne faut pas les confondre (`statuts.md:17`, `:39`, `:43`, `:45` ; `travail.md:178`).
- **Effet.** Le coût est confiné à la trace complète en principe, mais ces jetons apparaissent dans des routes lues en trace légère (par exemple le tableau de `ACTION/VISUAL_PROOF`, `preuve-visuelle.md:14-19`, en axes V/U/A/T).
- **Proposition.** Mesurer d’abord, dans la campagne (A5), si les agents emploient ces statuts correctement ; puis envisager de fusionner les homonymes entre issue et verdict.

### L3-04 · Mineur · COH, PRO — Le mode d’emploi de la recette de rendu existe en trois exemplaires

- **Où.** `SKILL.md:112`, `design/produit/preuve-visuelle.md:21` (environ 2 300 caractères), `design/produit/plancher.md:88`.
- **Proposition.** Avec L1-07 et L2-07 : une seule source (`ACTION/RECETTE-RENDU`), les autres citent la règle et renvoient.

### L3-05 · Mineur · COH — Un renvoi vague

- **Où.** `gouvernance/cloture.md:100` : la chaîne de lecture est définie « dans la constitution du document ». Elle se trouve dans `sections/DIRECTION.md:113`.
- **Proposition.** Nommer le fichier ou la route.

### Ce qui tient (vérifié)

- Frontière de validation (`gouvernance/travail.md:180-190`), mode agent seul (`:131-143`) et distinction entre auto-comparaison et regard indépendant (`gouvernance/verification.md:131`, `:146-169`) : le pilier d’honnêteté est solide.
- Les affirmations contrôlées sur le validateur sont exactes : `closure.b1b` exigé pour une direction acceptée avec V positif, captures distinctes (`gouvernance/outils/validate_run_card.py:388-400`) ; catégories de capacités disjointes (`:500-503`).
- Le gate C associe déjà chaque critère manqué à un geste et à une route à charger (`finition.md:16-23`) : c’est le modèle de mobilisation poussée que A1 propose d’étendre à `check_render.py`.
- `FAIL-ASSUMED` ne peut jamais couvrir un risque de sécurité, de dommage grave ou de conformité critique (`verification.md:214`).
- Le protocole de la campagne existe en grande partie : mesures de série (`cloture.md:78-80`), contrat `EVALUATION_CASE` pour un pilote (`verification.md:20`) et signaux d’apprentissage par run (`design/direction/boucle.md:78-80`).
