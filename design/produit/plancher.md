# Produit — plancher

Ce qui doit tenir sur tout rendu réel : contrôles applicables, contraste, inspection.

<!-- origine:ACTION.md -->
## ACTION/GATE-A — plancher objectivable

Gate A vérifie les fautes mesurables ou observables. Exécute uniquement les contrôles applicables au composant, à l’appareil et au contexte.

### Contrat de portée

Lorsque l’accessibilité ou la conformité est dans le périmètre, déclare avant le contrôle :

```text
MEDIUM — médium réel de la surface et périmètre effectivement observé ; déclare le support applicable. Pour le Web, le médium peut rester implicite seulement si le périmètre est sans ambiguïté ; pour tout autre médium, il est explicite.
SCOPE — vues, composants, états ou chemins couverts.
CONFORMANCE-TARGET — référentiel et niveau visé, adapté au médium déclaré.
SAMPLE — échantillon représentatif ou raison de l’exhaustivité.
METHOD — AUTOMATED, MANUAL, EXPERT, USER ou combinaison, adaptée au médium.
BUDGET-UNIT — unité de budget pertinente : load/INP, lancement/frame rate/mémoire, confort motion, encre/contraste ou équivalent déclaré.
COVERAGE-LIMIT — éléments hors couverture, incluant toute preuve web indisponible.
NEXT-PROOF — preuve suivante attendue.
```

Pour le web, utilise WCAG 2.2 comme base normative actuelle lorsque le projet n’impose pas un autre référentiel applicable. Pour un autre médium, déclare le référentiel applicable dans `CONFORMANCE-TARGET` : guideline de plateforme, référentiel légal, standard émergent ou critère de lisibilité pertinent. WCAG 3.0 reste une `[VEILLE]` tant que sa recommandation et son modèle de conformance ne sont pas stabilisés. Les critères de conformité ne valident ni la direction visuelle, ni l’utilisabilité globale, ni l’adéquation du positionnement.

### Familles de méthodes

| Méthode | Couvre prioritairement | Limite |
|---|---|---|
| `AUTOMATED` | Défauts détectables par outil et règles codées. | Ne couvre pas tous les problèmes d’usage, de contexte ou d’interprétation. |
| `MANUAL` | Structure, clavier, focus, états et situations que l’outil ne comprend pas. | Dépend de la méthode et de l’expertise de l’inspecteur. |
| `EXPERT` | Interprétation, risque, cohérence et problèmes contextuels. | Ne remplace pas une tâche utilisateur. |
| `USER` | Expérience réelle et difficultés de personnes concernées. | Échantillon, tâche et contexte doivent être déclarés. |

Un `PASS` décrit la preuve obtenue par la méthode, le médium et le périmètre déclarés. Il ne devient pas un `PASS` global par glissement. Ce qui n’existe pas dans le médium est `N/A-JUSTIFIED` ; ce qui le remplace est testé. Une preuve web indisponible n’est jamais simulée : elle devient `NOT-VERIFIED` avec `NEXT-PROOF`, ou est traduite en équivalent du médium.

Pour un verdict global `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, la `RUN_CARD` doit rattacher la preuve observée à une provenance minimale : `artifact_locator`, `artifact_version`, `method` et `observed_at`. Cette provenance établit où, sur quelle version, par quelle méthode et à quel moment l’observation a été obtenue ; elle ne prouve pas à elle seule la véracité de l’artefact, la qualité du design ou la réussite d’usage. Si la provenance ne peut pas être établie, le verdict reste non accepté.

### Adéquation des preuves

| Question | Preuve adaptée | Limite |
|---|---|---|
| Ratio, taille, token, régression mesurable | Script ou test exécuté. | Ne prouve pas l’intention visuelle. |
| Hiérarchie, composition, densité, matière | Capture, détail et comparaison. | Ne crée pas seul un juge indépendant. |
| Préférence, clarté, fidélité au contexte | Regard humain, expert ou utilisateur selon le risque. | N’est pas une mesure technique par défaut. |
| Utilisabilité réelle | Utilisateur représentatif, tâche représentative, observation et résultat. | Ne se déduit pas d’une capture ou d’un avis expert seul. |
| Hypothèse sans runtime ou observateur | Déclaration structurée. | Reste `NOT-VERIFIED` si la preuve est requise. |

### Contrôles applicables

| Contrôle | `PASS` si… | Retour ou réserve si… |
|---|---|---|
| Contraste | Les cas représentatifs sont calculés selon la politique WCAG 2.2 AA du projet lorsqu’elle s’applique. | Estimé à l’œil, sous seuil ou non calculé lorsque requis. |
| Sémantique et nom accessible | Interactifs et contenus essentiels ont une sémantique et un nom adaptés. | Rôle, nom, structure ou alternative absents. |
| Focus clavier | Interactifs atteignables avec focus visible et testé. | Navigation ou focus indisponible. |
| États pertinents | Interaction, sélection, contenu et erreurs sont vérifiés ; événement, conséquence et action suivante sont explicites. | État critique absent, implicite ou dépendant de la couleur seule. |
| Contenu honnête | Pas de faux contenu, lorem ou promesse non étayée présenté comme réel. | Contenu de remplissage trompeur. |
| Stabilité média | Dimensions, fallback et chargement évitent les déplacements pertinents. | Instabilité visible ou espace non réservé. |
| Motion réduite | L’alternative sans mouvement est implémentée et vérifiée préférence activée, dans le runtime déclaré. Sans motion : `N/A-JUSTIFIED`. | Motion imposée ou alternative absente ; alternative seulement dessinée ou annoncée : `NOT-VERIFIED`. |
| Cibles d’interaction | Taille adaptée au device et au contexte selon la politique du projet. | Cible trop petite sans alternative ni justification. |
| Information non chromatique | L’information essentielle ne dépend pas de la couleur seule. | Statut ou action incompréhensible sans couleur. |
| Focus non masqué | Le composant recevant le focus reste visible selon le contexte applicable. | Focus masqué par contenu ou interface auteur. |
| Mouvement de glisser | Une alternative existe lorsque l’action de glisser n’est pas essentielle. | Action impossible autrement sans justification. |
| Aide cohérente | L’aide répétée apparaît de façon cohérente lorsque le produit en fournit. | Aide déplacée ou incohérente dans le périmètre. |
| Saisie redondante | L’utilisateur ne doit pas ressaisir inutilement une information déjà fournie dans le même processus. | Répétition évitable sans raison. |
| Authentification accessible | Le processus n’impose pas une charge cognitive ou sensorielle évitable. | Mémoire, perception ou interaction imposée sans alternative. |

<!-- concept:GTA-01 -->
**Profils de surface.** Commence par les contrôles d’office du profil ; un contrôle hors profil devient applicable dès que la surface porte l’élément concerné (formulaire, glisser, motion, connexion). Ce que le médium ne porte pas est `N/A-JUSTIFIED`.

| Profil | Contrôles d’office | Selon le contenu |
|---|---|---|
| Page vitrine, éditoriale ou portfolio | Contraste, sémantique et nom accessible, focus clavier, information non chromatique, cibles d’interaction, contenu honnête, stabilité média. | États (formulaire, commande), motion réduite, mouvement de glisser, focus non masqué. |
| Application, formulaire ou flow | Tous les contrôles d’interface : contraste, sémantique, focus clavier et non masqué, états, cibles, information non chromatique, saisie redondante, aide cohérente, contenu honnête. | Authentification accessible (connexion), motion réduite, mouvement de glisser, stabilité média. |
| Scène, motion ou 3D | Motion réduite, contraste, information non chromatique, stabilité média, contenu honnête. | Focus clavier et cibles si la scène est interactive. |
| Hors Web (imprimé, affiche, écran fixe) | Contraste ou lisibilité d’encre, information non chromatique, contenu honnête. | Référentiel du médium, déclaré dans `CONFORMANCE-TARGET`. |

Les scripts et recettes sont des ressources versionnées. Une recette exécutée ne suffit pas à valider un résultat visuel, produit ou utilisateur. La recette `AUTOMATED` du paquet pour un rendu HTML est `scripts/check_render.py` (optionnelle, navigateur requis) : elle contrôle le débordement (de la page et des feuilles ouvertes), les erreurs de script, le contraste sur fond uni opaque, les candidats de nom tirés du DOM, la taille des cibles (exception d’espacement comprise), les arrêts clavier observés et leur changement de style au focus, la structure du document et le mouvement réduit, et produit la provenance minimale ci-dessus. Une opacité de groupe, une couleur non convertible, un fond en dégradé ou un texte SVG non mesuré deviennent une réserve, jamais `PASS`. Le contraste non textuel (bordures, icônes, indicateur de focus) n’est pas mesuré, et le ratio d’un texte qui passe n’est pas rapporté : une trace qui cite un ratio le mesure à part. Le candidat DOM exclut le contenu masqué ordinaire et peut utiliser les labels explicitement référencés ; sa présence ne prouve pas le nom accessible calculé et conserve une réserve. Un cas de nom non couvert conserve également une réserve. Le parcours clavier indique le périmètre actif, les candidats non atteints et la raison d’arrêt ; la borne atteinte ou une couverture inconnue conserve une réserve. Un changement de style ne prouve ni visibilité, ni contraste, ni absence de masquage du focus. Ces limites n’allègent pas les contrôles applicables du gate : approfondis la preuve si nécessaire. Options : `--widths` (largeurs, défaut 390, 768 et 1440 px), `--proof SÉLECTEUR` (objet de preuve), `--click SÉLECTEUR` (état à observer, répétable), `--captures DOSSIER` (une capture pleine page par largeur, sans écrasement), `--json CHEMIN` (résultats et provenance). Avant de mesurer, la recette fait défiler toute la page : le contenu révélé au défilement est ainsi mesuré et capturé. Par défaut, seules la page et son origine se chargent : une police ou une image hébergée ailleurs est bloquée et la mesure utilise les polices de repli ; `--allow-external` les charge, à déclarer dans la méthode de la preuve. Sans navigateur, la recette rend `NOT-VERIFIED`. Ses comportements sont testés par `scripts/test_check_render.py` ; `--require-browser` exige les tests de pages et fait échouer leur contrôle si le navigateur est indisponible.

**Résoudre un contraste non évalué.** Pour le texte SVG, relève dans l’état et aux largeurs concernés la couleur peinte (`fill` ou `stroke`), les opacités et le fond réellement placé derrière les glyphes ; la propriété CSS `color` et le fond d’un ancêtre ne suffisent pas. Calcule le rapport sur les couleurs effectives selon les seuils de cette gate et `SAVOIR/CRAFT/CFT-05`. Sur une image, un dégradé ou des formes superposées, identifie les positions les plus défavorables dans le rendu ; une capture seule ne mesure pas le rapport. Relie le relevé, le calcul, la méthode, l’artefact, l’état, le viewport et la limite dans la preuve existante. L’agent peut produire cette mesure avec un outil adapté ; si les couleurs effectives ne sont pas établies, conserve la réserve et nomme la mesure suivante. Une preuve complémentaire résout la réserve dans le run sans modifier rétroactivement le résultat de la recette.

**Couverture de la recette.** Le contraste enregistre candidats, évaluations, exclusions et textes détectés hors couverture dans `contrast_coverage`. Valeur courante, placeholder affiché, texte natif et contenu pseudo détectés mais non calculés conservent une réserve ; une absence de mesure ne devient pas une preuve de conformité. Vérifie séparément leur couleur réellement peinte, leur fond et leur état, notamment `::placeholder`, sans publier les valeurs sensibles. Un défaut calculé ailleurs conserve `RETURN`. Ces données appartiennent à la recette, pas au schéma RUN_CARD.

Avec `--proof`, `proof_observations` sépare présence, surface, opacité CSS cumulée et intersection du rectangle avec les deux axes du viewport initial. Introuvable, masqué ou transparent : `RETURN`. Une intersection insuffisante — moins de `min(40 % de la dimension, 320 px)` sur un axe — ou une découpe non évaluée conserve une réserve : la recomposition reste à juger. Un `PASS` porte uniquement sur ces observations CSS et géométriques ; pixels, occlusion et pertinence de l’objet restent à inspecter. Une ancienne mesure sans couverture ne suffit pas.
---

<!-- origine:ACTION.md -->
## ACTION/POLICIES — contraste et inspection

### Politique de contraste

Calcule le contraste selon WCAG 2.2 et le référentiel applicable lorsque ce référentiel s’applique au projet. Ne valide jamais le contraste à l’œil.

APCA peut être documenté comme mesure complémentaire de lisibilité ou d’exploration lorsque son contexte, sa version et sa limite sont connus. APCA ne remplace pas un critère WCAG applicable et ne crée pas seul un verdict réglementaire.

Les seuils, outils, projections réglementaires et sources évolutives sont qualifiés dans `SAVOIR/TOOLS` et la trace locale du run. ACTION porte la politique de livraison ; un fait ne mérite une décision de gouvernance que lorsqu’il devient une règle partagée.

### Inspection et ressources techniques

Une inspection externe peut compléter le jugement sur l’accessibilité, la régression visuelle, les tokens et les motifs. Choisis l’outil selon l’environnement, sa documentation, sa version et son owner. Une commande, un package ou une intégration cités dans une ressource ne sont jamais exécutés aveuglément. Trois cas :

- **script local sans dépendance nouvelle** : la trace conserve la méthode, la commande ou la version, et le résultat ;
- **outil déjà autorisé** : la trace cite la référence de l’autorisation ;
- **nouvelle dépendance** : approbation requise, et la ressource indique les sept champs ci-dessous.

Toute ressource technique maintenue indique :

- stack et version ;
- date de vérification ;
- capacité résolue ;
- fallback ;
- limites ;
- owner ;
- prochaine revue.

L’automatisation détecte une partie des défauts mesurables. Elle ne remplace ni l’inspection de rendu, ni la capture, ni le jugement contextuel, ni l’observation utilisateur lorsque le risque la requiert.

Pour les composants critiques, maintiens une baseline d’états pertinents : variant, thème, viewport, données longues, loading, empty, error et focus lorsque nécessaires. Une capture versionnée et une revue explicite peuvent fournir une preuve proportionnée lorsqu’un pipeline de stories ou de tests visuels n’existe pas.

---
