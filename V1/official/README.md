# Design Governance V1.0.0

Ce dossier contient les sources officielles de **Design Governance V1.0.0**, une expérimentation maintenue : un cadre de direction, de création, de jugement et de vérification du design.

Pour commencer, lisez la section [« Commencer »](../../README.md#commencer) du README à la racine du package : vous n’avez pas à choisir de mode. Pour piloter un run, lisez le guide opérateur [`QUICKSTART.md`](./QUICKSTART.md) ; un agent entre par la skill `design-governance-practice`. Le vocabulaire est défini dans [`GLOSSAIRE.md`](./GLOSSAIRE.md).

## Sources normatives

Les cinq fichiers suivants sont les **seules sources normatives** de V1 :

| Source | Responsabilité |
|---|---|
| [`DIRECTION.md`](./DIRECTION.md) | Mode, classification, risque, cible et direction. |
| [`ACTION.md`](./ACTION.md) | Run, preuve, gates, statuts, verdict et clôture. |
| [`SAVOIR.md`](./SAVOIR.md) | Jugement, craft, contenu, contexte, sources et intégrité. |
| [`BIBLIOTHEQUE.md`](./BIBLIOTHEQUE.md) | Support, grille, scène, objet, micro-interface, contrat et compatibilité. |
| [`CHANGELOG.md`](./CHANGELOG.md) | État du corpus, changements, compatibilités et maintenance. |

`README.md`, `QUICKSTART.md` et `GLOSSAIRE.md` sont des **guides d’entrée non normatifs**. Ils orientent la lecture, mais ne créent aucune route, gate, statut, score ou autorité concurrente. `DESIGN-ATLAS` appartient à `SAVOIR.md` ; ce n’est pas un fichier séparé. La carte [`READING_MAP.md`](./READING_MAP.md) (chemin, combinaisons par résultat et locators) est dérivée et non normative.

Lorsqu’une décision exige une trace structurée, la `RUN_CARD` rassemble le mode, le risque, la décision, l’artefact, la preuve, la limite et la clôture ; son schéma et son validateur sont dans `schemas/` et `scripts/`. Une validation de package ou de `RUN_CARD` confirme uniquement les contrôles exécutés ; elle ne prouve ni l’usage, ni l’accessibilité exécutée, ni la performance, ni la qualité visuelle du produit.
