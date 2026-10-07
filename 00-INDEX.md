# Index de la refonte Design Governance : tout ce qui a été fait

**Mis à jour le :** 2026-10-07. **Dépôt :** `Palolo875/DESIGN-GOVERNANCE1`, branche `claude/repo-analysis-g87gag`.

**Seul changement apporté au dépôt :** le commit `d90869c`. Il remplace la copie Markdown par le paquet source de 69 fichiers. La CI est verte (run 37603355045). Aucune PR n'est ouverte.

Toutes les dates de cette page sont le 7 octobre 2026. Le travail s'est fait en une suite de sessions, et le contexte a été résumé une fois en cours de route.

---

## 1. Chronologie des échanges et des décisions

| # | Ta demande (résumée) | Ce qui a été fait | Décision |
|---|---|---|---|
| 1 | « Analyser le repo et donner mon avis » | Analyse du dépôt, qui ne contenait alors que la copie Markdown ; avis et recommandations | — |
| 2 | « Juste la recommandation 1 » | Restauration du paquet source (69 fichiers, empreintes vérifiées) ; commit `d90869c` poussé ; CI verte | Le dépôt git devient la source |
| 3 | Discussion du plan externe `Plan_final_refonte…v2` | Lecture et discussion | — |
| 4 | Démarche d'audit en quatre axes (organisation, capacités, fiabilité, relations) | Discussion et vérification | Reprise au §5 du plan v2 |
| 5 | Objectifs, et analyse d'un autre agent à vérifier | Vérification d'environ 60 affirmations ; 12 constats ajoutés (C26 à C37) | `U1/04` |
| 6 | « Étape par étape, zéro négligence » : constats, matrice, parcours | Unité U1 : registre, matrice des cinq absolus, trois parcours (P1 et P3 testés), 17 tests rejouables | `U1/00` à `U1/03` |
| 7 | Verdicts fichier par fichier d'un autre texte | Lecture et vérification | — |
| 8 | « Des textes à discuter, pas d'implémentation directe » | Règle adoptée | Aucune modification du dépôt sans accord |
| 9 | Plan v2_2, « rendre le système intelligent », puis « ne pas compliquer sans nécessité » | Discussion ; mécanismes inutiles écartés | Principe de simplicité |
| 10 | « Un plan solide, détaillé, structuré » | Plan de route v1 (U2 à U8) | `U1/05-plan-de-route-v1.md` |
| 11 | Ta mission et ton critère pour Design Governance | Intégrés au plan ; constats C38 et C39 | Mission et critère adoptés |
| 12 | « Vérifier ce que le système possède et son potentiel », lecture complète | Inventaire U1b : 10 fiches et une synthèse par couche ; tests T-18 à T-23 | `U1b/01` à `U1b/11` |
| 13 | « Les 5 points : je te laisse le choix » ; discuter créativité, gouvernance et potentiel ; ne pas figer par des exemples ou du code ; recherches complètes ; audit en 4 axes dans le plan ? | Choix des 5 points ; trois recherches extérieures ; lecture de l'historique (ancien dépôt) ; note de discussion | `U1b/12` ; `recherches/` |
| 14 | Juges : toi à la fin, et des sous-agents Sonnet 5.5 et Haiku 5.5 ; condition sans système acceptée, en ménageant ton usage ; ajouts validés après discussion | Sortie de Haiku 5.5 vérifiée (7 octobre) ; mon affirmation contraire corrigée | Décisions D3, D4, D5 du plan v2 |
| 15 | « Corriger d'abord ce qui peut l'être sans run ; recenser ; mettre le plan à jour ; l'ancien dépôt est obsolète » | Registre porté à C01–C60, chacun typé ; plan v2 ; cet index ; correction d'une erreur de la synthèse (motif M2) | Règle 1 du plan v2 : corriger, puis mesurer, puis parier |

## 2. Où se trouve chaque chose

Racine : mon espace de travail (`scratchpad/`).

### Documents de référence, à lire dans cet ordre

| Fichier | Contenu |
|---|---|
| `00-INDEX.md` | Cette page |
| `U1/05-plan-de-route.md` | **Plan v2** : règles, décisions prises et à prendre, grille en quatre axes, unités U2 à U8, place de chaque constat |
| `U1/01-registre-constats.md` | **Registre** C01 à C60, avec preuve, statut, gravité, type (A, D, M, S) et disposition |
| `U1b/11-synthese.md` | Ce que le système possède, couche par couche |
| `U1b/12-discussion-creation-gouvernance.md` | Créativité, gouvernance, exemples et slop, potentiel ; sources |

### Unité U1 : constats et vérifications

| Fichier | Contenu |
|---|---|
| `U1/00-bilan-U1.md` | Bilan de l'unité 1 |
| `U1/02-matrice-couverture.md` | Couverture des cinq absolus et de l'intégrité |
| `U1/03-parcours.md` | Trois parcours ; P1 (contraste) et P3 testés |
| `U1/04-verification-analyse-externe.md` | Vérification d'environ 60 affirmations d'une analyse externe |
| `U1/01-registre-constats-v1.md`, `U1/05-plan-de-route-v1.md` | Versions précédentes, conservées pour traçabilité |
| `U1/preuves/reproduire_U1.py` et `sortie_reproduire_U1.txt` | Tests T-01 à T-17, rejouables sans modifier le dépôt |
| `U1/preuves/p1/` | Page de test du contraste, avant et après (#a3a3a3 → #3f3f46, de 2,52:1 à 10,44:1) |
| `U1/preuves/restaurer_embarque.py` | Script de restauration extrait de la copie (identique à `RESTORE`) |

### Unité U1b : inventaire

| Fichier | Contenu |
|---|---|
| `U1b/01-SAVOIR.md` à `U1b/10-validateurs.md` | Une fiche par partie du paquet : SAVOIR, BIBLIOTHEQUE, skill, DIRECTION, ACTION, outils, guides, schémas, CHANGELOG, validateurs |
| `U1b/10-notes.md` | Notes de lecture des validateurs |
| `U1b/preuves/` | Tests T-18 à T-23 et journal de `validate_all` (125 s) |
| `U1b/test/police.html` | Page de test des polices externes (C39) |
| `U1b/jsondiff.py` | Comparaison des fixtures champ par champ |

### Recherches

| Fichier | Contenu |
|---|---|
| `recherches/01-fixation-uniformisation.md` | Fixation de design, uniformisation par les modèles, ancrage sur les exemples |
| `recherches/02-retour-visuel-evaluation.md` | Pratiques des éditeurs, boucles visuelles, juges automatiques, protocoles d'évaluation |
| `recherches/03-skills-gouvernance.md` | Recommandations d'Anthropic sur les skills, contexte long, gouvernance des design systems, taille des skills comparables |
| `recherches/04-historique-DG-AUDIT-001.md` | Lecture de l'ancien audit. **Obsolète**, contexte seulement |
| `skills/`, `dl/` | SKILL.md téléchargés pour la comparaison (frontend-design, impeccable…) |
| `acar/`, `chan.txt`, `gb.txt`, `pdf/` | Articles téléchargés par les recherches |
| `tools/` | Petits scripts de comptage écrits par l'agent de recherche sur l'historique |

### Ancien dépôt (obsolète)

| Emplacement | Statut |
|---|---|
| `historique/kit/` (29 Mo) | Archive extraite de `Palolo875/design-governance`, version V1.1.1 du 26 septembre. **Obsolète** selon ta décision ; jamais exécutée, seulement lue |
| `/home/user/palolo875/design-governance` et `design-g.` | Clones en lecture seule. `DESIGN-G.` est vide |

### Fichiers de travail intermédiaires

Ces fichiers ne sont pas des livrables. Ce sont les copies et les cartes de test qui ont produit les preuves déjà consignées.

| Emplacement | Origine |
|---|---|
| Racine : `A1_…json` à `A4_…json`, `eleve_…json`, `okcard.json`, `preuve_creuse_…json`, `textes libres ok1..ok46…json`, `temoin_…json`, `normal_…json`, `base_strict.json`, `x.json`, `x2.json`, `pc_vide.json` | Cartes de test des tests T-06 à T-14 et de la vérification de l'analyse externe |
| Racine : `orig.md` | Copie Markdown d'origine (`DG-COPY files=69`) |
| Racine : `prep.log`, `va.log`, `p3.log`, `p3b.log`, `restaurer.py` | Journaux de préparation, de validation et des parcours |
| `fresh/`, `pkg/` | Copies du paquet, pour les tests de restauration et de build |
| `rt/` | Tests de restauration (T-01 à T-05) |
| `md/` | Copies Markdown régénérées |
| `p1/` | Première version de la page du parcours P1 |

On peut les supprimer sans perte, puisque leurs résultats sont dans les livrables. Je ne le fais pas sans ton accord.

## 3. État actuel

| Élément | État |
|---|---|
| Dépôt | Lots L3 et L4 faits : 13 constats corrigés (L3 : C01, C04, C13, C14, C15, C17 ; L4 : C10, C25, C38, C39, C43, C45, C47), dernier commit `f796824`, `validate_all` vert ; suivi dans `U1/01-registre-constats.md`, section « Suivi des corrections » |
| Constats | 60 : 32 de type A (lots L1 à L5, plus C09 en option), 5 de type D (lot L6), 16 de type M (U4 et U7), 5 de type S, et 2 déjà traités (C02 dans le plan, C20 par la décision D1). Décompte vérifié par script |
| Plan | v2 accepté ; U2 en cours, ordre L3, L4, L5, L6 (D7, D8), L2, L1 |
| Décisions prises | D1 à D6 (plan v2, §4.1) |
| Décisions à prendre | D7 à D13 (plan v2, §4.2). Aucune ne bloque les lots L1 à L5 |
| Prochaine action | Lot L5 : C34 |

## 4. Erreurs de mon côté, corrigées

| Erreur | Correction |
|---|---|
| Glossaire compté à 63 termes | 57 (vérification de l'analyse externe) |
| C39 : « check_render bloque les ressources externes » | Le blocage est le comportement par défaut ; l'option `--allow-external` existe mais n'est pas documentée |
| Fiche n°7 : « 5 versions du parcours » | Au moins 6 (RELEASE_NOTES) |
| Synthèse, motif M2 : « points de départ annoncés et non tenus » | Choix assumé (DIRECTION l. 137), pas une promesse |
| « Haiku 5.5 n'existe pas » | Sorti le 7 octobre 2026 (`claude-haiku-5-5`) ; vérifié après ta remarque |
