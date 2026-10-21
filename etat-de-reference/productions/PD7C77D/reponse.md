Bonjour,

La page de votre saison 2026-2027 est prête : `index.html`. Elle fonctionne hors ligne. La seule ressource dont elle a besoin est la police de titres, rangée dans le dossier `fonts/` juste à côté.

## Ce que contient la page

- **Une ouverture** qui donne l'essentiel en un coup d'œil : la saison, le prix unique de 14 €, le tarif réduit et un bouton vers la billetterie. Un bandeau liste aussi les six dates ; chacune renvoie au spectacle correspondant.
- **Le programme** : les six spectacles dans l'ordre chronologique. Pour chacun, vous trouverez les dates et les horaires, le genre, la durée, l'âge conseillé, votre texte et un bouton « Réserver ». Pour la Nuit de la parole libre, les modalités d'inscription sont mises en avant dans un encadré.
- **Tarifs et billetterie** : 14 € et 7 € (avec justificatif). Une phrase précise que les places se réservent sur le site externe et non sur la page.
- **Infos pratiques** : adresse, ouverture des portes, bar, salle (180 places en gradin, accès de plain-pied, boucle magnétique) et contact. L'e-mail et le téléphone sont cliquables.

J'ai repris vos textes tels quels, sans rien ajouter sur le fond. Je n'ai pas mis de photos, d'artistes ni de mentions qui ne figuraient pas dans votre brief. J'ai vérifié les jours de la semaine de toutes les dates : ils correspondent au calendrier.

## Hypothèses que j'ai faites

1. **Un seul lien de billetterie.** Vous n'avez donné qu'une adresse. Tous les boutons « Réserver » y renvoient donc et s'ouvrent dans un nouvel onglet. Si chaque spectacle a sa propre page sur la billetterie, il suffira de remplacer le lien dans chaque bouton.
2. **Sans visuels.** En l'absence d'images fournies, l'identité repose sur la typographie et sur une couleur « rouge rideau ». Si vous avez des photos ou des affiches, chaque spectacle peut accueillir une image.
3. **Repère « Prochain spectacle ».** Un petit script compare les dates à la date du jour. Il signale le prochain spectacle et estompe ceux qui sont passés, en retirant leur bouton de réservation. La page reste donc juste toute la saison sans retouche. Si JavaScript est désactivé, tout reste affiché normalement.
4. **Petits ajouts de liaison**, comme le prévoyait le brief : les titres de section, les libellés des boutons, la phrase d'accroche (qui résume vos six spectacles), « Lyon 7e » (déduit du code postal) et la précision « pour les personnes malentendantes » après « boucle magnétique ».
5. **L'âge conseillé** n'est pas indiqué pour le Quatuor Lumen. Je n'en ai pas inventé, et la page n'affiche rien à cet endroit.

## Qualité et accessibilité

- La mise en page s'adapte aux ordinateurs, aux tablettes et aux téléphones. Je l'ai vérifiée en 1366, 800 et 375 px de large, sans défilement horizontal.
- La page est structurée pour les lecteurs d'écran : titres hiérarchisés, lien d'évitement « Aller au programme », dates balisées. Chaque bouton « Réserver » nomme le spectacle et annonce qu'il ouvre un site externe. Le contour de focus est visible et les contrastes sont suffisants.
- La version imprimée est épurée : la navigation et les boutons sont retirés, et l'adresse de la billetterie s'imprime en toutes lettres.
- Des données structurées (schema.org) décrivent le lieu et les six spectacles pour les moteurs de recherche.

## À vérifier avant la mise en ligne

- Remplacez les adresses fictives : billetterie, e-mail, téléphone.
- Dans les données structurées en bas du fichier, les dates de début sont exactes. Pour les spectacles joués plusieurs jours, seule la première représentation porte une heure : c'est simplifié, mais suffisant pour le référencement.
- La police Fraunces est sous licence libre (SIL OFL). Sa licence est jointe dans `fonts/OFL.txt` et doit rester à côté des fichiers de police.

Bien à vous.

---

### Fichiers produits

- `index.html` : la page de saison (styles et scripts intégrés)
- `fonts/fraunces.woff2` : police de titres (romain)
- `fonts/fraunces-italic.woff2` : police de titres (italique)
- `fonts/OFL.txt` : licence de la police
- `reponse.md` : ce message
