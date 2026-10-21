# Outil de jugement esthétique — plan de suivi

Version 3 · 21-10-2026 · Junior (Kamel). Document de travail, hors paquet : il ne fait pas partie des pages de présentation du système.

## Objectif et périmètre

Comprendre **pourquoi une production réussit ou échoue** : ce que le système mobilise réellement, comment il l'utilise et ce que cela apporte au résultat. La capacité esthétique de Design Governance V1 devient ainsi observable, et elle progresse sur des faits, comme la gouvernance progresse grâce à ses validateurs.

L'évaluation porte sur quatre questions :

1. **Le caractère déclaré est-il perçu ?** Densité, foyer, matière, calme ou tension, comparés à ce que le run a annoncé.
2. **La page est-elle propre à son projet ?** Distance au rendu qu'un agent produirait sans le système, et répétition d'un run à l'autre.
3. **Qu'est-ce qui a été mobilisé, et avec quel effet ?** Connaissances et moyens, du simple accès jusqu'à l'application, avec la conséquence observée.
4. **Qu'est-ce qui aurait dû l'être et ne l'a pas été ?** Route jamais ouverte, déclencheur mal formulé, problème non reconnu, moyen absent ou en échec.

**Dans le périmètre :** le contenu du système, son accès (les routes), son déclenchement, son application, et les **moyens** qui permettent de le concrétiser :
- outils et scripts ;
- références, bibliothèques et composants ;
- polices et images ;
- capacités de construction et d'observation.

Les routes organisent l'accès à ces moyens et aux connaissances ; leur articulation fait partie de l'examen.

**Hors périmètre :** prouver en général que le système fait de meilleures pages ; juger la qualité d'une idée ; remplacer la revue créative (`CFT-00`) ; lire l'attention interne de l'agent.

## Décisions validées

| Décision | Raison |
| --- | --- |
| Comparer le rendu au caractère **déclaré par le run**, jamais à une norme universelle de goût | Des seuils universels pousseraient les pages vers une moyenne |
| L'outil émet des `SIGNAL` et des `RELEVÉ`, jamais PASS ni RETURN | Un vert ne doit pas ressembler à une preuve de qualité |
| Un signal ne bloque rien mais attend une réponse dans la trace : corrigé, ou gardé avec sa raison | Rendre l'écart visible sans retirer le jugement |
| Outil séparé de `check_render.py`, qui reste déterministe sur les fautes | Ne pas mélanger fautes certaines et indicateurs perceptifs |
| Évaluer la **mobilisation réelle**, pas le volume documentaire | Un nombre de caractères ne dit ni si un savoir est concret, ni s'il est compris, lu au bon moment et appliqué |
| Distinguer un **savoir qui développe le jugement** d'une **recette qui oriente les réponses à l'avance** | Le risque de ressemblance vient des recettes (palettes, polices, compositions récurrentes), pas du savoir esthétique en général ; leur effet reste à observer |
| Garder un **socle de discernement** lu à chaque run, puis des approfondissements conditionnels | Une lecture « sur signal » suppose que l'agent reconnaisse déjà le problème qu'elle lui apprend à reconnaître |
| Une répétition peut avoir une fonction | Rappeler une protection juste avant l'action qu'elle encadre |
| Un défaut récurrent ne prouve pas un manque de savoir : diagnostic d'abord | Il peut venir d'un brief ambigu, d'un moyen absent, d'une mauvaise traduction en code ou d'une observation insuffisante |
| **État de référence avant toute réécriture importante** | On ne peut alléger ou renforcer avec discernement sans savoir ce qui sert |
| La recette de caractère mesure la **fidélité à l'intention**, ni le générique ni la qualité | Une page conventionnelle peut respecter sa densité et sa matière déclarées ; une page singulière peut s'en écarter volontairement |
| Bornes figées entre deux recalibrations ; recalibration par lot, sur au moins cinq runs qui n'ont pas servi à les régler | Éviter qu'un outil réglé run après run ne finisse d'accord avec lui-même |
| L'outil vit dans le paquet, en `PILOT` : `scripts/check_caractere.py`, route `ACTION/RECETTE-CARACTERE` | Sa procédure de retrait est écrite ; un nom unique partout |
| La déclaration est un fichier rangé à côté de l'artefact, cité par la trace (ligne « modal, trame et parti ») ; la réponse aux signaux va sur la ligne du défaut dominant | La déclaration voyage avec le run, sans ligne de trace en plus |
| Le tronc `DIRECTION` (98 % de 35 000) ne grossit plus : un ajout s'y compense par un allègement | La hausse de budget ne se répète pas |
| Juge par modèle seulement en avis : par paires, à l'aveugle, ordre inversé | Biais de préférence et justifications peu fidèles |
| Le périmètre inclut la BIBLIOTHEQUE et toutes les parties qui portent la capacité esthétique | La structure fait partie du jugement esthétique |

## Niveaux de mobilisation

Chaque niveau raconte une chose différente ; on note le plus haut atteint, avec sa preuve.

| Objet | Niveaux | Ce qu'on observe |
| --- | --- | --- |
| **Connaissance (route)** | Présente dans le contexte (noyau, tronc) → consultée explicitement → appliquée → effet visible | Lecture dans le journal des routes ; décision ou geste correspondant dans la trace et dans l'artefact ; changement sur capture |
| **Outil, script** | Non sollicité → sollicité et en échec → exécuté sans information utile → exécuté avec une information qui change une décision | Appel, code de sortie, sortie lue ; modification qui suit |
| **Ressource, moyen** (police, image, composant, bibliothèque, référence) | Absente → cherchée sans être atteinte → inspectée puis écartée, avec sa raison → intégrée et vue sur capture | Recherche, accès, licence relue ; présence dans l'artefact ; rendu effectif (police réellement rendue, image chargée) |

## Fiche de mobilisation, par production

Pour chaque production observée, on doit pouvoir dire ce qui a été mobilisé, pourquoi, à quel moment et avec quelle conséquence.

| Champ | Contenu |
| --- | --- |
| Élément | Route, outil ou ressource |
| Déclencheur | Ce qui a conduit à le mobiliser : tronc, signal de l'index, demande, défaut observé |
| Moment | Cadrage, premier objet, construction, observation, correction, sortie |
| Niveau atteint | Selon le tableau précédent |
| Conséquence | Choix de composition, correction visible, contrainte protégée, option écartée, limite correctement identifiée, ou aucune |
| Preuve | Lecture journalisée, appel d'outil, différence dans l'artefact, capture avant/après |

**Manques.** La fiche liste aussi ce qui aurait dû être sollicité et ne l'a pas été, avec la cause retenue :
- route jamais ouverte ;
- déclencheur mal formulé ;
- problème non reconnu par l'agent ;
- moyen absent ;
- moyen sollicité mais en échec.

L'utilité ne se réduit pas à un changement esthétique : une contrainte protégée ou une limite bien identifiée sont des conséquences à part entière.

## Du diagnostic à la correction

Chaque cause appelle une correction différente ; ajouter du savoir n'est qu'une réponse parmi d'autres.

| Cause constatée | Correction possible |
| --- | --- |
| Savoir absent, ou trop abstrait pour guider un geste | Le concrétiser ou le compléter, là où il est lu au moment utile |
| Route pertinente jamais ouverte, déclencheur flou | Reformuler le déclencheur, ou l'inscrire dans l'index des signaux |
| Problème non reconnu par l'agent | Renforcer le socle de discernement, ou ajouter une observation (recette, capture) |
| Moyen absent (photographie, police, composant) | Carte des moyens, route de production ; à défaut, limite déclarée |
| Moyen en échec (police non chargée, image bloquée) | Outil ou contrôle de rendu, pas du savoir |
| Bonne intention, mauvaise traduction en code | Craft, exemple, contrôle ciblé |
| Brief ambigu | Cadrage et questions d'entrée |
| Observation insuffisante | Capture, état, recette appropriée |

**Exemple : une typographie qui paraît faible.** Quatre questions avant toute correction :
1. La route typographique a-t-elle été lue ?
2. Plusieurs voix ont-elles réellement été comparées sur le vrai contenu ?
3. La police choisie était-elle accessible ?
4. Le navigateur l'a-t-il effectivement rendue ?

Ajouter du savoir ne résout pas un problème de chargement de police ; changer de police ne résout pas une hiérarchie mal construite.

## Combinaisons, ordre et coût

Une référence peut devenir utile seulement lorsqu'elle est associée à une connaissance de composition et à un moyen de fabrication adapté. À l'inverse, plusieurs routes peuvent :
- répéter les mêmes instructions ;
- créer des tensions entre elles ;
- multiplier les lectures sans améliorer la décision.

On examine donc leur contribution commune, leur ordre et leur coût total : lectures, recherches supplémentaires, reprises. Le gain d'attention d'un texte plus court reste une hypothèse : il peut devenir plus clair, ou trop condensé et demander davantage d'interprétation.

## Analyse des passages

Chaque passage est lu à travers une question : **quelle décision ou quelle erreur influence-t-il, et quand faut-il le lire ?** Cela sépare :
- les contraintes indispensables, lues avant la décision qu'elles protègent ;
- les instructions de fabrication directement utiles ;
- les développements consultables à la demande.

Gate A passe aussi par cette analyse : son rôle protecteur justifie sa présence, sans démontrer que chaque explication doit toujours être lue en entier. Toute réorganisation préserve la lecture des contraintes avant les décisions concernées. Un passage n'est déplacé ou retiré qu'après avoir montré qu'il ne protège ni n'oriente aucune décision observée.

## Limites de méthode

- **Ce qui s'observe :** les lectures, les appels d'outils, les modifications et les rendus.
- **Ce qui ne s'observe pas directement :** l'attention interne de l'agent. Son explication d'un choix est un indice à confronter au travail produit, pas une preuve.
- **Attribuer un gain à une route :** une comparaison contrôlée est parfois nécessaire. On retire ou on déplace le passage, puis on relance les mêmes briefs. Ces ablations coûtent cher ; on les réserve aux passages candidats.
- **Compter des caractères :** cela renseigne sur le volume documentaire, pas sur l'apport.

## Carte de la capacité esthétique

| Rôle | Parties du système | Ce qu'on observe | Fiabilité attendue |
| --- | --- | --- | --- |
| Décider la direction | `DIRECTION/VISUAL_TARGET`, `CREATIVE-BOOT`, `DIRECTION-ATELIER`, `FIRST-OBJECT` | Lecture et application ; caractère déclaré perçu ou non ; dominance de l'objet de preuve ; écart au modal annoncé | Bonne pour la dominance, indicative pour le caractère |
| Structurer | `BIBLIOTHEQUE/TENSION`, `SIGNATURE`, `SELECT`, `SEQUENCE`, routes de forme | Route ouverte ou non ; tension visible ; forme propre ou générique ; données pour le cycle de vie des routes | Bonne pour densité et foyer, indicative pour la signature |
| Savoir fabriquer | `SAVOIR/FRAME`, `TYPE`, `CRAFT` (CFT-00 à 06), `STATE`, `STYLE`, `DESIGN-ATLAS` | Voix comparées, gestes appliqués, effet visible d'un geste ; échelle, rythme, couleur | Bonne pour les relevés, indicative pour l'effet d'un geste |
| Se procurer les moyens | `SAVOIR/SOURCE`, `TOOLS/MOYENS`, routes de production d'asset | Ressource cherchée, atteinte, écartée ou intégrée ; rendu effectif ; plafond atteint face au plafond déclaré | Bonne |
| Éviter le générique | `TOOLS/CONVERGENCE`, `CFT-01`, `REUSE-CHALLENGE` | Répétition entre runs ; marqueurs de vague ; écart à la trame modale (méthode à définir) | Bonne pour la détection, le sens reste humain |
| Observer et corriger | `ACTION/GATE-C`, `ANTI-SLOP`, `VISUAL_PROOF`, `ATELIER-EDITION`, `RECETTE-RENDU`, `RECETTE-CARACTERE` | Outils sollicités, sorties lues, corrections qui suivent | Consommateur des signaux |

Cycle de vie des routes, dans `maintenance/evolution.md` : `SEED`, `PILOT`, `ADOPTED`, `DEPRECATED`, `ABANDONED`. `ADOPTED` exige le contrat de gain réel (`BIBLIOTHEQUE/EVOLUTION`).

## Étapes

| Étape | Livrable | Réussite | Arrêt | Statut |
| --- | --- | --- | --- | --- |
| 1. Vérifier le socle technique | Contrôle déclaration → rendu sur Seuil et sur une page volontairement fautive | Les trois défauts plantés sont détectés, aucun faux signal sur Seuil | Si tout tient : socle minimal confirmé | Fait |
| 2. Prototype des mesures esthétiques | Densité, vide, foyer, matières, colorfulness, chacune avec sa route de savoir | Les mesures séparent Seuil, une version générique et une version dense | Générique et dirigée indistinctes : on n'intègre pas | Fait (avec réserve) |
| 3. Instrumenter la mobilisation | Journal des routes lues (lecteur de routes), des outils appelés et de leur sortie, des ressources cherchées ou intégrées ; fiche de mobilisation remplie à partir de ce journal | Pour une production, on reconstitue ce qui a été mobilisé, pourquoi, quand et avec quelle conséquence, manques compris | Si le journal ne permet pas de reconstituer la fiche : revoir ce qu'il enregistre | Fait : journal et fiche (`R2026-10-21`) éprouvés sur 7 runs réels ; conséquences et manques restent à remplir à la main |
| 4. État de référence | Cinq ou six briefs contrastés (vitrine culturelle, outil métier dense, parcours de formulaire, éditorial, commerce local, tableau de données) ; mêmes modèle, outils et ressources ; sans le système et avec le système actuel ; deux ou trois productions par brief et par condition ; évaluation à l'aveugle par paires ; fiches de mobilisation | Pour chaque production : fidélité à l'intention, qualité de réalisation, spécificité au projet, diversité entre projets, défauts, effort total, et ce qui a été mobilisé ou manqué | Si les productions ne se distinguent pas, on le note : c'est un résultat | En cours : 15 productions sur 24 (briefs 1 à 4), arrêt décidé pour le coût ; évaluation à l'aveugle à faire |
| 5. Méthode du générique | Pistes : écart à la trame `MODAL` déclarée, test « cette page pourrait-elle appartenir à cinquante produits ? », comparaison des six champs `REUSE-CHALLENGE` entre runs | Sépare la version générique (même modèle, même brief, sans le système) d'une version dirigée | Indistinctes : méthode non retenue | À définir |
| 6. Analyse des passages | Classement de chaque passage du noyau, du tronc et des lectures conditionnelles (contrainte, fabrication, à la demande), appuyé sur les étapes 3 et 4 | On sait quelles instructions améliorent les productions, lesquelles protègent une contrainte, lesquelles consomment de la lecture sans apport identifiable | Sans observation : reste en hypothèse | Pas commencé |
| 7. Ajustements ciblés | Conserver, déplacer, renforcer, simplifier ou retirer ; ablations limitées aux passages candidats ; mêmes briefs avant et après | Gain ou neutralité constatés sur l'état de référence, contraintes toujours lues avant leurs décisions | Régression : retour arrière | Pas commencé |
| 8. Calibration sur le jugement du mainteneur (sur décision) | Une vingtaine de paires de captures à l'aveugle | On sait quelles mesures prédisent ce jugement ; les bornes sont recalibrées par lot | Une mesure qui ne prédit rien est retirée ; rien n'est présenté comme validé | Pas commencé |

**Prérequis :** les mesures avec modèle appris (saillance, représentation d'images) restent facultatives ; sans elles, mesures sans modèle (encombrement, vide, contraste).

**Règles transversales :**
- un indicateur qui ne change aucune décision sur trois runs est retiré ;
- un indicateur bruyant devient un relevé sans statut ;
- un passage n'est retiré qu'après avoir montré qu'il ne protège ni n'oriente aucune décision observée.

## Ce que ça apporte

1. **On comprend pourquoi une production réussit ou échoue**, et on corrige la bonne chose : le savoir, l'accès, le déclencheur, le moyen ou l'observation.
2. **La capacité esthétique devient observable, donc améliorable.**
3. **Le système se trie sur des faits** : ce qui décide, ce qui protège, ce qui coûte sans apport.
4. **Le premier rendu s'améliore pendant le run** grâce à un second regard sur la capture.
5. **La BIBLIOTHEQUE peut évoluer sur preuve** (`PILOT` → `ADOPTED` sur observations).

**Ce que ça n'apporte pas :** une preuve générale que les pages sont meilleures ; un jugement sur la qualité d'une idée ; une lecture de l'attention interne de l'agent ; une validation du savoir (les données calibrent, elles ne valident pas).

## Risques et garde-fous

| Risque | Garde-fou |
| --- | --- |
| Effet lampadaire : on privilégie ce qui se mesure | Chaque mesure déclare ce qu'elle ne couvre pas ; `CFT-00` reste obligatoire |
| Un vert lu comme preuve de qualité | Statut `SIGNAL` ou `RELEVÉ` uniquement |
| Confondre présence dans le contexte, lecture et application | Niveaux de mobilisation notés séparément, avec leur preuve |
| Prendre l'explication de l'agent pour une preuve | Toujours confrontée au travail produit |
| Attribuer à une route un gain qui vient d'une combinaison | Contribution commune examinée ; ablation ciblée quand l'attribution compte |
| Alléger une protection | Contraintes toujours lues avant leurs décisions ; retrait seulement après preuve d'absence de rôle |
| Répondre à tout défaut par plus de savoir | Diagnostic de la cause avant la correction |
| Faux signaux sur une direction de retenue | Comparaison au caractère déclaré ; contrôle bruyant → relevé |
| Fidélité à l'intention lue comme qualité ou comme singularité | Trois axes séparés : intention, réalisation, spécificité au projet |
| Juge par modèle biaisé | Paires, aveugle, ordre inversé, avis |
| Fréquence d'usage lue comme efficacité | Le journal distingue calibration et validation |

## Questions tranchées

| Question | Décision | Raison |
| --- | --- | --- |
| Format de la déclaration courte | Le JSON décrit dans `ACTION/RECETTE-CARACTERE` (`fonts`, `density`, `material`, `focus`, `proof`, `intensity`, `intended_voids`), écrit avant la construction, à côté de l'artefact, et cité par la trace | Chaque champ a sa route de savoir dans la sortie ; pas de ligne de trace supplémentaire |
| Étape 8 et refus des juges extérieurs | Compatible, sous le nom « calibration sur le jugement du mainteneur » : elle règle des bornes, elle ne valide rien et ne crée aucun seuil universel | Une calibration sur une seule personne recréerait une moyenne si on la lisait comme une validation |
| Version générique de référence | Même modèle, même brief, sans le système | Seule comparaison qui isole l'effet du système ; un autre modèle mesure autre chose |
| Où vit l'outil | Dans le paquet, en `PILOT` | Retrait écrit dans la fiche de version |
| Où vit le journal | Dans ce document, hors paquet, et nulle part ailleurs | Les pages de présentation restent sans historique |

## Questions ouvertes

- [x] Journaliser sans changer le comportement de l'agent : journal passif activé par `DG_JOURNAL`, sur le lecteur de routes et les deux recettes (sortie identique avec ou sans journal, testé).
- [ ] Ressources cherchées hors des outils du paquet (recherche web, connecteurs) : non journalisées ; à relever dans la trace ou par l'évaluateur.
- [ ] Charge d'évaluation de l'état de référence : une production avec le système coûte environ 1,7 fois une production sans (jetons) ; 15 productions faites, 7 paires à évaluer en deux passages.
- [ ] Méthode du générique : laquelle des pistes de l'étape 5 sépare réellement une version générique d'une version dirigée.

## Journal de suivi

| Date | Événement | Détail |
| --- | --- | --- |
| 21-10-2026 | Étape 4, premières mesures | 15 productions : 8 sans le système, 7 avec (briefs 1 à 4). Recette de rendu : 2 défauts bloquants sans le système, 0 avec ; réserves 2,75 contre 1,7 en moyenne. Coût avec le système : environ 1,7 fois plus de jetons. Tronc lu en entier à chaque run ; `check_caractere.py` sollicité une fois sur 7. La recette de caractère donne les mêmes signaux aux deux conditions sur chaque brief : caractères attendus à recaler ou mesure à revoir. Convergence : Atkinson Hyperlegible Next dans 5 productions sur 7 avec le système, sans qu'aucune route ne la cite. Défaut de `check_render.py` trouvé par un run (défilement doux pendant la mesure) et corrigé. Détail dans le protocole. |
| 21-10-2026 | Étape 3, journal de mobilisation | `scripts/journal_mobilisation.py` (`PILOT`, révision `R2026-10-21`) : avec `DG_JOURNAL=run.jsonl`, `read_route.py`, `check_render.py` et `check_caractere.py` notent routes lues ou proposées, appels et résultats ; la fiche en Markdown liste lectures et appels dans l'ordre, signale le tronc non consulté et laisse conséquence et preuve à établir. Sans la variable, rien n'est écrit ; un journal impossible à écrire ne bloque rien. Limites : ni l'attention de l'agent, ni l'application d'une route, ni les ressources cherchées hors des outils du paquet. |
| 21-10-2026 | Version 3 du plan | Périmètre étendu à la mobilisation réelle (connaissances et moyens : accès, déclenchement, application, conséquence) et aux manques. État de référence et instrumentation de la mobilisation avant toute réécriture ; analyse des passages par décision et moment de lecture ; formulations corrigées (savoir de jugement et recettes, recette de caractère limitée à la fidélité à l'intention, défaut récurrent ≠ manque de savoir). |
| 16-10-2026 | Intégration dans le paquet | Révision `R2026-10-16.2`. Outil renommé `check_caractere.py` ; bornes figées, recalibration par lot de cinq runs hors échantillon ; tests de mesure dans un vrai navigateur (pages aérée, dense, à aplats, police absente) ; numpy et Pillow installés par la CI ; `--tronc` affiche la marge et la signale sous 10 % ; bandeaux de sections et fiche de version au vocabulaire neutre. Questions ouvertes tranchées. |
| 16-10-2026 | Étape 2, signaux de caractère | Aplats corrigés ; `check_character.py` confronte les mesures au caractère déclaré. Seuil étape 3 sans signal ; Seuil accueil : foyer faible et vide central ; version dense : densité contredite ; génériques déclarés « retenue, typographie » : intensité et matière contredites. Réserve : bornes réglées sur ces mêmes pages. |
| 16-10-2026 | Étape 2, premier passage | Mesures sans modèle (modèles appris inaccessibles). Densité, vide et bande vide répondent comme attendu (le vide central de Seuil est trouvé, 144 px). La distance d'empreinte au générique échoue (deux génériques à 0,73 l'un de l'autre, Seuil à 0,61 du générique clair) : non retenue. Aplats imbriqués comptés deux fois. |
| 16-10-2026 | Étape 1 faite | Prototype `check_declaration.py` hors paquet : police de repli, teinte en trop, objet noyé et objet réduit détectés ; Seuil sans faux signal, un vrai signal (libellés de la bande de semaine à 9,1–9,5 px). Limite : faux gras non détecté. |
| 16-10-2026 | Plan créé | Périmètre, décisions, carte et étapes fixés |
| 16-10-2026 | Run de test Seuil | Deux défauts esthétiques trouvés à l'œil : cas de contrôle pour l'étape 2 |
| 16-10-2026 | Paquet corrigé | Notice de check_render hors de Gate A, Gate A dans le tronc DIRECTION, budget 35 000, bandeaux LIEUX |

**16-10-2026 — Run réel hors échantillon (programme d'un club de jazz fictif).** Déclaré : compression, foyer distribué, intensité, matière typographique. Premier rendu : 0 signal technique, 4 signaux de caractère. Deux ont changé une décision : en 1440 px, densité contredite et matière « aplats » au lieu de « typographie » → bureau recomposé en affiche typographique. Après correction, la matière concorde ; la densité reste « aérée » : c'est la déclaration qui était fausse, gardée avec sa raison. Mobile : cartes gardées volontairement. Faux signal : le vide final de page compté comme « bande vide entre deux contenus ». Raté par les outils : la coupure « LE SOUS- / SOL » du titre mobile. Critère de réussite atteint sur ce run.

**16-10-2026 — Runs 2 et 3 hors échantillon (atelier de céramique calme ; écran de tournée de livreur).** Atelier : la police serif déclarée n'était pas rendue (repli Liberation Serif, 24 % des glyphes) → corrigée en embarquant une vraie police : décision changée. Matière en quasi-égalité (aplats 28 % contre texte 24 %) : faux signal → marge de 25 % ajoutée. Livreur : la règle « plus grande masse peinte » de `check_declaration.py` signalait la liste, alors que la carte noire domine à l'œil et que la saillance le confirme → faux signal, contrôle retiré ; la dominance perçue appartient désormais au seul `check_character.py`.

**Bilan sur trois runs hors échantillon.** Ont changé une décision : polices rendues (1), densité (1), matière (1). Aucune décision changée : rôles de couleur, lisibilité de l'objet de preuve, foyer, intensité, vide (hors Seuil). Selon la règle du plan, ces cinq-là sont candidats au retrait ou au statut de relevé.
