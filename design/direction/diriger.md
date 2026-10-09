# Direction — diriger

Rendre la direction pilotable : cible visuelle, atelier de direction, direction divergente.

<!-- origine:DIRECTION.md -->
## DIRECTION/VISUAL_TARGET — rendre la direction pilotable

Sur une surface `DIRECTION`, la cible visuelle rassemble les décisions nécessaires avant le build. Elle ne remplace ni la spec détaillée ni les preuves d’ACTION. Elle empêche de commencer avec un adjectif, une palette ou une liste de composants.

| Champ | Décision à déclarer avant le build |
|---|---|
| **Thèse** | Quel monde, quel public et quelle promesse la surface doit-elle rendre crédibles ? |
| **Conséquence observable** | Ce que l’utilisateur doit percevoir, comprendre ou pouvoir faire dans la première scène si la thèse est tenue. |
| **Ancre** | `ANCHOR-GENERATED`, `ANCHOR-OBSERVED` ou `ANCHOR-PROVIDED` ; ce qui a été observé ; attributs retenus, rejetés et limites de transfert. |
| **Silhouette** | Rapport vide/masses, foyer, axe, cadre ou circulation reconnaissable sans le contenu fin. |
| **Relations de plans** | Relation entre premier plan, contexte, asset, preuve et action ; ne pas confondre profondeur décorative et hiérarchie de lecture. |
| **Opération visuelle dominante** | Relation par laquelle un contenu, une preuve ou une donnée rend la promesse perceptible. |
| **Matière / asset** | Rôle dans la promesse, route de production initiale, cadrage, zone sûre, contraste, mobile, fallback et condition de retrait. Une matière native au code — règle, trame, masque, gradient, typographie, SVG ou composition procédurale — est un choix complet lorsqu’elle porte mieux la relation qu’un asset externe. |
| **Typographie** | Rôle du display, du corps, des données et de l’action ; mesure, cadence et contre-indication. |
| **Objet de preuve** | Objet, média, état ou fenêtre produit qui répond directement à la promesse. |
| **Modal / parti** | Le modal nommé (ce que n’importe quelle IA produirait ici) et le parti : garder ou s’écarter, où et pourquoi, avec raison produit ou perceptuelle. |
| **Résolution initiale** | Quel niveau de contenu réel, d’état, de responsive, d’asset et de détail doit déjà tenir au premier rendu ? |

Cette table est la seule représentation canonique de la cible. L’opération dominante peut être discrète : retenue, vide, séquence, contraste de densité ou émergence d’un signal critique. Elle ne prescrit ni texture, ni type géant, ni masque, ni palette, ni composant.

### Compilation de la première proposition

Pour une surface visuelle ouverte, ne traite pas les champs de `VISUAL_TARGET` comme une liste indépendante. Compile-les dans cet ordre : **contexte réel → promesse → tension → relation perceptible → objet de preuve → geste → composition → matière, typographie et asset → états et contraintes → premier rendu jugeable**. La sortie attendue est une relation visible dans l’artefact, pas un dossier complet autour d’un artefact générique.

Les décisions de compilation se lisent dans la table : promesse = thèse + conséquence observable ; relation = opération dominante + relations de plans ; composition = silhouette + relations de plans ; résolution initiale = ligne du même nom.

La qualité ne vient pas d’une police, d’une image ou d’une texture ajoutées séparément, mais du renforcement mutuel de la composition, du contenu, du type, de l’objet de preuve, de la matière, des états et du comportement ; un élément sans relation visible est retiré ou sa limite nommée.

Un registre naturel, organique, éditorial, architectural, tactile ou technique est une hypothèse située, non un preset. Il peut modifier la matière, la respiration, la profondeur, la typographie, la donnée ou le geste lorsque cette relation appartient au produit. Dans une surface de qualité, l’agent peut aussi composer un composant authored : un objet visible dont la silhouette, le contenu, la hiérarchie, la matière et le comportement sont pensés pour le contexte, sans rendre les primitives critiques inhabituelles par principe.

**Qualifier la direction.** Une direction artistique est située lorsqu’elle relie un point de vue, un produit, un public, un contenu, un médium et une contrainte à un premier objet observable. Sa créativité se juge par la pertinence de l’écart ou de la relation produite, pas par la nouveauté seule ; son goût se lit dans la sélection, la proportion et la retenue des choix, pas dans une préférence universelle. Le craft et le polish du rendu construit restent jugés dans `SAVOIR` et vérifiés dans `ACTION` ; ils ne sont pas promis par la seule force de la thèse ou de la référence.

### Test d’utilité de l’ancre

Une ancre visuelle est suffisante seulement si elle apporte au moins :

1. une décision qui change réellement la structure, la hiérarchie, la matière ou le rapport texte/preuve ;
2. une contre-indication identifiable, c’est-à-dire un choix à ne pas transférer ;
3. une liste d’attributs retenus, rejetés et non transférables.

Une image jolie mais sans conséquence de décision est décorative et ne suffit pas comme ancre. Une référence ne prouve ni l’efficacité produit, ni le droit de réemploi, ni l’adéquation au public ; elle documente une relation observée ou une résolution de craft.

### Décider la route de production

Lorsqu’un asset ou son absence porte une décision perceptible, nomme **une route de production initiale** avant le build. Cette route peut être révisée sur preuve si la décision de direction reste stable et si la révision réduit un risque de droits, de performance, de fidélité, de maintenance ou d’intégration.

Ce n’est ni un statut, ni une préférence d’outil : c’est une réponse située au rôle de l’asset, aux droits, au délai et à la **destination**. En produit réel, un asset manquant devient une route `CODE-NATIVE` ou `SANS-ASSET` ou un emplacement marqué, jamais un faux asset ; en démo, une approximation marquée illustrative ; un contenu absent, un emplacement illustratif.

| Route | À retenir lorsque | À déclarer honnêtement |
|---|---|---|
| `CODE-NATIVE` | La relation utile est mieux portée par type, données, matière, SVG, mise en page ou mouvement produit. | Ce qui ne sera pas simulé comme image, photo ou illustration authentique. |
| `FOURNI` | Un asset réel transmis ou déjà autorisé porte la promesse. | Disponibilité, droit connu ou inconnu, zones de crop et contraintes d’usage. |
| `CURATÉ` | Une source externe autorisée apporte une matière, une preuve ou une spécificité qu’il serait faible de simuler. | Provenance, droit, transformation prévue et raison de ce choix plutôt qu’un voisin facile. |
| `GÉNÉRÉ-DIRIGÉ` | Une image originale sert réellement la direction et aucune source autorisée observée dans le scope, le délai et les droits du run ne résout mieux le besoin. | Direction de composition, référence(s) de calibration, modèle/outil si connu, itérations observées et limites de fidélité. |
| `HYBRIDE` | La valeur vient de la rencontre entre asset, composition, traitement, donnée, type ou code. | Quelle part porte le sens, ce qui est transformé et le fallback si l’asset est retiré. |
| `SANS-ASSET` | La retenue porte mieux la relation que tout asset. | Ce qui porte la promesse à la place et la condition qui ferait revenir sur ce choix. |

La génération ne reçoit ni le rôle de défaut, ni celui de rattrapage décoratif. Une image générée est une **hypothèse visuelle comparable**, non une autorité esthétique. Une référence observée est un calibrateur, non un modèle à reproduire. La recherche ne vaut pas accumulation : elle explore seulement lorsqu’une source, un médium ou un registre peut modifier la direction.

Une route est insuffisante si elle n’explique pas pourquoi l’asset, à son crop réel et dans son contexte réel, augmente la preuve, la compréhension ou la singularité de la surface. Sources par couche : carte des moyens (`SAVOIR/TOOLS`, `[VEILLE]`) ; un asset moyen reçoit le traitement que justifie la thèse (`SAVOIR`, section `DESIGN-ATLAS`), jamais un dessin de remplacement.

### Réserve `ANCHOR-GENERATED` en enjeu identitaire élevé

Lorsque l’enjeu identitaire est élevé et que seule la voie `ANCHOR-GENERATED` — hypothèse visuelle générée — est utilisée, la `RUN_CARD` porte une réserve explicite : « Direction calibrée uniquement sur hypothèse générée, sans référence observée ni contrainte réelle. » Le statut de direction ne peut pas être `HELD` sans cette réserve ou sans calibration complémentaire par `ANCHOR-OBSERVED`, `ANCHOR-PROVIDED` ou contrainte réelle. Cette réserve décrit une limite de calibration ; elle ne déclare ni l’image fausse, ni la direction invalide par principe. Dans une `RUN_CARD`, cette base est `direction.calibration.basis` : `real_constraint` lorsqu’une contrainte réelle calibre la direction, sinon `generated_only_reserved`, qui interdit `ACCEPTED` (`ACTION/PIPELINE-DIRECTION`).

> **Passage à `SPECCED`.** Dans `ACTION/STATUS`, `SPECCED` signifie que la direction, la hiérarchie, le contrat ou l’ancre nécessaires sont disponibles ; cela ne signifie ni construit, ni observé, ni accepté. Une surface `DIRECTION` est prête à construire lorsque chaque champ de la table de `VISUAL_TARGET` est renseigné ou `N/A-JUSTIFIED` ; la route d’asset seulement si nécessaire.

La cible peut vivre dans la `RUN_CARD`, le ticket ou le manifeste local. Après le build, `ACTION/VISUAL_PROOF` vérifie le rendu réel contre cette cible.

---

<!-- origine:DIRECTION.md -->
## DIRECTION/DIRECTION-ATELIER — module officiel de direction située

`DIRECTION-ATELIER` est un module de craft officiel de V1. Il est **activable**, jamais automatique : utilise-le pour une surface `DIRECTION` lorsque la première scène, l’identité, la confiance culturelle ou la relation entre promesse et preuve demandent une position située. Ne l’active pas si son contrat ne peut modifier ni la structure, ni l’objet de preuve, ni le choix de direction. Il ne doit jamais devenir un questionnaire imposé à la personne. La direction reste le propriétaire du cadrage créatif ; la preuve exécutée, les gates, les verdicts et la clôture restent ceux d’`ACTION`.

> **Règle de portée.** Une fois le module activé, son noyau s’applique dans la même trace locale que `DIRECTION/VISUAL_TARGET`. Il n’ajoute ni mode, ni gate, ni statut, ni owner, ni seconde `RUN_CARD`. `ACTION` reste le propriétaire de la preuve, de la capture, de `CAPABILITY-BASIS`, des verdicts et de la clôture.

### Noyau du contrat

Le contrat utilise la cible visuelle existante ; il ne la remplace pas par un formulaire parallèle. Il rend explicites les décisions qui risquent autrement de se réduire à un adjectif, une palette ou une tendance.

| Élément | Décision à rendre retrouvable | Limite à conserver |
|---|---|---|
| **Moment humain** | Dans quelle situation concrète la personne rencontre-t-elle la promesse ? | Ce n’est pas un portrait de public ni une donnée utilisateur validée. |
| **Tension** | Quelle polarité organise la direction : hésitation/élan, densité/respiration, mémoire/disparition, contrôle/transmission ou équivalent situé ? | La tension ne suffit pas si elle ne change aucune décision visible. |
| **Geste produit** | Quelle action, relation ou transformation l’artefact rend-il perceptible ? | Un geste de démonstration ne prouve pas un résultat produit réel. |
| **Position et exclusion** | Quelle lecture est retenue, et quel gabarit, effet ou relation est refusé avec une raison produit ou perceptuelle ? | L’exclusion n’impose ni nouveauté ni opposition artificielle. |

Lorsque le choix est ouvert, formule des familles internes réellement distinctes, puis conserve la position retenue et un **contre-choix situé** : le choix plausible qui serait meilleur sous une autre contrainte. Ces familles restent internes ; la personne reçoit une proposition principale, sauf arbitrage stratégique ou demande explicite. Si aucun choix plausible ne peut modifier la décision, l’absence de contre-choix est `N/A-JUSTIFIED` dans la trace existante. Aucun quota de familles, de variantes ou de builds n’est créé.

### Vérité de la scène et clôture de craft

<!-- noyau:début VER-SCENE -->
<!-- concept:HON-01 -->
Place un **marquage local de vérité** à proximité du claim ou de l’objet concerné. Ce marquage n’est ni un statut ACTION, ni une voie d’ancrage, ni un verdict. Il a deux axes : la **factualité**, `OBSERVED` ou `ILLUSTRATIVE`, obligatoire et exclusive ; la **nature**, `MECHANISM`, qui se cumule avec la factualité. La fiction l’emporte : un élément illustratif rend le tout `ILLUSTRATIVE`.
<!-- noyau:fin VER-SCENE -->

| Label local | Signification exacte |
|---|---|
| `TRUTH/OBSERVED` | L’affirmation se limite à l’artefact, la capture, le test ou la source réellement observés ; sa base et son scope restent déclarés selon ACTION. |
| `TRUTH/ILLUSTRATIVE` | L’objet, le contenu ou l’exemple sert à rendre une hypothèse visible ; il ne représente ni une personne, ni une donnée, ni un résultat réels. |
| `TRUTH/MECHANISM` | Le rendu matérialise une relation produit, une action ou une transformation ; il ne prouve pas à lui seul un effet externe, une préférence ou une tâche réussie. |

<!-- noyau:début VER-AUDIENCE -->
**Audience.** Les labels `TRUTH/*` sont internes : spec, trace, annotations. Ils n’apparaissent jamais dans l’interface produit. Quand le public doit savoir, la divulgation se fait en langage produit (« données d’exemple », « taux illustratifs »).
<!-- noyau:fin VER-AUDIENCE -->

Après le build, utilise la capture et les preuves applicables d’ACTION. La critique de craft, consignée dans la revue créative unique, emploie des verbes et leurs effets — par exemple **isole**, **déplace**, **matérialise**, **ralentit**, **efface** — puis nomme le défaut ou la réserve qui reste. « Premium », « beau » ou « créatif » ne constituent pas une preuve de clôture.

Le module est terminé lorsqu’il a changé, confirmé ou abandonné une décision visible, ou documenté honnêtement qu’il ne pouvait pas le faire : `N/A-JUSTIFIED` si aucune conséquence n’était applicable, `NOT-OBSERVED` si la conséquence attendue n’a pas été observée (`ACTION/STATUS`). Il reste un conseil de craft instrumenté : il ne garantit ni goût universel, ni préférence, ni compréhension utilisateur, ni conformité, ni qualité de sortie par simple invocation.

<!-- origine:DIRECTION.md -->
## 1. Direction divergente — déclenchement `DIRECTION`

Le mode `DIRECTION` exige une comparaison de positions réellement distinctes lorsque la décision est ouverte. Il ne demande pas un catalogue de variantes et n’impose aucun quota de nouveauté.

Avant de diverger, situe la première idée sur les axes de position de `SAVOIR/CRAFT/CFT-02`, leur seul propriétaire : structure, matière, voix, temporalité, densité, rapport texte/image.

<!-- concept:ALT-01 -->
En `DIRECTION`, considère une **alternative située** lorsque la décision est ouverte et qu’une position différente peut raisonnablement modifier le choix. Elle doit répondre à un public, un JTBD, une contrainte ou une opportunité distincte. Ses leviers sont les axes de `SAVOIR/CRAFT/CFT-02` ; sa matérialisation, sa trace selon le niveau retenu et sa comparaison suivent `ACTION/PIPELINE-DIRECTION` (étapes 3 et 7).

La direction retenue ne l’emporte que si son avantage est formulé en une phrase vérifiable reliant la position à un effet attendu sur la tâche, la compréhension, la preuve, la singularité ou la contrainte. Une palette seule, un adjectif ou une variation cosmétique ne constituent pas une direction distincte.

L’axe matière doit toujours être **déclaré**, y compris lorsqu’il est hérité, plat, absent ou inchangé. Il n’impose jamais une texture. Une surface peut être plate, photographique, illustrée, spatiale ou retenue si cette position sert mieux le contenu, la tâche, la preuve ou la contrainte.

Le checkpoint suit `ACTION/PIPELINE-DIRECTION` : la première proposition en tient lieu, sauf action irréversible ou coûteuse ; elle présente la position retenue, l’alternative considérée, la raison du choix et la preuve attendue. Si le regard requis n’est pas disponible, le run indique `BLOCKED`, `EXPLORATORY` ou le statut prévu par `ACTION` ; l’absence ne devient jamais une validation implicite.

---
