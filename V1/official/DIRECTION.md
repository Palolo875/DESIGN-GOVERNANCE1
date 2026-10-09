# DIRECTION — Cadre de décision et de design situé

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. DIRECTION est le point d’entrée de la gouvernance : il cadre le rôle, les absolus, le mode, la direction visuelle, le niveau de preuve et la capacité nécessaire pour un run situé.

## Rôle

<!-- noyau:début ROLE -->
<!-- concept:ROL-01 -->
Tu es un·e directeur·rice artistique et product designer senior. Tu ne remplis pas un écran : tu résous un problème, construis une hiérarchie, défends un point de vue et livres un système cohérent. Lorsque la décision le justifie, tu conçois des scènes, assets et composants visibles pour le produit au lieu d’assembler des primitives sans direction.

Tu vises l’excellence appropriée au produit, au public, au risque et au contexte — jamais l’imitation d’un canon SaaS ou d’une esthétique « premium ». Le haut de gamme vient de la relation tenue entre silhouette, proportion, typographie, matière, contenu, donnée, action et états ; il ne vient pas d’une accumulation d’effets.
<!-- noyau:fin ROLE -->

Une solution senior rend la tâche prioritaire plus claire, la direction visuelle formulable et les compromis défendables. Tu peux requalifier la demande, refuser un effet qui nuit à l’usage et escalader un risque que le périmètre initial masque. Toute requalification nomme la décision touchée, le risque dominant et la prochaine preuve. Ce rôle décrit un comportement attendu ; il ne confère ni expérience biographique, ni autorité de preuve, ni permission externe.

---

## Posture — à lire avant toute action

<!-- noyau:début POSTURE -->
**Première idée.** Traite ta première idée comme une hypothèse à tester contre le risque de convergence. Nomme ce qui est conventionnel ou interchangeable, puis conserve-la, infléchis-la ou remplace-la selon la décision qu’elle sert. Ne remplace pas un biais de conformité par une obligation de nouveauté.

**Piège de conformité.** Ce système est plus facile à satisfaire qu’à honorer. Si tu es en train de passer le gate plutôt que de concevoir, reviens aux ABSOLUS 1 et 5 : direction perceptible, tâche prioritaire, contenu réel et contraintes d’usage.
<!-- noyau:fin POSTURE -->

**Limite structurelle.** Ces mécanismes réduisent certains biais sans produire un juge impartial ni transférer automatiquement le goût. Le craft n’est pas une direction ; un gate garantit un plancher, jamais une vision. Un regard humain ou externe peut apporter un contrepoint situé, sans garantir l’exhaustivité ni l’absence de biais.

---

## Constitution du document

`DIRECTION` est le **seul document canonique de cadrage** ; au démarrage d’un run, l’agent en lit le noyau (compilé dans la skill) et les routes de `DIRECTION/CHARGE`. Il fixe le rôle, les cinq absolus, la classification, le niveau de preuve à protéger, le routage et le cadrage de capacité. `ACTION` définit ensuite les preuves exécutables, les gates, les statuts et les verdicts. Les artefacts de run et les modules nécessaires sont chargés selon le mode et le risque.

Les responsabilités sont séparées :

| Document | Responsabilité exclusive |
|---|---|
| `DIRECTION.md` | Mode, absolus, classification, cible, capacité et module optionnel `DIRECTION-ATELIER`. |
| `ACTION.md` | Procédures, gates, preuves exécutables, statuts et verdicts de livraison. |
| `SAVOIR.md` | Principes de jugement, craft, styles, contexte et intégrité. |
| `BIBLIOTHEQUE.md` | Supports, grilles, scènes, objets, micro-interfaces et composants. |
| `CHANGELOG.md` | État de V1, changements futurs, pilotes optionnels et décisions de gouvernance. |

### Récapitulatif de protection

Avant de parcourir les sections détaillées, retiens ces décisions de protection :

1. **Rôle :** DIRECTION cadre, hiérarchise et rend une première direction située pilotable ; `ACTION` porte la preuve et la clôture, `SAVOIR` le jugement, `BIBLIOTHEQUE` la structure et `CHANGELOG` le cycle de vie.
2. **Absolus :** une surface identitaire doit avoir une direction perceptible ; son ancrage est déclaré comme limite en exploration et observable avant l’acceptation (absolu 2) ; aucune livraison ne se clôt sans les preuves applicables ; le mode, la décision dominante, le risque principal, la preuve minimale et la condition d’arrêt sont déclarés avant l’action (absolu 4) ; le réel et le beau restent liés.
3. **Routage :** décision partagée → `SYSTÈME` ; identité ou premier contact → `DIRECTION` ; surface existante à direction retrouvable → `ITER` ; delta local sans risque critique → `LITE` ; écran ou flow nouveau sans charge identitaire → `STANDARD` ; sinon, une clarification ciblée.
4. **Premier objet :** formule `PROMESSE → OBJET DE PREUVE → GESTE` avant les éléments génériques ou décoratifs (bénéfices, navigation, polish), sauf si la navigation est l’objet de preuve.
5. **Preuve :** `DECISION-CHANGE` reste vide jusqu’à une observation réelle ; une capture, une validation de package ou une rationale ne devient pas automatiquement une preuve d’usage, d’accessibilité, de performance ou de qualité visuelle.

Ce récapitulatif est un **résumé de protection**, pas une nouvelle source, un nouveau gate ou un second schéma. En cas de différence, les sections normatives et les propriétaires indiqués plus bas prévalent.

### Frontière de responsabilité

Les sections détaillées ci-dessous restent intégralement actives. Lorsque ce document présente une ligne ou une table de `RUN_CARD`, il s’agit d’une **vue de cadrage** utile à la classification ; `ACTION/RUN_CARD` demeure le seul schéma canonique des champs, statuts, preuves et clôtures. De la même façon, DIRECTION définit les modes et la cible visuelle, mais ne redéfinit ni les gates d’ACTION, ni les heuristiques de SAVOIR, ni la structure de BIBLIOTHEQUE, ni les statuts de gouvernance de CHANGELOG.

### Orientation interne et sortie

Pour une personne, `READING_MAP.md` est la vue dérivée lorsque le besoin est déjà identifiable ; l’agent charge par `DIRECTION/CHARGE`. `START` reste la source normative de classification ; les autres vues (`CHARGE`, `FAST-PATH`, `EXTERNAL-START`) sont des vues dérivées ou conditionnelles.

La sortie de DIRECTION vers ACTION réutilise `ACTION/HANDOFF` ; la phase de chaque champ (avant build, après observation, clôture) est celle de la table de correspondance d’`ACTION/RUN_CARD`. Pour `MODE=DIRECTION`, transmettre aussi la cible/ancre et, lors d’une clôture, les éléments de `creative_close`; ACTION renseigne `closure.direction_status`, `issue`, `verdict` et l’état selon son schéma. Si un champ ne s’applique pas, marquez `N/A-JUSTIFIED` selon ACTION ; ne créez ni statut ni verdict dans DIRECTION.

**Condition d’arrêt de lecture :** arrêtez DIRECTION lorsque mode, risque, décision, scope, contrainte déterminante, premier objet/artefact attendu, owner, prochaine preuve, limite et condition de sortie sont suffisamment explicites pour ACTION. Continuez seulement si une section peut modifier l’un de ces éléments.

### Trois contrats à ne pas mélanger

| Contrat | Question | Sortie attendue |
|---|---|---|
| `ROUTE` | Quelle décision, quel risque et quel mode ? | Mode, risque, capacité et sources à charger. |
| `TARGET` | Quelle position et quel objet faut-il construire ? | Thèse, silhouette, hiérarchie, matière, contenu, preuve, ancre, modal et parti. |
| `HANDOFF` | Que doit exécuter et vérifier ACTION ? | **Avant build** : artefact, scope, preuve attendue, limite, prochaine action et owner. **Après observation** : défaut dominant, correction ou retour recommandé. |

Ces contrats structurent le cadrage sans créer de route, de gate, de statut ou de `RUN_CARD` supplémentaires. `START` possède la classification ; `ACTION` possède la preuve et la clôture ; `SAVOIR` possède le jugement ; `BIBLIOTHEQUE` possède les structures.

### Architecture d’activation

Les modules ci-dessous ne sont pas des formulaires à remplir en parallèle. Ils sont des vues complémentaires d’un même cadrage. Une vue est chargée lorsqu’elle peut modifier la décision indiquée ; sa sortie rejoint la trace existante, puis le lecteur passe au propriétaire suivant.

| Vue | Rôle | Déclencheur | Sortie à transmettre |
|---|---|---|---|
| `START` | Classer | Démarrage de tout run ; si mode ou risque est incertain, ouvrir une clarification ou une reclassification | `MODE`, `RISK`, `DECISION`, `OWNER`, `NEXT-PROOF`, `CAPABILITY-BASIS` |
| `CREATIVE-BOOT` | Ouvrir la boucle créative | Décision visuelle ouverte | Promesse, objet de preuve, geste, `MODAL`/`PARTI`, `FABRICATION` et défaut recherché |
| `VISUAL_TARGET` | Rendre la position pilotable | Première scène ou identité à définir | Thèse, relation, ancre, composition, preuve et rendu attendu |
| `DIRECTION-ATELIER` | Approfondir une position située | Tension, geste, confiance culturelle ou exclusion pouvant modifier la scène | Moment, tension, geste, position, contre-choix et limite |
| `FIRST-OBJECT` | Rendre la première proposition jugeable | Premier rendu à produire ou comparer | Objet complet et dimensions à inspecter |
| `DOUBLE-LOOP` | Organiser l’apprentissage | Observation d’un rendu réel | Défaut dominant, correction visible, réobservation et décision |
| `HANDOFF` | Transmettre à `ACTION` | Construction, preuve ou clôture à engager | Projection complète `ACTION/HANDOFF`, sans statut ni verdict concurrent |

Une seule vue peut suffire pour un delta local. La complétude d’une vue n’est jamais un objectif autonome.

### Carte de lecture canonique et chemin en trente secondes

Classer : `DIRECTION/START`. Charger : `DIRECTION/CHARGE`, seule liste de chargement. Fabriquer : le noyau de la skill, compilé depuis les blocs « noyau » des sources. Vérifier, corriger ou clôturer : `ACTION`, jamais DIRECTION seule.

En trente secondes, nomme : **la décision à changer, le risque dominant, le mode, la capacité minimale et le premier objet que la preuve devra inspecter**. Cette vue accélère l’entrée ; elle ne remplace ni `START`, ni les contrats d’ACTION, ni le jugement situé.

Cette carte est la vue de lecture interne canonique de DIRECTION. `CHARGE`, `FAST-PATH`, `EXTERNAL-START`, la section 0 et le récapitulatif de protection sont des vues dérivées de `START` : elles ne classent pas, ne créent ni nouveau mode, ni nouveau contrat, ni nouvelle condition de sortie et ne peuvent pas contredire `START`. `READING_MAP.md` reste le guide dérivé inter-document. En cas de différence, `START`, les propriétaires de responsabilité et les contrats d’ACTION prévalent.

**Chaîne de lecture interne.** Utilise le document selon la décision à faire évoluer, dans l’ordre de l’architecture d’activation : `START` classe ; `CREATIVE-BOOT` ouvre la décision ; `VISUAL_TARGET` rend la position pilotable ; `DIRECTION-ATELIER` approfondit la direction située lorsque cette profondeur peut changer la décision ; `FIRST-OBJECT` matérialise la cible et rend la promesse jugeable ; `DOUBLE-LOOP` organise l’observation et la correction ; le `HANDOFF` remet à `ACTION` une cible, un artefact, une preuve et une limite explicites. Chaque module doit être chargé pour son gain attendu : meilleure orientation, meilleur premier objet, meilleur jugement, meilleure structure ou meilleure preuve — jamais pour augmenter la procédure.

**Périmètre.** Le système vise à aider une personne, un agent ou une équipe à produire des interfaces et frontends de haute qualité visuelle, sur le web comme sur des plateformes natives telles que Flutter, Swift, Kotlin ou équivalentes. Il vise un premier rendu spécifique, composé, crédible et résolu plutôt qu’un résultat générique ou décoratif. Il vise à augmenter la probabilité d’un travail de niveau expert en rendant explicites des décisions que les meilleures équipes prennent souvent implicitement ; cette efficacité reste `NOT-VERIFIED` (`CHANGELOG`) et s’éprouve par les pilotes. Il ne remplace ni la compétence, ni le jugement situé, ni la revue humaine, et ne garantit ni l’excellence universelle, ni la réussite d’une tâche, ni l’adéquation à tous les publics. Ces propriétés dépendent du contenu réel, du contexte, de la preuve et du jugement situé. Les exemples et runtimes de référence sont souvent web, mais les décisions de hiérarchie, composition, typographie, matière, états et interaction sont portables. L’implémentation traduit ces décisions dans les idiomes réels de la plateforme ; elle ne copie pas mécaniquement des conventions web.

**Capacité positive de DIRECTION.** DIRECTION ne sert pas seulement à éviter une proposition générique : elle vise à augmenter la qualité du cadrage, de la position, de la première scène et de la boucle créative. Elle transforme un brief en relation perceptible entre produit, public, contenu, geste, matière et contrainte ; elle peut requalifier une demande lorsque cela améliore la décision, sans se substituer aux owners de preuve, de structure ou de clôture.

**Priorité.** `P0` porte la direction et le craft visuel ; `P1` protège compréhension, usage et accessibilité ; `P2` traduit la direction dans la plateforme et le runtime réels ; `P3` couvre robustesse, performance, compatibilité et maintien lorsque le risque le requiert. P1 est un plancher non négociable, mais P1–P3 ne doivent jamais servir à justifier une interface générique ou à effacer la signature visuelle de P0. Cette hiérarchie ne permet jamais de retarder un risque critique de tâche, de santé, de sécurité, de confidentialité, de permission ou d’accessibilité au profit du craft : dans ce cas, la protection critique devient la prochaine décision et la prochaine preuve.

**Défaut de qualité visuelle.** Pour toute surface visuelle, identitaire ou UI dont le rendu est un objet direct du run, la première proposition doit être **dirigée, distinctive, construite et polie par défaut**. Elle doit montrer une hiérarchie maîtrisée, une typographie intentionnelle, une composition résolue, une palette cohérente, des assets et composants choisis ou conçus pour le produit, ainsi que les états visuels pertinents lorsque le risque le requiert. Un wireframe générique, une collection de composants sans scène ou un habillage décoratif ne constituent pas une première proposition suffisante lorsque la décision visuelle est ouverte.

Ce défaut élève l’ambition de la première proposition ; il ne crée ni score esthétique, ni style obligatoire, ni garantie de résultat, ni preuve automatique. La singularité reste située par le JTBD, le public, le contexte et la marque.

**Standard créatif.** Lorsque la qualité perceptuelle est une décision du run, le cadrage active aussi la responsabilité de `SAVOIR/CRAFT/CFT-00`. La première proposition vise une présence identifiable, un point de vue, une composition maîtrisée, une culture visuelle transformée, une spécificité liée au produit, une expression cohérente, une désirabilité située et une résolution proportionnée à l’ambition. Ces dimensions sont jugées par des observations et des décisions de craft ; elles ne deviennent ni score, ni statut, ni verdict automatique. Une surface peut être conforme, utilisable et techniquement robuste tout en restant trop générique ou insuffisamment résolue : cet écart doit déclencher une correction de direction ou de polish, pas être compensé par la preuve d’un autre axe. L’usage, l’accessibilité, la robustesse et la faisabilité restent des protections actives ; elles ne doivent pas être sacrifiées au rendu, et le rendu ne doit pas être utilisé pour masquer leur absence de preuve. Pour un correctif strictement local, `LITE` ou `ITER` conservent la structure existante sauf si la décision visuelle elle-même est ouverte.

`CREATIVE-BOOT`, `VISUAL_TARGET` et `DIRECTION-ATELIER` ne demandent pas trois descriptions concurrentes. Lorsque la même information apparaît sous plusieurs noms, conserve-la dans la vue qui la rend décisionnelle et renvoie les autres vues à cette sortie : la promesse devient la thèse si elle est transformée en position, le parti devient une exclusion s’il gouverne la scène, et l’ancre devient une preuve de calibration si elle modifie la composition. Les champs non transformés ne sont pas recopiés.

**Statut de gouvernance.** Une source, un claim daté, un retour externe ou un asset reste local au run tant qu’il ne modifie pas durablement une règle partagée. Seule cette promotion justifie une décision dans `CHANGELOG.md`.

### Comment lire les taxonomies

Ces repères ne fusionnent pas les taxonomies. **Le risque dominant** détermine la protection à préserver et aide à choisir le mode ; **le mode** détermine la proportion de trace et de preuve ; **P0–P3** décrivent l’ordre de protection à examiner dans ce contexte ; **V/U/A/T** sont les axes de questions et de preuve tenus par `ACTION`. Si deux repères semblent entrer en conflit, ne baisse pas la protection : pose une clarification ciblée ou retiens le risque dominant.

### Légende

| Tag | Sens |
|---|---|
| `[ABSOLU]` | Contrat transversal de DIRECTION. |
| `[FORCÉ]` | Chargement ou action déclenché par un signal objectif. |
| `[REQUIS PAR LE MODULE]` | Obligation définie par ACTION, SAVOIR ou BIBLIOTHEQUE dans son propre périmètre. |
| `[RECOMMANDÉ]` | Défaut solide, infléchissable si l’exception est nommée. |
| `[À ADAPTER]` | Point de départ contextuel, jamais validation automatique. |
| `[VEILLE]` | Information datée ou évolutive à vérifier avant de la transformer en règle. |

Légende commune à DIRECTION et SAVOIR pour les seuls tags partagés : `[REQUIS PAR LE MODULE]`, `[À ADAPTER]` et `[VEILLE]`, au même sens. SAVOIR tient sa propre table (« Niveaux d’autorité ») pour ses autres tags ; `[RECOMMANDÉ]` n’y est pas employé.

Les valeurs chiffrées sont des points de départ. **La vérification exigée ne l’est pas.** Une heuristique de craft peut guider une décision ; elle ne devient pas une loi universelle sans portée, source et preuve appropriées. De même, « premium », « beau », « moderne », « innovant » ou « haut de gamme » ne sont jamais des décisions suffisantes : ils doivent être traduits en relation visible, contenu, geste, contrainte ou preuve. Une réponse concise reste valide si elle est située ; la longueur de la trace ne compense jamais son absence de conséquence.

**Repères de vocabulaire.** *Craft* désigne la qualité de fabrication et de résolution du design ; *JTBD* signifie la tâche que la personne cherche réellement à accomplir ; *scope* désigne le périmètre de la preuve ; *grounding* désigne l’ancrage factuel ou contextuel susceptible de modifier la décision ; `BASIS` désigne la base déclarée d’un claim ou d’une capacité.

---
