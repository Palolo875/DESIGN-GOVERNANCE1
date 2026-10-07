# U1 — Les trois parcours du plan (§6)

Chaque parcours distingue ce qui est **sur papier**, c'est-à-dire déroulé en lisant les règles, de ce qui a été **réellement testé** (tests T-xx rejouables avec `preuves/reproduire_U1.py`). Aucun parcours n'a été exécuté par un agent qui découvrirait le système : ce sont des parcours de conception, menés par une instance qui connaît déjà le corpus.

Les charges sont en octets UTF-8 servis par `read_route.py`, plus `SKILL.md` (43 201 octets). Les tokens ne sont pas mesurés.

---

## P1 — Retouche du contraste d'un bouton secondaire

**Situation.** Page existante d'un atelier vélo. Le bouton secondaire « Voir les tarifs » est gris clair sur blanc. On corrige sans toucher la structure.

### Sur papier : ce que le système fait mobiliser

| Étape | Règle suivie | Observation |
|---|---|---|
| Classer | `DIRECTION/START/TREE` : q4 « fix ou delta local » → `LITE`. La frontière LITE/ITER cite le contraste comme LITE. | **Ambiguïté (C14)** : `ACTION/FAST-PATH`, chargé juste après, dit « reviens à un mode plus riche si le changement touche […] l'accessibilité ». Un contraste touche l'accessibilité. Seule la Protection de niveau (risque *critique*) permet de trancher, et FAST-PATH ne la reprend pas. |
| Charger | Ligne LITE de CHARGE : `RUN-LITE`, `FAST-PATH`, `GATE-A` applicable, `GATE-B` du risque dominant. | « Applicable » et « du risque dominant » ne se chargent pas à part : le lecteur sert les blocs entiers (C15). |
| Lancer | `RUN-LITE` : « écrire la ligne de run, déclarer `DECISION-INTENT` ». | Ni l'une ni l'autre ne figurent dans le noyau (C18) : l'agent les découvre ici, dans une route. |
| Modifier et prouver | `GATE-A` : contraste calculé selon WCAG 2.2 AA, jamais à l'œil ; recette `check_render`. `GATE-B` : famille B2 « Système et robustesse » → axe A. | Utile et précis. |
| Tracer | Trace légère par défaut (six lignes au plus ; les lignes sans effet sont omises) ; forme courte LITE en trace complète. | Cohérent. La trace demande « ratio avant → après », mais la recette ne donne pas le ratio d'un texte qui passe (C21). |

**Charge (T-15) :** 70 170 octets au total. Le noyau en fait 43 201, les routes 26 969.

| Route | Octets | Part utile à ce parcours (estimation par lecture) |
|---|---|---|
| `DIRECTION/START/TREE` | 3 429 | Utile : arbre, frontière, Protection de niveau |
| `ACTION/RUN-LITE` | 831 | Utile |
| `ACTION/FAST-PATH` | 800 | Utile, mais contient l'ambiguïté C14 |
| `ACTION/GATE-A` | 11 583 | En grande partie utile (portée, contraste, profils), dont environ 3 Ko de mode d'emploi de la recette |
| `ACTION/GATE-B` | 10 326 | **1 591 octets utiles** (B2 et B6, servis par leurs sous-locators). B1b et l'atelier (4,7 Ko) ne concernent que DIRECTION, et l'atelier est déjà dans le noyau. |

### Réellement testé

| Test | Résultat |
|---|---|
| T-16 avant | `check_render` sur `preuves/p1/avant.html` : **RETURN**, `button.secondaire #a3a3a3 sur #ffffff = 2.52:1` (seuil 4,5:1), code de sortie 1, provenance AUTOMATED datée. |
| T-16 après | `preuves/p1/apres.html` (texte `#3f3f46`, bordure `#71717a`) : **PASS**, code de sortie 0. Ratio du texte calculé à part : **10,44:1**. |
| Limite observée | La bordure d'origine (`#d4d4d4`, environ 1,5:1) n'est pas signalée : la recette ne mesure pas le contraste non textuel (C21). |
| Sous-locators | `ACTION/GATE-B/B2` et `ACTION/GATE-B/B6` se résolvent déjà (1 206 et 385 octets). |

### Ce que le parcours apprend

- La partie « preuve » fonctionne de bout en bout : calcul, provenance, code de sortie exploitable.
- La partie « classer et charger » coûte environ 27 Ko de routes, dont une part importante ne sert pas ce cas.
- **Gain immédiat possible sans nouveau mécanisme :** dans la ligne LITE, citer `ACTION/GATE-B/B2` et `ACTION/GATE-B/B6` au lieu de `ACTION/GATE-B` (−8,7 Ko), et aligner FAST-PATH sur la Protection de niveau.

---

## P2 — Landing SaaS avec une vraie direction artistique

**Situation.** « Une landing pour notre SaaS de facturation, avec une vraie direction artistique. » Peu de contenu fourni.

### Sur papier

| Étape | Règle suivie | Observation |
|---|---|---|
| Classer | `DIRECTION/START` q2 (premier contact, identité) → `DIRECTION`. | Net. |
| Prendre le brief | Bloc BRIEF du noyau. | **Contradiction C01** : faut-il attendre la réponse avant de construire ou non ? C'est le premier geste de ce parcours, et la règle se contredit (§3 contre §8). |
| Charger | Ligne DIRECTION de CHARGE (trace légère) : EXTERNAL-START « si le brief est vague », CREATIVE-BOOT, VISUAL_TARGET, FIRST-OBJECT, FIRST-RENDER, UI-UX-REALITY, RUN-DIRECTION, GATE-A, GATE-C. | Le seuil de « vague » n'est pas défini. CREATIVE-BOOT, VISUAL_TARGET et FIRST-OBJECT font 19,8 Ko de vues voisines ; DIRECTION:116 dit qu'elles ne demandent pas trois descriptions concurrentes, mais l'agent doit les lire toutes les trois pour le savoir. |
| Exécuter | `RUN-DIRECTION` : « Exécuter le pipeline `ACTION/PIPELINE-DIRECTION` […] `ACTION/VISUAL_PROOF` ». | **Omission possible (C13)** : ces deux routes (14,2 Ko) ne sont pas dans CHARGE. Elles sont découvertes en cours de run, ou pas du tout. |
| Nommer le modal | CREATIVE-BOOT : `MODAL` « se nomme avec les marqueurs de vague datés de `SAVOIR/TOOLS` ». Test de trame du noyau (« pour un SaaS : promesse, logos, trois bénéfices, tarifs, FAQ »). | **Point fort.** Le noyau donne directement la trame modale d'un SaaS et la question de convergence palette et police : c'est actionnable dès la première minute. |
| Structurer | « Activer la bibliothèque » → `BIBLIOTHEQUE/SELECT` si le levier reste indéterminé. | 11,4 Ko supplémentaires, probables ici. |
| Boucler | Boucle d'édition, tableau d'activation du craft, Gate C en trace légère (« un critère absent déclenche son geste »). | Point fort : gestes concrets et conditionnés. Gate C renvoie au mauvais paragraphe pour la typographie (C12). |
| Répondre | Quatre rubriques en langage produit ; trace de six lignes. | Clair. |

**Charge (T-15) :** CHARGE donne 98 445 octets (43 201 de noyau et 55 244 de routes). Les renvois probables ajoutent 41 870 octets : PIPELINE-DIRECTION 12 571, BIBLIOTHEQUE/SELECT 11 389, CFT-00 5 783, DIRECTION-ATELIER 4 891, SAVOIR/TYPE 3 244, TOOLS/CONVERGENCE 2 338, VISUAL_PROOF 1 654. **Environ 140 Ko lisibles avant le premier rendu.** La copie mot pour mot avec le noyau n'en représente que 6 % : le poids vient des blocs entiers, pas des doublons.

### Réellement testé

- La charge en octets (T-15) et la résolution de toutes les routes citées.
- **Non testé : aucune landing n'a été construite.** La qualité du rendu, le temps jusqu'au premier artefact et les omissions réelles d'un agent restent inconnus. C'est l'objet de la prochaine action proposée.

### Ce que le parcours apprend

- Le savoir actionnable (trame modale, convergence, objet de preuve, gestes) est déjà dans le noyau. Le poids est dans les routes de procédure.
- Deux défauts de la règle touchent le tout début du run : la contradiction de prise de brief (C01) et la liste de chargement incomplète (C13).

---

## P3 — Changement d'un contenu canonique (décision §9.2 du plan)

**Situation.** Appliquer « construire dans le même tour, demandes dans la proposition » à la source canonique.

### Sur papier : fichiers à aligner trouvés par lecture et recherche

| Fichier | Lieu | Ce qu'il dit aujourd'hui | Trouvé par `--trouver --guides` ? |
|---|---|---|---|
| `DIRECTION.md` | 350, bloc BRIEF | « Humain présent : […] le build suit la réponse » | Oui |
| `SKILL.md` (noyau) | 43 | Copie compilée | Non : c'est un fichier généré, recompilé |
| `QUICKSTART.md` | 47 | « si la personne est présente, ces demandes précèdent le build » | Oui |
| `README.md` (et README Local) | 16 | « l'agent vous pose d'abord […] avant de construire » | **Non (C25)** |
| `references/examples.md` | 34 | « Prise de brief, en un seul échange, avant le build : la personne est présente » | **Non (C25)** |
| `validate_structure.py` | 227 | Garde exigeant « Humain présent » | Non : c'est un script |
| `validate_reading_map.py` | LCF-44 | Ordre des intrants et « au plus trois » | Non ; compatible avec le changement |

### Réellement testé (T-17, copie de travail git détachée, dépôt non modifié)

| Étape | Résultat |
|---|---|
| a) DIRECTION modifiée, noyau recompilé (43 116 / 46 000 octets) | `validate_all` **échoue** : « résumé infidèle (prise de brief : humain présent) » sur DIRECTION et SKILL. La garde protège l'**ancienne** décision. |
| b) Garde retirée | `validate_all` **passe** (« FULL VALIDATION PASSED »), alors que QUICKSTART, README et examples portent encore l'ancienne règle. |

### Ce que le parcours apprend

- Le coût d'un changement canonique tient moins aux sources qu'à leurs reprises non déclarées. L'outil de recherche en manque la moitié, et les validateurs signalent la source modifiée plutôt que ses reprises restées en retard (C03).
- C'est un cas de test prêt à l'emploi pour l'étape 3 : la vue d'impact devra lister ces sept lieux pour cette règle.

---

## Bilan des parcours : papier et test

| Parcours | Sur papier | Réellement testé | Non testé |
|---|---|---|---|
| P1 | Classement, chargement, preuve, trace | Charge, rendu avant/après avec `check_render`, sous-locators | Un agent réel suivant le parcours |
| P2 | Classement, brief, chargement, boucle, réponse | Charge et résolution des routes | **Construction de la landing**, qualité, durée, omissions |
| P3 | Inventaire des fichiers à aligner | Mutation canonique, validation, recherche `--trouver` | Mise à jour du CHANGELOG et des notes de version, export Local |
