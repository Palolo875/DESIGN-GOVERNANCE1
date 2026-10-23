# Produit — interface

Le contrat d’interface réelle, puis le cadrage du médium et des capacités disponibles.

<!-- origine:ACTION.md -->
## ACTION/UI-UX-REALITY — construire l’interface et la tâche ensemble

Pour une surface UI/UX nouvelle ou substantiellement modifiée, le premier objet doit rendre observables, dans la proportion du mode et du risque : hiérarchie de contenu, premier geste, feedback, états `loading`, `empty`, `error`, `unavailable`, `disabled` et succès partiel lorsque pertinents, contenu long ou multilingue, responsive recomposé, focus et récupération. Une capture de l’état nominal ne suffit pas lorsque l’état, la tâche ou la récupération fait partie de la décision. Pour présenter la proposition, l’état qui ouvre la page est rempli, avec des valeurs marquées comme exemple si besoin ; l’état vide se conçoit pour l’usage réel. Lorsque la première utilisation réelle commence sans données (nouvel espace de travail, premier projet), cet état vide conçu est l’accueil du produit : l’état rempli de démonstration se montre à côté, marqué comme tel, sans le remplacer.

Le contrat de production relie :

```text
CONTENT-MODEL: données et hiérarchie réellement portées
PRIMARY-TASK: tâche et résultat attendu
FIRST-GESTURE: action initiale et feedback associé
CRITICAL-STATES: états, erreurs, permissions et récupération applicables
RESPONSIVE-RELATION: ce qui est préservé, recomposé ou remplacé selon le viewport
ACCESSIBILITY-BASIS: sémantique, nom, focus, clavier, contraste et alternative selon le risque
ROBUSTNESS-BASIS: contenu extrême, chargement, compatibilité, performance ou non-régression selon le risque
EXPECTED-SCOPE: scope attendu — surface, état, viewport, données, population ou runtime à observer (avant build)
OBSERVED-SCOPE: scope observé — surface, état, viewport, données, population ou runtime réellement observé (après observation)
```

La couverture de chaque exigence emploie `OBSERVED`, `NOT-VERIFIED` ou `N/A-JUSTIFIED` avec sa raison. `OBSERVED` n’est pas `PASS` : une observation peut être négative, et son résultat vit dans `EVALUATION_CASE` ou dans la trace. `NOT-OBSERVED` n’y est pas employé : il qualifie une conséquence de décision (`ACTION/STATUS`). Une exigence porte un seul statut par locator ; deux contextes distincts (état, largeur, version) se déclarent par deux locators distincts.

Ces lignes décrivent les décisions de construction et la couverture attendue ; elles ne créent pas un nouveau gate ni un formulaire universel. `ACTION` garde les preuves, les limites et le verdict ; `SAVOIR/CONTEXT` et `SAVOIR/TECH` sont chargés seulement lorsque leurs questions peuvent changer la décision, la preuve ou la limite. Lorsque la capacité nécessaire manque, déclare `NOT-VERIFIED` ou l’issue appropriée au lieu de réduire silencieusement l’ambition de protection.

**Flux d’engagement.** Dans un flux d’inscription, d’abonnement, de paiement, de consentement ou de résiliation, refuser, annuler ou se désabonner reste aussi visible et aussi court qu’accepter. Sont exclus les motifs trompeurs (dark patterns) : formule culpabilisante sur le choix de refus (« Non merci, je préfère payer plus »), option présélectionnée en faveur de l’offre, prix ou frais révélés seulement à la fin, résiliation par un autre canal ou par un parcours plus long que l’inscription. Une exception demandée par la personne est déclarée dans la réponse. Ces motifs ont valu à Amazon, en septembre 2025, un accord de 2,5 milliards de dollars avec la FTC sur l’inscription et la résiliation de Prime, dont 1 milliard de pénalité civile, sans reconnaissance de faute [VEILLE 2026-10].

**Source de classification.** Le mode est classé par `DIRECTION/START`. ACTION ne reclassifie pas silencieusement une tâche parce qu’une capacité, un outil ou une preuve manque. Il déclare alors la limite, le statut et la prochaine preuve.

<!-- origine:DIRECTION.md -->
## DIRECTION/CAPACITY — cadrage de médium et de capacité

Après le choix du mode, choisis la capacité minimale qui permet de construire ou de vérifier la décision : code et runtime, fichier de design et handoff, CMS, primitive accessible, typographie variable, motion d’état, scène spatiale ou aucune capacité spéciale. Pour un médium non Web, parcours explicitement **médium réel → capacité → preuve propre au médium → fallback** ; ne transpose pas un critère Web sans vérifier son équivalent réel.

Une **capacité** est une possibilité de construction ou de vérification qui change le résultat, la preuve ou la robustesse. Elle n’est activée que si son absence empêcherait de construire, décider, observer ou tenir une contrainte.

Distingue la capacité de **construction** de la capacité de **vérification**. Un runtime peut être nécessaire pour vérifier un comportement sans devenir le médium principal de conception.

Lorsque la plateforme ou la stack change réellement la construction, le rendu, l’interaction, l’accessibilité ou la performance, la ligne de run déclare la cible concernée et adapte la preuve au runtime réel. Le système ne connaît ni la stack, ni les contraintes techniques, ni les délais tant qu’ils ne sont pas déclarés ; une contrainte déterminante porte owner, conséquence et prochaine preuve. Une adaptation de plateforme ne doit pas dégrader l’intention visuelle ni simuler un rendu qui n’a pas été observé.

| Besoin | Capacité possible | Contrat |
|---|---|---|
| Système partagé ou handoff complexe | Fichier de design, variables/tokens, documentation et liens code. | Source de vérité, owner, mapping et non-régression. |
| Publication éditoriale à cadence élevée | CMS ou système de publication. | Modèle, templates, locales, états, assets et recette. |
| Comportement critique | Primitive accessible ou composant du projet. | Sémantique, clavier, focus, états, tokens et responsive. |
| Feedback ou narration interactive | Motion d’état. | États, triggers, interruptions, reduced motion, fallback et capture. |
| Profondeur informative ou produit spatial | Scène 3D/spatiale. | Rôle spatial, performance, alternative, fallback et mobile. |
| Aucun gain de tâche, de preuve ou de compréhension | Aucune capacité additionnelle. | Solution la plus simple qui tient la direction. |

Une technique est un moyen de production ou de preuve. Elle ne devient jamais la direction par défaut.

---
