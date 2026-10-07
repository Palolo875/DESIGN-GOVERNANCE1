# Glossaire — Design Governance V1

Ce glossaire explique les mots nécessaires pour commencer. Il n’ajoute aucune règle et ne remplace pas les cinq sources normatives.

| Terme | Signification simple |
|---|---|
| **Décision** | Le choix concret que le travail doit permettre de prendre, de confirmer ou d’abandonner. Exemple : conserver la structure d’un bouton tout en améliorant sa lisibilité. |
| **Risque** | Le coût possible d’une mauvaise décision. Il peut concerner l’apparence, l’usage, l’accessibilité, la technique ou un système partagé. |
| **JTBD** | « Job to be done » : la tâche ou le progrès concret que la personne cherche à accomplir dans le contexte déclaré. |
| **Blast radius** | L’étendue des consommateurs, surfaces ou décisions susceptibles d’être touchés par un changement. |
| **Preuve** | Ce qui permet de confirmer ou d’infirmer une décision dans un périmètre déclaré : observation, capture, test, mesure, comparaison ou retour adapté. |
| **Mode** | Le niveau de protection adapté au travail : `LITE`, `ITER`, `STANDARD`, `DIRECTION` ou `SYSTÈME`. Le niveau de trace (légère ou complète) se choisit à part, selon que le run est persistant, partagé ou audité. |
| **FAST-PATH** | Une vue courte pour un delta local ou une décision presque tranchée. Elle réduit la formalité, jamais la preuve requise ni l’honnêteté du statut. |
| **Façade d’activation** | Le cadrage court avant les routes détaillées : mode, risque dominant, décision à changer, prochaine preuve et owner. Elle n’est ni un nouveau mode ni un nouveau gate. |
| **Source propriétaire** | Le fichier normatif responsable d’une règle. Un guide peut la résumer, mais ne peut pas la remplacer. |
| **Run** | Un travail délimité, avec une décision, un risque, un artefact et une preuve. Il s’arrête à une proposition (trace légère) ou à une clôture (trace complète). |
| **RUN_CARD** | Projection structurée et persistante d’un run, produite lorsque les règles d’`ACTION/RUN_CARD` exigent ce format. Son exigence dépend du niveau de trace et du mode ; une proposition en trace légère ne produit pas de RUN_CARD. Les formes de clôture restent définies par `ACTION/CLOSE-PACKAGE`. Elle porte décision, risque, artefact, preuve, limite et clôture. |
| **Artefact** | Le résultat concret que l’on peut inspecter : code, écran, capture, composant, test, diff ou autre livrable. |
| **Owner** | La personne ou l’équipe responsable de la décision, de la reprise ou de l’escalade. |
| **Scope** | Le périmètre réellement couvert par la construction ou la preuve : vues, états, appareils, consommateurs, données ou tâches. |
| **Limite** | Ce que le travail ne permet pas d’affirmer honnêtement. Une limite n’est pas un échec caché ; elle rend le niveau de confiance lisible. |
| **Direction** | La position de design qui relie le produit, le contenu, la forme, la matière, la structure, l’action et les états. |
| **Direction artistique (DA)** | Le point de vue visuel situé qui rend une promesse, un contenu et un contexte reconnaissables ; ce n’est pas une simple ambiance ou référence. |
| **Craft** | La qualité de construction perceptible : hiérarchie, composition, typographie, matière, contenu, états et comportement. |
| **Polish** | La résolution précise des détails et comportements du rendu réel : un défaut conduit à un geste concret, conditionné et réinspecté (`SAVOIR/STATE`), sans accumulation d’effets décoratifs. |
| **Créativité située** | Un écart, une relation ou une reformulation qui apporte une réponse spécifique et utile ; ce n’est pas la nouveauté pour elle-même. |
| **Goût situé** | La sélection, la proportion et la retenue adaptées au contexte ; ce n’est pas une préférence universelle. |
| **Spécificité** | Ce qui relie le rendu au produit et au contexte au point qu’un template générique ne pourrait pas le remplacer sans perte. |
| **Thèse** | La position de design en une phrase : ce que la proposition affirme sur le produit et sur la personne à qui elle s’adresse. |
| **Ancre** | Une référence réellement regardée (observée, fournie ou générée) qui calibre une décision visuelle ; on note ce qu’on en retient, ce qu’on écarte et sa date. |
| **Creative Boot** | Le cadrage court fait avant le premier pixel d’une décision visuelle ouverte : promesse, objet de preuve, geste, `MODAL`, `PARTI`, tension, `FABRICATION` et premier objet. |
| **`MODAL`** | Ce que n’importe quelle IA produirait par défaut pour ce brief (structure, palette, typographie, assets), nommé pour pouvoir le garder ou s’en écarter en connaissance de cause. |
| **`PARTI`** | La décision prise face au `MODAL` : le garder ou s’en écarter, à quel endroit et pour quelle raison liée à la thèse. |
| **`FABRICATION`** | Le bilan des moyens réels (assets, marque, polices, composants, génération, contenu) et du niveau atteignable couche par couche avant le build. |
| **Plafond** | Le niveau qu’une couche peut atteindre avec les moyens disponibles ; lorsqu’il est bas, l’agent le déclare et dit ce qui le relèverait. |
| **Objet de preuve** | L’élément de la première scène qui rend la promesse crédible : de préférence un composant, une donnée, un état ou une interaction du produit. |
| **Défaut dominant** | Le défaut qui pèse le plus sur la qualité perçue ou sur l’usage ; c’est lui que l’on corrige en premier. |
| **Trace légère** | La trace par défaut d’un run ni persistant, ni partagé, ni audité : six lignes au plus (mode ; thèse ; modal, trame et parti ; plafond atteint et contenus marqués ; défaut dominant restant, rendu comme revue de présence lorsque la qualité perceptuelle est en jeu ; prochaine preuve). Le run livre une proposition, sans verdict ni clôture. |
| **Trace complète** | La trace d’un run persistant, partagé, audité ou dont on demande l’acceptation : handoff, paquet de clôture, gates écrits et projection selon `ACTION/CLOSE-PACKAGE`. La forme courte LITE définie par `ACTION/HANDOFF` est complète sans RUN_CARD ; elle ne se confond pas avec la trace légère. |
| **Première proposition** | Le premier rendu, présenté avec sa thèse et ce qu’il faut décider. Il vaut checkpoint, sauf action irréversible ou coûteuse. |
| **Livraison** | La remise d’un artefact à une personne : la première proposition (trace légère ; elle vaut checkpoint) ou la remise acceptée (trace complète). Les preuves applicables au mode sont dues dans les deux cas ; seule leur écriture s’allège en trace légère. |
| **Trame modale** | L’ordre de sections que n’importe quelle IA produirait pour un brief. Le test de trame la nomme, puis la rompt ou la justifie par la tâche. |
| **Profil de surface** | Le type de surface (vitrine, application, scène, hors Web) qui fixe les contrôles d’accessibilité à faire d’office. |
| **Vérité de scène** | La règle qui marque comme illustratif tout exemple, chiffre ou témoignage non observé, et qui le signale au public en langage produit. |
| **Slop** | Une production générique, répétitive ou trompeuse faite avec peu de soin ; le slop procédural est une trace remplie sans décision réelle. |
| **Premier objet** | L’élément qui rend la direction visible et utile dans la première proposition : objet, scène, composant, interaction ou relation de contenu. |
| **Boucle d’amélioration** | Après la première proposition, observer le réel, isoler le défaut dominant, modifier l’artefact, observer à nouveau et décider ; une critique textuelle seule ne constitue pas une correction. |
| **Gate** | Un contrôle ciblé, avec une preuve ou une condition adaptée. `A/B/C` désignent des familles de contrôles ; ils ne constituent pas une note globale. |
| **Axes V/U/A/T** | Les questions de preuve : caractère visuel ; compréhension et usage observables dans la tâche déclarée ; accessibilité ou conformité ; robustesse technique. |
| **État (`STATE`)** | L’étape du cycle de vie du run, de `INTAKE` à `CLOSED`. Il ne signifie pas que le résultat est accepté. À ne pas confondre avec la route `SAVOIR/STATE`, qui traite du craft et des états, ni avec le statut de direction. |
| **Issue (`ISSUE`)** | L’issue ou la condition de traitement qui affecte le run, par exemple `BLOCKED`, `RETURNED` ou `EXPLORATORY`. |
| **Verdict (`VERDICT`)** | La conclusion globale sur le périmètre observé : `ACCEPTED`, `ACCEPTED-WITH-RESERVATION`, `RETURN`, `RETURN-DIRECTION`, `EXPLORATORY` ou `SYSTEM-ESCALATION`. Les résultats d’axes peuvent utiliser `PASS`, `PASS-WITH-RESERVATION`, `RETURN`, `NOT-VERIFIED` ou `N/A-JUSTIFIED`, mais ils ne sont pas des verdicts globaux. |
| **Statut de direction** | La fidélité de la direction dans le rendu : `HELD`, `HELD-WITH-ACCEPTED-DIFFERENCE`, `PARTIALLY-HELD` ou `LOST-IN-BUILD`. Il ne remplace pas le verdict global. |
| **`DECISION-INTENT`** | La décision que la procédure doit permettre de trancher au lancement du run. |
| **`DECISION-CHANGE`** | La décision effectivement changée, confirmée ou abandonnée grâce à une observation. Sinon, les valeurs de repli d’`ACTION/STATUS` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, avec la raison ; `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée. |
| **`TRACE-LOCATOR`** | Le repère qui permet de retrouver la trace persistante du run : ticket, manifeste, fichier, espace de travail ou autre emplacement déclaré. |
| **`CLOSED`** | La trace et les artefacts sont persistés. Cela ne signifie pas automatiquement « réussi » ou « vérifié ». |
| **`NOT-VERIFIED`** | Une propriété importante n’a pas été vérifiée dans le périmètre ou avec les capacités disponibles. |
| **`NOT-OBSERVED`** | Une conséquence attendue, un changement ou un résultat n’a pas été observé dans le périmètre déclaré. |
| **`N/A-JUSTIFIED`** | Une preuve ou un contrôle n’est pas applicable, avec une justification explicite. |
| **`SPECCED`** | État canonique du cycle de run : la direction, la hiérarchie, le contrat ou l’ancre nécessaire sont suffisamment spécifiés pour permettre le passage à `BUILDING`. Ce n’est ni un verdict, ni une preuve de qualité. |
| **`READING_MAP`** | Carte dérivée qui indique le premier chemin, les perspectives conditionnelles, les sorties et les locators ; elle ne crée aucune règle normative. |
| **Locator** | Repère stable permettant de retrouver un fichier, une section, une trace ou un artefact déclaré. |

## Exemples express

Ces exemples illustrent l’usage des termes ; ils ne créent pas de règle supplémentaire.

| Terme | Exemple concret |
|---|---|
| **Décision** | « Garder la structure du formulaire, mais rendre le premier geste compréhensible sur mobile. » |
| **Preuve** | « Comparer le rendu avant/après à 390 px, puis vérifier le focus clavier dans le scope déclaré. » |
| **NOT-VERIFIED** | « Le contraste a été inspecté ; aucun test avec lecteur d’écran n’a été exécuté. » |
| **DECISION-CHANGE** | « `CHANGED` — après observation à 390 px, la décision « deux CTA de même poids » est remplacée par un CTA principal unique (observation : capture avant/après). » |
| **N/A-JUSTIFIED** | « Aucun test de préférence n’est applicable : la décision porte ici uniquement sur la robustesse du composant. » |
| **CLOSED** | « La trace et les artefacts sont persistés. `CLOSED` ne dit rien du verdict : un run peut être clos en `RETURN`. Clos en `ACCEPTED-WITH-RESERVATION`, il porte une réserve complète (owner, portée, date ou version, impact, prochaine preuve, date de revue, condition de sortie). Une protection critique restée `NOT-VERIFIED` exclut `ACCEPTED`, pas la réserve ; une protection en échec (`FAIL`) exclut tout verdict accepté. » |

## Pour commencer sans vocabulaire préalable

Cette suite s’adresse à l’opérateur ou à l’agent ; une personne qui fait une demande n’a pas de mode à choisir (section « Commencer » du README du package).

1. Classez la demande avec `DIRECTION/START` : mode et risque dominant ; notez la décision à changer, la prochaine preuve et l’owner.
2. Chargez la ligne de ce mode dans `DIRECTION/CHARGE`, puis seulement le propriétaire normatif utile.
3. Produisez ou modifiez l’artefact, puis observez-le dans le scope déclaré.
4. Isolez le défaut dominant, corrigez l’artefact lorsque c’est nécessaire, observez à nouveau et séparez ce qui a été observé de ce qui reste non vérifié.

La direction est la position globale ; la direction artistique en est l’expression visuelle située. Le craft décrit la qualité de fabrication, le polish sa résolution cohérente, et la spécificité le lien non interchangeable avec le produit et le contexte.

Si deux lecteurs raisonnables choisissent des modes très différents, il faut clarifier le périmètre ou le risque au lieu de masquer le désaccord derrière le vocabulaire.
