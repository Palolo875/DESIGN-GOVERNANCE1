# Sections de référence — Design Governance V1.0.0

Ce dossier contient les sections propriétaires regroupées par domaine (ACTION, BIBLIOTHEQUE, DIRECTION, SAVOIR) et la carte de lecture de **Design Governance V1.0.0**, une expérimentation maintenue. Leur autorité suit la section propriétaire, comme dans les autres dossiers. Le tableau ci-dessous mène à chaque responsabilité normative, où qu’elle soit rangée.

Pour commencer, lisez le [niveau 1](../guides/1-utiliser.md#commencer) : vous n’avez pas à choisir de mode. Pour piloter un run, lisez le [niveau 3](../guides/3-maitriser.md) ; un agent entre par la skill `design-governance-practice`. Le vocabulaire est défini dans [`guides/glossaire.md`](../guides/glossaire.md).

## Sources normatives

L’autorité appartient à la **section propriétaire à son emplacement actuel**. Les cinq noms ci-dessous désignent des responsabilités normatives, et non cinq fichiers complets à lire. Une section rangée dans un dossier thématique garde la même autorité ; le marqueur `origine:` indique sa responsabilité. Le registre `LIEUX` de `scripts/read_route.py` relie chaque responsabilité à ses fichiers, et le lecteur résout la section exacte. Un fichier de ce dossier ne contient donc pas toute sa responsabilité : son bandeau de tête, généré depuis `LIEUX`, liste les fichiers et routes qui portent le reste.

| Source | Responsabilité |
|---|---|
| `DIRECTION` | Mode et chargement : [chemins de l’agent](../agent/chemins.md) ; cadrage et direction : [design](../design/README.md) ; rôle et posture : [sections regroupées](DIRECTION.md). |
| `ACTION` | Production : [qualité du produit](../design/produit/README.md) ; réponse et trace : [répondre](../agent/repondre.md) ; preuve et clôture : [gouvernance](../gouvernance/README.md) ; [sections regroupées](ACTION.md). |
| `SAVOIR` | Jugement, craft, contenu, contexte et sources : [savoir](../design/savoir/README.md) ; [sections regroupées](SAVOIR.md). |
| `BIBLIOTHEQUE` | Structures : [formes](../design/formes/README.md) ; contrats : [gouvernance](../gouvernance/structure.md) ; évolution : [maintenance](../maintenance/evolution.md) ; [sections regroupées](BIBLIOTHEQUE.md). |
| `CHANGELOG` | Version : [versions](../maintenance/versions.md) ; cycle de vie et migrations : [évolution](../maintenance/evolution.md). Pour lire, ouvrir ces fichiers actuels. |

Les marqueurs de provenance ne rendent pas un guide normatif : une section de règle fait foi, un guide ou une carte l’oriente. Le noyau de la skill est une projection générée ; les archives sont des distributions dérivées. En cas de divergence, corriger la projection ou le guide depuis la section propriétaire, puis régénérer et valider.

Les codes stables et les adresses lisibles sont deux noms pour une même section. L’agent utilise les codes stables du noyau ; une personne peut utiliser les adresses lisibles. Aucune seconde lecture n’est requise. Les noms de fichiers inscrits dans le registre et dans les marqueurs servent à la provenance ; ce ne sont pas des chemins à ouvrir.

Le README et les guides (`guides/`) sont des **guides d’entrée non normatifs**. Ils orientent la lecture, mais ne créent aucune route, gate, statut, score ou autorité concurrente. `DESIGN-ATLAS` appartient à `SAVOIR.md` ; ce n’est pas un fichier séparé. La carte [`sections/READING_MAP.md`](./READING_MAP.md) (chemin, combinaisons par résultat et locators) est dérivée et non normative.

Lorsqu’une décision exige une trace structurée, la `RUN_CARD` rassemble le mode, le risque, la décision, l’artefact, la preuve, la limite et la clôture ; son schéma est dans `gouvernance/schemas/` et son validateur est `gouvernance/outils/validate_run_card.py`, exécuté depuis la racine du paquet. Une validation de package ou de `RUN_CARD` confirme uniquement les contrôles exécutés ; elle ne prouve ni l’usage, ni l’accessibilité exécutée, ni la performance, ni la qualité visuelle du produit.
