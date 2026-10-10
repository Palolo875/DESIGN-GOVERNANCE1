# Cartes du système

Trois vues pour comprendre Design Governance V1 expérimentale. Elles orientent vers les sections propriétaires, qui font foi ; elles ne créent aucune règle ni nouvelle route pour l’agent.

| Vue | Page consultable | SVG | Équivalent écrit |
|---|---|---|---|
| Responsabilités et entrées | [Carte du système](index.html) | [Clair](systeme-clair.svg) · [Sombre](systeme-sombre.svg) | [Lire](systeme.md) |
| De la demande à la sortie | [Parcours d’un travail](parcours.html) | [Clair](parcours-clair.svg) · [Sombre](parcours-sombre.svg) | [Lire](parcours.md) |
| Observer, modifier et décider | [Créer puis apprendre](boucle.html) | [Clair](boucle-clair.svg) · [Sombre](boucle-sombre.svg) | [Lire](boucle.md) |

Chaque page garde le contexte lorsque vous choisissez un public ou une étape. Sur petit écran, les responsabilités se recomposent en texte lisible. Le thème clair/sombre et l’export de la sélection demandent JavaScript ; les cartes, textes et liens restent disponibles sans script. Les SVG embarquent Manrope sous licence OFL et gardent du texte sélectionnable.

## Reprendre les supports

Le contenu vient de trois fichiers JSON, un par carte ; la palette commune est déclarée avec la carte du système. Le générateur et son gabarit produisent les pages, les deux variantes SVG et les équivalents écrits. Aucun contenu normatif n’est copié dans une nouvelle source d’autorité.

Depuis la racine du paquet :

```sh
python3 supports/generer.py
python3 scripts/validate_supports.py
```

Le contrôle refuse une sortie périmée ou une cible absente. Il ne juge ni la lisibilité du rendu ni la compréhension par une personne. La validation visuelle, ses captures et l’historique de fabrication restent dans les travaux de la branche `refonte`, séparés du paquet produit.

Le langage documentaire retenu sert ces supports. Il n’impose ni Manrope, ni ces couleurs, ni une structure aux productions que le système aide à créer. La V1 reste expérimentale.
