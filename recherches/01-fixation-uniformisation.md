# Rapport : exemples, fixation et homogénéisation dans un système de consignes de design pour agents LLM

**Comment lire ce rapport.** Chaque affirmation porte un niveau de preuve : [revue à comité de lecture], [preprint], [blog/doc éditeur] ou [avis de praticien]. Si j'ai seulement lu l'abstract ou une source secondaire, je l'indique par « (via abstract) » ou « (via source secondaire) ». J'ai fait environ 25 recherches et lectures de pages.

---

## 1. La fixation de design chez l'humain

**Jansson & Smith 1991** (*Design Studies* 12(1)) [revue à comité de lecture, via source secondaire]
- On montrait à des designers une image de solution existante, volontairement défectueuse (elle contredisait le brief).
- Ils en reprenaient les traits clés.
- Ils continuaient à les reprendre même quand on leur demandait explicitement d'éviter ces traits.
- Sources : TU Delft repository (https://repository.tudelft.nl/file/File_6a026941-2298-42fd-bf7a-dc08eaa73bd5) ; Jon Kolko (https://www.jonkolko.com/phd/writing/25-06-12-design-fixation) [avis de praticien]. Je n'ai pas ouvert l'article original.

**Purcell & Gero 1996** (*Design Studies* 17(4)) [revue à comité de lecture, via source secondaire]
- Ils ont refait l'expérience avec des designers industriels et des ingénieurs mécaniciens.
- Les designers industriels ne montraient pas de fixation. Les ingénieurs mécaniciens, si.
- Les auteurs l'attribuent à une formation qui valorise les solutions distinctes.
- Ils notent aussi que la fixation apparaît surtout quand l'exemple est **familier** au domaine.
- Les réplications de 1993 avaient été en grande partie infructueuses.
- Source : https://repository.tudelft.nl/file/File_6a026941-2298-42fd-bf7a-dc08eaa73bd5 (synthèse secondaire).

**Chrysikou & Weisberg 2005** (*JEP:LMC* 31(5)) [revue à comité de lecture, via abstract]
- Les participants suivaient l'exemple même quand il contenait des éléments inappropriés.
- En revanche, des **instructions de défixation** (« évitez ces éléments problématiques ») ont réduit l'effet.
- Cela **contredit en partie** Jansson & Smith.
- Source : https://researchdiscovery.drexel.edu/esploro/outputs/journalArticle/Following-the-wrong-footsteps-fixation-effects/991020531858804721

**Linsey et al. 2010** (*J. Mechanical Design*) [revue à comité de lecture, via abstract et citations]
- Des enseignants-chercheurs en ingénierie étaient significativement fixés sur l'exemple, sans s'en rendre compte entièrement.
- Des matériaux de défixation (représentations alternatives du problème) ont atténué l'effet.
- Un suivi montre que ces matériaux aident peu les novices.
- Sources : https://cognitive.designsociety.org/publication/28853/Reducing+and+Perceiving+Design+Fixation%3A+Initial+Results+from+an+NSF-Sponsored+Workshop ; https://peer.asee.org/22645.pdf. Le PDF intégral (lrdc.pitt.edu/…/JMD041003.pdf) renvoie une erreur 404.

**Chan et al. 2011** (*J. Mechanical Design*, DOI 10.1115/1.4004396) [revue à comité de lecture, texte intégral lu]
- Les exemples étaient croisés selon trois axes : distance (proche / lointain), banalité (commun / peu commun) et modalité (image / texte).
- Les exemples **lointains** et **peu communs** ont amélioré la nouveauté.
- La combinaison « lointain + peu commun » a battu le groupe contrôle sans exemple.
- La modalité (image ou texte) n'a pas modulé ces effets.
- Source : https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf
- Fu et al. 2013 proposent l'idée d'une distance optimale (« sweet spot »), ni trop proche ni trop lointaine : https://www.lrdc.pitt.edu/Schunn/papers/fuchanetal-near-far-2013.pdf (non ouvert).

**Viswanathan, Tomko & Linsey 2016** (*AI EDAM* 30(2)) [revue à comité de lecture, via abstract]
- Un exemple aux traits **familiers** fixe plus qu'un exemple aux traits peu familiers.
- La modalité de présentation (croquis ou prototype) module aussi l'effet.
- Source : https://www.cambridge.org/core/product/AD93E342571AB85057D36CFD4C53EE77

**Exemples partiels** (Cheng, Mugge & Schoormans) [revue à comité de lecture, via abstract seulement]
- Des photos partielles d'exemples ont produit des designs plus originaux que des photos complètes.
- Je n'ai pas pu vérifier l'année ni l'échantillon.
- Source : https://scholar.hit.edu.cn/en/publications/a-new-strategy-to-reduce-design-fixation-presenting-partial-photo/

**Vasconcelos & Crilly 2016** (*Design Studies* 42) [revue à comité de lecture, via abstract]
- Ce n'est **pas une méta-analyse au sens statistique**. C'est une revue de 25 études qui identifie 14 variables manipulées.
- Elle constate une **grande hétérogénéité** des méthodes et des résultats.
- Source : https://www.repository.cam.ac.uk/handle/1810/252511
- La méta-analyse proprement dite est **Sio, Kotovsky & Cagan 2015** (*Design Studies*). Je n'ai pas pu en ouvrir l'abstract.
- Des travaux de Vasconcelos et al. suggèrent qu'une partie de la « baisse de fluence » vient du niveau de détail de l'exemple : un exemple détaillé incite à des idées détaillées, donc moins nombreuses. Ce ne serait donc pas seulement de la fixation. Source : https://www.repository.cam.ac.uk/handle/1810/265815 (via résumé secondaire).

**En résumé pour la question 1**
- Ce qui fixe le plus : les exemples uniques, concrets, familiers, proches du domaine et détaillés.
- Ce qui atténue la fixation :
  - des exemples lointains ou peu communs ;
  - des exemples partiels ou abstraits ;
  - des instructions de défixation (résultats mixtes) ;
  - des représentations alternatives du problème ;
  - l'expertise et la formation.
- Je n'ai trouvé aucune preuve solide que **plusieurs exemples diversifiés** suffisent à eux seuls. Aucune source ouverte ne teste directement cette variable.

---

## 2. Homogénéisation des sorties de LLM

**Doshi & Hauser 2024** (*Science Advances* 10(28), eadn5290) [revue à comité de lecture, via abstract et communiqué]
- Des idées fournies par l'IA rendent chaque histoire jugée plus créative.
- Mais les histoires deviennent **plus semblables entre elles** : c'est un dilemme social.
- Source : https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532

**Padmakumar & He 2024** (ICLR) [revue à comité de lecture, conférence]
- Écrire avec InstructGPT (ajusté par retour humain), mais pas avec GPT-3 (modèle de base), réduit la diversité entre auteurs.
- La baisse vient du texte apporté par le modèle.
- Sources : https://arxiv.org/abs/2309.05196v3 ; https://proceedings.iclr.cc/paper_files/paper/2024/hash/02dec8877fb7c6aa9a79f81661baca7c-Abstract-Conference.html

**Anderson, Shah & Kreminski 2024** (Creativity & Cognition) [revue à comité de lecture, N=36]
- Avec ChatGPT, les idées de différents utilisateurs sont sémantiquement moins distinctes entre elles.
- Source : https://arxiv.org/abs/2402.01536v2

**Wenger & Kenett 2026** (*PNAS Nexus* 5(3)) [revue à comité de lecture, lu]
- Comparaison de 22 LLM et 102 humains.
- Les LLM ont une originalité individuelle comparable, mais une **variabilité de population bien plus faible**.
- Un prompt « très créatif » n'augmente que modestement la variabilité.
- Une température de 2.0 produit surtout du charabia.
- Source : https://academic.oup.com/pnasnexus/article/5/3/pgag042/8529001

**De Rooij & Biskjaer 2026** (*Behaviour & Information Technology*, e-pub) [revue à comité de lecture, via abstract]
- Méta-analyse de 19 études et 61 tailles d'effet.
- Effet d'homogénéisation **petit mais significatif**.
- L'effet est plus fort dans les tâches d'idéation **sémantiquement contraintes**.
- Source : https://research.tilburguniversity.edu/en/publications/does-generative-ai-make-us-think-alike-a-systematic-review-and-me-2/

**Verbalized Sampling 2025** (arXiv 2510.01171) [preprint, poster ICML 2026, via résumés]
- L'effondrement de mode (le modèle produit toujours les mêmes réponses) viendrait d'un **biais de typicalité** dans les données de préférence humaine, et pas seulement de l'algorithme.
- Le remède : demander N réponses avec leurs probabilités.
- Résultat annoncé : diversité multipliée par 1,6 à 2,1 en écriture créative.
- Source : https://arxiv.org/abs/2510.01171v3

**Shin et al. 2026** (arXiv 2603.13036) [preprint, lu]
- **Article conceptuel**, sans mesure empirique de sites générés.
- Traits homogénéisés relevés :
  - mises en page minimalistes ;
  - polices sans-serif standard ;
  - tons sourds ;
  - ombres et coins arrondis standard ;
  - Bootstrap et Tailwind.
- Points de risque :
  - un prompt vague, que le modèle comble avec ses défauts ;
  - la génération elle-même ;
  - l'acceptation du premier résultat.
- La fixation de l'utilisateur sur la première sortie est explicitement citée.
- Remède proposé, la « friction productive » :
  - moodboards contrastés à choisir avant de générer ;
  - injection de tokens et guidelines de marque ;
  - styles communautaires.
- Source : https://arxiv.org/html/2603.13036

**IDEAFix** (Carichon et al., mai 2026, arXiv 2606.00875) [preprint, via abstract]
- De simples stratégies de « défixation » par prompt augmentent l'originalité.
- Mais l'homogénéisation **persiste** entre les modèles.
- Source : https://arxiv.org/abs/2606.00875

---

## 3. Ancrage des exemples few-shot

**Min et al. 2022** (EMNLP) [revue à comité de lecture, conférence]
- Les démonstrations transmettent surtout le **format**, l'espace de réponses et la distribution des entrées.
- La justesse des paires compte beaucoup moins.
- Autrement dit, le modèle apprend la **forme de surface** des exemples.
- Source : https://arxiv.org/abs/2202.12837

**Effet des exemples sur la diversité** [preprint]
- Le seul résultat direct que j'ai trouvé vient de la génération de molécules (arXiv 2604.18031).
- 10 exemples en contexte améliorent la créativité convergente mais **réduisent la créativité divergente**.
- Le domaine est éloigné du design, donc le transfert est incertain.
- Source : https://arxiv.org/pdf/2604.18031

**Documentation Anthropic sur les prompts** [blog/doc éditeur]
- Les exemples sont « l'un des moyens les plus fiables » d'orienter le format, le ton et la structure.
- Ils doivent être **variés** « pour que Claude ne capte pas de motifs non voulus ».
- La doc recommande 3 à 5 exemples balisés `<example>`.
- Elle conseille de dire **quoi faire plutôt que quoi ne pas faire**.
- Source : https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

**L'effet « éléphant rose »** (Castricato et al. 2024) [preprint]
- Interdire un sujet à un LLM peut le rendre plus saillant. Cette formulation vient d'une revue tierce.
- Les auteurs corrigent le problème par fine-tuning, pas par prompt.
- Source : https://arxiv.org/abs/2402.07896

**Zhou et al., CHI 2024** [revue à comité de lecture]
- Des humains utilisant un générateur d'images IA étaient **plus fixés** sur l'exemple initial qu'avec une simple recherche d'images.
- Leurs idées étaient aussi moins variées et moins originales.
- Les auteurs observent un « déplacement de fixation » : on se fixe sur les sorties de l'IA.
- Source : https://arxiv.org/abs/2403.11164

**Lacune importante.** Je n'ai trouvé **aucune étude** qui reproduise le paradigme de Jansson & Smith *sur le LLM lui-même* : un exemple dans le contexte, puis une mesure de la recopie de ses traits par le modèle. L'ancrage des LLM sur les exemples visuels ou de code reste donc **inféré**, pas mesuré.

---

## 4. Convergence des interfaces générées par IA

**Billet Anthropic du 12/11/2025** (« Improving frontend design through Skills ») [blog éditeur, lu]
- Il nomme le phénomène « distributional convergence ».
- Par défaut, les modèles produisent : Inter, des dégradés violets sur fond blanc et peu d'animation.
- Ce qui a été fait :
  - des principes par axe (typographie, couleur/thème, mouvement, fonds) ;
  - une liste « à éviter » ;
  - l'instruction « varier clair/sombre, polices, esthétiques » ;
  - éviter les deux extrêmes, notamment le « hardcoding » de codes hex précis.
- Le texte reconnaît : « You still tend to converge on common choices (Space Grotesk, for example) across generations ».
- Or Space Grotesk figure dans la liste de polices **suggérées** par ce même prompt.
- Le billet ne publie **aucune mesure quantitative**.
- Sources : https://claude.com/blog/improving-frontend-design-through-skills ; prompt reproduit dans la doc (lien ci-dessus).

**Origine « indigo » de Tailwind** [avis de praticien]
- Adam Wathan aurait admis qu'indigo-500 était un choix par défaut des démos Tailwind UI.
- Cette valeur serait ensuite devenue majoritaire dans les données d'entraînement.
- C'est plausible, mais non mesuré. Je n'ai pas vu le tweet original.
- Source : https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website

---

## Implications pratiques pour un système de consignes

### A. Ce que les preuves soutiennent

1. **Un exemple unique, concret et complet est le cas le plus risqué.** Le risque augmente s'il est familier et proche du domaine (Jansson & Smith ; Purcell & Gero ; Viswanathan 2016). Côté LLM, les démonstrations transmettent surtout la forme de surface (Min 2022).
2. **Interdire ne suffit pas toujours.**
   - Chez l'humain, l'effet est mixte : Jansson & Smith constatent un échec, Chrysikou & Weisberg un succès.
   - Côté LLM, Anthropic recommande les formulations positives.
   - Côté LLM, une liste d'interdits **déplace** l'attracteur au lieu de le supprimer (l'aveu sur Space Grotesk).
3. **Le lointain et le peu commun inspirent ; le proche et le commun fixent** (Chan 2011).
4. **Le modèle converge par défaut** même sans aucun exemple (Wenger & Kenett ; Anthropic ; Verbalized Sampling). L'absence d'exemples ne protège donc pas de l'uniformité : elle laisse le mode statistique s'imposer.
5. **Les remèdes par prompt sont modestes.** Les mots « très créatif » ou une haute température aident peu. Demander **plusieurs alternatives explicites** (Verbalized Sampling) et imposer une friction avant de générer (Shin) sont les pistes les mieux étayées.

### B. Inférences (non testées directement sur des agents de design)

- Préférer les **principes et les raisons** (le « pourquoi » d'un choix) aux instances.
- Si des exemples sont nécessaires :
  - en donner **plusieurs, mutuellement contrastés**, qui divergent sur les axes à garder libres ;
  - les étiqueter « illustration d'un principe, pas modèle » ;
  - les montrer **partiels** (un fragment typographique plutôt qu'une page entière) ;
  - les choisir **éloignés** (autres cultures, médias, époques).
- Réserver les extraits de code aux **invariants techniques** : accessibilité, structure des tokens, contrat de page. Ne pas en mettre pour l'esthétique, où la recopie de surface est le risque principal.
- Ne pas nommer de polices ou couleurs « recommandées » en liste fixe, car elles deviennent les nouveaux défauts. Décrire plutôt des **critères de choix** dérivés du contexte (marque, sujet, public).
- Ajouter une étape de **divergence avant convergence** :
  1. l'agent énumère 3 à 5 directions distinctes et indique laquelle serait la plus « typique » ;
  2. il l'écarte ou la justifie ;
  3. ensuite seulement, il génère.
- Faire contrôler la recopie : comparer la sortie aux exemples fournis et aux défauts connus.
- Mesurer empiriquement avant de trancher. Générer N pages avec et sans exemples, puis comparer leur similarité (couleurs, polices, structure) : aucune étude publiée ne répond à cette question précise.

---

## Sources

**Pas ouvertes ou lues seulement en partie :** article original de Jansson & Smith ; Purcell & Gero (via source secondaire) ; PDF de Linsey 2010 (404) ; Sio et al. 2015 (introuvable) ; Cheng et al. (abstract seulement) ; tweet de Wathan.

**Design et fixation**
- https://repository.tudelft.nl/file/File_6a026941-2298-42fd-bf7a-dc08eaa73bd5
- https://www.jonkolko.com/phd/writing/25-06-12-design-fixation
- https://researchdiscovery.drexel.edu/esploro/outputs/journalArticle/Following-the-wrong-footsteps-fixation-effects/991020531858804721
- https://cognitive.designsociety.org/publication/28853/Reducing+and+Perceiving+Design+Fixation%3A+Initial+Results+from+an+NSF-Sponsored+Workshop
- https://peer.asee.org/22645.pdf
- https://edrl.engr.wisc.edu/wp-content/uploads/sites/142/2022/02/2011-jmd-distancecommonness.pdf
- https://www.lrdc.pitt.edu/Schunn/papers/fuchanetal-near-far-2013.pdf
- https://www.cambridge.org/core/product/AD93E342571AB85057D36CFD4C53EE77
- https://scholar.hit.edu.cn/en/publications/a-new-strategy-to-reduce-design-fixation-presenting-partial-photo/
- https://www.repository.cam.ac.uk/handle/1810/252511
- https://www.repository.cam.ac.uk/handle/1810/265815

**Homogénéisation des LLM**
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532
- https://arxiv.org/abs/2309.05196v3
- https://arxiv.org/abs/2402.01536v2
- https://academic.oup.com/pnasnexus/article/5/3/pgag042/8529001
- https://research.tilburguniversity.edu/en/publications/does-generative-ai-make-us-think-alike-a-systematic-review-and-me-2/
- https://arxiv.org/abs/2510.01171v3
- https://arxiv.org/html/2603.13036
- https://arxiv.org/abs/2606.00875

**Exemples few-shot et fixation assistée par IA**
- https://arxiv.org/abs/2202.12837
- https://arxiv.org/pdf/2604.18031
- https://arxiv.org/abs/2402.07896
- https://arxiv.org/abs/2403.11164

**Éditeur et praticiens**
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://claude.com/blog/improving-frontend-design-through-skills
- https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website