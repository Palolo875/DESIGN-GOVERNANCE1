# Design Governance V1.0.0 — expérimental

Design Governance aide un agent, ou une personne, à concevoir des pages, des écrans et des identités visuelles qui ont une vraie direction, qui sont réellement construits et soignés dès la première proposition, puis à les améliorer en regardant le rendu ; il sert aussi à juger et analyser un existant. Quand un travail doit être livré ou audité, le système garde la trace de ce qui a été vérifié, et de ce qui ne l’a pas été.

Son objectif : obtenir un niveau élevé plus régulièrement, avec moins d’oublis, de tâtonnements et de reprises inutiles. C’est une hypothèse à éprouver, pas un résultat acquis ; [le cap](maintenance/versions.md#cap) dit comment elle se juge.

> **Statut :** V1.0.0, révision `R2026-10-21`. Expérimentation maintenue, pensée pour un usage avec revue humaine (voir [les limites](#limites)). Le contenu complet est décrit dans [ce que contient le système](maintenance/versions.md).

## Par où entrer

Les guides suivent un niveau de maîtrise, pas un métier : chacun entre au niveau 1 et monte quand il en a besoin.

| Niveau | Entrée | Ce que vous saurez faire |
|---|---|---|
| **1 — Utiliser** | [`guides/1-utiliser.md`](guides/1-utiliser.md) | Demander, fournir, recevoir une proposition et la faire évoluer, sans apprendre le système |
| **2 — Comprendre** | [`guides/2-comprendre.md`](guides/2-comprendre.md) | Savoir comment le système raisonne, trouver un sujet, combiner les savoirs selon le résultat, savoir quand s’arrêter |
| **3 — Maîtriser** | [`guides/3-maitriser.md`](guides/3-maitriser.md) | Piloter un travail, le confier à un agent, le vérifier, le décider, le conserver et le transmettre |

D’autres entrées servent des besoins précis :

| Besoin | Entrée | Contenu |
|---|---|---|
| Relire ce qui a été prouvé | [`gouvernance/README.md`](gouvernance/README.md) | Preuves, limites, clôture |
| Brancher un agent | [`SKILL.md`](SKILL.md) | Le noyau, puis quoi lire selon le chemin |
| Faire évoluer le système | [`maintenance/README.md`](maintenance/README.md) | Distributions, validation, contenu de la version |

Le vocabulaire est expliqué dans [`guides/glossaire.md`](guides/glossaire.md).

## Installer la skill dans un agent

Le paquet entier est la skill : `SKILL.md` est à sa racine, avec à côté les sources, les scripts et les références qu’elle lit au moment utile. On installe donc le dossier complet, sous le nom `design-governance-practice` (le format [Agent Skills](https://agentskills.io/specification) exige que le dossier porte le nom de la skill).

<!-- github:début installation -->
**Avec l’outil `skills`**, depuis la racine de votre projet :

```bash
npx skills add Palolo875/DESIGN-GOVERNANCE1 --skill design-governance-practice
```

L’outil demande pour quels agents installer (Claude Code, Codex, Cursor, Gemini CLI, GitHub Copilot…) et où : dans le projet ou dans votre dossier personnel. `npx skills update` met la skill à jour. Cette commande a été vérifiée le 14 octobre 2026 depuis une copie locale du paquet, pour Claude Code et Codex.

**Sans cet outil**, clonez le paquet dans le dossier de skills de votre agent :

```bash
git clone https://github.com/Palolo875/DESIGN-GOVERNANCE1 .claude/skills/design-governance-practice
```

| Agent | Dossier du projet | Dossier personnel |
|---|---|---|
| Claude Code | `.claude/skills/` | `~/.claude/skills/` |
| Codex | `.agents/skills/` | `~/.agents/skills/` |
| Cursor, Gemini CLI, GitHub Copilot | `.agents/skills/` | `~/.cursor/skills/`, `~/.gemini/skills/`, `~/.copilot/skills/` |

Pour mettre à jour un clone : `git -C .claude/skills/design-governance-practice pull`.
<!-- github:fin installation -->

Un agent sans gestion de skills reçoit `SKILL.md` comme instructions et travaille depuis le dossier du paquet. Python 3.10 ou plus récent suffit (la CI teste 3.11). Les recettes demandent aussi Playwright avec son Chromium (version testée : 1.56.0) ; la recette de caractère, numpy et Pillow. Évitez d’activer dans le même projet une autre skill générale de design : deux skills se déclencheraient sur la même demande avec des consignes différentes.

**Vérifier.** Le fichier principal est à la racine du dossier installé, et le lecteur y affiche une route :

```bash
cd .claude/skills/design-governance-practice && python3 scripts/read_route.py DIRECTION/START
```

Ce contrôle ne prouve pas que l’agent a chargé la skill : demandez-lui quelles skills sont actives, ou consultez la liste de skills de l’hôte.

## Fonctionnement

Deux boucles se répondent. La première **crée** : cadrer le produit et son public, chercher des références quand elles peuvent changer la décision, choisir une direction, construire une scène complète, polir. La seconde **apprend** : regarder le rendu réel, nommer le défaut principal, corriger, regarder à nouveau, décider. Le détail est dans [`design/README.md`](design/README.md). Le [parcours d’un travail](supports/parcours.md) et la [boucle créer/apprendre](supports/boucle.md) en donnent deux vues complémentaires.

<!-- github:début titre-contenu -->
## Ce que contient le dépôt
<!-- github:fin titre-contenu -->

<a href="supports/systeme.md">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="supports/systeme-sombre.svg">
    <img src="supports/systeme-clair.svg" alt="Carte du système : entrées, responsabilités et autorité des sections">
  </picture>
</a>

[Consulter les trois cartes](supports/README.md) · [Lire la carte en texte](supports/systeme.md).

| Partie | Chemin | Contenu |
|---|---|---|
| **Guides** | [`guides/`](guides/README.md) | Trois niveaux de maîtrise (utiliser, comprendre, maîtriser) et un glossaire. |
| **Design** | [`design/`](design/README.md) | Le cœur : direction, savoir, formes, qualité du produit. |
| **Skill** | [`SKILL.md`](SKILL.md), `references/` | Le point d’entrée de l’agent (noyau commun) et ses références : [exemples de runs](references/examples.md), [flux de décision](references/flow.md), [aide-mémoire minimal](references/canonical_minimum.md), [projection machine](references/machine_projection.md). |
| **Agent** | [`agent/`](agent/README.md) | Le chemin de l’agent par mode et la forme de sa réponse. |
| **Gouvernance** (selon le besoin) | [`gouvernance/`](gouvernance/README.md) | Contrôles et trace adaptés au risque, à la décision et aux besoins de reprise ; schémas et outils de validation. |
| **Supports** | [`supports/`](supports/README.md) | Trois cartes du système, en HTML, SVG clair et sombre, et texte. |
| **Maintenance** | [`maintenance/`](maintenance/README.md) | Ce que contient la version, évolution du système, distributions et validation. |
| **Sections de référence** | [`sections/`](sections/README.md) | Sections regroupées par domaine et carte de lecture. Chaque fichier ne contient qu’une partie de sa responsabilité et liste en tête où vivent les autres sections. |
| **Outils** | [`scripts/`](scripts/README.md) | <!-- github:début outils -->Lecteur de routes, recette de rendu dans un navigateur, compilation du noyau, contrôles du paquet et construction des distributions ; chaque commande est décrite dans [la validation](maintenance/README.md#validation).<!-- github:fin outils --> |

La gouvernance s’adapte au travail : chaque contrôle et chaque élément de trace doit aider à vérifier une affirmation, protéger un risque, permettre une reprise ou préparer une acceptation. Une proposition exploratoire garde une trace légère ; un travail persistant, partagé, audité ou soumis à acceptation conserve les éléments formels nécessaires. Les preuves applicables restent dues.

Les guides orientent ; ils ne créent aucune règle. Une règle fait foi dans sa section propriétaire, à son emplacement actuel, décrit dans le [sommaire des sources](sections/README.md). Les codes de route et les adresses lisibles désignent les mêmes sections.

Pour lire une seule partie du système :

```bash
python3 scripts/read_route.py --sommaire            # toutes les sections et leur rôle
python3 scripts/read_route.py savoir/typographie    # une section, par son adresse
python3 scripts/read_route.py --trouver "contraste" # chercher un terme
```

Ajoutez `--guides` pour chercher aussi dans les guides. Une recherche sans résultat ne prouve pas que la notion manque : reformulez.

<!-- constitution:début -->
## Les cinq règles essentielles

Quel que soit le travail, cinq règles priment :

1. **Une surface d’identité doit avoir une direction visible.** Être conforme (contraste, états, focus, performance) est un plancher, pas un résultat.
2. **Une direction d’identité s’appuie sur une ancre** : une référence observée, ou fournie pour un produit réel. On peut explorer sans ancre, à condition de le dire.
3. **Rien n’est livré sans les vérifications qui s’appliquent.**
4. **Avant d’agir, on déclare** le chemin suivi, la décision principale, le risque principal, la vérification minimale et le moment où l’on s’arrête.
5. **Pas de beauté hors sol.** Le produit, la tâche visée, les contraintes et les preuves font partie du design : le réel et le beau sont cadrés ensemble.

Une conformité de surface ne vaut ni direction visible, ni preuve d’usage, ni qualité réelle. Ces règles résument [la direction de design](design/direction/standard.md#directionstandard--les-cinq-règles-absolues), qui fait foi ; elles ne remplacent pas les règles détaillées du design, du produit ou de la gouvernance.
<!-- constitution:fin -->

## Limites

- **Efficacité non vérifiée** (`NOT-VERIFIED`) : usage recommandé en pilote, avec revue humaine. Ce qui est vérifié, et ce qui ne l’est pas, est décrit une fois dans [la fiche de version](maintenance/versions.md#ce-qui-est-vérifié-ce-qui-ne-lest-pas). <!-- github:début limite-ci -->La CI du dépôt exécute les contrôles sur chaque commit ([notes de version](RELEASE_NOTES.md#contrôles-inclus)) ; elle atteste la cohérence du paquet, pas cette efficacité.<!-- github:fin limite-ci -->
- **Séduisant n’est pas prouvé, conforme n’est pas réussi.** Le système demande de rendre cet écart visible et de corriger le défaut principal, sans le compenser par une autre preuve. Une étape ou une référence qui ne change rien est retirée.
- **Savoir daté.** Les observations de tendances, d’outils et de normes portent une date (`[VEILLE AAAA-MM]`) et une échéance de revue ; passé cette échéance, elles se revérifient avant usage.
- **Le système ne remplace** ni le jugement créatif, ni les tests utilisateurs, ni la responsabilité du projet. Toute conclusion dit ce qui a été observé, comment, sur quel périmètre et avec quelle limite.
