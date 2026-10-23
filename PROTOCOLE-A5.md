# Protocole de la campagne d’évaluation (A5)

Validé le 2026-10-23 avec les décisions de la section 10. Sert de `campaign.protocol` aux contrats `EVALUATION_CASE`.

## 1. Ce que la campagne éprouve

L’hypothèse du cap, question par question, par comparaison avec un travail fait sans le système :

| Question | Ce qu’on regarde |
|---|---|
| **Q1 — orienter les choix** | Les rendus ont-ils une direction située plutôt que la réponse modale ? Se répètent-ils d’un brief à l’autre ? |
| **Q2 — mobiliser les bons moyens** | L’agent lit-il les routes que les signaux du brief appellent ? Lesquelles manque-t-il ? |
| **Q3 — conduire au niveau visé** | Le rendu final est-il meilleur, avec moins d’oublis et de reprises inutiles ? |

La campagne est petite : elle produit des observations situées, pas une preuve statistique. Elle dit ce qu’elle n’a pas pu observer.

## 2. Briefs

Huit briefs fixés à l’avance, écrits une fois et donnés tels quels dans les deux conditions. Ils varient le domaine, le mode, le risque et la quantité de contenu fourni.

| N° | Brief (résumé) | Mode attendu | Particularité |
|---|---|---|---|
| 1 | Page d’une boulangerie de quartier | `DIRECTION` | Brief vague, contenu réel absent |
| 2 | Prise de rendez-vous d’un cabinet médical | `STANDARD` | Risque critique (santé, formulaire) |
| 3 | Premier écran de pilotage d’incidents (B2B) | `DIRECTION` | Données denses |
| 4 | Fiche produit d’une boutique en ligne de vêtements | `STANDARD` | Commerce en ligne, guide des tailles |
| 5 | Article long d’un média indépendant | `DIRECTION` | Lecture, typographie dominante |
| 6 | Programme d’un festival | `DIRECTION` | Événement, contenu fourni |
| 7 | Retouche du brief 1 (« plus chaleureux ») | `ITER` | Reprise d’une direction existante |
| 8 | Bouton partagé d’un système de design | `SYSTÈME` | Composant, tokens, états |

## 3. Conditions

- **A — avec le système** : la skill installée, le journal de mobilisation activé (`DG_JOURNAL`).
- **B — sans le système** : même modèle, mêmes outils (navigateur compris), même brief, sans la skill.
- Même budget de temps ou de tours par run. L’ordre des conditions est tiré au sort pour chaque brief.
- Un run par brief et par condition (décision du 2026-10-23) : la variance d’un même agent n’est pas mesurée, ce qui est une limite déclarée.

## 4. Jugement

- **Évaluateurs** : la personne qui pilote le système (non indépendante : `author`) et un agent juge d’une autre instance (`agent`), qui ne connaît ni la condition ni le système. Aucun designer humain indépendant n’est disponible : c’est une limite déclarée. Leur rôle et leur indépendance vont dans `evaluator`.
- **À l’aveugle** : les rendus sont anonymisés avant le jugement (trace retirée, noms de fichiers neutres, ordre de présentation tiré au sort).
- **Grille** : les six questions de la revue créative du noyau (présent, spécifique, culturellement transformé, encore générique, manque de résolution, intervention la plus utile). Pour chaque paire A/B et chaque question : préférence A, B ou égalité, avec une phrase de justification ; puis une préférence d’ensemble.
- **Mesures objectives, par run** : nombre de `RETURN` et de réserves de `check_render.py` sur le rendu final ; preuves `NOT-VERIFIED` à la sortie ; temps jusqu’au premier rendu jugeable ; nombre de passes de correction qui ont réellement changé l’artefact (mesure expérimentale de `ACTION/CLOSE-EXIT-CHECK`).

## 5. Mobilisation (A2)

Avant de voir le journal, une personne relève pour chaque brief les signaux que la table des signaux du noyau associe à une route (brief vague, typographie ouverte, sujet réel et idée ouverte, risque critique…). On compare ensuite avec la fiche de mobilisation du run A (`journal_mobilisation.py`) : pour chaque signal, lu, proposé non lu, ou manqué. Résultat : un taux de signaux manqués par signal, sur l’ensemble des runs A.

## 6. Convergence (A18)

Pour chaque run, relever les six champs de « Réutilisation située » : teinte dominante, paire typographique, ossature, objet de preuve, thèse, registre. On compte les répétitions entre briefs, dans chaque condition.

## 7. Statuts (A16)

Relever dans les traces des runs A les jetons de statut employés (issue, verdict, statut de direction) et leurs homonymes, pour décider ensuite s’il faut les fusionner.

## 8. Enregistrement

- Un contrat `EVALUATION_CASE` par run, avec `condition`, `campaign` (identifiant commun, ce protocole, `paired_case` vers le run de l’autre condition) et `evaluator`.
- Un gain ne s’écrit dans `gain_claims` qu’avec sa référence (le cas apparié) et sa limite ; le validateur refuse un gain sans référence.
- Un tableau de résultats par question, avec le point de départ (condition B), l’observation et la limite (contrat de gain réel, `BIBLIOTHEQUE/EVOLUTION`).

## 9. Règles de décision, fixées avant les runs

- Un gain est affirmé pour une question seulement si la condition A est préférée sur au moins six paires sur huit par chacun des évaluateurs, sans dégradation des mesures objectives.
- Moins que cela : « pas de différence observée » ou `NOT-VERIFIED`, jamais un gain.
- Une dégradation dans la condition A (préférence B majoritaire, plus de `RETURN`, plus de temps sans gain) est rapportée comme telle et ouvre une action.
- Les méthodes à l’essai (`PILOT`) ne passent en `ADOPTED` que sur un gain observé ici.

## 10. Décisions du 2026-10-23

- Les runs sont faits par des agents Sonnet 5.5, effort moyen, lancés depuis la session de maintenance ; un run par brief et par condition.
- Juges : la personne qui pilote le système et un agent juge (Sonnet 5.5), à l’aveugle.
- Pas de limite de temps ni de jetons ; les deux sont relevés par run pour estimer les coûts.
- Briefs fixés dans `briefs.md` ; consignes des conditions dans `consignes-A.md` et `consignes-B.md`.
