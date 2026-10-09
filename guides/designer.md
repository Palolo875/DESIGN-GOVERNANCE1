# Guide du designer

Pour qui connaît le design et veut aller droit au sujet. Ce guide sert à trois choses : trouver où un sujet est traité, combiner plusieurs savoirs selon le résultat cherché, et savoir quand s’arrêter de lire. Les liens entre domaines sont dans [`design/savoir/connexions.md`](../design/savoir/connexions.md).

Les adresses entre accents graves, comme `savoir/couleur`, se lisent avec le lecteur : `python3 scripts/read_route.py savoir/couleur`.

<!-- origine:READING_MAP.md -->
## Carte des sujets

Quand un sujet est traité à plusieurs endroits, cette carte dit où le lire d’abord, puis où regarder ensuite. Elle oriente seulement : c’est la section indiquée qui fait foi. `python3 scripts/read_route.py --trouver` l’affiche en tête quand la recherche nomme un sujet ou l’un de ses synonymes.

| Sujet | Où le lire d’abord | Voir aussi |
|---|---|---|
| capture | `produit/preuve-visuelle` | `gouvernance/verification#comparaison-sur-capture`, `produit/plancher` |
| hiérarchie | `savoir/composition` | `savoir/qualite-creative#ambition`, `savoir/typographie` |
| contraste | `produit/plancher` | `savoir/couleur`, `produit/plancher#contraste` |
| typographie | `savoir/typographie` | `savoir/couleur`, `produit/finition` |
| couleur | `savoir/couleur` | `produit/plancher` |
| mobile | `produit/interface` | `savoir/composition#jugement-visuel`, `savoir/contexte`, `formes/catalogue#sequence` |
| état | `savoir/composition#jugement-visuel` | `produit/interface` |
| performance | `savoir/techniques` | `savoir/contexte` |
| accessibilité | `savoir/contexte` | `produit/plancher`, `produit/plancher#contraste` |
| densité | `savoir/composition` | `produit/finition` |
| grille | `formes/catalogue#grilles` | `formes/choisir` |
| composant | `formes/catalogue#composants` | `savoir/systeme-de-design`, `agent/chemins#systeme` |
| exemple | `direction/cadrer#demande-vague` | `direction/premier-objet` |
| image | `savoir/images-et-sources` | `direction/diriger#cible-visuelle`, `savoir/images-et-sources#familles` |
| convergence | `savoir/gout-et-tendances#tendances-datees` | `savoir/couleur`, `formes/choisir` |
| structure | `formes/choisir` | `formes/choisir#lire` |
| séquence | `formes/catalogue#sequence` | `formes/catalogue#scenes` |
| texte sur image | `savoir/composition` | — |
| graphique | `formes/catalogue#micro` | — |
| état vide | `produit/interface` | `savoir/composition#jugement-visuel` |
| pied de page | `formes/catalogue#sequence` | — |
| cartes | `formes/catalogue#sequence` | `formes/choisir` |

<!-- origine:READING_MAP.md -->
## Combinaisons par résultat recherché

Quand plusieurs savoirs peuvent changer la même décision, ou protéger le même risque, cette table propose comment les combiner. Elle ne crée ni chemin, ni règle, ni vérification : le chemin de travail est choisi d’abord (`agent/chemins#classer`), puis la combinaison selon le résultat cherché et le périmètre réel.

> **Principe :** composer ce qui apporte vraiment, pas tout lire. Chaque savoir ajouté doit avoir un apport qu’on peut nommer ; on le retire s’il ne change ni la décision, ni le rendu, ni la preuve, ni la limite, ni la prochaine étape.

La combinaison choisie n’est notée dans la trace du travail que si elle peut changer la décision. Pas de trace par savoir ajouté, et une table d’orientation n’est pas une preuve.

| Résultat recherché | Base | À ajouter seulement si nécessaire | Preuve à privilégier |
|---|---|---|---|
| **Direction forte et spécifique** | `agent/chemins#quoi-lire`, chemin « direction ouverte » (`DIRECTION`) | `direction/diriger#lancement`, `direction/cadrer#domaine`, `savoir/qualite-creative`, `savoir/images-et-sources`, `savoir/styles`, `formes/choisir` | Un premier objet réel, une revue créative, le défaut principal observé puis réellement corrigé. |
| **Beauté, goût et craft situés** | `direction/premier-objet` + `savoir/qualite-creative` + `produit/premier-rendu` | La traduction de `formes/choisir` si l’intention n’a pas encore de levier ; le réglage de `gouvernance/structure` si la fabrication reste ouverte ; les gestes conditionnels de `savoir/composition#jugement-visuel` (dans le noyau) ; puis `savoir/styles`, le contenu, la matière, la typographie ou l’ancre, seulement si la décision l’exige (`agent/chemins#quoi-lire`) | La relation et l’effet attendu sont nommés avant de construire, puis vérifiés sur le même périmètre ; le jugement créatif reste séparé des preuves d’usage, d’accessibilité et de robustesse. |
| **Créativité variée mais utile** | `direction/diriger#lancement` + `direction/diriger#cible-visuelle` + une alternative adaptée au projet | `direction/cadrer#domaine`, `savoir/images-et-sources` ou l’atelier, seulement si l’axe de divergence change une décision | Une comparaison sur le même périmètre : public, tâche visée, promesse, geste, structure ou expression. |
| **UI/UX habitable** | `produit/interface` + `formes/choisir` + `produit/plancher` (contrôles applicables) + contenus et états réels | Responsive, focus, récupération après erreur, exécution technique ou `savoir/contexte`, selon le risque | Tâche, états, tailles d’écran, contenus extrêmes, clavier, ou méthode adaptée à ce qu’on affirme. |
| **Preuve et décision fiables** | `gouvernance/verification#contrats` + rendu réel + vérification (gate) adaptée au risque + `gouvernance/cloture#test-de-sortie` | Une preuve croisée, ou une fiche de travail (`RUN_CARD`) stricte si la trace doit durer | Ce qu’on affirme, la méthode, le périmètre, la date, le rendu, la limite et l’emplacement de la trace, retrouvables. |
| **Vitesse sans appauvrissement** | `agent/chemins#classer` + `agent/chemins#chemin-court` + une retouche (`LITE`) ou une itération (`ITER`) bien classée | Une seule capacité de plus, si elle peut changer la décision ; reclasser si le risque ou le périmètre grandit | Rendu réel, observation ciblée, preuve minimale applicable et prochaine étape. |
| **Système maintenable** | `agent/chemins#systeme` + `formes/catalogue#composants` si un composant change + migration, retour arrière (rollback) et `maintenance/versions.md` (paquet SYSTÈME) | `maintenance/evolution#routes` ou `savoir/systeme-de-design`, selon la décision partagée | Qui utilise le composant, compatibilité, non-régression, responsable, migration et condition de reprise. |
| **Domaine sensible ou incertain** | `direction/cadrer#domaine` + `savoir/images-et-sources` + `gouvernance/verification#contrats` | Contexte culturel, conventions, confiance ou recherche, seulement si un déclencheur peut changer la décision | Une source ou une observation reliée à la décision, ce qu’on en a fait, ce qu’on a écarté, et la limite. |
| **Agent contrôlé** | `agent/chemins#classer` + `gouvernance/principes#portee` + `SKILL.md` + un responsable | Cette carte, seulement si plusieurs capacités sont vraiment nécessaires ; une fiche de travail (`RUN_CARD`) en trace complète (travail qui dure, partagé, audité ou dont on demande l’acceptation), quel que soit le nombre de capacités ; exception de forme courte LITE sans RUN_CARD selon `agent/repondre` | Rendu livré, autonomie exercée, décision, preuve, limite, remontée et prochaine étape. |

Ces combinaisons ne sont pas des parcours obligatoires. Elles indiquent des savoirs qui vont bien ensemble ; c’est chaque section indiquée qui définit son contenu exact.

### Variation créative

Pour varier sans bruit, faites varier un seul axe à la fois (`savoir/qualite-creative#registres`).

Une alternative n’est utile que si elle peut changer le choix. Une référence, une ancre, une justification ou une variante n’est pas une preuve indépendante.

### Garde-fous de la combinaison

- Une itération (`ITER`) rappelle et réévalue une direction existante, retrouvable dans son périmètre ; un correctif local qui la conserve reste une retouche (`LITE`) (`agent/chemins#classer`).
- Un chemin court ne réduit jamais la protection d’un risque critique.
- Une capacité indisponible limite ce qu’on peut affirmer ; elle ne justifie pas de baisser le chemin en silence.
- Inutile de remplir toutes les sections d’une combinaison si une seule suffit.
- N’ajoutez ni trace, ni variante, ni preuve qui ne peut changer la décision, le rendu, la limite ou l’étape suivante.

Arrêtez de combiner quand la décision, le risque, le périmètre, le responsable, le rendu, la preuve, la limite et la prochaine étape sont assez clairs. Lire beaucoup n’est pas un résultat ; le résultat cherché est **un effet positif, visible dans le périmètre déclaré**.

<!-- origine:READING_MAP.md -->
## Les angles à examiner

Un angle (usage, accessibilité, contenu…) ne s’examine que si son déclencheur peut changer la décision. « Sans objet, justifié » (`N/A-JUSTIFIED`) est une réponse valable quand l’angle a été examiné et ne s’applique pas. Ne pas lire une section ne rend jamais « sans objet » un contrôle qui s’applique.

| Angle | Déclencheur | Lire au minimum | Ce qu’on en tire | Quand ne pas le lire |
|---|---|---|---|---|
| Direction | Identité, présence, premier objet ou composition ouverte | `design/direction/` et la cible visuelle (`direction/diriger#cible-visuelle`) | Thèse, objet, ancre, relation, défaut principal | Décision visuelle intacte et changement strictement local |
| Production | Un rendu ou une modification à construire | La section du chemin choisi (`agent/chemins#modes`) | Rendu, périmètre, état et prochaine preuve | Aucun rendu, ou simple clarification |
| Usage | Tâche visée, action, confiance, récupération ou tâche critique | `produit/interface` | Geste, résultat, état, limite | Aucun effet sur l’usage déclaré |
| Contenu | Données, longueur, langue, affirmation ou état | `savoir/typographie` ou `savoir/composition#jugement-visuel` | Contenu crédible, hiérarchie, limite | Contenu inchangé et sans effet |
| Responsive | Mobile, zoom, réagencement ou taille d’écran critique | `produit/interface` + `savoir/contexte` | Recomposition, priorité, preuve sur le périmètre | Aucun changement de taille d’écran ni risque déclaré |
| Accessibilité | Focus, clavier, sémantique, contraste, mouvement ou public critique | `savoir/contexte` + `produit/plancher` | Méthode, périmètre, résultat, limite | Aucun risque d’accessibilité au-delà des contrôles applicables de `produit/plancher`, qui restent dus |
| Exécution technique | Compatibilité, performance, solution de repli ou plateforme | `savoir/techniques` + la qualité du produit (`design/produit/`) | Environnement, méthode, erreur, repli, preuve | Aucune affirmation technique |
| Preuve | Affirmation, capture, mesure, verdict ou clôture | `produit/preuve-visuelle`, puis le module de gouvernance si le travail est tracé | Affirmation, méthode, périmètre, date, limite, emplacement | Aucune affirmation de résultat |
| Maintenance | Composant partagé, trace, migration ou reprise | Le module de gouvernance + `maintenance/versions.md` si la décision dure | Responsable, différences, compatibilité, revue, réouverture | Changement local sans conséquence future |
| Coordination | Passage de relais, remontée, action externe ou responsable suivant | `gouvernance/principes#portee` et `agent/repondre` | Destinataire, autonomie, confirmation, prochaine étape | Aucun passage de relais |
| Mémoire | Décision durable, version, réserve ou migration | La fiche de travail (`RUN_CARD`) et `maintenance/versions.md` si la décision est promue | Décision, date, statut, preuve, réserve, revue | Décision strictement éphémère |

<!-- origine:READING_MAP.md -->
## Quand s’arrêter de lire

Arrêtez quand la décision, le risque, le responsable, ce qu’on rend, la prochaine preuve et la limite sont assez clairs pour la personne suivante. Ne lisez une section de plus que si elle peut changer l’un de ces points. Une décision visuelle peut rester exploratoire (`EXPLORATORY`) ; une validation de documents ne prouve ni l’usage, ni l’accessibilité, ni la performance, ni la qualité réelle.
