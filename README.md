# Design Governance V1.0.0

Design Governance aide un agent, ou une personne, à concevoir des pages, des écrans et des identités visuelles qui ont une vraie direction, qui sont réellement construits et soignés dès la première proposition, puis à les améliorer en regardant le rendu. Quand un travail doit être livré ou audité, le système garde aussi la trace de ce qui a été vérifié, et de ce qui ne l’a pas été.

> **Statut :** expérimentation maintenue, pensée pour un usage avec revue humaine. Son effet sur la qualité des rendus n’est pas encore mesuré (`NOT-VERIFIED`).

## Par où entrer

| Vous êtes | Entrée | Ce que vous y trouvez |
|---|---|---|
| Débutant : vous voulez un résultat, sans apprendre le système | [`guides/commencer.md`](guides/commencer.md) | Quoi demander, quoi fournir, ce que vous recevrez, comment poursuivre |
| Designer | [`guides/designer.md`](guides/designer.md) | Où se trouve chaque sujet, comment combiner les capacités, quand s’arrêter |
| Équipe ou opérateur | [`guides/equipe.md`](guides/equipe.md) | Piloter un travail, le tracer et le livrer |
| Relecteur ou responsable | [`gouvernance/README.md`](gouvernance/README.md) | Ce qui a été prouvé, les limites, la clôture |
| Agent | [`agent/skill/SKILL.md`](agent/skill/SKILL.md) | Le noyau, puis quoi lire selon le chemin |
| Personne qui fait évoluer le système | [`maintenance/README.md`](maintenance/README.md) | Distributions, validation, versions |

Le vocabulaire est expliqué dans [`guides/glossaire.md`](guides/glossaire.md).

## Installer la skill dans un agent

La skill ne contient que le noyau ; ses routes, ses scripts et ses schémas restent dans le paquet. Gardez donc le paquet entier, puis :

1. **Rendre la skill visible.** Avec Claude Code, copiez le dossier `agent/skill` sous le nom `design-governance-practice`, dans `.claude/skills/` du projet ou dans `~/.claude/skills/` (par exemple `cp -r agent/skill .claude/skills/design-governance-practice`). Avec un autre agent, donnez-lui `SKILL.md` comme instructions.
2. **Donner accès au paquet.** Les commandes de la skill (`python3 scripts/read_route.py …`) s’exécutent depuis la racine du paquet : travaillez dans ce dossier, ou indiquez son chemin à l’agent (« Design Governance est dans /chemin/du/paquet ; lance ses scripts depuis ce dossier »). Python 3.10 ou plus récent suffit ; la recette de rendu demande aussi Playwright et Chromium.
3. **Vérifier.** Depuis la racine du paquet, `python3 scripts/read_route.py DIRECTION/START` affiche la route.

Sans accès au paquet, l’agent n’a que le noyau. Après une mise à jour du paquet, recopiez la skill.

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

## Comment ça marche

Deux boucles se répondent. La première **crée** : cadrer le produit et son public, chercher des références quand elles peuvent changer la décision, choisir une direction, construire une scène complète, polir. La seconde **apprend** : regarder le rendu réel, nommer le défaut principal, corriger, regarder à nouveau, décider. Le détail est dans [`design/README.md`](design/README.md).

## Ce que contient le dépôt

```mermaid
flowchart TD
  R["README"] --> G["guides/ : une porte par public"]
  G --> D["design/ : direction, savoir, formes, produit"]
  R --> AG["agent/ : la skill et son chemin"]
  AG --> D
  D -. "si le travail est tracé ou livré" .-> GV["gouvernance/ : facultatif"]
  R --> M["maintenance/ : faire évoluer le système"]
```

| Partie | Chemin | Contenu |
|---|---|---|
| **Guides** | `guides/` | Les portes : commencer, designer, équipe, glossaire. |
| **Design** | `design/` | Le cœur : direction, savoir, formes, qualité du produit. |
| **Agent** | `agent/` | La skill (`agent/skill/`), le chemin de l’agent et sa réponse. |
| **Gouvernance** (facultative) | `gouvernance/` | Trace, vérification formelle et livraison ; schémas et outils de validation. |
| **Maintenance** | `maintenance/` | Faire évoluer le système : distributions, validation, versions. |
| **Sources en cours de rangement** | `V1/official/` | Sections pas encore rangées ; toutes les adresses restent valables. |
| **Outils** | `scripts/` | Lecteur, contrôles et construction des distributions. |

Les guides orientent ; ils ne créent aucune règle. Les règles qui font foi sont décrites dans le [sommaire des sources](V1/official/README.md).

Pour lire une seule partie du système :

```bash
python3 scripts/read_route.py --sommaire            # toutes les sections et leur rôle
python3 scripts/read_route.py savoir/couleur        # une section, par son adresse
python3 scripts/read_route.py --trouver "contraste" # chercher un terme
```

Ajoutez `--guides` pour chercher aussi dans les guides. Une recherche sans résultat ne prouve pas que la notion manque : reformulez.

## Limites

- **Version.** V1.0.0, révision `R2026-10-09-REFONTE` : voir le [journal des versions](maintenance/versions.md) et les [notes de version](RELEASE_NOTES.md).
- **Efficacité non vérifiée** (`NOT-VERIFIED`). Aucune mesure comparative ne montre encore l’effet du système sur la qualité des rendus. Usage recommandé : un pilote, avec revue humaine. L’exécution de la CI hébergée pour cette révision n’est pas vérifiée non plus.
- **Une validation confirme seulement les contrôles exécutés.** Une capture prouve un rendu, pas un usage : à elle seule, elle ne prouve ni une tâche utilisateur, ni un lecteur d’écran, ni la sécurité, la performance ou une intégration réelle.
- **Séduisant n’est pas prouvé, conforme n’est pas réussi.** Le système demande de rendre cet écart visible et de corriger le défaut principal, sans le compenser par une autre preuve. Une étape ou une référence qui ne change rien est retirée.
- **Le système ne remplace** ni le jugement créatif, ni les tests utilisateurs, ni la responsabilité du projet. Toute conclusion dit ce qui a été observé, comment, sur quel périmètre et avec quelle limite.
