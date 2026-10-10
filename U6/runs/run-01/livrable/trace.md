# Run 01 — première proposition

Début : 2026-10-10 12:24:26 UTC. Producteur : agent run-01 ; responsable de la prochaine décision de marque : personne porteuse du SaaS. Autorité : produire une proposition locale réversible, sans publication, service, paiement ni sous-agent. Aucun précédent consulté.

RUN — run-01 — DIRECTION — rendre le geste de facturation tangible au premier contact — risque important : page SaaS interchangeable ou démonstration prise pour une capacité réelle — scope : une landing française et sa facture d’exemple, desktop/mobile — artefact attendu : index.html — prochaine preuve : captures et parcours du formulaire — limite : aucun contenu de marque ou produit réel — arrêt : prototype complet vérifié, proposition exploratoire livrée.

DECISION-INTENT : vérifier qu’une facture éditable, reliée à un total exact et à un aperçu local, porte mieux la promesse qu’un dashboard décoratif.

## Cible avant build

- Hypothèse de public : indépendants et petits studios de services en français. Pas de connaissance établie de l’audience réelle. JTBD : comprendre l’outil, essayer de préparer une facture, juger l’offre.
- Thèse : « Le projet est livré. La facture aussi. » Le produit suit le travail, sans interrompre sa continuité. Promesse → facture d’exemple calculée → modifier une prestation et préparer son aperçu. Ce mécanisme est une hypothèse, pas une preuve de disponibilité.
- Position retenue : instrument accessible et direct ; masses vert pâle et encre sombre, document blanc, données précises. Alternative : promesse centrée suivie d’un tableau de bord de revenus. Écartée au niveau d’une description, car ni données réelles ni aperçu global ne justifient ce tableau ; la facture répond directement au besoin.
- MODAL : promesse / logos / trois cartes de bénéfices / tarifs / FAQ ; palette neutre avec accent, titre grotesque ou serif expressive. PARTI : garder la simplicité de l’action et la lisibilité ; rompre l’ordre en plaçant l’instrument métier dans la première scène, sans logos ni chiffres de performance inventés.
- Séquence : comprendre et manipuler une facture → lire le chemin du brouillon au suivi → choisir une offre illustrative → lever les questions → essayer de nouveau. Le milieu est une séquence linéaire, pas trois cartes égales.
- Tensions : PROOF-POSITION intégrée (l’objet répond à la promesse et permet le geste) ; DENSITY respiration au discours / précision dans la facture. Effet attendu : titre et geste évidents sans effacer les données. Reprise si la preuve monopolise la scène ou devient illisible sur mobile.
- Silhouette : texte large à gauche, facture à droite dans un champ continu ; pas de screenshot. Le volet produit blanc distingue action et discours. Au mobile : texte → action → éditeur recomposé ; aucun tableau comprimé.
- Matière : CODE-NATIVE, champs, lignes, total et document. Pas de photographie, illustration ou faux logo client. Planéité du champ, petite ombre seulement pour distinguer le document du contexte.
- Typographie : comparer Manrope et Instrument Serif sur le vrai titre ; corps et données Manrope, chiffres tabulaires ; titre 68/72 px desktop, 42/44 px mobile. Voix finale à confirmer sur spécimen et capture. Police locale intégrée, licence OFL conservée.
- Palette par rôles : champ #e8f1ed, texte #173c32, actions #d7ed9f sur encre, document #fff, frontières #b9c9c0, erreurs #9c2929 ; états accompagnés de texte. Contrastes à calculer.
- Objet : client, prestation, quantité, prix HT, taux de TVA illustratif, total TTC ; référence d’exemple, deux dates cohérentes, état brouillon. Local TRUTH/ILLUSTRATIVE + TRUTH/MECHANISM, interface : « Démonstration locale · données d’exemple ». Aucun envoi ni paiement.
- Contrat local : document interactif comme preuve, uniquement dans cette proposition ; 44 px minimum pour champs/actions ; titre et client longs doivent se replier ; aperçu dans dialog natif, focus et Escape ; champs invalides gardés et erreurs à proximité. Pas de promotion de composant partagé.
- Résolution : ouverture remplie ; modification de champs, recalcul, erreurs, reprise, aperçu, fermeture ; pas de loading (calcul synchrone), unavailable explicite pour envoi, ni compte/permissions requis. Pas de sauvegarde serveur.
- FABRICATION : HTML/CSS/JS, SVG illustratifs autorisés mais inutiles ici ; Manrope et Instrument Serif fournis, OFL lue ; ressources et contenu réels absents. Plafond : structure, typo, couleur et interaction inspectables ; marque, adéquation au public, conformités et intégrations non vérifiées. Aucun asset externe.
- Ancre : absente de sources observées ou fournies. La cible est une hypothèse autonome, pas une ancre déclarée. Direction EXPLORATORY ; aucune acceptation identitaire.
- Défaut fragile anticipé : objet plus dense que le discours, largeur étroite des champs. Geste préparé : réduire une masse secondaire plutôt qu’ajouter du décor ; remonter le total auprès des champs et recomposer les deux colonnes sur mobile.

## Contrôle prévu

Web, cible de travail WCAG 2.2 AA ; aucune certification. Méthode : Playwright/Chromium, DOM et CSS, clavier exécuté, captures inspectées par le producteur. Échantillon : page entière 1440×1000 et 390×844, débordement 320 px, états nominal/erreur/aperçu/focus. Budget : aucune requête externe ; police embarquée, pas de motion décorative. Hors scope : AT, Safari/Firefox, participants, produit réel, conformité réglementaire des factures.

## Sources entièrement lues et décisions utiles

Racine propriétaire : `/workspace/remesure-phase5/runs/run-01/paquet/`. Les routes sont résolues par `/workspace/remesure-phase5/lire.py`, avec pagination jusqu’à lecture terminée. Skill entière : `/workspace/remesure-phase5/runs/run-01/paquet/agent/skill/SKILL.md` (contenu reçu via `skill`, chemin confirmé dans le paquet).

| Routes lues | Source complète sous la racine | Conséquence |
|---|---|---|
| DIRECTION/START, CREATIVE-BOOT, DOMAIN-FRAME, ACTION/RUN-DIRECTION | agent/chemins.md | Mode DIRECTION, public hypothétique, démarrage avant code |
| DIRECTION/EXTERNAL-START | design/direction/cadrer.md | Vérité locale, démonstration avant bénéfices |
| DIRECTION/VISUAL_TARGET | design/direction/diriger.md | Spec, silhouette et plafond, absence d’ancre |
| DIRECTION/FIRST-OBJECT | design/direction/premier-objet.md | CTA réel local, pas d’inscription fictive |
| SAVOIR/TYPE | design/savoir/typographie.md | Comparaison de voix, figures tabulaires |
| ACTION/FIRST-RENDER, UI-UX-REALITY | design/produit/premier-rendu.md | États et récupération au premier build |
| ACTION/PIPELINE-DIRECTION | V1/sections/ACTION.md | Observer, retirer/réduire, comparer avant arrêt |
| ACTION/VISUAL_PROOF | design/produit/preuve-visuelle.md | Captures de page et états au scope déclaré |
| ACTION/GATE-A | design/produit/plancher.md | Contrastes calculés, clavier et vérité |
| ACTION/GATE-B | gouvernance/verification.md | Auto-comparaison, absence de regard indépendant |
| ACTION/GATE-C | design/produit/finition.md | Composition, densité, état métier sur rendu |
| ACTION/HANDOFF | agent/repondre.md | Trace complète car run persistant et partagé |
| ACTION/RUN_CARD | gouvernance/travail.md | Projection structurée et limites séparées |
| ACTION/CLOSE-PACKAGE | gouvernance/cloture.md | Livraison exploratoire persistée, pas d’acceptation |
| SAVOIR/INTEGRITY | V1/sections/SAVOIR.md | Pas de preuve inventée, relier aux captures/tests |
| SAVOIR/CRAFT/CFT-00 | design/savoir/qualite-creative.md | Revue courte liée à une intervention |
| SAVOIR/TOOLS/CONVERGENCE | design/savoir/gout-et-tendances.md | Marqueurs considérés comme signaux, aucune tendance affirmée |
| BIBLIOTHEQUE/SELECT, TENSION | design/formes/choisir.md | Objet intégré, différence de densité |
| BIBLIOTHEQUE/SEQUENCE, GRID/HIERARCHICAL, SCENE/PRODUCT_NARRATIVE, OBJECT/PROOF_PRODUCT_STAGE | design/formes/catalogue.md | Première scène calculable et séquence linéaire |
| BIBLIOTHEQUE/CONTRACTS | gouvernance/structure.md | Contrat local calibré aux champs, états et mobile |

Modules conditionnels : DOMAIN-FRAME, SELECT, SEQUENCE et CFT-00 ouverts car audience/structure/revue changent l’objet. DOUBLE-LOOP et STATE appliqués depuis le noyau (pas de double lecture). ROUTING écarté : aucun conflit de route. ATELIER écarté : promesse→objet→geste déjà explicite. FRAME écarté : hypotheses suffisantes pour une proposition locale. CRAFT supplémentaire écarté : gestes précis disponibles dans le noyau et CFT-00. SOURCE écarté : aucun claim externe, droits et calculs bornés. STYLE écarté : relation type/champ/document résolue par le contrat, pas de catalogue à choisir. CFT-03 supplémentaire écarté avant rendu : n’approfondir que si le geste de réduction échoue. INTEGRITY ouvert avant verdict. Grounding externe interdit par les moyens ; contre-hypothèse : le vrai produit vise les PME avec multi-devises et conformité réglementaire, ce qui changerait preuve et discours ; aucune affirmation de ce scope dans la démo. Réemploi non applicable : aucun précédent lu ou disponible dans le scope.

La commande `mode DIRECTION` a été essayée : option non proposée par cette version (erreur `--mode`). Aucun paquet modifié ; classification par START et chargement de la ligne DIRECTION de la skill.

## Observations et clôture

### Observation et décisions réellement prises

Premier build observé à 1440×1000, 390×844 et 320×844 : catégorie perçue sans lire la rationale, « outil de facturation pour indépendants, marque calme et directe, preuve illustrative par une facture saisissable ». Le document et son total dominent le regard ; la marque est une hypothèse, aucun signal client réel.

Revue CFT-00 : présence portée par le champ continu et le document blanc ; spécificité par les jours, montant HT, TVA, échéance et geste de préparation ; culture visuelle externe N/A-JUSTIFIED (aucune référence observée, aucun transfert culturel affirmé) ; élément encore générique : split discours/outil et offre en abonnement ; défaut dominant initial : les deux petits arguments sous le bouton répètent le geste et retardent le document sur mobile. Intervention : retirer entièrement ce groupe, sans ajout compensatoire.

Atelier d’édition, tour 1 : comparaison `captures/before-1440-first.png` / `captures/after-1440-first.png` et équivalents 390. Le document apparaît environ 90 px plus tôt sur mobile ; il garde ses données et son action. Sur desktop le texte se recentre plus bas par rapport au document ; respiration conservée, foyer toujours évident. Décision CHANGED : supprimer les arguments secondaires. Diff visible dans index.html ; pas de variante de palette décorative. Corrections de résolution concomitantes : glyphe ↗ mal rendu dans la police remplacé par → ; labels et note de démonstration mobile rendus plus lisibles. La paire prouve cette réduction, pas une préférence indépendante.

Spécimen `captures/type-study.png` : Manrope et Instrument Serif sur « Le projet est livré. La facture aussi. », corps et action réels. Manrope retenue après observation : même voix entre titre et chiffres, formes plus stables et directes à taille mobile. Instrument Serif écartée : caractère éditorial plus distinct du document, sans besoin de cette distance dans ce brief. Les deux voix restent lisibles ; aucune supériorité universelle ni effet utilisateur affirmé. Manrope était provisoire au premier build, choix confirmé sur le spécimen et la capture. Police française, ponctuation et chiffres constatés ; figures tabulaires dans les totaux ; fallback Arial présent mais non comparé.

Tours 2 et 3 : parcours réels révélant un arrêt de focus sans élément actif dans la modale (Tab après le dernier bouton) puis le lien d’évitement masqué au retour en haut depuis le bas de page. Corrections : boucle explicite Tab/Shift+Tab de la modale ; lien d’évitement fixé au viewport lorsqu’il reçoit le focus. Le test clavier attend maintenant la fin du scroll animé avant mesure : les premières mesures instantanées avaient aussi marqué des champs hors viewport pendant cette transition. Archives honnêtes dans `functional-tests-initial.json` (31 réussites, 2 échecs) et `functional-tests-second.json` (32 réussites, 1 échec). Les arrêts sans focus visible sont corrigés dans la dernière version ; aucune preuve initiale réécrite en réussite. Frontières de champs renforcées de #99afa1 à #789486 pour le contraste non textuel. Trois tours de correction au total, aucun quatrième build.

La repasse finale a inspecté `captures/final-1440-first.png`, `captures/final-390-first.png`, `captures/final-390-full.png`, les captures d’erreur 390/320, l’aperçu 390 et le contenu long 390. Le rythme entier, l’objet, les statuts textuels et la fin de page tiennent. Aucun débordement document constaté aux trois largeurs. Les états d’erreur gardent les valeurs et une action de reprise ; le nom/prestation longs sont complets dans l’aperçu, avec retour à la ligne. Le titre fait deux lignes à 390 et trois à 320, coupe sémantique lisible. Pas de diminution de l’usage, de la hiérarchie ou de la robustesse observée après les corrections.

### Preuve applicable et limites

- Runtime : Chromium local par Python Playwright. `capture_page.py` et `verify.py` lancent chacun un serveur 127.0.0.1 à port éphémère, puis l’arrêtent en `finally`. Aucun serveur laissé actif. CSS/JS et Manrope en data URL dans index.html ; aucune ressource externe requise.
- `functional-tests.json` : 33 cas effectivement exécutés, 33 résultats locaux PASS, aucune exception d’exécution ni erreur JS. Ils couvrent nominal, overflow et cibles ≥44 px, action principale, quatre erreurs simultanées, reprise, recalcul, aperçus, Escape et retour du focus, taux 0 %, noms/prestations longs, Tab de page, Tab dans modale, FAQ Enter, préférence de mouvement réduit, téléchargement local et requêtes. Chaque cas garde sélecteurs, actions et observations ; ce chiffre ne signifie pas une conformité globale.
- Le téléchargement a réellement produit `download-observed.txt` avec client et total testés, et la mention « PAS UNE FACTURE FISCALE ». Aucun envoi ou paiement exécuté.
- Contrastes : 99 échantillons textuels et valeurs de champs sur fonds unis opaques, plus faible ratio 4,83:1 (numéros de séquence sur blanc) ; aucun cas échantillonné sous son seuil. Méthode, couleurs, corps et seuils dans functional-tests.json. Les erreurs et leur focus sont aussi inspectés sur captures ; pas de conformité totale inférée.
- Contraste non textuel : ratios calculés dans `supplemental-contrast.json` pour bord de champ et anneau de focus. Pas d’icône essentielle sans texte. Toute couleur de statut porte un libellé.
- Probe body `font-size:200%` réellement exécuté mais insuffisant pour le zoom : la majorité des corps sont définis en px, ce probe ne prouve pas leur agrandissement. Zoom navigateur réel NOT-VERIFIED ; cette limite est conservée sans prétendre une conformité.
- Chromium seulement ; AT, Safari/Firefox, chargement sur appareils réels, utilisabilité avec participants, pertinence commerciale et conformité de facturation NOT-VERIFIED. L’échantillon automatisé de contraste ne mesure pas toutes les combinaisons d’AT ou les fonctionnalités d’un vrai produit.
- Regard : SAME-AUTHOR, auteur du rendu = agent run-01 ; revue non aveugle, exposition au code et au brief ; aucun conflit commercial connu, aucun évaluateur externe. Les captures et les décisions sont une auto-comparaison.

### Gates et handoff

Gate A : PASS-WITH-RESERVATION dans le scope décrit : calculs, états, sémantique des champs, cibles et focus exécutés, contenu honnête, absence de réseau externe ; zoom/AT et compatibilité élargie non vérifiés. Gate B : PASS-WITH-RESERVATION comme auto-comparaison et parcours du prototype ; ancre réelle, public et préférences non vérifiés. Gate C : PASS-WITH-RESERVATION sur les captures indiquées : C1 document et champ lié au métier ; C2 voix comparées ; C3 séquence du calcul vers l’aperçu ; C4 réduction des arguments secondaires ; C5 planéité intentionnelle, ombre du document seulement ; C6 erreur/reprise et contenu long observés. Aucun gate ne vaut acceptation de marque.

Axes : V PASS-WITH-RESERVATION (composition observée, ancre absente), U PASS-WITH-RESERVATION (tâches locales exécutées, public/usage réel inconnus), A PASS-WITH-RESERVATION (plancher échantillonné, AT/zoom incomplets), T PASS (autonomie et runtime Chromium local au scope exécuté). État de livraison CLOSED ; issue et verdict EXPLORATORY ; direction PARTIALLY-HELD, faute de contexte de marque et de produit. L’absence d’ancre ne devient ni FAIL-ASSUMED ni acceptation implicite. `run-card.json` sérialise cette limite et le paquet de clôture ; validation de forme distincte des preuves.

Creative close : présence = encre sombre, champ calme et document clair dans les captures finales ; signature = relation jours/prix/TVA/total puis aperçu ; détail de craft = récupération de quatre erreurs avec saisie gardée et focus retourné au bouton ; défaut dominant restant = l’offre et la séquence de suivi sont génériques tant que le produit réel manque ; STOP polish — demander le contenu et les capacités avant une nouvelle direction. Aucune nouvelle retouche attendue ne peut remplacer ces informations.

Prochaine action : personne porteuse du SaaS fournit (1) nom/identité et public cible, (2) fonctions réellement disponibles et destination du CTA, (3) offre et preuves autorisées. Prochaine preuve : confronter cette proposition au vrai parcours et faire tester l’action par un utilisateur de la cible. Condition de sortie : page et claims réécrits sur ces contenus, puis tests AT/zoom/compatibilité et validation de direction par le responsable réel. Pas de publication autorisée ou exécutée.

DECISION-CHANGE — CHANGED : retrait des arguments secondaires, focus de modale et lien d’évitement corrigés après observation. CONFIRMED : la facture locale porte bien le geste et le total au scope observé. Preuves : paire before/after, captures finales, functional-tests.json et index.html.

Sources de distribution et preuve supplémentaires : `/workspace/remesure-phase5/runs/run-01/paquet/gouvernance/schemas/run_card.example.json`, `/workspace/remesure-phase5/runs/run-01/paquet/gouvernance/schemas/run_card.schema.json`, `/workspace/remesure-phase5/runs/run-01/paquet/gouvernance/outils/validate_run_card.py` ; police `/workspace/remesure-phase5/moyens/manrope.ttf` (SHA-256 3ae11c49db0455a3cc33e37d380f20fdb8c7f8b41dc07625c177e3d87a9d6ae6), licence `/workspace/remesure-phase5/moyens/OFL-manrope.txt` copiée dans le livrable ; voix étudiée `/workspace/remesure-phase5/moyens/instrument-serif.ttf`, licence `/workspace/remesure-phase5/moyens/OFL-instrument-serif.txt` entièrement lue. Fonts non modifiées. Aucun droit de marque réelle prétendu.

Incident technique : le premier script nommé inspect.py masquait le module Python standard du même nom, empêchant Playwright de démarrer. Renommé capture_page.py ; observations faites uniquement après démarrage réussi. Aucun test de navigateur annoncé à partir de cet échec.

Fin : 2026-10-10 12:40:14 UTC, soit 15 min 48 s depuis le début instrumenté. Limite de vingt minutes non dépassée. Validation stricte de run-card.json exécutée avec le validateur du paquet : RUN_CARD VALIDATION PASSED ; cette réussite ne prouve que la forme et les invariants contrôlés, pas les qualités externes déclarées non vérifiées.

Inventaire : index.html, response.md, trace.md, run-card.json, functional-tests.json, functional-tests-initial.json, functional-tests-second.json, supplemental-contrast.json, download-observed.txt, OFL-manrope.txt, capture_page.py, verify.py, dossier captures (nominal avant/après/final, erreurs, aperçus, contenu long et comparaison typographique). Tout le livrable et les scripts sont dans le dossier autorisé. Les journaux du lecteur sont instrumentés par lire.py, hors responsabilité d’écriture du producteur.
