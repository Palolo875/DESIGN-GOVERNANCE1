# Écran de suivi des interventions — Lyon Sud

Bonjour,

Voici l’écran de suivi des interventions du mardi 20 octobre, tel qu’il se présente à 10 h 30. Ouvrez `index.html` : il fonctionne directement, sans installation.

## Ce que j’ai fait

L’écran répond à une seule question : **qui va où, maintenant**. Il comporte trois zones :

- **« Où aller ensuite »** : une carte par technicien. Elle donne l’intervention en cours (« Sur place »), puis l’intervention suivante en grand : heure, adresse sur deux lignes, type, appareil, note, avec un bouton **Itinéraire** qui ouvre la carte sur le téléphone. Une ligne « Puis… » annonce l’intervention d’après.
- **« À surveiller »** : la liste que le chef d’équipe lit d’un coup d’œil. On y trouve la panne urgente en cours (la cabine bloquée avec une personne à l’intérieur, INT-2611) et les 4 retards, chacun avec sa durée de retard calculée (« En retard de 2 h 35 ») et la note qui l’explique (pièce manquante, accès refusé…). Le compte des pannes urgentes encore à venir est affiché (6).
- **« Journée »** : les 40 interventions par heure, coupées par une ligne **« 10:30 Maintenant »**. Les interventions terminées sont tassées pour que le présent arrive vite.

**Les deux filtres** sont des gros boutons (48 px de haut, pensés pour des gants). Le filtre statut affiche le nombre d’interventions par statut, recalculé pour le technicien choisi. Sur le téléphone, le choix du technicien **est mémorisé** : Karim retrouve sa propre vue en rouvrant l’écran. L’adresse de la page garde aussi les filtres, ce qui permet d’envoyer un lien direct (par exemple `#tech=sophie`).

**Les états prévus :**
- **Aucun résultat** (par exemple Karim + « En retard ») : l’écran le dit en clair, rappelle ce que Karim a dans sa journée (1 en cours, 10 à faire, 3 terminées) et propose deux boutons : « Voir toutes ses interventions » ou « Voir “En retard” pour toute l’équipe ».
- **Données non chargées** : un message explique le problème. Aucune adresse n’est affichée, pour ne pas envoyer quelqu’un à une adresse périmée. Les filtres sont désactivés. L’écran propose un bouton **Réessayer** et un bouton pour appeler Nathalie Roux.
- **Chargement** : des emplacements gris s’affichent et les filtres restent désactivés tant que la liste n’est pas arrivée.

Les liens en bas de page permettent de voir chacun de ces états.

## Pourquoi ces choix

- **J’ai écarté le tableau de bord classique** (4 compteurs, un graphique, un grand tableau). Il montre des chiffres, mais il ne dit pas à Sophie où aller. Ici, les compteurs sont dans les filtres eux-mêmes et l’information « en retard / urgent » est placée à côté de l’action.
- **La couleur ne sert qu’aux statuts** : rouge pour le retard, bleu pour « en cours », vert pour « terminée ». La priorité haute porte un **jaune de signalisation** avec un triangle noir, pour ne pas la confondre avec le retard. Aucun statut ne repose sur la couleur seule : chaque statut est aussi écrit en toutes lettres et a une icône différente.
- **La police est Atkinson Hyperlegible Next**, conçue pour la lisibilité. Elle distingue bien le 0 du O et le I du l et du 1, ce qui compte pour lire « ASC-1431 » ou une adresse en marchant. Elle est livrée avec l’écran, ce qui évite de dépendre du réseau.
- **Sur ordinateur**, les cartes des techniciens et la journée occupent la gauche, et « À surveiller » reste fixé à droite. **Sur téléphone**, l’ordre change selon l’usage. Sans filtre, les points à surveiller viennent en premier. Avec un technicien choisi, sa prochaine intervention vient en premier. Quand on filtre par statut, la liste filtrée remonte juste sous les filtres.

## Hypothèses à valider

1. **L’ordre de la « prochaine intervention »** : j’ai placé les retards avant les rendez-vous à venir, les pannes de priorité haute en tête, puis l’heure prévue. Pour Sophie, la prochaine est donc la panne de l’école (08:25, appareil à l’arrêt) et non l’entretien de 07:30. Pour Théo, c’est la porte palière de 07:55, alors que la note signale une pièce manquante. Cette règle ne lit pas les notes : si le service préfère un autre ordre, ou un statut « bloqué », c’est à décider ensemble.
2. **L’heure est figée à 10:30** pour la démonstration, comme demandé. Dans la vraie version, elle suivra l’horloge, et les retards seront recalculés.
3. **Les données** : quand l’écran est ouvert directement, il utilise une copie de `interventions.csv` intégrée au fichier. Quand il est servi par un serveur web, il lit `interventions.csv` à côté de lui. Le bas de page indique la source utilisée.
4. **Le numéro du chef d’équipe** (04 78 00 00 00) est un **numéro d’exemple**, signalé comme tel à l’écran. Il faut le remplacer.
5. **L’écran est en lecture seule** : les techniciens ne peuvent pas changer un statut depuis l’écran, car ce n’était pas demandé.
6. **Pas de thème sombre** : l’écran est clair, ce qui est plus lisible en extérieur.

## Ce qui a été vérifié et ce qui ne l’a pas été

- **Vérifié** dans le navigateur, sur téléphone (390 px), tablette (768 px) et bureau (1 100 et 1 440 px) : pas de débordement ni de texte coupé, contrastes du texte conformes au niveau AA, boutons assez grands, navigation au clavier avec un focus visible, aucune animation.
- **Calculs recoupés automatiquement** : 40 lignes au total, 4 retards dont la durée est recalculée, « dans 15 min » pour Karim, comptes par technicien. Le message « aucun résultat » apparaît à l’écran avec les bons chiffres, et « Réessayer » recharge bien la liste.
- **Pas vérifié** : l’usage réel. Il faudrait observer un technicien avec des gants, dehors, sur son propre téléphone, et le chef d’équipe pendant une matinée. Il reste aussi à confirmer l’ordre de la file et à vérifier la lecture par un lecteur d’écran.

## La suite

1. Validez (ou corrigez) la règle d’ordre de la prochaine intervention et dites-moi si les notes du type « pièce manquante » ou « accès refusé » doivent devenir un statut « bloqué ».
2. Si l’écran convient, l’étape suivante consiste à le brancher sur votre vraie source de données avec l’heure réelle, puis à le tester une demi-journée avec un technicien. Il me faudra pour cela le format d’export de votre outil de planification et le vrai numéro de joignabilité.

---

**Fichiers produits**
- `index.html` : l’écran (données intégrées, lecture de `interventions.csv` quand il est servi par un serveur web)
- `atkinson-hyperlegible-next-latin.woff2` : la police utilisée par l’écran
- `OFL-atkinson-hyperlegible-next.txt` : la licence de la police (SIL Open Font License)
- `reponse.md` : ce message
