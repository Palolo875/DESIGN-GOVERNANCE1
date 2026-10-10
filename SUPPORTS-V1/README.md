# Présentation V1 expérimentale

Le propriétaire a demandé d’améliorer les schémas, puis de nettoyer et mettre en forme le système pour une V1 professionnelle qui reste expérimentale. Les travaux et les preuves sont conservés sur `refonte`, séparément du paquet produit.

## Première proposition livrée

[La carte du système](carte-01/index.html) montre les entrées, les responsabilités et l’autorité des sections. [La notice](carte-01/README.md) relie les sources, SVG clair/sombre, équivalent textuel, langage visuel, résultats et limites. Les 27 parcours passent dans Chromium ; les réserves de couverture demeurent explicites. Ce support reste proposé à la discussion.

Le contenu est dérivé de `main` au commit `4e1f9cc20a9887d570a720934ca5b1752c78971a`. La carte ne devient pas une source normative. Manrope, palettes par rôle et composition documentaire constituent une hypothèse de langage pour les supports, pas une contrainte de style pour les productions des agents.

## Lot de présentation livré

Le propriétaire a délégué le choix visuel par « à toi le choix ». Manrope, les palettes par rôle et la composition documentaire sont retenus pour ces supports. La première proposition reste conservée ; elle n’impose aucun style aux productions des agents.

Le [lot 02](lot-02/README.md) intègre trois cartes au candidat produit : [le système](lot-02/produit/supports/index.html), [le parcours d’un travail](lot-02/produit/supports/parcours.html) et [la boucle créer/apprendre](lot-02/produit/supports/boucle.html). Chaque carte possède ses sources JSON, SVG clair/sombre et équivalent écrit. Le README, le journal public et les notes de version sont nettoyés pour une V1 expérimentale. Les huit originaux sont conservés exactement dans `lot-02/avant/`.

La [PR 2](https://github.com/Palolo875/DESIGN-GOVERNANCE1/pull/2), en brouillon, porte le commit `213cfbaf8867142eb834c834311adb0fa626d8fe` ; elle n’est pas fusionnée. La validation complète avec navigateur et la reproductibilité des deux archives passent. Les 76 contrôles ciblés, trois recettes de rendu avec leurs réserves et trois mutations refusées sont conservés. La skill est identique à la base ; les règles, modes et schémas restent conservés. L’observation de la CI est datée dans [la livraison](lot-02/livraison.json). Les CI [55](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38092791148) et [56](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38092813117) sont réussies sur le commit de présentation `213cfbaf8867142eb834c834311adb0fa626d8fe`.

## Ce qui reste ouvert

La compréhension des supports par un nouveau public reste à observer. Les autres vues de phase 6 — architecture des fichiers, chemins par effort et gabarits — ne sont pas déclarées terminées : elles seront ajoutées si elles expliquent davantage que les entrées actuelles. L’intégration de ce candidat sur `main` reste distincte de sa livraison en brouillon.

Concurrents et anglais restent reportés. Les dossiers historiques, les jugements et les originaux U6 ainsi que le prototype Folio sont conservés. Ce lot ne prouve pas une efficacité générale du système ni une conformité d’accessibilité exhaustive.
