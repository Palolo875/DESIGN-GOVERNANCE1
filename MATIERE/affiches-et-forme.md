# Matière à enrichir — affiches de référence et forme de page (2026-10-08)

Statut : matière gardée en tête, pas encore une correction. À transformer en **opérations** (savoir), jamais en exemples à copier (règle 9).

## Affiches partagées par le propriétaire (5)

rétro (collines devant le mot), BORING (figure devant le mot), Fieldtrip (formulaire administratif comme décor), warmth (image dans les lettres), main et curseur (collision pixel / fresque).

Constat commun : une seule opération visuelle, poussée à fond, dans un grand champ calme.

Manques repérés dans le système :
1. TXI-01 traite le texte sur image seulement de façon défensive ; rien sur le mot et l'image dans le même plan (figure devant, image dans la lettre, mot comme horizon).
2. Rien sur le rapport d'échelle et le champ calme majoritaire autour d'une seule opération.
3. Rien sur l'idée par collision ou contresens de registres.

Mises en garde : c'est aussi une vague (grain, fausses métadonnées, code-barres, ✦) à nommer comme MODAL ; les fausses métadonnées sont de la fiction assumée sur une affiche, de fausses preuves sur une page produit.

## Forme de page (discussion)

Constat U3/U5 : les pages rompent la trame modale au premier écran, puis le bas retombe dans le gabarit (sections de même poids, titre à gauche et texte à droite, tarifs, FAQ, CTA). Le propriétaire juge tout le défilement : rythme, cartes, pied de page.

Manques repérés : aucune occurrence de « pied de page », « fin de page » ou « séquence de sections » dans les sources ; le test de trame (TRM-01) est lu comme un test de premier écran. La N-convergence crème + serif correspond déjà au marqueur « vague 2 » de SAVOIR/TOOLS/CONVERGENCE, que le chemin par défaut n'ouvre pas toujours.

## Lecture structurelle des affiches (côté BIBLIOTHEQUE)

Une affiche est un champ unique et fixe ; une page web est une séquence qui défile. Ce qui se transpose : le premier écran, un « moment affiche » en cours de page, les transitions entre sections et la fin. Ce qui ne se transpose pas : la lecture d'un seul coup d'œil de toute la surface.

| Opération de structure | Où on la voit | Couverture actuelle | Transposition web |
|---|---|---|---|
| Bandes de cadrage haut et bas : une bande d'informations en haut, un colophon en bas, un champ libre entre les deux | rétro (métadonnées en 5 colonnes ; n°, devise, code-barres) ; Fieldtrip (bande de formulaire) | Partielle : `MODIFIER/NAVIGATION_SHELL`, `SUPPORT/ARCHITECTED_FRAME` ; rien sur la bande basse | Navigation comme bande typographique ; pied de page comme colophon qui referme |
| Ancrage aux coins : de petits éléments aux coins tiennent un grand vide sans boîte | BORING (4 coins), warmth, rétro (étoiles) | Absente | Structure sans cartes : repères en périphérie, champ central libre |
| Franchissement de cadre : un élément chevauche deux zones | warmth (mot à cheval sur le bord de la photo) ; rétro et BORING (le paysage ou la figure coupe le mot) | Absente (aucune occurrence de chevauchement ou de franchissement) | Un élément qui traverse la frontière entre deux sections, au lieu de sections-boîtes fermées |
| Plans superposés comme structure | rétro, BORING, warmth | Partielle : « relations de plans » dans `DIRECTION/VISUAL_TARGET`, sans route de structure | Profondeur entre titre, objet et fond, avec ses risques (lecture, recadrage mobile) |
| Champ libre et petit objet : échelle disjointe | rétro (bus minuscule), main et curseur | Couverte : `SUPPORT/FREE_FIELD`, `SCENE/EDITORIAL_FIELD` | Moment affiche |
| Le document vernaculaire comme gabarit : formulaire, ticket, carnet ou fiche structure la page | Fieldtrip (autorisation de sortie) | Absente en structure (« vernaculaire » n'existe que pour la typo et le style) ; N4 l'a trouvé seul (le carnet à souche) | Facturation : la facture ou le carnet ; natation : fiche d'inscription, carnet de progrès, planning du bassin |

Limites : six opérations tirées de cinq images ; à transformer en opérations avec conditions, contre-indications et preuve, comme les routes existantes, jamais en catalogue d'exemples.

## Constat outil incident

`read_route.py --trouver ... | head` lève un BrokenPipeError (trace Python) quand la sortie est coupée. Les agents utilisent `| head` : à corriger (sortie silencieuse sur tube fermé).
