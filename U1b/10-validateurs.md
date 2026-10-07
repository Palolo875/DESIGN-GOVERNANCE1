# U1b — Fiche d'inventaire n°10 : les validateurs et les tests

**Base :** commit `d90869c`.

**Lecture intégrale :** les 13 fichiers, soit 5 377 lignes et 310 Ko : `validate_all.py`, `validate_design_governance.py`, `validate_run_card.py`, `validate_contracts.py`, `validate_reading_map.py`, `validate_structure.py`, les cinq `test_*.py`, `build_distributions.sh` et `package_manifest.json`. Mes notes de lecture sont dans `U1b/10-notes.md`.

**Exécuté :**
- chaque suite séparément, pour compter ses cas ;
- `validate_all.py` complet : **succès en 125 s**, dépôt resté propre ;
- deux tests de limite, T-22 et T-23, dans `U1b/preuves/`.

**Angle :** ce que le système sait **contrôler automatiquement**, ce qu'il protège ainsi, et ce que ces protections coûtent à chaque changement.

## 1. Identité

| Fichier | Lignes | Rôle |
|---|---|---|
| `validate_all.py` | 190 | Chef d'orchestre : lance tout dans l'ordre, puis construit deux fois les archives et compare leurs empreintes |
| `validate_design_governance.py` | 353 | Intégrité du paquet : inventaire fermé, liens, version, vocabulaire des statuts, positionnement expérimental |
| `validate_run_card.py` | 1 077 | Fiche de run : schéma, environ 45 règles métier, profil strict, suite de cas |
| `validate_contracts.py` | 486 | Cadrage de domaine, recherche et contrats de production |
| `validate_reading_map.py` | 729 | Carte de lecture, locators, connexions et **56 conditions de façade** |
| `validate_structure.py` | 815 | **18 gardes « une chose, un lieu »** : concepts protégés, vocabulaire retiré, fidélité des résumés, noyau, chargement, entrée humaine |
| `test_check_render.py` | 390 | 125 cas : 48 d'interprétation, 51 de JavaScript sur DOM simulés, 26 dans un vrai navigateur sur 19 pages pièges |
| `test_read_route.py` | 317 | 50 cas |
| `test_preparer_livraison.py` | 265 | 20 cas |
| `test_audit_regressions.py` | 210 | 30 cas |
| `test_core_budget.py` | 90 | 10 cas |
| `build_distributions.sh` | 316 | Construit les distributions GitHub et Local : verrou, validation, archives identiques d'un build à l'autre, retour arrière en cas d'échec |
| `package_manifest.json` | 139 | La liste fermée des 69 et 63 fichiers |

Bilan : environ **235 cas de test**, plus environ 150 cas intégrés aux validateurs, plus des centaines de règles textuelles. Aucune dépendance hors de Python standard, sauf Playwright pour la partie navigateur.

## 2. Ce qu'ils possèdent

### Une méthode de test exemplaire

| Pratique | Où | Pourquoi elle compte |
|---|---|---|
| **Une faute par cas, sur une base d'abord vérifiée valide** | `validate_run_card` (87 cas), `validate_contracts` (25 cas) | Chaque règle est prouvée isolément. Un cas qui passerait pour une autre raison est signalé |
| **L'échec doit avoir le bon motif** | `expect_failure`, table des fixtures | Échouer ne suffit pas, il faut échouer pour la raison attendue et sans plantage |
| **Témoins négatifs avant tout succès** | Chargement des schémas | Un schéma vide, ou un mot-clé que le validateur ignorerait, est refusé avant de valider quoi que ce soit |
| **Mutation rouge pour chaque garde** | LCF, régressions d'audit, `check_craft_regressions` | On casse volontairement le texte et on vérifie que la garde le voit |
| **NOT-VERIFIED plutôt qu'un faux succès** | `test_check_render` sans navigateur | Le paquet ne se déclare jamais vérifié sur ce qu'il n'a pas exécuté |
| **Builds reproductibles et transactionnels** | `build_distributions.sh` | Deux builds donnent les mêmes octets ; un échec remet l'état précédent |

### Ce qu'ils contrôlent

| Famille | Contrôles principaux | Lien avec la mission |
|---|---|---|
| **Intégrité du paquet** | Inventaire fermé, liens et ancres, version unique, pas de liens symboliques, distributions identiques | Fiabilité du support |
| **Honnêteté des fiches de run** | Un résultat accepté exige une observation, une provenance, une limite et des réserves datées ; une direction perdue ne peut pas être acceptée ; un risque critique exige sa protection ; un droit inconnu interdit l'acceptation en DIRECTION | **Rend impossible de déclarer « accepté » sans dire ce qui a été vu**. C'est formel seulement (C11, T-18 à T-20) |
| **Cohérence des copies** | 56 conditions de façade et 65 règles de fidélité : chaque copie d'une règle (guides, glossaire, noyau, exemples) garde sa condition | Empêche qu'un guide dise autre chose que la source. Le test U1 l'a montré avec C20 |
| **Une chose, un lieu** | 26 concepts protégés à un seul endroit, 37 formulations retirées interdites, une seule table de chargement, une seule entrée humaine, une seule constitution | Lutte contre la redondance. Elle n'empêche pas les 6 versions du parcours (fiche n°7), qui sont formulées différemment |
| **Le noyau** | Compilé à l'identique, sous 46 000 octets, et 11 phrases qui doivent y rester (dont « Conçois une palette par rôles », « Choisis une typographie pour ses langues ») | Garantit le plancher de savoir de l'agent |
| **La recette de rendu** | 125 cas, dont 19 pages pièges (contraste oklch, focus invisible, cible trop petite, modale, texte SVG, objet de preuve transparent…) | Prouve que `check_render` dit vrai sur des cas connus |

### Ce qu'ils protègent du design (le texte, pas le résultat)

| Garde | Ce qu'elle impose |
|---|---|
| **LCF-46 : marqueurs de tendance** | 18 marqueurs de « vague » (hero SaaS, gradient décoratif, violet, Inter, halos, beige, crème, serif italique, orange rouille, bandeau défilant, illustration peinte, tramage, dithering, logos pixel, ASCII, hachures de plan, bleu Klein, paysage peint) ne peuvent apparaître **que sur une ligne datée `[VEILLE 20xx]`**. Seule exception : un halo de détourage, qui est un défaut de production |
| **UNI-01 : pas de style universel** | Refuse « toujours » ou « à tous les » associé à « un seul traitement » ou « une seule famille ». Protège la diversité |
| **Concepts HON-01, HON-02, EXD-01** | Vérité de scène, aucun faux asset, données d'exemple cohérentes : chacun défini à un seul endroit |
| **Concepts TIT-01, TXI-01, PRC-01, RCV-01, FIN-01, TRM-01** | Équilibre d'un titre, texte sur image, tests perceptifs, récupération après erreur, activation du craft, test de trame : présents et atteignables en un saut depuis leur route |
| **LCF-15, 16, 30 et 47** | Les 8 dimensions du premier objet sont identiques dans DIRECTION et QUICKSTART ; l'objet de preuve est « de préférence codé » |

## 3. Ce qu'ils ne font pas

1. **Aucun contrôle d'une réalisation.** Aucun validateur ne regarde un rendu de design réel. Les seules pages ouvertes sont les 19 pages pièges de `test_check_render`. Le paquet vérifie son **texte** et ses **outils**, jamais ce qu'un agent produit avec eux.
2. **La substance n'est pas contrôlée.** Des champs remplis de « ok » passent (C11, T-18 à T-20). C'est une limite déclarée (RELEASE_NOTES l. 121-132).
3. **Les captures avant/après ne sont jamais vérifiées.** Testé (T-22) : le profil strict accepte une RUN_CARD dont la paire B1b pointe vers `captures/premiere-scene-v1.png` et `…-sans-objet.png`, **qui n'existent pas**. Le profil strict ne vérifie l'existence que de l'artefact et de la trace. La seule preuve visuelle structurée du système n'est donc contrôlée ni sur son existence ni sur sa nature. `validate_all` passe d'ailleurs déjà ce cas à chaque exécution, avec l'exemple officiel.
4. **`evaluation_case` n'a aucun contrôle sémantique.** Seul le schéma s'applique, alors que c'est le contrat qui servirait à mesurer le système.
5. **La CI ne lance pas le navigateur.** Les 26 cas de la partie B y restent NOT-VERIFIED (fiche n°9).
6. **L'absence de synonymes est figée par un test** (`test_no_semantic_match`). Une recherche par sens obligerait à modifier ce test. C'est un choix assumé, pas un oubli.
7. **Un angle mort de C10, précisé.** Le test de restauration refuse un lien symbolique qui pointe vers un autre fichier de l'inventaire ou hors de la destination. Il ne couvre pas le lien vers un fichier interne hors inventaire (T-02), le dossier lié (T-03) ni l'écrasement d'un fichier différent (T-01). C'est exactement ce que U1 a trouvé. J'ai vérifié qu'il s'agit du même script : `RESTORE` est identique, à l'octet près, à celui testé en U1.

## 4. Le coût d'un changement

C'est le point qui compte le plus pour la suite du plan. Une partie des protections porte sur des **formulations exactes** :

| Verrou | Nombre | Exemple |
|---|---|---|
| Conditions de façade (LCF) | 56 | « au plus trois » demandes, « cinq paquets », « sept champs », ordre VISUAL_TARGET → FIRST-OBJECT dans 4 fichiers |
| Règles de fidélité (un mot déclencheur exige sa condition dans le même paragraphe) | 65 | « checkpoint » exige « irréversible ou coûteuse » |
| Formulations retirées | 37 | « anti-direction », « Démarrage en 90 secondes » |
| Phrases exactes | environ 40 | READING_MAP : 15 titres ; noyau : 11 phrases ; README officiel, ACTION, BIBLIOTHEQUE : plusieurs phrases fixes ; 4 questions de « Commencer » |
| Lignes de tableau imposées | 10 | GLOSSAIRE « Mode », DIRECTION « STANDARD »… |
| Marqueurs de tendance | 18 mots | Testé (T-23) : ajouter « Titre en Inter 600, accent violet sur le bouton. » à `examples.md` fait échouer LCF-46 |

**Ce que cela implique.**
- **Avantage.** Une règle ne peut pas diverger en silence entre la source et ses copies. Les révisions passées en ont profité, et le test de U1 l'a confirmé (la garde FIDÉLITÉ a bloqué un changement non propagé).
- **Coût.**
  - Simplifier, fusionner ou reformuler un guide (U3, U4) oblige souvent à modifier aussi la garde correspondante. La règle du validateur l'exige : « une entrée n'entre que par une décision écrite, avec sa mutation rouge ».
  - Un exemple réaliste qui nomme la police Inter ou une couleur violette est refusé, sauf sur une ligne datée.
  - La liste des scripts est tenue à la main en trois endroits : le manifeste, la copie GitHub et la copie Local.
  - Il existe deux implémentations distinctes du sous-ensemble de JSON Schema (RUN_CARD et contrats), avec des mots-clés différents.
  - Une validation complète prend environ 2 minutes.
- **La limite déclarée par le validateur lui-même :** « une contradiction nouvelle hors de la LCF n'est pas détectée ».

## 5. Potentiel présent mais peu exploité

| Élément | Pourquoi il compte au regard de la mission | Usage actuel |
|---|---|---|
| **La méthode « une faute par cas »** | Elle permettrait de tester n'importe quelle nouvelle règle de façon fiable | Limitée aux fiches JSON |
| **Le mécanisme des conditions de façade** | C'est la façon déjà en place de protéger une règle et toutes ses copies | 56 conditions sur des formulations, aucune sur une réalisation |
| **L'infrastructure de `test_check_render`** (serveur local, pages, navigateur) | Elle pourrait accueillir des **pages de référence réelles** (U2) et vérifier qu'une correction ne les dégrade pas | 19 pages pièges d'une ligne chacune |
| **La liste des 18 marqueurs de tendance** | Un catalogue anti-banalité daté, directement utile à la distinction | Sert seulement à interdire ces mots hors de SAVOIR |
| **Le profil strict** | Il vérifie déjà l'existence d'un fichier local | Pas étendu aux captures B1b |

## 6. Observations à verser au registre

| Observation | Preuve | Lien |
|---|---|---|
| Aucun validateur ne contrôle une réalisation : seules 19 pages pièges sont ouvertes | Lecture des 13 fichiers | Synthèse finale ; U2 |
| Le profil strict accepte une paire B1b vers des captures inexistantes | **T-22** ; `validate_run_card.py` l. 589-640 | **Nouveau** ; proche de C11 |
| `evaluation_case` n'a aucun contrôle sémantique | `validate_contracts.py` (aucune fonction dédiée) | Fiche n°8 |
| Environ 220 verrous textuels (56 LCF, 65 fidélités, 37 retraits, environ 40 phrases exactes, 10 lignes, 18 marqueurs) : tout changement de texte doit les traiter | Comptage ; **T-23** | **À intégrer au plan** (U3, U4) : prévoir pour chaque lot la mise à jour des gardes |
| LCF-46 interdit « Inter », « violet », « beige »… hors ligne datée, y compris dans un exemple | T-23 | À prévoir si l'on ajoute des exemples rendus |
| C10 confirmé et précisé : le test de restauration couvre les collisions d'inventaire, pas les liens internes hors inventaire ni l'écrasement | `test_preparer_livraison.py` ; RESTORE identique au script testé en U1 | C10 |
| Deux validateurs JSON distincts ; liste de scripts tenue à trois endroits | `validate_run_card.py`, `validate_contracts.py` ; manifeste et `build_distributions.sh` | Maintenance (basse) |
| Le champ `anti_direction` garde un nom retiré de la doctrine ; il est documenté comme projection de PARTI | DIRECTION l. 205 ; ACTION l. 334 | Mineur |
| `validate_all` complet : 125 s, succès | Exécution | Base de référence pour U8 |

## 7. En une phrase

Les validateurs et les tests sont **la partie la plus rigoureuse du paquet**. Leurs méthodes sont exemplaires et leur honnêteté est constante : jamais de faux succès. Ils garantissent que le **texte** reste cohérent avec lui-même et que les **outils** disent vrai. Mais ils ne regardent **aucune réalisation**, ne vérifient ni la substance des fiches ni l'existence des captures, et ils **verrouillent environ 220 formulations** : chaque simplification du texte devra aussi mettre à jour ces verrous.
