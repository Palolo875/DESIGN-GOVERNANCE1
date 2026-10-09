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
