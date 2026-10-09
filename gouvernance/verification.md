# Gouvernance — vérification

Contrats de décision et leur preuve, vérification en contexte, dérogation et péremption.

<!-- origine:ACTION.md -->
## ACTION/STRUCTURED-PROOF — contrats de décision et leur preuve

Ces artefacts rendent les décisions inspectables. Chacun n’est dû que si son déclencheur est actif ; sinon il est `N/A-JUSTIFIED`, avec sa raison. Zéro contrat est valide lorsqu’aucun déclencheur n’est actif : aucun fichier `production_contracts` n’est alors produit ; un fichier présent en porte au moins un.

| Contrat | Déclencheur |
|---|---|
| Carte de hiérarchie | `STANDARD` ou `DIRECTION` ; tout run dont la hiérarchie peut changer la décision |
| Preuve U structurée | U dominant |
| Partition typographique | Famille, registre, langue, données ou hiérarchie typographique pouvant changer la décision |
| Fiche d’asset directeur | Asset ou absence d’asset portant une décision perceptible (`DIRECTION/VISUAL_TARGET`) |
| Contrat de composant partagé | Pattern réutilisable, composant critique ou partagé : défini dans `BIBLIOTHEQUE/COMPONENTS` |
| Motion ou scène spatiale | Motion non triviale, animation interactive, scène 3D |
| `CREATIVE_DIRECTION_SET` | `DIRECTION` à décision ouverte avec alternative plausible |
| `UI_UX_REALITY_PACK` | Surface UI/UX nouvelle ou substantiellement modifiée (`ACTION/UI-UX-REALITY`) |
| `EVALUATION_CASE` | Pilote ou série de runs (`ACTION/CLOSE-EXIT-CHECK`, mesure expérimentale) |

**Règle de phase.** Les lignes de preuve sont marquées « après observation ». Avant build, elles restent vides ou `NOT-VERIFIED`, jamais préremplies par l’attendu. Après build, la cible est conservée et l’observation s’ajoute à côté.

### Carte de hiérarchie

- **Public prioritaire :**
- **Contexte et tâche dominante :**
- **Contenu primaire :**
- **Action critique :**
- **Contenu secondaire :**
- **Contenu à la demande :**
- **Risque de mauvaise lecture :**
- **Signal visuel prévu :**
- **Preuve U attendue :**

Lorsque U est dominant, la preuve U attendue peut être structurée ainsi :

```text
USER / PROFILE
TASK
CONTEXT
SUCCESS-CRITERION
OBSERVATION / MEASURE — après observation
SATISFACTION-OR-QUALITATIVE-RETURN — après observation
LIMIT — après observation
NEXT-PROOF — après observation
```

Une capture ou une inspection experte peut formuler un risque U ; elle ne doit pas être nommée test d’utilisabilité si aucune tâche représentative n’a été exécutée avec un utilisateur ou un profil concerné.

### Partition typographique

La partition est requise lorsque famille, registre, langue, données ou hiérarchie typographique peuvent changer la décision ; licence, glyphes nécessaires et coût de chargement sont vérifiés selon `SAVOIR/TYPE`. Sinon, le système existant et la raison de sa conservation suffisent.

| Rôle | Fonction | Famille / registre | Mesure / interligne | Poids / axe | Contextes | Fallback | Justification |
|---|---|---|---|---|---|---|---|
| Fonctionnel | Corps, lecture longue |  |  |  |  |  |  |
| Éditorial | Titre, rythme, angle |  |  |  |  |  |  |
| Microcopie | Labels, métadonnées, actions |  |  |  |  |  |  |
| Donnée | Chiffres, tableaux, comparaisons |  |  |  |  |  |  |
| Signature | Usage expressif limité, si nécessaire |  |  |  |  |  |  |

La partition vérifie aussi reflow, zoom et ajustements d’espacement utilisateur : aucun rôle critique ne doit être tronqué, recouvert ou rendu illisible lorsque ces conditions sont dans le périmètre.

### Fiche d’asset directeur

- **ID et rôle dans la promesse :**
- **Route de production et statut :** `CODE-NATIVE`, `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` ou `HYBRIDE` ; image, illustration, SVG, vidéo, Rive, 3D ou absence intentionnelle.
- **Raison et alternative refusée :** quelle relation devient plus lisible, crédible ou singulière avec cette route ?
- **Source, disponibilité et droits :** locator et version du fichier, pack ou bibliothèque retenus ; moyen réellement accessible et constat qui l’établit ; licence documentée, autorisation requise ou inconnu. Une ressource citée n’est pas présumée connectée.
- **Provenance et transformations :** origine, créateur, génération ou édition connue.
- **Usage et intégration :** informatif, décoratif ou mixte ; relation au type, cadrage, grade, masque, composition ou donnée ; modification précise à effectuer dans l’artefact et effet attendu ; alt, description longue ou justification décorative.
- **Desktop et mobile :** ratio, crop, focal point, zone sûre, suppression ou alternative.
- **Format, poids cible, fallback, mouvement et reduced motion :**
- **Preuve V/U/A/T (après observation) et contre-indication :** observation capable de confirmer, remplacer ou retirer la ressource ; scope, limite et réexamen après changement du fichier, du contenu voisin, du support ou des droits.

La fiche rapproche les moyens et l’intervention dans la trace existante ; elle n’ajoute aucun champ RUN_CARD. Pour un composant, rattache ces informations au contrat existant de `BIBLIOTHEQUE/COMPONENTS` ; le comportement fiable de la primitive reste distinct de la contribution expressive de son habillage.

<!-- concept:HON-08 -->
La provenance informe l’origine ; elle ne constitue pas une autorisation de réemploi. Un droit inconnu (`rights_status` : `unknown`) interdit `ACCEPTED` ; `ACCEPTED-WITH-RESERVATION` reste possible avec une réserve structurée dont le scope couvre les droits et dont la condition de sortie est leur clearance, et la diffusion attend cette clearance. Un droit non autorisé déclenche `RETURNED`, `ESCALATED` ou le statut prévu par le contexte avant diffusion. La machine ne contrôle cette exclusion que pour une `RUN_CARD` `DIRECTION`, où `artifact.rights_status` est requis ; dans les autres modes, comme pour la réserve sur les droits, le contrôle reste à la trace.

### Contrat de composant et baseline

Pour un nouveau pattern réutilisable, un composant critique ou un composant partagé, le contrat de structure est défini par `BIBLIOTHEQUE/COMPONENTS` (contrat de composant partagé). ACTION en garde la baseline comme preuve, la migration et le verdict.

Une baseline visuelle est une image versionnée d’un état réel. Elle signale un écart ; elle ne produit pas automatiquement un `PASS`. Dans un paquet SYSTÈME, la baseline de non-régression est `system_package.non_regression.baseline` : locator, version et état.

Une différence est une régression seulement si elle s’écarte de l’intention, du comportement attendu ou du contrat de compatibilité. Une différence intentionnelle doit être reliée à une décision et à une preuve ; elle ne doit pas être supprimée comme régression visuelle par défaut.

Toute différence est revue contre l’intention, l’usage, l’accessibilité et le risque de régression.

### Contrat de motion ou scène spatiale

Toute motion non triviale, animation interactive ou scène 3D porte : rôle utilisateur ou narratif, état initial, déclencheurs, transitions, interruptions, clavier/tactile, reduced motion, fallback statique, performance, contenu alternatif, capture de référence et contre-indication.

Un effet qui ne produit ni feedback, ni information, ni relation spatiale ni décision de direction est candidat à la suppression.

---

<!-- origine:ACTION.md -->
## ACTION/GATE-B — jugement contextualisé et risques

Gate B compare, observe et explique les risques restants. Il ne produit pas une moyenne décorative.

### B1 — Comparaison relationnelle

En `DIRECTION`, compare le build à l’ancre utile sur les axes réellement concernés. En `STANDARD`, utilise une ancre seulement lorsqu’une direction locale, une matière, une composition ou une comparaison perceptuelle le justifie.

Pose des questions relationnelles : quel résultat conduit mieux à l’action critique, rend le rythme plus lisible, porte mieux l’intention ou maintient mieux la singularité du produit ?

Une différence significative sur un axe dominant déclenche une correction, un écart assumé ou une justification de non-transfert. Aucun nombre fixe de comparaisons ne constitue une condition de `PASS`.

### B1b — Discrimination sur capture, requise dans son scope

`B1b` est **requis par module** sur toute surface `DIRECTION` qui accepte (`ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`) avec l’axe V en `PASS` ou `PASS-WITH-RESERVATION` : un V positif n’y est pas accordé sans une décision principale confrontée à une variante, ou sans l’un des deux motifs `N/A-JUSTIFIED` admis ci-dessous. Avant la clôture, il est déclenché dès que le risque V/craft est dominant dans la ligne de run ou que le verdict V visé repose sur une intention, une composition, une matière ou un traitement qui n’a pas encore été confronté à une variante. Le déclencheur porte sur le risque, la décision et le verdict déclarés ; il ne dépend pas de l’affirmation qu’une comparaison « ne changerait rien ».

La preuve minimale est une paire de captures réelles : une capture initiale, puis une capture après l’édition réversible d’une seule décision principale. La variable doit être observable : masse, vide, silhouette, lumière, densité, cohérence de rayon, définition d’état, crop, vocabulaire, preuve, couleur ou action.

#### Atelier d’édition — opération observable

<!-- noyau:début BOUCLE-ATELIER -->
Dans le scope de B1b (surface `DIRECTION` qui accepte avec l’axe V positif, en trace complète : `ACTION/GATE-B/B1b`), cet atelier est requis, sauf deux motifs `N/A-JUSTIFIED` : aucune décision principale éditable, ou une paire équivalente encore valide qui couvre la même décision. Hors de ce scope, sur une surface `DIRECTION` en trace légère, fais-en au moins un tour (lecture légère, édition, nouvelle capture comparée) ; la paire n’est pas exigée en trace.

Après la première capture, fais une lecture légère en ignorant le texte explicatif et nomme en une phrase la catégorie, la marque et le niveau de preuve que la surface semble raconter. Nomme ensuite la décision principale à mettre à l’épreuve. Édite-la par **retrait, réduction ou transformation** ; une décision peut coordonner plusieurs diffs, mais l’unité de compte n’est pas le nombre de changements. N’ajoute rien pour compenser.

Conserve et compare la capture suivante. La trace nomme le changement, sa direction, son effet et la décision qu’il confirme, modifie ou abandonne. Garder l’original lorsqu’il résout mieux la décision est un résultat valide : la variante a alors confirmé une décision par comparaison plutôt que par déclaration.
<!-- noyau:fin BOUCLE-ATELIER -->

`N/A-JUSTIFIED` n’est recevable que si aucune décision principale éditable n’existe dans le périmètre, ou si une paire équivalente, toujours valide après le dernier changement substantiel, couvre déjà exactement la même décision. La justification lie l’artefact concerné, l’owner et la prochaine preuve. Une thèse encore incertaine, un élément producteur introuvable ou une paire qui n’autorise aucune conclusion maintiennent le run en `EXPLORATORY` ; ils ne produisent pas un `PASS` indirect.

Dans une `RUN_CARD`, B1b est `closure.b1b`. Statut `DONE` : `pair` avec `before_locator` et `after_locator` (deux captures distinctes), `decision` et `outcome` (`confirmed`, `modified` ou `abandoned` ; `modified` correspond à `CHANGED` de `decision_change`). Statut `N/A-JUSTIFIED` : `reason` prend l’une des deux seules valeurs admises, `no_editable_decision` ou `equivalent_pair_valid` (avec `pair_ref`), plus `covered_decision`, `owner` et `next_proof`. Le validateur exige `closure.b1b` pour une surface `DIRECTION` acceptée avec V en `PASS` ou `PASS-WITH-RESERVATION` ; il ne vérifie pas que la décision couverte par une paire équivalente est bien la même.

B1b n’est ni un sixième absolu, ni un score esthétique, ni un quota universel. Hors de son scope, il ne s’applique pas. Dans son scope, il ne peut être omis sans la sortie matérielle ci-dessus.

Si l’équipe accepte consciemment l’écart narratif entre la thèse déclarée et le récit implicite de la capture, ne crée pas une nouvelle `ISSUE`. Utilise le statut de direction `HELD-WITH-ACCEPTED-DIFFERENCE` et, lorsque le périmètre permet la clôture, le verdict global `ACCEPTED-WITH-RESERVATION`. La trace doit nommer : `NARRATIVE-DIFFERENCE`, `REASON`, `PRODUCT-OR-PUBLIC-CONSTRAINT`, `OWNER`, `NEXT-PROOF` et `EXIT-CONDITION`. Cette issue n’est acceptable que si l’écart est explicite, assumé, compatible avec U/A/T et révisable ; elle ne convertit pas une preuve manquante en acceptation.

En l’absence de regard indépendant, déclarer cette limite selon B3. Une B1b menée par l’auteur du rendu est une **auto-comparaison** : elle peut soutenir une correction de craft, mais ne satisfait jamais un claim de revue indépendante. Une décision identitaire importante qui requiert un contrepoint externe reste avec réserve ou prochaine preuve tant que ce regard n’existe pas.

### B2 — Familles de preuve

Ajoute une preuve de contexte lorsque le risque produit est dominant : source de l’hypothèse, niveau de confiance, coût d’erreur, owner et prochaine preuve. Une direction peut être visuellement tenue et néanmoins répondre au mauvais problème ; ce cas doit rester visible dans U et dans le risque restant.

| Famille | Axes | Preuves privilégiées | Sortie principale |
|---|---|---|---|
| Caractère et perception | Point de vue, hiérarchie, typo/contenu, craft/états, singularité/retenue. | Capture, paires, détail, regard externe. | V |
| Compréhension et produit | UX, architecture, action critique et contenu. | Carte de hiérarchie, scénario, états, test ou retour de tâche. | U |
| Système et robustesse | Couleur, accessibilité, responsive, dark, performance et motion. | Tokens, inspection, tests, capture responsive. | A/T |
| Gouvernance | Best-fit, limites, délégation et arbitrages. | Journal, recherche, compromis, escalade. | Réserve ou prochaine action |

Chaque axe jugé porte une observation factuelle. Une note sur cinq peut localiser un risque, mais aucune note globale ne remplace V/U/A/T. Une note sans observation est invalide.

### B3 — Regard externe

Un regard humain ou un autre évaluateur peut réduire l’auto-préférence. Une seconde session du même auteur est une auto-comparaison différée : elle n’est jamais un regard externe, indépendant ou aveugle. Documente la source, l’expertise ou le profil, l’artefact regardé et la limite du jugement. Une B1b exécutée par le même auteur est une auto-comparaison et ne doit jamais être étiquetée regard externe, indépendant ou aveugle.

Un regard externe fournit un contrepoint situé ; il ne garantit ni indépendance parfaite ni exhaustivité. Pour une décision importante, triangule selon le risque : plusieurs évaluateurs, plusieurs méthodes, ou inspection et observation utilisateur.

Si aucun regard externe n’est disponible, déclare l’absence, conserve la capture et la comparaison, et inscris la réserve ou la prochaine preuve. L’absence de regard indépendant ne devient jamais une validation implicite.

Lorsqu’un regard est présenté comme **indépendant**, **comparatif** ou **aveugle**, la trace conserve aussi :

```text
REVIEWER-ROLE
REVIEWER-RELATION — SAME-AUTHOR / INVOLVED-IN-RUN / UNINVOLVED-COLLABORATOR / EXTERNAL
RENDER-AUTHOR
CONFLICT — DECLARED / NONE-KNOWN
ARTEFACTS-REVIEWED
REVIEW-EXPOSURE — BLIND / CODE-EXPOSED / PROMPT-EXPOSED / MAPPING-EXPOSED / NOT-BLIND ; plusieurs expositions sont listées ensemble, sans être condensées en une valeur
MAPPING-TIMING — BEFORE / AFTER / NOT-APPLICABLE
LIMIT
```

Le label « indépendant » exige une relation `UNINVOLVED-COLLABORATOR` ou `EXTERNAL`, un reviewer qui n’est pas l’auteur du rendu, et aucun conflit déclaré. Sinon, le regard est nommé selon sa relation réelle.

Une revue non aveugle reste une preuve située utile si son exposition est déclarée. Elle ne reçoit pas le poids d’une passe aveugle. Une divulgation du mapping après l’avis peut enrichir la passe d’interprétation, mais ne réécrit pas le jugement initial.

### B4 — Corrections ancrées

Une correction de direction répond à un écart ou une critique observable. Retourne à la divergence, à l’ancre, à la spec ou au build lorsque l’écart dominant persiste, lorsque la preuve manque ou lorsque la correction locale dénature le produit.

Aucun nombre fixe d’itérations ne constitue une règle de qualité. Le run s’arrête lorsque la direction est tenue, l’écart est explicitement assumé, la preuve est impossible et statuée, ou le périmètre doit être reclassifié.

### B5 — Trace d’assets et statut de direction

Avant le verdict d’une surface `DIRECTION`, conserve dans la trace locale les éléments utiles : capacités vérifiées, ancre et références observées, attributs retenus/rejetés, direction, écarts, réserves et statut.

Si un asset est directeur, la trace relie aussi sa route de production, sa raison, son droit ou son incertitude, son traitement et l’observation de son intégration au rendu réel. Un asset techniquement disponible mais faible dans son crop final, hors récit, ou seulement « joli » reste un écart de direction, pas une preuve de finition.

### B6 — Format de sortie compact

Livre d’abord l’artefact ou le lien. Ensuite, expose le verdict adapté au mode : une ligne en `LITE`, quelques lignes en `ITER` ou `STANDARD`, et un bloc direction + risques en `DIRECTION`.

Les paires, logs, preuves et diffs vivent dans un artefact associé ou la `RUN_CARD`. Ne répète pas les mêmes valeurs en prose et en structure.

---

<!-- origine:ACTION.md -->
## ACTION/OVERRIDE — FAIL-ASSUMED et péremption

### FAIL-ASSUMED

Un utilisateur peut demander une diffusion limitée malgré un échec connu lorsque le risque est documenté, assigné et re-testable. Le FAIL ne devient jamais un PASS.

Journalise :

> `FAIL-ASSUMED — [gate / axe] — [mesure ou preuve] — [date] — [risque] — [périmètre de diffusion] — [owner] — [condition de re-vérification].`

Toute exception conserve également :

```text
SCOPE
IMPACT
REVIEW-DATE
NEXT-PROOF
EXIT-CONDITION
```

Dans une `RUN_CARD`, l’exception est `closure.exception` : la structure de réserve de `ACTION/CLOSE-PACKAGE` (owner, scope, impact, date de revue, prochaine preuve, condition de sortie ; la date est celle de la carte), plus `gate_axis`, `failure_evidence` — un échec présent dans `proof.observed`, jamais un `NOT-VERIFIED` requalifié —, `requested_by` et `disposition` (`NON-DIFFUSÉ`, `DIFFUSÉ-LIMITÉ`, `RETIRÉ` ou `ESCALADÉ`). Si la protection critique du run a échoué, `FAIL-ASSUMED` n’est pas disponible sur ce risque : l’issue suit l’action déclarée par la protection.

Un `FAIL-ASSUMED` ne peut pas autoriser la mise en production d’un risque de sécurité, de dommage grave, de conformité critique ou de défaillance qui rend l’action essentielle trompeuse ou dangereuse. Ces cas passent en `ESCALATED` ou restent non livrables.

Les risques d’accessibilité, de sécurité ou de conformité à fort impact sont rappelés factuellement. Un `FAIL-ASSUMED` est re-présenté à la prochaine modification du même périmètre.

### Péremption

La péremption d’un claim, d’un outil, d’une watchlist ou d’une ressource déclenche une revue lorsque le livrable en dépend. La trace conserve type de claim ou de ressource, source, version, date de vérification, portée, limite, owner, date de revue et prochaine preuve.

La péremption ne bloque pas un fix sans rapport, mais ne peut pas être silencieusement reconduite lors d’une prochaine utilisation.

Une réserve périmée conserve owner, date de revue, impact, nouvelle preuve attendue et condition de clôture.

---
