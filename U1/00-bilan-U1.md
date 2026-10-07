# Unité U1 — Bilan

**Base :** `d90869c` sur `claude/repo-analysis-g87gag` (paquet V1.0.0, révision `R2026-10-04-AUDIT2-FIXES`). **Date :** 2026-10-07.
**Le dépôt n'a pas été modifié dans cette unité** (voir C20 : il n'existe aucun lieu admis pour des documents de travail).

| Document | Contenu |
|---|---|
| `01-registre-constats.md` | 25 constats : preuve, statut, gravité, parties concernées, disposition |
| `02-matrice-couverture.md` | Cinq absolus et intégrité : énoncé, noyau, activation, contrôle machine testé, écart |
| `03-parcours.md` | P1, P2 et P3, en séparant le papier du réellement testé |
| `preuves/reproduire_U1.py` | Rejoue les 17 tests sans modifier le dépôt ; sortie de référence dans `preuves/sortie_reproduire_U1.txt` |

## Ce qui a avancé

1. **Lecture intégrale** de DIRECTION, d'ACTION, du noyau `SKILL.md` et de SAVOIR/INTEGRITY. Lecture ciblée des validateurs et guides concernés. Les parties non lues sont déclarées.
2. **Les constats du plan sont vérifiés ou corrigés.** Les annexes 1, 3 (en partie), 4, 5, 6 et 7 et les essais de restauration du §2.2 sont reproduits. L'affirmation « le README est déjà aligné » (§9.2) est **fausse** (C02). Le compteur 27/30 n'est pas retrouvé (C23).
3. **Treize constats nouveaux** par rapport au plan (C03, C12 à C22, C25). Les plus structurants :
   - **C03** : les validateurs figent la formulation d'une règle et laissent passer ses reprises restées en retard (testé, T-17).
   - **C13** : la « seule liste de chargement » n'est pas complète. En DIRECTION, deux routes exigées par `RUN-DIRECTION` en sont absentes (14,2 Ko).
   - **C14** : une retouche de contraste est ambiguë entre LITE et un mode plus riche.
   - **C15** : un run LITE lit 70 Ko ; dans GATE-B, 1,6 Ko sur 10,3 Ko servent le cas, et des sous-locators existants permettraient d'alléger tout de suite.
   - **C18 et C19** : sur le chemin par défaut (trace légère), le noyau ne porte ni la déclaration préalable de l'absolu 4, ni le piège de conformité.
   - **C25** : la recherche ne voit pas le README ni les références de la skill.
4. **Matrice de couverture complète.** La protection machine est solide **en trace complète**. Sur 8 cartes modifiées, 6 sont refusées comme attendu. T-09 est admise conformément à la règle (réserve générée, verdict avec réserve). T-07 est admise à tort (preuve creuse). **En trace légère, chemin par défaut, aucun contrôle machine ne s'exécute** : le noyau est donc le lieu décisif.
5. **Trois parcours préparés** et partiellement testés : P1 avec un vrai rendu (contraste 2,52:1 → 10,44:1, `check_render` RETURN puis PASS) ; P3 avec une vraie mutation canonique. P2 reste sur papier pour la qualité.

## Sur quelles preuves on s'appuie

| Type | Exemples | Force |
|---|---|---|
| Reproduit par script | T-01 à T-17 | Rejouable sur toute version ; résultat observé |
| Lu à l'endroit cité | C01, C04 à C08, C12 à C14, C17 à C19, C22 | Vérifiable en ouvrant la ligne citée |
| Estimé | Part utile de GATE-A ; « renvois probables » de P2 | Jugement de lecture, non mesuré |
| Non vérifié | Tokens, qualité des rendus, comportement d'un agent qui découvre le système | Aucune donnée |

## Limites restantes

- **Même instance, biais d'ancrage** : aucune seconde lecture indépendante.
- **SAVOIR (hors INTEGRITY), BIBLIOTHEQUE, CHANGELOG, GLOSSAIRE, READING_MAP et schémas non lus** : la carte de couverture de l'étape 0 bis n'est pas complète.
- **Aucun run de design complet** : rien n'est encore établi sur la qualité de la première proposition, le temps ou les omissions réelles d'un agent.
- **Charges en octets**, pas en tokens.

## Décisions à prendre avant la suite

| # | Décision | Pourquoi maintenant | Options |
|---|---|---|---|
| D1 | Où vivent les documents de refonte (C20) ? | Rien de ce travail ne peut être versionné sans faire échouer la CI. | a) branche `refonte` séparée du paquet ; b) dossier `refonte/` exclu de l'inventaire par le validateur (modifie un script) ; c) dépôt séparé. |
| D2 | Une seule liste de chargement (C13) : compléter CHARGE ou retirer la carte d'ACTION ? | Conditionne toute réduction de charge. | — |
| D3 | Accord pour lancer des agents neufs pour la baseline ? | La prochaine action en dépend (coût en tokens). | — |

## Prochaine action précise : U2, mesurer la baseline **avant** toute modification du noyau

Pourquoi en premier : la correction de C01 (§9.2) change le comportement de l'agent au premier tour. Le plan prévoit de la comparer à « l'ancien comportement sur les mêmes briefs ». Si l'on corrige d'abord, l'ancien comportement n'est plus mesurable.

1. Figer la base : `d90869c`.
2. Trois briefs : P1 (fourni avec `preuves/p1/avant.html`), P2 (landing SaaS de facturation), et l'atelier de vélos de `examples.md` en brief flou.
3. Pour chaque brief, un agent **neuf**, avec le paquet seul et sans notre contexte. Relever : routes ouvertes et octets lus, questions posées, attente ou non avant de construire, nombre de tours jusqu'au premier artefact, `check_render` sur le rendu, affirmations non marquées, trace produite.
4. Lecture à l'aveugle de chaque rendu par une seconde instance neuve, sans trace ni corpus. Elle sera déclarée comme substitut, jamais comme regard humain (plan §9.1).
5. Livrable : `baseline-d90869c` (rendus, mesures et lectures), puis seuils arrêtés **avant** U3.

**U3 (après la baseline) :** un lot de corrections locales, chacune précédée d'une relecture intégrale des sections touchées et suivie de `validate_all` : C01 avec ses sept reprises (C02, C03, C25), C04, C07, C08, C12, C14, C15 (sous-locators), C17, C22 et la restauration (C10). Ensuite, le même protocole est rejoué sur les mêmes briefs.
