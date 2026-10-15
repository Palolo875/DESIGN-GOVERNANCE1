# Savoir — typographie

Choisir et régler la typographie, y compris pour les données.

<!-- origine:SAVOIR.md -->
# SAVOIR/TYPE — typographie et données

<!-- noyau:début COMP-TYPO -->
[REQUIS PAR LE MODULE — lecture, ton, données, hiérarchie ou surface identitaire] Choisis une typographie pour ses langues, chiffres, ponctuation, graisses, lisibilité, licence, performance, fallback et ton.
<!-- noyau:fin COMP-TYPO -->

Une famille fréquente n’est pas un problème en soi. Le problème est le réflexe sans alternative comparée, système existant interrogé ou raison formulée.

Une ou deux voix expressives peuvent souvent suffire, mais cette heuristique reste `[À ADAPTER]`. Une famille mono-fonctionnelle pour données, version ou métadonnées ne constitue pas nécessairement une voix supplémentaire.

Hiérarchie, longueur de ligne, interligne, figures tabulaires, fallback et chargement font partie de la décision.

Une police variable peut devenir un système adaptatif : poids pour hiérarchie, largeur pour densité justifiée, taille optique pour rendu à l’échelle et grade lorsqu’il existe. N’utilise que les axes présents dans la famille livrée. Préfère les propriétés typographiques de haut niveau et évite les styles synthétiques non déclarés.

Une signature typographique ne tient pas si zoom, reflow, locale ou ajustement d’espacement la transforment en défaut de lecture.

<!-- noyau:début COMP-TITRE -->
<!-- concept:TIT-01 -->
**Équilibre d’un titre.** Quand un titre porte la scène (grand titre, accroche, chiffre mis en avant), règle-le sur le vrai texte, puis corrige ce que la capture montre. D’abord le sens : une coupe de ligne ne doit pas le casser, et un mot isolé en dernière ligne doit être voulu. Ensuite la forme : des lignes trop inégales gênent la lecture du bloc (`text-wrap: balance` peut aider si la cible le permet), et une approche trop lâche aux grandes tailles se resserre si la police le demande. Enfin la hiérarchie : si elle est aplatie, rétablis-la par l’écart d’échelle entre le titre et le texte qui suit, ou par le poids, la position ou l’espace. Un mot isolé, un déséquilibre ou un faible écart peut être le choix de composition : on le garde si la capture montre qu’il fonctionne. Observe sur capture, en desktop et en mobile, avec le contenu réel : la forme du bloc de titre reste lisible au flou.
<!-- noyau:fin COMP-TITRE -->

**Longueur d’un titre.** Budget de longueur et formes d’un titre : `SAVOIR/CRAFT/CFT-06`.

**Réglage d’un grand texte.** `[À ADAPTER]` Points de départ, **non des mesures**, à essayer sur la police livrée et le vrai texte. Plus un texte grandit, plus il se resserre : au-delà d’environ 40 px, rapproche l’interligne de 1,0 (moins pour des capitales ou une police condensée) et rends l’approche légèrement négative, réglée par palier de taille, car une approche juste en très grand corps étouffe un titre moyen. Surveille les collisions entre jambages et accents d’une ligne à l’autre. Les capitales demandent au contraire une approche un peu ouverte. Une lettre ronde ou oblique en début de ligne peut demander un léger retrait optique pour paraître alignée. Pas de césure dans un titre ; laisse plus d’espace au-dessus d’un titre qu’en dessous, pour qu’il appartienne à ce qu’il annonce. Une ombre, un contour ou un dégradé sur un grand texte se juge par retrait (que perd le titre sans eux ?), non par interdit. Contre-indications : police déjà réglée pour l’affichage, écriture non latine ou à ligatures, marque qui impose ses valeurs, texte long. Preuve : capture à 390 et 1440 px sur le vrai titre (`COMP-TITRE`).

### Preuve typographique

La preuve est documentée dans `ACTION/STRUCTURED-PROOF` lorsque la typographie peut changer la décision. Sépare, lorsque nécessaire :

```text
FORM-LEGIBILITY — reconnaissance des formes et caractères.
TEXT-READABILITY — lecture du texte dans son contexte.
HIERARCHY — distinction des rôles et priorités.
PERSONALITY — tonalité ou individuation perçue.
TASK-EFFECT — effet sur compréhension ou action lorsque pertinent.
LIMIT
```

| Preuve | Cas |
|---|---|
| Spécimen de rôle | Display, corps, interface, données et légale sur contenu réel. |
| Résilience | Texte long, locale, chiffres, zoom, ajustement d’espacement, reflow, petit corps, fallback et caractère absent. |
| Rendu | Couple taille/interligne/mesure et axe variable si pertinent. |
| Décision | Voix, lisibilité ou densité réellement améliorées ; contre-indication déclarée. |

Une famille n’est jamais déclarée supérieure sur la seule base d’une impression de marque. Lorsque U est dominant, l’effet sur la tâche est prouvé par ACTION, pas inféré de la typographie seule.

---
