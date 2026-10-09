# BIBLIOTHEQUE — Structures d’interface situées

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. BIBLIOTHEQUE sélectionne les responsabilités structurelles — support, grille, scène, objet, micro-interface, modificateur, primitive et couche — puis les encadre par des contrats transversaux (`BIBLIOTHEQUE/CONTRACTS`, `BIBLIOTHEQUE/COMPAT`).

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
| `CHANGELOG.md` | Cycle de vie des routes, migrations, promotions, dépréciations et décisions de gouvernance. |

### Orientation interne et sortie de sélection

Après `DIRECTION/START`, et après `SAVOIR/STYLE` seulement si le registre d’expression peut modifier la structure, commencez par `BIBLIOTHEQUE/READ`, puis `SELECT` si une décision structurelle est ouverte. Cette instruction est interne à BIBLIOTHEQUE et ne remplace jamais le démarrage DIRECTION. La chaîne `support → grille → scène → objet → primitive` décrit des responsabilités, pas un ordre obligatoire de chargement. `READING_MAP.md` est une vue dérivée pour le déclencheur et le non-chargement.

Toute sélection ou non-sélection doit transmettre : `DECISION`, niveau ou héritage, `STRUCTURAL-SIGNATURE` si applicable, contre-indication, premier objet attendu, preuve, limite, owner et condition de sortie. Ces champs sont une projection structurelle locale vers le handoff canonique ACTION ; ils ne le remplacent pas. Le reste de la transmission suit le handoff canonique (`ACTION/HANDOFF`). Si la structure existante suffit, utilisez l’héritage ou le cas documentaire ; `N/A-JUSTIFIED` est réservé à une non-applicabilité justifiée selon ACTION. La clôture et le verdict restent chez ACTION.

**Condition d’arrêt de lecture :** arrêter lorsque la relation structurelle à modifier, la route ou l’héritage, la conséquence observable, la preuve, la limite et le propriétaire suivant sont explicites.

En run local, le contrat réduit de `BIBLIOTHEQUE/CONTRACTS` suffit ; si la structure existante suffit, conserve l’héritage ou le cas documentaire avec sa source et sa justification. `N/A-JUSTIFIED` est réservé à une non-applicabilité réelle selon ACTION. Les exigences par périmètre de contribution (pilote, partagé, durable) et les statuts de cycle de vie relèvent de `BIBLIOTHEQUE/EVOLUTION`.

<!-- noyau:début STRUCT-OU -->
> L’interface ne commence ni avec une « landing premium », ni avec une grille de cartes, ni avec une image inspirante. Elle déclare d’abord **où elle vit**, **comment le regard circule**, **quelle preuve devient tangible** et **comment la personne agit**.
<!-- noyau:fin STRUCT-OU -->

---

## BIBLIOTHEQUE/GATE — contrôle de module structurel complémentaire

Ce contrôle appartient au périmètre de BIBLIOTHEQUE. Il ne constitue pas un quatrième gate global : `ACTION/GATE-A`, `ACTION/GATE-B` et `ACTION/GATE-C` restent les gates canoniques du run.

Il s’agit d’un **contrôle structurel complémentaire**, pas d’une route de clôture concurrente. BIBLIOTHEQUE peut décrire le parti structurel et sa limite ; `ACTION` reste propriétaire du scope, de la méthode, de la preuve, des statuts, des issues, du verdict de livraison et de la clôture. `BIBLIOTHEQUE/GATE` ne possède ni statut ni verdict propres.

<!-- concept:PRC-01 -->
Le contrôle de module vérifie support, grille, scène, objet, états, mobile et accessibilité structurelle, pas seulement code ou conformité d’une primitive. Il vérifie également que la thèse structurelle est visible dans le premier objet habitable et que la relation déclarée reste observable lorsque le contenu, le viewport ou l’état changent. Pour une micro-interface d’identification, de santé, de permission ou de récupération, reviens à `DIRECTION/START` pour la classification et à `ACTION` pour la preuve, le scope et le verdict ; le contrat structurel seul ne suffit jamais.

| Test | Question | Type possible |
|---|---|---|
| Non-généricité | Sans image, données et nom, la structure pourrait-elle appartenir à cinquante produits ? Si oui, la structure dépend de ce qui a été retiré. Si la dépendance est porteuse (relation déclarée, fallback prévu par `DIRECTION/VISUAL_TARGET`), la conserver. Si elle est décorative, changer la relation support/grille/scène/preuve plutôt qu’ajouter du polish. Dans les deux cas, décider sur le rendu entier, la tâche et `ACTION/GATE-C`. | `PERCEPTUAL`, `EXPERT` |
| Silhouette | Après floutage, support, foyer, masses et axes restent-ils perceptibles ? | `PERCEPTUAL` |
| Grille | Éléments critiques partagent-ils un axe, rythme ou relation identifiable ? Les ruptures changent-elles une priorité ? | `PERCEPTUAL`, `EXPERT` |
| Preuve | Objet ou micro-interface répond-il à la promesse avec contenu, état et action crédibles ? | `EXPERT`, `USER/TASK` |
| Asset | Route de production, cadrage, occupation et contraste changent-ils support, scène ou preuve ? Source, droits, provenance et raison de route sont-ils tracés ? | `TECHNICAL`, `EXPERT` |
| Clarté | Tâche, référence, conséquence et action sont-elles lisibles ? | `EXPERT`, `USER/TASK` |
| États | Loading, empty, error, unavailable, disabled, succès, contenu long et données sensibles préservent-ils le rôle ? | `TECHNICAL`, `USER/TASK` |
| Mobile | Priorité, voisinage, action, état, contenu et performance sont-ils recomposés plutôt que compressés ? | `TECHNICAL`, `USER/TASK` |
| Accessibilité | Focus, clavier, contrastes, noms, alternatives et information non chromatique sont-ils présents ? | `TECHNICAL`, `USER/TASK` |
| Contexte | La structure répond-elle au public, au JTBD et au risque dominant ? | `EXPERT`, `USER/TASK` |
| `DECISION-CHANGE` | Après observation, la sélection a-t-elle changé, confirmé ou abandonné une décision, ou est-elle seulement documentée ? | Sortie de trace ACTION ; méthode et scope séparés |

BIBLIOTHEQUE/GATE reste complémentaire d’ACTION/GATE-A, B et C. BIBLIOTHEQUE vérifie le parti structurel et rend explicite la limite ; ACTION contrôle scope, méthode, preuve et verdict de livraison.

### Statut ACTION du contrôle structurel

Ce contrôle ne possède ni statut ni verdict propres. Les statuts ACTION applicables sont `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` ou `NOT-VERIFIED`, dans le registre de gate ou de preuve approprié.

Une description dans la `RUN_CARD` peut suffire pour une relation simple et non critique. Une relation visuelle critique exige une capture annotée, un rendu ou une comparaison adaptée. Une description seule ne devient pas une preuve de rendu.

Une chaîne de routes complète sans `DECISION-CHANGE` observable est une trace documentaire, pas une preuve de structure.

La structure reçoit la route d’asset décidée par `DIRECTION` et vérifiée par `ACTION` seulement lorsqu’elle modifie support, scène, objet ou mobile. Elle ne source ni ne hiérarchise les outils. La preuve structurelle reste locale au run ; BIBLIOTHEQUE ne devient ni galerie d’assets, ni archive de références visuelles, ni corpus de goût.

---

## BIBLIOTHEQUE/EVOLUTION — promotion et dépréciation

BIBLIOTHEQUE est stable dans ses responsabilités, mais pilotée dans ses routes. Une route devient durable après plusieurs usages contrastés documentés, lorsque sa responsabilité reste stable, son contrat est complet, sa maintenance est assumée, ses rendus ne s’homogénéisent pas et un gain réel est observé ou mesuré avec baseline, contexte et limite. Elle doit également démontrer qu’elle permet des premiers objets composés, spécifiques et crédibles dans ces contextes, et pas seulement des structures conformes ou jolies dans un screenshot.

**Mesure de lecture.** Pour mesurer ce qu’un run instrumenté lit dans les routes structurelles, les catégories de `DIRECTION` (« Lecture instrumentée et règle de passage ») s’appliquent ; un run ordinaire ne les déclare pas.

### Contrat minimal par périmètre de contribution et statut de route

| Niveau | Minimum attendu | Ne pas exiger par défaut |
|---|---|---|
| Local | Contrat réduit (`BIBLIOTHEQUE/CONTRACTS`) ; héritage ou cas documentaire si la structure suffit, avec source et justification ; `N/A-JUSTIFIED` seulement si réellement non applicable selon ACTION. | Contrat complet de promotion. |
| Route au statut `PILOT` | Contrat réduit, contre-indication, preuve, `DECISION-CHANGE` et périmètre déclaré. | Adoption ou compatibilité générale. |
| Partagé | Contrat complet, consumers, owner, compatibilité, états, mobile, accessibilité, migration et rollback selon le risque. | Promotion silencieuse. |
| Durable | Usages contrastés, baseline, observation ou mesure de gain, maintenance, owner et prochaine revue. | Validation par beauté, fréquence ou screenshot unique. |

`SEED`, `PILOT`, `ADOPTED`, `DEPRECATED` et `ABANDONED` sont des statuts de cycle de vie `CHANGELOG`, jamais des modes, niveaux de structure, états, issues ou verdicts `ACTION`. `OWNER` désigne le responsable de la décision et de sa prochaine preuve ; `NEXT-OWNER` désigne le destinataire de l’action suivante ; l’owner de maintenance d’une route partagée reste distinct et se conserve dans le contrat d’évolution.

### Contrat de gain réel

Le gain réel ne doit pas être déclaré sans :

```text
TASK / DECISION
BASELINE
OBSERVATION OR MEASURE
CONTEXT
LIMIT
OWNER
NEXT-REVIEW
```

Il peut s’agir d’une réduction d’erreur, d’une décision plus directe, d’un temps de décision réduit, d’une diminution de réassemblage ou d’une maintenance plus fiable. La nature du gain et la limite de l’observation sont toujours nommées.

| Critère | Preuve attendue |
|---|---|
| Usages contrastés | Plusieurs usages distincts, documentés dans des runs et non une répétition du même cas. |
| Responsabilité claire | La route réduit une décision identifiable. |
| Contrat complet | Usage, contre-indication, preuve, états, mobile, a11y, owner et revue. |
| Gain réel | Tâche/baseline/observation ou mesure/contexte/limite. |
| Non-homogénéisation | Les rendus restent situés malgré la route commune. |
| Maintenance | Owner et prochaine revue nommés. |

Une route peut être `SEED`, `PILOT`, `ADOPTED`, `DEPRECATED` ou `ABANDONED` dans la gouvernance du `CHANGELOG`. Ces statuts ne sont pas des verdicts d’écran, des issues de run ou des statuts de gate.

### Contribution et retour d’usage

Une proposition de route commence par ce qui existe déjà : vérifier les routes compatibles, les discussions ou les usages documentés, puis expliquer la décision que la nouvelle combinaison permet de mieux prendre. Une contribution n’est promue que si ses usages, sa contre-indication, sa preuve, son owner, son coût de maintenance et sa prochaine revue sont lisibles. Les retours d’équipe, d’usagers ou de production peuvent corriger le contrat ; ils ne remplacent pas l’observation du run ni ne créent un gate supplémentaire.

Le niveau de contribution reste proportionné au risque : un run local peut conserver une trace courte ; une route partagée exige un contrat et une preuve de gain ; une promotion ou une dépréciation relève de `CHANGELOG`. Ne pas transformer la recherche de feedback, la revue communautaire ou le nombre de réutilisations en quota ou en verdict automatique.

**Chaîne de promotion et de gouvernance.** Lorsqu’une route devient partagée ou candidate à une durée canonique, `DIRECTION/START` classe le risque et le blast radius ; `ACTION/RUN-SYSTEM` prépare l’impact, les consumers, l’owner, la preuve, la compatibilité, la migration et le rollback ; `BIBLIOTHEQUE/EVOLUTION` examine les usages contrastés, le gain réel, la non-homogénéisation et la maintenance ; `CHANGELOG` persiste uniquement la décision de cycle de vie autorisée. Une route locale ou exploratoire ne doit pas ouvrir cette chaîne complète sans raison.

Un style reste dans `SAVOIR/STYLE`. Une image, un site, une capture ou un asset reste local à la `RUN_CARD` ou à l’artefact de projet déjà disponible. Une route locale ne devient pas canonique simplement parce qu’elle est jolie ou fréquemment demandée.

Les anciens aliases `REFERENCES/QUERY`, `REFERENCES/SOURCE`, `REFERENCES/ASSET`, `REFERENCES/MEMORY` et `REFERENCES/CORPUS` sont `DEPRECATED` et ne doivent pas apparaître dans un nouveau run. Leur mapping est défini dans la section « Migration des anciens aliases » de `CHANGELOG.md`, pas dans les instructions actives.
