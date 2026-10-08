# Trace — landing « Souche » (SaaS de facturation)

RUN — N4-B2 — DIRECTION — direction et premier contact d'une landing de facturation — convergence SaaS générique + claims non vérifiés — captures 390/768/1440 + B1b — EXPLORATORY (proposition livrée, index.html version eed681204309)
DECISION-INTENT — choisir l'objet de preuve et la structure qui rendent la promesse « être payé sans relancer soi-même » crédible au premier regard.
OWNER — la personne (produit réel inconnu) ; agent = auteur du rendu.
DECISION-CHANGE — collisions de l’axe corrigées (v1→v2) ; graduation au jour confirmée par B1b (v2 vs variante sans graduation) puis réduite (v4) ; masse des contrôles réduite (v2).

## Boot (avant build)

- DECISION : quel objet organise la page (promesse → preuve → geste).
- PROMISE : facturer une fois ; les relances suivent jusqu'au paiement et s'arrêtent d'elles-mêmes dès qu'il arrive.
- PROOF-OBJECT : l'échéancier codé d'une facture d'exemple (F-2026-0142) : envoi, rappel, échéance, relances, mise en demeure soumise à accord, paiement qui annule la suite. TRUTH/ILLUSTRATIVE + TRUTH/MECHANISM.
- GESTURE : choisir le délai (30/45/60 j) et le scénario de paiement ; lire le message que reçoit le client à chaque étape.
- MODAL : hero promesse + capture de dashboard violette, Inter, plinthe de logos, 3 cartes bénéfices, tarifs à 3 colonnes, témoignages, FAQ ; objet central convergent pour ce brief : « facture tamponnée PAYÉE » (SAVOIR/TOOLS/CONVERGENCE, 30-09-2026) ; signal à confirmer : grotesque large sur blanc + un accent vif.
- PARTI : s'écarter de la trame et de l'objet. La page suit la vie d'une facture (envoi → échéance → relances → paiement), pas un catalogue de fonctions. Pas de facture tamponnée : la preuve est la séquence et son arrêt, pas le document. Pas de logos ni de témoignages (aucun réel disponible). Couleur par rôles issue du registre comptable (encre verte du papier listing, rouge de retard), pas un accent unique décoratif.
- STRUCTURAL-TENSION : TEMPORALITY séquencée ; PROOF-POSITION intégrée (l'objet est dans le premier écran).
- STRUCTURAL-SIGNATURE : un axe de temps gradué au jour, ancré sur l'échéance, où la position de chaque message est exacte et où le paiement coupe visiblement la suite.
- CFT-TARGETS : spécificité (relances réelles, jours ouvrés, 40 €), résolution (dates exactes, états), retenue.
- FABRICATION : polices Google Fonts atteignables (vérifié, HTTP 200) ; aucun asset de marque, photo ou contenu réel ; route CODE-NATIVE (type, données, règles, SVG/CSS) ; contenu d'exemple marqué. Plafond : structure, type, couleur, interaction au niveau ; assets figuratifs et contenu réel hors plafond ; ancre : aucune observée/fournie (EXPLORATORY).
- DOMINANT-DEFECT recherché en premier : collisions d'étiquettes sur l'axe et lisibilité mobile de la séquence.

## Cadrage (FND-03 / DOMAIN-FRAME, hypothèses)

- Public : indépendants et TPE/PME en France (hypothèse PRODUIT, inférée de la langue du brief ; coût d'erreur moyen : ton et exemples ; owner : la personne).
- JTBD : « Quand j'ai envoyé une facture, je veux ne plus avoir à surveiller ni à relancer, afin d'être payé sans abîmer la relation client. »
- trust_model : confiance = ton des relances, jamais de mise en demeure sans accord, arrêt au paiement ; destruction = relancer un client qui a payé.
- originality_tolerance : medium.
- Claims réglementaires (MODEL-KNOWLEDGE-NOT-RECHECKED, à vérifier) : indemnité forfaitaire de 40 € (C. com. L441-10, D441-5) ; délai max 60 jours ; réforme facture électronique (réception obligatoire 1er sept. 2026 ; émission TPE/PME 1er sept. 2027). Marqués « à confirmer » dans la page.

## Structure (BIBLIOTHEQUE)

- Trame modale : promesse, logos, 3 bénéfices, fonctions, tarifs, témoignages, FAQ. Rompue : promesse + échéancier (premier écran) → la souche (registre des factures) → avant l'envoi (mentions vérifiées) → tarif + essai.
- SUPPORT/ARCHITECTED_FRAME (règles, seuils, panneau échéancier) ; GRID/AXIAL pour l'échéancier (axe du temps) + GRID/COLUMN pour le reste ; SCENE/INSTRUMENT ; objet local dérivé de MICRO/ITINERARY_SEGMENTS (séquence modifiable avec conséquence) ; registre proche de MICRO/USAGE_LEDGER.
- Mobile : l'axe horizontal devient une liste verticale datée (recomposition).

## Type et couleur

- Titre comparé sur le vrai texte (etudes/specimen.png) : A Schibsted Grotesk, B Zilla Slab (mécane), C Newsreader (serif), D Instrument Sans. Retenu : B Zilla Slab pour le titre (voix de registre/formulaire, hors marqueurs de vague) ; D Instrument Sans pour texte et données (chiffres tabulaires propres ; la virgule tabulaire de Schibsted s'écarte trop : « 2 880 , 00 »). C écartée (serif de caractère = vague 2).
- Palette par rôles : papier #F5F6F1, encre #14211B, texte 2 #46534C, règles #B9CDBE, bande #E8F0E8, action #0F5B3C, retard #B42318 ; statut toujours doublé d'un texte et d'une icône.

## Trace légère (6 lignes)

1. Mode : DIRECTION, proposition EXPLORATORY (aucune ancre observée ni fournie ; pas de verdict, pas de RUN_CARD : run non persistant, aucune acceptation demandée).
2. Thèse : facturer une fois, les relances suivent et s'arrêtent au paiement → échéancier codé et gradué au jour d'une facture d'exemple → choisir délai et scénario, lire chaque message.
3. Modal / trame / parti : hero + dashboard + logos + 3 cartes + tarifs + témoignages + FAQ, objet « facture tamponnée » → rompus : la page suit la vie d'une facture (échéancier → registre « souche » → mentions vérifiées → tarif + essai) ; mécane Zilla Slab + Instrument Sans ; encre verte/rouge du registre comptable.
4. Plafond : structure, type, couleur, interaction au niveau ; assets figuratifs SANS-ASSET (aucun n'est nécessaire) ; nom, tarif, clients, montants, fonctions, conformité = exemples marqués (mention globale en pied, mentions locales sur tarif, réforme, simulation).
5. Défaut dominant restant (revue CFT-00) : retient = l'échéancier (dates exactes, jours ouvrés visibles, arrêt au paiement, mise en demeure soumise à accord) et le registre ; reste générique = bloc tarif + formulaire et grille de mentions à deux colonnes ; geste appliqué et réinspecté = « gestion du vide » (couloirs d'étiquettes 174/262 px) puis « masse visuelle » (contrôles sélectionnés en contour, graduation raccourcie) ; envisagé non appliqué = recomposer le bas de page autour d'une vraie facture du produit quand elle existera.
6. Prochaine preuve : contenu réel (nom, offre, modèles de relance du produit), regard externe sur l'ordre de lecture, test de tâche « comprendre ce qui se passe si le client paie en retard » avec 3 à 5 indépendants.

## Routes ouvertes et effet

| Route | Ouverte parce que | Effet sur l'artefact |
|---|---|---|
| DIRECTION/START, CHARGE | classer | Mode DIRECTION (premier contact de marque). |
| DIRECTION/EXTERNAL-START | brief vague | RUN-PRIORITY : vérité d'abord → marquage global + local ; pas de questions avant build. |
| DIRECTION/CREATIVE-BOOT, VISUAL_TARGET, FIRST-OBJECT | ligne DIRECTION | Boot ci-dessus ; route d'asset CODE-NATIVE/SANS-ASSET ; CTA final avec comportement local réel et limite déclarée. REUSE-CHALLENGE : aucun antécédent lisible dans le périmètre autorisé → LIMIT. |
| ACTION/FIRST-RENDER, UI-UX-REALITY | surface UI nouvelle | États construits : sélection d'étape, annulé/payé, attend votre accord, filtre du registre, erreur + reprise du formulaire, succès. |
| ACTION/RUN-DIRECTION, PIPELINE-DIRECTION, VISUAL_PROOF | ligne DIRECTION | Captures 390/768/1440 par version, états cliqués, comparaison spec/rendu. |
| ACTION/GATE-A | plancher | Contraste « Essayer » 1,01:1 détecté puis corrigé. |
| ACTION/GATE-C | craft DIRECTION | Critères relus sur capture (voir plus bas). |
| ACTION/GATE-B (+B1b), HANDOFF | atelier demandé | B1b exécuté (paire ci-dessous) ; trace légère retenue (HANDOFF). |
| DIRECTION/DOUBLE-LOOP | boucle | Une correction substantielle par défaut dominant ; test de résilience : mobile (axe → liste), états 45/60 j, contenu long des messages. |
| DIRECTION/DIRECTION-ATELIER | la tension et l'anti-choix changeaient la première scène | Moment humain = après l'envoi, l'attente ; geste = l'arrêt au paiement ; exclusion = facture tamponnée, faux dashboard ; contre-choix situé = éditeur de facture en direct (meilleur si la douleur était la création/conformité d'auto-entrepreneurs débutants). |
| DIRECTION/DOMAIN-FRAME + C01 | public et confiance inconnus | trust_model a fixé deux décisions : mise en demeure jamais sans accord ; « si le virement est parti, ignorez ce message ». |
| SAVOIR/FRAME (FND-01..03) | cadrage ambigu | JTBD écrit ; hypothèses public/claims nommées avec coût d'erreur. |
| SAVOIR/CRAFT (CFT-00..05) | qualité perceptuelle dominante | CFT-04a : objet de preuve au premier écran (mécanisme abstrait sans exemple) ; CFT-05 : palette par rôles + question de convergence. |
| SAVOIR/TYPE + C02 | chiffres et dates portent la preuve | Spécimen 4 voix sur le vrai titre ; Instrument Sans retenue pour les données (virgule tabulaire de Schibsted trop large) ; tabulaires retirés de « 19 € » isolé. |
| SAVOIR/STYLE | le registre pouvait changer voix et matière | PROFILE-DECISION : proche de QUIET_SYSTEM avec une voix éditoriale (EDITORIAL_PRECISION) pour le titre ; dials : matérialité basse, contraste net sur statuts, formalité moyenne ; contre-indication : préciosité éditoriale si le public est très opérationnel. |
| SAVOIR/SOURCE | ancre DIRECTION | Aucune ancre observée/fournie ; références culturelles (carnet à souches, papier listing comptable) = MODEL-KNOWLEDGE-NOT-RECHECKED ; aucun sourcing web (périmètre de fichiers restreint) → direction EXPLORATORY. |
| SAVOIR/TOOLS (CONVERGENCE, MOYENS) | nommer MODAL, choisir les polices | « Facture tamponnée » et « grotesque sur blanc + un accent » identifiés comme convergents et écartés ; vague 2 (serif de caractère, crème) écartée ; Google Fonts vérifié atteignable puis chargé en capture. |
| SAVOIR/STATE | gestes de craft | Gestion du vide, masse visuelle, chiffres, états/récupération du formulaire. |
| SAVOIR/INTEGRITY | détail final et robustesse | Test de non-récitation : chaque module ci-dessus a changé ou confirmé une décision ; claims réglementaires marqués « à confirmer ». |
| BIBLIOTHEQUE/SELECT, AVANT-SELECTION, TENSION, SIGNATURE, SUPPORT, GRID, SCENE, OBJECT, MICRO, CONTRACTS, GATE | structure ouverte | Trame rompue ; ARCHITECTED_FRAME + GRID/AXIAL + SCENE/INSTRUMENT ; objet local dérivé de MICRO/ITINERARY_SEGMENTS ; axe avec rupture « 30 jours // » pour donner 30 jours de fenêtre lisible autour de l'échéance ; mobile recomposé en liste. |
| Connexions C01, C02, C03, C07 | plusieurs propriétaires | C03 confirmé : aucun asset ne porte mieux la relation que le code → SANS-ASSET. |

Non ouvertes, avec raison : ACTION/ROUTING (aucune décision de routage ouverte) ; SAVOIR/DESIGN-ATLAS (aucune famille reliée à une décision ; pas d'asset moyen à traiter) ; ACTION/RUN_CARD, ACTION/CLOSE-PACKAGE (trace légère, pas d'acceptation ni de clôture demandée) ; C04 (erreur traitée par SAVOIR/STATE, déjà lu), C05 (aucun antécédent dans le périmètre), C06, C08, C09 (non applicables).

## Boucle d'édition

- v1 (captures/v1) : premier regard 1440 = titre, puis contrôles noirs et drapeaux de l'axe en concurrence. Défaut dominant : collisions « Relance ferme » / « Mise en demeure », boîte collée au bord. Locaux : contraste bouton menu 1,01:1 (spécificité CSS), « 2880,00 € » sans espace (U+202F absent de la police), numéros/dates coupés dans le registre.
- v2 (captures/v2) : couloirs 174/262 px, scène 346 px → collisions CORRECTED ; contrôles sélectionnés passés du noir plein au contour (masse visuelle) → l'axe devient le foyer du panneau ; contraste PASS.
- B1b (auto-comparaison, auteur du rendu, pas un regard externe) — lecture légère v2 : « outil de gestion financière sobre, registre à encre verte, preuve = instrument daté manipulable, niveau de preuve : démonstration de mécanisme ». Décision éprouvée : la graduation au jour + bandes de week-end (signature structurelle). Édition par retrait : etudes/index-b1b-variante.html, captures/v3-b1b-variante ; paire : captures/v2/capture-1440px.png → captures/v3-b1b-variante/capture-1440px.png (montage captures/b1b-paire.png). Effet : plus calme, mais on ne voit plus pourquoi la relance part un lundi ni l'écart réel entre messages ; l'axe redevient une frise d'étapes interchangeable. Résultat : décision CONFIRMÉE (original conservé). Ce que la variante a appris, appliqué ensuite par réduction (v4) : graduations courtes, bandes resserrées, traits de rappel sous les numéros.
- v4/v5 : états 60 j impayé, 45 j à temps, erreur formulaire observés ; corrigés : drapeau d'échéance contre le bord (couloirs 50/92), espaces avalés par inline-flex, « 19 € » tabulaire, libellé coupé sur mobile, points derrière le trait (v6).
- Gate C (sur v5/v6, 1440 + 390) : C1 planéité papier + bandes de registre reliées au produit (présent) ; C2 mécane + grotesque comparées, rôles fixés (présent) ; C3 lecture titre → échéancier → registre (présent) ; C4 densité forte dans l'objet, respiration autour (présent ; bas de page plus conventionnel) ; C5 planéité assumée (N/A-JUSTIFIED pour la profondeur) ; C6 résolution située : jours ouvrés, arrêt au paiement, accord avant mise en demeure, reprise du formulaire (présent).
- Gate A (recette AUTOMATED, --allow-external, version eed681204309, 2026-10-08T11:13:13Z) : PASS débordement, JS, cibles, structure, clavier, mouvement réduit, objet de preuve ; PASS-WITH-RESERVATION contraste (placeholder et pseudo-contenu non mesurés) et noms accessibles (candidats DOM). NOT-VERIFIED : lecteur d'écran réel, contraste du focus, zoom 200 %.

## Claims et vérité

- TRUTH/ILLUSTRATIVE + MECHANISM : échéancier, registre, messages, client « Atelier Morel », montants (2 400 + 480 = 2 880 ; registre 1 920 + 1 250 + 480 + 2 880 = 6 530 ; encaissé octobre 3 600), dates (calendrier 2026 réel, reports aux jours ouvrés calculés).
- Claims réglementaires MODEL-KNOWLEDGE-NOT-RECHECKED : indemnité de 40 €, mentions obligatoires, calendrier facture électronique, Factur-X ; affichés « à confirmer ». Owner : la personne / son conseil ; prochaine preuve : vérification sur impots.gouv.fr et Légifrance.
- Fonctions affirmées (rapprochement bancaire, export comptable, arrêt automatique) = exemples tant que le produit réel n'est pas connu.
