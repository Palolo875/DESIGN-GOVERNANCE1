# Mutuelle des Trois Rivières : parcours « modifier ou résilier mon contrat santé »

Ouvrez `index.html` dans un navigateur. C'est une maquette cliquable de l'espace adhérent de Camille Moreau. Un bandeau sombre en haut, qui ne fait pas partie du produit, permet de passer d'un écran à l'autre (« Précédent / Suivant ») ou d'aller directement à l'un des **19 écrans et états** (« Tous les écrans »). Les parcours fonctionnent aussi pour de vrai : on peut saisir une adresse fausse, annuler, envoyer.

## Ce que j'ai fait

À partir de « Mon contrat santé », il y a deux parcours de même longueur : **changer de formule** (deux étapes, puis la confirmation) et **résilier** (deux étapes, puis l'accusé de réception). Chaque parcours a ses états :
- l'étape en cours ;
- l'erreur de saisie : courriel incomplet, la saisie est conservée et le message apparaît à côté du champ ;
- l'envoi en cours ;
- l'envoi impossible : rien n'est parti, avec un bouton pour réessayer ;
- la confirmation ;
- l'annulation ;
- le contrat après la demande : changement programmé, ou résiliation en cours ;
- un cas « changement indisponible », quand le passage Confort → Essentielle a déjà été utilisé dans l'année. Pour Camille, ce cas est hypothétique.

Le cœur de chaque étape est un **échéancier daté**. Avant de valider, l'adhérent voit ce qui change, à quelle date et pour quel montant, calculé pour son foyer. Par exemple, pour Camille et Léo : Essentielle coûte 50,50 € par mois au lieu de 81,70 €, soit 31,20 € de moins par mois. Le changement prend effet le 1er novembre 2026, et le premier prélèvement au nouveau tarif a lieu le 5 novembre. Une résiliation demandée aujourd'hui met fin au contrat le 21 novembre 2026.

## Pourquoi

- **La résiliation n'est pas plus difficile que le changement.** Les deux boutons ont le même poids sur la page du contrat. Le parcours n'est pas plus long. « Confirmer » et « Annuler, garder mon contrat » sont côte à côte, à la même taille, et la page dit clairement que rien ne part avant la confirmation. « Résilier » n'est pas en rouge : c'est un choix légitime, pas une erreur, et le rouge est réservé aux erreurs. On évite ainsi les pratiques de rétention trompeuses, que les autorités sanctionnent.
- **Le rappel du changement de formule** est un encadré discret sur la première étape de la résiliation, avec les deux prix et un lien. Il ne bloque rien.
- **Le questionnaire sur la raison du départ arrive après l'envoi**, sur l'accusé de réception, avec la mention « facultatif, ne change rien à votre résiliation ». C'est la seule façon de garantir qu'il ne freine ni ne fait pression. *Option écartée :* le poser avant la confirmation. On aurait plus de réponses, mais la résiliation serait plus longue et la question pourrait paraître servir à retenir l'adhérent.
- **L'accusé de réception est montré comme un document** (date de la demande, date d'effet, bénéficiaires, frais : aucun), le même que celui envoyé par courriel, plutôt qu'une simple coche verte.
- **Typographie :** les titres sont en Source Serif 4, pour un ton posé de courrier mutualiste. Le texte et les chiffres sont en Atkinson Hyperlegible Next, une police conçue pour les personnes malvoyantes : les chiffres et les identifiants (TR-204-58817) restent lisibles pour des adhérents de tous âges.
- **Couleurs :** un fond « papier » chaud, une couleur d'action « eau de rivière » et une couleur « limon », réservée au repère « aujourd'hui » et aux mentions à confirmer.

Vérifications faites : affichage à 390, 768 et 1440 px ; contrastes de texte (norme WCAG 2.2 AA, aucun en dessous) ; navigation au clavier et focus visible ; tailles des boutons ; aucune erreur de script. J'ai aussi joué les parcours complets dans un navigateur. Le contrôle automatique ne juge pas l'usage réel : cela demande un test avec des adhérents.

## Mes hypothèses (à valider)

1. **Date du jour : 21 octobre 2026.** La demande en ligne est considérée comme reçue le jour même. La résiliation prend donc effet le 21 novembre 2026 et le changement de formule le 1er novembre 2026.
2. **Le prélèvement du 5 couvre le mois en cours.** La cotisation d'octobre au tarif Confort est déjà prélevée, et le 5 novembre est le premier prélèvement au tarif Essentielle.
3. **« Modifier » veut dire changer de formule.** Les changements de bénéficiaires ou de compte bancaire ne font pas partie de ce parcours.
4. **La résiliation porte sur tout le contrat** (Camille et Léo), et l'écran le dit clairement.
5. **L'adresse électronique pour l'accusé de réception est pré-remplie et modifiable.** C'est le seul champ obligatoire, d'où l'erreur de saisie montrée.

## Ce qui manque pour la vraie version

- **Les règles du dernier mois :** la cotisation de novembre est-elle calculée au prorata jusqu'au 21 ? Son montant est marqué « à confirmer » dans l'échéancier.
- **Ce que vit un adhérent après l'envoi :** peut-il annuler une résiliation déjà envoyée ? Je ne l'ai pas proposé.
- **Contenus marqués « exemple » :** l'adresse électronique de Camille et les numéros de demande (CF-… / RS-…).
- **Le logo et la charte réelle :** le nom est écrit en texte, je n'ai pas inventé de logo.
- **Une relecture juridique** des libellés de résiliation et de l'accusé de réception.
- **La vraie technique :** l'envoi est simulé, sans serveur ni envoi de courriel.

## La suite

1. Me confirmer les règles du dernier mois et la date de réception. J'ajuste alors les montants et les dates.
2. Faire un test rapide avec 5 adhérents, dont des plus de 60 ans, sur deux tâches : « passer à Essentielle » et « résilier ». Il faudrait aussi un passage avec un lecteur d'écran.

---

**Fichiers produits**
- `index.html` : la maquette interactive, avec ses 19 écrans et états. Une courte trace de conception est en commentaire en tête du fichier.
- `fonts/source-serif-4.woff2`, `fonts/atkinson-hyperlegible-next.woff2` : les polices, hébergées avec la maquette.
- `fonts/OFL-source-serif-4.txt`, `fonts/OFL-atkinson-hyperlegible-next.txt` : leurs licences (SIL Open Font License).
- `reponse.md` : cette réponse.
