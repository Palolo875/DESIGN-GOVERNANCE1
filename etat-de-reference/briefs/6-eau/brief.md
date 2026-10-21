# Brief 6 — Consommation d'eau de Saint-Aubin

## Demande

La commune de Saint-Aubin veut montrer à ses habitants la consommation d'eau des deux dernières années, par quartier.

Livrable : une page HTML autonome (un fichier, données intégrées ou lues depuis `consommation-eau.csv`).

## Contenu fourni

Les données et la commune sont fictives. Elles sont à utiliser telles quelles.

### La commune

- **Nom :** Saint-Aubin (commune fictive), 10 550 habitants
- **Service :** régie municipale de l'eau ; contact : eau@saint-aubin.example
- **Public :** tous les habitants, y compris des personnes âgées et des lecteurs peu habitués aux graphiques

### Les quartiers

| Quartier | Habitants | Description |
|---|---|---|
| Centre-bourg | 4 180 | Appartements et commerces |
| Les Coteaux | 2 950 | Maisons individuelles avec jardins |
| La Gare | 3 420 | Logements collectifs et petites entreprises |

### Les données

Le fichier `consommation-eau.csv` donne, pour chaque mois d'octobre 2024 à septembre 2026, la consommation moyenne en **litres par habitant et par jour** :
- une colonne par quartier ;
- une colonne pour la moyenne départementale, à titre de comparaison.

### Faits connus, que la commune veut faire comprendre

- **Fuite sur le réseau de La Gare :** de novembre 2025 à février 2026, une fuite sur une canalisation principale a fait monter la consommation mesurée du quartier. Elle a été réparée début mars 2026. Cette eau perdue n'a pas été facturée aux habitants.
- **Arrêté sécheresse :** en juillet et août 2026, l'arrosage des jardins a été limité. La baisse est visible aux Coteaux.
- **Compteurs :** les compteurs ont été remplacés au cours de l'hiver 2025-2026. Une petite partie de la baisse de 2026 peut venir de cette mesure plus précise.
- La commune ne veut **ni culpabiliser un quartier, ni présenter la sécheresse comme un succès**.
