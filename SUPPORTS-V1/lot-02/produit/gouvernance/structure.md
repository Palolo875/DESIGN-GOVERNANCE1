# Gouvernance — contrats de structure

Les contrats, contrôles et tests de sortie qui encadrent l’usage des formes.

<!-- origine:BIBLIOTHEQUE.md -->
### Entrée prioritaire — à lire avant le catalogue

Avant de parcourir les routes détaillées, retiens ces décisions de protection :

1. **Responsabilité :** BIBLIOTHEQUE transforme une décision située en structure habitable ; elle ne choisit ni le mode, ni le style, ni le verdict de livraison.
2. **Zéro route est valide :** si la structure existante suffit, conserve-la par héritage ou comme cas documentaire, avec sa source et sa justification. `N/A-JUSTIFIED` est réservé à une non-applicabilité réelle selon ACTION. Une route n’est sélectionnée que si elle peut changer une décision d’espace, de hiérarchie, de comportement ou de preuve.
3. **Premier objet :** toute sélection ouverte doit relier une thèse structurelle, une tension et, lorsque l’écart est ouvert, une signature à un premier objet habitable, avec contenu crédible, hiérarchie, action, états et résolution proportionnée.
4. **Preuve :** distingue ce que la structure rend perceptible, ce qu’un regard expert interprète, ce qu’un contrôle technique mesure et ce qu’une personne accomplit dans une tâche. Une chaîne de routes ne constitue jamais une preuve à elle seule.
5. **Proportion :** commence par le niveau minimal qui peut changer la décision ; ajoute support, grille, scène, objet, micro, modificateur ou couche seulement lorsque leur responsabilité est active.
6. **Promotion :** une route partagée ou candidate à la durée suit `DIRECTION/START` → `ACTION/RUN-SYSTEM` → `BIBLIOTHEQUE/EVOLUTION` → `maintenance/versions.md`. Cette chaîne organise la décision et la preuve ; elle n’accorde aucune promotion.

Cette entrée est un **résumé de protection**, pas une nouvelle route, un nouveau gate, un nouveau statut ou un second contrat machine. Les sections détaillées et les propriétaires existants prévalent en cas de différence.

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/CONTRACTS — contrat commun de route

Une route locale commence par un contrat réduit : décision initiale, responsabilité, contre-indication, preuve attendue et limite. C’est la seule définition du contrat réduit ; la ligne `Local` du contrat minimal par périmètre et les lignes « avant build » de `BIBLIOTHEQUE/DERIVE` y renvoient. Lorsqu’elle est suivie comme candidate, elle peut porter le statut de cycle de vie `PILOT`, distinct du niveau de contrat et des statuts de run. Après observation, renseigne `DECISION-CHANGE` ou l’issue ACTION appropriée. Le contrat complet est nécessaire, mais non suffisant, pour `ADOPTED` : la promotion exige aussi usages contrastés, gain observé ou mesuré, maintenance, compatibilité, owner, prochaine revue et décision persistée dans `maintenance/versions.md`.

Toute route durable déclare :

| Champ | Question |
|---|---|
| Responsabilité | Quelle décision d’espace, de lecture, de preuve ou d’action porte la route ? |
| Usage juste | Dans quel contexte la route accélère-t-elle une décision ? |
| Contre-indications | Quand la route refroidit-elle, masque-t-elle ou ralentit-elle la tâche ? |
| Preuve attendue | Quelle capture, test, état ou observation montre qu’elle aide ? |
| `PROOF-TYPE` | Perceptuelle, experte, technique, utilisateur/tâche ou combinaison ? |
| `PROOF-SCOPE` | Quelle surface, tâche, medium/runtime, viewport/device, état, données ou population est couverte ? |
| `PROOF-LIMIT` | Que ne permet pas de conclure la preuve ? |
| Contenu et états | Que se passe-t-il avec contenu long, localisation, empty, error, loading, unavailable, disabled, focus, permissions, récupération et succès partiel ? |
| Mobile | Quelle relation est recomposée, conservée ou remplacée ? |
| Accessibilité | Quels risques de sémantique, nom, clavier, focus, contraste, cibles, motion et information non chromatique sont couverts, par quelle méthode et dans quel scope ? |
| Confidentialité et permissions | Quelles données, autorisations, expositions et voies de récupération sont couvertes ? |
| Compatibilité | Quels consumers, scènes, grilles, objets, plateformes ou runtimes peuvent l’accompagner, avec quel fallback, migration et rollback ? |
| Owner | Qui décide pour le run, qui reçoit l’action suivante et qui maintient la route ? La promotion/dépréciation reste une décision `maintenance/versions.md`. |
| Revue | Quels usages contrastés, baseline, observation ou mesure ont été réalisés, avec quelle limite et quand la route sera-t-elle revue ? |
| `DECISION-CHANGE` | Quelle décision a changé, été confirmée ou abandonnée grâce à la route ? |
| Contribution expressive | Quelle présence, quel rythme, quelle atmosphère ou quelle signature la route rend-elle possible dans son contexte ? |
| Risque de banalisation | Comment la route peut-elle devenir interchangeable, mécanique ou décorative ? |

Les sorties de contrôle suivent ACTION : `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` ou `NOT-VERIFIED`. Elles ne créent ni statut de route, ni état de run, ni issue, ni verdict global concurrent.

Un objet ou composant accessible en isolation doit encore être testé dans sa scène, son contenu, ses états, son viewport, ses permissions et ses interactions réels lorsque le risque le requiert. Une preuve de structure ne vaut pas automatiquement preuve de tâche, de performance ou de conformité globale.

### Calibration locale de la relation retenue

Lorsqu’une sélection ou un héritage laisse des choix de fabrication ouverts, calibre ceux qui peuvent changer la relation retenue. Cette calibration précise le contenu, la contribution expressive, les états, le mobile et la preuve du contrat existant ; elle ne crée ni formulaire, ni schéma, ni route de style supplémentaire. Les valeurs vivent dans la spec, les tokens ou le composant du projet, à côté de l’artefact. Une valeur héritée déjà adaptée reste valable.

Si la ressource reste ouverte, nomme la primitive, le pack ou le fichier réellement retenu, sa source/version et le moyen disponible pour le modifier. Relie cette ressource au levier de la table et à son observation, selon la fiche existante d’`ACTION/STRUCTURED-PROOF` ; un composant cité mais inaccessible ne devient pas une capacité acquise. Le repli conserve la responsabilité utile, sans imposer l’habillage de la bibliothèque.

| Dimension ouverte | Ce qu’il faut rendre concret dans le projet | Ce qu’il faut réinspecter |
|---|---|---|
| Support et grille | Largeur utile, axes, proportions des masses, marges et distances entre groupes ; relation recomposée au format étroit. | Silhouette, regroupement et priorité avec le vrai contenu ; éviter d’empiler mécaniquement les colonnes. |
| Objet et micro-interface | Anatomie utile, ordre valeur/contexte/action, dimensions liées au contenu, états et valeurs extrêmes. | Lecture à taille réelle, référence de la mesure, précision des données, état critique et reprise lorsqu’elle est pertinente. |
| Voix typographique | Police disponible, graisse, taille, interligne, longueur de ligne et figures numériques sur le vrai titre, le texte et les données. | Hiérarchie, caractère, wrapping et repli ; jugement par `SAVOIR/TYPE` et `SAVOIR/CRAFT/CFT-05`. |
| Image, matière et couleur | Asset retenu, point focal, traitement, occupation, rôle des couleurs et paramètres de frontière ou de lumière utiles. | Relation image/texte, raccord, contraste et effet sur l’ensemble ; juger par `SAVOIR/STYLE` et `SAVOIR/STATE`, vérifier par ACTION. |
| Comportement | Changement d’état porté par le geste, place réservée, trajectoire ou durée seulement si utiles, alternative réduite. | Début, interruption, fin, récupération et réduction dans le runtime réel ; une image fixe ne couvre pas ces observations. |

**Exemples de traduction, à adapter.** Pour une scène à deux masses, un rapport initial `3:2` peut privilégier l’objet ; le vrai titre et la lecture au format étroit peuvent imposer `1:1` ou une autre relation. Pour un groupement simple, tester une distance entre groupes supérieure à celle entre membres, puis vérifier que les unités restent perceptibles. Pour un arrondi emboîté ou un bord éclairé, utiliser les conditions de `SAVOIR/STATE`. Ces essais n’établissent aucune valeur universelle et ne sont pas des tokens partagés.

Avant le build, indique l’effet attendu du levier retenu ; après le rendu ou l’interaction, compare cet effet à ce qui est réellement observable dans le même scope. Conserve, ajuste ou retire le choix et vérifie l’ensemble. Sans observation, conserve la limite prévue par ACTION. Un paramètre inscrit dans la spec, un token ou une route nommée ne constitue pas sa réussite visuelle. Une calibration locale ne devient une règle partagée que par le parcours système et la gouvernance existants.

---

<!-- origine:BIBLIOTHEQUE.md -->
## Test de sortie BIBLIOTHEQUE

Avant de clôturer une sélection, vérifie :

1. Chaque route sélectionnée change-t-elle une décision réelle ?
2. Chaque route possède-t-elle une responsabilité et une contre-indication claires ?
3. L’objet ou la micro-interface porte-t-il une preuve, un état et une action crédibles ?
4. Le type, le scope et la limite de preuve sont-ils déclarés ?
5. La recomposition mobile couvre-t-elle priorité, voisinage, action, état, contenu et performance lorsque le risque le requiert ?
6. La combinaison choisie est-elle justifiée par JTBD, preuve, risque et condition de sortie ?
7. Chaque identifiant sélectionné existe-t-il dans le catalogue canonique, ou est-il explicitement marqué local ou `PILOT` ?
8. En trace complète, la sélection structurelle et sa justification sont-elles persistées dans la `RUN_CARD` ou la trace canonique référencée par `trace_locator`, le paquet de preuve n’étant qu’une pièce jointe localisable ?
9. Les routes et identifiants respectent-ils le bon niveau : support, grille, scène, objet, micro, modificateur ou couche ?

Si une réponse reste inconnue, utilise `NOT-VERIFIED`. Si un contrôle doit être repris, utilise `RETURN`; si le périmètre reste exploratoire, utilise l’issue ACTION appropriée, par exemple `EXPLORATORY` ou `RETURNED`. Ne transforme pas une chaîne complète de routes en preuve de qualité et ne remplace pas `ACTION/CLOSE-EXIT-CHECK`.
