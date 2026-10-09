# Fiche — `V1/official/DIRECTION.md`

Lecture intégrale faite (844 lignes, 5 lectures). Les chiffres viennent de `mesures.md` / `mesures.json` ; les comptages complémentaires (grep) sont marqués « grep ». Toutes les dispositions sont des **propositions**.

## Identité

- **Rôle actuel.** Point d'entrée de la gouvernance (`DIRECTION.md:3`) : fixe le rôle de l'agent, classe le mode et le risque (`START`), donne la liste de chargement (`CHARGE`), porte la direction créative (boot, cible visuelle, premier objet, atelier, boucle d'édition) et les cinq absolus. Il mêle donc direction de design et règles de gouvernance.
- **Public réel.** L'agent, qui lit surtout le noyau recopié dans la skill (15 blocs) et quelques routes. Peu lisible pour un débutant ou un designer (codes partout, renvois constants vers `ACTION/...`).
- **Public visé par la charte.** Agent (route courte), designer (savoir de direction explicable, utilisable sans agent), équipe (module de gouvernance séparé). Le débutant passe par une autre entrée.
- **Mesures.** 102 309 caractères, 844 lignes, 14 618 mots. Titres : 1 / 18 / 43 (profondeur 3). 712 codes, soit 49 pour 1000 mots. Phrases : moyenne 18,7 mots, p90 32, 2 % au-dessus de 40. « Non vérifié » : 9. Vestiges : 0. Plus grosse section : « Constitution du document » (15 994). Autres sections lourdes : `START` 13 978, absolus 11 217, `CHARGE` 9 061, `VISUAL_TARGET` 9 209, `DOUBLE-LOOP` 8 210.
- **Répartition estimée design / gouvernance** (d'après les tailles de section, ordre de grandeur) : environ 43 000 caractères de design et de produit, environ 45 000 de gouvernance, environ 13 000 mixtes (`EXTERNAL-START`, `DOUBLE-LOOP`).

## Verdicts de la grille

| Critère | Verdict | Preuve |
|---|---|---|
| F1 Rôle | à corriger | `DIRECTION.md:3` : « point d'entrée de la gouvernance », alors que le fichier porte aussi la direction créative (`:5-24`, `:193-221`, `:430-615`). Plusieurs rôles dans un seul fichier. Contraire au principe 2 de la charte (le design d'abord, la gouvernance en module). |
| F2 Public | à corriger | Le public n'est dit nulle part. Le contenu s'adresse à un agent (`:285` commande `read_route.py`, `:558` `check_render.py`). Un designer ne trouve pas son savoir hors du vocabulaire de run (`RUN_CARD`, `N/A-JUSTIFIED`, `HANDOFF`). |
| F3 Structure | à corriger | Maximum trois niveaux : conforme. Mais trois systèmes de titres coexistent : routes `DIRECTION/X` (`:143`, `:149`, `:280`...), sections numérotées `0.` `1.` `2.` `3.` (`:707`, `:746`, `:763`, `:805`), sections libres (`:723` « Cadrage de médium », `:825` « Clôture de direction »). Des routes sont au niveau 3 (`CREATIVE-BOOT :193`, `DOMAIN-FRAME :223`, `FAST-PATH :312`). Les absolus, qui sont la partie la plus normative, viennent au milieu du fichier (`:617`), après les routes. Titres d'absolus de près de 100 caractères (`:623`-`:689`). Deux traits `---` coupent `DOUBLE-LOOP` (`:597`, `:599`). |
| F4 Une seule fois | à corriger | Répartition des propriétaires redite au moins 8 fois (`:32`, `:36-42`, `:48`, `:58`, `:76`, `:310`, `:829`, `:844`). « Vue dérivée de `START`, ne crée ni mode, ni gate... » répété en `:54`, `:76`, `:100`, `:153`, `:195`, `:322`, `:505` (grep : une vingtaine de lignes portent la formule négative). Règles d'ancre redites 5 fois (`:438`, `:491-495`, `:645`, `:656`, `:660`). Fenêtres de 14 mots communes : avec `ACTION.md` 22, avec `README.md` 8, avec `QUICKSTART.md` 6, avec `SAVOIR.md` 3 ; avec lui-même 7 (`:276` et `:719`, règle `ITER`) ; en-tête `:3` partagé avec les trois autres sources (18 fenêtres). |
| F5 Langue | à corriger | 49 codes pour 1000 mots (cible de la grille : aucun dans un fichier pour humains). Jargon non défini avant usage : `JTBD` utilisé en `:112`, défini en `:139` ; `blast radius` (`:165`), `consumer` (`:161`), `CTA` (`:375`), `slop` (`:547`, `:807`), `above-the-fold` (`:625`) jamais définis. Seuls cinq termes sont définis (`:139`). |
| F8 Longueur | à corriger | 102 309 caractères. `Constitution` (15 994) et `START` (13 978) sont plus lourdes que la plupart des routes de savoir. Les sections ne se comprennent pas seules : chacune renvoie à `START`, `ACTION/...`, `CHARGE`. Les modules de design sont plus propres (boot, domaine, cible : 0 à 3 renvois `ACTION/` chacun, grep). |
| F9 Limites | à corriger (mineur) | Les 9 « NOT-VERIFIED » sont au bon endroit. Mais les limites sont redites sous forme de litanie négative (« ne crée ni score, ni statut, ni gate... ») et dans l'en-tête (`:3`), `:26`, `:104`, `:112`, `:114`, `:539`, `:611`, `:615`. Le fichier dit « expérimentation maintenue » en `:3`, puis l'efficacité « NOT-VERIFIED » en `:104`. |
| F10 Exemples | à corriger (mineur) | Aucune valeur de couleur, police ni mise en page type (grep : aucun hexadécimal, aucun nom de police). Mais sept gabarits à remplir sont recopiables tels quels : `RUN` (`:256`), entrée minimale (`:182-189`), `CREATIVE-BOOT` (`:199-212`), `DOMAIN-FRAME` (`:227-243`), `RUN-PRIORITY` (`:327-339`), `GROUNDING-DECISION` (`:401-407`), `REUSE-CHALLENGE` (`:416-422`). Listes d'amorces qui peuvent figer : polarités de tension (`:514`), verbes de critique (`:537`), registres (`:458`). |
| F11 Vestiges | à corriger (mineur) | Mesure automatique : 0. Lecture : numérotation `0.` à `3.` résiduelle (`:707-805`) ; « anciens renvois de section » (`:801`, la table existe dans `CHANGELOG.md:72`) ; trois étiquettes de la légende jamais employées dans le corps (`[ABSOLU]` `:128`, `[RECOMMANDÉ]` `:131`, `[À ADAPTER]` `:132`, grep) ; `DIRECTION 72` / `DIRECTION 55` cités par `validate_reading_map.py:645` comme numéros de ligne (à vérifier : étiquettes de contrôle devenues sans sens). |

## Sections

Famille : D = design, P = produit, G = gouvernance, M = méta. « Agent » = lu surtout par l'agent. Les numéros de ligne sont ceux du fichier actuel.

| Section (ligne) | Ce qu'elle apporte | Famille | Public | Observation principale | Disposition proposée |
|---|---|---|---|---|---|
| Intro (`:1-3`) | Titre, statut « expérimentation maintenue », rôle du fichier. | M | tous | Dit « point d'entrée de la gouvernance » : contredit la charte. Phrase d'en-tête partagée avec 3 autres fichiers. | réécrire (forme) : un rôle, un public ; garder la mention d'expérimentation une seule fois. |
| Rôle (`:5-14`, bloc `ROLE`) | Pose l'agent comme directeur·rice artistique et product designer senior ; l'excellence appropriée. | D | agent, designer | Court, clair. Noyau copié (`ROLE`, `ROL-01`). | garder en tête du futur fichier de design. |
| Posture (`:18-26`, bloc `POSTURE`) | Première idée = hypothèse ; piège de conformité ; limite structurelle (`:26`). | D | agent, designer | Bon contenu de fond. `:26` « Limite structurelle » est hors noyau. | garder avec Rôle. |
| Constitution (`:30-141`) | Contrats de répartition entre fichiers, routage, architecture d'activation, lecture, légende. | G (avec D enfoui en `:104-116`) | agent | 15 994 caractères avant la première route de design. Sous-sections ci-dessous. | scinder (voir lignes suivantes). |
| — Intro, table des responsabilités (`:32-42`) | Dit qui possède quoi. | G | agent | Redite de `:48`, `:58`, `:76`, `:310`, `:829`. | fusionner avec Frontière (`:56`) en une seule table des propriétaires. |
| — Récapitulatif de protection (`:44-54`) | Résumé en 5 points des absolus, routage, premier objet, preuve. | G | agent | Se dit « pas une nouvelle source » (`:54`) ; duplique le corps. Verrouillé par l'ordre `ORD-01` (`validate_structure.py:196-198`). | retirer (répétition), après avoir changé `ORD-01` en phase 5. Raison : un résumé qui reprend ce qui suit. |
| — Frontière de responsabilité (`:56-58`) | `RUN_CARD` appartient à `ACTION`. | G | agent | Redit en `:274`, `:64`. | fusionner avec la table des propriétaires. |
| — Orientation interne et sortie (`:60-66`) | Renvoi vers `READING_MAP` ; sortie vers `ACTION/HANDOFF` ; condition d'arrêt de lecture. | G | agent | `:62` répété en `:100`. | fusionner ; la condition d'arrêt (`:66`) reste dans la gouvernance. |
| — Trois contrats ROUTE / TARGET / HANDOFF (`:68-76`) | Distingue classer, viser, transmettre. | G | agent | Redit par la table suivante (`:82-90`). | fusionner avec Architecture d'activation. |
| — Architecture d'activation (`:78-92`) | Table des 7 vues et de leur déclencheur. | G | agent | Utile comme carte de l'agent ; redit `:102`. | garder (module gouvernance), fusionner avec le précédent. |
| — Carte de lecture et chemin en trente secondes (`:94-118`) | Chemin de lecture, périmètre, priorité P0-P3, défaut de qualité visuelle, standard créatif, statut de gouvernance. | D et G mêlés | agent, designer | Le cœur du standard visuel (`:104`, `:108`, `:110`, `:112`, `:114`, `:116`) est enfoui dans une section de lecture. Plus grosse sous-section (6 882). | scinder : `:104-116` vers le fichier de design (standard de qualité, priorité) ; `:94-102` et `:118` vers la gouvernance. |
| — Comment lire les taxonomies (`:120-122`) | Risque, mode, P0-P3, V/U/A/T : ordre de lecture. | G | agent | Court. | garder (gouvernance). |
| — Légende (`:124-139`) | Étiquettes `[FORCÉ]`, etc. ; valeurs chiffrées = points de départ ; vocabulaire. | M | agent, humain | 3 étiquettes sans emploi (`:128`, `:131`, `:132`). Définit 5 termes trop tard (`:139`). `:137` contient une règle de fond (« premium » n'est pas une décision). | réécrire (forme) : définir les termes à la première occurrence ; déplacer `:137` vers le fichier de design ; retirer les étiquettes inutilisées (à valider avec `LCF-29`). |
| `SERVICE-BOUNDARY` (`:143-147`) | Une proposition de cadrage n'est ni un build ni une preuve ; une action externe n'est pas autorisée par V1. | G | agent, équipe | Règle de vérité importante, courte. | garder (gouvernance). |
| `START` (`:149-276`) | Classer le mode et le risque, entrée minimale, ligne de run, mémoire de lancement. | G | agent | 13 978 caractères, dont 5 521 de design (boot, domaine). Source normative des modes. | scinder : classification et sorties restent en gouvernance ; boot et domaine passent au design. |
| — Arbre de classification (`:157-176`) | Six questions ordonnées pour choisir le mode ; frontière LITE/ITER ; protection de niveau ; micro-deltas ; conflit. | G | agent, équipe | Texte de fond clé (`:172` risque critique). Verrouillé (`START`, `LCF-55`). | garder (gouvernance), intact. |
| — Entrée minimale (`:178-191`) | Gabarit DECISION / RISK / SCOPE / CONSTRAINT / NEXT-PROOF / OWNER. | G | agent | Gabarit recopiable (F10). | garder ; réécrire en langage clair en phase 3. |
| — `CREATIVE-BOOT` (`:193-221`, bloc `MOY-PLAFOND`) | Les décisions à tenir avant le premier pixel : promesse, objet de preuve, geste, modal, parti, tension, fabrication. | D | agent, designer | Cœur du chemin de design, logé dans `START`. Gabarit de 13 lignes avec codes. | déplacer vers le fichier de design ; réécrire (forme) sans codes. |
| — `DOMAIN-FRAME` (`:223-250`) | Adapter la direction au domaine (public, confiance, conventions, risques). | D (P) | agent, designer | Gabarit calqué sur un schéma JSON (`:246`). Garde-fou utile contre les stéréotypes (`:248`). | déplacer vers le fichier de design ; garder le lien avec `schemas/domain_frame.schema.json`. |
| — Sortie immédiate (`:252-268`) | Ligne de run, `DECISION-INTENT`, `DECISION-CHANGE`. | G | agent, équipe | Règle de vérité (« ne déclare jamais un changement avant observation »). | garder (gouvernance). |
| — Mémoire de lancement (`:270-276`) | Mémoire de run, renvoi à `RUN_CARD`, `creative_close`. | G | agent, équipe | `:276` redit la règle `ITER` de `:719`. | fusionner avec `ITER se souvient`. |
| `CHARGE` (`:280-310`, blocs `CHARGE-REGLE`, `CHARGE-TABLE`, `CHARGE-FIN`) | Règle de vitesse, recherche de savoir, table mode → routes à charger. | G (chargement) | agent | Seule liste de chargement. Verrouillée de partout (`CORE-01`, `UIX-01`, `CHG-04`, `LCF-01`...). Mélange chemin de design et chemin de gouvernance dans une même cellule (ligne `DIRECTION`). | garder ; en phase 5, séparer les routes de design et de gouvernance dans les cellules. Ne pas déplacer avant. |
| — `FAST-PATH` (`:312-316`) | Renvoi vers la exécution courte d'`ACTION`. | G | agent | Quasi vide : renvoi pur. | fusionner avec `CHARGE` (ou retirer : renvoi sans contenu propre). |
| `EXTERNAL-START` (`:320-349`, blocs `BRIEF`, `CONTENU`) | Priorités du brief (vérité, direction, premier objet, finition), prise de brief en ≤ 3 demandes, contenu d'exemple marqué. | D, P (G pour `NO-GO`) | agent, designer | Le bloc `RUN-PRIORITY` est un gabarit. Texte de fond précieux sur le contenu réel (`:348`). | garder dans le fichier de design ; réécrire le gabarit en prose. |
| — Traduction humaine (`:351-364`) | Six questions simples → contrats. | M | débutant, designer | Seul passage pensé pour un humain, enfoui en `:351`. | déplacer vers l'entrée humaine ou vers le fichier de design. |
| `FIRST-OBJECT` (`:366-426`, bloc `PREMIER-OBJET`) | Du brief au premier objet : chaîne promesse → objet → geste, contrat positif (8 dimensions), grounding, réutilisation. | D, P | agent, designer | Cœur de la qualité. Table des 8 dimensions verrouillée (`LCF-15`, `LCF-16`, `LCF-30`). `:375` (CTA) est produit. | garder dans le fichier de design. |
| — Grounding contestable (`:396-409`) | Refus de recherche rendu contestable. | G (P) | agent | Gabarit. | garder ; réécrire en prose. |
| — Réutilisation située (`:411-426`) | Évite la répétition de confort ; où lire l'antécédent. | D | agent | Aide à la variété (charte, principe 3). | garder (design). |
| `VISUAL_TARGET` (`:430-497`) | Table canonique de la cible : thèse, ancre, silhouette, plans, matière, typographie, objet de preuve, modal/parti ; compilation ; test de l'ancre ; route de production d'asset. | D | agent, designer | Table verrouillée (`LCF-28`). `:491-495` mêle réserve `RUN_CARD` et `SPECCED` (gouvernance). | garder (design) ; déplacer `:491-497` vers la gouvernance. |
| `DIRECTION-ATELIER` (`:501-539`, blocs `VER-SCENE`, `VER-AUDIENCE`) | Moment, tension, geste, position, contre-choix ; marquage de vérité de scène. | D | agent, designer | Les trois labels `TRUTH/*` sont définis ici (règle de vérité). | garder (design). |
| `DOUBLE-LOOP` (`:541-615`, blocs `BOUCLE`, `BOUCLE-DIAGNOSTIC`, `BOUCLE-QUESTIONS`) | Boucle observer → corriger → réobserver ; table du diagnostic ; signaux de réouverture ; résilience visuelle. | D, P | agent, designer | Contenu cohérent. Les `---` (`:597`, `:599`) coupent la section ; `:615` (pilote) est de la méta. | garder (design) ; retirer les `---` ; déplacer `:613-615` vers la méta. |
| Les cinq règles absolues (`:617-703`, bloc `ANCRE`) | Cinq contrats : standard visuel, ancrage, gate, mode/preuve/budget, réel et beau. | D (1, 5), G (2, 3, 4) | agent | Absolus 1 et 5 sont du design et du produit ; 2, 3, 4 de la gouvernance. Le texte dit « une règle de plus doit en remplacer une » (`:621`). | scinder : absolus 1 et 5 vers le design ; 2, 3, 4 vers la gouvernance. Garder la numérotation si les renvois externes l'exigent. |
| `0. Classification du mode` (`:707-719`) | Vue de `START` ; `ITER se souvient`. | G | agent | Se dit « vue contractuelle » (`:709`) : redit `START`. | fusionner avec `START`. |
| Cadrage de médium et de capacité (`:723-742`) | Capacité minimale, médium non Web, table besoin → capacité. | P (D) | agent | Sans numéro, entre `0.` et `1.`. Utile (portabilité). | garder (produit) ; renommer. |
| `1. Direction divergente` (`:746-759`) | Alternative située, axe matière déclaré, checkpoint. | D | agent, designer | Cœur de la variété. Bloc concept `ALT-01` (`:752`). Renvoie à `SAVOIR/CRAFT/CFT-02` et `ACTION`. | garder (design). |
| `2. Routage` (`:763-801`) | Déclencheurs critiques et index à la demande. | G | agent | Se dit « pas une seconde liste de chargement » (`:769`) mais en est une. | fusionner avec `CHARGE` (gouvernance) ou lui renvoyer explicitement ; à décider. |
| `3. Invariants de jugement` (`:805-821`) | Convergence de genre ≠ slop ; PASS ≠ direction tenue ; listes ≠ canon. | D | agent, designer | Court, précieux. | garder (design). |
| Clôture de direction (`:825-833`) | Test de sortie avant `ACTION/CLOSE-EXIT-CHECK`. | G | agent | Redit les propriétaires (`:829`). | garder (gouvernance) ; supprimer la redite. |
| Lecture instrumentée (`:833-844`) | Catégories de lecture pour les runs mesurés ; ordre de passage. | G / M | équipe | Verrouillée par `MNT-01` (`validate_structure.py:331`). Utile seulement pour une mesure. | déplacer vers la méta/maintenance (à vérifier avec `MNT-01`). |

## Défauts

| n° | Type | Gravité | Preuve | Proposition |
|---|---|---|---|---|
| 1 | structure / convergence | bloquant (critère S9) | Design et gouvernance sont mêlés dans un seul fichier. Les modules de design sont pourtant propres (0 à 3 renvois `ACTION/` chacun, grep) et la gouvernance se laisse isoler (`Constitution`, `START` classification, `CHARGE`, absolus 2-4, `0.`, `2.`, clôture). | Scinder en deux fichiers (design / gouvernance), en gardant les blocs `noyau` dans leur propriétaire. Décision à valider. |
| 2 | structure | important | Le standard de qualité visuelle (`:104-116`) est enfoui dans « Carte de lecture » au sein de la Constitution (15 994). | Remonter ces paragraphes en tête du fichier de design. |
| 3 | répétition | important | Répartition des propriétaires redite au moins 8 fois ; formule « ne crée ni mode, gate, statut... » sur une vingtaine de lignes (grep) ; règle `ITER` en `:163`, `:276`, `:298`, `:719` ; règle d'ancre en `:438`, `:493`, `:645`, `:656`, `:660`. | Une table des propriétaires ; une phrase sur « vue dérivée » ; une règle `ITER` ; une règle d'ancre. |
| 4 | répétition | important | Recoupement avec `ACTION.md` : 22 fenêtres de 14 mots (`DIRECTION.md:108`, `:172` = `ACTION.md:75`, `:277`). Avec `README.md:73` (`:49`), `QUICKSTART.md:47` (`:343`), `SAVOIR.md:30` (`:268`). | Choisir un propriétaire par passage ; l'autre fichier renvoie. |
| 5 | langue | important | 49 codes pour 1000 mots ; 712 codes. Gabarits en capitales (`:199-212`, `:227-243`, `:327-339`). Termes non définis avant usage : voir F5. | Réécrire en phase 3 (langue) sans toucher au fond : prose avec le code entre parenthèses la première fois. |
| 6 | structure | important | Trois systèmes de titres (F3). Les absolus, plus normatifs que tout, sont au milieu (`:617`). Titres d'absolus de ~100 caractères. | Titres courts et prévisibles ; absolus en tête du fichier de gouvernance et du fichier de design. Contrainte : `ORD-01` (`validate_structure.py:196-198`). |
| 7 | structure | mineur | `0. Classification` se dit vue de `START` (`:709`) ; `FAST-PATH` est un renvoi pur (`:312-316`) ; `ITER se souvient` est une règle de `START` (`:717`). | Fusionner dans `START`. |
| 8 | convergence (risque) | important | Gabarits recopiables (F10) ; `CREATIVE-BOOT` demande « jusqu'à trois qualités », « un ou deux axes » ; le gabarit incite à remplir chaque champ même si le texte dit le contraire (`:221`, « sa valeur se juge à sa conséquence »). | Les écrire en prose, ou les marquer « point de départ » ; conserver le contenu. |
| 9 | risque | mineur | Listes d'amorces : polarités de tension (`:514`), verbes de critique (`:537`), registres (`:458`). Le texte les met en garde (`:821`), mais l'agent peut les recopier. | Garder ; ajouter « liste d'amorces » une fois au point d'usage, ou remplacer par un critère. |
| 10 | obsolète / vestige | mineur | Légende : `[ABSOLU]`, `[RECOMMANDÉ]`, `[À ADAPTER]` jamais employées dans le corps (grep). `:801` « anciens renvois ». | Retirer les étiquettes sans emploi (vérifier `LCF-29`). |
| 11 | coût de lecture | important | Pour un run `DIRECTION`, `CHARGE` (`:300`) envoie vers `CREATIVE-BOOT`, `VISUAL_TARGET`, `FIRST-OBJECT`... mais ces routes vivent dans le même fichier de 102 k. L'agent lit par routes (`read_route.py`) : coût limité, mais la structure ne l'indique pas. | Après scission, une route = un fichier ou une section autoportante (phase 5). |
| 12 | langue | mineur | « Traduction humaine minimale » (`:351-364`) est le seul passage lisible par un débutant ; il est dans un fichier d'agent. | Le déplacer vers l'entrée humaine (à valider avec `LCF-10`, `LCF-24`). |
| 13 | risque (déplacement) | important | Le texte est verrouillé par ~60 phrases de contrôle (voir Dépendances). Tout déplacement sans mise à jour des scripts casse `validate_all.py`. | Déplacer d'abord les contrôles (phase 5), pas le texte seul. |
| 14 | convergence | mineur | La table `CHARGE` fait dépendre le design du contenu de gouvernance : la cellule `DIRECTION` (`:300`) contient 7 routes `ACTION/` et 6 routes de design/savoir dans la même phrase. | Séparer les deux listes dans la cellule (forme seule). |

## Savoir à protéger

- Rôle de directeur·rice artistique et product designer senior ; excellence appropriée, pas imitation d'un canon (`:9-14`).
- Première idée = hypothèse ; piège de conformité ; limite structurelle (`:21-26`).
- Standard de qualité visuelle : périmètre multi-plateformes, priorité P0-P3, défaut « dirigé, distinctif, construit, poli », standard créatif, plancher d'usage non sacrifiable (`:104-116`).
- Les trois contrats ROUTE / TARGET / HANDOFF (`:68-76`) et l'architecture d'activation (`:78-92`).
- Une proposition de cadrage n'est ni un build ni une preuve ; une action externe n'est pas autorisée par V1 (`:145-147`).
- Arbre de classification en six questions, frontière LITE/ITER, protection de niveau contre les risques critiques, silence des micro-deltas, règle de conflit (`:157-176`).
- Entrée minimale et rôle de `OWNER` / `SCOPE` (`:178-191`).
- `CREATIVE-BOOT` : décisions avant le premier pixel, `MODAL`, `PARTI`, `FABRICATION`, premier objet complet, pas de wireframe creux (`:195-221`).
- `DOMAIN-FRAME` : variables de domaine ; le domaine contraint mais ne fournit pas la direction ; pas de stéréotype ; profondeur selon les déclencheurs (`:225-250`).
- Ligne de run, `DECISION-INTENT`, `DECISION-CHANGE` : jamais déclarer un changement avant observation (`:254-268`).
- Traces : légère, persistante ; mémoire de lancement ; règle `ITER` (`:270-276`, `:717-719`).
- Table `CHARGE` des cinq modes, règle de vitesse, recherche de savoir, tags du noyau (`:282-306`).
- Prise de brief : au plus trois demandes, build dans le même tour, hypothèses nommées (`:342-344`).
- Contenu d'exemple marqué, action principale toujours fonctionnelle, aucun faux signe de preuve (`:346-349`).
- `RUN-PRIORITY` : vérité, direction, premier objet, finition ; `NO-GO` (`:326-340`).
- Chaîne promesse → objet de preuve → geste ; objet de préférence codé ; marquage `TRUTH/ILLUSTRATIVE` ; données d'exemple cohérentes (`:368-373`).
- CTA réel ou limite déclarée (`:375`).
- Contrat positif du premier objet : 8 dimensions, « retour si », correspondance avec les dimensions de qualité (`:377-394`).
- `GROUNDING-DECISION` : un refus de recherche doit être contestable (`:396-409`).
- `REUSE-CHALLENGE` et lecture de l'antécédent, sans reconstitution de mémoire (`:411-426`).
- Table de la cible visuelle (11 champs), compilation, test d'utilité de l'ancre (`:430-470`).
- Six routes de production d'asset et règles : jamais de faux asset en produit réel, la génération n'est pas un défaut (`:472-489`).
- Réserve `ANCHOR-GENERATED` en enjeu identitaire élevé, passage à `SPECCED` (`:491-497`).
- Atelier : moment, tension, geste, position et exclusion, contre-choix situé ; familles internes, une seule proposition à la personne (`:501-518`).
- Marquage de vérité de scène `TRUTH/*` ; interne, jamais dans l'interface (`:522-539`).
- Contrôle du premier objet, une correction substantielle sans quota, one-shot (`:545-555`).
- Boucle d'édition, table de diagnostic, questions de revue sur l'ensemble de la page (`:557-578`).
- Signaux de réouverture ; création et preuve distinctes (`:580-595`).
- Test de résilience visuelle (`:599-611`).
- Absolu 1 : standard visuel, trois décisions nommables, la protection critique prévaut (`:623-639`).
- Absolu 2 : explorer, accepter, diffuser ; voies d'ancrage ; `FAIL-ASSUMED` ne vaut pas pour une ancre absente (`:641-660`).
- Absolu 3 : aucune livraison sans preuves ; `N/A-JUSTIFIED` / `NOT-VERIFIED` ; un seul override (`:662-672`).
- Absolu 4 : déclarer mode, décision, risque, preuve, arrêt ; jalons ; pas de baisse silencieuse (`:674-687`).
- Absolu 5 : réel et beau ; contenu synthétique marqué ; icônes fonctionnelles ; enjeux élevés ; accessibilité sans glissement de preuve ; usage ≠ capture (`:689-703`).
- Classification vue contractuelle, axes V/U/A/T, lettres des gates (`:707-715`).
- Cadrage de médium et de capacité, table besoin → capacité (`:723-742`).
- Direction divergente : alternative située, avantage en une phrase, axe matière déclaré, checkpoint (`:746-759`).
- Déclencheurs critiques et index à la demande (`:767-799`).
- Invariants : convergence de genre ≠ slop ; PASS ≠ direction tenue ; listes ≠ canon (`:807-821`).
- Clôture : `ACTION/CLOSE-EXIT-CHECK` unique ; DIRECTION ne ferme pas un run (`:827-831`).
- Lecture instrumentée : 4 catégories de lecture ; aucune affirmation de réduction sans méthode (`:835-842`).
- Ordre de décision pour une route partagée (`:844`).

## Ce qui fige ou pousse à la convergence

- Gabarits à champs recopiables : `CREATIVE-BOOT` (`:199-212`), `DOMAIN-FRAME` (`:227-243`), `RUN-PRIORITY` (`:327-339`), `GROUNDING-DECISION` (`:401-407`), `REUSE-CHALLENGE` (`:416-422`), entrée minimale (`:182-189`). Ils encouragent à tout remplir alors que le texte dit de ne remplir que ce qui change la décision (`:221`, `:191`).
- Polarités de tension nommées : « hésitation/élan, densité/respiration, mémoire/disparition, contrôle/transmission » (`:514`) ; verbes « isole, déplace, matérialise, ralentit, efface » (`:537`) ; registres « naturel, organique, éditorial, architectural, tactile ou technique » (`:458`) ; « tension, déséquilibre assumé, vide calibré, débord, rythme » (`:637`). Le texte les déclare des amorces (`:821`), mais ce sont les premières options qu'un agent cite.
- Les deux contre-exemples de stéréotype (`:248`, financier / culturel / technique) sont utiles ; ils restent des garde-fous, pas des défauts.
- Aucune valeur de couleur, police ou mise en page type : aucun relevé de ce genre.

## Dépendances et risques de déplacement

- **Blocs « noyau » copiés dans la skill** par `scripts/build_core.py` (registre `NOYAU`, lignes 33-60 ; budget `CORE_BUDGET_BYTES = 46 000`, `SKILL.md` fait 42 978). 15 blocs, tous attribués à `DIRECTION.md` dans le registre :
  - `ROLE` (`:7-12`), `POSTURE` (`:20-24`), `MOY-PLAFOND` (`:216-219`), `CHARGE-REGLE` (`:282-288`), `CHARGE-TABLE` (`:294-302`), `CHARGE-FIN` (`:304-306`), `BRIEF` (`:342-344`), `CONTENU` (`:346-349`), `PREMIER-OBJET` (`:368-373`), `VER-SCENE` (`:522-525`), `VER-AUDIENCE` (`:533-535`), `BOUCLE` (`:557-559`), `BOUCLE-DIAGNOSTIC` (`:563-574`), `BOUCLE-QUESTIONS` (`:576-578`), `ANCRE` (`:643-646`).
  - Repères de concept dans ou près des blocs : `ROL-01`, `HON-03`, `CNT-01`, `EXD-01`, `HON-01`, `ANC-01`, plus `ALT-01` (`:752`, hors noyau). Contrôlés par `validate_structure.py:56-80`.
  - Les marqueurs `<!-- noyau:début X -->` / `fin X` doivent rester sur des lignes seules, avec l'identifiant en capitales ; déplacer un bloc vers un autre fichier impose de changer le propriétaire dans `build_core.py`.
- **Contrôles qui verrouillent du texte de ce fichier** (mesures.json : `validate_structure.py` 25 phrases, `validate_reading_map.py` 26, `read_route.py` 3, `test_audit_regressions.py` 3, `test_read_route.py` 3, `test_preparer_livraison.py` 2, `validate_contracts.py` 1, `validate_design_governance.py` 1) :
  - `ORD-01` : `## Rôle`, `## Posture — à lire avant toute action` et `### Récapitulatif de protection` doivent exister une fois, avant `## DIRECTION/START` (`validate_structure.py:196-198`, `:605-611`).
  - `CORE-01`, `UIX-01`, `CHG-04` : contenu et cellules de la table `CHARGE` (`validate_structure.py:~380-640`) ; la section est cherchée par `"## DIRECTION/CHARGE"` jusqu'au `## ` suivant.
  - Lignes de table verrouillées (`ROW_NEEDLES`, `validate_structure.py:724-727`) : `| Décision suffisamment établie |`, `| **STANDARD** |`, `| **DIRECTION** |`, `| Détail final susceptible`.
  - Expressions interdites hors de certains fichiers : `→ isoler|observer, isoler` autorisé seulement dans `DIRECTION.md`, `SKILL.md`, `CHANGELOG.md` (`validate_structure.py:115-116`).
  - `validate_reading_map.py` découpe des sections par titres : `## DIRECTION/CHARGE`, `## DIRECTION/VISUAL_TARGET` jusqu'à `### Compilation de la première proposition`, `## DIRECTION/EXTERNAL-START` jusqu'à `### Traduction humaine minimale`, `## DIRECTION/FIRST-OBJECT` jusqu'à `### Contrat positif du premier objet` (`:355`, `:511`, `:550`) ; contrôles `LCF-01`, `-04`, `-06`, `-07`, `-08`, `-09`, `-15` à `-17`, `-21`, `-24`, `-28`, `-29`, `-30`, `-36`, `-43` à `-47`, `-53` à `-55`. Renommer ces titres les casse.
  - `read_route.py` : les routes sont les titres `## X/Y` ; `--trouver`, `--sommaire`, `--connexions` (cités en `:285-287`) ; 3 phrases verrouillées ; `test_read_route.py:217-218` manipule la ligne `| \`DIRECTION/START\` |` de `READING_MAP.md`.
  - `test_preparer_livraison.py:253` modifie une copie de `DIRECTION.md` ; `preparer_livraison.py:37` et `package_manifest.json:11,79` listent le fichier à son chemin actuel.
- **Ce qui cite `DIRECTION.md`** : `ACTION.md` (renvois `DIRECTION/DOUBLE-LOOP`, `START`, `CHARGE`), `BIBLIOTHEQUE.md:211`, `QUICKSTART.md:88,261`, `READING_MAP.md:310` (table des locators), `README.md` racine et `V1/official/README.md:13`, `CHANGELOG.md:14`, `SKILL.md` (copie du noyau et renvois), `GLOSSAIRE.md`, `references/examples.md` (« DIRECTION — première scène identitaire ») et `references/flow.md`.
- **Ce qu'il cite** : `ACTION.md` (69 renvois `ACTION/...`, 127 mentions), `SAVOIR.md` (`CRAFT`, `TYPE`, `STATE`, `TOOLS`, `INTEGRITY`, `DESIGN-ATLAS`...), `BIBLIOTHEQUE.md` (`SELECT`, `TENSION`, `SEQUENCE`, `CONTRACTS`), `CHANGELOG.md`, `READING_MAP.md`, `schemas/domain_frame.schema.json` (`:246`), `scripts/read_route.py` (`:285-287`), `scripts/check_render.py` (`:558`).
- **Risque principal.** Une scission du fichier est possible sur le fond (les modules de design sont presque autonomes) mais touche : le registre de `build_core.py`, les locators de `READING_MAP`, ~60 phrases verrouillées, l'ordre `ORD-01`. Selon la charte (section 5), ne pas toucher au chargement avant la phase 5 : en phases de rangement, rester sur le réécrit en place et les fusions internes.

## Synthèse

DIRECTION est un fichier de gouvernance qui contient, enfoui, le cœur du savoir de direction créative : environ 43 000 caractères de design et de produit, 45 000 de gouvernance, 13 000 mixtes. Les modules de design (boot, domaine, cible, premier objet, atelier, boucle) sont presque autonomes (0 à 8 renvois `ACTION` chacun) ; la séparation est donc faisable. Le standard de qualité visuelle (`:104-116`) est caché dans la Constitution, et la répartition des propriétaires est redite au moins 8 fois. Les risques sont le jargon (49 codes pour 1000 mots), les gabarits recopiables et un verrouillage dense (15 blocs de noyau, ~60 phrases de contrôle, `ORD-01`). Aucun savoir n'est à retirer ; ce qui est à retirer est de la redite (récapitulatif, `FAST-PATH`, section `0.`) et trois étiquettes inutilisées.
