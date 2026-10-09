# Direction — créer puis apprendre

Observer le rendu, corriger le défaut principal, réobserver.

<!-- origine:DIRECTION.md -->
## DIRECTION/DOUBLE-LOOP — créer puis apprendre

DIRECTION porte la première boucle de création et formule le défaut dominant de direction ou de craft. Après observation du rendu réel, la boucle d’amélioration suit : **observer → isoler le défaut dominant → modifier l’artefact → observer à nouveau → comparer → décider**. DIRECTION ne remplace pas l’artefact par une rationale ; elle demande une correction visible lorsque la décision le requiert, ou documente pourquoi aucune correction utile n’est possible. `ACTION` reste propriétaire de la preuve exécutée, de la réinspection, des gates, des verdicts et de la clôture.

### Contrôle du premier objet — qualité intrinsèque sans nouveau gate

Avant de présenter un premier rendu comme proposition principale, inspecte l’artefact réel et sa capture dans le scope disponible. Le premier rendu doit déjà être **beau, composé, crédible, spécifique et suffisamment résolu** à l’échelle du mode ; ce contrôle ne sert pas uniquement à repérer le slop ou les défauts de conformité. Ce contrôle ne remplace ni les gates d’ACTION, ni les axes V/U/A/T, ni une tâche utilisateur ; il protège la qualité **intrinsèque** du premier objet contre le rendu générique, creux, décoratif ou trompeur.

Avant de présenter, applique le contrat positif de `DIRECTION/FIRST-OBJECT` à la capture réelle ; un défaut appelle la réponse de la colonne « Retour si… ».

Lorsqu’une dimension échoue, l’agent peut effectuer **une correction substantielle**, c’est-à-dire une correction qui change réellement l’artefact ou la décision, sans quota d’itérations. Si aucune correction utile n’est possible avec les capacités et contraintes disponibles, il présente la limite ou escalade le besoin ; il ne boucle pas pour polir, ni ne substitue une déclaration de goût à une observation.

### One-shot et boucle d’amélioration

Le `one-shot` est une branche raccourcie de la même discipline, jamais l’absence de discipline. Avant le build, vérifie : décision dominante, risque, public ou JTBD lorsque pertinent, position, premier objet attendu, contrainte réelle et prochaine preuve. Après le build, vérifie : capture réelle dans le scope, contrôle des huit dimensions du premier objet, revue créative, vérification du risque dominant, états et transformations pertinentes. Tu peux t’arrêter après cette observation si la qualité initiale attendue est atteinte, que la direction est identifiable, que les risques applicables sont couverts et qu’aucune amélioration utile ne promet un gain réel (B1b dans son scope, `ACTION/GATE-B/B1b`). Si le rendu est faible, générique ou incomplet, corrige, retourne ou escalade ; ne transforme pas `EXPLORATORY` en permission de livrer une première proposition creuse.

<!-- noyau:début BOUCLE -->
La boucle commune est : **préparer → construire → observer → isoler le défaut dominant → modifier l’artefact ou la décision → observer à nouveau → comparer → décider**. La modification doit changer une relation visible, une tâche, une preuve, une contrainte ou une propriété de robustesse. Une nouvelle rationale, une variante décorative ou une reformulation de la trace ne constitue pas une correction. Pour un rendu HTML, `python3 scripts/check_render.py page.html` (navigateur requis) observe les fautes objectivables aux largeurs courantes : `--click SÉLECTEUR` observe un autre état, `--captures DOSSIER` écrit une capture pleine page par largeur ; les polices et images hébergées ailleurs sont bloquées sauf avec `--allow-external` ; il ne juge ni la direction ni l’usage.
<!-- noyau:fin BOUCLE -->

### Boucle d’édition — du diagnostic au geste

<!-- noyau:début BOUCLE-DIAGNOSTIC -->
La seconde boucle n’est pas une suite de petits polish. Après observation, choisis la suite qui correspond au diagnostic :

| Diagnostic | Suite appropriée |
|---|---|
| Défaut local et direction intacte | Corriger l’artefact puis réobserver. |
| Défaut de craft ou de résolution | Appliquer un geste de `SAVOIR/STATE` avec sa condition, puis réinspecter. |
| Direction faible, interchangeable ou contradictoire | Rouvrir la direction, reformuler ou requalifier la cible avant de continuer le polish. |
| Risque ou périmètre changé | Reclassifier avec `DIRECTION/START`. |
| Preuve insuffisante | Déclarer la limite et produire la prochaine preuve proportionnée. |
| Décision suffisamment établie | Proposer (trace légère : la proposition vaut checkpoint) ; en trace complète, décider et persister la trace. Ne pas prolonger le polish sans changement attendu. |
<!-- noyau:fin BOUCLE-DIAGNOSTIC -->

<!-- noyau:début BOUCLE-QUESTIONS -->
Pour une décision créative, en plus de la revue de `SAVOIR/CRAFT/CFT-00`, note ce qui a réellement changé. Note aussi si la correction a affaibli l’usage, l’accessibilité, la robustesse, la direction, ou la hiérarchie et l’harmonie de l’ensemble : réobserve la page entière, pas seulement la zone corrigée. Dis enfin si la direction doit être corrigée, rouverte ou maintenue.
<!-- noyau:fin BOUCLE-QUESTIONS -->

### Signaux de réouverture

Rouvre la direction, la cible, l’ancre, la structure ou le build lorsque l’un de ces signaux est observé :

| Signal | Retour privilégié |
|---|---|
| La thèse ou la promesse n’est pas perceptible dans la scène. | `VISUAL_TARGET` ou `FIRST-OBJECT`. |
| Le foyer est perdu ou plusieurs éléments se disputent l’attention. | Composition, hiérarchie ou contenu réel. |
| La signature devient générique ou ne survit pas au remplacement du produit. | Position, contre-choix ou `SAVOIR/STYLE` si le style change une décision. |
| L’objet de preuve ou le geste produit est absent, décoratif ou trompeur. | `FIRST-OBJECT`, contenu, action ou vérité de scène. |
| La résolution, un état critique, le mobile ou le runtime détruit la relation principale. | Build, états, fallback, capacité ou résilience. |
| Une observation, une source, un asset ou un claim devient obsolète ou non vérifiable. | Ancre, preuve, scope ou réserve dans ACTION. |

Ces signaux déclenchent une décision de retour, pas un nouveau gate ni un nouveau statut. Si aucun retour utile n’est possible avec les capacités disponibles, conserve la limite, l’owner et la prochaine preuve dans ACTION.

La création et la preuve restent distinctes. `DIRECTION` choisit la relation visuelle, la cible, la position et le défaut dominant ; `ACTION` exécute les preuves, la réinspection, les gates, les verdicts et la clôture. DIRECTION ne ferme jamais un run à la place d’ACTION. Aucun nombre d’itérations, score, état de qualité ou claim « haut de gamme » n’est créé. Sans capture inspectée, la qualité perceptuelle correspondante reste `NOT-VERIFIED` selon ACTION.

---

### Test de résilience visuelle

Avant la clôture d’une direction, choisis une transformation pertinente lorsque celle-ci peut révéler une faiblesse réelle : crop mobile, contenu long, état vide ou erreur, retrait ou remplacement d’asset, zoom, reflow, réduction d’effet, fallback typographique ou runtime cible. Ce n’est pas un quota ; la transformation est choisie parce qu’elle peut modifier le jugement.

| Transformation | Relation à vérifier |
|---|---|
| **Asset absent ou remplacé** | La promesse, la preuve et la signature tiennent-elles sans dépendance à une image séduisante ? |
| **Contenu long ou extrême** | La composition et la hiérarchie survivent-elles au contenu réel ? |
| **Mobile, zoom ou reflow** | La direction reste-t-elle lisible sans sacrifier la tâche ou l’accessibilité ? |
| **État critique** | Erreur, empty, permission, loading ou récupération conservent-ils la relation principale ? |
| **Réduction d’effet** | La direction tient-elle si la motion, la profondeur ou la matière doivent être réduites ? |

La réponse documente l’observation et la limite ; elle ne transforme pas un test perceptuel en preuve d’utilisabilité ou de conformité.

### Signaux d’apprentissage expérimental

Lorsque le projet est suivi comme pilote, conserve dans la trace existante le défaut dominant du premier rendu, sa cause probable, la correction choisie, le gain visible, la régression éventuelle et la capacité manquante. Ces signaux servent à améliorer V1 au niveau de la série de runs ; ils ne deviennent ni score esthétique, ni verdict, ni quota.
