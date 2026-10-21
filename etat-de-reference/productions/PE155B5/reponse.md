Bonjour,

La page de l'article « Le pont de la Clé rouvre, cent quinze ans après sa première traversée » est prête : `index.html`. C'est un fichier unique et autonome, sans appel réseau. Les polices sont intégrées au fichier, et il s'ouvre aussi bien hors ligne que sur un serveur.

## Ce que contient la page

- **Le texte, tel quel.** Le titre, le chapeau, les 14 paragraphes, la citation, la légende et l'encadré sont repris mot pour mot. Un script a comparé la page au brief pour s'assurer qu'aucune phrase n'a été coupée ni modifiée. Je n'ai ajouté aucun intertitre, puisque ce serait de l'écriture.
- **L'en-tête de l'article.** On y trouve la rubrique Ville, le titre, le chapeau, puis la signature : « Par Julien Arnaud », publié le mercredi 21 octobre 2026, 6 min de lecture.
- **Les chiffres clés.** « 4,2 millions d'euros » est placé à côté du paragraphe sur le choix de la rénovation. Une petite barre montre la part de la région (1,6 sur 4,2, soit 38 %). « 9 300 traversées par jour » est placé à côté du paragraphe sur les cyclistes. Sur grand écran, les deux chiffres sont dans la marge, à la hauteur du paragraphe qui en parle. Sur tablette et sur mobile, ils s'insèrent dans le texte.
- **La citation d'Agnès Vidal.** Elle est mise en exergue juste avant le paragraphe sur la clé de voûte, car elle répond au passage sur les garde-corps refaits d'après le dessin de 1911.
- **La photo d'archive.** Elle n'a pas été fournie, donc la page montre un emplacement réservé, clairement marqué « Photo d'archive à intégrer », avec la légende complète. Il est placé après le paragraphe sur l'histoire du pont (1909-1911, la passerelle en bois). Pour mettre la photo, il suffit de remplacer le bloc `.photo-frame` par une balise `<img>` au format 16:9 ou plus haut. La légende reste en place.
- **L'encadré « Ce qui change pour la circulation ».** Il ferme l'article, avec une icône pour chacun des quatre points.

## Partis pris graphiques

- Le texte est en Newsreader, un caractère de presse, avec des lignes de 65 à 70 signes, une lettrine et la césure en français. Les éléments d'interface (signature, légendes, chiffres, encadré) sont en Public Sans. Les deux polices sont sous licence libre (SIL OFL).
- La couleur d'accent est un ocre, en écho à la pierre que le nettoyage a révélée. Le bleu-vert de l'encadré évoque l'Ardière.
- Le bandeau du média reste fixé en haut de l'écran, avec une fine barre qui indique la progression dans la lecture.
- La page fonctionne en mode sombre (elle suit le réglage du système), à toutes les largeurs (vérifiée en 390, 1024 et 1440 px, sans défilement horizontal) et à l'impression.
- J'ai soigné l'accessibilité et le référencement : balises sémantiques (article, figure, aside, time), lien d'évitement, texte alternatif pour l'emplacement de la photo, métadonnées de partage (Open Graph) et balisage schema.org NewsArticle.

## Hypothèses à valider

1. **Typographie.** J'ai appliqué les règles françaises : apostrophes typographiques (’), espaces insécables devant « : ; ? ! », à l'intérieur des guillemets, dans « 9 300 » et entre un nombre et son unité. Pour moi, ce n'est pas de la réécriture, mais je préfère vous le signaler.
2. **Habillage du site.** Le bandeau et le pied de page sont volontairement sobres : nom du média, « Quotidien en ligne », rubrique et date. Je n'ai pas inventé de menu, d'articles liés ni de boutons de partage. Votre gabarit habituel pourra les ajouter.
3. **Liens.** Le nom du média et la rubrique pointent vers `#`. Il faut les relier aux bonnes adresses de votre site.
4. **Libellés des chiffres clés.** J'ai simplement mis une majuscule au début (« Coût total des travaux… »). Les mots « Chiffre clé » et la légende de la barre (« Région 1,6 M€ / Total 4,2 M€ ») ne font pas partie du texte de l'article : ce sont des éléments de mise en page.
5. **Date.** L'article ne donne pas la date exacte de « samedi ». Je l'ai laissée telle quelle.

Bonne publication,

---

**Fichiers produits**
- `index.html` : la page de l'article, autonome (CSS, polices et petit script intégrés)
- `reponse.md` : ce message
