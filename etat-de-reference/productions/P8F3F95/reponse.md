# Écran de suivi des interventions : Lyon Sud, mardi 20 octobre 2026

Bonjour,

Voici l’écran de suivi des interventions du jour : `index.html`. C’est un seul fichier qui s’ouvre directement dans un navigateur, sans connexion. Les quarante interventions de `interventions.csv` y sont intégrées sans aucune modification, ainsi que les polices.

## Ce que j’ai fait

L’écran sert à répondre à une question : **que faut-il faire maintenant ?** La journée est coupée par une ligne bien visible, **« 10 h 30 · maintenant »**. Au-dessus de la liste, un panneau change selon la personne choisie.

- **Pour Nathalie Roux (« Toute l’équipe », sur écran de bureau)**, le panneau « À traiter maintenant » montre d’un coup d’œil :
  - l’urgence en cours, mise en avant en rouge : INT-2611, quai Claude-Arnaud, cabine bloquée avec une personne à l’intérieur ;
  - les **4 interventions en retard**, les urgentes d’abord, avec la durée du retard (« Retard 2 h 35 ») et le motif tiré de la note (pièce manquante, accès refusé, technicien retenu) ;
  - les **6 urgences encore à faire**, dans l’ordre de l’heure ;
  - une carte par technicien : ce qu’il fait en ce moment, sa prochaine intervention (« 10:45, dans 15 min »), ses retards et ce qu’il lui reste. Un appui sur la carte ouvre sa journée.
- **Pour Karim, Sophie et Théo (au téléphone)**, il suffit d’appuyer sur son nom. Le téléphone s’en souvient pour les fois suivantes. Le haut de l’écran affiche alors :
  - **sa prochaine intervention** : l’heure en grand, le temps restant, l’adresse en gros caractères, la note et un gros bouton **« Itinéraire vers cette adresse »** ;
  - en dessous, son intervention en cours et ses retards à replanifier.
- **Les deux filtres demandés** (technicien et statut) sont de gros boutons, d’au moins 52 px de haut, utilisables avec des gants. Chaque bouton de statut indique son nombre, et ce nombre suit le technicien choisi.
- **La liste du jour** est triée par heure. Chaque ligne affiche le statut en toutes lettres avec une icône et une couleur, donc il se lit même sans voir la couleur. La mention « Urgent » est sur fond jaune. Selon le cas, la ligne indique aussi le retard (« +3 h ») ou le temps restant (« dans 1 h 10 »). Pour que la ligne de 10 h 30 arrive vite, les interventions terminées sont regroupées en une seule ligne qu’on peut déplier.
- **Les états prévus :**
  - **Aucune intervention pour un filtre** (par exemple Karim + En retard) : un message l’explique, rappelle sa journée (« 14 interventions : 1 en cours, 10 à faire, 3 terminées ») et propose « Afficher tous les statuts ».
  - **Données qui ne se chargent pas** : un message clair et un bouton « Réessayer ». Si une liste a déjà été enregistrée sur l’appareil, on peut l’afficher, avec un bandeau jaune qui indique qu’elle peut avoir changé. C’est utile en local machinerie ou en sous-sol, où le réseau manque souvent.
  - **Chargement** : les filtres sont désactivés et la place de la liste est réservée.

  Pour les voir, utilisez les liens en bas de page (« Aperçu des états »), ou ajoutez `?etat=chargement`, `?etat=erreur` ou `?etat=horsligne` à l’adresse.
- L’écran passe automatiquement en **thème sombre** si l’appareil est réglé ainsi.

## Pourquoi

- J’ai écarté le tableau de bord classique, avec des tuiles de chiffres et un tableau à dix colonnes. Ce format est lisible au bureau mais inutilisable sur un téléphone, avec des gants, entre deux interventions. Les chiffres sont présents, mais toujours à côté de ce qu’il faut faire (adresse, heure, motif).
- La police (Atkinson Hyperlegible) a été conçue pour la lisibilité. Elle distingue nettement 0 et O, 1, l et I, ce qui compte pour lire un numéro d’appareil comme « ASC-4006 » rapidement. Je l’ai comparée à une police plus étroite et plus dense (IBM Plex Condensed), qui faisait tenir plus de texte mais confondait davantage ces caractères.
- Le jaune est réservé à l’urgence et à l’heure de référence, comme les marquages de sécurité sur les seuils et les cuvettes d’ascenseur. Le rouge sert aux retards, le bleu à ce qui est en cours et le vert à ce qui est terminé.

## Hypothèses que j’ai faites (à confirmer)

1. **La « prochaine intervention » d’un technicien est sa première intervention « À faire » dans l’ordre de l’heure.** Ses interventions en retard ne remplacent pas la prochaine : elles sont affichées juste en dessous, « à replanifier avec Nathalie Roux ». La plupart sont bloquées (pièce manquante, accès refusé, technicien retenu), et l’ordre de reprise me semble être une décision de la cheffe d’équipe. Si vous préférez que la plus ancienne intervention en retard devienne la prochaine, la règle se change en une ligne.
2. **« Urgent » veut dire priorité Haute et pas encore terminée.**
3. **L’heure est figée à 10 h 30**, comme le demande le brief. Les durées (« dans 15 min », « retard 2 h 35 ») sont calculées à partir de cette heure.
4. **Le bouton Itinéraire** ouvre une recherche Google Maps avec l’adresse. Les adresses étant fictives, la carte ne trouvera pas toujours le lieu exact.
5. Je n’ai pas mis de **bouton d’appel** : aucun numéro de téléphone n’est fourni, et je n’en ai pas inventé.

**Points relevés dans les données, laissés tels quels :**
- la même rue apparaît avec deux codes postaux : impasse des Glycines en 69007 et 69008, et de même pour le boulevard des Tchécoslovaques-Sud ;
- INT-2605 est « Terminée » alors que sa note dit encore « Pièce reçue, pose prévue ».

## Ce qui manque pour la vraie version

- **Le branchement aux vraies données.** Pour l’instant, la liste est lue depuis la copie intégrée du CSV. Il faudra la remplacer par l’appel à votre outil de planification (un seul endroit du code, signalé), et utiliser l’heure réelle au lieu de 10 h 30.
- **Les numéros utiles**, si vous voulez des boutons d’appel : cheffe d’équipe, gardiens, bureau de contrôle.
- **Un essai sur le terrain** : un technicien, sur son téléphone, avec ses gants, en extérieur au soleil et en sous-sol. Les contrôles automatiques sont bons (contrastes, taille des boutons, navigation au clavier, pas de débordement en largeur sur mobile, tablette et bureau), mais ils ne remplacent pas cet essai.
- **Un avis de Nathalie Roux sur le panneau « équipe » au téléphone.** Il est long avant d’arriver à la liste. Si elle consulte aussi l’écran sur mobile, on peut replier les urgences à venir.

## La suite

1. Faites valider les hypothèses 1 et 2 par Nathalie Roux et un technicien.
2. Si elles tiennent, envoyez-moi le format de vos données réelles (export ou API) et les numéros utiles, et je branche l’écran.

---

### Compte rendu : fichiers produits

- `index.html` : l’écran livré, en un seul fichier (données et polices intégrées).
- `reponse.md` : ce message.
- `_atelier/index.src.html` : la source de l’écran, avant intégration des polices et des données.
- `_atelier/construire.py` : script qui assemble `index.html` à partir de la source, des polices et de `interventions.csv`.
- `_atelier/captures.py` : script qui produit les captures des différents états.
- `_atelier/fonts/next.woff2` et `_atelier/fonts/mono.woff2` : polices Atkinson Hyperlegible Next et Mono (licence SIL OFL 1.1).
- `_atelier/final/` : captures de contrôle :
  - écran à 390, 768 et 1440 px ;
  - Sophie au téléphone ;
  - Karim + En retard (aucune intervention) ;
  - échec du chargement, chargement, liste hors ligne ;
  - thème sombre ;
  - Théo sur écran de bureau ;
  - comparaison des deux polices.
- `_atelier/final.json` et `_atelier/final-equipe.json` : résultats des contrôles automatiques de rendu.
