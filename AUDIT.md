# Audit du système

Ce fichier conserve les constats de l’audit de Design Governance, lot par lot. Les actions qui en découlent sont suivies dans `SUIVI.md`. On constate pendant l’audit ; on corrige ensuite, par lots.

## Méthode

**Perspectives.**

| Code | Perspective | Question |
|---|---|---|
| P1 | Mission | La section sert-elle Q1 (orienter les choix), Q2 (mobiliser les moyens) ou Q3 (atteindre le niveau visé) ? Quelle décision change-t-elle ? |
| P2 | Mobilisation | Est-elle atteinte au bon moment (noyau, tronc, signal, renvoi) et à quel coût de lecture ? |
| P3 | Justesse du savoir | Exacte, à jour, sourcée, de niveau senior, sans dogme ni goût réflexe ? |
| P4 | Cohérence | Contradictions, doublons, source unique, vocabulaire stable, renvois valides ? |
| P5 | Exécutabilité | Claire, actionnable, sans ambiguïté pour un agent ; résiste-t-elle à l’agent qui coche sans concevoir ? |
| P6 | Proportionnalité | La règle mérite-t-elle sa place, son poids et son jargon ? |
| P7 | Vérité des affirmations | Ce que le système dit de lui-même correspond-il à ce qui est vérifiable ? |
| P8 | Lisibilité humaine | Pour les fichiers destinés aux personnes (niveau 3). |

**Gravités.** `Bloquant` : une promesse essentielle ne tient pas ou une obligation est inapplicable. `Important` : un défaut qui fragilise un run ou induit l’agent en erreur. `Mineur` : un défaut local sans effet probable sur un run. `Question` : un point à trancher, pas forcément un défaut.

**Format d’un constat.** Identifiant (`L<lot>-<n>`), gravité, perspectives, emplacement (`fichier:ligne`), preuve, effet, proposition.

**Couverture.** Chaque fichier lu est inscrit avec le commit, les lignes lues et les perspectives appliquées. Une deuxième passe, transversale par perspective, suivra la lecture fichier par fichier.

## Couverture

| Fichier | Commit | Lignes lues | Lot | Perspectives | Date |
|---|---|---|---|---|---|
| `SKILL.md` | `c77a8bc` | 1–190 (entier) | 1 | P1–P7 | 2026-10-22 |
| `agent/chemins.md` | `c77a8bc` | 1–397 (entier) | 1 | P1–P7 | 2026-10-22 |

## Lot 1 — noyau et chemins de l’agent

**Synthèse.** Le noyau oriente bien les choix (Q1) : la première proposition vaut checkpoint, la question de convergence, le marquage de vérité et la protection de niveau sont clairs et utiles. La mobilisation (Q2) est fragilisée : une partie des règles de routage, dont des obligations `[FORCÉ]`, n’est servie par aucune route, et cinq tables de routage divergent alors que chacune affirme ne pas en être une seconde. La déclaration de lancement est sur-spécifiée : six formats se recouvrent, dont certains contredisent la trace légère de six lignes.

### L1-01 · Bloquant · P2, P4 — Des obligations `[FORCÉ]` hors de toute route

- **Où.** `agent/chemins.md:217-272` : sections « 0. Classification du mode, preuve et capacité » (avec « ITER se souvient ») et « 2. Routage — quoi charger et quand » (« Déclencheurs critiques », « Index à la demande »).
- **Preuve.** Aucune des 74 routes ne sert ces sections ; `read_route.py --trouver "théâtre procédural"` les marque « (hors route) » (lignes 248 et 269). Elles portent pourtant des obligations : ligne 249, « Doute sur l’application d’une règle → `SAVOIR/INTEGRITY` `[FORCÉ]` » ; ligne 252, « Motif possiblement générique → `ACTION/ANTI-SLOP` `[REQUIS PAR LE MODULE]` » ; ligne 229, la condition d’entrée d’`ITER`.
- **Effet.** Un agent qui suit le système (noyau, ligne du mode, tronc) ne lit jamais ces obligations. La règle du noyau « toute contrainte critique est lue avant le choix qu’elle protège » ne tient pas pour elles.
- **Proposition.** Rattacher ce qui reste utile à `DIRECTION/START` ou `DIRECTION/CHARGE`, supprimer ce qui double d’autres tables (voir L1-02), et ajouter au validateur un contrôle qui refuse une obligation `[FORCÉ]` ou `[REQUIS]` hors route.

### L1-02 · Important · P2, P4 — Cinq tables de routage qui divergent

- **Où.** Signaux du noyau (`SKILL.md:158-179`, compilés depuis `agent/chemins.md:177-198`) ; ligne de chargement (`agent/chemins.md:157-163`) ; « Déclencheurs critiques » (`:242-253`) ; « Index à la demande » (`:257-270`) ; `ACTION/ROUTING` (`:349-360`).
- **Preuve.** Chacune déclare ne pas former une seconde liste (lignes 154, 240, 347), mais leurs correspondances diffèrent. Mouvement, responsive, performance : `SAVOIR/CONTEXT` dans l’index et `ACTION/ROUTING`, absent du noyau et de la ligne de chargement. Motif générique : `CFT-01` dans le noyau, `CFT-01` plus `ACTION/ANTI-SLOP` obligatoire dans les déclencheurs. Couleur : `CFT-05` dans le noyau, `SAVOIR/CRAFT`, `SAVOIR/SYSTEM` et la politique de contraste dans `ACTION/ROUTING`. Doute d’application : `SAVOIR/INTEGRITY` `[FORCÉ]` absent du noyau.
- **Effet.** L’agent ne voit que la table du noyau ; les autres correspondances sont invisibles (L1-01) ou ne s’atteignent qu’en lisant une route secondaire. C’est une cause directe du constat C4 du suivi (routes atteintes seulement en cascade).
- **Proposition.** Une seule table de signaux, celle du noyau, enrichie de ce qui manque ; les autres supprimées ou générées à partir d’elle.

### L1-03 · Important · P6, P5, P4 — Six formats de déclaration au lancement

- **Où.** Absolu 4 en une ligne (`SKILL.md:28`) ; « Entrée minimale », six champs dont `OWNER` et `SCOPE` « jamais omis » (`agent/chemins.md:37-48`) ; Creative Boot, douze champs (`:54-69`) ; ligne `RUN`, six cases, qui « doit exister dès qu’une action de production […] commence » (`:111-115`) ; `DECISION-INTENT` « au lancement » (`:117-119`) ; mémoire de lancement, dix champs, dont la ligne `RUN` « est l’affichage » alors qu’elle n’en montre que cinq plus un état (`:129`) ; trace légère de six lignes au plus (`SKILL.md:152`).
- **Preuve.** La ligne `RUN`, `DECISION-INTENT` et l’entrée minimale ne prévoient aucune exception pour la trace légère, alors que le noyau limite celle-ci à six lignes.
- **Effet.** En trace légère, l’agent ne sait pas ce qu’il doit écrire : soit il écrit tout et alourdit la trace, soit il choisit et laisse d’autres obligations non tenues. `OWNER` n’a pas de sens évident pour un agent seul.
- **Proposition.** Une seule déclaration de lancement, définie une fois (la ligne de l’absolu 4, plus la trace légère) ; les autres formats deviennent des projections réservées à la trace complète, dites comme telles.

### L1-04 · Important · P5, P4 — Plusieurs cadres de pensée sans relation déclarée

- **Où.** `SKILL.md:38` (situation, tension, geste produit, objet de preuve, marquage de vérité, position/exclusion, contre-choix situé) ; `:48` (six paires de caractère) ; `:52-60` (sept axes de tension) ; `:64` (séquence de composition en dix temps) ; `:78` (formule de la forme située) ; `agent/chemins.md:56-69` (champs du boot) ; `SKILL.md:152` (thèse ; modal, trame et parti).
- **Preuve.** Les mêmes notions changent de nom d’un cadre à l’autre (geste produit et `GESTURE`, contre-choix situé et `PARTI`, tension et `STRUCTURAL-TENSION`). « Trame » est une ligne de la trace légère mais n’est définie nulle part comme champ ; ailleurs, le mot désigne une matière (`design/direction/diriger.md:18`).
- **Effet.** L’agent doit deviner quel cadre appliquer et comment ils se correspondent ; un cadre rempli pour lui-même ressemble à l’« échappatoire théâtrale » que le système veut éviter.
- **Proposition.** Un vocabulaire unique de cadrage, défini une fois dans le noyau, et une phrase qui dit comment chaque cadre s’y rattache ; définir « trame » ou la retirer de la trace.

### L1-05 · Mineur · P4 — Le sens d’`EXPLORATORY` varie

- **Où.** `agent/chemins.md:212` et `gouvernance/statuts.md:33` : `EXPLORATORY` est « réservé au cas où un rendu observable existe mais qu’une preuve requise manque ». `SKILL.md:100` et `:152` : statut par défaut de toute proposition en trace légère et de toute direction sans ancre.
- **Effet.** Les deux lectures se concilient (une proposition légère manque des preuves d’acceptation), mais le texte ne le dit pas. Le même mot sert aussi d’issue, de verdict et de statut de direction (`gouvernance/statuts.md:24`, `:33`, `:71`).
- **Proposition.** Une phrase dans le noyau qui relie la proposition légère à la définition canonique.

### L1-06 · Mineur · P4 — Renvois périmés

- **Où et preuve.**
  - `agent/chemins.md:31`, `:264`, `:358` renvoient à « la section `DESIGN-ATLAS` de `SAVOIR.md` » ; la route vit dans `design/savoir/images-et-sources.md` (`read_route.py SAVOIR/DESIGN-ATLAS`).
  - `agent/chemins.md:397` : « Les routes stables suivantes sont les routes quotidiennes. » Rien ne suit : c’est la dernière ligne du fichier.
  - `agent/chemins.md:10` : un conflit avec `START` « est inscrit dans `maintenance/versions.md` », alors que cette fiche « ne retrace pas son histoire » (`maintenance/versions.md`, introduction).
- **Proposition.** Corriger les trois renvois ; dire où un conflit s’inscrit.

### L1-07 · Mineur · P6 — Mode d’emploi des recettes dans le noyau

- **Où.** `SKILL.md:112` : options de `check_render.py` (`--click`, `--captures`, `--baseline`, `--allow-external`, `--assert`, `--in-frame`) et de `check_caractere.py`, environ 1 200 caractères lus à chaque run.
- **Effet.** La notice complète a été sortie vers `ACTION/RECETTE-RENDU`, mais cette route n’est citée ni par le noyau ni par la ligne de chargement (constat C4) : le noyau reste le seul endroit où l’agent apprend les options. Les retirer couperait l’accès.
- **Proposition.** Garder dans le noyau la règle (preuve à l’état qui compte) et ajouter un signal « recette de rendu → `ACTION/RECETTE-RENDU` » ; alléger ensuite.

### L1-08 · Mineur · P5, P6 — Codes et anglicismes non définis dans le noyau

- **Où.** `SKILL.md:152` et `:178` (`B1b`), `agent/chemins.md:131` et `:225` (axes V/U/A/T), et passim : *blast radius*, *consumers*, *owner*, *JTBD*, *one-shot*.
- **Effet.** Faible pour un agent, réel pour une personne qui lit la skill ; `B1b` apparaît dans le noyau sans définition.
- **Proposition.** Une définition à la première occurrence dans le noyau, ou un renvoi au glossaire.

### L1-09 · Question · P4 — Une route normative dont l’adresse lisible est un guide

- **Où.** `read_route.py SAVOIR/ROUTING` : adresse `guides/2-comprendre#routes`, propriétaire `sections/SAVOIR.md`.
- **Question.** Les guides sont déclarés non normatifs (`README.md`, `sections/README.md`). Une route normative peut-elle avoir pour adresse lisible une section de guide ? À vérifier au lot 8.

### L1-10 · Question · P5 — Demander ou construire ?

- **Où.** `agent/chemins.md:23` : « Si aucune réponse n’est nette, pose une clarification ciblée […] Ne devine pas. » `SKILL.md:137` : « Une marque, un public ou une hypothèse nouvelle est nommée dans la proposition ; elle ne bloque pas le build. »
- **Question.** Les deux règles portent sur des objets différents (le mode, puis le contenu), mais un agent peut lire la première comme une invitation à questionner avant de construire. Faut-il préciser que la clarification ne concerne que le classement ?

### Ce qui tient (vérifié)

- Les clés du gabarit `DOMAIN-FRAME` (`agent/chemins.md:84-101`) sont exactement celles de `gouvernance/schemas/domain_frame.schema.json`, toutes requises.
- La description de la skill fait 429 caractères, sous la limite de 1 024 du format Agent Skills.
- La référence Tuch et al. (2012) du noyau (`SKILL.md:76`) est conforme à ce que j’en connais (première impression en une fraction de seconde, préférence pour une complexité faible et une forme prototypique) ; non revérifiée en ligne.
- Les routes dont la résolution était douteuse se résolvent : `DIRECTION/START/TREE`, `SAVOIR/DESIGN-ATLAS`, `SAVOIR/ROUTING`, `SAVOIR/SYSTEM`, `ACTION/PRECONDITION`, `ACTION/ANTI-SLOP`. Le reste des références est couvert par la validation du paquet.
