# Consigne commune — fiche d'audit (phase 1)

Tu audites un ou plusieurs fichiers du système Design Governance, un cadre français de gouvernance du design packagé en skill d'agent. **Tu ne modifies rien dans `/home/user/DESIGN-GOVERNANCE1`** : lecture seule. Tu écris seulement ta fiche, à l'emplacement indiqué.

## À lire d'abord

1. **La charte :** `/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/wt-refonte/PLAN/charte.md`.
2. **Les grilles :** `.../wt-refonte/PLAN/grilles.md`, même dossier. La grille d'un fichier est F1 à F13.
3. **Les mesures automatiques :** `.../wt-refonte/AUDIT2/donnees/mesures.md`, avec le détail dans `mesures.json`. Utilise-les ; ne les recalcule pas.

## Le but

Le propriétaire veut rendre le système pro, propre, clair et beau. Le design doit être au cœur ; la gouvernance aide ou renforce. Le système doit servir quatre publics : débutant, designer, équipe, agent.

Cette fiche sert à décider, fichier par fichier et section par section : garder, déplacer, fusionner, réécrire ou retirer. **Rien ne doit se perdre sans décision.**

## Règles

- **Lis le fichier en entier, sans extrait.** S'il est long, lis-le en plusieurs morceaux, mais lis tout.
- **Chaque constat cite sa preuve :** `fichier:ligne`, et une courte citation si utile. N'invente rien. Si tu n'es pas sûr, écris « à vérifier ».
- **Juge selon la charte et la grille**, pas selon tes goûts. Une disposition proposée n'est qu'une proposition.
- **Distingue le fond de la forme.**
  - *Le fond* : ce que le texte enseigne ou exige. Il n'est pas à changer pendant le rangement.
  - *La forme* : place, structure, langue, répétition.
- **Classe chaque section dans une famille :**
  - *design* : direction, savoir, formes ;
  - *produit* : qualité du rendu réel, UI/UX, accessibilité, vérification visuelle ;
  - *gouvernance* : runs, gates, traces, clôture, statuts, schémas ;
  - *méta* : comment lire, maintenir ou versionner le système.
- **Sois concis.** Une ligne par constat ; le détail seulement là où il y a un défaut.

## Format de la fiche (Markdown, en français)

```
# Fiche — <fichier(s)>

## Identité
Rôle actuel (2 phrases au plus) · public réel · public visé par la charte · taille et principales mesures (reprises de mesures.md).

## Verdicts de la grille
Table : critère (F1, F2, F3, F4, F5, F8, F9, F10, F11) | verdict (conforme / à corriger / bloquant) | preuve.

## Sections
Table, une ligne par section de niveau 2 ou de route :
section (ligne) | ce qu'elle apporte (1 phrase) | famille | public | observation principale | disposition proposée.
Dispositions : garder ; déplacer vers … ; fusionner avec … ; réécrire (forme) ; scinder ; retirer (raison).

## Défauts
Table : n° | type (structure, langue, répétition, obsolète, risque, visuel, coût de lecture, convergence) | gravité (bloquant, important, mineur) | preuve | proposition.

## Savoir à protéger
Liste des unités de savoir ou des règles importantes de ce fichier, une par ligne, avec leur plage de lignes.
C'est le point de départ de la table de correspondance : rien de cette liste ne doit disparaître.

## Ce qui fige ou pousse à la convergence
Exemples, valeurs, gabarits ou réglages par défaut que l'agent risque de recopier, avec la preuve. Si aucun, écris « aucun relevé ».

## Dépendances et risques de déplacement
Ce qui cite ce fichier, ce qu'il cite, et ce qui casserait si on le déplace, notamment les contrôles qui verrouillent ses phrases (voir mesures.json).

## Synthèse
3 à 5 lignes : l'essentiel pour décider.
```

Termine en renvoyant dans ta réponse finale **uniquement** : le chemin de la fiche écrite, et ta synthèse en 5 lignes au plus.
