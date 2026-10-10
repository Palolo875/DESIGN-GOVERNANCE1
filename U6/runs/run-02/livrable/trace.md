# Run-02 — première proposition, Design Governance V1

Date : 2026-10-10. Producteur : agent run-02. Owner de fabrication : agent ; owner de la décision produit : demandeur, indisponible pendant le run. Autorité : construire et tester une proposition locale réversible ; aucun envoi, paiement ou déploiement. Aucun autre run consulté.

## Avant construction

MODE DIRECTION ; DECISION : la première page doit-elle convaincre par un document manipulable plutôt que par un tableau de bord ? RISK : confondre hypothèse de produit et service disponible ; preuve minimale : facture illustrée, action locale, captures desktop/mobile, erreur puis récupération, parcours clavier ; arrêt : proposition complète observée, risques restants déclarés, au plus trois corrections sur captures.

Brief connu : « Il me faut une landing page pour notre SaaS de facturation. » Hypothèses : langue française, indépendants et petites activités de service, produit fictif nommé Folio, offre illustrative. Public, identité, fonctions et tarification réels inconnus. Plafond : prototype local, pas de preuve de marché ni de conformité fiscale.

Thèse : rendre le travail administratif tangible et calme — promesse de clarté → facture avec détail et total → composer une facture d’exemple. Alternative située : vue dense de pilotage des encaissements, écartée au niveau de la phrase car elle répond d’abord au suivi plutôt qu’à la première facture. Cette alternative n’est pas un rendu comparé.

MODAL : titre centré, double CTA, logos, dashboard décoratif, trois bénéfices égaux, tarifs, FAQ. PARTI : garder une navigation courte et le genre landing ; déplacer l’objet de preuve dans la première scène, sans logos ni avis fictifs, puis montrer le fil de la facture avant l’offre.

TENSION-AXES : respiration/compression, preuve intégrée/latérale. Pôles retenus : respiration dans le discours, précision dans le document latéral. Effet attendu : lire la promesse puis comprendre le calcul avant les arguments. Owner agent ; scope hero et facture ; reprise si le document devient secondaire ou illisible en mobile.

VISUAL_TARGET : support page claire ; grille asymétrique à deux masses, titre puis facture ; scène promesse/document/action ; objet facture de service à une ligne et total HT/TVA/TTC. Silhouette : grande voix de titre face à une feuille compacte, puis bande sombre de parcours et fin d’action. Opération dominante : la donnée et sa conséquence partagent le même objet. Planéité avec une frontière nette pour le document, sans faux asset photographique. Matière CODE-NATIVE : HTML/CSS du document, aucun asset figuratif ni tampon officiel. Typographie candidate : Instrument Serif pour le titre, Manrope pour l’interface et chiffres tabulaires ; alternative Manrope sur le vrai titre à comparer sur capture. Palette par rôles : fond #f7f8f2, encre #172d2b, action #172d2b, champ de preuve #e4ecce, texte secondaire #52625c, frontière #a0aca0, signal d’exemple discret et explicite. Pas de statut porté par la couleur seule.

Ancre : aucune ancre observée ou fournie. La composition sera une hypothèse construite et auto-observée ; elle ne sert pas d’ancre d’acceptation. Direction EXPLORATORY, pas de verdict accepté. Aucun antécédent autorisé à lire ; aucune réutilisation d’un run précédent.

Calibration locale : largeur 1240px, marges 40–64px desktop / 20px mobile ; titre 88px / 56px ; facture 440px maximum ; cibles 44px minimum ; données de service 1 × 850 € HT, TVA illustrative 20 % = 170 €, TTC 1 020 €. Sur mobile : discours, CTA, facture dans cet ordre ; contenu long coupe sur les mots, chiffres et unités restent liés. Sans asset : texte et document portent seuls la promesse.

CONTENT-MODEL : produit d’exemple, promesse, document, parcours de statuts, offre illustrative, FAQ et démo. PRIMARY-TASK : ouvrir une démo, compléter une prestation et afficher son exemple calculé. États : nominal rempli, formulaire vide/erreur, reprise, succès local ; unavailable pour un vrai compte/envoi ; loading N/A (calcul synchrone local), disabled N/A (pas d’action conditionnellement désactivée), succès partiel N/A. Saisie conservée lors de l’erreur. Clavier : dialog natif, labels, focus visible, erreur liée, Escape et retour au déclencheur. Données en mémoire seulement. Pas de persistance ni de collecte.

Gate A attendu : Web, base WCAG 2.2 AA, captures Chromium 1440×1000 / 390×844, débordement 320px, contrastes calculés sur fonds opaques, sémantique, cibles, clavier et erreurs inspectés. Méthodes AUTOMATED et MANUAL par auteur. Limite : aucune certification, aucun lecteur d’écran ni utilisateur représentatif. Preuve suivante : revue par demandeur et tâche utilisateur sur vrai contenu.

## Sources utiles lues intégralement

Sources de Design Governance V1 dans `/workspace/remesure-phase5/runs/run-02/paquet`, via lecteur instrumenté `/workspace/remesure-phase5/lire.py` et pagination jusqu’à fin :

- `agent/skill/SKILL.md` : noyau complet, vérité et première proposition.
- `agent/chemins.md` : DIRECTION/START/TREE, DIRECTION/CHARGE (mode), DIRECTION/CREATIVE-BOOT, ACTION/RUN-DIRECTION, DIRECTION/DOMAIN-FRAME.
- `design/direction/cadrer.md` : DIRECTION/EXTERNAL-START, hypothèses en absence de personne.
- `design/direction/diriger.md` : DIRECTION/VISUAL_TARGET, spec et plafond d’ancrage.
- `design/direction/premier-objet.md` : DIRECTION/FIRST-OBJECT, objet avant arguments et CTA effectif.
- `design/savoir/typographie.md` : SAVOIR/TYPE, voix comparées et résilience.
- `design/produit/premier-rendu.md` : ACTION/FIRST-RENDER, ACTION/UI-UX-REALITY, états et scope.
- `V1/sections/ACTION.md` : ACTION/PIPELINE-DIRECTION, alternative et revue sur rendu.
- `design/produit/preuve-visuelle.md` : ACTION/VISUAL_PROOF, limites des captures.
- `design/produit/plancher.md` : ACTION/GATE-A, calculs et contrôles applicables.
- `design/produit/finition.md` : ACTION/GATE-C, ACTION/ATELIER-EDITION, édition comparée.
- `agent/repondre.md` : ACTION/HANDOFF, trace persistante et réponse.
- `design/savoir/fondements.md` : SAVOIR/FRAME/COMPOSITION et SAVOIR/FRAME/SINGULARITE, objet spécifique au métier.
- `design/formes/choisir.md` : BIBLIOTHEQUE/READ, BIBLIOTHEQUE/SELECT, BIBLIOTHEQUE/TENSION ; responsabilité des deux masses et rejet des cartes de bénéfices.
- `design/formes/catalogue.md` : BIBLIOTHEQUE/SEQUENCE, séquence promesse/document → parcours → offre → FAQ → action/colophon.
- `design/savoir/qualite-creative.md` : SAVOIR/CRAFT/CFT-05 (couleur) et CFT-00 (revue créative).
- `design/savoir/composition.md` : SAVOIR/STATE, chiffres tabulaires, masses et récupération après erreur.
- `gouvernance/verification.md` : ACTION/GATE-B, comparaison d’auteur et absence de regard indépendant.
- `gouvernance/travail.md` : ACTION/RUN_CARD, projection persistante.
- `gouvernance/cloture.md` : ACTION/CLOSE-PACKAGE, preuve fraîche et limite d’acceptation.
- `V1/sections/SAVOIR.md` : SAVOIR/INTEGRITY, aucune observation inventée.
- `design/savoir/gout-et-tendances.md` : SAVOIR/TOOLS/CONVERGENCE ; marqueurs internes datés, pas de claim de fréquence dans la page.
- `gouvernance/structure.md` : BIBLIOTHEQUE/CONTRACTS, dimensions et états de la forme locale.

Colonne conditionnelle de DIRECTION : DOMAIN-FRAME ouvert (métier ambigu) ; FRAME, BIBLIOTHEQUE, SEQUENCE, CFT-00, CFT-05, STATE, INTEGRITY ouverts car décisions effectives ci-dessus. DOUBLE-LOOP écarté : boucle commune déjà lue, arrêt et diagnostic déterminés. ACTION/ROUTING écarté : route connue. DIRECTION/DIRECTION-ATELIER écarté : tension/objet déjà établis par les sources propriétaires. STYLE écarté : aucun catalogue d’apparences nécessaire. SOURCE écarté : pas d’asset ni de référence culturelle. CFT-03 écarté : pas de texte sur image, geste de masse disponible dans STATE. Lecture de connexions écartée : relations déjà résolues par sources utiles. B1b hors acceptation ; une comparaison d’édition sera conservée sans claim de regard indépendant.

Ressources retenues : fichiers `/workspace/remesure-phase5/moyens/manrope.ttf` et `instrument-serif.ttf`, licences OFL lues intégralement ; intégration locale data URL, notices incluses dans le HTML et jointes. SVG uniquement icônes fonctionnelles explicitement décoratives.

## Observations, corrections et clôture

Version livrée : SHA-256 `e6d5ed677986691617d1d3314a12c33990e62b79ec8eaf82337440dc3960e45a`. Captures finales et parcours : Chromium 151.0.7922.173, Playwright Python 1.56.0, le 2026-10-10. Deux tours de correction du produit après capture ; une comparaison typographique réversible en complément. Toutes les écritures sont dans le livrable, hors journaux techniques du lecteur autorisés. Aucun sous-agent, service réel, requête externe, compte, paiement ou envoi.

### Revue créative sur captures

Lecture légère sans rationale : page de facturation à nom proposé, centrée sur un document de service, avec démonstration plutôt que preuve de clients. Présence : le titre en trois lignes équilibre la masse rectangulaire de la facture desktop. Spécificité : prestation, quantité, montant HT, TVA d’exemple, total TTC et recalcul attachent le foyer au métier. Culture visuelle : aucune référence culturelle observée, donc non revendiquée. Généricité restante : split landing, FAQ et formule unique restent des conventions ; elles servent respectivement la relation discours/document, les limites d’usage et l’offre inconnue. Résolution : les erreurs conservent les champs, la reprise conduit à un total cohérent et le téléchargement porte le marquage d’exemple.

Atelier d’édition : `desktop.png` / `type-alternative-desktop.png`, puis `mobile.png` / `type-alternative-mobile.png`. Variable principale : voix de l’accroche, Instrument Serif 88/59px contre Manrope 74/49px et graisse 600, sur le titre identique. L’alternative sans serif est lisible et plus compacte ; la voix serif est conservée car elle reprend la voix du document et différencie le discours des contrôles Manrope sans modifier leur usage. Effet observé : le titre conserve trois lignes aux deux formats et le CTA reste lisible. Ce choix est une auto-comparaison, pas une préférence humaine ou un regard indépendant. La paire finale porte le même état et les mêmes données. B1b n’est pas requis pour accepter ici, car aucune acceptation n’est visée ; paire persistée volontairement.

Geste anticipé de STATE : chiffres tabulaires et alignement du total ; dans le parcours 1 234,56 € HT + 246,91 € de TVA = 1 481,47 € TTC, aperçu et téléchargement concordent. Geste de reprise : erreurs locales, saisie conservée, focus sur premier champ erroné puis succès local. Les captures `error-desktop.png`, `error-mobile.png`, `focus-error-390.png` et `long-invoice-detail.png` rendent ces états consultables.

Correction 1 : observation de lisibilité et contrôle DOM ; agrandir le pied de document de 9 à 10px, donner un espace au texte sous hero, étendre le landmark main aux cinq sections et choisir un focus clair sur fond sombre. Effet réinspecté : un seul main contenant cinq sections, contenu d’exemple plus lisible, focus de 3px sur le champ en erreur et sur les contrôles de parcours. Le produit conserve sa silhouette.

Correction 2 : `long-mobile.png` montrait initialement une date tassée par le nom de client long. Modifier la relation de colonnes, par grille `minmax(0,1fr) 105px`, et conserver la date sur une ligne. `long-invoice-detail.png` réinspecté : client sur plusieurs lignes, date entière « 10 octobre 2026 », montant et total lisibles. Aucun débordement mesuré à 320px après contenu long.

Limite de journal des captures : les réexécutions de `verify.py` ont régénéré les captures nominales au même chemin, plutôt que conserver chaque première capture. La source d’avant correctifs reste dans `before-final-corrections.html.txt`, la recette intermédiaire dans `gate-a-render-before-meta-correction.json`. Les comparaisons de voix finale utilisent deux captures distinctes actuelles ; les correctifs précédents sont documentés par le source et les observations, sans prétendre disposer d’une paire initiale complète. Pour une prochaine reprise, donner un dossier distinct à chaque version.

### Gates, couverture et limites

Gate A : recette versionnée `scripts/check_render.py`, exécutée avec `--serve-local --widths 320,390,1440 --proof '#proof' --browser-executable /usr/bin/chromium --json gate-a-render.json`. La première tentative d’arguments utilisait une syntaxe incorrecte, puis le chargement file:// a été bloqué par le navigateur ; ces tentatives ne sont pas des PASS. La voie HTTP locale temporaire a exécuté la recette, puis a été arrêtée. Rapport final rattaché à version `e6d5ed677986`, après correction 2 : débordement externe/interne, erreurs JS, cibles, lang/titre/h1, parcours clavier et mouvement réduit observés sans défaut signalé. Contraste et noms DOM : PASS-WITH-RESERVATION pour les exclusions détaillées dans le JSON. Objet de preuve mobile partiellement visible dans le premier écran : réserve géométrique maintenue, recomposition observée et choisie ; le CTA précède le document, le total demande de défiler. Aucun claim d’efficacité utilisateur ne découle de cela.

Complément `supplementary-checks.json` : treize paires sRGB de rôles opaques calculées, toutes au-dessus du seuil fixé ; texte secondaire/fond 6,031:1, erreur locale/fond 7,275:1, focus clair/fond 6,394:1, focus sombre/fond 10,987:1, frontière input/blanc 3,768:1. Chargement des deux polices attesté dans Chromium. `accessible-dialog.txt` expose dialog, labels, contrôles et alert dans l’arbre accessible calculé ; le nom des inputs reprend aussi leur aide car le label englobe l’aide. Aucun lecteur d’écran exécuté. Pseudo-contenus, opacity des petits numéros, exhaustivité des noms et tous les cas de contraste restent hors certification. Aide, statut et erreur ont un texte, pas seulement une couleur.

Parcours réellement exécutés : `functional-tests.json` contient 14 cas, chaque cas avec selectors/actions/observations/résultat. Action principale ouvre le dialog et cible client ; trois erreurs affichées et saisies conservées ; correction avec noms longs et décimales ; téléchargement lu ; retour à modification ; Escape restitue le focus ; nominal et long à 320px ; erreur de montant sur mobile ; Tab/Shift+Tab/Enter/Escape ; parcours de statuts ; FAQ avec Enter ; reduced-motion ; aucune requête externe ni erreur JS. La succession Tab du dialog contient un arrêt transitoire BODY dans Chromium avant de revenir au bouton fermer : le test atteste les contrôles atteignables et le retour de focus, sans annoncer un piège de focus exhaustif multi-navigateurs. Aucun PASS inventé pour un parcours non exécuté.

Gate B : comparaison de la spec à la page desktop entière, mobile entière, états et détail ; ancre fournie/observée NOT-VERIFIED ; contexte produit réel et tâche utilisateur NOT-VERIFIED ; revue indépendante absente. Alternative de position dense écartée au niveau phrase ; alternative de voix réellement capturée. Direction PARTIALLY-HELD dans le scope de fabrication et issue EXPLORATORY : la promesse est matérialisée, sa pertinence au produit réel reste à établir.

Gate C, jugement d’auteur borné aux captures finales : C1 surface de document et de calcul découle du métier ; C2 voix comparées sur texte réel ; C3 premier foyer discours/document et CTA puis parcours ; C4 contraste de densité titre/document et changement de rythme sombre ; C5 planéité retenue, seule ombre plate du document pour séparation ; C6 récupération du montant erroné puis total/download cohérents. Aucun de ces constats ne prouve une préférence humaine. Verdict global EXPLORATORY ; V PASS-WITH-RESERVATION, U NOT-VERIFIED, A PASS-WITH-RESERVATION, T PASS uniquement pour les parcours et largeurs déclarés.

Creative close : présence par titre/feuille, signature par calcul manipulable, craft par erreur récupérable et colonne de date résistante. Défaut dominant restant : direction proposée sur un public hypothétique et sans identité réelle ; la preuve tangible mobile est séquencée après l’action. Prochaine action : fournir les contenus et faire observer la première facture par un indépendant représentatif ; pas de polish supplémentaire avant cela.

Grounding : nécessaire pour public, prix, conformité et disponibilité d’un service ; sources réelles absentes et réseau externe interdit. Effet : retirer tous claims réglementaires, chiffres de performance, intégrations, témoignages et clients réels ; marquer fonctions et prix comme exemples. Résiduel : produit réel, noms, public et offre inconnus. Demandes groupées pour la vraie version : 1) public et fonctions réelles ; 2) nom/identité existante et droits ; 3) offre et destination réelle des CTA. Le nom proposé et les données ne sont pas des marques ou personnes acceptées.

Handoff : artefact `index.html`, source embarquée autonome ; méthode et preuve ci-dessus ; trace `trace.md`, projection `run-card.json`. La route `gouvernance/schemas/run_card.example.json` a été refusée par le lecteur de routes ; l’exemple référencé par ACTION/RUN_CARD et le validateur ont alors été lus directement à leur chemin complet autorisé dans le paquet. Projection validée avec `gouvernance/outils/validate_run_card.py run-card.json --strict` : validation de forme réussie, sans convertir cela en preuve de design. Paquet persistant CLOSED, issue/verdict EXPLORATORY, aucune direction identitaire acceptée. Owner de reprise : demandeur pour les décisions produit, agent pour intégration et nouvelles vérifications. Condition de reprise : vrais contenus disponibles et choix de direction demandé. Condition d’arrêt : prototype complet, défaut de colonnes corrigé, risques bornés et réserves persistées. Tous les serveurs temporaires sont arrêtés.
