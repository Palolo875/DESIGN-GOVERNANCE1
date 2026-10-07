# U1b — Fiche d'inventaire n°4 : `V1/official/DIRECTION.md`

**Base :** commit `d90869c`. **Lecture :** intégrale (lignes 1 à 867), faite le 7 octobre pendant l'unité U1 et reprise ici sous l'angle de l'inventaire ; tailles des sections mesurées par script. **Angle :** ce que le fichier possède et permet de fabriquer.

## 1. Identité

| Élément | Valeur |
|---|---|
| Taille | 104 836 o, 867 lignes, 21 tables, 6 gabarits |
| Part compilée dans le noyau | 15 blocs, 14,0 Ko : 13 % du fichier, 32 % du noyau |
| Concepts protégés | 7 (ROL-01, HON-03, CNT-01, EXD-01, HON-01, ANC-01, ALT-01) |

## 2. Rôle

- **Déclaré** (l. 3, 32) : « seul document canonique de cadrage » : rôle, absolus, classification, direction visuelle, capacité.
- **Réel :** deux natures mêlées.
  1. **Un cadre de décision**, c'est-à-dire classer la demande et choisir quoi charger.
  2. **Une méthode de direction artistique**, c'est-à-dire passer d'un brief à une première scène dirigée et la corriger.

  La seconde est la plus utile pour fabriquer, mais elle est éclatée en sept modules : CREATIVE-BOOT, DOMAIN-FRAME, EXTERNAL-START, FIRST-OBJECT, VISUAL_TARGET, DIRECTION-ATELIER, DOUBLE-LOOP.

## 3. Répartition du volume (mesurée)

| Partie | Taille | Nature |
|---|---|---|
| Orientation et vues de navigation (récapitulatif, contrats, architecture, carte de lecture, légende, CHARGE, FAST-PATH, section 0, routage) | ≈ 26,5 Ko | Méta ; une partie est compilée au noyau (CHARGE) |
| Classer (START, arbre, entrée minimale, sortie immédiate, mémoire de lancement) | ≈ 8,7 Ko | Décision |
| **Méthode de direction** (CREATIVE-BOOT, DOMAIN-FRAME, EXTERNAL-START, FIRST-OBJECT, VISUAL_TARGET, ATELIER, DOUBLE-LOOP) | **≈ 40 Ko** | Fabrication |
| Cinq absolus | ≈ 11,6 Ko | Protection |
| Médium et capacité, direction divergente, invariants, clôture | ≈ 11 Ko | Mixte |

## 4. Ce qu'il possède

Niveaux : **A** actionnable · **O** orientant. Accès : **Noyau** ou **Route**.

### Comprendre et classer la demande

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Arbre de classification en 5 questions et une clarification ciblée ; frontière LITE / ITER ; Protection de niveau ; silence des micro-deltas ; règle de conflit (découper si les risques sont indépendants) | 157-176 | A | Route (`START/TREE`) |
| Entrée minimale : DECISION, RISK, SCOPE, CONSTRAINT (dont la destination), NEXT-PROOF, OWNER | 180-191 | A (gabarit) | Route |
| **Traduction humaine de START** : 6 questions simples (que doit comprendre, ressentir ou faire la personne ? que doit-on voir tout de suite ? qu'est-ce qui rend la proposition propre à ce produit ?…) | 360-371 | **A** | Route |
| Chemin en trente secondes (décision, risque, mode, capacité minimale, premier objet) | 98 | A | Route |
| Frontière service : une « proposition de cadrage » peut précéder un run, sans prétendre à un résultat | 143-147 | O | Route |
| **DOMAIN-FRAME** : 16 variables de domaine ; règle anti-stéréotype (« un produit financier n'est pas minimaliste par défaut… ») ; déclencheurs de profondeur | 223-250 | A | Route |

### Diriger (direction artistique)

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| **Creative Boot** : 12 décisions avant le premier pixel (promesse, objet de preuve, geste, MODAL, PARTI, tension, signature, cibles créatives, FABRICATION, premier objet, défaut recherché) | 197-212 | A (gabarit) | Route |
| Plafond de fabrication déclaré avant le build | 218 | A | **Noyau** |
| **RUN-PRIORITY** : TRUTH → DIRECTION → FIRST-OBJECT → FINISH, et une liste **NO-GO** (faux réalisme, dashboard décoratif, cartes avant le mécanisme, retour automatique au dernier style) | 333-347 | **A** | Route |
| Prise de brief ; contenu d'exemple marqué | 350-355 | A | **Noyau** |
| Promesse → objet de preuve → geste ; marquage de vérité ; cohérence des données d'exemple | 376-379 | A | **Noyau** |
| Règle des CTA : comportement réel, action disponible, ou limite déclarée | 382 | A | Route (en partie au noyau) |
| **Contrat positif du premier objet** : 8 dimensions, chacune avec « suffisant quand… » et « retour si… », reliées aux dimensions CFT-00 | 386-401 | **A** | Route |
| Grounding contestable (un « NO » sans contre-hypothèse est invalide) | 405-416 | A (gabarit) | Route |
| **REUSE-CHALLENGE** : lire l'antécédent dans les traces (teinte dominante, paire typographique, ossature, objet de preuve), jamais de mémoire ; chaque reprise justifiée | 420-433 | **A**, mécanisme anti-convergence | Route |
| **VISUAL_TARGET** : 11 champs (thèse, conséquence observable, ancre, silhouette, relations de plans, opération dominante, matière, typographie, objet de preuve, modal et parti, résolution initiale) ; ordre de compilation de la première proposition | 441-465 | A | Route |
| Test d'utilité de l'ancre | 471-477 | A | Route |
| **Six routes de production d'un asset** : CODE-NATIVE, FOURNI, CURATÉ, GÉNÉRÉ-DIRIGÉ, HYBRIDE, SANS-ASSET, avec quand les retenir et quoi déclarer ; en produit réel, un asset manquant n'est **jamais** remplacé par un faux | 479-496 | **A** | Route (le noyau ne garde que « pas de faux asset ») |
| Réserve sur l'ancre générée en enjeu identitaire élevé | 498-500 | A | Route (C04) |
| **DIRECTION-ATELIER** : moment humain, tension, geste produit, position et exclusion, contre-choix situé ; critique par verbes (isole, déplace, matérialise, ralentit, efface) | 514-546 | A | Route |
| Labels `TRUTH/OBSERVED`, `ILLUSTRATIVE`, `MECHANISM` et leur audience | 531-542 | A | **Noyau** (en partie) |

### Observer et corriger

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Contrôle du premier objet avant présentation ; une correction substantielle, sans quota | 552-558 | A | Route |
| One-shot (conditions pour s'arrêter après la première observation) | 560-562 | A | Route |
| Boucle commune, table de diagnostic, 6 questions | 564-592 | A | **Noyau** |
| **Signaux de réouverture** : 6 signaux observés → où revenir (cible, composition, position, objet, build, preuve) | 596-607 | **A** | Route |
| **Test de résilience visuelle** : 5 transformations (asset retiré, contenu long, mobile et zoom, état critique, effets réduits) | 615-625 | **A** | Route |

### Protéger (les cinq absolus)

| Absolu | Ce qu'il possède de concret | Accès |
|---|---|---|
| 1. Standard visuel | Définition de la surface identitaire ; trois décisions nommables (matière, typographie, composition) ; la protection critique prime | Route |
| 2. Ancrage observable | Explorer, accepter, diffuser ; table des 3 voies d'ancrage ; une source web doit être réellement ouverte | **Noyau** (bloc ANCRE) |
| 3. Gate | Non applicable = `N/A-JUSTIFIED` ; non vérifiable = `NOT-VERIFIED` | Route |
| 4. Mode, preuve et budget | Le budget comme **6 jalons** avec leur question d'arrêt (cadrage, direction, ancrage, build, vérification, clôture) | Route |
| 5. Réel et beau ensemble | Contenu synthétique admis s'il garde les propriétés qui comptent (longueur, densité, langue, extrêmes) ; icône fonctionnelle ou remplissage ; contextes à enjeu ; une capture ne prouve pas l'utilisabilité | Route |

### Capacités et divergence

| Élément | Lignes | Concr. | Accès |
|---|---|---|---|
| Médium réel → capacité → preuve propre au médium → fallback ; construction distincte de vérification ; table de 6 besoins → capacité → contrat | 739-756 | A | Route |
| Direction divergente : 6 axes, avantage formulé en une phrase vérifiable, axe matière toujours déclaré | 762-782 | A | Route |
| Invariants : convergence de genre ≠ slop ; PASS technique ≠ direction tenue ; les listes ne sont pas un canon | 830-844 | O | Route |

## 5. Ce que le fichier ne possède pas

1. **Aucune valeur, aucune ressource, aucun exemple visuel** (comme SAVOIR et BIBLIOTHEQUE).
2. **Aucune méthode propre aux médiums hors écran** ; le cadrage de capacité les nomme (natif, spatial, CMS) mais renvoie la preuve à SAVOIR/TECH.
3. **Aucune vue unifiée de la méthode de direction** : 7 modules voisins (12 + 11 + 8 + 16 champs de gabarits), que le texte dit lui-même ne pas devoir remplir en parallèle (l. 80, 116).

## 6. Potentiel présent mais peu exploité

| Élément | Pourquoi il compte au regard de la mission | Accès actuel |
|---|---|---|
| **Traduction humaine de START** (l. 360-371) | Six questions simples qui portent tout le cadrage sans jargon : c'est l'interface « sans maîtriser la mécanique » | Route |
| **RUN-PRIORITY et liste NO-GO** (l. 333-347) | La priorité la plus claire du corpus pour un brief vague : vérité, puis direction, puis premier objet, puis finition | Route |
| **Contrat positif du premier objet** (l. 386-401) | Dit précisément quand un premier rendu est « suffisant » et quoi faire sinon | Route |
| **REUSE-CHALLENGE** (l. 420-433) | Seul mécanisme existant contre la répétition d'un run à l'autre ; il dépend de traces que l'agent doit retrouver | Route |
| **Six routes de production d'asset** (l. 479-496) | La réponse honnête à « je n'ai pas d'image » ; cœur du lien entre moyens et fabrication | Route ; une phrase au noyau |
| **Signaux de réouverture** et **test de résilience** (l. 596-625) | Que regarder après le premier rendu, et quand rouvrir au lieu de polir | Route |
| **Budget en 6 jalons** (l. 692-699) | Une façon simple de savoir où s'arrêter | Route |

## 7. Connexions

- **Vers ACTION :** toutes les preuves, gates, statuts et la clôture ; HANDOFF, RUN_CARD, PIPELINE-DIRECTION, OVERRIDE (FAIL-ASSUMED).
- **Vers SAVOIR :** CRAFT (CFT-00, CFT-02), TOOLS (marqueurs de vague, carte des moyens), SOURCE, STYLE, INTEGRITY, CONTEXT, DESIGN-ATLAS.
- **Vers BIBLIOTHEQUE :** TENSION, SELECT, CONTRACTS.
- **Vers les schémas :** `domain_frame.schema.json` (« reprend exactement », l. 246) ; projection de la carte de run.
- **Vers CHANGELOG :** conflits avec START, migration des anciennes routes.

## 8. Observations faites en passant (à verser au registre)

| Observation | Lignes | Lien |
|---|---|---|
| La méthode de direction est découpée en 7 modules voisins dont les champs se recoupent (promesse et thèse, parti et exclusion…) ; le texte demande de ne pas les remplir en parallèle | 80, 116 | Charge cognitive ; grilles parallèles (C37) |
| La « carte de lecture canonique » fait à elle seule 7,1 Ko de méta | 94-119 | Volume d'orientation |
| Les axes de la direction divergente doublent ceux de SAVOIR (CFT-02) | 766-773 | Troisième jeu d'axes avec BIBLIOTHEQUE |
| Le budget en 6 jalons (absolu 4) n'apparaît pas dans les résumés de l'absolu 4 | 692-699 | Précise C17 |

## 9. En une phrase

DIRECTION possède **la méthode de direction artistique la plus complète du système** : priorités sur brief vague, contrat du premier objet, routes d'asset honnêtes, anti-répétition entre runs, signaux de réouverture, résilience. Mais elle est **éclatée en sept modules voisins et enfouie sous environ 26 Ko d'orientation**, et la plupart de ces outils restent hors du noyau, donc invisibles si l'agent ne charge pas la bonne route.
