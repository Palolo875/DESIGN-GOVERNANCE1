# Suite de la phase 5 — noyau commun, détails activés, essais pratiques

Date : 10 octobre 2026. Référence avant : `99caa027ddf08b077ab6664365df2f91e266ae66`, `R2026-10-09-COHERENCE`. Révision après : `R2026-10-10-PHASE5`. Commit après : `6e5a8c2a9016b31969051499b1c895a116fd75b4`. [CI 50](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38031656584) et [CI 51](https://github.com/Palolo875/DESIGN-GOVERNANCE1/actions/runs/38031659967) réussies sur ce SHA exact, navigateur et audit du paquet compris.

La suite technique réduit la lecture systématique en conservant les règles dans leurs sources. La gouvernance reste adaptée au risque, à la décision, à la reprise et à l’acceptation. La qualité esthétique et la variété générales restent `NOT-VERIFIED`.

## Changements et conservation

La skill passe de **44 437 à 18 852 octets UTF-8**, soit −57,6 %. En caractères : 42 866 → 18 241. Ces unités ne sont pas des jetons.

Le registre contient les 42 blocs protégés précédents, plus un bloc de relais. Vingt blocs sont communs ; vingt-trois restent servis entièrement à la demande. La compilation refuse un bloc absent, non classé, classé deux fois, une route absente, un texte incomplet ou un relais absent. Le lecteur replie seulement les blocs complets trouvés dans la partie compilée de la skill réellement installée. Un simple marqueur, une première phrase conservée ou une skill périmée ne suffisent plus.

La conservation par empreinte des corps des anciens blocs donne **39 blocs identiques, 3 blocs de chargement adaptés, aucun bloc absent**. Les trois changements sont `CHARGE-REGLE`, `CHARGE-TABLE` et `CHARGE-FIN`. Ce relevé porte sur les blocs protégés, pas sur une prétendue identité de tous les paragraphes du dépôt.

La ligne du mode vient de l’unique table `DIRECTION/CHARGE`, servie par `read_route.py --mode MODE`. L’arbre de classification et sa protection de niveau restent prioritaires. Le noyau rappelle les déclencheurs de composition, typographie, palette, sources, états et retouche sur capture. L’atelier est accessible par `ACTION/ATELIER-EDITION` dans `design/produit/finition.md` ; la preuve formelle B1b reste dans `gouvernance/verification.md`, avec son scope et ses deux exceptions. Le traitement des assets moyens rejoint `SAVOIR/SOURCE`, sans changer son texte.

La [correspondance complémentaire](../ARCHI/correspondance-phase5.csv) relève les blocs différés. La table historique de 388 sections reste un état de migration ; elle n’est pas réécrite comme si ces changements avaient déjà existé à son origine.

Aucun mode, gate, statut ou champ RUN_CARD ajouté. Aucun contrôle retiré pour atteindre un quota. Les gardes de façade acceptent une activation vérifiée au lieu d’exiger une deuxième copie de la règle.

## Vérifications

La validation complète exige le navigateur et reconstruit les deux distributions deux fois. Les tests du lecteur comptent 84 cas, ceux du budget et de l’activation 18, l’audit 68, la préparation 9. Le rendu conserve ses 55 cas A, 51 cas C et 33 pages pièges B. Les fixtures, contrats, déplacements et contrôles de référence restent inclus. Résultat local : `FULL VALIDATION PASSED`, code de sortie 0. GitHub : 108 fichiers ; Local : 103 fichiers. Les résultats effectifs et les empreintes des archives sont joints à la livraison.

Le premier précontrôle a révélé un garde qui ne reconnaissait pas l’activation de la table par `--mode`. Il a été corrigé, avec un cas positif et des mutations négatives. Les gardes continuent à vérifier les conditions dans la source propriétaire et la présence du texte entier servi.

## Mesure reproductible de lecture

La recette de chaque pilote est fixée : skill complète, classification, ligne du mode, routes du travail, détails activés et contrôles après fabrication. Une route répétée est comptée une seule fois. Le lecteur replie normalement les blocs chargés ; les en-têtes de transport sont exclus. Avant, les routes parentes disponibles remplacent les nouvelles sous-routes qui n’existaient pas. Les recettes et la liste de chaque route sont conservées en JSON.

| Cas | Avant, caractères | Après, caractères | Variation |
|---|---:|---:|---:|
| Retouche locale | 69 323 | 38 973 | −43,78 % |
| Nouveau composant de comparaison | 110 547 | 78 000 | −29,44 % |
| Autre première scène | 157 767 | 126 839 | −19,60 % |

Ce sont des comparaisons mécaniques du lecteur, pas deux exécutions indépendantes d’agents. Les détails différés sont inclus : la baisse du fichier seul n’est pas présentée comme la baisse du run entier. Les totaux incluent des contrôles après fabrication ; ils ne valident pas les cibles provisoires de lecture **avant** production (35 000 / 75 000 / 110 000). Ces cibles restent ouvertes, sans modification opportuniste du seuil ni retrait de protection. Cette recette ne mesure ni jetons, ni durée, ni charge cognitive ; les durées observées lors des nouvelles créations U6 sont documentées séparément ci-dessous.

## Trois pilotes sur la landing page Lisière

La baseline existante est conservée. Chaque pilote repart de cette même baseline ; ils ne sont pas cumulatifs. Même auteur, même contexte, mêmes images, polices, tarifs d’exemple et logique de séjour. Ce protocole permet de détecter des défauts et d’éprouver des décisions ; il ne peut isoler l’effet du système.

| Pilote | Décision et changement | Lecture et preuve |
|---|---|---|
| Retouche locale | Le bouton « Composer mon séjour » annonce mieux l’action réelle. Le statut de séjour d’exemple est lisible juste dessous. Direction et logique conservées | Classification locale, plancher ciblé, repasse du libellé ; parcours et capture étroite |
| Composant | Comparer capacités et prix des trois refuges avant leurs détails. Liens au clavier vers le panneau correspondant, sélection et refuge transmis au formulaire | Composition et singularité, sélection de structure, contrôles, états, repasse ; neuf parcours supplémentaires sur trois largeurs |
| Direction | Transformer l’entrée en une promesse typographique suivie d’un paysage architectural commun. Retirer la formule manuscrite concurrente ; aucun asset ajouté | Typographie sur le vrai titre, composition, alternatives, revue et atelier ; première scène comparée à la baseline, puis repasse mobile |

Dans les trois cas, le mode et la trace ne sont pas demandés au visiteur. Les prototypes restent des maisons et tarifs imaginaires ; aucune disponibilité, réservation ni paiement n’est simulé comme réel. L’ancre disponible est la baseline et ses assets déclarés, pas une marque réelle à accepter. L’atelier examine la transformation de la première scène ; il ne prononce aucun verdict d’acceptation identitaire.

Les quatre surfaces ont chacune 61 vérifications de parcours et 12 de résilience : débordement, polices, images, onglets au clavier, transmission du choix, capacités, focus modal dans les deux sens, erreurs et récupération de dates, total, téléchargement, mouvement réduit, JavaScript absent et ressources bloquées. Le nouveau composant ajoute neuf parcours de sélection. Les quatre HTML autonomes passent aussi le parcours « La Terrasse, trois nuits, 945 € », le téléchargement du récapitulatif, les polices et images intégrées et trois contrastes ciblés. Une seule requête document est observée, sans dépendance externe. Le navigateur cloud bloque `file://` par politique ; cette vérification utilise HTTP local et ne revendique pas une ouverture directe sur ce runtime. Aucun test de lecteur d’écran humain ni audit WCAG exhaustif n’est revendiqué.

Le premier essai du composant a rencontré un test qui attendait des images lazy avant de les faire entrer dans le viewport. L’instrumentation déclenche leur chargement, puis garde l’assertion de succès. Le test de focus attend la fermeture effective du dialogue et le retour de focus, puis utilise Tab et Maj+Tab avant de mesurer `:focus-visible` ; le focus programmatique après clic ne suffisait pas. Les captures finales utilisent des contextes neufs et un retour vérifié à `scrollY=0` ; cette précaution évite les artefacts de lien fixe dans une capture longue prise après scroll.

Appréciation de l’auteur : la retouche précise l’action ; l’aperçu rend les prix et capacités comparables mais allonge le parcours ; la variante donne davantage de place à l’architecture, au prix d’une image moins immédiate sur ordinateur. Ce sont des compromis observables, pas des notes de qualité attribuées à la nouvelle skill. Les trois variantes restent proposées pour examen ; la baseline n’est pas remplacée automatiquement.

## Comparaison indépendante U6

Le propriétaire a choisi plusieurs agents séparés et des juges aveugles. Le [protocole](../U6/protocole.md) a été figé avant les générations. Six producteurs ont commencé dans des contextes neufs, en série, avec les versions `99caa027` et `6e5a8c2` : deux répétitions du même brief de facturation par version, puis un brief nouveau d’atelier vélo par version. Aucun ancien rendu U3/U5 ne sert de témoin. Deux juges séparés examinent seulement les captures finales anonymisées, dans des ordres inversés. Le [bilan U6](../U6/resultats.md) conserve leurs avis, la [galerie](../U6/Galerie-U6.html), les parcours et les écarts au protocole. Le jugement du propriétaire sur R1 à R4 et R9 reste distinct.

| Paire avant → après | Union des caractères servis | Caractères servis avec répétitions | Minutes observées |
|---|---:|---:|---|
| Facturation, F → A | +0,59 % | −2,46 % | 16,8 → 15,5 |
| Facturation, E → C | +0,04 % | −6,69 % | 18,7 → 18,8 |
| Atelier vélo, B → D | +1,73 % | +0,34 % | comparaison exclue : interruption d’usage |

Ces [mesures](../U6/mesures.md) comptent les textes servis par le lecteur DG, en-têtes inclus, puis leur union par clé. Elles ne comptent pas tout le contexte, ne dédupliquent pas les recouvrements sémantiques entre routes et ne donnent pas les jetons API. Les producteurs ont chargé leurs routes complètes avant le premier fichier HTML ; ce repère ne date pas toute la préparation. Le périmètre diffère des recettes mécaniques de retouche de Lisière. La baisse de la skill ne se traduit pas ici par une baisse nette du volume unique pour les créations complètes.

Les six livrables passent les captures sans débordement aux trois largeurs contrôlées. Les parcours du coordinateur donnent F : 24/0, A : 27/3, C : 27/0, E : 27/0, D : 30/0 et B : 39/0 (réussites/échecs). Leur nombre dépend du parcours ; ce n’est pas un score comparatif. Le focus de la modale A sort vers l’interface du navigateur après validation. Une [copie corrigée](../U6/corrections/A/index.html), hors expérience, passe 30 contrôles et conserve six captures statiques identiques aux originales. L’original reste compté avec ses échecs. La règle était présente dans les deux versions ; une causalité liée à la refonte n’est pas démontrée.

Les deux juges préfèrent F à A, E à C et D à B, avec une confiance moyenne et des réserves : deux préférences pour l’ancienne version en facturation, une pour la nouvelle sur le vélo. Ils trouvent les variations de ton et de présentation utiles, mais l’architecture générale reste proche. Ce résultat ne valide pas une supériorité uniforme de la refonte. La mention de prix de B chevauche le bouton mobile ; la [copie corrigée B](../U6/corrections/B/index.html) résout ce défaut et passe les 39 parcours, sans changer le brut ni les captures jugées.

Le tour D termine sur une limite d’usage alors que les fichiers finaux existent déjà. Ils sont contrôlés à la reprise sans nouveau tour producteur. Sa durée murale entière de 145,1 minutes est conservée, sans comparaison. Les premières captures d’A ont été écrasées par le producteur ; des sources et rapports intermédiaires restent, sans prétendre reconstituer les PNG perdus. Les runs 04, 05 et 06 déclarent la lecture de la skill cloud héritée. Les restrictions entre agents sont des consignes, pas des sandboxes distincts. Voir les [notes](../U6/notes-coordinateur.md).

## Suite pratique après U6

Le propriétaire reporte concurrents et anglais. Le [nouveau lot](../SUITE-PRATIQUE/resultats.md) analyse les raisons des juges, précise le moment des lectures et les gestes de mobile/mouvement, puis construit Folio hors expérience U6. Produit `3b79b3a10d2344a52db76f6e6239cf0a91c056c7`, noyau compilé 18 960 octets ; validation complète locale réussie, CI 52 et 53 en cours. 41 blocs protégés restent identiques, deux consignes changent, aucun bloc absent ou ajouté. Ces chiffres suivent ceux de la révision PHASE5, sans remplacer son état historique.

Folio passe 53 parcours finaux, après trois échecs initiaux conservés et corrigés. La comparaison à contenu constant retient une entrée réduite pour garder le total visible sur petit écran. L’auteur connaît U6 : aucun gain esthétique causal, aucune réduction de coût API et aucun comportement natif ne sont établis. Voir le [diagnostic](../SUITE-PRATIQUE/diagnostic/diagnostic-u6.md), la [galerie](../SUITE-PRATIQUE/galerie.html), la [trace mobile](../SUITE-PRATIQUE/mobile/trace.md) et la [livraison](../SUITE-PRATIQUE/livraison.md). Les originaux U6 restent inchangés.

## État final et suites

La suite technique a une compilation, une activation et des distributions vérifiables. Les six productions et la comparaison visuelle indépendante U6 sont livrées ; elles décrivent un petit échantillon, sans prouver une efficacité générale. La décision du propriétaire, les jetons API, la charge cognitive et les cibles initiales de lecture restent ouverts. La phase 6 conserve son périmètre minimal ; la phase 7 reste reportée. La PR du produit reste ouverte vers `main`.
