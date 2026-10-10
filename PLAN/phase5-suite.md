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

Ce sont des comparaisons mécaniques du lecteur, pas deux exécutions indépendantes d’agents. Les détails différés sont inclus : la baisse du fichier seul n’est pas présentée comme la baisse du run entier. Les totaux incluent des contrôles après fabrication ; ils ne valident pas les cibles provisoires de lecture **avant** production (35 000 / 75 000 / 110 000). Ces cibles restent ouvertes, sans modification opportuniste du seuil ni retrait de protection. Jetons, durée et charge cognitive restent non mesurés.

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

## État final et suites

La suite technique a une compilation, une activation et des distributions vérifiables. La comparaison indépendante de qualité et de variété reste ouverte : briefs identiques et demande nouvelle, capacités constantes, exécutions séparées et jugement sans indication de version. Les essais actuels ne ferment pas ce point. La phase 6 conserve son périmètre minimal ; la phase 7 reste reportée. La PR du produit doit encore être fusionnée vers `main`.
