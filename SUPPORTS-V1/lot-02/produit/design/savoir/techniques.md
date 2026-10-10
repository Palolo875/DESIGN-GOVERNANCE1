# Savoir — techniques

Techniques, tests et production par médium.

<!-- origine:SAVOIR.md -->
# SAVOIR/TECH — techniques, tests et stack

[MÉTHODE] CSS, code, outils et automatisation servent hiérarchie, performance, cohérence et accessibilité. Utilise une technique parce qu’elle produit un effet ou une robustesse impossible à obtenir plus simplement, non parce qu’elle est disponible.

Associe chaque technique à une preuve adaptée :

| Question | Preuve adaptée |
|---|---|
| Transformation ou calcul non trivial | Script ou test déterministe. |
| Comportement d’interface | Inspection du runtime. |
| Relation visuelle simple | Capture et revue de code. |
| Coût de performance | Mesure de build, profiling ou observation runtime. |
| Compatibilité | Test sur support déclaré et fallback. |

### Hiérarchie de jugement pour les interfaces

Le jugement commence par `P0` : direction visuelle, hiérarchie, composition, typographie, matière, états, contenu et action dominante. `P1` vérifie le plancher de compréhension, d’usage et d’accessibilité. `P2` vérifie que la décision est correctement traduite dans le runtime réel — web, Flutter, Swift, Kotlin ou autre stack. `P3` couvre performance, compatibilité, robustesse et maintien lorsque le risque le requiert. Si un risque critique d’usage, d’accessibilité, de sécurité, de confidentialité ou de permission est déclaré, sa protection passe avant l’optimisation visuelle, sans supprimer les autres contrôles. Une plateforme ne justifie ni une dégradation silencieuse du craft ni un `PASS` sans preuve.

### Traduire production et observation par médium

Ces points de départ adaptent le contrat au support utile ; ils ne constituent ni catalogue obligatoire ni preuve que les moyens sont connectés. Rapproche ressource retrouvable, action de fabrication et observation dans la fiche ou la spec existante ; charge seulement la famille qui peut changer la décision.

| Médium concerné | Ressource et intervention à concrétiser | Observation adaptée et limite |
|---|---|---|
| Web ou application native | Primitives de la stack réelle, tokens, contenu, états et intégration des assets. | Runtime, device, clavier ou gestes pertinents ; la recette HTML ne couvre pas automatiquement le natif. |
| Image ou identité | Fichiers source, police, marque, dessin, photo ou pack autorisé ; silhouette, cadrage, matière et déclinaisons. | Taille d’usage, détails, fonds et série ; l’image produite ne prouve ni authenticité ni droits. |
| Print, document ou présentation | Gabarit, contenu, police, format, marges, pagination ou ordre de lecture ; préparer l’export utile. | Pages ou slides finales, distance et support ; une prévisualisation numérique ne prouve pas encre, papier ou projection. |
| Motion ou vidéo | Assets, séquence, transitions, rythme, interruptions et alternative adaptée au canal. | Séquence rendue et durée, lecture et interruption si applicables ; une image fixe ne prouve pas la fluidité. |
| Son | Fichier, voix ou matière autorisée ; montage, niveaux, temporalité et alternative textuelle lorsque pertinente. | Écoute du fichier exporté et contexte de restitution ; waveform et transcription ne prouvent pas la qualité sonore. |
| Spatial ou 3D | Modèle, matériaux, éclairage, échelle, caméra, interaction et fallback selon le support. | Runtime, device, profondeur, confort et coût ; une capture 2D ne prouve pas l’expérience spatiale. |

Si production ou observation manque, conserve le plafond et la prochaine preuve dans les responsabilités ci-dessous ; une documentation de médium n’est pas une capacité de fabrication.

### Mettre en œuvre une transition interactive

[MÉTHODE] Le contrat d’états de `SAVOIR/CONTEXT` précède le choix technique. Commence par un état correct sans animation, puis ajoute la continuité qui aide à suivre sa transformation. La donnée, le nom accessible, la sélection et l’action disponible se mettent à jour sans attendre la fin de l’effet.

| Relation à construire | Point de départ technique | Fragilité à éprouver |
|---|---|---|
| Feedback d’un contrôle ou d’une valeur | Transition CSS ou animation locale, courte et annulable. | Actions répétées : l’état final correspond à la dernière intention, sans file d’effets périmés. |
| Déplacement ou recomposition d’un même objet | Mesurer avant/après, puis animer leur différence (FLIP) ; les View Transitions si le runtime et le fallback s’y prêtent. | Identité stable, contenu long, changement de largeur, interruption et état sans effet. |
| Entrée d’un panneau ou changement de vue | CSS ou Web Animations API selon le besoin de contrôle ; conserver le repère utile. | Ouverture/fermeture rapide, focus, retour, fermeture pendant l’entrée et absence de l’API. |
| Geste direct | Suivre le pointeur pertinent, avec capture et annulation explicites ; séparer poignée et zone défilable. | Défilement, mouvement inverse, plusieurs pointeurs, annulation du geste et alternative par bouton/clavier. |

Lis la géométrie nécessaire ensemble, puis écris les changements ; évite d’alterner mesure et écriture à chaque élément. `transform` et `opacity` sont souvent de bons points de départ, sans garantir le coût réel d’un effet. Si une animation est remplacée, observe la position courante, annule l’ancienne puis raccorde la nouvelle ; son callback périmé ne peut pas rétablir l’ancien état. Garde un état final correct si l’API manque, si le document devient caché ou si le mouvement réduit est activé pendant la transition. Une durée est calibrée sur la distance et la tâche : elle ne retarde ni validation, ni calcul, ni récupération.

Éprouve dans le runtime : action nominale, répétition rapide, inversion, fermeture ou annulation, puis préférence de mouvement réduit. Observe les états et les erreurs, pas seulement la fin de la séquence. Mesure le coût lorsque c’est le risque ; une émulation de viewport ou une capture fixe ne démontre pas la fluidité sur appareil physique.

### Adapter une interface mobile

[MÉTHODE] Distingue Web mobile et application native. Sur le Web, examine viewport dynamique, zones sûres, défilement du panneau, focus visible, champs adaptés et action qui reste accessible lorsque la hauteur disponible baisse. Une poignée de glissement garde un bouton de fermeture et ne détourne pas le défilement du contenu.

Dans le natif, utilise les primitives et les conventions de la plateforme : navigation et retour, taille de texte réglable, clavier et insets, sémantique d’accessibilité, gestes et réduction de mouvement. Les points iOS, les dp Android et les pixels CSS ne sont pas interchangeables ; des cibles usuelles de 44 points iOS ou 48 dp Android sont des repères de confort à vérifier dans leur contexte, pas une conversion automatique. SwiftUI, UIKit, Compose, Flutter ou React Native demandent une observation dans leur runtime et leurs devices déclarés.

Le Web mobile peut éprouver un contrat de tâche et une continuité visuelle ; il ne certifie ni un build natif, ni le clavier logiciel, les gestes système ou la performance d’un téléphone réel. Conserve ces limites et la prochaine preuve dans la trace existante.

[MÉTHODE] Pour tout médium non web — natif mobile, desktop, spatial, print ou embarqué — examine cinq responsabilités de preuve, regroupables dans un même artefact, avant de juger :

| Dérivation | Question | Conséquence de preuve |
|---|---|---|
| Rendu observable | Comment le rendu réel est-il observé ? | Capture device, émulateur, build sur support réel, capture casque, vidéo d’interaction ou épreuve print. Sans support d’observation, le craft reste `NOT-VERIFIED`. |
| Idiomes d’interaction | Pointer/clavier, tactile/gestes, controller, regard ou voix ? | Un idiome est `N/A-JUSTIFIED` uniquement s’il est non applicable au médium et au scope déclarés ; tout substitut est nommé, testé et limité. |
| Référentiel applicable | Quelle norme ou guideline fait référence ? | Séparer `CONFORMANCE-TARGET` — référentiel, version, niveau, scope et owner — de `QUALITY-TARGET` — confort, lisibilité, contraste ou autre cible qualitative. |
| Unité de budget | Qu’est-ce qui coûte dans ce médium ? | Load/INP pour le web ; lancement, frame rate et mémoire pour le natif ; frame rate, confort motion et lisibilité à distance pour le spatial ; encre et contraste pour le print, ou équivalent déclaré. |
| Preuve indisponible | Que ne peut-on pas vérifier ici ? | `NOT-VERIFIED` + `NEXT-PROOF`, jamais simulé. Traduire en équivalent du médium lorsque cela est possible. |

Un médium non web ne rétrograde pas silencieusement la décision : il traduit le craft et l’usage dans d’autres idiomes, puis adapte le support, l’unité de budget et la limite de la preuve lorsque le risque le requiert. L’adaptation de production est distincte : stack, délais, équipe et capacité déterminent ce qui est exécutable. Une contrainte déterminante porte owner, conséquence et prochaine preuve. L’absence de preuve produit d’abord `NOT-VERIFIED` et `NEXT-PROOF` ; `FAIL-ASSUMED` reste réservé à un échec connu, limité, assigné, documenté et re-testable selon ACTION/OVERRIDE, sans usage pour masquer une indisponibilité de runtime.

`CONFORMANCE-TARGET` nomme la référence ou le niveau visé ; il ne signifie pas que la conformité est obtenue. Pour juger ou transmettre un claim, conserver séparément la cible, la méthode exécutée, le scope et le runtime observés, le résultat, la limite et la `NEXT-PROOF`. Une cible déclarée sans observation adaptée reste `NOT-VERIFIED` ; une observation hors scope ne s’étend pas silencieusement à l’ensemble du produit.

Aucun outil, script ou package ne reçoit automatiquement un `PASS`. Une nouvelle dépendance exige l’approbation et les champs de la politique d’`ACTION/POLICIES` (inspection et ressources techniques) ; à défaut, conserve `NOT-VERIFIED` ou retourne le run.

Toute ressource de stack indique les sept champs d’`ACTION/POLICIES` (inspection et ressources techniques) et, lorsqu’elle soutient un claim, les claims applicables (`SAVOIR/TOOLS`). `SAVOIR/TOOLS` définit les exigences et limites ; ACTION conserve la fiche exécutée, la preuve, les statuts et le verdict ; CHANGELOG intervient lorsqu’une règle ou une route devient partagée.

---
