# Design Governance V1.0.0

**Révision : `R2026-10-08-ACCES-MATIERE` — activation, accès au savoir et matière.** Typographie chargée d’office et routes facultatives tranchées en mode `DIRECTION`, lecteur avec sommaire, synonymes, classement et carte des sujets, nouvelle route de séquence de page, compléments de craft, de sources et de vérité. Les formats et champs V1.0.0 sont conservés ; les protections des révisions précédentes restent actives. Limites : [notes de version](RELEASE_NOTES.md). L’historique des révisions de travail est tenu hors distribution.

Design Governance V1 est un cadre de **direction, de création, de jugement et de vérification du design**. Il aide à transformer un brief en décision située, artefact réel, observation pertinente et trace proportionnée au risque.

> **Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue. La baseline est contrôlée et destinée à un usage supervisé ; elle ne promet ni beauté automatique, ni réussite universelle, ni validation d’usage, ni conformité sans preuve adaptée.

<!-- entree:début -->
## Commencer

Design Governance aide un agent à produire un design dirigé, construit et soigné dès la première proposition, puis à l’améliorer avec vous. Vous n’avez besoin de connaître ni les modes, ni le vocabulaire interne : l’agent s’en charge.

**1. Que demander ?** Décrivez en quelques phrases ce que vous voulez obtenir (une page, un écran, une identité, une correction), pour qui, et où cela servira : démonstration, maquette ou vrai produit. S’il s’agit d’un vrai commerce ou d’un vrai service, dites-le.

**2. Que fournir ?** Ce que vous avez déjà : textes, prix, horaires, logo, couleurs, photos (même prises au téléphone, à la lumière du jour), exemples que vous aimez, lien vers l’existant. Vos textes, votre marque et vos photos aident à produire une proposition plus spécifique et crédible. S’il en manque, l’agent construit quand même une première proposition, avec des exemples marqués, et vous pose dans sa réponse au plus trois questions, seulement celles qui améliorent vraiment le résultat : contenu réel, marque, image principale ou source d’images autorisée, destination si elle est incertaine. Si vous préférez répondre avant qu’il construise, dites-le.

**3. Que recevoir ?** Une première proposition réellement construite, pas un gabarit vide. La réponse dit simplement ce qui a été fait et pourquoi, ce qui est un exemple à remplacer, ce qui manque pour la vraie version, et la suite proposée. C’est une proposition à discuter, pas une validation.

**4. Comment poursuivre ?** Validez pour continuer, réorientez ou arrêtez. Pour retenir cette direction pour votre vrai produit, dites-le : l’agent réunit alors les éléments réels et fait les vérifications nécessaires. Dites en une phrase ce qui ne va pas (« le titre écrase la photo », « trop froid pour une boulangerie ») : l’agent corrige le défaut principal, regarde de nouveau le résultat et vous dit ce qui a changé. Avant toute action irréversible ou coûteuse (publier, envoyer, payer, remplacer l’existant), il vous demande votre accord.

Pour aller plus loin : le [guide opérateur](guides/equipe.md), la [skill](agent/skill/SKILL.md) pour les agents, le [glossaire](guides/glossaire.md) et les [sources normatives](V1/official/README.md).
<!-- entree:fin -->

## Fiche de version

| Élément | État |
|---|---|
| Contrat documentaire et machine | Validé avec réserves explicites |
| Build et distributions | Révision contrôlée localement et distributions reproductibles ; exécution de la CI hébergée pour cette révision : `NOT-VERIFIED` |
| Architecture de lecture | Noyau de fabrication compilé ; liste de chargement unique ; carte dérivée disponible |
| Efficacité sur des runs réels | `NOT-VERIFIED` |
| Usage recommandé | Pilote contrôlé, revue humaine et preuve adaptée |

La carte [`V1/official/READING_MAP.md`](V1/official/READING_MAP.md) résout le premier chemin, l’activation multi-perspective, les handoffs et les locators principaux. Elle est dérivée et non normative. Les cinq sources officielles, le schéma `RUN_CARD` et leurs validateurs restent les autorités.

Pour exploiter plusieurs capacités sans les charger mécaniquement, utilisez la section « Combinaisons par résultat recherché » de la même carte. Cette vue dérivée compose les résultats recherchés, les capacités, les intensités, les patterns créatifs et la preuve ; elle ne crée aucun mode ni aucune règle concurrente.

## Mission

> Aider à créer des projets dirigés, construits et spécifiques, puis rendre visibles les décisions, les preuves et les limites qui permettent de les juger honnêtement.

Le corpus s’adresse à un designer, une équipe produit ou un agent qui doit produire un travail visuellement dirigé, spécifique, construit et poli, tout en rendant ses décisions, ses preuves et ses limites lisibles.

V1 vise une première proposition composée, spécifique et soignée, sans imposer un registre esthétique par défaut. La méthode protège l’ambition de création — présence, point de vue, culture visuelle, spécificité, craft et polish — sans confondre une référence, une rationale, un asset ou une capture avec une preuve d’usage. Lorsqu’une décision exige une trace structurée, la `RUN_CARD` rassemble le mode, le risque, la décision, l’artefact, la preuve, la limite et la clôture. Pour les runs multi-domaines ou de profondeur élevée, les contrats `DOMAIN_FRAME`, `RESEARCH_BRIEF`, `CREATIVE_DIRECTION_SET`, `UI_UX_REALITY_PACK` et `EVALUATION_CASE` rendent exécutables le cadrage, la recherche, la divergence, la réalité UI/UX et l’apprentissage.

## Pour les agents et les opérateurs

| Lecteur | Entrée | Ce qu’il y trouve |
|---|---|---|
| Agent | [`SKILL.md`](agent/skill/SKILL.md) | Noyau de fabrication et liste de chargement unique (`DIRECTION/CHARGE`). |
| Opérateur ou designer qui pilote un run | [Guide opérateur](guides/equipe.md) | Parcours commun, classement, chargement, handoff et exemple complet. |
| Reviewer ou lead | [`READING_MAP.md`](V1/official/READING_MAP.md), puis [`ACTION.md`](V1/official/ACTION.md) | Preuve dans le scope, limites et décision de clôture. |
| Mainteneur du package | Ce README, [`CHANGELOG.md`](maintenance/versions.md) et les validateurs | Contrat cohérent, testable et reproductible. |

### Installer la skill dans un agent

La skill ne contient que le noyau ; ses routes, ses scripts et ses schémas restent dans le paquet. Gardez donc le paquet entier, puis :

1. **Rendre la skill visible.** Avec Claude Code, copiez le dossier `agent/skill` sous le nom `design-governance-practice`, dans `.claude/skills/` du projet ou dans `~/.claude/skills/` (par exemple `cp -r agent/skill .claude/skills/design-governance-practice`). Avec un autre agent, donnez-lui `SKILL.md` comme instructions.
2. **Donner accès au paquet.** Les commandes de la skill (`python3 scripts/read_route.py …`) s’exécutent depuis la racine du paquet : travaillez dans ce dossier, ou indiquez son chemin à l’agent (« Design Governance est dans /chemin/du/paquet ; lance ses scripts depuis ce dossier »). Python 3.10 ou plus récent suffit ; la recette de rendu demande aussi Playwright et Chromium.
3. **Vérifier.** Depuis la racine du paquet, `python3 scripts/read_route.py DIRECTION/START` affiche la route.

Sans accès au paquet, l’agent n’a que le noyau : les routes que demande la table de chargement lui manquent. Après une mise à jour du paquet, recopiez la skill.

Le mode d’un run est choisi par l’agent avec `DIRECTION/START`, seule classification ; il n’est jamais demandé à la personne qui fait la demande. Le parcours complet d’un run est : classer, diriger, construire, observer, corriger, puis proposer (par défaut, en trace légère : la première proposition vaut checkpoint) ou fermer (trace complète) ; chaque mode n’en garde que les étapes de sa route.

Le README oriente la navigation. Il ne crée aucune règle concurrente. Les sources normatives font foi dans leur périmètre.

<!-- constitution:début -->
## Constitution minimale

Les cinq absolus transversaux de `DIRECTION` forment le noyau de protection de V1 : une surface identitaire doit avoir une direction perceptible ; une direction identitaire n’est acceptée qu’avec une ancre, observée ou fournie pour un produit réel (l’exploration peut commencer sans ancre, avec sa limite déclarée) ; aucune livraison ne contourne les preuves applicables ; le mode, la décision dominante, le risque principal, la preuve minimale et la condition d’arrêt sont déclarés avant l’exécution ; le réel et le beau sont cadrés ensemble.

Ces absolus ne remplacent pas les procédures propriétaires d’`ACTION`, de `SAVOIR` ou de `BIBLIOTHEQUE`. Ils rappellent la priorité de gouvernance et renvoient à [DIRECTION.md](design/direction/standard.md#les-cinq-règles-absolues), qui reste la source normative. Le piège de conformité est explicite : une conformité de surface ne vaut ni direction perceptible, ni preuve d’usage, ni qualité réelle.
<!-- constitution:fin -->

## Le modèle à double boucle

V1 sépare deux boucles qui se répondent :

| Boucle de création | Boucle de gouvernance et d’amélioration |
|---|---|
| Cadrer le produit et le public. | Classer le risque et le mode. |
| Cultiver des références et un territoire lorsque cela peut changer la décision. | Définir le scope et la preuve nécessaire. |
| Ouvrir puis sélectionner une direction située. | Protéger les contraintes critiques. |
| Composer et construire une scène complète, avec les assets et composants utiles. | Observer le rendu réel et ses limites. |
| Polir la proposition sans confondre finition et décoration. | Isoler le défaut dominant, corriger l’artefact, observer à nouveau et décider. |

La seconde boucle ne se résume pas à une critique textuelle. Lorsque la décision créative ou perceptuelle est en jeu, son chemin est :

> **La boucle d’édition** (`DIRECTION/DOUBLE-LOOP`, reprise dans le noyau de la skill) : observer, nommer le défaut dominant, modifier l’artefact, comparer, décider.

Le noyau relie désormais les symptômes de finesse à des gestes conditionnels, aux savoirs qui les approfondissent et à ce qu’il faut réinspecter : bord éclairé, alignement optique, chiffres stables, recadrage, groupement ou récupération. Le système guide l’intervention concrète ; il ne s’arrête pas à demander de la cohérence et n’impose pas ces gestes à tous les rendus. La preuve d’un gain esthétique sur des runs réels reste à établir.

BIBLIOTHEQUE relie aussi l’intention perceptuelle au niveau structurel, au levier de construction et à son effet attendu. Sa traduction dans `SELECT` et sa calibration locale dans `CONTRACTS` aident à choisir proportions, distances, typographie, cadrage et états selon le projet ; le relais est compilé dans le noyau. Ces ressources ne constituent ni un catalogue de styles, ni une bibliothèque de composants déjà implémentés, ni une garantie de qualité.

La trace doit dire ce qui a changé, ce qui n’a pas été vérifié et ce qui doit se passer ensuite. Une preuve technique ne devient pas automatiquement un jugement esthétique ; une intention créative ne masque pas une preuve d’usage ou d’accessibilité manquante.

## Structure du dépôt

| Couche | Chemin | Responsabilité |
|---|---|---|
| **Sources et guides** | `V1/official/` | Corpus normatif et guides d’entrée de la V1. |
| **Activation pratique** | `agent/skill/` | Couche d’activation et références conditionnelles ; elle ne crée pas de règles concurrentes. |
| **Projection machine** | `gouvernance/schemas/` | Schémas, exemples et fixtures de `RUN_CARD`, du cadre de domaine, du brief de recherche et des contrats de production. |
| **Contrôles et distributions** | `scripts/` | Validation du package, validation des RUN_CARD et génération des exports. |

Les cinq sources normatives sont les suivantes :

| Source | Décision principalement couverte |
|---|---|
| `DIRECTION.md` | Mode, risque, absolus, direction, cible et capacité. |
| `ACTION.md` | Procédures, preuve, gates, états, verdicts et clôture. |
| `SAVOIR.md` | Jugement, craft, contenu, contexte, styles, sources et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, évolution, cycle de vie et décisions de gouvernance. |

`README.md`, `QUICKSTART.md` et `GLOSSAIRE.md` facilitent l’orientation et la compréhension ; ils ne créent pas de route, de gate, de statut ou d’autorité supplémentaire.

Pour charger uniquement un bloc documenté, utilisez `python3 scripts/read_route.py DIRECTION/START` ; pour rechercher un terme dans les sources normatives, `python3 scripts/read_route.py --trouver "terme"` (mots entiers, casse et accents ignorés, quelques synonymes et traductions ; routes classées) ; pour voir toutes les routes et leur rôle, `python3 scripts/read_route.py --sommaire`. Ajoutez `--guides` pour inclure les documents d’orientation (guides du corpus, ce README et les références de la skill), séparés des résultats normatifs. L’absence de résultat ne prouve pas l’absence d’une notion : essayez une reformulation ciblée. Le noyau active cette recherche si la route utile est inconnue ou si un signal reste sans intervention concrète. Pour une carte concrète, `python3 gouvernance/outils/validate_run_card.py --strict chemin/vers/run_card.json` complète la validation structurelle en rejetant les placeholders et en contrôlant l’existence des locators locaux (artefact, trace, captures B1b) ; remplacez le chemin d’exemple par celui de votre fichier.

## Limites et discipline d’usage

Une capture prouve un rendu dans son scope ; elle ne prouve pas à elle seule une tâche utilisateur, un lecteur d’écran, une sécurité, une performance ou une intégration réelle. Une trace complète sans conséquence est du slop procédural : si une étape, une variante, une référence ou un tag ne change aucune décision, observation, preuve, limite ou prochaine action, retirez-le ou justifiez `N/A-JUSTIFIED`.

La qualité créative reste située. Une proposition peut être visuellement convaincante sans avoir prouvé l’usage, l’accessibilité ou la robustesse ; elle peut aussi être conforme et robuste tout en restant générique ou insuffisamment résolue. V1 demande de rendre cet écart visible et de corriger le défaut dominant plutôt que de le compenser par une autre preuve.

V1 rend certaines affirmations plus difficiles à simuler ; elle ne remplace pas le jugement créatif, les tests utilisateurs, l’inspection technique ou la responsabilité du projet. Toute conclusion doit préciser ce qui a été observé, par quelle méthode, dans quel scope et avec quelle limite.
