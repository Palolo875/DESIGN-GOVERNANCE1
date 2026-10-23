# Direction — standard

Le standard de qualité visuelle, les cinq règles essentielles et les invariants de jugement.

<!-- origine:DIRECTION.md -->
## DIRECTION/STANDARD — les cinq règles absolues

<!-- noyau:début ABSOLUS -->
**Les cinq absolus.** Ils valent pour tout run, quel que soit le mode ; leur texte complet est servi par `DIRECTION/STANDARD`.

1. **Direction visible.** Une surface identitaire conforme mais sans direction perceptible est un échec de livraison ; la conformité est un plancher, pas un résultat. Un écart de direction se corrige ; il ne se compense pas par la preuve d’un autre axe.
2. **Ancrage.** Aucune direction identitaire n’est acceptée sans ancre ; sans elle, elle reste `EXPLORATORY`, avec sa limite.
3. **Preuves.** Aucune livraison sans les preuves applicables au mode ; un gate non applicable est `N/A-JUSTIFIED`, un gate non vérifiable `NOT-VERIFIED`, jamais `PASS`.
4. **Déclarer avant d’agir.** Mode, décision dominante, risque principal, preuve minimale et condition d’arrêt, en une ligne `RUN` (`DIRECTION/START`). Un moyen ou une preuve qui manque ne fait jamais baisser le mode en silence : la propriété concernée devient `NOT-VERIFIED`.
5. **Réel et beau ensemble.** Le produit, la tâche, le contenu réel et les contraintes sont la matière de la direction : pas de faux réalisme pour faire joli ; en contexte à enjeu, clarté, prévention d’erreur et robustesse priment sur le spectaculaire.
<!-- noyau:fin ABSOLUS -->

Il y en a cinq. Elles sont les seuls **absolus transversaux de DIRECTION**. Une obligation spécialisée reste la propriété du module qui la définit ; `DIRECTION` la route sans lui voler son statut ni dupliquer sa procédure.

Une règle supplémentaire doit remplacer une règle existante. Une constitution où tout est absolu ne priorise rien. Ces cinq contrats existent pour préserver le craft, l’usage et la direction quand le coût de production monte.

### [ABSOLU 1 — STANDARD VISUEL] Une surface identitaire conforme mais sans direction perceptible est un échec de livraison.

La conformité — contraste, états, focus, performance — est un plancher, non un résultat. Une **surface identitaire** est une surface dont l’échec principal serait une mauvaise perception du positionnement, de la marque ou de la promesse avant même l’échec d’une tâche opérationnelle : hero, landing, above-the-fold, accueil identitaire, page de marque ou surface équivalente.

Si l’échec principal concerne une action, un état ou une compréhension opérationnelle, utilise le mode proportionné correspondant, sauf signal identitaire explicite.

Avant la livraison d’une surface identitaire, trois décisions doivent être présentes et nommables :

1. une stratégie matérielle perceptible et justifiée ;
2. une typographie déclarée et appropriée, avec une raison ;
3. une composition intentionnelle.

Une stratégie matérielle peut être une image, une lumière, une donnée, une illustration, un support imprimé, une surface, un cadrage, un traitement typographique, une planéité assumée ou l’absence intentionnelle d’asset. Elle ne sert jamais de signal générique d’humanité ou de « premium ».

La composition peut prendre la forme d’une tension, d’un déséquilibre assumé, d’un vide calibré, d’un débord, d’un rythme, d’un ancrage ou d’une retenue. Elle ne se réduit pas à des sections centrées de largeur identique empilées par réflexe.

Si ce standard entre en conflit avec une protection critique de compréhension, d’usage, de sécurité ou d’accessibilité, **la protection critique prévaut**. Résous alors la direction par la hiérarchie, la typographie, le contenu, la structure et le détail, sans effet nuisible à la tâche. L’ABSOLU 5 fournit le cadre de coordination entre réel et beauté ; il ne remplace pas le plancher P1 ni les protections spécialisées d’ACTION.

### [ABSOLU 2 — ANCRAGE OBSERVABLE] Ne fais jamais accepter une direction identitaire calibrée uniquement de mémoire.

<!-- noyau:début ANCRE -->
<!-- concept:ANC-01 -->
**Explorer, accepter, diffuser.** Une première proposition peut commencer sans ancre, quelle que soit sa destination : elle déclare cette limite et reste `EXPLORATORY` ; une hypothèse générée (`ANCHOR-GENERATED`) aide alors à comparer. **Accepter** une direction identitaire exige une ancre : une direction acceptée n’a jamais d’ancres vides. Pour un produit réel, l’ancre est observée ou fournie (`ANCHOR-OBSERVED`, `ANCHOR-PROVIDED`), pertinente et inspectée, avec les autres preuves applicables ; elle peut venir du projet lui-même (identité existante, produit, photographies, interface actuelle). Pour une démonstration ou un modèle, une hypothèse générée peut servir d’ancre à l’acceptation, avec sa limite déclarée ; en enjeu identitaire élevé, elle exige une réserve explicite ou une calibration par ancre observée, fournie ou contrainte réelle. Sans l’ancre requise, la direction reste `EXPLORATORY` : elle peut être montrée ou partagée comme proposition, avec sa limite. `FAIL-ASSUMED` (`ACTION/OVERRIDE`) ne vaut que pour un échec connu et observé, jamais pour une ancre absente, qui reste `NOT-VERIFIED` ; le verdict reste non accepté.
<!-- noyau:fin ANCRE -->

Les voies d’ancrage sont les suivantes ; une ancre est datée et inspectable :

| Voie | Fonction | Sortie minimale |
|---|---|---|
| **ANCHOR-GENERATED — hypothèse visuelle générée** | Rendre une possibilité visible et comparable. | Cible ou hypothèse retenue, attributs observés, contre-indications et limites de transfert. |
| **ANCHOR-OBSERVED — références observées** | Calibrer un principe, une résolution ou un niveau de craft, notamment par recherche Web ou documentaire. | Une ou plusieurs références réellement ouvertes selon le risque de calibration, source/provenance, date, portée, attributs retenus/rejetés, rôle de l’ancrage et comparaison. Deux ou trois références peuvent être utiles, mais ne constituent pas un quota universel. |
| **ANCHOR-PROVIDED — ancre fournie** | Exprimer une intention, un contexte ou un actif réel. | Annotation des attributs utilisables, limites et écarts à éviter. |

`ANCHOR-GENERATED` est une hypothèse visuelle comparable, non une calibration externe suffisante par défaut. Lorsque l’enjeu identitaire est élevé, accompagne-la d’une référence observée, d’une contrainte réelle ou d’une réserve explicite sur l’absence de calibration externe.

Une référence humaine ou produite est un calibrateur, non un modèle à reproduire. Elle ne prouve ni l’efficacité produit, ni le droit de réemploi, ni l’adéquation à tous les publics. Une source Web doit être réellement ouverte et réinspectable ; un extrait de résultat de recherche, une image isolée ou une tendance non datée ne suffit pas à constituer une ancre de direction.

Sans ancre utile, les axes visuels concernés restent `NOT-VERIFIED` et la direction ne peut pas être acceptée ; elle reste `EXPLORATORY` avec sa limite. Une ancre absente n’est pas un échec connu : `FAIL-ASSUMED` ne s’y applique pas (`ACTION/OVERRIDE`). Le validateur de `RUN_CARD` refuse une direction acceptée sans ancre, mais ne connaît pas la destination : l’exigence d’une ancre observée ou fournie pour un produit réel relève de la revue d’acceptation.

### [ABSOLU 3 — GATE] Aucune livraison sans les preuves applicables au mode.

Les gates et leurs conditions d’exécution sont définis par `ACTION`. DIRECTION ne fait ici que router le besoin : une surface `DIRECTION` doit suivre la route de preuve appropriée, tandis que les autres modes appliquent les contrôles proportionnés à leur risque. La procédure, les critères d’acceptation et la clôture restent dans `ACTION`.

Un gate non applicable est `N/A-JUSTIFIED`. Un gate non vérifiable est `NOT-VERIFIED`, jamais `PASS` par défaut.

Une alternative ou un retrait n’est requis que si un choix plausible pourrait modifier la décision. En `DIRECTION`, l’alternative située suit `DIRECTION/DIVERGENCE` (déclenchement), `SAVOIR/CRAFT/CFT-02` (leviers) et `ACTION/PIPELINE-DIRECTION` (matérialisation, trace et comparaison) ; une alternative qui ne peut rien changer n’est pas produite, et sa non-production est justifiée.

Le verdict nomme le risque ou conflit le plus important. **Aucun quota de retraits, de variantes ou de différences n’est imposé.**

Le seul override est le `FAIL-ASSUMED` journalisé dans `ACTION`. Il ne devient jamais un `PASS`, ne contourne aucun risque critique et ne masque jamais une preuve absente.

### [ABSOLU 4 — MODE, PREUVE ET BUDGET] Déclare la route et la prochaine preuve avant d’exécuter.

Avant toute action qui engage un artefact, une preuve, un état, une diffusion ou une persistance, déclare le mode, la décision dominante, le risque principal, la preuve minimale et la condition d’arrêt. Le budget est une suite de jalons, pas un nombre d’appels d’outil. L’intake nécessaire au classement reste possible avant cette déclaration. Lorsque le coût de production est déterminant, déclare aussi la contrainte de temps, de dépendance, de maintenance, de performance ou de capacité.

| Jalon | Question d’arrêt |
|---|---|
| Cadrage | Le public, la tâche, la contrainte et la décision sont-ils assez clairs pour choisir ? |
| Direction | La position retenue et l’alternative considérée sont-elles comparables au niveau nécessaire ? |
| Ancrage | L’ancre est-elle utile et ses limites déclarées ? |
| Build | L’artefact permet-il d’observer la décision ? |
| Vérification | La preuve dominante est-elle obtenue, ou son absence est-elle explicitement statuée ? |
| Clôture | Le verdict, le risque restant et la prochaine action sont-ils persistants ? |

Ne choisis ni `LITE` pour éviter l’effort, ni `DIRECTION` pour paraître complet. Si une preuve est indisponible, le mode ne baisse pas silencieusement : l’axe ou la propriété concernée devient `NOT-VERIFIED`, puis l’issue ou le verdict est déterminé par `ACTION`, par exemple `EXPLORATORY`, `RETURNED` ou `ESCALATED` ; `FAIL-ASSUMED` ne vaut que pour un échec connu (`ACTION/OVERRIDE`). Une contrainte d’outil, de temps ou de compétence peut modifier la preuve disponible ; elle ne transforme pas une qualité non observée en qualité acquise.

### [ABSOLU 5 — RÉEL ET BEAU ENSEMBLE] Cadre le produit, le JTBD, les preuves et les contraintes pour produire une beauté pertinente.

Utilise du contenu réel et une microcopie honnête. Quand l’information manque, pose la question utile, déclare l’hypothèse avec son niveau de confiance ou marque l’artefact comme exploratoire. N’invente pas un faux réalisme pour faire joli. Le réel n’est pas une étape qui bride la création : le produit, le public, la tâche, la donnée et les contraintes sont la matière première d’une direction visuelle pertinente.

Un contenu synthétique est autorisé en exploration lorsqu’il conserve les propriétés qui peuvent changer la décision — longueur, densité, langue, structure, ambiguïté, statut, permission ou extrême de données — et qu’il est marqué comme hypothèse. Un placeholder générique n’est pas acceptable s’il masque précisément ces propriétés.

Une icône est fonctionnelle lorsqu’elle sert une action ou une information dans un système cohérent ; elle devient un remplissage lorsqu’elle n’ajoute aucun sens.

En santé, finance, légal, secteur public ou tout contexte à enjeu, la clarté, la prévention d’erreur, la confirmation, la traçabilité et la robustesse priment sur l’esthétique spectaculaire. Une information essentielle ne dépend jamais de la couleur seule.

**Cadre d’accessibilité web.** Lorsque la conformité web est dans le périmètre, applique le référentiel et la version retenus par la source propriétaire de preuve et de contexte, puis vérifie les critères applicables au contexte réel. Une référence externe évolutive reste une `[VEILLE]` tant qu’elle n’est pas adoptée par le propriétaire compétent ; elle ne devient pas automatiquement une obligation de livraison. Un référentiel de conformité ne valide ni la direction visuelle, ni l’utilisabilité globale, ni l’adéquation du positionnement.

Lorsque le risque dominant concerne une population, une accessibilité réelle, une tâche critique ou un coût d’erreur élevé, DIRECTION signale ce risque ; le choix de méthode — observation avec des personnes représentatives, revue experte ou contrôle technique — relève d’`ACTION/GATE-B` et de `SAVOIR/CONTEXT`, avec owner et prochaine preuve. Une méthode non utilisateur ne soutient pas un claim d’usage.

Une capture, une lecture perceptuelle ou une comparaison peut établir une observation de caractère visuel ou de compréhensibilité présumée. Elle ne constitue une preuve d’utilisabilité que si un utilisateur, un objectif, une tâche, un contexte et un résultat observé sont définis.

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

### Comment lire les repères

Ces repères ne fusionnent pas les taxonomies. **Le risque dominant** détermine la protection à préserver et aide à choisir le mode ; **le mode** détermine la proportion de trace et de preuve ; **P0–P3** décrivent l’ordre de protection à examiner dans ce contexte ; **V/U/A/T** sont les axes de questions et de preuve tenus par `ACTION`. Si deux repères semblent entrer en conflit, ne baisse pas la protection : pose une clarification ciblée ou retiens le risque dominant.

### Invariants de jugement

#### Convergence de genre ≠ slop

Une structure conventionnelle peut être la bonne réponse. Ne juge pas la ressemblance du squelette seul : juge le contenu, la microcopie, les états, les données, la résolution des détails et la spécificité du produit.

Si les détails sont interchangeables, cherche d’abord ce qui peut devenir spécifique à partir du produit réel — contenu, donnée, relation, interaction ou hiérarchie. N’ajoute un signal distinctif que s’il améliore la tâche, la compréhension, la preuve ou le positionnement.

#### PASS technique ≠ direction tenue

Le gate A garantit l’absence de certaines fautes. Il ne prouve ni la direction, ni le goût, ni l’adéquation au produit. Sur une surface identitaire, l’ancre, la cible, la capture et les écarts nommés restent nécessaires.

De même, une capture, une lecture perceptuelle, une conformité WCAG ou un avis externe ne prouve pas seul l’utilisabilité globale. Lorsque U est dominant, la preuve doit relier un utilisateur, un objectif, une tâche, un contexte et un résultat observé.

#### Les listes ne sont pas un canon

Références, designers, matières, outils et registres sont des amorces de jugement. Une liste appliquée mécaniquement recrée la convergence qu’elle cherchait à empêcher.

---
