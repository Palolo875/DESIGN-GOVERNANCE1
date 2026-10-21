Bonjour,

Voici l'écran de suivi des interventions du jour pour l'agence de Lyon Sud. C'est le fichier `index.html` : il s'ouvre d'un double-clic dans un navigateur, sans installation ni connexion.

## Ce que fait l'écran

**Les deux filtres demandés** sont en haut de l'écran :
- **Technicien** : Tous, Karim, Sophie ou Théo ;
- **Statut** : Tous, En retard, En cours, À faire ou Terminée. Chaque bouton indique le nombre d'interventions concernées, selon le technicien choisi.

Les boutons sont grands (48 px de haut au minimum) pour qu'on puisse les toucher avec des gants. Le choix est gardé en mémoire sur l'appareil : un technicien qui s'est sélectionné une fois retrouve directement sa journée la fois suivante.

**Pour Nathalie Roux (vue « Tous », sur écran de bureau)**
- Quatre compteurs (en retard, en cours, à faire, terminées). Un clic sur l'un d'eux filtre la liste.
- Un bloc **« À surveiller »** avec deux colonnes :
  - **En retard** (4 interventions), avec le retard en heures et la raison notée ;
  - **Urgent** : les interventions de priorité haute qui ne sont pas terminées (7, sans compter celles déjà en retard). L'intervention en cours est affichée en premier.
- Un bloc **« Équipe »** qui montre, pour chacun des trois techniciens, ce qu'il fait en ce moment, sa prochaine intervention et son nombre de retards.
- La liste complète, triée par heure. Les interventions en retard sont repérées par une barre rouge, celles en cours par une barre bleue, et les terminées sont grisées.

**Pour un technicien (sur téléphone)**
- En tête : une grande carte **« Prochaine intervention »** avec l'heure, le temps restant (« dans 15 min »), l'adresse en gros, l'appareil, le type, la note et un bouton **Itinéraire** qui ouvre l'adresse dans Google Maps.
- En dessous : l'intervention en cours, puis ses interventions en retard, marquées « à voir avec Nathalie Roux ».
- Enfin, la liste de sa journée.

**Les états prévus**
- **Aucune intervention pour ce filtre** : un message adapté au cas, par exemple « Aucune intervention en retard pour Karim Benali », avec deux boutons, « Voir tous les statuts » et « Voir toute l'équipe ». Pour essayer : filtres Karim + En retard.
- **Données non chargées** : un message clair, un bouton « Réessayer » et la consigne d'appeler Nathalie Roux en cas d'urgence. Dans ce cas, aucune ancienne liste n'est affichée.
- **Connexion perdue** (fréquent en sous-sol ou en gaine) : la dernière liste reçue reste visible, avec un bandeau qui avertit qu'elle n'est peut-être plus à jour.
- **Chargement** : des blocs gris temporaires s'affichent à la place des cartes en attendant les données.

Pour voir ces états sans attendre une vraie panne, des liens « Aperçu des états » se trouvent en bas de page. Ils ajoutent `?etat=chargement`, `?etat=erreur` ou `?etat=hors-ligne` à l'adresse. Ils servent à la démonstration et sont à retirer en production.

**Autres points** : textes et couleurs bien contrastés pour une lecture en plein soleil. Le statut n'est jamais indiqué par la seule couleur : il y a toujours un libellé. Un thème sombre s'applique automatiquement si le téléphone est réglé ainsi. L'écran n'utilise aucune police ni ressource externe et se charge donc même avec un réseau faible.

## Hypothèses retenues

1. **Heure figée à 10 h 30** le mardi 20 octobre 2026, comme indiqué dans le brief. Les retards (« +3 h ») et les délais (« dans 50 min ») sont calculés à partir de cette heure. En production, il suffira de la remplacer par l'heure réelle.
2. **Données utilisées telles quelles.** Le statut « En retard » vient du fichier ; l'écran ne le recalcule pas. À 10 h 30, aucune intervention « À faire » n'a d'ailleurs déjà dépassé son heure prévue.
3. **La « prochaine intervention » d'un technicien** est sa première intervention « À faire » dans l'ordre des heures prévues. Les interventions en retard sont affichées à part, juste en dessous, et ne prennent pas automatiquement sa place. D'après les notes, elles sont bloquées (pièce manquante, accès refusé) ou le technicien a été retenu ailleurs : décider de les replacer revient au chef d'équipe. Si vous préférez qu'une intervention en retard devienne automatiquement la prochaine, c'est un réglage simple à modifier.
4. **« Urgent » = priorité haute et non terminée.** Une note qui signale un danger pour des personnes (« personne à l'intérieur », « pompiers ») est en plus écrite en rouge et en gras. C'est le cas de INT-2611, au quai Claude-Arnaud (Théo).
5. **Source des données** : servie par un serveur web, la page lit le fichier `interventions.csv` placé à côté d'elle. Si ce fichier manque ou que le serveur répond en erreur, l'écran « données non chargées » s'affiche (testé). Ouverte directement depuis le disque, la page utilise une copie des 40 lignes intégrée au fichier, car les navigateurs interdisent dans ce cas la lecture d'un fichier voisin.
6. **Pas de mise à jour des statuts depuis l'écran** : le brief demande un écran de suivi, pas de saisie. Pas non plus de numéro de téléphone pour Nathalie Roux, car le brief n'en donne pas. Il est conseillé d'en ajouter un dans les messages d'erreur.

## Deux points relevés dans les données, à vérifier de votre côté

- **Sophie Lambert** est sur un entretien de priorité basse (INT-2613, école) alors qu'une panne de priorité haute avec appareil à l'arrêt, dans une autre école (INT-2604, prévue à 8 h 25), est en retard. L'écran fait bien apparaître ce cas, mais l'arbitrage revient à Nathalie Roux.
- **INT-2605** est indiquée « Terminée », mais sa note dit encore « Pièce reçue, pose prévue ». La note n'a peut-être pas été mise à jour.

## Fichiers produits

- `index.html` : l'écran de suivi, en un seul fichier (styles, script et copie des données intégrés).
- `reponse.md` : ce message.
- `interventions.csv` : non modifié. Il est lu par la page quand celle-ci est servie par un serveur web.
