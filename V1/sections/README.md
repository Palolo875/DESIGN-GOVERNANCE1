# Design Governance V1.0.0

Ce dossier conserve les sections non encore déplacées et la carte de lecture de **Design Governance V1.0.0**, une expérimentation maintenue. Leur autorité suit la section propriétaire, comme dans les autres dossiers. Le sommaire reste le point d’entrée vers toutes les responsabilités historiques.

Pour commencer, lisez le [guide pour commencer](../../guides/commencer.md#commencer) : vous n’avez pas à choisir de mode. Pour piloter un run, lisez le guide d’équipe [`guides/equipe.md`](../../guides/equipe.md) ; un agent entre par la skill `design-governance-practice`. Le vocabulaire est défini dans [`guides/glossaire.md`](../../guides/glossaire.md).

## Sources normatives

L’autorité appartient à la **section propriétaire à son emplacement actuel**. Les cinq noms historiques ci-dessous désignent des responsabilités normatives, et non cinq fichiers complets à lire. Les sections déplacées conservent leur autorité ; leur provenance est marquée par `origine:`. Le registre `LIEUX` de `scripts/read_route.py` relie chaque source historique à ses fichiers actuels, et le lecteur résout la section exacte.

| Source | Responsabilité |
|---|---|
| `DIRECTION` | Mode et chargement : [chemins de l’agent](../../agent/chemins.md) ; cadrage et direction : [design](../../design/README.md) ; rôle et posture : [sections conservées](DIRECTION.md). |
| `ACTION` | Production : [qualité du produit](../../design/produit/README.md) ; réponse et trace : [répondre](../../agent/repondre.md) ; preuve et clôture : [gouvernance](../../gouvernance/README.md) ; [sections conservées](ACTION.md). |
| `SAVOIR` | Jugement, craft, contenu, contexte et sources : [savoir](../../design/savoir/README.md) ; [sections conservées](SAVOIR.md). |
| `BIBLIOTHEQUE` | Structures : [formes](../../design/formes/README.md) ; contrats : [gouvernance](../../gouvernance/structure.md) ; évolution : [maintenance](../../maintenance/evolution.md) ; [sections conservées](BIBLIOTHEQUE.md). |
| `CHANGELOG` (identité historique) | Version : [versions](../../maintenance/versions.md) ; cycle de vie et migrations : [évolution](../../maintenance/evolution.md). Pour lire, ouvrir ces fichiers actuels. |

Les marqueurs de provenance ne rendent pas un guide normatif : une section de règle fait foi, un guide ou une carte l’oriente. Le noyau de la skill est une projection générée ; les archives sont des distributions dérivées. En cas de divergence, corriger la projection ou le guide depuis la section propriétaire, puis régénérer et valider.

Les anciens codes et les adresses lisibles sont deux noms pour une même section. L’agent utilise les codes stables du noyau ; une personne peut utiliser les adresses lisibles. Aucune seconde lecture n’est requise. Les noms historiques de fichiers conservés dans le registre et les marqueurs servent à la provenance, pas de chemins à ouvrir.

Le README et les guides (`guides/`) sont des **guides d’entrée non normatifs**. Ils orientent la lecture, mais ne créent aucune route, gate, statut, score ou autorité concurrente. `DESIGN-ATLAS` appartient à `SAVOIR.md` ; ce n’est pas un fichier séparé. La carte [`V1/sections/READING_MAP.md`](./READING_MAP.md) (chemin, combinaisons par résultat et locators) est dérivée et non normative.

Lorsqu’une décision exige une trace structurée, la `RUN_CARD` rassemble le mode, le risque, la décision, l’artefact, la preuve, la limite et la clôture ; son schéma est dans `gouvernance/schemas/` et son validateur est `gouvernance/outils/validate_run_card.py`, exécuté depuis la racine du paquet. Une validation de package ou de `RUN_CARD` confirme uniquement les contrôles exécutés ; elle ne prouve ni l’usage, ni l’accessibilité exécutée, ni la performance, ni la qualité visuelle du produit.
