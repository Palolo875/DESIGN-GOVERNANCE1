# Notes du coordinateur — six essais U6

Ces notes ne sont montrées ni aux producteurs ni aux juges. Les sources des deux conditions sont figées ; aucune correction du système n'est introduite entre deux essais.

## Mesures et limites

Les caractères sont ceux servis par `lire.py`, avec les en-têtes produits par le lecteur du paquet. Les intervalles sont réunis par clé de requête. Une route sous un autre nom peut contenir du texte déjà rencontré ; le décompte n'est pas une déduplication sémantique. Le compteur ne démontre ni la compréhension ni la quantité de texte réellement retenue dans le contexte. Les lectures directes des schémas, scripts ou autres fichiers autorisés ne sont pas comptées. Aucun jeton API n'est disponible. Les anciennes mesures U5 ne sont donc pas directement comparables.

La mesure « avant premier HTML » utilise l'existence de `index.html` au moment d'une lecture. Elle ne date pas la première réflexion, la préparation de code en mémoire ou un autre fichier. La durée démarre au marqueur du coordinateur avant le lancement et termine à réception du résultat ; elle comprend les outils et l'attente de service, et exclut les contrôles du coordinateur. Le modèle exact du service, ses graines et ses variations internes ne sont pas attestés.

L'accès aux seuls fichiers autorisés est une consigne attestée par les producteurs, pas une isolation technique entre agents. Les deux juges sont aveugles à la condition et aux résultats techniques, mais appartiennent à la même famille de modèles. Six pages et deux briefs donnent des observations descriptives, pas un effet causal général.

## Contrôles des six livrables

- run-01 : 24 contrôles indépendants passent sur trois largeurs. Le producteur a conservé ses échecs intermédiaires et les corrections. Les preuves finales et le paquet sont intacts.
- run-02 : 27 contrôles passent ; trois échouent sur le bouclage Tab/Maj+Tab de la fenêtre modale après validation. Le diagnostic complémentaire observe une sortie vers l'interface du navigateur, avec `document.hasFocus() = false`, et non une interaction avec le contenu derrière la modale. Cela échoue au contrat local de confinement du focus retenu pour la comparaison ; ce résultat seul ne constitue pas un audit WCAG complet. Les autres parcours, calculs et téléchargement passent. Le producteur annonçait ses propres 14 parcours réussis ; son observation de BODY n'avait pas une assertion de confinement équivalente. La validation de RUN_CARD porte sur la forme, pas la réalité de chaque comportement.
- run-03 : 27 contrôles indépendants passent sur trois largeurs. Les captures initiales et les observations des corrections sont conservées. Les preuves finales et le paquet sont intacts.
- run-04 : 27 contrôles indépendants passent sur trois largeurs. Le premier test du coordinateur attendait le retour au CTA après validation alors que le produit place le focus sur le résultat `#success`. Cette attente trop spécifique produisait trois échecs ; elle est corrigée sans changer la page. Le rapport initial et l'intervention sont conservés. Le journal d'audit initial mentionnait à tort le clavier modal ; l'intervention et le second audit rectifient cette erreur. Le clavier modal passait déjà.

- run-05 : 30 contrôles indépendants passent sur trois largeurs à la reprise ; les artefacts étaient déjà complets avant l’erreur de limite d’usage. Aucun nouveau tour producteur.
- run-06 : 39 contrôles indépendants passent sur trois largeurs, dont erreurs, jour indisponible, créneaux au clavier, reprise, récapitulatif local et remise à zéro. Captures finales inspectées et paquet intact.

Les six pages n'ont ni débordement horizontal à 1440, 390 et 320 px, ni erreur de script ou requête externe dans les scènes et parcours contrôlés. Le lien de marque `href="#"` est un retour en haut natif ; le signal automatique « ancre non résolue » n'est pas un lien mort dans ce cas. Les observations de petites cibles et de focus ne sont pas des verdicts automatiques d'accessibilité exhaustive.

## Lectures supplémentaires déclarées

Les runs 04, 05 et 06 déclarent une lecture de la skill cloud `c2/setup`, imposée par une instruction de priorité supérieure transmise aux agents. Elle se trouve hors du périmètre de lecture défini par la consigne expérimentale. Aucune lecture croisée d'une autre version ou d'un autre résultat n'est déclarée. Les trois premières traces ne renseignent pas une lecture de cette skill : son absence ne peut être attestée. Cette différence et les lectures techniques directes ne sont pas incluses dans le compteur du lecteur DG. L'étude n'est pas présentée comme une égalité vérifiée de tout le contexte reçu.

## Interruption d’usage du run-05

Le cinquième tour producteur s'est terminé sur une erreur de limite d'usage. Les fichiers finaux existaient déjà : les derniers sont datés de 13:56:53 UTC. La reprise du coordinateur à 16:06 UTC a constaté ces fichiers complets ; aucun nouveau tour de production ni quatrième correction n'a été lancé. Le parent a exécuté 30 contrôles indépendants, tous réussis, validé la carte stricte et inspecté les captures. Le tour en erreur reste déclaré, les artefacts ne sont pas remplacés. Le temps mural complet jusqu'à réception à la reprise est conservé ; il n'est pas comparé au sixième essai. La date de fichier n'est pas présentée comme une durée de calcul attestée. L'heure exacte de réception de l'erreur n'avait pas été enregistrée.

## Marqueur de lancement rectifié

Le premier marqueur de run-05 a été écrit avant la correction de l'attente du test de run-04 ; aucun agent n'avait été lancé. Un second marqueur valide précède le lancement effectif. Les deux restent dans le journal avec l'explication. La consolidation utilise le dernier marqueur de début, et ne compte pas ce délai de contrôle comme un coût du producteur.

## Dérogation documentaire du run-02

Le producteur a remplacé ses premières captures PNG aux mêmes chemins pendant ses corrections. Il a signalé cette limite ; le source avant les dernières corrections et des rapports intermédiaires subsistent. La série initiale complète n'est pas reconstituable et n'est pas présentée comme conservée. Les captures indépendantes finales sont valides. La consigne remise aux producteurs n'explicitait pas le versionnement de chaque PNG aussi précisément que le protocole privé ; elle n'est pas modifiée au milieu de l'expérience.

## Réparation pratique séparée

La copie corrigée de la page A ajoute un bouclage clavier calculé sur les contrôles visibles et activés. Elle passe 30 contrôles indépendants, et ses six captures statiques sont identiques octet pour octet aux originales. Cette correction manuelle est hors de la comparaison et du coût de production. La page brute et son échec restent dans les résultats ; les juges reçoivent les captures brutes.

Le défaut de cette page ne suffit pas à prouver qu'une règle a disparu du système. La règle de focus est présente dans les deux paquets. Une validation de schéma réussie et une liste de contrôles déclarés ne garantissent pas le parcours ; les observations et assertions doivent être consultables.

## Galerie de revue

Le premier contrôle de la galerie a buté sur le nom accessible du select « Pages » dont le label englobait les options. La galerie reçoit des labels explicitement associés par `for`/`id` ; aucun PNG ni livrable brut ne change. La version et le constat initiaux sont conservés. La galerie finale passe ses 23 contrôles : cinq groupes, deux largeurs de capture, deux vues, puis absence de débordement du conteneur à trois largeurs. Ces contrôles portent sur l’outil de revue, pas sur la qualité des pages.

## Jugements reçus

Les deux juges ont livré un Markdown et un JSON après inspection déclarée des 24 captures. Les ordres et les fichiers vus sont contrôlés ; le coordinateur vérifie les empreintes des deux dossiers anonymes. Chacun préfère F à A, E à C et D à B avec une confiance moyenne, et conserve ses réserves. Ces avis ne remplacent pas le choix du propriétaire. Les deux déclarent aussi la lecture de la skill cloud héritée, sans autre workflow de design ni lecture de dossiers voisins.

## Finition mobile de B corrigée séparément

Les deux juges signalent la faible séparation des mentions de prix et des boutons flèche dans B. L’inspection du PNG brut puis le contrôle des rectangles de texte confirment un chevauchement sur trois lignes à 390 et 320 px, absent à 1440. La copie B permet le retour à la ligne de la petite mention dans sa colonne. Le contrôle des rectangles passe aux trois largeurs et les 39 parcours passent à nouveau. Les captures complètes mobiles changent ; les premières scènes et les captures desktop restent identiques. Le brut, les captures anonymes et les jugements sont conservés. Cette réparation manuelle reste hors de l’expérience et de son coût.

## Consultation du propriétaire

La galerie et les questions ont été proposées pendant la fin des jugements, au lieu d’attendre leur réception complète. Aucun avis du propriétaire ni retour de l’autre juge n’a été envoyé aux juges. Le choix du propriétaire reste distinct et n’est pas déclaré aveugle : il a accès aux échanges du coordinateur. Au moment de cette livraison, aucun choix de page ni verdict de mise en ligne n’a été reçu.
