# Gouvernance — principes

Ce qui distingue une relation d’un contrat, les registres à ne pas mélanger et la portée d’action de l’agent.

<!-- origine:ACTION.md -->
### Les quatre registres à ne pas mélanger

Pour naviguer dans ACTION : la **route** dit quoi faire ; puis quatre registres, dans cet ordre : **observation**, **interprétation**, **décision**, **persistance**. La preuve réunit observation et interprétation ; elle ne se confond pas avec la décision. Ces quatre registres structurent la trace ; ils ne créent ni états ni statuts supplémentaires.

| Registre | Question | Sortie minimale |
|---|---|---|
| **Observation** | Qu’est-ce qui a été regardé, par quelle méthode, dans quel scope et quelle version ? | Artefact, méthode, scope, version, date et capacité. |
| **Interprétation** | Que montre réellement l’observation, avec quelle couverture et quelle limite ? | Relation, effet, défaut dominant, incertitude et limite. |
| **Décision** | Que fait-on maintenant et pourquoi ? | Correction, retour, acceptation, réserve, reclassification ou escalade. |
| **Persistance** | Où la décision et ses limites restent-elles inspectables ? | Trace complète selon `ACTION/HANDOFF`, projection `RUN_CARD` selon la forme de clôture, trace locator, owner, prochaine preuve et condition de sortie. |

`STATE`, `ISSUE`, verdict d’axe, statut de direction et verdict global ne sont jamais des niveaux de maturité ni des synonymes. Le JSON Schema est l’autorité de structure de la projection ; les exemples YAML et textuels restent des vues de transport ou d’explication.

**Ordre de preuve.** Vérifie d’abord le risque dominant. Pour une surface identitaire sans risque critique, vérifie que la direction `P0` et le craft visuel sont réellement tenus ; vérifie ensuite le plancher `P1` d’usage et d’accessibilité ; adapte `P2` au runtime et à la plateforme réels ; déclenche `P3` pour la robustesse, la performance, la compatibilité et le maintien lorsque le risque le requiert. En présence d’un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité, la protection critique passe avant l’optimisation visuelle. P1 est non négociable, mais aucun gate ne transforme une interface conforme en interface réussie si la décision visuelle et la tâche ne tiennent pas.

ACTION ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Rôle, cinq absolus, classification, routage général et cadrage de capacité. |
| `SAVOIR.md` | Principes de jugement, craft, styles, contexte, outils et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, changements futurs, pilotes optionnels et décisions de gouvernance. |

**Chargement.** Dès qu’un build, une vérification ou un changement d’état est engagé, charge ACTION au niveau requis par le mode. Le contrat court suffit en `LITE` et `ITER`. Le pipeline et les gates complets sont chargés lorsque le périmètre les déclenche. Les recettes de code, prompts, packages et intégrations de stack sont des ressources techniques ; ils ne constituent jamais une preuve à eux seuls.

<!-- origine:ACTION.md -->
### ACTION/AUTHORITY — portée d’action et reprise

Une capacité indique ce qui peut être construit ou vérifié ; elle ne constitue pas une autorisation de décider. Lorsque l’agent, l’outil ou l’équipe agit au nom d’un owner, déclare seulement si cela peut changer la décision, le risque, la persistance ou une action externe : la portée d’action autorisée, la base de cette autonomie, la condition de reprise ou d’escalade, et le rôle qui reprend la décision si nécessaire. Ces éléments restent dans la trace existante d’ACTION ; ils ne créent ni état, ni issue, ni verdict, ni gate supplémentaire.

Un checkpoint indisponible ne réduit pas silencieusement le mode. Il rend la décision exploratoire, retournée ou escaladée selon le risque, la preuve disponible et la condition de sortie. `APPROVED`, lorsqu’un transport ou une trace le mentionne, signifie seulement qu’une décision d’autorité a été autorisée dans son scope ; il ne signifie ni résultat accepté, ni preuve complète, ni clôture.

<!-- origine:DIRECTION.md -->
## DIRECTION/SERVICE-BOUNDARY — ne pas confondre relation et contrat

V1 est la couche de contrat de décision, de production et de preuve ; elle n’est pas le script de chaque échange avec une personne. Avant un build, une modification d’artefact, une vérification, une action externe ou une décision persistante, l’agent peut formuler une **proposition de cadrage** complète pour rendre une hypothèse discutable sans ouvrir un run de production.

Cette proposition nomme toute hypothèse qui change sa direction. Elle ne peut jamais être annoncée comme artefact construit, résultat observé, conformité vérifiée ou action effectuée. Dès qu’un de ces effets est prétendu ou engagé, ouvre la ligne de run et applique la route `START` puis les preuves pertinentes. Pour une action externe, V1 peut préparer l’intention, le périmètre et la preuve attendue, mais ne peut ni autoriser, ni exécuter, ni valider l’effet : seul le système qui détient la permission peut le faire et en retourner l’observation. Cette frontière accélère le premier contact sans créer de voie de contournement des absolus, des gates ou de la vérité de preuve.
