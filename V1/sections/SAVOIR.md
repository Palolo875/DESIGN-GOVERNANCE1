# SAVOIR — Bibliothèque de jugement, craft et production

**Design Governance V1 — expérimentation maintenue.** Cette V1 est un cadre de travail en évaluation ; elle n’est pas présentée comme une release publique stabilisée. Ses limites, preuves et conditions d’usage restent explicites. SAVOIR porte le jugement de design : craft, style, contenu, contexte, technique, sources, intégrité et limites de ce qui peut être affirmé.

## Responsabilité

SAVOIR explique **comment exercer le jugement** : cadrer, choisir, comparer, retirer, vérifier et reconnaître une limite. Il contient les fondations, le craft, les profils de style, la production, la veille et la gouvernance de principes.

**Capacité positive de SAVOIR.** SAVOIR transforme une impression visuelle ou une question de craft en décision située : il aide à comprendre ce qui doit être perceptible, à choisir les leviers de composition et de fabrication, à comparer des options, à retirer ce qui détourne l’attention et à formuler une limite honnête. Il augmente la précision du jugement et la qualité de l’artefact ; il ne remplace ni l’observation réelle d’ACTION, ni la décision de clôture, ni le contexte humain.

**Chemin par problème.** Charge SAVOIR lorsqu’une décision de jugement peut modifier le prochain artefact ou sa preuve : `FRAME` pour le problème, le public et le compromis ; `CRAFT` pour la composition et la fabrication ; `TYPE`, `STATE` ou `CONTEXT` pour la lisibilité, les états et les contraintes ; `SOURCE`, `STYLE`, `SYSTEM`, `TECH`, `TOOLS` ou `INTEGRITY` seulement lorsque leur question est active. Le bénéfice attendu de chaque route doit être identifiable avant son chargement.

SAVOIR ne remplace pas :

| Document | Responsabilité |
|---|---|
| `DIRECTION.md` | Rôle, cinq absolus, classification, routage général et capacité. |
| `ACTION.md` | Routes de run, preuves, gates, verdicts et maintenance. |
| `BIBLIOTHEQUE.md` | Structures, supports, grilles, scènes, objets, micro-interfaces et composants. |
| `maintenance/versions.md` | État de release, changements futurs, pilotes optionnels et décisions de gouvernance. |

> Un principe SAVOIR guide une décision ; une méthode décrit comment formuler la raison ; une preuve ACTION établit ce qui a été observé ou mesuré. Aucun principe, ancre, profil ou texte de justification ne produit seul un `PASS` d’usage, d’accessibilité ou de qualité.

---

### Orientation interne et sortie vers ACTION

`SAVOIR/ROUTING` est la carte de décision principale de ce fichier. Commencez par une seule route principale ; ajoutez une route de renvoi uniquement si elle peut modifier la décision, la preuve ou la limite. `V1/sections/READING_MAP.md` fournit une vue dérivée des déclencheurs et du non-chargement ; il ne remplace ni DIRECTION ni ACTION.

La sortie de SAVOIR n’est pas un verdict. Elle doit transmettre à ACTION la décision jugée, le principe ou la méthode utilisés, la conséquence observable, la preuve attendue, la limite, le propriétaire et la prochaine preuve. Si aucune décision ne peut changer, ne chargez pas une route supplémentaire. À la clôture, si aucune décision n’est changée, confirmée ou abandonnée, les valeurs de repli d’`ACTION/STATUS` s’appliquent : `N/A-JUSTIFIED` lorsqu’aucune conséquence n’était applicable, `NOT-OBSERVED` lorsqu’une conséquence attendue n’a pas été observée.

**Condition d’arrêt de lecture :** arrêter lorsque la question de jugement, le levier choisi, la contre-indication, la limite et la prochaine observation sont explicites.

## SAVOIR/ROUTING — routes stables

Une question possède une route principale. Les autres routes sont des renvois qui ne créent pas une seconde procédure.

| Question | Route principale | Renvoi |
|---|---|---|
| Public, JTBD, décision, compromis | `SAVOIR/FRAME` | `ACTION` pour preuve et sortie. |
| Direction, matière, composition, émotion | `SAVOIR/CRAFT` | `SOURCE` ou `STYLE` si nécessaire. |
| Langue, lecture, données, ton | `SAVOIR/TYPE` | `CONTEXT` pour accessibilité et `ACTION` pour preuve. |
| États, contenu extrême, récupération | `SAVOIR/STATE` | `CONTEXT` et `ACTION/GATE-A`. |
| Ancre, référence, asset, droit | `SAVOIR/SOURCE` | `TOOLS` pour claims et `ACTION` pour trace. |
| Profil ou dial d’expression | `SAVOIR/STYLE` | `CRAFT` et `BIBLIOTHEQUE`. |
| Token, consumer, composant partagé | `SAVOIR/SYSTEM` | `ACTION/RUN-SYSTEM`. |
| Accessibilité, responsive, performance, motion, risque critique | `SAVOIR/CONTEXT` | `TECH` ; `ACTION/GATE-A` pour le contrôle objectivable et l’axe `T` dans la portée de preuve d’ACTION. |
| Technique, compatibilité, mesure | `SAVOIR/TECH` | `TOOLS` si claim daté. |
| Source, tendance, outil, claim | `SAVOIR/TOOLS` | `maintenance/versions.md` si promotion. |
| Récitation, limite, délégation | `SAVOIR/INTEGRITY` | `ACTION` pour issue et verdict. |

---

# SAVOIR/INTEGRITY — limites, délégation et critique

### Test de non-récitation

Avant de conserver un artefact de jugement, demande : « Quelle décision concrète a changé grâce à ce module ? » Si la réponse est aucune, l’artefact est documentaire plutôt que décisionnel ; arrête ou simplifie. Une décision que le module a confirmée se déclare comme confirmation ; `N/A-JUSTIFIED` reste réservé au module qui ne pouvait rien changer.

## Modes d’échec d’application

[REQUIS PAR LE MODULE — avant verdict `DIRECTION` ou lorsqu’une règle risque d’être satisfaite dans la forme] Le danger principal n’est pas l’absence de règles ; c’est l’artefact textuel qui affirme qu’une règle a été suivie sans que décision, observation ou preuve aient réellement eu lieu.

Les échecs récurrents sont :

- mode choisi par confort ;
- directions seulement adjectivales ;
- fiche textuelle présentée comme ancre ;
- référence citée mais non observée ;
- test non rejoué après modification ;
- compromis vague ;
- retrait artificiel ;
- effet de matière choisi avant la direction ;
- feedback humain invoqué sans artefact regardable ;
- preuve de contexte produit supposée plutôt qu’établie ;
- style ou dial choisi sans décision réelle à modifier.

Avant un verdict `DIRECTION`, réponds par une phrase liée à un objet concret :

| Question | Bloque si… |
|---|---|
| Quelle ancre utile et quelle spec ont été réellement observées ? | Une ancre ou une spec est requise par le risque ou le contrat, mais aucune n’est exploitable ; si aucune ancre ne peut modifier la décision, justifie sa non-applicabilité. |
| Quelle décision perceptible porte la direction ? | Rien ne dépasse un défaut de stack ou une intention déclarée. |
| Quelle alternative située a été considérée ? | La décision est ouverte ou exposée à la convergence, mais aucune position distincte ni raison de non-comparaison n’est donnée. |
| Quel écart entre spec et rendu reste ? | Écart important ignoré ou justifié après coup. |
| Quelle preuve manque encore ? | `PASS` affirmé sans preuve adaptée. |
| Quelle hypothèse de contexte reste incertaine ? | Coût d’erreur élevé sans owner ni prochaine preuve. |
| Quelle décision concrète a changé grâce à cette procédure ? | Aucune décision modifiée, confirmée ou abandonnée, sans `N/A-JUSTIFIED` justifié ni `NOT-OBSERVED` déclaré (valeurs de repli d’`ACTION/STATUS`). |
| Quelle règle risque d’être satisfaite dans la lettre seulement ? | Aucun test d’échappatoire théâtrale ni artefact de conséquence observable n’a été fourni. |

## Contrôle d’intégrité

Relie au moins une réponse portant sur le risque le plus élevé à un artefact consultable : capture, spec, diff, test, code, URL, donnée ou journal.

Si le lien ne peut pas être inspecté, la réponse n’est pas une preuve. Si une capacité a été déléguée, inspecte l’artefact et le résultat ; la délégation seule ne constitue jamais une validation.

Lorsque la règle est satisfaite par le texte mais qu’aucun objet ou changement de décision n’est inspectable, renvoie le run à ACTION avec le couple canonique approprié : `N/A-JUSTIFIED` si le contrôle ou la décision est réellement non applicable ; `NOT-VERIFIED` si la preuve pertinente manque ; `EXPLORATORY` si un artefact existe mais que le périmètre ou la preuve de décision est incomplet ; `RETURNED` si une correction ou une preuve doit être reprise. SAVOIR rend visible la limite ; ACTION décide si le run peut être fermé.

## Limites, délégation et critique

[REQUIS PAR LE MODULE — capacité incertaine, direction ambiguë, asset critique ou besoin de second regard] Distingue ce qui est connu, inféré, vérifié et hors de portée.

Une capacité disponible modifie le type de preuve possible ; elle ne permet jamais d’affirmer une qualité sans examen du résultat. Toute délégation conserve délégataire, rôle, capacité déclarée, méthode, scope, artefact/résultat consulté, date/version, limite, owner de décision finale, `NEXT-PROOF` et condition de reprise ou d’escalade.

<!-- noyau:début VER-FAUX-ASSET -->
<!-- concept:HON-02 -->
Ne fais jamais passer abstraction CSS, SVG, image générée ou placeholder pour photo, illustration, logomark, son ou asset authentique. Une abstraction assumée est autorisée si son rôle est honnête, son contenu non trompeur et son effet approprié. Un faux asset de marque ne l’est pas.
<!-- noyau:fin VER-FAUX-ASSET -->

Le modèle, le prompt ou l’outil de génération ne constituent jamais, à eux seuls, une preuve de qualité, de droit ou d’adéquation au contexte.

La curation dirigée est admise lorsqu’elle comble un besoin réel, avec type d’origine, source/provenance, statut d’autorisation, portée d’usage, transformation, limite, owner et prochaine revue dans la trace locale du run. Ne la confonds pas avec une accumulation passive.

Les rôles de critique sont des lentilles, non une simulation d’équipe. Chaque rôle identifie un problème observable, une correction, une preuve et un périmètre. Un regard humain distinct de l’auteur ou de l’owner peut apporter un contrepoint situé ; ne le qualifie pas d’indépendant sans déclarer relation, rôle, méthode, date et limites. Active `ACTION/GATE-B/B3` lorsque son scope est requis.

L’autonomie accordée à l’agent par l’utilisateur ou l’owner couvre uniquement le périmètre `DIRECTION` explicitement annoncé. Elle ne remplace ni les droits, ni l’owner final, ni une escalade requise ; le checkpoint suit `ACTION/PIPELINE-DIRECTION` (la première proposition en tient lieu, sauf action irréversible ou coûteuse).

---

## Règles d’or — lecture rapide

Ce résumé n’est pas une procédure de livraison. Il ne crée aucune route, gate, issue ou verdict concurrent ; `DIRECTION` est propriétaire de la classification et du routage général, `SAVOIR` de ses routes de jugement, `BIBLIOTHEQUE` de ses routes structurelles et `ACTION` des routes d’exécution, preuves, gates, états, issues, verdicts et clôtures.

1. Classe le mode dans `DIRECTION/START` avant de choisir la procédure.
2. Cadre JTBD, décision dominante, contraintes et hypothèses à impact.
3. Retire avant d’ajouter ; une décision tenue vaut mieux qu’une accumulation de signaux.
4. Utilise contenu réel, états pertinents et microcopie honnête.
5. Fais passer accessibilité, responsive, récupération et performance avant l’effet.
6. Sur une surface `DIRECTION`, la spec est toujours requise ; l’ancre suit `DIRECTION/VISUAL_TARGET` (utile, ou absence déclarée en exploration ; avant l’acceptation, absolu 2 de `DIRECTION`).
7. Exécute les preuves applicables au mode ; déclare `NOT-VERIFIED` plutôt que de le noter comme `PASS`.
8. Si un risque bloquant reste, retourne, passe en `EXPLORATORY` ou journalise un `FAIL-ASSUMED` autorisé (échec connu) ; un risque non bloquant peut rester en réserve structurée (`ACCEPTED-WITH-RESERVATION`, `ACTION/STATUS`) ; ne compense jamais un axe bloquant par une moyenne.

---

## Méthodologie studio

[MÉTHODE] Le niveau de formalité dépend du mode :

- cadrage et preuve de contexte ;
- direction si `DIRECTION` ;
- système si blast radius partagé ;
- contrat de composant si pattern réutilisable ou critique ;
- assemblage ;
- repasse ciblée ;
- QA et gates applicables ;
- décision et persistance.

<!-- noyau:début BOUCLE-REPASSE -->
Une repasse complète est attendue en `DIRECTION`, recommandée en `STANDARD` et ciblée en `ITER` ou `LITE` sur le périmètre modifié. Cherche ce qui est resté par défaut : alignement optique, échelle, distance, état, composant, mouvement, contenu réel, breakpoint ou récupération. « Rendre plus fin » ou « harmoniser » seul n’est pas une résolution : nomme le geste et réinspecte son effet.
<!-- noyau:fin BOUCLE-REPASSE -->

Le système n’installe pas mécaniquement le goût. Il soutient la finesse par des gestes précis, conditionnés et réinspectés, et rend le jugement plus difficile à simuler : références observées, décisions nommées, preuves adaptées, compromis assumés et limites déclarées.

> Ce résumé et cette méthodologie aident à lire SAVOIR ; ils ne créent pas de route, gate, statut ou obligation concurrente. Les routes de jugement et de structure restent définies par SAVOIR et BIBLIOTHEQUE ; les routes de classification et d’exécution, ainsi que les verdicts, restent définis par DIRECTION et ACTION.

L’honnêteté sur ce qui manque fait partie de la qualité.
