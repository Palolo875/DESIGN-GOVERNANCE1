# Design Governance V1.0.0 — expérimental

Design Governance aide un agent, ou une personne, à concevoir des pages, des écrans et des identités visuelles qui ont une vraie direction, qui sont réellement construits et soignés dès la première proposition, puis à les améliorer en regardant le rendu ; il sert aussi à juger et analyser un existant. Quand un travail doit être livré ou audité, le système garde aussi la trace de ce qui a été vérifié, et de ce qui ne l’a pas été.

> **Statut :** V1.0.0, révision `R2026-10-14-REVUE`. Expérimentation maintenue, pensée pour un usage avec revue humaine ; son effet sur la qualité des rendus n’est pas encore mesuré (`NOT-VERIFIED`). Le contenu complet est décrit dans [ce que contient le système](maintenance/versions.md).

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
| Brancher un agent | [`agent/skill/SKILL.md`](agent/skill/SKILL.md) | Le noyau, puis quoi lire selon le chemin |
| Faire évoluer le système | [`maintenance/README.md`](maintenance/README.md) | Distributions, validation, contenu de la version |

Le vocabulaire est expliqué dans [`guides/glossaire.md`](guides/glossaire.md).

## Installer la skill dans un agent

La skill ne contient que le noyau ; ses routes, ses scripts et ses schémas restent dans le paquet. Gardez donc le paquet entier, puis :

1. **Rendre la skill visible.** Avec Claude Code, copiez le *contenu* de `agent/skill` dans un dossier `design-governance-practice`, sous `.claude/skills/` du projet ou sous `~/.claude/skills/`. Depuis la racine de votre projet :

   ```bash
   mkdir -p .claude/skills/design-governance-practice
   cp -R /chemin/du/paquet/agent/skill/. .claude/skills/design-governance-practice/
   ```

   La même commande met la skill à jour : elle remplace les fichiers sans créer de sous-dossier. Si une mise à jour retire des fichiers de référence, supprimez d’abord le dossier installé. La skill suit le format ouvert [Agent Skills](https://agentskills.io/specification) ; d’autres agents la lisent dans leurs propres dossiers :

   | Agent | Dossier du projet | Dossier personnel |
   |---|---|---|
   | Claude Code (vérifié) | `.claude/skills/` | `~/.claude/skills/` |
   | Codex | `.agents/skills/` | `~/.agents/skills/` |
   | Cursor, Gemini CLI, GitHub Copilot | `.agents/skills/` | `~/.cursor/skills/`, `~/.gemini/skills/`, `~/.copilot/skills/` |

   Dans tous les cas, le dossier installé s’appelle `design-governance-practice`, comme le champ `name` de la skill (le format l’exige). Seul Claude Code a été vérifié ici ; les autres dossiers suivent la documentation de ces outils. Un agent sans gestion de skills reçoit `SKILL.md` comme instructions. Évitez d’activer dans le même projet une autre skill générale de design : deux skills se déclencheraient sur la même demande avec des consignes différentes.
2. **Donner accès au paquet.** Les commandes de la skill (`python3 scripts/read_route.py …`) et les fichiers qu’elle cite s’entendent depuis la racine du paquet : travaillez dans ce dossier, ou indiquez son chemin à l’agent (« Design Governance est dans /chemin/du/paquet ; lance ses scripts depuis ce dossier »). Python 3.10 ou plus récent suffit ; la recette de rendu demande aussi Playwright et Chromium.
3. **Vérifier.** La copie est correcte si le fichier principal est à la racine du dossier installé, sans sous-dossier `skill/` ; l’accès au paquet l’est si la route s’affiche :

   ```bash
   ls .claude/skills/design-governance-practice/SKILL.md
   cd /chemin/du/paquet && python3 scripts/read_route.py DIRECTION/START
   ```

   Ces deux contrôles ne prouvent pas que l’agent a chargé la skill : demandez-lui quelles skills sont actives, ou consultez la liste de skills de l’hôte.

Sans accès au paquet, l’agent n’a que le noyau. Après une mise à jour du paquet, relancez la copie. Le noyau commun active la ligne du mode et les détails au moment utile ; un détail marqué « noyau » dans sa source n’est pas nécessairement embarqué dans la skill.

## Comment ça marche

Deux boucles se répondent. La première **crée** : cadrer le produit et son public, chercher des références quand elles peuvent changer la décision, choisir une direction, construire une scène complète, polir. La seconde **apprend** : regarder le rendu réel, nommer le défaut principal, corriger, regarder à nouveau, décider. Le détail est dans [`design/README.md`](design/README.md). Le [parcours d’un travail](supports/parcours.md) et la [boucle créer/apprendre](supports/boucle.md) en donnent deux vues complémentaires.

## Ce que contient le dépôt

<a href="supports/systeme.md">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="supports/systeme-sombre.svg">
    <img src="supports/systeme-clair.svg" alt="Carte du système : entrées, responsabilités et autorité des sections">
  </picture>
</a>

[Consulter les trois cartes](supports/README.md) · [Lire la carte en texte](supports/systeme.md).

| Partie | Chemin | Contenu |
|---|---|---|
| **Guides** | `guides/` | Trois niveaux de maîtrise (utiliser, comprendre, maîtriser) et un glossaire. |
| **Design** | `design/` | Le cœur : direction, savoir, formes, qualité du produit. |
| **Agent** | `agent/` | La skill (`agent/skill/`), le chemin de l’agent et sa réponse. |
| **Gouvernance** (selon le besoin) | `gouvernance/` | Contrôles et trace adaptés au risque, à la décision et aux besoins de reprise ; schémas et outils de validation. |
| **Supports** | `supports/` | Trois cartes du système, en HTML, SVG clair et sombre, et texte. |
| **Maintenance** | `maintenance/` | Ce que contient la version, évolution du système, distributions et validation. |
| **Sections d’origine** | `V1/sections/` | Sections restées à leur emplacement d’origine et carte de lecture ; même autorité que les autres. |
| **Outils** | `scripts/` | Lecteur, contrôles et construction des distributions. |

La gouvernance s'adapte au travail : chaque contrôle et chaque élément de trace doit aider à vérifier une affirmation, protéger un risque, permettre une reprise ou préparer une acceptation. Une proposition exploratoire garde une trace légère ; un travail persistant, partagé, audité ou soumis à acceptation conserve les éléments formels nécessaires. Les preuves applicables restent dues.

Les guides orientent ; ils ne créent aucune règle. Une règle fait foi dans sa section propriétaire, à son emplacement actuel, décrit dans le [sommaire des sources](V1/sections/README.md). Les codes historiques et les adresses lisibles désignent les mêmes sections.

Pour lire une seule partie du système :

```bash
python3 scripts/read_route.py --sommaire            # toutes les sections et leur rôle
python3 scripts/read_route.py savoir/couleur        # une section, par son adresse
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

Une conformité de surface ne vaut ni direction visible, ni preuve d’usage, ni qualité réelle. Ces règles résument [la direction de design](design/direction/standard.md#les-cinq-règles-absolues), qui fait foi ; elles ne remplacent pas les règles détaillées du design, du produit ou de la gouvernance.
<!-- constitution:fin -->

## Limites

- **Efficacité non vérifiée** (`NOT-VERIFIED`). Aucune mesure comparative ne montre encore l’effet du système sur la qualité des rendus. Usage recommandé : un pilote, avec revue humaine. La CI du dépôt exécute les contrôles sur chaque commit ([notes de version](RELEASE_NOTES.md#contrôles-inclus)) ; elle atteste la cohérence du paquet, pas cette efficacité.
- **Une validation confirme seulement les contrôles exécutés.** Une capture prouve un rendu, pas un usage : à elle seule, elle ne prouve ni une tâche utilisateur, ni un lecteur d’écran, ni la sécurité, la performance ou une intégration réelle.
- **Séduisant n’est pas prouvé, conforme n’est pas réussi.** Le système demande de rendre cet écart visible et de corriger le défaut principal, sans le compenser par une autre preuve. Une étape ou une référence qui ne change rien est retirée.
- **Le système ne remplace** ni le jugement créatif, ni les tests utilisateurs, ni la responsabilité du projet. Toute conclusion dit ce qui a été observé, comment, sur quel périmètre et avec quelle limite.
