# Pourquoi les juges ont préféré F et E

Analyse du 10 octobre 2026. Périmètre autorisé : consolidation, lectures utiles, choix de direction et essai mobile avec mouvement. La comparaison concurrentielle et l’anglais sont reportés.

Cette relecture connaît les versions et les résultats. Elle explique les raisons déclarées des deux juges et les rapproche des artefacts ; ce n’est ni un nouveau jugement aveugle ni une démonstration causale.

## Ce que les deux juges disent réellement

| Comparaison | Préférence commune, confiance moyenne | Motif commun | Qualité reconnue à l’autre proposition |
|---|---|---|---|
| F / A — facturation 1 | F, ancienne version | Client, prestation, quantité, prix, TVA et échéance visibles ; accès à la tâche concret ; trois exemples de statuts dans la page complète. | A montre immédiatement le document obtenu, avec une voix typographique distincte et des alignements soignés. |
| E / C — facturation 2 | E, ancienne version | Relation explicite entre prestation et montant ; « Modifier cet exemple » près de la facture ; « Changez les heures. Le total suit. » ; bénéfices précis et offre repérable. | C explique les étapes plus brièvement, nomme les petites équipes et propose une lecture plus dépouillée. |
| B / D — atelier vélo | D, nouvelle version | Besoin, jour et heure visibles ; dépôt distingué de la durée de réparation ; états et action finale mieux exposés. | B présente des choix plus amples et des prix immédiatement associés aux besoins. |

Le point commun est la **compréhension du mécanisme et de l’engagement proposé**, avec des compromis de densité et de présentation. Une préférence pour F ou E n’établit pas une supériorité universelle de Manrope, du vert, du terre cuite ou du formulaire visible.

Sources originales : [juge 1](../../U6/jugements/resultats/juge-1.md), [juge 2](../../U6/jugements/resultats/juge-2.md). Captures revues par le coordinateur : [F](../../U6/jugements/juge-1/F-1440-premiere.png), [A](../../U6/jugements/juge-1/A-1440-premiere.png), [E](../../U6/jugements/juge-1/E-1440-premiere.png), [C](../../U6/jugements/juge-1/C-1440-premiere.png). Les vues complètes et mobiles restent accessibles dans la [galerie U6](../../U6/Galerie-U6.html).

## Ce que les décisions des producteurs éclairent

F choisit dès sa trace initiale un instrument éditable dans l’accueil. E choisit un document final avec un lien explicite vers son éditeur. Deux dispositions différentes conduisent donc à une préférence commune ; l’avantage ne se résume pas à « mettre le formulaire dans le hero ».

A choisit le document et une expression éditoriale à empattements. Sa comparaison construite porte sur la voix du titre. C compare son champ coloré et construit une facture de prestation à quantité unique. Les deux possèdent une démo locale fonctionnelle : les juges, qui voient uniquement les captures, ne peuvent pas en explorer les autres états. Une capacité implémentée mais peu expliquée dans l’état montré n’améliore pas automatiquement sa compréhension visuelle.

Les quatre producteurs citent un tableau de bord ou une grille de bénéfices comme contre-choix. Les traces ne documentent pas une comparaison construite entre plusieurs solutions viables de la même relation : document à modifier, instrument déjà visible, ou révélation progressive. Cette absence donne une piste d’amélioration ; elle ne prouve pas qu’une telle comparaison aurait changé le verdict.

Traces : [F](../../U6/runs/run-01/livrable/trace.md), [A](../../U6/runs/run-02/livrable/trace.md), [C](../../U6/runs/run-03/livrable/trace.md), [E](../../U6/runs/run-04/livrable/trace.md).

## La refonte a-t-elle retiré une règle utile ?

La comparaison des paquets exacts U6 retrouve **39 blocs protégés identiques, trois blocs de chargement modifiés, aucun bloc absent et un relais ajouté**. Les six sources principales examinées — premier objet, direction, premier rendu/UI-UX, typographie, qualité créative et sélection des formes — sont identiques entre les deux versions. Le [relevé machine](diff-normatif-u6.json) conserve leurs empreintes et son périmètre.

La refonte change la disponibilité immédiate de certains détails et les consignes de lecture. Elle peut donc modifier l’attention ou la séquence de travail, même avec un contenu conservé. U6 ne permet pas d’isoler cet effet : pas de graine attestée, peu de répétitions, deux briefs succincts et des moyens communs restreints. La préférence esthétique ou la charge cognitive n’ont pas de mesure causale.

Il n’est donc pas justifié d’attribuer les préférences à une perte de savoir ni de restaurer tout l’ancien noyau sur ce seul résultat. Les originaux sont conservés ; [1 344 fichiers ont été figés](u6-originaux.sha256.json) avant cette suite.

## Pourquoi les lectures restent lourdes

Les six producteurs servent toutes leurs clés avant le premier HTML. La ligne DIRECTION place cadrage, fabrication, contrôle et clôture dans une seule colonne intitulée « Charger d’abord ». Elle demande aussi une raison pour chaque route conditionnelle ouverte ou écartée. Ces formulations peuvent encourager une préparation exhaustive. La conformité à ces formulations est observable ; leur coût cognitif et leur effet esthétique ne le sont pas.

La correction précise le **moment** des lectures : cadrage et contraintes avant le premier objet ; fabrication et observation à leur usage ; formalisation complète à la sortie. Une précondition ou un risque critique avance la lecture nécessaire. Les gates et les conditions de trace restent applicables. L’inventaire anticipé de toutes les exclusions cède la place aux raisons qui changent une décision dans la trace existante.

Le volume final peut rester proche si toutes les responsabilités sont nécessaires. Cette modification ne revendique donc ni baisse du coût API, ni amélioration générale des rendus.

## Corrections retenues et condition de preuve

1. Clarifier les étapes dans l’unique table de chargement, sans deuxième registre de routes.
2. Rendre observable le lien objet → action → conséquence, sans imposer une forme de premier écran.
3. Comparer des positions plausibles sur une relation réellement ouverte, au niveau de matérialisation utile.
4. Détailler l’implémentation des transitions annulables et du mobile dans le savoir technique, chargé à la demande.
5. Construire un essai Web mobile séparé d’U6 : état correct sans animation, modifications rapides, panneau interrompu, clavier, erreurs, reprise et mouvement réduit.

L’essai est une fabrication contrôlée du coordinateur, qui connaît les résultats U6. Il éprouve une méthode et un comportement ; il ne remplace ni un nouveau protocole indépendant ni un test utilisateur. L’amélioration esthétique générale reste ouverte.
