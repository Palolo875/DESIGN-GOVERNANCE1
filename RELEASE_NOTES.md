# Release notes — Design Governance V1.0.0

**Statut expérimental :** Design Governance V1.0.0 est une expérimentation maintenue.  
**Date de V1.0.0 :** 2026-10-01\
**Usage recommandé :** pilote contrôlé, supervision humaine et preuve adaptée au risque

## Révision R2026-10-08-ACCES-MATIERE

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

Le détail est dans [`V1/official/CHANGELOG.md`](V1/official/CHANGELOG.md).

## Contenu

| Élément | Fonction |
|---|---|
| `V1/official/` | Sources normatives, guides d’entrée, glossaire et carte de lecture |
| `skills/design-governance-practice/` | Couche d’activation : noyau de fabrication compilé, références conditionnelles |
| `schemas/` | Projections machine, exemples et fixtures de contrôle |
| `scripts/` | Validateurs, compilation du noyau, runner global et construction des distributions |

## Parcours

**Pour une personne qui fait une demande :** la section « Commencer » du README du package. Elle n’a pas de mode à choisir.

**Pour un agent :**

```text
lire la skill (noyau de fabrication) → classer avec DIRECTION/START
→ charger la ligne de son mode dans DIRECTION/CHARGE → construire la première proposition
→ boucle d’édition → réponse visible et trace légère (trace complète si le run est persistant, partagé, audité ou à accepter)
```

**Pour un opérateur :** le guide [`V1/official/QUICKSTART.md`](V1/official/QUICKSTART.md).

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

Le [workflow livré](.github/workflows/validate.yml) configure Linux (`ubuntu-latest`), Python 3.11 et Playwright 1.56.0 avec Chromium ; il exige les tests de pages (`--require-browser`). Sa présence n’atteste pas son exécution : l’exécution CI de cette révision est `NOT-VERIFIED`. Les contrôles locaux sont décrits ci-dessus.

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
