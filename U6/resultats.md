# U6 — comparaison pratique de la refonte

**État au 10 octobre 2026 : six livrables contrôlés, deux jugements aveugles reçus.** Cinq tours producteurs terminent normalement ; le cinquième tour atteint une limite d’usage après avoir écrit ses fichiers finaux. Ses artefacts sont vérifiés à la reprise, sans nouveau tour. Le choix du propriétaire reste attendu.

La refonte a fortement réduit la skill, mais ces créations complètes ne montrent pas de baisse nette du texte unique chargé. Les deux juges préfèrent les pages de l’ancienne version dans les deux paires de facturation, et celle de la nouvelle version pour l’atelier vélo. Ils observent des variations utiles, avec une architecture générale encore proche. L’objectif « plus varié, plus pro, pour moins cher » n’est donc pas établi par cet échantillon.

La comparaison porte sur les versions `99caa027` et `6e5a8c2` de Design Governance. Quatre pages utilisent le même brief de SaaS de facturation, deux par version ; deux autres utilisent le brief nouveau d'atelier vélo avec rendez-vous. Les producteurs ont commencé dans des contextes neufs, avec les mêmes moyens, et se sont succédé après les contrôles indépendants. Aucun résultat ancien U3/U5 n'est utilisé comme témoin.

Le [protocole initial](protocole.md), ses [empreintes](PROTOCOLE-SHA256SUMS), la [consigne commune](consigne-commune.txt) et la [grille aveugle](grille-aveugle.md) précèdent les générations. Leurs champs initiaux `prepared` et `generation_started: false`, ainsi que le [README du kit préparatoire](README.md), sont conservés comme état historique. Le [journal d'exécution](execution.jsonl) et l'[état courant](etat-execution.json) portent l'exécution réelle. Le kit préparatoire ne doit pas être présenté comme une archive de résultats.

## Lecture et coût

La taille de la skill passe de 44 437 à 18 852 octets, baisse technique déjà vérifiée. Dans les deux paires de facturation, l'union des caractères servis varie de +0,6 % et +0,04 %. Les caractères servis avec répétitions baissent de 2,5 % et 6,7 %. La réduction du fichier n'a donc pas produit une baisse nette du volume unique chargé pour ces quatre créations complètes.

L’atelier vélo donne +1,73 % d’union et +0,34 % de caractères servis avec répétitions. Les minutes observées pour la facturation sont 16,8 → 15,5 puis 18,7 → 18,8. Ces durées comprennent les outils et l'attente de service, et n'établissent pas un effet général. Le cinquième tour se termine sur une limite d'usage, malgré des fichiers finaux déjà présents ; la reprise vérifie les artefacts sans nouveau build. Son temps mural complet de 145,1 minutes est conservé et exclu de la comparaison de durée. Aucun compteur fiable de jetons API n'est disponible. Voir le [tableau complet](mesures.md) et le [bilan machine](bilan-observe.json).

Le [relevé de lecture](lecture-mesuree.json) compte les textes DG servis et leur union par clé, en-têtes compris. Tous les textes demandés ont été servis entièrement ; les 25 à 37 clés chargées par producteur le sont avant le premier fichier HTML. Les lectures directes des schémas, scripts, licences et instructions techniques restent hors compteur. Le repère avant premier HTML ne date pas tout le début de production. Les cibles initiales et les chiffres U5 en jetons ne sont pas validés ou remplacés par ces caractères. Le contrôle des [paragraphes exactement répétés](repetitions-observees.json) n’en trouve aucun d’au moins 250 caractères entre clés distinctes ; cela n’établit ni absence de répétition sémantique ni absence de charge cognitive.

## Parcours et réparation

Les contrôles du coordinateur sont exécutés sur 1440, 390 et 320 px, dans des contextes neufs. Ils suivent les actions présentes dans chaque page : erreurs, reprise, transmission, calcul ou créneau, clavier et résultat local. Leur nombre dépend du parcours ; il n'est pas une note de qualité. Les cartes validées en mode strict prouvent leur structure, pas la réalité de toutes les observations. Les captures et parcours contrôlés n’observent ni débordement horizontal, ni erreur de script, ni requête externe.

| Page et condition | Parcours bruts | Livrable autonome |
|---|---|---|
| F — ancien, facturation 1 | [24 réussites, 0 échec](runs/run-01/parcours-coordinateur.json) | [Sillage](runs/run-01/livrable/index.html) |
| A — nouveau, facturation 1 | [27 réussites, 3 échecs](runs/run-02/parcours-coordinateur.json) | [Folio](runs/run-02/livrable/index.html) |
| C — nouveau, facturation 2 | [27 réussites, 0 échec](runs/run-03/parcours-coordinateur.json) | [Trait](runs/run-03/livrable/index.html) |
| E — ancien, facturation 2 | [27 réussites, 0 échec](runs/run-04/parcours-coordinateur.json) | [Pli](runs/run-04/livrable/index.html) |
| D — nouveau, atelier vélo | [30 réussites, 0 échec](runs/run-05/parcours-coordinateur.json) | [Rayon](runs/run-05/livrable/index.html) |
| B — ancien, atelier vélo | [39 réussites, 0 échec](runs/run-06/parcours-coordinateur.json) | [Rayon libre](runs/run-06/livrable/index.html) |

La page A échoue au confinement local du focus dans la modale, après validation, sur les trois largeurs. Le diagnostic observe une sortie vers l'interface du navigateur ; il ne démontre pas une interaction avec l'arrière-plan ni une non-conformité WCAG exhaustive. La copie corrigée dans [corrections/A](corrections/A/index.html) passe 30 contrôles, avec six captures statiques identiques aux originales. L'original et ses trois échecs restent dans la comparaison. La règle de focus est présente dans les deux paquets ; ce défaut ne démontre pas une perte de règle dans la refonte.

Sur E, le premier test du coordinateur exigeait à tort un retour au CTA après validation. La page place légitimement le focus sur le résultat. L'attente du test est corrigée sans changer la page ; les deux rapports et la rectification du journal sont conservés.

Les deux juges relèvent aussi une mention de prix trop proche du bouton sur B. L’inspection et le [contrôle ciblé](runs/run-06/prix-coordinateur.json) confirment un chevauchement sur trois lignes à 390 et 320 px. La [copie corrigée B](corrections/B/index.html) permet le retour à la ligne dans la colonne de prix : [absence de chevauchement](corrections/B-prix.json) aux trois largeurs et [39 parcours réussis](corrections/B-parcours.json). Les captures complètes mobiles changent ; les premières scènes et les vues desktop restent identiques. L’original et les avis sur ses captures restent conservés. Les deux réparations manuelles sont hors du coût mesuré et du jugement aveugle.

## Jugement visuel

Les deux juges ont examiné les 24 captures finales brutes à 1440 et 390 px. Ils disposent des briefs et des noms anonymes, avec des ordres inversés, sans code, version, trace, défaut technique ni résultat de l’autre juge. Leurs rapports [juge 1](jugements/resultats/juge-1.md) et [juge 2](jugements/resultats/juge-2.md) sont conservés sans réécriture.

| Paire | Juge 1 | Juge 2 | Motif commun et réserve |
|---|---|---|---|
| F / A — facturation 1 | F, confiance moyenne | F, confiance moyenne | Champs et suivi plus concrets sur F ; A montre mieux un document fini et possède une voix typographique distincte |
| E / C — facturation 2 | E, confiance moyenne | E, confiance moyenne | Lien entre exemple, modification et bénéfices plus explicite sur E ; C explique plus brièvement les étapes |
| B / D — atelier vélo | D, confiance moyenne | D, confiance moyenne | Jour, heure et nature du dépôt visibles sur D ; B offre des choix plus spacieux et des prix plus immédiats |

Les deux juges trouvent les différences F/E utiles pour distinguer une entrée par la saisie d’une entrée par le document obtenu. Dans A/C, les empattements et la présentation sélective du parcours changent le ton et la quantité de contenu visible. Ils constatent toutefois la proximité de la séquence générale : promesse et document, fonctionnement, offre, questions, action finale. Ils n’infèrent pas les interactions à partir des captures.

L’[inventaire de styles calculés](inventaire-visuel.json) complète ces avis sans note de qualité : les six corps utilisent Manrope ; cinq titres principaux utilisent Manrope, celui d’A utilise Instrument Serif. Les palettes et les détails varient, mais l’échantillon ne montre pas une diversification générale des architectures. Le choix des moyens communs et les briefs succincts limitent également ce constat.

La [galerie autonome](Galerie-U6.html) permet de revoir les paires et les répétitions, sur ordinateur et mobile, en première scène ou page entière. Ses [23 contrôles](audit-galerie/galerie-verification.json) vérifient l’outil de revue. La préférence du propriétaire sur R1 à R4 et R9 reste distincte : **avis demandé, non reçu au moment de cette livraison**. Aucun verdict de mise en ligne ne lui est attribué.

## Limites à conserver

Les producteurs ont une restriction de lecture par consigne, sans sandbox individuel. Les runs 04, 05 et 06 ainsi que les deux juges déclarent une lecture supplémentaire de la skill cloud héritée, de priorité supérieure. L'égalité de tout le contexte reçu n'est pas attestée. Le modèle parent est hérité sans override ; l'identifiant exact du service et ses graines internes ne sont pas attestés. Deux juges de la même famille constituent un aveugle imparfait.

La première série de PNG du run-02 a été remplacée par le producteur pendant ses corrections. Le source intermédiaire et des rapports restent conservés, ainsi que les captures finales indépendantes ; la série initiale complète n'est pas reconstituée. Le cinquième tour en erreur n'est ni masqué ni remplacé ; ses fichiers complets ont été vérifiés à la reprise. Voir les [notes du coordinateur](notes-coordinateur.md) et l'[interruption](interruptions.json).

Six pages et deux briefs donnent une comparaison descriptive. Ils ne prouvent ni efficacité générale, ni significativité, ni acceptation d'une marque réelle. Les contenus et fonctions sont des exemples locaux, sans réservation, envoi ou paiement réels. L'anglais reste reporté et la PR du produit reste ouverte vers `main`.

## Conséquences pour le plan et les preuves

La livraison technique de phase 5 et l’exécution de cette comparaison sont terminées. L’objectif de coût des créations complètes et la supériorité visuelle générale restent non établis ; le choix du propriétaire reste ouvert. Les prochaines améliorations doivent examiner les routes réellement nécessaires et leur moment de chargement, puis la diversité des décisions adaptées au brief. Une suppression de règle utile ou une préférence de police imposée ne découle pas de ces résultats. Aucun changement du système n’a été introduit entre les six productions.

La branche documentaire `refonte` reçoit le bilan, les pages, les captures, les jugements et les outils. Elle omet les six paquets source extraits et les TTF communs ; les licences et leurs empreintes restent. L’archive complète `Resultats-U6.zip` contient aussi ces paquets exacts et les polices. Les HTML de livraison embarquent leurs polices et se consultent seuls. Les scripts de rejeu nécessitent Python, Playwright 1.56.0, Chromium et les chemins de runtime déclarés ; aucune portabilité automatique de ce runtime n’est revendiquée.

Après extraction de l’archive complète, `python verifier-preuves.py` vérifie les empreintes avec des chemins relatifs. Sur la branche documentaire, utiliser `python U6/verifier-preuves.py U6 --documentation`. Ce contrôle ne rejoue pas les parcours et ne certifie pas les préférences. Les empreintes de l’archive et de chaque fichier sont vérifiées lors de l’export ; le kit préparatoire initial reste une livraison distincte.
