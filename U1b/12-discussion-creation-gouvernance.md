# Discussion avant toute implémentation : capacité créative, gouvernance, potentiel

**Date :** 2026-10-07. **Base :** commit `d90869c`.

**Sources de cette note :**
1. l'inventaire U1b (10 fiches et la synthèse) ;
2. l'historique du projet, trouvé dans ton dépôt public `Palolo875/design-governance` (version V1.1.1 du 26 septembre, audit DG-AUDIT-001, plan V1.2), lu en lecture seule ;
3. trois recherches extérieures, environ 100 lectures de sources, dont la liste est en annexe.

**Rien n'a été modifié dans le dépôt.**

**Légende des niveaux de preuve :**
- **[mesuré]** : testé par nous ;
- **[historique]** : observé lors de l'audit précédent, souvent N = 1 et avec un seul juge ;
- **[étude]** : recherche publiée ;
- **[éditeur]** : documentation ou blog d'Anthropic, OpenAI, etc. ;
- **[inférence]** : mon raisonnement, à vérifier.

---

## 0. L'essentiel en dix lignes

1. **Le système sait rendre le travail plus vrai, plus robuste et plus accessible.** Il ne sait pas encore le rendre plus beau ni plus présent. C'est la seule comparaison avec et sans le système qui existe [historique, N = 1].
2. **Ta crainte sur les exemples est fondée.** Un exemple unique, concret, familier et proche du domaine est ce qui fige le plus, chez l'humain comme chez le modèle [étude, historique]. Une seule phrase trop affirmative a déjà codifié la palette par défaut du modèle [historique].
3. **Mais ne rien montrer ne protège pas non plus.** Sans guidage, le modèle retombe sur sa moyenne (« neutres + un accent », dégradés, Inter). Les listes d'interdits déplacent cette moyenne au lieu de la supprimer [étude, éditeur].
4. **Ce qui marche le mieux, d'après les sources :**
   - diverger avant de converger (nommer la réponse attendue, proposer plusieurs directions) ;
   - donner les raisons plutôt que des modèles à copier ;
   - observer le vrai rendu avec un regard extérieur au producteur [étude, éditeur].
5. **Le système a déjà la moitié de ces leviers** (MODAL et PARTI, ancres transformées, directions comparées). **L'autre moitié lui manque** : l'observation outillée et le regard extérieur.
6. **Sa gouvernance est lourde pour un modèle.** Le noyau est 4,5 fois plus gros que la skill de design d'Anthropic, et un run DIRECTION lit 600 à 1 300 lignes. Les études montrent que beaucoup d'instructions et de formats imposés réduisent le respect des consignes, le raisonnement et la diversité [étude, mesuré]. C'est une **hypothèse sérieuse** sur la faible présence des rendus, pas encore un fait.
7. **Les quatre axes d'audit que tu cites sont bien couverts par U1, U1b et le plan, sauf la « qualité esthétique et mobilisation effective »**, qui ne peut être mesurée que par des runs réels (U2, U5). Je propose de rendre cette grille explicite dans le plan.
8. **J'ai tranché les cinq points (§1).** Je propose aussi deux ajouts à U2 : une condition **sans le système**, et un **regard humain à l'aveugle**.

---

## 1. Les cinq points : mes choix

| # | Point | Choix | Raison |
|---|---|---|---|
| **D1** | Où ranger les documents de refonte | Une **branche dédiée `refonte`**, qui ne contient que les documents (plan, registre, mesures, preuves). Elle sera créée **au début de l'implémentation**. D'ici là, tout reste dans mon espace de travail | Le paquet refuse tout fichier hors inventaire (C20). Une branche séparée versionne le travail sans toucher au paquet |
| **D2** | Une seule liste de chargement | Garder `DIRECTION/CHARGE` comme liste unique. La carte d'ACTION deviendra un renvoi, mais **en U4 seulement, après mesure** | C13 est confirmé par l'inventaire (au moins 8 tables de routage) |
| **D3** | Agents neufs pour la mesure | **Oui**, avec deux ajouts tirés de la recherche (§6) : une condition « sans le système » et un juge humain à l'aveugle | Un modèle qui juge sa propre production est biaisé en sa faveur [étude] ; l'audit précédent n'a jamais pu lever ce biais [historique] |
| **4** | Règle d'évolution du CHANGELOG | **Adoptée.** Chaque lot porte une fiche de 8 lignes dans son commit : source, propriétaire, périmètre, compatibilité, preuve, limite, revue, retour. Tu décides. S'y ajoute un test d'entrée inspiré de GOV.UK : une règle nouvelle doit être **utile** (un échec observé), **unique** (pas un doublon) et **polyvalente** | C'est la règle du système lui-même, et le test évite d'ajouter par précaution |
| **5** | Verrous des validateurs | Chaque lot liste les verrous qu'il touche et les adapte **explicitement**, avec leur mutation rouge. **Pas de hausse nette** : retirer une phrase retire son verrou | Environ 220 formulations verrouillées (fiche n°10) ; elles ne doivent pas grossir à chaque correction |

---

## 2. Les quatre axes d'audit sont-ils dans le plan ?

| Axe | Ce qui a été audité | Où | Ce qui manque | Vérification après changement |
|---|---|---|---|---|
| **Organisation et lecture** (hiérarchie, vocabulaire, répétitions, parcours, charge cognitive) | Charge par mode mesurée en octets ; au moins 6 parcours, 8 tables de routage, 3 jeux d'axes, 4 FAST-PATH ; glossaire ; registre | U1 (C07, C13, C15, C16, C22, C26, C27) ; fiches n°4, 7 ; synthèse M1, M6 | La charge **réelle** (tokens, ce que l'agent ouvre) n'est mesurable que pendant un run | U4 : charges remesurées ; U5 : routes réellement ouvertes |
| **Capacités et ressources** (disponibilité, adaptation, qualité esthétique, mobilisation effective) | Disponibilité et adaptation par couche (fiches n°1 à 6, synthèse) ; moyens réduits à des noms (C38) ; polices bloquées (C39) | U1b ; U3b prévu | **La qualité esthétique et la mobilisation effective ne sont pas auditables sur papier** : elles demandent des runs | U2 (référence), puis U5 (après), avec les mêmes briefs |
| **Fiabilité** (protections, contrats, preuves, clôtures, transmissions, restauration) | Matrice des cinq absolus ; 23 tests reproductibles ; C10 (restauration) ; C11, T-18 à T-22 (forme sans fond) | U1 ; fiches n°8, 9, 10 | Rien d'important | `validate_all` après chaque lot ; tests T-01 à T-23 rejouables |
| **Relations entre fichiers** (dépendances, consommateurs, compilation, guides, distributions) | Noyau compilé ; guides ; distributions GitHub et Local ; reprises de règles (C03, C25) ; verrous | U1 ; fiches n°3, 6, 7, 10 | Une vue d'impact simple (qui reprend quelle règle), prévue en U3 via C25 | `validate_all`, deux builds identiques, CI |

**Réponse.**
- **Oui pour trois axes sur quatre.** L'audit qui détermine les corrections est fait (U1, U1b). Les vérifications après changement sont prévues (validation à chaque lot, U5).
- **L'axe « capacités et ressources » n'est couvert qu'à moitié**, et c'est normal : sa partie esthétique ne peut se mesurer qu'en faisant travailler le système.

**Ce que je propose d'ajouter au plan** : une section courte, « Grille d'audit en quatre axes ». Elle servirait deux fois avec les mêmes rubriques : avant (constats) et après (vérification des effets et des régressions). Elle ne crée aucun nouveau mécanisme.

**Pour mémoire, l'audit précédent couvrait déjà ces quatre axes** dans son protocole :
- §15, architecture de l'information et charge cognitive ;
- §16, dix dimensions esthétiques ;
- §14, contrats ;
- §6.2, interfaces entre fichiers.

Mais **environ 10 % seulement de ses 158 constats portaient sur la création** ; le reste portait sur la cohérence entre textes et machine [historique]. **La refonte doit corriger ce déséquilibre**, pas le reproduire.

---

## 3. Ce que l'histoire du projet nous apprend

Source : dépôt `Palolo875/design-governance`, archive du 26 septembre. L'auditeur était Claude, seul observateur, et il jugeait ses propres corrections. **Toutes ces observations sont donc des signaux, pas des preuves.**

| Observation | Où | Portée |
|---|---|---|
| **Les agents imitent les exemples** : un exemple qui contredit une règle « enseigne la contradiction mieux que la règle n'enseigne la règle ». Les quatre exemples de l'époque contredisaient les règles ; ils ont été corrigés et verrouillés | Phase 11.13 (C6) | Postulat de l'audit ; l'épreuve d'imitation a échoué (0/2), mais sur la forme |
| **Une phrase a codifié la pente du modèle.** « Les neutres portent l'essentiel de la structure ; l'accent signale… », sous le tag le plus fort, menait au canon « sombre + serif + doré » que le système lui-même dit ne pas être le premium. Elle a été corrigée en quatre phrases et remplacée par la **question de convergence** | Phases 9.06, 11.14 (C7) | Le risque n'était pas un manque de règle, mais une phrase trop affirmative |
| **Le système faisait fabriquer de la diversité** : un quota de « deux changements structurels » par direction, sans source, a été retiré | Phase 11.10 (C3) | Diversité simulée, corrigée |
| **Huit grilles de jugement du craft** coexistaient : « cinq grilles mobilisées pour un seul objet ». Ramenées à une revue, une grille, un gate | Phase 11.17 (D1) | La gouvernance pesait sur le geste créatif |
| **La seule comparaison avec et sans le système** (brief : ton app de budget pour freelances) : le système gagne nettement en vérité (aucune affirmation inventée, liens fonctionnels), en accessibilité (0 défaut contre 7 à 8), en robustesse et en ordre mobile. **Il perd en présence et en désirabilité** : la version sans système était « plus chaleureuse, plus calme » | Phase 9.08, planche C | N = 1, un seul juge. **C'est le résultat le plus important pour ta question** |
| **La convergence vient d'abord du modèle** : avec et sans le système, l'accent était un **vert profond** sur des neutres. Sur 3 briefs : sans le système, 3/3 dans des palettes convergentes ; avec, 2/3, plus un cas incertain | Phases 9.08, 13.02 (mesure M) | « Non concluant » |
| **L'épreuve à l'aveugle avec des juges humains extérieurs** (chantier F du plan V1.2), condition de publication, **n'a jamais eu lieu** | Plan V1.2 ; CHANGELOG actuel | L'efficacité reste `NOT-VERIFIED` |
| Une partie du plan V1.2 est passée dans la version actuelle : bilan de fabrication, prise de brief en trois questions, MODAL et PARTI, marqueurs de tendance datés. L'« atlas d'ancres annotées » (chantier E) n'a pas été livré : l'actuel DESIGN-ATLAS est un index de familles | Comparaison de l'archive et du dépôt actuel | — |

**Un détail visible sur la planche C.** Le rendu « avec système » est en police de repli : une grotesque système, grasse et sèche. Le rendu « sans système » utilise un serif d'affichage avec italique. Une partie de l'écart de présence peut venir des **moyens** (polices non chargées, C39), pas seulement de la gouvernance [inférence].

---

## 4. La capacité esthétique et créative

### 4.1 Ce que le système sait faire (preuves concordantes)

- **La vérité et l'honnêteté.** Il n'invente pas d'affirmations, marque les exemples et n'utilise pas de faux assets [historique 9.08 ; fiches n°3 à 5].
- **La robustesse et l'accessibilité automatisable** [historique 9.08 ; `check_render`, fiche n°6].
- **Corriger dans la bonne direction.** Face à un rendu « séduisant mais générique », ses règles orientent la correction vers la relation entre l'objet et la promesse, pas vers du polish [historique 9.06].
- **Un jugement riche** : grammaire de composition, 13 gestes de craft, émotions, traduction des mots vagues (fiches n°1, 2, 4).

### 4.2 Ce qu'il ne montre pas encore

**La présence et la désirabilité.** C'est le cœur de ta question.

### 4.3 Quatre causes probables

Ce sont des hypothèses à mesurer, classées de la plus étayée à la moins étayée.

| # | Cause | Ce qui l'étaye | Ce qui la tempère |
|---|---|---|---|
| **C-a** | **Pas d'observation réelle ni de regard extérieur.** L'agent juge ses propres captures, quand il en a | Dans un pipeline de génération web, la critique visuelle externe apporte +10 à +18 %, contre **+1,5 %** pour une simple seconde passe sans critique [étude, Amazon 2026] ; sans retour externe, l'auto-correction n'aide pas et peut nuire [étude, Huang 2024] ; un modèle préfère ses propres productions [étude, NeurIPS 2024] ; Anthropic recommande un **vérificateur en contexte frais** [éditeur] | Les gains sont souvent mesurés par des juges automatiques, rarement par des humains |
| **C-b** | **Le poids des consignes.** Noyau d'environ 43 Ko, soit environ 11 000 à 14 000 tokens [inférence], contre une cible d'environ 5 000 tokens et 500 lignes recommandée par Anthropic [éditeur] ; 600 à 1 300 lignes lues en DIRECTION [historique] | Le respect simultané d'instructions décroît avec leur nombre (environ 68 % à 500 instructions) [étude, IFScale] ; les formats imposés réduisent le raisonnement [étude, Tam 2024] et la diversité [étude, *Price of Format*] ; les contraintes de processus ont un effet en U inversé sur la créativité [étude, Acar 2019] | Aucune étude ne mesure l'effet sur une skill de design précise ; c'est à mesurer chez nous |
| **C-c** | **Pas de moyens concrets** : polices bloquées par défaut à l'observation, moyens réduits à des noms (C38, C39) | La planche C montre un rendu en police de repli ; les éditeurs dont les rendus sont cohérents fournissent des ressources concrètes (pile de composants, exemples récupérés, style persistant) [éditeur] | Des ressources fixes peuvent devenir un style maison (§5) |
| **C-d** | **La pente du modèle**, présente avec ou sans le système | Convergence vers « neutres + un accent » des deux côtés [historique] ; faible variabilité entre les modèles de langage, comparés aux humains [étude, Wenger 2026] | Le système la nomme déjà (MODAL, question de convergence) |

---

## 5. Exemples et code : comment guider sans figer ni produire du slop

### 5.1 Ta crainte est fondée

| Constat | Niveau |
|---|---|
| Un exemple unique, concret, complet, **familier et proche du domaine** fixe le plus. Les designers en reprennent les traits même quand on leur demande de les éviter (Jansson & Smith 1991, puis Purcell & Gero, Viswanathan 2016) | [étude] |
| Pour un modèle, les démonstrations transmettent surtout la **forme de surface** (Min et al. 2022) | [étude] |
| Avec un générateur d'images, les humains se fixent davantage sur la première sortie qu'avec une simple recherche d'images (CHI 2024) | [étude] |
| Les agents imitent les exemples du système ; une phrase trop affirmative a codifié la palette par défaut | [historique] |
| Anthropic interdit Inter et les dégradés violets… et observe une nouvelle convergence sur **Space Grotesk**, qui figurait dans ses propres suggestions. Son guide le plus récent note qu'un « n'utilise pas de crème » déplace le modèle vers une autre palette fixe | [éditeur] |

**Le système le sait déjà.**
- BIBLIOTHEQUE refuse de devenir « galerie d'assets ou corpus de goût ».
- Les marqueurs de tendance ne peuvent apparaître que datés.
- Les ancres doivent être transformées, jamais copiées.
- Le plan V1.2 avait déjà ce critère d'arrêt : « si la diversité baisse, retirer les exemples de familles, garder les critères ».

### 5.2 Mais ne rien montrer ne protège pas non plus

- Sans exemple, le modèle retombe sur son mode statistique [étude, Wenger 2026 ; éditeur].
- Les mots « très créatif » ou une température élevée n'aident que peu [étude].

La question n'est donc pas « exemples ou pas », mais **quels guides orientent sans devenir un modèle à copier**.

### 5.3 Ce qui oriente sans figer

Ce tableau est une proposition de principes pour la discussion, pas une liste de choses à construire.

| Principe | Ce que disent les sources | Ce que le système a déjà | Ce qui manque |
|---|---|---|---|
| **Diverger avant de converger** : nommer la réponse attendue, puis proposer plusieurs directions réellement différentes | *Verbalized Sampling* (diversité ×1,6 à ×2,1) [étude] ; Lovable, OpenAI et le guide Anthropic récent recommandent 3 ou 4 directions avant de construire [éditeur] | MODAL et PARTI au noyau ; `creative_direction_set` (au moins 2 directions), mais seulement conditionnel | La comparaison de directions n'est pas le chemin par défaut ; sa diversité n'est vérifiée que sur la forme (T-18) |
| **Des raisons plutôt que des instances** : dire *pourquoi*, et à quoi le choix doit répondre dans ce contexte | Anthropic : expliquer la motivation, éviter les MUST rigides [éditeur] ; contraintes appariées de Stokes : « évite X *parce que…*, choisis plutôt selon Y » [étude] | Critères de choix typographiques, palette par rôles, question de convergence : déjà formulés en raisons | Plusieurs listes d'interdits restent sans leur « parce que » |
| **Des références lointaines, partielles, observées sur le moment, jamais archivées comme modèle** | Les exemples **lointains et peu communs** améliorent la nouveauté ; les **partiels** fixent moins que les complets [étude, Chan 2011 ; Cheng] | Ancres : retenu, rejeté, transformation ; calibrations par domaine (cinéma, édition, affichage) | Rien d'outillé pour aller chercher une référence lointaine |
| **Du code seulement pour les invariants et l'observation**, jamais pour l'esthétique | La recopie de surface est le risque principal [étude] ; les éditeurs fournissent du code pour la pile technique et la vérification (Playwright) [éditeur] | `check_render` : du code qui **observe**, pas du code qui **produit** un style | Un outil de capture et de vue floue (aucun aujourd'hui) |
| **Des moyens décrits par critères et par statut, pas des listes « recommandées »** | Une liste nommée devient le nouveau défaut [éditeur, Space Grotesk] | Carte des moyens (des noms) ; U3b prévu (statuts) | Le statut réel de chaque moyen ; des polices observables à la mesure (C39) |
| **Mesurer la diversité** : c'est le garde-fou contre le slop **et** contre le figement | Aucune étude ne répond à notre cas précis ; il faut le mesurer [étude] | B2 lancé deux fois dans U2 | Une mesure de similarité simple (palette, police, ossature, objet) |

**La règle que je propose pour la refonte** (à valider) : **aucun exemple, gabarit ou extrait de code à visée esthétique n'entre dans le paquet sans une mesure de diversité avant et après.** Les exemples de **trace** (forme d'une décision) et le code d'**observation** restent permis.

---

## 6. La gouvernance : ce qu'elle doit garder, ce qu'elle doit alléger

**À garder.** C'est ce que la seule comparaison montre comme utile :
- la vérité (exemples marqués, aucun faux asset) ;
- les protections critiques (consentement, santé, accessibilité) ;
- l'honnêteté de la preuve (« non vérifié » plutôt qu'un faux succès) ;
- la trace légère par défaut.

**Ce que disent les pratiques humaines** [éditeur, praticien] :
- Les design systems qui durent distinguent un **cœur** stable, une zone **expérimentale** (Carbon Labs, l'étiquette « Experimental » de l'ONS) et l'**exception locale** (le « snowflake » de Brad Frost).
- Ils **révisent régulièrement leur gouvernance** pour retirer ce qui ne sert pas.
- La critique de design se rattache aux objectifs, pas aux préférences, et ne se transforme pas en séance de résolution.

**Ce que j'en déduis pour Design Governance** [inférence, à mesurer] :
1. **Les validateurs ne coûtent rien à l'agent**, puisqu'ils s'exécutent hors de son contexte. **Le texte du noyau, si.** Alléger, c'est d'abord déplacer du texte de gouvernance du noyau vers les routes, pas supprimer des protections.
2. **Créer d'abord, conformer ensuite.** Le système le fait déjà en partie : la trace légère vient après la proposition, la RUN_CARD seulement en trace complète. C'est le bon principe, à préserver.
3. **Graduer selon l'enjeu.** Les modes le font déjà ; c'est le noyau, lu par tous les modes, qui porte tout le poids.
4. **Un regard extérieur plutôt qu'une grille de plus.** L'histoire montre que multiplier les grilles a alourdi sans améliorer. Ce qui manque, c'est un **autre regard**, pas une autre règle.

---

## 7. Le potentiel du système

À mon avis, Design Governance peut devenir **un directeur artistique honnête** : il dit la vérité, dirige, **regarde réellement** ce qu'il produit et **mesure** ce qu'il apporte. Il possède déjà la vérité, la direction et l'honnêteté de la preuve. Il lui manque **le regard et la mesure**.

Les leviers les plus prometteurs sont surtout des **déplacements** :

| Levier | Nature | Appui |
|---|---|---|
| Rendre l'observation réelle : `check_render` et ses options au noyau ; capture desktop et mobile, vue floue (U6) | Outil existant, à déplacer et compléter | Étude (critique externe), éditeur (Playwright) |
| Faire juger par un **contexte frais**, sur captures, avec une grille courte à plusieurs dimensions, en n'acceptant que les révisions qui battent la précédente | Méthode, sans nouveau mécanisme lourd | Étude (auto-préférence, ReLook, Amazon), éditeur (Anthropic) |
| **Alléger le noyau** vers la cible Anthropic, en déplaçant la gouvernance vers les routes | Déplacement | Éditeur, étude |
| Faire de la **divergence** (MODAL, puis directions comparées) le chemin court par défaut en DIRECTION | Promotion d'un outil existant | Étude, éditeur |
| Donner aux **moyens** un statut réel, et rendre les polices observables | U3b déjà prévu | Inventaire (C38, C39) |

**Aucun de ces leviers n'est décidé.** Chacun sera jugé sur la mesure (U2, puis U5), comme le prévoit le plan.

---

## 8. Ce que je propose de changer dans le plan

Changements à discuter, sans implémentation :
1. **U2, ajouter une condition « sans le système »** : le même brief produit par un agent neuf sans la skill. C'est la seule façon de savoir si le système améliore, ce que personne n'a encore établi.
2. **U2, ajouter un regard humain à l'aveugle** : toi, et si possible une personne extérieure. Comparaison **par paires** (A contre B, ordre inversé une fois), plus une grille courte (présence, spécificité, finition, vérité, défaut dominant). Un juge automatique en contexte frais peut compléter, déclaré comme tel.
3. **U2, mesurer la diversité** : B2 lancé deux fois (déjà prévu), plus une comparaison simple palette, police, ossature et objet de preuve.
4. **Ajouter la grille d'audit en quatre axes** (§2), utilisée avant et après chaque lot.
5. **Ajouter aux règles de conduite :**
   - règle 9 : aucun exemple ni code esthétique sans mesure de diversité ;
   - règle 10 : la fiche de changement en 8 lignes et le test « utile, unique, polyvalent » ;
   - règle 11 : pas de hausse nette des verrous.
6. **Déclarer une limite de U2** : une condition sans le système et un juge humain restent un pilote. Ils orientent la décision, ils ne prouvent rien de général.

## 9. Questions pour toi

1. **Qui peut juger à l'aveugle ?** Toi seul, ou aussi une ou deux personnes extérieures (dont si possible un designer) ? C'est le seul point que je ne peux pas fournir moi-même.
2. **Acceptes-tu la condition « sans le système » dans U2 ?** Elle double à peu près le coût de la mesure.
3. **Les ajouts au plan du §8 te conviennent-ils ?** Si oui, je les intègre au plan, toujours sans toucher au paquet.

---

## Annexe : sources principales

**Historique du projet** (dépôt `Palolo875/design-governance`, archive `DG_kit_ClaudeCode.zip`, lecture seule) :
- `plans/Plan_V1.2_Qualite_senior_gouvernance.md` ;
- `audit/reports/` : 6.02b, 9.06, 9.08, 11.10, 11.13, 11.14, 11.17, 13.02, clôture finale ;
- `audit/logs/PLANCHE_LOT_A.png`, `PLANCHE_LOT_C.png`, `DG_AUDIT_001_13-02_run_DIRECTION_v2_desktop.png`.

**Fixation et uniformisation** :
- Jansson & Smith 1991 (via TU Delft) : https://repository.tudelft.nl/file/File_6a026941-2298-42fd-bf7a-dc08eaa73bd5
- Chan et al. 2011 (exemples lointains et peu communs) : https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf
- Chrysikou & Weisberg 2005 : https://researchdiscovery.drexel.edu/esploro/outputs/journalArticle/Following-the-wrong-footsteps-fixation-effects/991020531858804721
- Vasconcelos & Crilly 2016 : https://www.repository.cam.ac.uk/handle/1810/252511
- Doshi & Hauser 2024 : https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532
- Padmakumar & He 2024 : https://arxiv.org/abs/2309.05196v3
- Wenger & Kenett 2026 : https://academic.oup.com/pnasnexus/article/5/3/pgag042/8529001
- *Verbalized Sampling* : https://arxiv.org/abs/2510.01171v3
- Shin et al. 2026 : https://arxiv.org/html/2603.13036
- Min et al. 2022 : https://arxiv.org/abs/2202.12837
- Zhou et al., CHI 2024 : https://arxiv.org/abs/2403.11164

**Retour visuel et évaluation** :
- Anthropic, *Improving frontend design through Skills* : https://claude.com/blog/improving-frontend-design-through-skills
- Skill `frontend-design` d'Anthropic (9,4 Ko, 71 lignes, vérifié) : https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md
- Claude Code, *Best practices* (vérificateur en contexte frais) : https://code.claude.com/docs/en/best-practices
- OpenAI, *Designing delightful frontends* : https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4
- Lovable, *Design guidance* : https://docs.lovable.dev/features/design-guidance
- Amazon AGI 2026, raffinement guidé par la vision : https://cdn.amazon.science/e2/87/68ecc1e04ecc9e2e92bcd5fd3750/scipub-approval152129-45356067-visionguided-iterative-refinement-for-frontend-code-generation.pdf
- UICrit (UIST 2024) : https://arxiv.org/html/2407.08850v3
- *MLLM as a UI Judge* : https://arxiv.org/html/2510.08783v1
- Auto-préférence (NeurIPS 2024) : https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html
- Huang et al. 2024, auto-correction : https://arxiv.org/abs/2310.01798v2
- ReLook : https://huggingface.co/papers/2510.11498.md
- Deque, axe-core : https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues

**Skills et gouvernance** :
- Anthropic, Agent Skills, *best practices* : https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- Anthropic, *Effective context engineering* : https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- *Lost in the Middle* (TACL 2024) : https://aclanthology.org/2024.tacl-1.9/
- IFScale : https://arxiv.org/abs/2507.11538
- Tam et al. 2024 : https://arxiv.org/html/2408.02442v1
- *The Price of Format* : https://arxiv.org/abs/2505.18949
- Acar et al. 2019 : https://openaccess.city.ac.uk/id/eprint/20459/
- Brad Frost, gouvernance : https://bradfrost.com/blog/post/a-design-system-governance-process/
- GOV.UK, critères de contribution : https://design-system.service.gov.uk/community/contribution-criteria
- IBM Carbon, contribution : https://www.carbondesignsystem.com/contributing/get-started/overview
- NN/g, critiques de design : https://www.nngroup.com/articles/design-critiques/

**Sources non vérifiées** : *Curse of Instructions* (source secondaire seulement), la page EightShapes (inaccessible) et l'article original de Jansson & Smith (lu via une synthèse).
