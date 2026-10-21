Bonjour,

Voici le parcours en ligne pour changer de formule ou résilier un contrat santé, dans l'espace adhérent de la Mutuelle des Trois Rivières. Tout est dans un seul fichier, **index.html**. Il s'ouvre dans n'importe quel navigateur, sans connexion ni installation.

## Comment le parcourir

- **En prototype cliquable** : ouvrez index.html. Vous êtes connecté comme Camille Moreau et vous pouvez faire les deux démarches de bout en bout. Les erreurs de saisie se déclenchent vraiment, par exemple en confirmant sans cocher la case ou en vidant le champ e-mail.
- **Écran par écran** : la barre sombre « Maquette » en haut de la page sert à la revue et ne fait pas partie du site. Son menu vous amène directement à n'importe quel écran ou état.
- **Sur une planche** : le lien « Voir tous les écrans sur une planche » affiche les 15 écrans et états les uns sous les autres, chacun avec une courte note. C'est le plus pratique pour une relecture ou une impression.

## Ce que contient le parcours

**Point de départ : Mon contrat santé.** On y trouve la formule, les personnes couvertes, la cotisation de 81,70 € (61,90 € + 19,80 €) et le prélèvement. « Changer de formule » et « Résilier mon contrat » sont au même niveau, aucun des deux n'est caché.

**Changer de formule** (2 étapes, puis confirmation)
1. Comparer : tableau Confort / Essentielle, avec en tête le total pour le foyer (81,70 € ou 50,50 €, soit 31,20 € de moins par mois). Sous le tableau, les trois règles à connaître : effet le 1er du mois suivant, mois en cours au tarif actuel, une fois par année civile.
2. Vérifier et confirmer : date d'effet, ce qu'on paie ce mois-ci et à partir du mois prochain, la liste des garanties qui baissent pour Camille et Léo, et un avertissement sur la règle « une fois par année civile ». Une case à cocher sert d'accord explicite.
   - État d'erreur : si on confirme sans cocher la case, un résumé d'erreur s'affiche en haut de page et un message apparaît sous le champ.
3. Confirmation, puis la page « Mon contrat » qui affiche le changement programmé.
- Variante « changement déjà utilisé cette année » : écran qui explique le refus et indique la date à partir de laquelle la demande redevient possible. **Il ne s'applique pas à Camille**, qui est en Confort depuis 2024, mais il faut le prévoir pour les autres adhérents.

**Résilier** (3 étapes, puis confirmation ou annulation)
1. Ce qu'il faut savoir : date de fin calculée, fin de couverture pour les deux bénéficiaires, aucuns frais, aucun justificatif demandé. Un encadré rappelle la formule Essentielle et son prix, avec un lien. Il ne bloque pas : depuis la comparaison, un lien « Reprendre ma résiliation » ramène à la démarche.
2. Questionnaire facultatif sur la raison du départ (prix, garanties, déménagement, autre, avec un texte libre possible). Les boutons « Continuer » et « Passer cette question » ont le même poids. Il est écrit clairement que la réponse ne change rien à la demande.
3. Vérifier et confirmer : récapitulatif, adresse e-mail pour l'accusé de réception, puis le choix explicite **« Confirmer et envoyer la résiliation »** ou **« Annuler la résiliation »**.
   - État d'erreur : adresse e-mail vide ou incomplète.
4. Demande envoyée : date de fin, référence, mention de l'accusé de réception envoyé par e-mail avec la date d'effet, et la suite. Si l'adhérent annule, un écran confirme qu'aucune demande n'est partie et que le contrat continue.

## Choix de conception

- **Les dates sont calculées à partir du jour de la demande**, comme sur le vrai site. Pour une demande faite aujourd'hui, 21 octobre 2026, le changement de formule prend effet le 1er novembre 2026 et la résiliation le 21 novembre 2026. Pour simuler un autre jour, ajoutez `?date=AAAA-MM-JJ` à l'adresse, par exemple `index.html?date=2027-01-31`. Une demande faite un 31 janvier prend effet le dernier jour de février.
- **Les montants sont toujours donnés pour le foyer** (Camille + Léo), parce que c'est ce que l'adhérent paie réellement.
- **Aucune pression pour retenir l'adhérent** : le rappel du changement de formule n'apparaît qu'une fois, le questionnaire peut être ignoré, et le bouton de confirmation de la résiliation est le bouton principal de l'écran.
- **Accessibilité** :
  - titres de page mis à jour à chaque étape (précédés de « Erreur : » quand il y en a une) ;
  - focus placé sur le titre ou sur le résumé d'erreurs ;
  - liens du résumé vers les champs concernés ;
  - étape en cours annoncée ;
  - les erreurs ne reposent pas sur la couleur seule ;
  - boutons d'au moins 48 px ;
  - mise en page vérifiée sur mobile (390 px) : sur petit écran, le tableau de comparaison passe en lignes empilées.
- Après un envoi, le bouton « Retour » du navigateur ne permet pas de renvoyer la même demande.

## Hypothèses à valider de votre côté

Le brief ne tranchait pas ces points. J'ai fait un choix raisonnable pour chacun et je le signale :

1. **Cotisations pendant le préavis de résiliation** : j'écris que l'adhérent reste couvert et que les cotisations restent dues jusqu'à la date de fin. Le montant du dernier prélèvement (au prorata ou non) n'est pas précisé. À confirmer.
2. **Prélèvement du 5** : j'ai supposé qu'il paie le mois en cours. Le premier prélèvement au tarif Essentielle est donc celui du 5 novembre.
3. **« Une fois par année civile »** : je compte l'année de la demande. Pour une demande faite en décembre, avec effet en janvier, il faut décider quelle année compte.
4. **Adresse e-mail de Camille** : elle n'était pas fournie. J'ai mis une adresse fictive, `camille.moreau@courriel.example`, modifiable dans le formulaire.
5. **Confirmation par e-mail du changement de formule** : je l'ai prévue par cohérence. Le brief ne l'impose que pour la résiliation.
6. **Revenir sur une demande déjà envoyée** : les règles n'en parlent pas. Les écrans renvoient vers le service adhérents plutôt que de promettre une annulation en ligne.
7. **Référence de demande** : format inventé (R-AAAAMMJJ-xxxxx), à remplacer par le vôtre.
8. **Périmètre de « modifier »** : j'ai traité le changement de formule, seul cas pour lequel le brief donne des règles. Les autres modifications (bénéficiaires, coordonnées bancaires) ne sont pas maquettées, ni le passage d'Essentielle à Confort, qui ne concerne pas Camille.
9. **Typographie** : j'ai utilisé les polices système, faute de charte graphique fournie. Le logo est provisoire.

Je reste disponible pour ajuster les textes ou ajouter les écrans manquants si vous le souhaitez.

---

**Compte rendu : fichiers produits**
- `index.html` : prototype cliquable et planche des 15 écrans et états (fichier unique, sans dépendance externe)
- `reponse.md` : cette réponse
