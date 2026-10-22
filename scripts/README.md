# Outils du paquet

Ce dossier contient les scripts qui lisent le système, observent un rendu et contrôlent la cohérence du paquet. Les commandes s’exécutent depuis la racine du paquet ; leur mode d’emploi complet est dans [la validation](../maintenance/README.md#validation).

| Script | Rôle |
|---|---|
| `read_route.py` | Lecteur de routes : sert une section par son locator ou son adresse lisible, la ligne d’un mode et son tronc (`--mode`, `--tronc`), les cartes de moment (`--moment` avant, regard ou sortie), une recherche (`--trouver`) et les connexions situées. |
| `check_render.py` | Recette de rendu dans un navigateur : fautes objectivables d’une page HTML aux largeurs courantes. Son périmètre et ses limites sont décrits dans `produit/plancher#recette` (`ACTION/RECETTE-RENDU`). |
| `check_caractere.py` | Recette de caractère : confronte le caractère déclaré d’un run à son rendu (polices, densité, matière ; foyer, intensité et vide en relevé). Méthode et limites : `produit/preuve-visuelle#caractere` (`ACTION/RECETTE-CARACTERE`). |
| `journal_mobilisation.py` | Journal de mobilisation, passif : avec la variable `DG_JOURNAL=chemin.jsonl`, le lecteur de routes, les deux recettes et les outils du regard notent ce qu’ils ont servi (routes lues ou proposées, résultats, code de sortie) ; sans elle, rien n’est écrit. `python3 scripts/journal_mobilisation.py chemin.jsonl` en tire une fiche de mobilisation dont la conséquence et la preuve restent à établir. |
| `gestes.py` | Gestes servis par les recettes : sous les signaux de `check_render.py` et `check_caractere.py`, la ligne liée du tableau des gestes de `SAVOIR/STATE`, lue dans sa source (trois au maximum ; rappel seulement si déjà servie dans le journal). `python3 scripts/gestes.py` liste les termes ; `--sans-gestes` les retire d’une recette. |
| `registre_choix.py` | Registre des choix : relève sur le rendu la police du titre, les fichiers de police réellement rendus, le fond et l’accent, les compare aux runs précédents d’un registre local choisi (`--registre` ou `DG_REGISTRE`), puis ajoute l’entrée ; `--lire` en donne la synthèse. Rien n’est écrit sans registre. |
| `specimen.py` | Spécimen de voix : compose le vrai titre dans plusieurs polices à 390 et 1440 px, écrit la page et les captures, signale une police de repli. Ne choisit rien. |
| `planche.py` | Planche de regard humain : captures, défaut dominant restant, gestes essayés et questions, avec un champ « ce que je changerais d’abord » ; méthode dans `DIRECTION/DOUBLE-LOOP`. |
| `build_core.py` | Compile le noyau de la skill dans `SKILL.md` et les bandeaux de tête de `sections/` depuis le registre `LIEUX` ; `--check` vérifie sans écrire. |
| `validate_all.py` | Lance l’ensemble des contrôles ci-dessous. |
| `validate_design_governance.py`, `validate_structure.py`, `validate_reading_map.py`, `validate_supports.py` | Inventaire, liens et références, structure et chargement, carte de lecture, fraîcheur des cartes. |
| `test_read_route.py`, `test_core_budget.py`, `test_audit_regressions.py`, `test_check_render.py`, `test_check_caractere.py`, `test_journal_mobilisation.py`, `test_gestes.py`, `test_outils_regard.py` | Tests du lecteur, du budget du noyau, des régressions de navigation, de la recette de rendu, de la recette de caractère, du journal de mobilisation, des gestes servis et des outils du regard (registre, spécimen, planche, cartes de moment). |
| `package_manifest.json` | Liste des fichiers attendus dans chaque distribution. |

Ces outils attestent la cohérence du paquet et observent des fautes mesurables ; ils ne jugent ni la direction, ni le goût, ni l’usage. La recette de caractère, le journal, les gestes servis et les outils du regard sont à l’essai ; leur statut est tenu dans [la fiche de version](../maintenance/versions.md#sections-à-lessai). Les schémas et validateurs de la fiche de travail sont dans [`gouvernance/`](../gouvernance/README.md).
