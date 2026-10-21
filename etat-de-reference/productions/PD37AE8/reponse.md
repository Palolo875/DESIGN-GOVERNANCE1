# Page article : « Le pont de la Clé rouvre, cent quinze ans après sa première traversée »

Bonjour,

La page de l'article est prête. C'est le fichier `index.html`, une page HTML autonome : elle tient en un seul fichier, sans appel réseau, et la police est intégrée. On peut l'ouvrir telle quelle dans un navigateur ou l'héberger n'importe où.

## Ce que contient la page

- **En-tête du média** : L'Écho du Val, « Quotidien en ligne », avec la date du jour.
- **En-tête de l'article** : rubrique Ville, titre, chapeau, puis une ligne de signature (Par Julien Arnaud · Publié le mercredi 21 octobre 2026 · Lecture : 6 min).
- **Texte intégral** : les quatorze paragraphes, sans coupe ni réécriture, avec une lettrine sur le premier.
- **Les deux chiffres clés**, chacun dans un bloc mis en avant, juste après le paragraphe qui l'évoque :
  - **4,2 millions d'euros** après le paragraphe sur le choix de la rénovation ;
  - **9 300 traversées par jour** après le paragraphe sur les voies cyclables.

  Placés ainsi, ils rythment ce long texte au lieu d'être regroupés en tête.
- **La citation d'Agnès Vidal**, en grand, après le paragraphe sur la clé de voûte et les initiales des ouvriers. Elle répond directement à ce passage (« sans qu'on oublie qui l'a construit »).
- **L'emplacement de la photo d'archive**, avec sa légende et le crédit « Archives municipales », après le paragraphe qui raconte la construction de 1909-1911.
- **L'encadré « Ce qui change pour la circulation »** en fin d'article.

## Choix et hypothèses

1. **La photo n'a pas été fournie.** J'ai donc prévu un emplacement clairement signalé (« Photo d'archive à intégrer »), au format 3:2 et avec un dessin neutre de pont. Je n'ai pas fabriqué de fausse photo d'époque. Pour mettre la vraie photo, un commentaire dans le code indique la ligne à remplacer par une balise `<img>`, texte alternatif compris.
2. **Typographie française.** Le texte est mot pour mot celui que vous avez fourni. Je n'ai changé que la typographie :
   - apostrophes typographiques (’) ;
   - espaces insécables avant « : ; ? ! », à l'intérieur des guillemets et dans « 9 300 », « 30 km/h », « 1,80 m », etc.

   Ainsi, un guillemet ou une unité ne se retrouve jamais seul en début de ligne.
3. **Identité visuelle.** Je n'avais pas de charte pour L'Écho du Val, j'en ai donc proposé une sobre :
   - fond papier clair ;
   - police à empattements Source Serif 4, sous licence libre OFL et intégrée au fichier ;
   - une couleur d'accent ocre, qui rappelle la vraie couleur de la pierre du pont révélée par le nettoyage.

   Le logo n'est qu'un logotype en texte. Si vous avez une charte, il suffit de remplacer les quelques variables de couleur en tête du CSS.
4. **Les liens du site.** Le logo pointe vers « # ». Je n'ai pas ajouté de faux menu de navigation ni de faux boutons de partage, faute d'adresses réelles. Ils sont à brancher sur votre site.
5. **Confort de lecture** :
   - une fine barre de progression en haut de l'écran, désactivée si l'utilisateur a demandé à réduire les animations ;
   - un mode sombre automatique ;
   - une mise en page adaptée aux mobiles ;
   - une feuille de style pour l'impression.
6. **Référencement.** La page contient un titre, une description, des balises de partage (Open Graph) et des données structurées « NewsArticle ». Il manque l'image de partage, à ajouter quand la photo sera disponible.

## Vérifications faites

- Rendu contrôlé dans Chromium sur ordinateur (1280 px) et sur mobile (390 px), en mode clair et en mode sombre. Il n'y a pas de défilement horizontal.
- Une comparaison automatique confirme que tous les paragraphes, le titre, le chapeau, la citation, la légende et l'encadré figurent mot pour mot dans la page. Les seuls écarts sont les retouches typographiques décrites au point 2.

---

**Fichiers produits**

- `index.html` : la page de l'article, autonome (CSS, police et script intégrés).
- `reponse.md` : ce message.
