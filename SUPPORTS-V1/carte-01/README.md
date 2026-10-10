# Carte du système — proposition de support

**V1 expérimentale, carte 01.** Vue dérivée du produit `4e1f9cc20a9887d570a720934ca5b1752c78971a`. Le support est proposé à la discussion ; la direction visuelle n’est pas adoptée.

Ouvrir [la page](index.html), les SVG [clair](carte-claire.svg) et [sombre](carte-sombre.svg), ou [l’équivalent textuel](equivalent.md). Les [PNG](carte-claire.png) servent à l’aperçu. Les exports SVG et la page embarquent leurs fontes ; les liens vers les sections propriétaires pointent vers le commit produit exact sur GitHub.

La carte explique les entrées, les responsabilités et l’autorité des sections. Design reste le cœur. La gouvernance s’adapte au risque et au travail ; la maintenance concerne toutes les parties. La page permet de choisir un public sans masquer le reste. Sur petit écran, elle recompose le contenu en blocs de texte.

## Résultat et limites

- **27 contrôles réussis, aucun échec**, dans Chromium 151.0.7922.173 : six largeurs de 320 à 1440 px, deux thèmes, six entrées, clavier, export rouvert, texte agrandi, fonte de repli et JavaScript absent. [Rapport et empreinte](preuves/verification.json).
- La recette Gate A du produit ne relève aucun `RETURN` sur les quatre largeurs mesurées. Elle conserve les réserves de couverture du contraste et des noms accessibles. [Résultat détaillé](preuves/gate-a.log). Le calcul spécifique du texte SVG utilise les couleurs réellement peintes : minimum 5,65:1 en clair et 7,07:1 en sombre.
- Les six sorties du générateur se reconstruisent à l’identique. [Empreintes](preuves/reconstruction.json). Les SVG restent du texte sélectionnable, avec licence de la fonte conservée, y compris dans l’export de la sélection.
- Le titre Manrope est proposé pour sa continuité avec les labels. La variante Instrument Serif est consultable par `index.html?typo=serif` et dans les captures comparées à 1440 et 390 px. Il s’agit d’un choix d’auteur, pas d’une préférence utilisateur mesurée.

Ces résultats ne certifient pas une conformité exhaustive. La compréhension par les publics, le lecteur d’écran, Firefox, Safari, le téléphone réel et le rendu Mermaid restent non vérifiés. L’agrandissement mesuré porte sur le texte et son espacement ; il ne constitue pas un essai du zoom navigateur. Aucun bénéfice général du système n’est déduit de cette carte.

## Sources et reprise

`carte.json` porte le contenu, les relations, les publics et les palettes. `page.template.html` porte la mise en page et les interactions ; `construire.py` produit les six sorties listées dans `construction.json`. [Le langage visuel](langage-visuel.md) et [la trace](trace.md) expliquent les choix. Les deux fontes et leurs licences OFL sont conservées dans `fonts/`.

Depuis ce dossier :

```sh
python3 construire.py
python3 -m venv /tmp/dg-carte-venv
/tmp/dg-carte-venv/bin/pip install -r requirements.txt
DG_BROWSER_EXECUTABLE=/usr/bin/chromium DG_SOURCE_REPO=/chemin/du/depot /tmp/dg-carte-venv/bin/python verifier.py
```

Utiliser un Chromium installé et indiquer son chemin. Le lecteur de preuve résout les cibles dans Git au commit produit figé : il fonctionne aussi quand la branche documentaire est extraite. Le commit doit être présent dans le dépôt indiqué. Le serveur de mesure n’écoute que sur 127.0.0.1, choisit un port temporaire et s’arrête après la mesure. La nouvelle exécution remplace `preuves/` : copier d’abord ce dossier pour conserver une observation précédente.

La recette Gate A et le validateur de carte de décision se trouvent dans le produit au commit figé, pas sur cette branche documentaire. Les commandes exactes de cette observation sont consignées dans [la trace](trace.md). [run-card.json](run-card.json) est la projection de la décision exploratoire ; sa validation structurelle ne juge pas le design.

## Conservation et suite

`preuves-premier-essai/` garde les erreurs d’instrumentation du premier passage. `preuves-deuxieme-essai/` garde les deux débordements réellement observés avec texte agrandi avant correction. Le premier appel de Gate A utilisait un sélecteur inexistant ; il est conservé comme erreur de commande dans `preuves/gate-a-selecteur-errone.json`, séparément de la mesure finale corrigée. Ces résultats ne sont pas attribués à la version finale.

Ce premier lot livre une carte et une proposition de langage. Les cartes du parcours de travail et de la boucle créer/apprendre, leur intégration dans le produit, puis le nettoyage du journal public et des notes de version restent à réaliser. Les travaux historiques demeurent sur `refonte` ; concurrents et anglais restent reportés.
