# Release notes — Design Governance V1.0.0

**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Date de V1.0.0 :** 2026-10-01\
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Révision R2026-10-09-COHERENCE

Correction des renvois après la refonte. Les sections propriétaires font foi à leur emplacement actuel ; les identités historiques servent à la provenance et les anciens codes restent compatibles. La gouvernance est adaptée au travail : chaque contrôle et chaque élément de trace doit aider une décision, une preuve ou une reprise, sans supprimer les protections applicables.

Le paquet contrôle désormais aussi les références opérationnelles entre accents graves et les emplacements déclarés dans le registre des sources. Le lecteur accepte le journal `maintenance/versions` et son alias historique `CHANGELOG`. La recette de rendu permet de sélectionner explicitement un Chromium installé, sans téléchargement ni substitution silencieuse.

La finalisation couvre les extensions courantes, les anciens noms sans extension et les commandes Python et shell simples. Les exemples explicites et blocs de code restent hors contrôle ; les arguments utilisateur ne sont pas des dépendances du paquet. Les sections conservées sont rangées dans `V1/sections/` ; les codes historiques gardent leur sens. Le principe de gouvernance utile est intégré à la règle de trace, puis recompilé dans la skill.

Compatibilité : V1.0.0 ; aucun nouveau mode, statut ou champ RUN_CARD. **Efficacité sur les rendus : `NOT-VERIFIED`.** CI hébergée observée : [run 45](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/37987098716), réussi pour `df5aa46`, et [run 46](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/37993730822), réussi pour `d2c4d01`. Ces preuves portent sur les commits cités ; les changements suivants ont leur propre validation.

## Révision précédente R2026-10-09-REFONTE

Refonte de la forme, sans nouvelle règle. Le système est rangé en parties lisibles : `guides/` (une porte par public : débutant, designer, équipe, glossaire), `design/` (direction, savoir, formes, qualité du produit), `agent/` (la skill, le chemin de l’agent et sa réponse), `gouvernance/` (module facultatif) et `maintenance/`. Le README, les guides et le glossaire sont réécrits en langue claire ; les sections se lisent par des adresses lisibles (`savoir/couleur`), les anciens codes restant acceptés.

Ce que lit l’agent change peu, et volontairement : deux observations de tendance récentes et une liste d’exemples typographiques sont retirées (sources de convergence), et deux exemples recopiables de la skill passent au format à compléter. L’export Local a désormais la même arborescence que la distribution GitHub ; la copie Markdown de l’outil de préparation est retirée.

Compatibilité : V1.0.0 ; aucun nouveau mode, contrôle, statut ni champ RUN_CARD. **Efficacité : `NOT-VERIFIED`** ; aucun effet sur la qualité des rendus n’est revendiqué.

## Révision précédente R2026-10-08-ACCES-MATIERE

Après une mesure à l’aveugle (U5), le système active mieux ce qu’il sait. En mode `DIRECTION`, la typographie se charge d’office, chaque route facultative est tranchée explicitement, une route ouverte se lit en entier et un tour d’édition sur capture a lieu même en trace légère. Les paris P1 et P3, non concluants, sont retirés.

Le lecteur `read_route.py` liste les routes (`--sommaire`), cherche par mots entiers avec synonymes et traductions, classe les routes, affiche le propriétaire d’un sujet (carte des sujets de READING_MAP) et replie les blocs déjà présents dans le noyau (`--complet` pour tout lire). Toutes les routes sont atteignables depuis le noyau.

Nouvelle route `BIBLIOTHEQUE/SEQUENCE` pour la forme d’une page de plusieurs sections et la structure mobile. Compléments de craft, de sources, de données, de premier état et de vérité des exemples ; un marqueur de vague daté.

Compatibilité : V1.0.0 ; aucun nouveau mode, gate, statut ni champ RUN_CARD. **Efficacité : `NOT-VERIFIED`** depuis la mesure U5 ; aucun effet sur la qualité des rendus n’est revendiqué.

## Révisions précédentes

- `R2026-10-08-CORRECTIONS` — corrections d’un audit complet, sans run de mesure.
- `R2026-10-04-AUDIT2-FIXES` — second audit interne : constats F07 à F10 et R01 à R04.
- `R2026-10-04-AUDIT-FIXES` — audit interne : constats F01 à F06, conservation des capacités de mobilisation et d’activation.

Leur détail fait partie de l’historique de travail, tenu hors de cette distribution.

## Présentation

Design Governance aide un agent à produire un travail de design dirigé, construit et soigné dès la première proposition, puis à l’améliorer avec la personne qui le demande.

L’agent lit un **noyau de fabrication**, compilé depuis les sources normatives, puis charge ce que la ligne de son mode dans `DIRECTION/CHARGE` demande. Il construit une première proposition composée et tient une **trace proportionnée** : légère par défaut, complète si le run est persistant, partagé, audité ou si une acceptation est demandée.

## Points clés

- **Direction avant fabrication.** Prise de brief minimale, Creative Boot (`MODAL` / `PARTI`), premier objet de preuve et signaux de convergence nommés.
- **Proposition par défaut.** La première proposition vaut checkpoint, sauf action irréversible ou coûteuse. Valider n’est pas accepter : l’acceptation pour un vrai produit se demande et passe en trace complète.
- **Vérité du contenu.** Exemples marqués plutôt qu’emplacements vides ; action principale fonctionnelle avec une valeur d’exemple marquée ; fonctions d’un produit fictif marquées comme exemples.
- **Ancre graduée.** Explorer sans ancre avec une limite déclarée ; accepter une direction identitaire avec une ancre, observée ou fournie ; `FAIL-ASSUMED` réservé à un échec connu.
- **Interfaces.** Réalité UI/UX chargée avant fabrication ; toute exigence UI/UX déclarée est couverte.
- **Projection machine.** Schéma `RUN_CARD` et contrats de production, avec exemples et fixtures.

Le détail est dans [`maintenance/versions.md`](maintenance/versions.md).

## Contenu

| Élément | Fonction |
|---|---|
| `guides/` | Entrées par public et glossaire |
| `design/` | Direction, savoir, formes et qualité du produit |
| `agent/` | Chemins, réponse et skill |
| `gouvernance/` | Trace et preuve adaptées au besoin |
| `maintenance/` | Versions, évolution et distributions |
| `V1/sections/` | Sections conservées et carte dérivée ; même autorité que les sections déplacées |
| `agent/skill/` | Couche d’activation : noyau de fabrication compilé, références conditionnelles |
| `gouvernance/schemas/` | Projections machine, exemples et fixtures de contrôle |
| `scripts/` | Validateurs, compilation du noyau, runner global et construction des distributions |

## Parcours

**Pour une personne qui fait une demande :** le [guide pour commencer](guides/commencer.md). Elle n’a pas de mode à choisir.

**Pour un agent :**

```text
lire la skill (noyau de fabrication) → classer avec DIRECTION/START
→ charger la ligne de son mode dans DIRECTION/CHARGE → construire la première proposition
→ boucle d’édition → réponse visible et trace légère (trace complète si le run est persistant, partagé, audité ou à accepter)
```

**Pour un opérateur :** le guide [`guides/equipe.md`](guides/equipe.md).

## Contrôles inclus

Le package contrôle :

- son inventaire, ses liens et son vocabulaire structuré ;
- ses gardes de propriété et son noyau compilé ;
- ses contrats machine, avec leurs fixtures positives et négatives ;
- sa carte dérivée et son lecteur de routes ;
- la reproductibilité de ses distributions.

Ces contrôles établissent la cohérence documentaire et technique du package. Ils ne remplacent ni une observation de rendu, ni un test utilisateur, ni une vérification d’accessibilité exécutée, ni une mesure de performance, ni une preuve d’adoption.

Pour vérifier le package :

```bash
python3 scripts/validate_all.py
```

Le workflow livré dans la distribution GitHub (`.github/workflows/validate.yml`) configure Linux (`ubuntu-latest`), Python 3.11 et Playwright 1.56.0 avec Chromium ; il exige les tests de pages (`--require-browser`). Son exécution a été observée : les runs 45 (`df5aa46`) et 46 (`d2c4d01`), liés ci-dessus, réussissent avec l’étape de navigateur et l’audit du paquet. Une CI verte atteste les contrôles du commit concerné, sans établir l’efficacité visuelle du système. Les contrôles locaux sont décrits ci-dessus. <!-- références:github -->

## Ce que le validateur atteste

Une `RUN_CARD` validée atteste la forme de la projection et les invariants de la liste close.

Elle n’atteste pas :

- que les observations ont eu lieu ;
- la justesse des jugements ;
- la réalité des droits et des données ;
- la qualité perceptuelle.

La frontière exacte est écrite dans `ACTION/RUN_CARD`.

## Limites déclarées

- **Efficacité : `NOT-VERIFIED`.** Aucune mesure comparative n’établit l’effet de la révision actuelle sur la qualité des rendus ; les runs pratiques orientent sans prouver.
- **Convergence.** Le système nomme le modal et demande de justifier ce qui est repris ; il ne garantit pas à lui seul une direction différente.
- **Taille et coût.** Le budget borne le fichier `SKILL.md` complet en octets UTF-8. Il ne mesure ni la charge cognitive, ni les lectures conditionnelles, ni les tokens ou le temps nécessaires au run complet. Aucune mesure actuelle de ce coût n’est établie.
- **Plateformes.** macOS et Windows n’ont pas été observés.
- **Champs libres.** Les placeholders n’y sont pas filtrés globalement.
