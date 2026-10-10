# Folio — essai Web mobile de tâche et de mouvement

Décision avant construction, 10 octobre 2026. Autorisation : poursuivre les corrections et la mise en pratique ; comparaison concurrentielle et anglais reportés.

Mode DIRECTION. Décision dominante : rendre le lien prestation → montant → brouillon immédiatement lisible dans une interface mobile. Risque : confondre un document en vitrine avec un instrument disponible, ou laisser une animation gouverner l’état. Preuve minimale : rendu, calcul, panneau interrompu, erreurs et récupération, clavier, contenu long, mouvement réduit et fallback. Arrêt : ces parcours sont exécutés, une relation de composition est comparée et les limites sont déclarées.

## Cible et moyens

Folio reprend la voix et l’objet documentaire de la proposition A d’U6, sans modifier cet original. Le public est une hypothèse : un indépendant qui prépare une facture de prestation. Ce prototype ne fournit ni conformité comptable, ni envoi, ni compte, ni réservation de service. Tous les noms et montants sont des exemples.

Promesse → objet → geste : comprendre son montant → prestation, quantité, tarif et total dans le même document → modifier la quantité ou ouvrir l’éditeur, puis télécharger un brouillon local. La première modification produit immédiatement un état correct ; le mouvement explique sa continuité.

Position : papier clair et encre sombre, voix documentaire à empattements et contrôles sans empattements. La silhouette mobile est un objet de travail vertical ; le desktop conserve un groupe d’action voisin du document. La direction ne cherche pas une nouvelle police ou une nouvelle palette pour prouver la variété. Familles retenues : Instrument Serif et Manrope, déjà fournies et licenciées ; pas d’asset extérieur ni de dépendance nouvelle.

Alternative plausible : une entrée éditoriale plus grande avant le document. La comparaison construite porte sur la hauteur et la masse de cette entrée, avec le même contenu et le même viewport ; elle vérifie la place restante pour le geste et le total. Un tableau de bord de revenus ne servirait pas de témoin à cette décision.

## Contrat de tâche

État initial rempli : 8 heures à 75 €, TVA illustrative de 20 %, soit 600 € HT et 720 € TTC. Le contrôle de quantité est visible ; l’éditeur permet de modifier client, prestation, quantité, tarif et TVA. Les données sont locales. La sauvegarde sur cet appareil est annoncée seulement si le stockage fonctionne ; sinon le brouillon est temporaire.

États à éprouver : ouverture, saisie, erreur liée au champ sans perte de texte, correction, application, annulation, modifications rapides, retour du focus, glissement de la poignée, annulation de pointeur, préférence de mouvement réduit, hauteur disponible réduite, contenu long, stockage absent et API d’animation absente. Le téléchargement produit un véritable fichier texte portant les limites du document.

Accessibilité visée dans le scope : contrôles natifs nommés, labels, erreurs textuelles, focus visible, boucle de focus du dialogue, Escape et bouton de fermeture, cibles de 44 pixels CSS, contrastes mesurés sur les couleurs construites. La cible ne constitue pas une certification WCAG.

Motion : Web Animations API sans bibliothèque. Entrée du panneau et raccord local de valeur ; annulation explicite des effets remplacés. La donnée et la sémantique ne dépendent jamais d’un callback de fin. Le mouvement réduit conserve le calcul, le feedback textuel et les actions.

Observation prévue : Chromium fourni, desktop 1440 × 1000, Web mobile émulé 390 × 844 et 320 × 844, puis hauteur réduite. Le clavier logiciel, les gestes système, le lecteur d’écran, Safari et les performances sur téléphone physique ne sont pas vérifiables par ces seuls contrôles.

## Sources et moment d’utilisation

Sources de cadrage consultées : skill du dépôt, arbre START, ligne DIRECTION, premier objet, cible visuelle, lancement, premier rendu/UI-UX, sélection et qualité créative. Sources d’implémentation : contexte et techniques, avec le contrat de mouvement et de mobile ajouté à cette suite. La revue utilise la finition et l’atelier d’édition ; la formalisation complète utilise les responsabilités de preuve et de clôture existantes.

Cette fabrication a lieu dans le contexte du coordinateur, qui connaît U6. Elle ne mesure pas un gain de coût d’agent et ne constitue pas un essai indépendant. Les lectures précédentes de cette conversation ne sont pas artificiellement exclues du contexte.

## Observation après fabrication

Le premier passage compte 50 réussites et trois échecs : le montant extrême déborde pendant son raccord animé. Le raccord est ancré à droite avec mise à l’échelle temporaire ; les textes longs du récapitulatif peuvent se replier. La quantité saisissable conserve une représentation sans séparateur de milliers. Le passage final compte **53 réussites, aucun échec**, sans erreur JavaScript ni requête externe. Les contextes sont séparés ; l’empreinte du HTML est consignée dans `preuves/parcours.json`.

Les parcours couvrent calcul et modifications rapides, ouverture et fermeture répétées, saisie erronée puis correction, annulation, retour et boucle du focus, glissement court/long et annulation de pointeur, hauteur réduite, valeurs et textes extrêmes, rechargement, téléchargement, mouvement réduit avant et pendant l’animation, API d’animation et stockage indisponibles, absence de JavaScript et deux parcours tactiles émulés. Le serveur écoute seulement sur la boucle locale et est arrêté après les mesures.

Les contrôles Gate A sur quatre largeurs ne trouvent aucun échec. Ils gardent les réserves de leur recette : noms accessibles approchés, contraste des champs natifs exclu et objet non sélectionné dans la mesure générique de l’éditeur. Le complément mesure les champs réellement construits (texte 12,88:1 ; bordure 3,34:1 ; focus 6,31:1), les noms/roles et huit cibles de l’éditeur au moins égales à 44 pixels CSS. Cela ne constitue ni un audit exhaustif de contraste ni une observation de lecteur d’écran.

Captures finales inspectées : première vue à 320 px, éditeur et focus à 390 px, facture après modification à 390 px. La comparaison ample/réduite à 390 px a été inspectée ; les six captures et leurs mesures sont conservées. Sur 390 et 320 px, la version ample place le total sous le viewport, la version réduite le conserve dès l’ouverture. À 1440 px, les deux le conservent. **Choix : entrée réduite pour cette tâche**, en conservant la voix serif. Cette paire éprouve la masse de l’entrée ; elle ne compare pas deux architectures produit entières et n’a pas de juge aveugle.

Clôture exploratoire, direction partiellement tenue. Présence : document et total lisibles ; signature : relation prestation → montant → brouillon ; détail : état sémantique correct sans attendre l’animation, annulation et reprise explicites. Défaut dominant restant : adéquation au public et au contexte métier hypothétiques. Stop : ne pas ajouter de décoration avant une tâche observée avec un indépendant représentatif et une vérification sur téléphone réel. Aucune acceptation de marque ni supériorité esthétique générale n’est prononcée. Le clavier logiciel, Safari, les gestes système, la fluidité matérielle et le lecteur d’écran restent non vérifiés.
