# Direction — cadrer

Partir d’une demande, même vague, et cadrer ce qui peut changer le résultat.

<!-- origine:DIRECTION.md -->
## DIRECTION/EXTERNAL-START — activation portable sur brief vague

Cette vue rend V1 activable lorsqu’un agent externe reçoit un brief court, une skill ou les fichiers du package dans une conversation. Elle s’applique aussi lorsqu’un brief interne est suffisamment vague pour que la première scène, le grounding ou le réemploi puisse changer la décision ; elle ne remplace pas le fast path de `LITE` ou `ITER`. Elle n’impose aucun profil ni style. Elle est une **vue de démarrage**, pas un nouveau mode, gate, statut, owner, score, questionnaire ni une seconde `RUN_CARD`. Propriétaires et modules : ordre de lecture minimal de `DIRECTION/START`.

Après `DIRECTION/START`, avant le premier code ou le premier rendu d’une surface `DIRECTION`, l’agent tient seulement les décisions qui peuvent changer l’artefact :

```text
RUN-PRIORITY
1. TRUTH — retirer, sourcer ou marquer tout claim, chiffre, logo, témoignage,
   disponibilité, intégration, personne, action ou résultat non observé.
2. DIRECTION — retenir support, tension, scène, typographie, modal et parti
   parce qu’ils servent ce brief ; « premium », « beau » ou « moderne » ne suffisent pas.
3. FIRST-OBJECT — matérialiser la cible : promesse → objet de preuve → geste,
   avant les éléments génériques ou décoratifs (bénéfices, navigation, cartes,
   polish), sauf si la navigation, la recherche ou les cartes sont elles-mêmes
   l’objet de preuve.
4. FINISH — corriger seulement le défaut dominant qui empêche lecture, action,
   contraste, état, mobile ou vérité ; ne pas polir une erreur de niveau supérieur.
NO-GO — faux réalisme, dashboard décoratif, cartes avant mécanisme, ou retour
        automatique au dernier style, asset ou rendu disponible.
```

<!-- noyau:début BRIEF -->
**Prise de brief.** Au plus trois demandes, en un seul échange, par gain de plafond : contenu réel (textes, chiffres, preuves, noms), marque, asset principal ou route autorisée, destination si elle est incertaine. Brief riche : aucune. Le build se fait dans le même tour, avec des hypothèses nommées ; les demandes accompagnent la proposition, sous « Ce qui manque pour la vraie version ». Une réponse n’est attendue avant le build que si la personne l’a demandé ou si l’action est irréversible ou coûteuse. Sans personne pour répondre : plafond déclaré, demandes listées à la livraison. La réponse est une proposition, pas un compte rendu de cadrage ; le raisonnement de cadrage reste dans la trace. Si une ligne ne peut modifier ni artefact, claim, preuve, limite ou décision, elle est omise ; `N/A-JUSTIFIED` reste réservé à une non-applicabilité réelle et justifiée selon ACTION.
<!-- noyau:fin BRIEF -->

<!-- noyau:début CONTENU -->
<!-- concept:CNT-01 -->
**Destination réelle sans contenu.** Si la surface sert un vrai commerce, service ou personne mais que ses contenus manquent (nom, offre, prix, horaires, photos, adresse), remplis-la d’un contenu plausible **marqué comme exemple** plutôt que d’emplacements vides : elle doit se lire comme une page, pas comme un gabarit. L’action principale (commander, écrire, appeler, venir) reste fonctionnelle avec une valeur d’exemple marquée (numéro, adresse, lien) : une valeur inconnue ne la retire pas. Pour un produit fictif ou non encore construit, les fonctions, intégrations et conformités affirmées sont aussi des contenus d’exemple, marqués comme le nom et le prix. Le marquage est discret dans l’interface (« exemple », « à confirmer ») et explicite dans la réponse, qui liste ce qu’il faut fournir. Le marquage de vérité s’applique sans exception. Les valeurs d’exemple restent cohérentes avec le métier (unités, catégories, ordres de grandeur). Une fiction assumée, comme une affiche ou un récit, n’est pas une preuve ; un signe de preuve inventé (logo client, avis, chiffre, mention officielle) n’est jamais un décor.
<!-- noyau:fin CONTENU -->

### Traduction humaine minimale de DIRECTION/START

Pour une personne non spécialiste, les mêmes décisions peuvent être formulées sans le vocabulaire du corpus :

| Question simple | Contrat correspondant |
|---|---|
| Qu’est-ce que la personne doit comprendre, ressentir ou faire ? | `DECISION`, `JTBD`, promesse et geste. |
| Qu’est-ce qui doit être visible tout de suite ? | `FIRST-OBJECT`, preuve, foyer et hiérarchie. |
| Qu’est-ce qui rend cette proposition propre à ce produit ? | Signature située, matière, contenu, public et contrainte. |
| Qu’est-ce que nous refusons de faire ? | `MODAL` écarté par le `PARTI`, contre-choix et limites. |
| Qu’est-ce qui coûterait cher si c’était faux ? | `RISK` et Protection de niveau (`DIRECTION/START`). |
| Comment saurons-nous si cela tient ? | `NEXT-PROOF`, observation, condition d’arrêt et owner. |

Cette traduction n’ajoute ni formulaire ni mode. Elle rend seulement le chemin d’entrée compréhensible par une personne qui ne connaît pas `VISUAL_TARGET`, `DIRECTION-ATELIER` ou `N/A-JUSTIFIED`.
