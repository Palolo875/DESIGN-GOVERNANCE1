# Produit — interface

Cadrage du médium et des capacités disponibles.

<!-- origine:DIRECTION.md -->
## Cadrage de médium et de capacité

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
