# Notes de lecture fiche 10 (brouillon)

## validate_all.py (190 l.)
- Ordre: py_compile tous scripts; build_core --check; validate_design_governance; validate_run_card (suite); validate_contracts (suite); validate_reading_map; validate_structure; check_craft_regressions; test_core_budget; test_read_route; test_audit_regressions; test_preparer_livraison (si présent); test_check_render (--require-browser optionnel); read_route DIRECTION/START; --trouver "Cohérence de rayon" -> SAVOIR/STATE; expect_failure locator inconnu; contracts domain_frame; run_card example; 4 fixtures en CLI; strict avec chemins réels; strict refuse placeholder; JSON malformé; fichier absent; build_distributions x2 + sha256 identiques (reproductibilité).
- expect_failure: exige échec, pas de Traceback, motif attendu => qualité des tests (pas juste "échoue").
- check_craft_regressions: LCF-46 halo: "halo" de production (détourage) admis ; "halos décoratifs", "halo violet" non datés rejetés => le système interdit de citer un marqueur de mode (vague IA) sans date [VEILLE]. 3 mutations de SAVOIR dans copie temporaire (mauvais propriétaire, gestes fermés, activation FIN-01 retirée) -> validate_structure doit les détecter.
- Aucune étape ne regarde un rendu de design réel (sauf test_check_render sur pages de test).

## package_manifest.json
- Liste close: 69 GitHub, 63 Local. Local: official/ et skill/ (chemins réécrits), sans .github, RELEASE_NOTES, build_distributions, preparer_livraison, test_preparer.
- Ajouter un fichier (ex. doc refonte, nouvel exemple rendu) = modifier manifeste + build script (copie fichier par fichier) + ... (C20).

## build_distributions.sh (316 l.)
- Verrou mkdir; owner.txt; trap cleanup.
- build_core --check; sauvegardes jamais supprimées à l'aveugle.
- Copie fichier par fichier (scripts listés à la main ; V1, skills, schemas en bloc).
- README Local généré: heredoc + blocs balisés <!-- entree --> et <!-- constitution --> du README racine (une seule source).
- Réécriture chemins V1/official/->official/, skills/design-governance-practice/->skill/ dans skill/*.md, QUICKSTART, official/README.
- Valide GitHub stage (5 validateurs), Local (manifeste + liens md + chemins `x/y.md` entre backticks), puis 5 validateurs + validate_all dans Local.
- Archives déterministes (touch SOURCE_DATE_EPOCH=0, tri C, zip -X). Membres = manifeste.
- Promotion transactionnelle avec rollback.
- Très solide. Coût: liste de scripts dupliquée en 3 endroits (manifeste, build GitHub, build Local) + validate_all scripts glob.

## validate_design_governance.py (353 l.)
- Manifeste: doublons, version = CHANGELOG ("**Version expérimentale :** `V1.0.0`"), titres des 4 docs portent V1.0.0.
- Inventaire clos: fichier attendu absent / inattendu ; liens symboliques refusés (C20 : refonte/ refusé).
- Liens relatifs + fragments (ancres GitHub reconstruites, pas parseur complet).
- ACTION doit citer run_card.example.json et ne contenir aucun bloc ```json/yaml.
- Valeurs STATE/ISSUE/VERDICT/DIRECTION-STATUS canoniques dans tous les .md (lignes "STATE: X").
- STATE: HELD interdit.
- PHRASES EXACTES exigées : "Les cinq fichiers suivants sont les **seules sources normatives** de V1" (official/README), "la `RUN_CARD` rassemble", "FAST-PATH" + "sixième voie" (ACTION), "section « Migration des anciens aliases » de `CHANGELOG.md`" (BIBLIOTHEQUE), "Carte de lecture par mode".
- "expérimentation maintenue" exigé dans 9 fichiers ; "version/release/distribution publique" interdit sauf négation exacte.
- Local: README ne doit pas renvoyer à GitHub comme dépendance.
- Rien sur le design.

## validate_run_card.py (1077 l.)
- Validateur maison d'un sous-ensemble JSON Schema (13 mots-clés) ; mot-clé inconnu refusé (évite ignorance silencieuse). Clés JSON répétées refusées. Pré-passe de types.
- Témoins : schéma absent/vide refusé ; mode inventé doit être rejeté ; enum du schéma fait autorité (test d'autorité).
- Règles métier (check_semantic_contract + sous-fonctions) ~45 règles : capacités exclusives ; basis ; risk.statement non placeholder ; critical interdit LITE/ITER ; protection critique (résultat FAIL → issue = failure_action ; NOT-VERIFIED → pas ACCEPTED) ; FAIL-ASSUMED → exception complète, failure_evidence ∈ observed, review_date ISO ; temps (avant CHECKING verdict null, decision_change/creative_close interdits avant observation) ; accepté → axes sans RETURN, ACCEPTED sans NOT-VERIFIED ni réserve, capability_profile, provenance.capability disponible et attestée, artifact.version = provenance.version, observed_at ISO, réserves complètes datées, droits inconnus interdisent ACCEPTED (DIRECTION), decision_change requis hors LITE, NOT-OBSERVED interdit ACCEPTED, profile observé ; RECLASSIFIED → successeur ; SYSTÈME accepté → package migration/rollback/non-régression/baseline ; DIRECTION V PASS accepté → B1b paire distincte ou N/A motivé ; DIRECTION → thèse, anti-direction, premier objet, trace, status, rights, identity_stake, ancres (sinon issue), transformées si accepté, calibration, enjeu élevé + générées seules → calibration ; creative_close à la clôture ; ITER → rappel de thèse ; LOST-IN-BUILD/PARTIALLY-HELD/issue non nulle → pas d'accepté ; observed ∩ not_verified = ∅ ; accepté → state DECIDED/CLOSED, observed, provenance complète, locator = artifact, limitation.
- Strict : placeholders exacts (8), hôtes example.*/.invalid, EXISTENCE de artifact.locator et trace_locator locaux. Rien d'autre.
- T-22 : strict PASSE avec paire B1b vers captures inexistantes (captures/premiere-scene-v1*.png) → la seule preuve visuelle exigée n'est jamais vérifiée (existence ni nature). validate_all le fait déjà implicitement (strict sur l'exemple).
- Suite : exemple ; table 25 fixtures ; 87 cas unitaires « une faute » sur base vérifiée valide d'abord (méthode excellente) ; 10 locators admis ; témoin mot-clé ; autorité.
- Placeholders en minuscules exactes: "ok", "x", "m" passent (déjà U1 : 42 champs creux).

## validate_contracts.py (486 l.)
- 2e implémentation du sous-ensemble JSON Schema (mots-clés différents : maxItems oui ; allOf/anyOf/const non). Duplication avec validate_run_card.
- Sémantique : domain_frame (contrôles ↔ plan de preuve, chaque risque couvert, contrôle connu, evidence_plan sans placeholder) ; research_brief (incertitudes, condition d'arrêt, entrée si depth≠none, décision + conséquence, date ISO/unknown, verified_in_run → locator+date) ; creative_direction_set (ids uniques, sélection existante, changements non dupliqués, directions distinctes = (tension normalisée, ensemble des changements) différents) ; ui_ux_reality_pack (couverture totale des matrices, N/A raison, OBSERVED → observed_scope).
- evaluation_case : AUCUN contrôle sémantique (schéma seul).
- 25 cas unitaires une faute ; cardinalité 4 et 8 directions ; clé répétée.
- Détection de type par clés racines.
- T-18/19/20 : forme seulement.

## validate_reading_map.py (729 l.)
- REQUIRED : 15 chaînes exactes dans READING_MAP (titres de sections, statut "guide dérivé non normatif", "ne reclassifie pas").
- Carte : locators uniques, propriétaire cohérent, destination = titre, résolution via read_route (un seul résolveur), titres porteurs uniques, tout locator cité dans official/*.md + SKILL.md résolu.
- Connexions : provenance/forme (révision = CHANGELOG).
- Témoins du lecteur (locator répété, propriétaire incohérent).
- **56 conditions de façade (LCF)** : chacune épingle une formulation, un ordre, une ligne de tableau ou un nombre (ex. « cinq paquets », « sept champs », « au plus trois », len(outs)==5) entre une source et ses copies (QUICKSTART, README, GLOSSAIRE, skill, exemples, READING_MAP). Garantit que les copies restent alignées — mais toute réécriture/simplification de ces phrases casse la validation et oblige à modifier la LCF (règle : « une entrée n'entre que par une décision écrite, avec sa mutation rouge »).
- LCF-46 (design) : liste WAVE_MARKERS = 18 marqueurs de tendance (hero SaaS, gradient décoratif, violet, Inter, halos, beige, crème, serif italique, orange rouille, bandeau défilant, illustration peinte, tramage, dithering, logos pixel, ASCII, hachures de plan, bleu Klein, paysage peint). Interdits partout hors ligne « [VEILLE 20xx] » (exception halo de détourage). T-23 : ajouter « Titre en Inter 600, accent violet sur le bouton. » à examples.md → LCF-46 échoue (exit 1). Conséquence : un exemple rendu/réaliste ne peut pas nommer la police Inter ni la couleur violet sans ligne datée.
- LCF-47 objet de preuve « de préférence codé » ; LCF-43 bilan FABRICATION ; LCF-44 ordre de prise de brief ; LCF-45 MODAL/PARTI ; LCF-15/16/30 dimensions du premier objet identiques DIRECTION ↔ QUICKSTART.
- Limite déclarée : contradiction hors LCF non détectée.

## validate_structure.py (815 l.)
- 18 gardes « une chose, un lieu ». Docstring : « une reformulation ne casse pas ces gardes ; une suppression, un déplacement, une copie ou un retour du vocabulaire retiré les cassent ».
- 26 concepts protégés (balise <!-- concept:ID -->, propriétaire unique, ≥12 mots) dont design : HON-01 vérité de scène, HON-02 aucun faux asset, ANT-01 marqueurs de vague, MOY-01 carte des moyens, TRM-01 test de trame, GTA-01, ROL-01 rôle DA senior, PRC-01 tests perceptifs, EXD-01 données d'exemple cohérentes, TIT-01 équilibre d'un titre, TXI-01 texte sur image, RCV-01 récupération, ANC-01, ALT-01 alternative, FIN-01 activation du craft.
- 9 renvois (une route mène au concept en un saut).
- 37 motifs de vocabulaire retiré (ex. « anti-directions? » remplacé par MODAL/PARTI ; « Démarrage en 90 secondes » ; « toujours »).
- 65 règles de fidélité (compté par le validateur) (déclencheur → condition exigée dans le même paragraphe).
- 16 termes de glossaire obligatoires ; lignes de table uniques (≥8 mots) ; vouvoiement QUICKSTART.
- Noyau : balises appariées, uniques, sources normatives ; skill = compilation ; budget.
- Chargement unique (CHARGE) ; ordre de DIRECTION (rôle, posture, récap avant START).
- UNI-01 (design) : refuse « toujours/à tous les… » + « un seul traitement/une seule famille » → garde du pluralisme (pas de style universel).
- ENT-01 : entrée humaine unique, 4 questions exactes, aucun mode, vouvoiement ; CST-01 constitution unique (« le réel et le beau sont cadrés ensemble »).
- CORE-FLOOR : 11 phrases exactes doivent rester dans le noyau compilé (dont « Conçois une palette par rôles », « Choisis une typographie pour ses langues »).
- SKL-01 en-tête YAML ; UIX-01 déclencheur UI ; FAC-01 lignes de façades (10), exemple examples.md « fabrication depuis un brief flou » avec trace légère, pas « boulangerie » ; RELEASE_NOTES doit garder « Efficacité NOT-VERIFIED », « Aucune mesure comparative ».
- anti_direction : champ du schéma conservé, documenté comme projection de PARTI (DIRECTION l.205, ACTION l.334). Nom hérité du vocabulaire retiré ; pas une incohérence, mineur.
- C20 (test U1) : la garde FIDÉLITÉ (l.227) bloque un changement canonique non propagé.

## test_core_budget.py (90 l., 10 cas) : seuil 46 000 octets UTF-8, fichier complet, refus sans écriture, deux layouts, option inconnue.
## test_audit_regressions.py (210 l., 30 cas) : 10 mutations LCF-51..56 ; 11 cas d'ancres/liens ; 6 capacités ; hôtes stricts (11 sous-cas) ; relais du noyau. Docstring : « n'établissent ni une compréhension utilisateur ni un gain esthétique ».
## test_read_route.py (317 l.) : clôtures de code imbriquées ; recherche (accents/casse, guides opt-in, **test_no_semantic_match : l'absence de synonymes est figée par un test**) ; identifiants structurels ; connexions (doublon, champ manquant, source étrangère, révision périmée) ; CLI (codes de sortie 0/1/2, pas de Traceback) ; activation dans le noyau.
## test_preparer_livraison.py (265 l.) : restauration à l'octet, corruption refusée (même en -O), inventaire incomplet, chemins non canoniques, collisions, destinations incompatibles, symlink vers un membre de l'inventaire ou vers l'extérieur refusé ; verrou ; journal ; Local refusé ; budget canonique refusé avant build.
- C10 confirmé, non contredit : même script (RESTORE identique à restaurer_embarque.py). Le test couvre les liens vers un autre fichier de l'inventaire (collision) ou hors destination ; il ne couvre pas un lien vers un fichier interne HORS inventaire (T-02) ni un dossier lié (T-03), ni l'écrasement d'un fichier régulier différent (T-01). Angle mort exact.
