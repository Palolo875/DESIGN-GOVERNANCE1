# Gouvernance — contrats de structure

Les contrats et contrôles qui encadrent l’usage des formes.

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/CONTRACTS — contrat commun de route

En trace légère, les formulaires de BIBLIOTHEQUE (signature, dérivation, grille, objet, grammaire de marque) sont tenus dans l’artefact : seule leur décision, si elle change la proposition, entre dans la trace ; leur forme écrite relève de la trace complète (`ACTION/HANDOFF`).

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

<!-- origine:BIBLIOTHEQUE.md -->
## BIBLIOTHEQUE/GATE — contrôle de module structurel complémentaire

Ce contrôle appartient au périmètre de BIBLIOTHEQUE. Il ne constitue pas un quatrième gate global : `ACTION/GATE-A`, `ACTION/GATE-B` et `ACTION/GATE-C` restent les gates canoniques du run.

Il s’agit d’un **contrôle structurel complémentaire**, pas d’une route de clôture concurrente. BIBLIOTHEQUE peut décrire le parti structurel et sa limite ; `ACTION` reste propriétaire du scope, de la méthode, de la preuve, des statuts, des issues, du verdict de livraison et de la clôture. `BIBLIOTHEQUE/GATE` ne possède ni statut ni verdict propres.

<!-- concept:PRC-01 -->
Le contrôle de module vérifie support, grille, scène, objet, états, mobile et accessibilité structurelle, pas seulement code ou conformité d’une primitive. Il vérifie également que la thèse structurelle est visible dans le premier objet habitable et que la relation déclarée reste observable lorsque le contenu, le viewport ou l’état changent. Pour une micro-interface d’identification, de santé, de permission ou de récupération, reviens à `DIRECTION/START` pour la classification et à `ACTION` pour la preuve, le scope et le verdict ; le contrat structurel seul ne suffit jamais.

| Test | Question | Type possible |
|---|---|---|
| Non-généricité | Sans image, données et nom, la structure pourrait-elle appartenir à cinquante produits ? Si oui, la structure dépend de ce qui a été retiré. Si la dépendance est porteuse (relation déclarée, fallback prévu par `DIRECTION/VISUAL_TARGET`), la conserver. Si elle est décorative, changer la relation support/grille/scène/preuve plutôt qu’ajouter du polish. Dans les deux cas, décider sur le rendu entier, la tâche et `ACTION/GATE-C`. | `PERCEPTUAL`, `EXPERT` |
| Silhouette | Après floutage, support, foyer, masses et axes restent-ils perceptibles ? | `PERCEPTUAL` |
| Grille | Éléments critiques partagent-ils un axe, rythme ou relation identifiable ? Les ruptures changent-elles une priorité ? | `PERCEPTUAL`, `EXPERT` |
| Preuve | Objet ou micro-interface répond-il à la promesse avec contenu, état et action crédibles ? | `EXPERT`, `USER/TASK` |
| Asset | Route de production, cadrage, occupation et contraste changent-ils support, scène ou preuve ? Source, droits, provenance et raison de route sont-ils tracés ? | `TECHNICAL`, `EXPERT` |
| Clarté | Tâche, référence, conséquence et action sont-elles lisibles ? | `EXPERT`, `USER/TASK` |
| États | Loading, empty, error, unavailable, disabled, succès, contenu long et données sensibles préservent-ils le rôle ? | `TECHNICAL`, `USER/TASK` |
| Mobile | Priorité, voisinage, action, état, contenu et performance sont-ils recomposés plutôt que compressés ? | `TECHNICAL`, `USER/TASK` |
| Accessibilité | Focus, clavier, contrastes, noms, alternatives et information non chromatique sont-ils présents ? | `TECHNICAL`, `USER/TASK` |
| Contexte | La structure répond-elle au public, au JTBD et au risque dominant ? | `EXPERT`, `USER/TASK` |
| `DECISION-CHANGE` | Après observation, la sélection a-t-elle changé, confirmé ou abandonné une décision, ou est-elle seulement documentée ? | Sortie de trace ACTION ; méthode et scope séparés |

BIBLIOTHEQUE/GATE reste complémentaire d’ACTION/GATE-A, B et C. BIBLIOTHEQUE vérifie le parti structurel et rend explicite la limite ; ACTION contrôle scope, méthode, preuve et verdict de livraison.

### Statut ACTION du contrôle structurel

Ce contrôle ne possède ni statut ni verdict propres. Les statuts ACTION applicables sont `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `N/A-JUSTIFIED` ou `NOT-VERIFIED`, dans le registre de gate ou de preuve approprié.

Une description dans la `RUN_CARD` peut suffire pour une relation simple et non critique. Une relation visuelle critique exige une capture annotée, un rendu ou une comparaison adaptée. Une description seule ne devient pas une preuve de rendu.

Une chaîne de routes complète sans `DECISION-CHANGE` observable est une trace documentaire, pas une preuve de structure.

La structure reçoit la route d’asset décidée par `DIRECTION` et vérifiée par `ACTION` seulement lorsqu’elle modifie support, scène, objet ou mobile. Elle ne source ni ne hiérarchise les outils. La preuve structurelle reste locale au run ; BIBLIOTHEQUE ne devient ni galerie d’assets, ni archive de références visuelles, ni corpus de goût.
