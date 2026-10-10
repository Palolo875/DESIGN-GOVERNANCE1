# Savoir — contexte et accessibilité

Accessibilité, contextes à fort enjeu, responsive et mouvement.

<!-- origine:SAVOIR.md -->
# SAVOIR/CONTEXT — accessibilité, contexte et robustesse

[REQUIS PAR LE MODULE — contrôle applicable dans ACTION] SAVOIR décrit la décision de conception contextualisée. ACTION porte le contrôle, le scope, la méthode, la preuve et le verdict. Une phrase de conformité dans SAVOIR ne remplace pas un contrôle Gate A.

Les principes de livraison sont : contraste calculé, sémantique, nom accessible, clavier, focus visible, information non chromatique, cibles adaptées, reduced motion, contenu long et récupération compréhensible.

### Contextes à fort enjeu

Cette liste est indicative et non exhaustive.

| Catégorie | Exemples | Priorité |
|---|---|---|
| Réglementé ou sécurité critique | Santé, paiement, commande machine, sécurité. | Convention, confirmation, traçabilité, prévention et récupération. |
| Décision intensive | Supervision, finance professionnelle, data dense. | Hiérarchie, densité utile, vitesse de lecture et précision. |
| Réactivité ou gameplay | Jeu, contrôle temps réel, action à latence sensible. | Lisibilité, feedback et réponse immédiate. |

La singularité d’un contexte critique peut être la clarté, la robustesse et la convention fiable. Elle ne requiert ni spectacle ni rupture de repère.

Lorsque expression et sécurité, clarté, conformité ou récupération entrent en tension, la protection critique déclarée par `DIRECTION/START` prévaut. Résous la direction par hiérarchie, contenu, confirmation et robustesse, non par un effet spectaculaire ; le référentiel, le médium, le scope, la méthode et la limite restent explicites dans ACTION.

### Responsive et performance

Recompose plutôt que comprimer. Contenu, priorité, ordonnancement et interaction peuvent changer selon appareil et contexte. Réserve l’espace des médias, donne un feedback immédiat, rends les erreurs récupérables, évite les attentes silencieuses et protège l’information prioritaire.

Les propriétés CSS, valeurs de viewport, formats, budgets et support navigateur sont des ressources techniques, non des lois de style.

### Motion et espace

La motion doit expliquer, confirmer, orienter ou rendre une relation matérielle compréhensible. Elle ne doit pas retarder la tâche. Intensité, durée, easing, distance et ressort s’ajustent à l’action, au device et au langage du produit.

Une animation interactive est décrite comme un système d’états : état initial, trigger, transition, interruption et résultat. Une scène 3D ou spatiale est justifiée seulement lorsqu’elle rend un produit, une relation de profondeur, une navigation ou une information spatiale plus compréhensible.

Documente l’équivalent de motion réduite, l’interruption, le fallback statique, clavier/tactile, contenu alternatif, performance, device, runtime, mobile et capture. Une capture documente le rendu dans son scope, mais ne remplace pas un test d’accessibilité, de performance ou de tâche. Si motion ou scène ne donnent ni feedback, ni information, ni relation spatiale, préfère la suppression ou une composition 2D plus juste.

Pour choisir le mécanisme, gérer des interruptions ou traduire un geste mobile, consulte les méthodes de `SAVOIR/TECH` au moment de l’implémentation. Un mouvement réduit conserve l’état, la conséquence et l’accès à l’action ; il réduit la transition, sans enlever le feedback utile.

---
