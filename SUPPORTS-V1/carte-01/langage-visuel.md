# Langage visuel proposé pour les supports

V1 expérimentale. Ce langage concerne les cartes et documents du système. Il n’impose pas de style aux productions des agents.

## Composition

Un domaine Design plus large rassemble les quatre matières. Guides et agent sont des accès ; la gouvernance protège risque, preuve et reprise ; la maintenance entretient l’ensemble. Les flèches nomment des relations, pas une séquence imposée.

Bordures fines, plans plats, espaces par responsabilité. Les noms et les fonctions distinguent les parties, en complément de leur couleur. Le petit écran recompose les responsabilités en texte lisible.

## Typographie

Manrope sert les titres, labels et descriptions. Les SVG conservent du texte sélectionnable et la fonte embarquée, avec sa licence. Une comparaison du titre avec Instrument Serif est conservée dans les captures ; le choix de la voix reste une proposition à discuter.

SVG : titre 32, rôle 14, domaine 26, matière 22, description 18, métadonnée 14 pixels à la taille native 1104 × 920. La page recompose ces rôles selon le viewport ; les contrôles natifs gardent un focus visible.

## Couleurs par rôle

| Rôle | Clair | Sombre |
|---|---|---|
| Fond | `#f4f5f1` | `#142428` |
| Surface de lecture | `#ffffff` | `#203439` |
| Texte principal | `#192f34` | `#f4f5ef` |
| Texte secondaire | `#4b6268` | `#bbcace` |
| Frontières et relations | `#5b7076` | `#93a9b0` |
| Mise en évidence | `#254eab` | `#acc8ff` |
| Guides | `#edf3e9` | `#23382e` |
| Agent | `#eaf0fb` | `#22364b` |
| Design | `#ffffff` | `#203439` |
| Gouvernance | `#f7efe1` | `#413525` |
| Maintenance | `#edf0f4` | `#29343e` |
| Focus | `#254eab` | `#acc8ff` |

## Construction et preuve

`carte.json` possède le contenu, les relations et les couleurs. `construire.py` génère page, SVG, équivalent textuel, Mermaid et cette fiche. Une modification partagée se fait dans cette source puis se régénère. Les résultats observés sont conservés dans `preuves/verification.json`, avec l’empreinte du HTML et le scope.
