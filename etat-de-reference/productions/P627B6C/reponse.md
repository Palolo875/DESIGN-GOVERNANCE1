# Parcours « Modifier ou résilier mon contrat santé » : Mutuelle des Trois Rivières

Bonjour,

Voici la maquette du parcours, dans `index.html`. Ouvrez le fichier dans un navigateur. On peut faire le parcours en cliquant, comme le ferait Camille Moreau, ou ouvrir directement chacun des 12 écrans et états avec le menu **« Écran »** du bandeau gris « Maquette » en haut de la page. Ce bandeau ne fait pas partie du produit.

## Ce que j'ai fait

Le parcours part de la page **« Mon contrat santé »** de l'espace adhérent. Sur cette page, **« Changer de formule »** et **« Résilier mon contrat »** apparaissent côte à côte, avec le même poids. Chaque parcours tient en **deux étapes et une confirmation**. Sur chaque étape, un **échéancier daté** (« Ce qui va se passer ») indique ce qui arrive, à quelle date et pour qui : Camille, mais aussi Léo.

| Écran | Contenu | Accès direct |
|---|---|---|
| 0 · Mon contrat santé | Formule, bénéficiaires, cotisation (81,70 €), les deux options à égalité | `index.html#contrat` |
| F1 · Comparer les formules | Tableau Confort / Essentielle pour le foyer (81,70 € → 50,50 €, soit 31,20 € de moins par mois), règle « une fois par année civile » | `#formule-1` |
| F2 · Vérifier et confirmer | Récapitulatif, ce qu'on perd (chambre particulière, médecines douces), octobre dû au tarif Confort, adresse de confirmation modifiable, **Confirmer / Annuler** | `#formule-2` |
| F2 · Erreur de saisie | Adresse courriel incomplète : résumé en haut, message sous le champ, saisie conservée | `#formule-2-erreur` |
| F3 · Changement enregistré | Effet le 1er novembre 2026, confirmation envoyée | `#formule-ok` |
| F · Indisponible | Cas où la règle annuelle bloque le passage à Essentielle : date de réouverture et autres options | `#formule-indispo` |
| R1 · Votre résiliation | Sans frais, sans justificatif, fin du contrat le 21 novembre 2026, questionnaire **facultatif** (prix, garanties, déménagement, autre), rappel discret du changement de formule | `#resiliation-1` |
| R2 · Confirmer ou annuler | Récapitulatif, adresse de l'accusé de réception, **« Confirmer la résiliation »** et **« Annuler la résiliation »** de même taille | `#resiliation-2` |
| R2 · Erreur de saisie | Adresse de l'accusé de réception incomplète | `#resiliation-2-erreur` |
| R2 · Échec de l'envoi | « Votre demande n'a pas été transmise : votre contrat continue », réponses conservées, bouton « Réessayer l'envoi » | `#resiliation-2-echec` |
| R3 · Demande envoyée | Accusé de réception envoyé par courriel avec la date d'effet, référence de la demande | `#resiliation-ok` |
| R3 · Résiliation annulée | « Aucune demande n'a été envoyée. Rien ne change pour vous et Léo. » | `#resiliation-annulee` |

Les interactions sont réelles :
- cocher « Autre raison » ouvre un champ libre ;
- les raisons choisies sont reprises dans le récapitulatif ;
- l'adresse courriel est vérifiée ;
- l'envoi affiche « Envoi en cours… » ;
- après l'envoi, le bouton Retour du navigateur ne ramène pas à l'écran de confirmation, ce qui évite un double envoi.

Les montants et les dates sont calculés à partir des tarifs et des règles du brief, pour une date simulée au **mercredi 21 octobre 2026**.

## Pourquoi

**L'idée :** une personne qui modifie ou quitte sa mutuelle veut savoir **ce qui change, quand, et pour qui**, avant d'envoyer quoi que ce soit. C'est pourquoi l'échéancier daté organise chaque étape. Il est à droite sur ordinateur. Sur mobile, il s'insère avant les boutons.

**Pour la résiliation, la sortie est aussi simple que l'entrée :**
- Deux clics depuis la page du contrat.
- Le changement de formule est rappelé une seule fois, en texte discret sous les boutons. Pas de fenêtre ni d'étape en plus.
- Aucune formule culpabilisante, aucune case cochée d'avance.
- Le questionnaire dit clairement qu'il est facultatif et qu'il ne change rien à la demande.
- « Annuler » est aussi visible que « Confirmer ».

Ce sont les pratiques que les autorités sanctionnent aujourd'hui dans les parcours de résiliation.

**Ton et lisibilité :**
- Les titres sont en Source Serif 4, une voix de « courrier » posée pour un moment engageant.
- Le texte est en Atkinson Hyperlegible Next, une police conçue pour la lisibilité, utile pour un public d'adhérents de tout âge.
- Le corps de texte fait 18 px.
- Les contrastes ont été contrôlés.
- Chaque information importante passe aussi par une icône ou un texte, jamais par la couleur seule.

**L'alternative écartée :** un parcours classique où chaque étape est un formulaire avec un stepper numéroté et une coche verte à la fin. Je l'ai écartée parce qu'il ne montre pas les conséquences datées. Or ce sont ces dates (1er novembre, 21 novembre, prélèvement du 5) qui font hésiter ou rassurent.

**Ce que la maquette permet de décider :**
- la place et le ton du rappel du changement de formule ;
- le contenu du questionnaire ;
- le niveau de détail de l'échéancier ;
- les libellés des boutons de la confirmation.

## Hypothèses que j'ai faites (à valider)

1. **Date du jour simulée : 21 octobre 2026.** Les dates d'effet en découlent :
   - changement de formule le **1er novembre 2026** (1er du mois suivant) ;
   - fin du contrat le **21 novembre 2026** (un mois après la réception).
2. **La demande en ligne est « reçue » au moment de l'envoi.** C'est cette date qui fait partir le délai d'un mois.
3. **Le prélèvement du 5 couvre le mois en cours.** J'ai donc indiqué un premier prélèvement à 50,50 € le 5 novembre après un changement de formule. Ce point est marqué « à confirmer » dans l'interface.
4. **Le prélèvement de novembre en cas de résiliation** (mois partiel, prorata ou non) n'est pas défini par le brief. J'ai seulement écrit que la cotisation reste due jusqu'à la fin du contrat, avec la mention « montant à confirmer ». Je n'ai inventé aucun montant.
5. **Camille n'a pas encore utilisé en 2026 son passage de Confort à Essentielle.** L'écran « Indisponible » montre le cas contraire, pour un autre adhérent.
6. **Le changement de formule concerne tout le foyer.** Camille et Léo passent ensemble à la même formule.
7. **Valeurs d'exemple**, marquées « exemple » à l'écran ou à remplacer :
   - l'adresse courriel de Camille (`camille.moreau@courriel.example`), qui n'était pas fournie ;
   - les références de demande (`RES-2026-58817-01`, `MOD-2026-58817-01`) ;
   - le mot-marque « Trois Rivières », provisoire, faute de logo.
8. L'écran de départ « Mon contrat santé » est une version minimale de l'espace adhérent. Je n'ai pas inventé le reste de la navigation.

## Ce qui manque pour la vraie version

- **Les règles de cotisation en cas de résiliation** (dernier prélèvement, prorata, remboursement éventuel), pour remplacer les mentions « à confirmer ».
- **Une relecture juridique des libellés**, surtout « Confirmez-vous la résiliation ? », l'accusé de réception et la date d'effet. Il faut aussi trancher si l'adhérent peut revenir sur une demande déjà envoyée. Je ne l'ai pas promis.
- **Le contenu exact du courriel d'accusé de réception** : je peux le maquetter aussi.
- **Votre identité visuelle** (logo, couleurs, police). La palette actuelle (encre bleu-vert, dates en ocre, fond papier) est une proposition.
- **Un test avec de vrais adhérents.** J'ai vérifié la maquette automatiquement à 390, 768 et 1 440 px de large :
  - pas de débordement ;
  - contrastes AA ;
  - parcours clavier et focus visible ;
  - taille des cibles ;
  - montants et dates recalculés.

  J'ai aussi déroulé l'erreur, sa correction puis l'envoi. Cela ne remplace pas un essai avec des personnes. Le nom accessible des contrôles est en place, mais je ne l'ai pas validé avec un lecteur d'écran.
- Pas de mode sombre ni de version anglaise dans cette maquette.

## La suite

1. **Valider ou réorienter la proposition**, surtout trois points :
   - la place du rappel « changer de formule » ;
   - le questionnaire facultatif ;
   - les libellés « Confirmer la résiliation / Annuler la résiliation ».

   Ensuite, je peux décliner l'accusé de réception par courriel et l'état « demande en cours » dans l'espace adhérent pendant le mois de préavis.
2. **Organiser un test court**, par exemple 5 adhérents dont 2 de plus de 60 ans, sur deux tâches : « passez à la formule la moins chère », puis « résiliez votre contrat ». Il me faudrait vos réponses aux points 3 et 4 des hypothèses avant ce test.

---

## Fichiers produits

- `index.html` : la maquette interactive (12 écrans et états), avec une courte note de travail en en-tête
- `fonts/atkinson-next-latin.woff2` : police du texte (Atkinson Hyperlegible Next, licence SIL OFL)
- `fonts/source-serif-4-latin.woff2` : police des titres (Source Serif 4, licence SIL OFL)
- `fonts/OFL-atkinson-hyperlegible-next.txt` et `fonts/OFL-source-serif-4.txt` : les licences des polices
- `reponse.md` : ce message
