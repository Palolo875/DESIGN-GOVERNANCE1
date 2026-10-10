# Glossaire — Design Governance V1

Les mots du système, expliqués simplement. Le glossaire n’ajoute aucune règle : chaque terme renvoie à la section qui fait foi. Les adresses entre accents graves (`savoir/couleur`) se lisent avec `python3 scripts/read_route.py ADRESSE` ; les valeurs en capitales (`NOT-VERIFIED`) sont celles qu’écrivent les fiches de travail.

Trois groupes : [le design](#les-mots-du-design), [le travail](#les-mots-du-travail), [la trace et la vérification](#la-trace-et-la-vérification). Pour commencer sans aucun vocabulaire, lisez plutôt le [guide pour commencer](commencer.md).

## Les mots du design

| Terme | Signification simple |
|---|---|
| **Direction** | La position de design qui relie le produit, le contenu, la forme, la matière, la structure, l’action et les états. |
| **Direction artistique (DA)** | Le point de vue visuel qui rend une promesse, un contenu et un contexte reconnaissables ; ce n’est pas une simple ambiance ou une référence. |
| **Thèse** | La position de design en une phrase : ce que la proposition affirme sur le produit et sur la personne à qui elle s’adresse. |
| **Craft** | La qualité de construction qu’on perçoit : hiérarchie, composition, typographie, matière, contenu, états et comportement. |
| **Polish** | La résolution précise des détails du rendu réel : un défaut mène à un geste concret, choisi pour ce cas, puis regardé de nouveau (`savoir/composition#jugement-visuel`), sans accumuler d’effets décoratifs. |
| **Créativité située** | Un écart, une relation ou une reformulation qui apporte une réponse propre au projet et utile ; pas la nouveauté pour elle-même. |
| **Goût situé** | La sélection, la proportion et la retenue adaptées au contexte ; pas une préférence universelle. |
| **Spécificité** | Ce qui relie le rendu au produit et à son contexte, au point qu’un modèle générique ne pourrait pas le remplacer sans perte. |
| **Ancre** | Une référence réellement regardée (observée, fournie ou générée) qui calibre une décision visuelle ; on note ce qu’on en retient, ce qu’on écarte et sa date. |
| **Voies d’ancrage (`ANCHOR-*`)** | `ANCHOR-OBSERVED` : référence réellement regardée ; `ANCHOR-PROVIDED` : fournie par la personne ou le projet ; `ANCHOR-GENERATED` : hypothèse générée, utile pour comparer, sans autorité par défaut. |
| **Creative Boot** | Le lancement créatif : un cadrage court avant le premier pixel d’une décision visuelle ouverte (promesse, objet de preuve, geste, `MODAL`, `PARTI`, tension, `FABRICATION` et premier objet). |
| **`MODAL`** | Ce que n’importe quelle IA produirait par défaut pour ce brief (structure, palette, typographie, images), nommé pour pouvoir le garder ou s’en écarter en connaissance de cause. |
| **`PARTI`** | La décision prise face au `MODAL` : le garder ou s’en écarter, à quel endroit, et pour quelle raison liée à la thèse. |
| **Trame modale** | L’ordre de sections que n’importe quelle IA produirait pour un brief. Le test de trame la nomme, puis la rompt ou la justifie par la tâche. |
| **`FABRICATION`** | Le bilan des moyens réels (images, marque, polices, composants, génération, contenu) et du niveau atteignable, couche par couche, avant de construire. |
| **Plafond** | Le niveau qu’une couche peut atteindre avec les moyens disponibles ; s’il est bas, l’agent le dit, et dit ce qui le relèverait. |
| **Objet de preuve** | L’élément de la première scène qui rend la promesse crédible : de préférence un composant, une donnée, un état ou une interaction du produit. |
| **Premier objet** | L’élément qui rend la direction visible et utile dans la première proposition : objet, scène, composant, interaction ou relation de contenu. |
| **Défaut dominant** | Le défaut qui pèse le plus sur la qualité perçue ou sur l’usage ; c’est lui qu’on corrige en premier. |
| **Boucle d’amélioration** | Après la première proposition : regarder le rendu réel, isoler le défaut dominant, modifier le rendu, regarder de nouveau et décider. Une critique écrite seule ne corrige rien. |
| **Profil de surface** | Le type de surface (vitrine, application, scène, hors Web) qui fixe les contrôles d’accessibilité à faire d’office. |
| **Vérité de scène** | La règle qui marque comme illustratif tout exemple, chiffre ou témoignage non observé, et qui le signale au public en langage produit. |
| **Marquage de vérité (`TRUTH/*`)** | Étiquette interne posée près d’une affirmation ou d’un objet : `OBSERVED` ou `ILLUSTRATIVE` (factualité, exclusive), cumulable avec `MECHANISM` (nature). Elle n’apparaît jamais dans l’interface. |
| **Slop** | Une production générique, répétitive ou trompeuse, faite avec peu de soin ; le slop procédural est une trace remplie sans décision réelle. |

## Les mots du travail

| Terme | Signification simple |
|---|---|
| **Décision** | Le choix concret que le travail doit permettre de prendre, de confirmer ou d’abandonner. Exemple : garder la structure d’un bouton tout en améliorant sa lisibilité. |
| **Risque** | Le coût possible d’une mauvaise décision : apparence, usage, accessibilité, technique ou système partagé. |
| **Tâche visée (JTBD)** | *Job to be done* : la tâche ou le progrès concret que la personne cherche à accomplir dans le contexte déclaré. |
| **Portée d’un changement (*blast radius*)** | Tout ce qu’un changement peut toucher : personnes, écrans, composants ou décisions qui en dépendent. |
| **Mode** | Le chemin de travail adapté à la demande : retouche (`LITE`), itération (`ITER`), écran cadré (`STANDARD`), direction ouverte (`DIRECTION`) ou système de design (`SYSTÈME`). Le niveau de trace (légère ou complète) se choisit à part, selon que le run est persistant, partagé ou audité. |
| **Chemin court (`FAST-PATH`)** | Une version courte pour un changement local ou une décision presque tranchée. Elle allège la forme, jamais la preuve requise ni l’honnêteté du statut. |
| **Cadrage d’entrée (façade d’activation)** | Le cadrage court avant les sections détaillées : chemin, risque principal, décision à changer, prochaine preuve et responsable. Ce n’est ni un nouveau chemin, ni une nouvelle vérification. |
| **Run** | Un travail délimité, avec une décision, un risque, un rendu et une preuve. Il s’arrête à une proposition (trace légère) ou à une clôture (trace complète). |
| **Première proposition** | Le premier rendu, présenté avec sa thèse et ce qu’il faut décider. Il vaut checkpoint, sauf action irréversible ou coûteuse. |
| **Livraison** | La remise d’un rendu à une personne : la première proposition (trace légère ; elle vaut checkpoint) ou la remise acceptée (trace complète). Les preuves qui s’appliquent au chemin sont dues dans les deux cas ; seule leur écriture s’allège en trace légère. |
| **Artefact** | Le résultat concret qu’on peut inspecter : code, écran, capture, composant, test, différence ou autre livrable. |
| **Responsable (owner)** | La personne ou l’équipe responsable de la décision, de la reprise ou de la remontée. |
| **Périmètre (scope)** | Ce que la construction ou la preuve couvre réellement : vues, états, appareils, utilisateurs, données ou tâches. |
| **Limite** | Ce que le travail ne permet pas d’affirmer honnêtement. Une limite n’est pas un échec caché ; elle rend le niveau de confiance lisible. |
| **Source propriétaire** | La section qui fait foi pour une règle. Un guide peut la résumer, jamais la remplacer. |
| **Adresse (locator)** | Le repère qui permet de lire une section avec le lecteur : une adresse lisible (`savoir/couleur`) ou l’ancien code (`SAVOIR/CRAFT/CFT-05`), qui reste accepté. Par extension, tout repère stable vers un fichier, une trace ou un rendu. |
| **Carte de lecture (`READING_MAP`)** | Les vues qui orientent la lecture : le [guide du designer](designer.md) (sujets, combinaisons, angles) et les [connexions](../design/savoir/connexions.md). Elles ne créent aucune règle. |

## La trace et la vérification

Ces mots servent surtout quand un travail doit être tracé, vérifié formellement ou livré (module de [gouvernance](../gouvernance/README.md)).

| Terme | Signification simple |
|---|---|
| **Trace légère** | La trace par défaut d’un run ni persistant, ni partagé, ni audité : six lignes au plus (mode ; thèse ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant restant, rendu comme revue de présence lorsque la qualité perceptuelle est en jeu ; prochaine preuve). Le run livre une proposition, sans verdict ni clôture. |
| **Trace complète** | La trace d’un run persistant, partagé, audité ou dont on demande l’acceptation : réponse et trace (`agent/repondre`), dossier de clôture, vérifications écrites et fiche selon `gouvernance/cloture`. La forme courte LITE définie par `agent/repondre` est complète sans RUN_CARD ; elle ne se confond pas avec la trace légère. |
| **RUN_CARD** (fiche de travail) | La version structurée et persistante d’un run, produite quand les règles de `gouvernance/travail` exigent ce format. Son exigence dépend du niveau de trace et du mode ; une proposition en trace légère ne produit pas de RUN_CARD. Les formes de clôture restent définies par `gouvernance/cloture`. Elle porte décision, risque, rendu, preuve, limite et clôture. |
| **Preuve** | Ce qui permet de confirmer ou d’infirmer une décision dans un périmètre déclaré : observation, capture, test, mesure, comparaison ou retour adapté. |
| **Gate** | Une vérification ciblée, avec une preuve ou une condition adaptée. `A`, `B` et `C` désignent des familles de vérifications ; elles ne donnent pas une note globale. |
| **Axes V/U/A/T** | Les questions de preuve : caractère visuel ; compréhension et usage observables dans la tâche déclarée ; accessibilité ou conformité ; robustesse technique. |
| **B1b** | L’atelier d’édition sur capture : une décision principale éditée par retrait, réduction ou transformation, puis comparée ; requis seulement dans son périmètre (`gouvernance/verification#comparaison-sur-capture`). |
| **État (`STATE`)** | L’étape du cycle de vie du run, de `INTAKE` à `CLOSED`. Il ne signifie pas que le résultat est accepté. À ne pas confondre avec `savoir/composition#jugement-visuel`, qui traite des états d’une interface, ni avec le statut de direction. |
| **Issue (`ISSUE`)** | La condition qui affecte le run, par exemple `BLOCKED`, `RETURNED` ou `EXPLORATORY`. |
| **Verdict (`VERDICT`)** | La conclusion globale sur le périmètre observé : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Les résultats par axe peuvent utiliser `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `NOT-VERIFIED` ou `N/A-JUSTIFIED`, mais ce ne sont pas des verdicts globaux. |
| **Statut de direction** | La fidélité de la direction dans le rendu : `HELD`, `HELD-WITH-ACCEPTED-DIFFERENCE`, `PARTIALLY-HELD` ou `LOST-IN-BUILD`. Il ne remplace pas le verdict global. |
| **`DECISION-INTENT`** | La décision que le travail doit permettre de trancher, posée au lancement. |
| **`DECISION-CHANGE`** | La décision effectivement changée, confirmée ou abandonnée grâce à une observation. Sinon, les valeurs de repli de `gouvernance/statuts` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, avec la raison ; `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. |
| **`TRACE-LOCATOR`** | Le repère qui permet de retrouver la trace persistante du run : ticket, manifeste, fichier, espace de travail ou autre emplacement déclaré. |
| **`SPECCED`** | Étape du cycle du run : la direction, la hiérarchie, le contrat ou l’ancre nécessaires sont assez précis pour passer à la construction (`BUILDING`). Ce n’est ni un verdict, ni une preuve de qualité. |
| **`CLOSED`** | La trace et les rendus sont enregistrés. Cela ne veut pas dire automatiquement « réussi » ou « vérifié ». |
| **`NOT-VERIFIED`** | Non vérifié : une propriété importante n’a pas été vérifiée dans le périmètre ou avec les moyens disponibles. |
| **`NOT-OBSERVED`** | Non observé : une conséquence, un changement ou un résultat attendu n’a pas été observé dans le périmètre déclaré. |
| **`N/A-JUSTIFIED`** | Sans objet, justifié : une preuve ou une vérification ne s’applique pas, avec une justification explicite. |
| **`FAIL-ASSUMED`** | Un échec connu et observé, assumé explicitement (`gouvernance/verification#derogation`) ; jamais pour une preuve ou une ancre absente, qui reste `NOT-VERIFIED`. |

## Exemples express

Ces exemples montrent les termes en usage ; ils ne créent aucune règle.

| Terme | Exemple concret |
|---|---|
| **Décision** | « Garder la structure du formulaire, mais rendre le premier geste compréhensible sur mobile. » |
| **Preuve** | « Comparer le rendu avant/après à 390 px, puis vérifier le focus clavier dans le périmètre déclaré. » |
| **NOT-VERIFIED** | « Le contraste a été inspecté ; aucun test avec lecteur d’écran n’a été exécuté. » |
| **DECISION-CHANGE** | « `CHANGED` — après observation à 390 px, la décision « deux CTA de même poids » est remplacée par un CTA principal unique (observation : capture avant/après). » |
| **N/A-JUSTIFIED** | « Aucun test de préférence n’est applicable : la décision porte ici uniquement sur la robustesse du composant. » |
| **CLOSED** | « La trace et les rendus sont enregistrés. `CLOSED` ne dit rien du verdict : un run peut être clos en `RETURN`. Clos en `ACCEPTED-WITH-RESERVATION`, il porte une réserve complète (responsable ou owner, portée, date ou version, impact, prochaine preuve, date de revue, condition de sortie). Une protection critique restée `NOT-VERIFIED` exclut `ACCEPTED`, pas la réserve ; une protection en échec (`FAIL`) exclut tout verdict accepté. » |
