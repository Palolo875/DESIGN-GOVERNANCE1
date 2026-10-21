Bonjour,

Voici le parcours en ligne « Modifier ou résilier mon contrat santé » pour la Mutuelle des Trois Rivières. Il tient dans un seul fichier, **index.html**. On l'ouvre directement dans un navigateur, sans installation ni connexion.

## Comment le parcourir

- **Prototype cliquable** : ouvrez `index.html`. Vous arrivez sur la page « Mon contrat santé » de Camille Moreau, déjà connecté, et vous pouvez faire les deux parcours de bout en bout. Les saisies, les erreurs, l'envoi et l'annulation fonctionnent.
- **Barre « Maquette »** (bandeau sombre en haut, qui ne fait pas partie du site) : le menu « Aller à l'écran » ouvre directement chacun des 18 états. « Recommencer » remet la maquette à zéro.
- **Planche de tous les états** : le lien dans ce même bandeau (ou `index.html?vue=planche`) montre tous les écrans côte à côte, en largeur mobile, avec une courte légende pour chacun. Elle sert à la relecture ou à une présentation.

## Ce que contient le parcours

**Point de départ, « Mon contrat santé »** : formule, cotisation (81,70 € pour Camille et Léo), bénéficiaires et prélèvement. « Changer de formule » et « Résilier mon contrat » y sont présentés à égalité : la résiliation n'est pas cachée.

**Résiliation, en 3 étapes puis la confirmation**
1. *Conditions* : date de fin, personnes concernées, aucun frais, aucun justificatif à fournir, accusé de réception par courriel. Le rappel du changement de formule n'apparaît qu'à cet endroit. Il donne le chiffre utile (Essentielle à 50,50 €, soit 31,20 € de moins par mois) et ne bloque rien.
2. *Raison du départ* : le questionnaire est facultatif (prix, garanties, déménagement, autre). Un bouton « Passer cette question » est prévu, et la page précise que la réponse ne change rien à la demande.
3. *Vérification* : le récapitulatif, puis **« Confirmer la résiliation »** ou **« Annuler la résiliation »**. Rien n'est envoyé avant cette étape, ce que le parcours rappelle à chaque écran. Le lien « Quitter sans rien envoyer » reste disponible à toutes les étapes.
4. *Confirmation* : la date d'effet, la mention de l'accusé de réception envoyé par courriel et les conseils pour la suite. Ensuite, la page « Mon contrat » affiche la résiliation en cours.

**Changement de formule, en 2 étapes puis la confirmation**
1. *Comparatif Confort / Essentielle*, calculé pour Camille et Léo, avec chaque garantie qui baisse signalée par du texte et pas seulement par une couleur. Un encadré « Bon à savoir » donne la prise d'effet au 1er novembre, la cotisation d'octobre qui reste au tarif actuel et la règle « une fois par année civile ».
2. *Vérification* : la nouvelle cotisation, la liste des garanties perdues et l'avertissement sur la règle annuelle, puis les boutons Confirmer et Annuler.
3. *Confirmation*, puis la page « Mon contrat », qui affiche le changement prévu.

**États demandés et états ajoutés**
- Étape en cours : barre d'étapes et libellé « Étape 2 sur 3 : … ».
- Erreurs de saisie :
  - adresse courriel sans « @ » ou incomplète, sur les deux écrans de vérification ;
  - texte « Autre raison » trop long (300 caractères au maximum).
  
  Chaque erreur s'affiche dans un résumé en haut de page et sous le champ concerné, avec un exemple de saisie correcte.
- Confirmations : résiliation envoyée, changement enregistré, résiliation annulée, changement annulé.
- Autres états ajoutés :
  - « envoi impossible » (panne technique : rien n'est enregistré, on peut réessayer) ;
  - « passage à Essentielle déjà utilisé cette année ». Ce dernier est une variante pour un autre adhérent, puisque Camille Moreau n'est pas dans ce cas.

L'accessibilité a été traitée dès la maquette :
- les champs ont de vrais libellés et les erreurs sont reliées à leur champ ;
- à chaque changement d'écran, le focus va au titre ou au résumé d'erreurs ;
- les contrastes sont suffisants et les boutons font au moins 48 px de haut ;
- la typographie française est respectée (espaces insécables).

Toutes les pages s'adaptent au mobile.

## Hypothèses que j'ai faites (à valider)

1. **Date du scénario : la demande est faite le mercredi 21 octobre 2026.** On en tire :
   - changement de formule effectif le **1er novembre 2026** ;
   - résiliation effective le **21 novembre 2026**, soit un mois après la réception ;
   - une demande en ligne est considérée comme reçue le jour même de l'envoi.
   
   Les dates sont fixées dans la maquette. En production, elles seront calculées.
2. **« Modifier le contrat » veut dire changer de formule.** Le brief ne donne de règles que pour cela. La seule modification possible pour Camille est donc le passage de Confort à Essentielle. La formule s'applique à tout le contrat, donc aussi à Léo.
3. **Adresse courriel de l'adhérent** : elle n'était pas fournie. J'ai mis une adresse fictive, `camille.moreau@courriel.example`, présentée comme l'adresse déjà connue. Elle peut être modifiée au moment de confirmer : c'est ce qui crée l'état d'erreur de saisie.
4. **Confirmation par courriel du changement de formule** : la règle ne le prévoit que pour la résiliation. Je l'ai ajoutée par cohérence ; elle peut être retirée.
5. **Prélèvement** : j'ai considéré que celui du 5 de chaque mois correspond à la cotisation du mois. La nouvelle cotisation de 50,50 € s'applique donc « à partir de novembre 2026 ».
6. Les liens de navigation de l'espace adhérent (Accueil, Mes remboursements…) ne servent qu'au décor et ne sont pas cliquables.

## Questions à trancher avec la mutuelle avant la mise en ligne

- **Dernière cotisation en cas de résiliation** : que devient le prélèvement du 5 novembre pour un contrat qui se termine le 21 novembre (prorata ou mois entier) ? Je n'ai rien affiché à ce sujet pour ne pas inventer une règle. C'est pourtant la première question que se posera l'adhérent.
- **« Un mois après »** : quelle date retenir pour une demande reçue le 31 janvier ? Le 28 février, le 1er mars ?
- **« Une fois par année civile »** : compte-t-on l'année de la demande ou celle de la prise d'effet ? Une demande faite le 15 décembre 2026 prend effet le 1er janvier 2027.
- **Changer d'avis après l'envoi** : peut-on retirer une résiliation avant sa date d'effet ? J'ai seulement renvoyé vers le service adhérents, sans rien promettre.
- **Destination des réponses au questionnaire** : à qui sont-elles transmises, et pour quel usage ? La réponse sert à la mention RGPD à ajouter sous la question.

## Fichiers produits

- `index.html` : le parcours complet, avec le prototype interactif, l'accès direct aux 18 états et la planche de tous les états (`index.html?vue=planche`).
- `reponse.md` : ce message.
