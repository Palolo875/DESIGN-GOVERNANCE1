# Cartes du système

Trois vues pour comprendre Design Governance. Elles orientent vers les sections propriétaires, qui font foi ; elles ne créent aucune règle ni nouvelle route pour l’agent.

| Vue | Lecture sur GitHub | SVG | Page interactive à ouvrir après extraction |
|---|---|---|---|
| Responsabilités et entrées | [Carte du système](systeme.md) | [Clair](systeme-clair.svg) · [Sombre](systeme-sombre.svg) | [HTML](index.html) |
| De la demande à la sortie | [Parcours d’un travail](parcours.md) | [Clair](parcours-clair.svg) · [Sombre](parcours-sombre.svg) | [HTML](parcours.html) |
| Observer, modifier et décider | [Créer puis apprendre](boucle.md) | [Clair](boucle-clair.svg) · [Sombre](boucle-sombre.svg) | [HTML](boucle.html) |

Sur GitHub, les textes Markdown sont directement lisibles ; les liens HTML ouvrent le code source. Les pages interactives se consultent après extraction du paquet. Chaque page garde le contexte lorsque vous choisissez un public ou une étape. Sur petit écran, les responsabilités se recomposent en texte lisible. Le thème clair/sombre et l’export de la sélection demandent JavaScript ; les cartes, textes et liens restent disponibles sans script. Les SVG embarquent une version WOFF2 de Manrope réduite aux caractères des supports, sous licence OFL, et gardent du texte sélectionnable. Les images des documents choisissent leur variante selon le thème clair ou sombre du lecteur.

## Reprendre les supports

Le contenu vient de trois fichiers JSON, un par carte ; la palette commune est déclarée avec la carte du système. Le générateur et son gabarit produisent les pages, les deux variantes SVG et les équivalents écrits. Aucun contenu normatif n’est copié dans une nouvelle source d’autorité.

Depuis la racine du paquet :

```sh
python3 supports/generer.py
python3 scripts/validate_supports.py
```

Si le contenu ou le gabarit change, préparer d’abord la police dans un environnement de fabrication :

```sh
python3 -m pip install -r supports/fonts/requirements.txt
python3 supports/preparer_police.py
python3 supports/generer.py
python3 supports/preparer_police.py --check
```

La police source, la licence, les versions des outils et le relevé de couverture restent livrés. Le contrôle courant utilise la bibliothèque standard Python : il vérifie couverture, empreintes, sorties et poids sans installer les outils de police. Les budgets techniques sont de 50 000 octets par SVG et 100 000 par page HTML ; ils empêchent le retour de la police complète dans chaque support.

Le contrôle refuse une sortie périmée ou une cible absente. Il ne juge ni la lisibilité du rendu ni la compréhension par une personne.

Le langage documentaire retenu sert ces supports. Il n’impose ni Manrope, ni ces couleurs, ni une structure aux productions que le système aide à créer.
