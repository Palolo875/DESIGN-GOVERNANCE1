# Sections de référence — BIBLIOTHEQUE : structures d’interface situées

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. BIBLIOTHEQUE sélectionne les responsabilités structurelles — support, grille, scène, objet, micro-interface, modificateur, primitive et couche — puis les encadre par des contrats transversaux (`BIBLIOTHEQUE/CONTRACTS`, `BIBLIOTHEQUE/COMPAT`).

<!-- lieux:début -->
> **Ce fichier ne contient pas toute la responsabilité `BIBLIOTHEQUE`.** Il contient les sections rangées dans ce fichier ; les autres sections `BIBLIOTHEQUE` vivent à leur emplacement, avec la même autorité, et ne sont pas recopiées ici. Une route se lit avec `python3 scripts/read_route.py LOCATOR`, qui trouve son fichier. _Bandeau généré par `scripts/build_core.py` depuis le registre `LIEUX` ; ne pas modifier à la main._
>
> - [`gouvernance/structure.md`](../gouvernance/structure.md) : `BIBLIOTHEQUE/CONTRACTS`, `BIBLIOTHEQUE/GATE`
> - [`design/formes/choisir.md`](../design/formes/choisir.md) : `BIBLIOTHEQUE/READ`, `BIBLIOTHEQUE/TENSION`, `BIBLIOTHEQUE/SIGNATURE`, `BIBLIOTHEQUE/SELECT`, `BIBLIOTHEQUE/AVANT-SELECTION`, `BIBLIOTHEQUE/DERIVE`
> - [`design/formes/catalogue.md`](../design/formes/catalogue.md) : `BIBLIOTHEQUE/SUPPORT`, `BIBLIOTHEQUE/GRID`, `BIBLIOTHEQUE/SCENE`, `BIBLIOTHEQUE/SEQUENCE`, `BIBLIOTHEQUE/OBJECT`, `BIBLIOTHEQUE/MICRO`, `BIBLIOTHEQUE/MODIFIER`, `BIBLIOTHEQUE/COMPONENTS`, `BIBLIOTHEQUE/COMPAT`
> - [`maintenance/evolution.md`](../maintenance/evolution.md) : `BIBLIOTHEQUE/EVOLUTION`
<!-- lieux:fin -->

<!-- orientation:début -->
## Responsabilité

BIBLIOTHEQUE est le système de sélection des **structures d’interface**. Elle décrit où une surface vit, comment le regard circule, comment texte, information, média et preuve se rencontrent, et quelles unités rendent une action tangible.

**Capacité positive de BIBLIOTHEQUE.** BIBLIOTHEQUE aide à transformer une décision de direction ou de produit en structure habitable, compatible et maintenable. Elle permet de choisir, adapter ou faire évoluer le support, la grille, la scène, l’objet, la micro-interface ou la couche qui rendent une relation perceptuelle et une action réellement tangibles. Elle augmente la robustesse et la richesse des possibilités sans imposer un style ; la structure retenue doit toujours servir une décision située et pouvoir être observée dans un premier objet.

**Chemin de sélection.** Après `DIRECTION/START` et la classification du mode, du risque, du scope et de la capacité, commence par la décision que la structure doit modifier, puis vérifie la relation perceptuelle ou produit concernée, la preuve attendue, la compatibilité et le coût de maintenance. Charge seulement les niveaux de structure nécessaires ; si aucune décision ne change, l’héritage explicite ou documentaire est préférable à une sélection décorative et `N/A-JUSTIFIED` ne s’emploie que selon le contrat ACTION.

Elle ne décrit pas un goût à reproduire, ne choisit pas le mode et ne ferme pas un run. Elle ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Mode, risque, classification, absolus, cible, capacité et routage général. |
| `ACTION.md` | Runs, méthodes, preuves exécutables, états, issues, gates, verdicts et clôture. |
| `SAVOIR.md` | Jugement, craft, styles, contexte, états spécialisés et intégrité. |
| `maintenance/evolution.md` et `maintenance/versions.md` | Cycle de vie des routes, migrations, promotions, dépréciations et décisions de gouvernance. |

### Orientation interne et sortie de sélection

Après `DIRECTION/START`, et après `SAVOIR/STYLE` seulement si le registre d’expression peut modifier la structure, commencez par `BIBLIOTHEQUE/READ`, puis `SELECT` si une décision structurelle est ouverte. Cette instruction est interne à BIBLIOTHEQUE et ne remplace jamais le démarrage DIRECTION. La chaîne `support → grille → scène → objet → primitive` décrit des responsabilités, pas un ordre obligatoire de chargement. `sections/READING_MAP.md` est une vue dérivée pour le déclencheur et le non-chargement.

Toute sélection ou non-sélection doit transmettre : `DECISION`, niveau ou héritage, `STRUCTURAL-SIGNATURE` si applicable, contre-indication, premier objet attendu, preuve, limite, owner et condition de sortie. Ces champs sont une projection structurelle locale vers le handoff canonique ACTION ; ils ne le remplacent pas. Le reste de la transmission suit le handoff canonique (`ACTION/HANDOFF`). Si la structure existante suffit, utilisez l’héritage ou le cas documentaire ; `N/A-JUSTIFIED` est réservé à une non-applicabilité justifiée selon ACTION. La clôture et le verdict restent chez ACTION.

**Condition d’arrêt de lecture :** arrêter lorsque la relation structurelle à modifier, la route ou l’héritage, la conséquence observable, la preuve, la limite et le propriétaire suivant sont explicites.

En run local, le contrat réduit de `BIBLIOTHEQUE/CONTRACTS` suffit ; si la structure existante suffit, conserve l’héritage ou le cas documentaire avec sa source et sa justification. `N/A-JUSTIFIED` est réservé à une non-applicabilité réelle selon ACTION. Les exigences par périmètre de contribution (pilote, partagé, durable) et les statuts de cycle de vie relèvent de `BIBLIOTHEQUE/EVOLUTION`.
<!-- orientation:fin -->

<!-- noyau:début STRUCT-OU -->
> L’interface ne commence ni avec une « landing premium », ni avec une grille de cartes, ni avec une image inspirante. Elle déclare d’abord **où elle vit**, **comment le regard circule**, **quelle preuve devient tangible** et **comment la personne agit**.
<!-- noyau:fin STRUCT-OU -->
