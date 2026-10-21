Bonjour,

Voici l'écran de suivi des interventions du jour (`index.html`). C'est un seul fichier. Il s'ouvre directement dans un navigateur, sur ordinateur comme sur téléphone, sans serveur ni connexion : les 40 interventions de `interventions.csv` sont intégrées telles quelles.

## Comment l'écran est organisé

**Le filtre « Technicien » sert de point d'entrée.** Il propose quatre gros boutons : Équipe, Karim, Sophie, Théo. Le téléphone retient le dernier choix, donc un technicien retrouve directement sa journée à chaque ouverture.

**Vue « Équipe », pour Nathalie Roux sur son écran de bureau :**
- En haut, quatre chiffres : **4 en retard** (en rouge), **9 en priorité haute non terminées** (en orange), 3 en cours, 6 terminées sur 40. Un clic sur un chiffre filtre la liste.
- Un bloc **« À surveiller »** contient deux parties :
  - les 4 retards, les priorités hautes en premier ;
  - les 7 autres interventions en priorité haute, en commençant par celle en cours (la cabine bloquée avec une personne à l'intérieur, quai Claude-Arnaud).

  Chaque ligne affiche la note. Un clic amène à l'intervention dans la liste.
- Un bloc **« Où en est chacun »** donne pour chaque technicien ce qu'il fait en ce moment, sa prochaine intervention et son nombre de retards.

**Vue d'un technicien, sur téléphone :**
- Une grande carte **« Prochaine intervention »** montre l'heure, le délai (« dans 15 min » ou « 2 h 05 de retard »), l'**adresse en gros**, l'appareil, la note et un bouton **« Itinéraire »** qui ouvre la navigation.
- En dessous, deux encadrés : l'intervention en cours et les trois suivantes.

**La liste complète** est triée par heure. Elle a son propre filtre **« Statut »** : Tous, En retard, En cours, À faire, Terminées, avec le nombre d'interventions dans chaque cas. Un trait « Maintenant · 10 h 30 » sépare la matinée du reste de la journée. Le statut est toujours écrit en toutes lettres, pas seulement en couleur. Chaque adresse ouvre l'itinéraire.

**Pour les gants et les déplacements :** les boutons font au moins 52 px de haut et le texte est grand et contrasté. Rien ne demande de faire défiler sur le côté. L'écran passe en thème sombre si le téléphone l'est.

## Les états prévus

Le bas de la page contient des liens pour voir chaque état :
- **Filtre sans résultat.** Exemple : Karim + « En retard », qui donne bien 0. Un message s'affiche, avec un bouton pour revenir à tous les statuts ou à toute l'équipe.
- **Données non chargées.** Un message d'erreur et un bouton « Réessayer ». Aucune liste n'est affichée : une liste périmée pourrait envoyer quelqu'un sur une intervention déjà prise. Le message invite à appeler Nathalie Roux.
- **Hors connexion avec des données anciennes.** C'est le cas fréquent sur le terrain. Un bandeau signale l'heure des données affichées et propose de réessayer.
- **Chargement.** Un message s'affiche pendant que la page se remplit.

## Hypothèses que j'ai faites

1. **L'heure est fixée à 10 h 30 le mardi 20 octobre 2026**, comme demandé. L'horloge de l'appareil n'est pas utilisée. Les retards (« +3 h ») et les délais (« dans 15 min ») sont calculés à partir de 10 h 30.
2. **« Urgent » veut dire priorité « Haute »** et pas encore terminée.
3. **« Prochaine intervention » d'un technicien :** d'abord ses interventions en retard, la priorité haute en premier, puis ses interventions « À faire » par ordre d'heure. Pour Sophie, c'est donc la panne de l'école à 8 h 25, avant l'entretien de 7 h 30. C'est un choix à valider avec vous : si vous préférez l'ordre strictement horaire, c'est une ligne à changer.
4. Le bouton « Itinéraire » ouvre Google Maps avec l'adresse telle qu'elle est écrite.
5. Pour brancher l'écran sur vos vraies données, il suffit de remplacer la fonction de lecture (repérée dans le code) par un appel à votre fichier ou à votre service. L'actualisation automatique n'est pas faite : il y a un bouton « Actualiser ».

## Ce que les données montrent à 10 h 30 (à signaler à Nathalie)

- **Sophie** fait un entretien en priorité basse (11, rue Pasteur-Prolongée) alors que sa **panne en priorité haute dans une école** (115, impasse des Glycines, appareil à l'arrêt) a 2 h 05 de retard. Une réaffectation est peut-être à envisager.
- **Les deux retards de Théo sont bloqués**, pas seulement en retard : une pièce manque à l'hôtel de la rue Chevreul-Basse, et l'accès au local machinerie a été refusé rue Paul-Duvernay. Il est par ailleurs mobilisé sur la cabine bloquée.
- **Karim** n'a aucun retard. Sa prochaine intervention est à 10 h 45, au 24, impasse des Glycines.

## Points relevés dans les données (laissés tels quels)

- INT-2605 est « Terminée », mais sa note dit encore « Pièce reçue, pose prévue ».
- Certaines rues apparaissent avec deux codes postaux différents : impasse des Glycines, rue du Vieux-Moulin, boulevard des Tchécoslovaques-Sud, place Jean-Macé-Haute et avenue Jean-Jaurès-Ouest, en 69007 et en 69008. Avec de vraies adresses, il faudrait le vérifier, car l'itinéraire en dépend.

---

**Fichiers produits**
- `index.html` : l'écran de suivi, avec les données intégrées et tous ses états.
- `reponse.md` : ce message.
- (`interventions.csv` et `brief.md` sont fournis par vous et n'ont pas été modifiés.)
