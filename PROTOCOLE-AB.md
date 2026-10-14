# Protocole A/B : préparé, non exécuté

Rédigé en manche 10. **Aucun run n'a eu lieu** et rien de ce document n'est un résultat. L'utilisateur a écarté l'exécution des deux systèmes sur un brief ; ce texte sert à décider plus tard, en connaissant le coût et ce que le dispositif peut ou ne peut pas dire. Il ne fait pas partie du paquet de Design Governance.

## 1. Ce qu'on voudrait savoir

| Question | Bras comparés |
|---|---|
| Q1. Les ajouts de la branche (inventaire du sujet, réglages, gabarits, images libres, relevés) changent-ils les rendus de DG ? | A2 contre A1 |
| Q2. DG change-t-il quelque chose par rapport à aucun skill ? | A1 contre A0 |
| Q3. DG contre Taste Skill v2, chacun avec ses outils ? | A2 contre A3 |

Q1 est la seule question qui décide de l'avenir des pilotes (`ADOPTED` ou retrait). Q2 et Q3 sont informatives.

## 2. Pourquoi les dispositifs existants ne suffisent pas

- **TS (`research.md` §11).** Un juré modèle par brief, bruit d'environ ±0,5 point, briefs de la manche finale déjà vus à la manche précédente, six briefs. C'est un signal de développement, pas un test.
- **DG (`ACTION/CLOSE-EXIT-CHECK`, « Mesure expérimentale de la méthode »).** Elle liste des observables au niveau d'un pilote : temps jusqu'au premier rendu jugeable, part des premiers rendus à corriger structurellement, part des corrections qui changent l'artefact, preuves encore `NOT-VERIFIED`, défauts récurrents, perception de qualité par plusieurs regards situés. Elle ne prévoit ni bras de comparaison, ni référence sans skill, ni relecture à l'aveugle, ni version figée par bras.
- **Particularité de DG, à ne pas oublier.** `SKILL.md` fait **20 246 octets avant et après** les changements des manches 4 à 10 : le noyau chargé est identique. La différence ne passe que par les routes lues à la demande (`DIRECTION/CHARGE` et les renvois du noyau) et par `check_render.py`. Si l'agent ne lit pas les routes ajoutées, A1 et A2 sont le même système. **L'exposition doit donc être mesurée**, sinon un résultat nul ne dit rien.

## 3. Bras

| Bras | Contenu | Version figée |
|---|---|---|
| A0 | aucun skill | sans objet |
| A1 | DG avant les changements | commit `897ed35` (parent de `8d91faf`) |
| A2 | DG avec les changements | `ccr-38b0a56f-t8xdo8` au dernier commit, empreinte notée avant le premier run |
| A3 | Taste Skill v2, avec ses scripts (tirage, lint, inspect) | version lue le 2026-10-14 ; relever l'empreinte |
| A4 (facultatif) | A2 sans l'inventaire du sujet (`CFT-01`) | seulement si A2 devance A1, pour isoler la pièce la plus lourde |

Pour chaque bras : même modèle et même version, mêmes outils (Node et Chromium disponibles, car les deux skills exécutent des scripts ; un bras sans outils est désavantagé), même budget de tours et de temps, même consigne d'utilisateur mot pour mot, aucune mémoire ni fichier d'instructions externe. Seul le skill chargé change.

## 4. Briefs

Huit briefs, écrits et figés **avant** de regarder un rendu, et jamais utilisés ensuite pour modifier un skill (un brief qui a servi à corriger un skill est brûlé ; c'est la limite que présente la manche finale de TS, dont les briefs avaient déjà été vus à la manche précédente).

**Écarté d'avance : le brief « atelier de vélos »**, qui a servi en manche 3 à des mesures qui ont orienté des changements de DG.

| # | Langue | Type | Ce qu'il éprouve |
|---|---|---|---|
| 1 | fr | Vitrine d'une activité locale, contenu fourni en partie | identité, contenu manquant marqué comme exemple |
| 2 | en | Page produit, trois photographies fournies | usage d'une ressource réelle, texte sur image |
| 3 | fr | Tableau de bord de suivi de chantier | états vides, erreurs, densité, application plutôt que vitrine |
| 4 | en | Article long (environ 2 500 mots fournis) | lecture, typographie, rythme |
| 5 | fr | Brief vague : « une page pour ma librairie de quartier » | prise de brief, premier objet, plafond déclaré |
| 6 | en | Retouche locale : page existante fournie, héros faible | mode `ITER`, conservation de ce qui tient |
| 7 | fr | Formulaire d'inscription à un service public | sobriété comme bonne réponse, accessibilité, récupération après erreur |
| 8 | en | Identité d'une céramiste, nom et quatre photographies fournis | direction, ancre, cohérence d'une série |

Moitié français, moitié anglais : la langue de la skill (française pour DG, anglaise pour TS) est un facteur, il faut le voir et non le subir.
Les briefs 1, 3, 5 et 7 sont hors du terrain habituel de TS (vitrines) ; les briefs 2, 4 et 8 sont dans le sien. Un protocole composé de vitrines favoriserait TS ; un protocole sans vitrine favoriserait DG.

Deux répétitions par bras et par brief (la graine ne se contrôle pas) : `4 bras × 8 briefs × 2 = 64` sessions, ou `3 bras × 8 × 2 = 48` sans A4.

## 5. Fabrication des rendus

- Sortie attendue : un dossier avec l'artefact (page ou projet).
- Captures prises **par l'expérimentateur**, avec un script indépendant des deux skills, à 390, 768 et 1440 px, après le même défilement. L'agent ne fournit pas sa propre capture aux relecteurs.
- **Journal d'exposition** (indispensable) : fichiers de skill lus, routes lues (appels à `read_route.py`), scripts exécutés (`check_render.py`, `draw.mjs`, `inspect.mjs`, `lint.mjs`, `assets.mjs`), nombre de tours, durée, jetons consommés.
- L'agent n'a accès ni aux rendus des autres bras ni aux briefs des autres.

## 6. Anonymisation

- Rendus renommés au tirage ; commentaires, métadonnées, traces de run (handoff de DG, rapports de TS) **retirés** du dossier montré aux relecteurs : seuls l'artefact et les captures sont vus.
- L'aveugle est imparfait : le style maison de TS et l'ordre de lecture de DG se reconnaissent. On le mesure plutôt que de le nier : à la fin, chaque relecteur devine le bras de chaque rendu ; le taux de bonnes réponses est publié avec les résultats.
- Ordre de présentation randomisé par relecteur.

## 7. Jugement

Trois sources, **jamais fondues en un seul nombre**.

1. **Contrôles mécaniques.** Pour chaque rendu, les statuts de `check_render.py` et de `inspect.mjs`, rapportés séparément (matrice rendu × contrôleur). Aucun des deux n'arbitre : leurs champs sont presque disjoints (manche 3). Un contrôleur tiers (par exemple axe-core) est souhaitable pour le contraste, le focus et les noms accessibles.
2. **Relecture humaine à l'aveugle.** Au moins trois relecteurs distincts de l'auteur des skills. Pour chaque brief, comparaison par paires dans l'ordre tiré (préféré, ex æquo, moins bon) avec une phrase de raison ; pas de note sur 10 (le bruit de ±0,5 relevé par TS montre qu'une telle échelle n'a pas la résolution). Critères guidés après un premier avis libre : spécificité, hiérarchie, finesse, adéquation au brief.
3. **Juré modèle** (secondaire). Un juré par rendu, sans connaître le bras, deux passes avec ordre permuté. Il sert à mesurer son accord avec les humains, pas à décider.

**Compte objectif de vérité du contenu**, par rendu : nombre de signes de preuve inventés (logo client, avis, chiffre, mention officielle présentés comme réels). DG et TS les interdisent tous les deux ; c'est le seul critère de gouvernance qui se compte sans avis.

## 8. Analyse décidée avant de voir les données

- **Unité d'analyse : le brief**, pas le relecteur ni la paire. Huit briefs donnent huit observations, pas vingt-quatre.
- Pour chaque comparaison de bras, nombre de briefs où le premier bras est préféré par la majorité des relecteurs (les ex æquo sont écartés ; **plus de deux ex æquo : pas de conclusion**).
- **Ce que huit briefs permettent.** Test des signes unilatéral : 8 sur 8 donne p = 0,004 ; 7 sur 8, p = 0,035 ; 6 sur 8, p = 0,145. Donc seul un écart **net** (7 ou 8 sur 8) est établi.
- **Puissance.** Si le vrai taux de préférence est de 70 % par brief, la probabilité d'obtenir au moins 7 sur 8 est d'environ **25 %**. Le dispositif peut confirmer un gain important et **manquera un gain modeste**. Un résultat nul ne prouve pas l'absence d'effet.
- **Critères posés d'avance pour Q1 :**
  - passage en `ADOPTED` d'un pilote : A2 préféré à A1 sur 7 briefs sur 8 ou plus, **exposition démontrée** (les routes ajoutées ont été lues dans au moins la moitié des sessions de A2 où elles s'appliquaient), aucun `RETURN` mécanique de plus qu'en A1, aucun signe de preuve inventé de plus ;
  - retrait : A1 préféré ou ex æquo sur 5 briefs sur 8 ou plus, ou régression mécanique ;
  - entre les deux : prolongation, et on ne conclut pas.
- Analyses secondaires, rapportées sans seuil : exposition par route, défauts mécaniques par bras, jetons et durée par bras, taux de dévoilement de l'aveugle.
- **Convergence (principe D4).** Question : DG, qui compte sur la discipline du modèle pour ne pas converger, converge-t-il plus que le même modèle sans skill (A0) ou avec le tirage de TS (A3) ? Mesure objective, tirée du relevé `--mesures` de chaque rendu : pour chaque brief et chaque bras, la **distance entre les deux répétitions** (teinte chromatique dominante, luminosité du fond, famille de titre, nombre de fonds de section, nombre de bords gauches, ossature) et, entre briefs, la dispersion de la teinte et de la luminosité du fond. Une distance faible entre deux répétitions signifie que le bras donne la même réponse à chaque fois. **Lecture décidée d'avance** : si A1 et A2 convergent nettement plus que A0 et que A3, alors seulement un tirage externe avec historique (point N2 des notes) devient défendable ; sinon la pluralité par discipline suffit et on n'ajoute pas de script. Limites : deux répétitions seulement, une distance mesurée sur le premier écran, des briefs qui imposent eux-mêmes une partie de la palette (contenu fourni).

## 9. Extension de `EVALUATION_CASE` (spécification, **non écrite dans DG**)

Aujourd'hui `EVALUATION_CASE` désigne « un pilote ou une série de runs » sans champ pour comparer. Si le protocole est lancé, ajouter, pour un cas de comparaison seulement :

| Champ | Contenu |
|---|---|
| `BRAS` | identifiant, version figée (empreinte), modèle, outils, budget |
| `BRIEF` | texte exact, date, statut (neuf, vu, brûlé) |
| `EXPOSITION` | fichiers et routes lus, scripts exécutés, durée, jetons |
| `RELECTURE` | relecteurs (rôle, relation à l'auteur), aveugle oui ou non, méthode, résultat par relecteur, taux de dévoilement |
| `MÉCANIQUE` | statuts de chaque contrôleur par rendu, séparés |
| `LIMITES` | bruit, nombre de briefs, ex æquo, puissance |
| `DÉCISION` | adopté, retiré ou prolongé, avec renvoi à la ligne de `maintenance/versions.md` |

Contraintes de cohérence avec le paquet : pas de score agrégé, pas de seuil esthétique (la section de mesure expérimentale écrit déjà que ces mesures « ne créent ni verdict esthétique, ni quota »), `OBSERVED` n'est pas `PASS`. **Non écrit** : cela ajouterait une obligation à un paquet qui n'en a pas l'usage avant un premier run réel ; à rédiger avec lui.

## 10. Ordre et coût

1. **Essai à blanc** sur un seul brief écarté (le brief « atelier de vélos »), sans comparer, pour vérifier le journal d'exposition, l'anonymisation et les captures.
2. **Q1** seule : A1 et A2, 8 briefs, 2 répétitions : 32 sessions.
3. **Q2 et Q3** seulement si Q1 est informatif ou si l'utilisateur veut la réponse pour elle-même : A0 et A3 en plus : 64 sessions au total.
4. Version minimale pour décider d'un seul pilote : A1 et A2, briefs 1, 5, 6 et 8 (ceux où l'inventaire du sujet devrait peser), 2 répétitions : 16 sessions. **Elle ne peut pas atteindre 7 sur 8** : elle ne servirait qu'à vérifier l'exposition et à repérer une régression, pas à promouvoir.

## 11. Risques du dispositif

- **Exposition nulle** : l'agent ne lit pas les routes ajoutées (voir 2). Un cas à anticiper : le noyau ne cite pas `CFT-01` à l'ouverture ; `DIRECTION/CHARGE` le charge « si la composition, la typographie ou l'ancrage peuvent modifier la décision », ce qui laisse l'agent juge.
- **Contamination** : les modèles connaissent peut-être Taste Skill (dépôt public). Non maîtrisable ; à noter.
- **Charge de contexte** : TS lit environ 2,4 fois plus de matière que DG (manche 3). Un écart de rendu peut venir de la charge, pas du contenu ; les jetons sont mesurés.
- **Préférence n'est pas qualité** : une préférence de relecteurs ne dit ni conversion ni accessibilité réelle. Elle reste un avis situé.
- **Biais de l'expérimentateur** : l'auteur de la branche A2 est aussi celui qui rédige le protocole. Les briefs et les critères doivent être figés et datés avant le premier run, de préférence relus par une personne qui n'a pas écrit les changements.

## 12. Ce que ce protocole ne dira pas

- Quel système est meilleur en général.
- L'effet de chaque pilote pris seul (sauf A4).
- La valeur de la traçabilité de DG (trace, handoff, limites déclarées) : aucune relecture de rendu ne la voit. Elle se juge par un autre type de cas (reprise d'un run par une autre personne, par exemple).
- Aucune conclusion sur un usage réel (visiteurs, conversion, maintenance).
