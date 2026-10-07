# U1b — Fiche d'inventaire n°8 : les schémas et les exemples de données

**Base :** commit `d90869c`. **Lecture intégrale :** les 4 schémas (`run_card`, `domain_frame`, `research_brief`, `production_contracts`), les 4 exemples, et les 25 fixtures. Pour les fixtures, j'ai comparé chacune, champ par champ, à `run_card.example.json` (script `U1b/jsondiff.py`), afin de voir exactement ce que chacune modifie. **Vérifié aussi :** qui consomme ces fichiers (scripts et documents), les deux suites de validation (toutes deux passent), et trois tests de limite (T-18 à T-20, dossier `U1b/preuves/`). **Angle :** ce que ces structures permettent de **consigner** sur une réalisation, et ce qu'elles laissent hors champ.

## 1. Identité

| Fichier | Taille | Décrit | Validé par | Nommé dans la doctrine ? |
|---|---|---|---|---|
| `run_card.schema.json` | 15 Ko | La fiche d'un run : décision, risque, sources, preuve, clôture | `validate_run_card.py` (validateur maison, pas la bibliothèque jsonschema) | Oui : ACTION l. 405, `machine_projection.md`, READING_MAP |
| `run_card.example.json` | 5 Ko | Un run DIRECTION fictif, clôturé avec réserve | Idem, plus `--strict` après remplacement des chemins | Oui |
| `domain_frame.schema.json` + exemple | 3 + 3 Ko | Le cadrage d'un domaine (16 champs) | `validate_contracts.py` | Oui : gabarit DOMAIN-FRAME de DIRECTION (l. 246), qui « reprend exactement » ses clés |
| `research_brief.schema.json` + exemple | 2 + 2 Ko | Une recherche ciblée : question, décision à risque, profondeur, entrées, condition d'arrêt | `validate_contracts.py` | **Non** : seul le README le cite |
| `production_contracts.schema.json` + exemple | 3 + 6 Ko | Trois contrats : directions créatives comparées, réalité UI/UX, cas d'évaluation | `validate_contracts.py` | Oui : ACTION/STRUCTURED-PROOF (l. 626-638) et l. 551 |
| `fixtures/` (25 fichiers) | 66 Ko | 3 cartes valides, 22 invalides, chacune avec le diagnostic attendu | Table déclarative de `validate_run_card.py` (l. 678-703) | Non (outillage de test) |

Aucun de ces fichiers n'est cité par le noyau `SKILL.md` (0 occurrence). L'agent n'y arrive que par ACTION ou par `machine_projection.md`.

## 2. Ce que les schémas possèdent

Niveaux : **A** actionnable · **O** orientant.

### RUN_CARD : une fiche de gouvernance très complète

| Bloc | Champs | Concr. | Ce qu'il consigne |
|---|---|---|---|
| Identité et décision | `id`, `owner`, `date_version`, `mode`, `decision`, `decision_intent` | A | Qui, quand, quel mode, quelle décision |
| Risque | `level` (normal, important, critical), `statement`, `critical_protection` (contrôle, owner, scope, action en cas d'échec, preuve, résultat) | A | Le risque et, s'il est critique, sa protection nommée |
| Direction | `thesis`, `anti_direction`, `first_object`, `scope`, `constraint`, `identity_stake`, `calibration` (sur quoi repose l'écart : ancre observée, fournie, contrainte réelle, ou génération seule) | A | La direction en une thèse, ce qu'elle refuse, son premier objet |
| Ancres | `role`, `type` (générée, observée, fournie), `source`, `retained`, `rejected`, `transformation`, `transformation_status`, `limitation` | **A** | **La seule structure qui oblige à dire ce qu'on prend d'une référence, ce qu'on refuse, et comment on le transforme** : un garde-fou direct contre la copie |
| Capacités | `available`, `unavailable`, `not_required`, `basis` (résultat d'outil, environnement attesté, source utilisateur, déclaration non attestée) | A | Ce que le run pouvait réellement faire, et sur quelle base |
| Preuve | `observed`, `not_verified`, `provenance` (artefact, version, méthode, date, capacité) | A | Ce qui a été vu, ce qui ne l'a pas été, d'où vient l'observation |
| Clôture créative | `presence`, `signature`, `craft_detail`, `dominant_defect`, `next_polish_action` | O | Cinq phrases sur la qualité perçue ; texte libre |
| Profil | `profile_decision` : phase (visée ou observée), décision, réglages, contre-indication, preuve | O | Un réglage de registre (densité, contraste…) et sa limite ; texte libre |
| Changement de décision | `outcome` (changée, confirmée, abandonnée…), `value`, `evidence` | A | Si le travail a réellement changé quelque chose |
| Clôture | `state`, `direction_status` (tenue, tenue avec écart accepté, partiellement tenue, perdue au build), `issue`, `verdict`, `limitations`, `axes` V/U/A/T, `reservations` (7 champs), `exception` (10 champs), `system_package` (migration, retour arrière, non-régression), `b1b` (paire avant/après), `reclassification` | A | Une clôture honnête et traçable, avec réserves datées et sortie prévue |

**Règles métier contrôlées** (lues dans la table des fixtures) : un verdict accepté exige une observation, une provenance, une limitation non vide, un état DECIDED ou CLOSED, et des ancres transformées ; une direction perdue au build ne peut pas être acceptée ; un risque critique exige une protection nommée, sans placeholder ; un run DIRECTION exige `direction`, `trace_locator`, et à la clôture `creative_close` et `direction_status` ; « PASS » est réservé aux axes, pas au verdict global ; chaque capacité déclarée disponible doit avoir une base.

### Contrats de production

| Contrat | Champs clés | Concr. | Valeur au regard de la mission |
|---|---|---|---|
| `creative_direction_set` | Au moins 2 directions, chacune avec une tension, des changements structurels et un premier objet ; direction retenue ; test de divergence ; raison de la convergence | **A** | **La seule structure du paquet qui exige de la diversité** avant de choisir |
| `ui_ux_reality_pack` | Modèle de contenu, tâche principale, premier geste, matrices d'états, de largeurs, d'accessibilité et de robustesse, portée attendue et observée, carte de couverture | **A** | **L'outil UI le plus concret du paquet.** Le validateur exige que chaque exigence déclarée soit couverte, quitte à la marquer non vérifiée. Rien ne peut disparaître par omission |
| `evaluation_case` | Brief, domaine, capacités, profondeur, artefact, observations, résultats de tâche, résultats d'accessibilité, revue visuelle, corrections, limites finales | A | **Un format déjà prêt pour mesurer le système lui-même**, c'est-à-dire l'objet de U2 et U5 |

### DOMAIN_FRAME et RESEARCH_BRIEF

| Contrat | Ce qu'il apporte | Concr. |
|---|---|---|
| `domain_frame` | 16 champs (public, expertise, JTBD, modèle de confiance, actions et états critiques, conventions, contexte culturel, tolérance à l'originalité, risques, recherches requises, plan de preuve) ; le validateur relie chaque risque déclaré à un contrôle ou une revue, et les contrôles au plan de preuve | A |
| `research_brief` | Question, décision à risque, profondeur, incertitude avant et après, condition d'arrêt ; chaque entrée doit produire une décision changée **et** une conséquence sur l'artefact ; une source « vérifiée dans le run » exige un locator et une date | A |

### Les exemples : un cas cohérent de bout en bout

Les trois exemples de contrats décrivent **le même cas** : le premier écran d'un outil B2B de pilotage d'incidents industriels. Domaine, recherche (entretiens opérateurs), deux directions comparées (A « instrument précis », B « investigation progressive »), matrice d'états (chargement, vide, erreur, données en retard, succès), couverture observée ou non, puis évaluation avec corrections et limites. C'est **le seul exemple concret et chaîné du paquet**. Ses chiffres (« 3 opérateurs sur 4 ») sont illustratifs et ne sont pas marqués comme tels dans le fichier.

## 3. Ce que les schémas ne possèdent pas

1. **Aucun champ pour le contenu de la réalisation.** Typographie, couleur, composition, grille, assets, textes : rien n'a de champ structuré. Tout ce qui touche à la forme passe par du texte libre (`thesis`, `first_object`, `craft_detail`, `dials`…). Les six contrats d'ACTION qui portent ce contenu (carte de hiérarchie, preuve U, partition typographique, fiche d'asset, composant partagé, motion) restent des gabarits texte sans schéma. Seuls 3 des 9 contrats en ont un.
2. **Le RUN_CARD d'exemple n'est relié à aucun cas réel.** Il reste abstrait (« Objet principal qui rend la relation produit-geste observable », `chemin-ou-url-local`). Il revendique une capacité « navigateur/capture » de type `tool_result` (« Captures du rendu »), alors qu'aucun outil du paquet ne produit de capture (fiche n°6). Il n'existe pas de RUN_CARD pour le cas des incidents.
3. **RESEARCH_BRIEF est orphelin.** Aucune source normative ne le nomme. SAVOIR décrit sa propre fiche de source en 12 rubriques (l. 556-569), qui diverge du schéma :

   | Côté SAVOIR seulement | Côté schéma seulement |
   |---|---|
   | ROLE, TRACE-LOCATOR obligatoire, OWNER / NEXT-PROOF | `reliability_basis`, `artifact_consequence`, `source_class` |
   | — | Tout le niveau du brief : question, décision à risque, profondeur, incertitude avant et après, condition d'arrêt |

4. **Les validateurs contrôlent la forme, pas la substance** (testé ; tous les codes de sortie valent 0) :

   | Test | Ce qu'il contient | Résultat |
   |---|---|---|
   | T-18 | Deux directions créatives identiques, à un point final près dans la tension (même premier objet, mêmes changements structurels) | **Acceptées comme distinctes** |
   | T-19 | DOMAIN_FRAME rempli de « ok », « m », « s », avec des liens risque → contrôle → preuve formellement corrects | **Accepté** |
   | T-20 | RESEARCH_BRIEF en lettres isolées, profondeur « targeted », une entrée | **Accepté** |

   C'est la limite normale d'un validateur automatique, et le même constat que pour la RUN_CARD en U1 (42 champs creux acceptés). Mais le nom `divergence_test` promet plus que ce que le contrôle vérifie : seule l'identité littérale est refusée.

## 4. Potentiel présent mais peu exploité

| Élément | Pourquoi il compte au regard de la mission | Accès actuel |
|---|---|---|
| **Ancres** (retenu, refusé, transformation) | Rend la distinction et la non-copie traçables | Dans la RUN_CARD, rarement remplie hors DIRECTION |
| **`creative_direction_set`** | Seule exigence structurée de diversité avant convergence | Conditionnel ; absent du noyau |
| **`ui_ux_reality_pack`** | Empêche qu'un état ou une largeur disparaisse par omission | Absent du noyau |
| **`evaluation_case`** | Format déjà prêt pour enregistrer les runs de référence (U2) et la remesure (U5) | Utilisé nulle part hors de l'exemple |
| **Le cas « incidents » chaîné** | Seul exemple qui va du domaine à l'évaluation | Dans `schemas/examples/`, non cité par la skill |

## 5. Observations à verser au registre

| Observation | Preuve | Lien |
|---|---|---|
| Aucun champ structuré pour la forme (typographie, couleur, composition, assets) ; seuls 3 contrats sur 9 ont un schéma | Schémas ; ACTION l. 630-638 | Fiche n°5 |
| RESEARCH_BRIEF n'est nommé par aucune source normative et diverge de la fiche de source de SAVOIR | `git grep` ; SAVOIR l. 556-569 | Nouveau |
| Les validateurs de contrats acceptent des directions quasi identiques et des cadrages creux | T-18, T-19, T-20 | Parent de la limite déjà relevée pour la RUN_CARD (U1) |
| L'exemple RUN_CARD revendique des « captures » de type résultat d'outil, qu'aucun outil du paquet ne produit | `run_card.example.json` l. 74-76 | Fiche n°6 |
| Les chiffres de l'`evaluation_case` d'exemple ne sont pas marqués comme illustratifs | Exemple l. 49 | Mineur |
| `evaluation_case` est candidat naturel pour consigner U2 et U5 | Schéma | Plan, U2 (à discuter, rien de décidé) |

## 6. En une phrase

Les schémas possèdent **une gouvernance des runs très complète et bien contrôlée** (risque, preuve, capacités, clôture honnête), **trois contrats de grande valeur** (directions comparées, réalité UI/UX, cas d'évaluation) et **le seul exemple chaîné du paquet**. Mais ils **ne consignent rien de la forme elle-même**, un contrat (RESEARCH_BRIEF) n'est relié à aucune doctrine, et leurs validateurs, comme celui de la RUN_CARD, vérifient la **forme** des réponses et non leur **substance**.
