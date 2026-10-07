# Rapport : guider un agent LLM en design visuel (boucles visuelles, évaluation et contrôles automatisés)

Légende des niveaux de preuve : **[PR]** évalué par les pairs · **[PP]** préprint · **[V]** documentation ou blog d'éditeur · **[P]** praticien ou source secondaire.

Méthode : environ 33 recherches et lectures web (octobre 2026). Quand je n'ai vu qu'un résumé ou un extrait, je le signale.

---

## 1. Comment les éditeurs guident l'IA en design front-end

**Anthropic, billet « Improving frontend design through Skills » [V]**
- Le billet attribue le rendu générique (« AI slop ») à une **convergence distributionnelle** : le modèle échantillonne les motifs les plus fréquents de ses données d'entraînement.
- Le remède proposé est un **guidage par principes**, livré sous forme de blocs de prompt balisés en XML, et non des valeurs codées en dur :
  - typographie : éviter Inter et Roboto, « Pick one distinctive font, use it decisively » ;
  - couleur : variables CSS, « Dominant colors with sharp accents outperform timid… palettes » ;
  - mouvement : un seul chargement de page orchestré ;
  - fonds : profondeur obtenue par superposition.
- Le seul élément de code est le skill `web-artifacts-builder`, qui fournit les scripts d'une pile React, Tailwind et shadcn.
- Le billet ne décrit **aucune boucle de critique visuelle ni aucune évaluation** ; il ne montre que des captures avant/après.
- Source : https://claude.com/blog/improving-frontend-design-through-skills

**Anthropic, `SKILL.md` du skill frontend-design, branche main actuelle [V]**
- Le fichier contient surtout des principes et **aucune police, palette ni gabarit** : les codes hexadécimaux cités sont des contre-exemples à éviter.
- Il demande pourtant : « Critique your own work as you build, taking screenshots to review **if your environment supports it** ».
- Il fixe un plancher qualité : responsive, focus clavier visible, reduced-motion, contraste.
- Le skill présente donc la même faille que votre système : il exige l'observation visuelle de façon conditionnelle, sans fournir l'outil.
- Source : https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md

**Anthropic, guide « Best practices » de Claude Code [V]**
- « Give Claude a check it can run: tests, a build, **a screenshot to compare** ».
- Exemple donné : « take a screenshot of the result and compare it to the original. list differences and fix them ».
- Le guide recommande un **vérificateur séparé** : « a fresh model try to refute the result, so the agent doing the work isn't the one grading it ».
- Il ajoute : « A fresh context improves code review since Claude won't be biased toward code it just wrote ».
- Il propose les Stop hooks comme porte déterministe.
- Source : https://code.claude.com/docs/en/best-practices

**OpenAI, « Designing delightful frontends with GPT-5.4 » [V]**
- Le billet mêle principes et **skill complet** (`frontend-skill`) :
  - « two typefaces max, one accent color » ;
  - « Default to cardless layouts » ;
  - « Treat the first viewport as a poster » ;
  - éviter les piles de polices par défaut.
- Il recommande des mood boards et plusieurs options visuelles avant de converger.
- Sur la vérification : « Providing a **Playwright** tool or skill significantly improves the likelihood » et « verify its work visually ».
- Ces affirmations ne sont accompagnées d'aucun chiffre publié.
- Sources : https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4 ; cookbook GPT-5, qui recommande une pile concrète (Tailwind, shadcn/ui, Radix, Lucide, Motion) : https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_frontend

**Vercel v0 [V]**
- Architecture « composite » : un modèle de base, un modèle Quick Edit et **AutoFix**.
- AutoFix (vercel-autofixer-01) corrige les **erreurs de code**, pas la qualité visuelle.
- La récupération de contexte puise dans la documentation et des « **UI examples** ».
- v0 ancre donc la génération sur des **exemples concrets** et sur la pile shadcn/Tailwind.
- Les chiffres d'AutoFix sont auto-déclarés par Vercel et Fireworks.
- Sources : https://vercel.com/blog/v0-composite-model-family ; https://fireworks.ai/blog/vercel

**Lovable [V]**
- Un « style prompt » réutilisable est enregistré dans la Knowledge du projet et injecté à chaque requête.
- Construction composant par composant.
- La fonction « Design guidance » propose **trois directions visuelles légères** ou pose des questions (typo, couleur, mise en page) avant de construire.
- Ce guidage est sauté si le brief fixe déjà polices, couleurs ou design system.
- Sources : https://docs.lovable.dev/features/design-guidance ; https://docs.lovable.dev/prompting/prompting-one

**Google** : je n'ai trouvé aucun guide officiel de design front-end pour Gemini sur ai.google.dev. Les résultats étaient tous tiers ([P]), donc rien n'est retenu ici.

**Synthèse (inférence)** : tous les éditeurs mettent des **principes** en avant. Ceux qui obtiennent un rendu cohérent ajoutent des **ressources concrètes** :
- une pile de composants imposée (v0, OpenAI) ;
- des exemples récupérés à la volée (v0) ;
- un style persistant (Lovable).

Les plus récents ajoutent une **vérification rendue** via Playwright ou capture d'écran (OpenAI, Claude Code). Aucun ne publie de mesure de l'effet de ces consignes.

---

## 2. Boucles de rétroaction visuelle pour agents qui génèrent de l'UI

**Design2Code (NAACL 2025) [PR]**
- Résultats humains : les pages générées par GPT-4V « can replace the original… in 49% of cases » et sont jugées meilleures dans 64 % des cas.
- Les modèles échouent surtout sur le **rappel des éléments visuels** et la **mise en page**.
- L'auto-révision (cible, capture du rendu précédent et code) n'aide que quelques modèles forts (GPT-4V, Claude 3). Je n'ai pas obtenu la table chiffrée.
- Sources : https://arxiv.org/abs/2403.03163v1 ; https://par.nsf.gov//servlets/purl/10591120 ; résumé [P] https://www.alphaxiv.org/overview/2403.03163

**Sansford et al., Amazon AGI, atelier ICLR 2026 [PR, atelier]**
- Pipeline : critique visuelle par VLM, puis amélioration.
- Gain de **+17,8 %** sur trois cycles (Distill-Qwen-14B) et de **+10,8 %** en auto-amélioration avec Claude 4.5 Sonnet.
- Point clé : raffiner **sans critique** (ni visuelle ni de code) ne rapporte que **+1,5 %**. C'est le retour externe qui produit le gain, pas la seconde passe.
- Validation du juge sur 200 paires WebDev Arena :
  - juge multidimensionnel : **69,5 % d'accord** avec les humains, 22 % de désaccord ;
  - juge à score unique : 48,5 % d'accord et 28,5 % d'égalités.
- Limite : les gains sont mesurés par le juge VLM lui-même, pas par des humains, et on retient la « meilleure solution » parmi les cycles.
- Source : https://cdn.amazon.science/e2/87/68ecc1e04ecc9e2e92bcd5fd3750/scipub-approval152129-45356067-visionguided-iterative-refinement-for-frontend-code-generation.pdf

**WebGen-Agent (ICLR 2026) [PR]**
- Un VLM note l'attrait visuel des captures et un agent GUI teste le fonctionnement.
- Ces scores servent de retour pas à pas et de récompense d'entraînement.
- Source : https://arxiv.org/html/2509.22644v1

**ReLook [PP]**
- Un critique MLLM est appelé comme outil.
- Les auteurs constatent qu'une révision peut **dégrader** le résultat même avec un bon retour. Ils n'acceptent donc que les étapes strictement améliorantes (« Forced Optimization »).
- Source : https://huggingface.co/papers/2510.11498.md

**UICoder (NAACL 2024) [PR]**
- Le retour automatique (compilateur et score multimodal) sert à **filtrer des données de fine-tuning** SwiftUI, pas à boucler à l'exécution.
- Il surpasse les modèles téléchargeables de référence.
- Source : https://aclanthology.org/2024.naacl-long.417

**DesignRepair (ICSE 2025) [PR]**
- Base de connaissances Material Design en deux couches (composants et système).
- Analyse du code et **analyse Playwright de la page rendue**, puis réparation par RAG.
- Le résumé fait état de gains significatifs sur la conformité aux règles de design, l'accessibilité et l'UX. Je n'ai pas vérifié les chiffres.
- Source : https://arxiv.org/abs/2411.01606

**UICrit (UIST 2024) [PR]**
- 3 059 critiques rédigées par 7 designers sur 983 UI mobiles.
- Gemini en zero-shot obtient 0,31 de qualité de commentaire, contre **0,75 pour les humains**.
- Avec 8 exemples few-shot et prompting visuel : 0,48 (le « +55 % » relatif).
- Les experts préfèrent les critiques humaines **81 %** du temps.
- Seuls 13,1 % des commentaires générés par Gemini ont été validés.
- L'accord entre experts n'est lui-même que **« fair »** (κ ≈ 0,29–0,31).
- L'étude est petite : 6 UI, 6 experts.
- Source : https://arxiv.org/html/2407.08850v3

**MLLM as a UI Judge [PP]**
- GPT-4o, Claude 3.5 Sonnet et Llama comparés à environ 500 évaluateurs MTurk sur 30 interfaces.
- Corrélations agrégées de r ≈ 0,69–0,73. Pour le facteur « Interesting », Claude atteint r = 0,85.
- La « facilité d'usage » ne corrèle pas (r ≈ −0,05).
- Préférence par paires : **≈ 60 %** globalement, ≈ 50 % quand l'écart humain est faible, ≈ 90–93 % quand il est grand.
- Conclusion des auteurs : utile en évaluation précoce et pour les gros écarts, **pas un substitut** aux humains.
- Source : https://arxiv.org/html/2510.08783v1

**ArtifactsBench [PP]**
- Juge MLLM appliqué à des captures temporelles, avec une checklist propre à chaque tâche.
- 94,4 % de cohérence de **classement de modèles** avec WebDev Arena, et jusqu'à environ 90,95 % d'accord par paires avec des experts.
- Il s'agit de classer des modèles, pas de juger un artefact isolé. Chiffres auto-déclarés.
- Source : https://arxiv.org/html/2507.04952v2

**Biais d'auto-préférence et limites de l'auto-correction**
- **Panickssery, Bowman et Feng, NeurIPS 2024 [PR]** : GPT-4, GPT-3.5 et Llama 2 favorisent leurs propres résumés. La force de ce biais est **corrélée linéairement** à leur capacité à se reconnaître. Le domaine étudié est le texte.
  - https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html
- **Xu et al., ACL 2024 [PR]** : l'auto-raffinement **amplifie** le biais en faveur de soi. Un retour externe exact et des modèles plus gros le réduisent.
  - https://aclanthology.org/2024.acl-long.826
- **Huang et al., ICLR 2024 [PR]** : sans retour externe, l'auto-correction n'améliore pas le raisonnement et le dégrade parfois.
  - https://arxiv.org/abs/2310.01798v2
- **Zheng et al., NeurIPS 2023 [PR]** : GPT-4 juge atteint plus de 80 % d'accord avec les humains sur du texte. Mais il souffre d'un **biais de position** : verdicts cohérents à 65 % seulement quand on inverse l'ordre des réponses.
  - https://arxiv.org/abs/2306.05685
- **Juges MLLM [PP]** : une étude sur le légendage d'images confirme un biais d'auto-préférence variable selon le modèle, atténué par un **ensemble de juges**. Je n'ai trouvé aucune étude sur l'auto-préférence quand un modèle juge ses **propres UI**.
  - https://arxiv.org/pdf/2604.11589

**Réponse à la question** : oui, une boucle sur captures d'écran améliore mesurablement les résultats (Sansford ; Design2Code pour les modèles forts). Mais cela tient quand la critique apporte une information **externe** :
- un rendu réel ;
- un critique distinct ou une checklist ;
- une sélection qui n'accepte que les améliorations.

Les mesures de gain reposent presque toujours sur des juges VLM, rarement sur des humains.

---

## 3. Protocoles d'évaluation légers pour un pilote

- **Préférence par paires à l'aveugle** :
  - c'est la méthode de Chatbot Arena, agrégée en Bradley-Terry ; les votes de la foule y concordent bien avec ceux des experts [PR] (https://proceedings.mlr.press/v235/chiang24b.html) ;
  - WebDev Arena l'applique déjà au web et sert de référence aux juges ci-dessus ;
  - il faut inverser l'ordre de présentation à cause du biais de position (Zheng).
- **Best-Worst Scaling** : à nombre d'annotations égal, il est **plus fiable que les échelles de notation** [PR] (https://aclanthology.org/P17-2074/). C'est utile pour comparer trois ou quatre variantes à la fois.
- **Rubrique multidimensionnelle plutôt que score global** : environ 69,5 % d'accord contre 48,5 %, et beaucoup moins d'égalités (Sansford [PR, atelier]).
- **Accord inter-évaluateurs** :
  - convention de Krippendorff : α ≥ 0,800 pour conclure, 0,667–0,800 pour des conclusions provisoires [P/secondaire] (https://en.wikipedia.org/wiki/Krippendorff%27s_alpha ; texte primaire : https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf) ;
  - l'accord entre designers experts n'est que « fair » (κ ≈ 0,3, UICrit). Il faut donc s'attendre à un plafond bas, d'où l'intérêt des paires et de plusieurs juges.

---

## 4. Contrôles automatisés pas chers ou jugement humain

- **axe-core** :
  - selon Deque, l'éditeur, environ **57 % des problèmes** (en volume) sont détectés sur plus de 2 000 audits [V] (https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues) ;
  - les règles sont conçues pour **limiter les faux positifs**.
- **Test indépendant GOV.UK (2017)** : 10 outils réunis trouvent 71 % de 143 barrières ; le meilleur outil seul, **41 %** [V/gouvernemental] (https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/).
- **Lighthouse** :
  - le score ignore les audits manuels (piège à focus, ordre visuel contre ordre du DOM) ;
  - il fonctionne en tout-ou-rien par audit [V] (https://developer.chrome.com/docs/lighthouse/accessibility/scoring).
- **Playwright `toHaveScreenshot`** :
  - utile pour la **régression** une fois une base de référence validée, pas pour juger la qualité ;
  - le rendu varie selon l'OS, le navigateur et le matériel ; il faut garder le même environnement et régler `maxDiffPixels` [V] (https://playwright.dev/docs/test-snapshots).
- **Proxys esthétiques calculables** : complexité visuelle et colorimétrie mesurées sur capture, plus la démographie, expliquent environ **la moitié de la variance** de l'attrait perçu à 500 ms (Reinecke et al., CHI 2013 [PR], https://kgajos.seas.harvard.edu/papers/reinecke13aesthetics.pdf).

**Ce qui relève du jugement humain** : hiérarchie et adéquation à la marque, facilité d'usage perçue (les MLLM n'y corrèlent pas), différences fines entre variantes proches, et environ 40–60 % des problèmes d'accessibilité.

---

## Implications pratiques

**Ce que les sources établissent**
1. Le gain d'une itération vient du **retour externe**, pas de la seconde passe : +1,5 % sans critique contre +10,8 à +17,8 % avec critique visuelle (Sansford). L'auto-correction intrinsèque est faible ou nuisible (Huang ; Xu).
2. Un LLM qui juge ses propres productions est biaisé en sa faveur, et l'auto-raffinement amplifie ce biais (Panickssery ; Xu). Anthropic recommande lui-même un vérificateur en contexte frais.
3. Les MLLM approchent les humains sur les **gros écarts** et les jugements globaux, mais restent proches du hasard sur les variantes proches et sur l'utilisabilité (MLLM as a UI Judge ; UICrit).
4. Une rubrique multidimensionnelle vaut mieux qu'un score global, et les paires ou le Best-Worst Scaling valent mieux que les échelles.
5. axe-core et Lighthouse détectent une part réelle mais partielle des problèmes d'accessibilité (≈ 41–57 %). Les captures Playwright servent la régression, pas l'esthétique.
6. Les éditeurs combinent principes, ressources concrètes (pile de composants, exemples, style persistant) et, de plus en plus, vérification par Playwright. Aucun ne publie de mesure de l'effet.

**Ce que j'en déduis (inférences, non testées)**
- **Point (a), observation visuelle sans outil** : soit fournir un outil de capture (Playwright, desktop, mobile, vue floue) et faire passer le vérificateur de rendu dans le cœur toujours lu, soit retirer les obligations visuelles et les remplacer par un « si disponible » explicite. En l'état, l'agent risque de déclarer avoir vu ce qu'il n'a pas vu.
- **Point (b), auto-évaluation** :
  - confier le jugement perceptif à un **sous-agent en contexte frais**, idéalement un autre modèle ou un ensemble de juges ;
  - le faire travailler à partir de captures réelles, avec une **rubrique multidimensionnelle** ;
  - en mode paires, inverser l'ordre de présentation ;
  - n'accepter une révision que si elle bat la précédente (logique ReLook) ;
  - garder les humains pour les arbitrages fins.
- **Point (c), aucune ressource concrète** : ajouter un petit jeu curé (quelques paires de polices sous licence libre, des palettes déjà validées en contraste, quelques gabarits ou composants de référence). L'ancrage par exemples de v0 et le style persistant de Lovable vont dans ce sens. L'effet doit être mesuré.
- **Pilote** :
  - 10 à 20 briefs, version actuelle contre version corrigée ;
  - préférence par paires à l'aveugle, 3 à 5 évaluateurs, ordre aléatoire ;
  - une rubrique courte à 4–6 dimensions ;
  - calcul du α de Krippendorff, en s'attendant à environ 0,3–0,6 pour l'esthétique ;
  - axe-core et un contrôle de débordement en porte automatique ;
  - un juge MLLM mesuré **contre** les votes humains avant de lui faire confiance.

---

## Sources
- https://claude.com/blog/improving-frontend-design-through-skills [V]
- https://raw.githubusercontent.com/anthropics/skills/main/skills/frontend-design/SKILL.md [V]
- https://code.claude.com/docs/en/best-practices [V]
- https://developers.openai.com/blog/designing-delightful-frontends-with-gpt-5-4 [V]
- https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_frontend [V]
- https://vercel.com/blog/v0-composite-model-family [V]
- https://fireworks.ai/blog/vercel [V]
- https://docs.lovable.dev/features/design-guidance [V]
- https://docs.lovable.dev/prompting/prompting-one [V]
- https://arxiv.org/abs/2403.03163v1 ; https://par.nsf.gov//servlets/purl/10591120 (Design2Code) [PR] ; https://www.alphaxiv.org/overview/2403.03163 [P]
- https://cdn.amazon.science/e2/87/68ecc1e04ecc9e2e92bcd5fd3750/scipub-approval152129-45356067-visionguided-iterative-refinement-for-frontend-code-generation.pdf [PR, atelier ICLR 2026]
- https://arxiv.org/html/2509.22644v1 (WebGen-Agent) [PR, ICLR 2026]
- https://huggingface.co/papers/2510.11498.md (ReLook) [PP]
- https://aclanthology.org/2024.naacl-long.417 (UICoder) [PR]
- https://arxiv.org/abs/2411.01606 (DesignRepair, ICSE 2025) [PR]
- https://arxiv.org/html/2407.08850v3 (UICrit, UIST 2024) [PR]
- https://arxiv.org/html/2510.08783v1 (MLLM as a UI Judge) [PP]
- https://arxiv.org/html/2507.04952v2 (ArtifactsBench) [PP]
- https://papers.nips.cc/paper_files/paper/2024/hash/7f1f0218e45f5414c79c0679633e47bc-Abstract-Conference.html (auto-préférence) [PR]
- https://aclanthology.org/2024.acl-long.826 (Pride and Prejudice) [PR]
- https://arxiv.org/abs/2310.01798v2 (auto-correction) [PR]
- https://arxiv.org/abs/2306.05685 (LLM-as-a-judge) [PR]
- https://arxiv.org/pdf/2604.11589 (biais des juges MLLM) [PP]
- https://proceedings.mlr.press/v235/chiang24b.html (Chatbot Arena) [PR]
- https://aclanthology.org/P17-2074/ (Best-Worst Scaling) [PR]
- https://en.wikipedia.org/wiki/Krippendorff%27s_alpha [P] ; https://www.asc.upenn.edu/sites/default/files/2021-03/Computing%20Krippendorff%27s%20Alpha-Reliability.pdf [primaire, seuils non vérifiés]
- https://www.deque.com/blog/automated-testing-study-identifies-57-percent-of-digital-accessibility-issues [V]
- https://accessibility.blog.gov.uk/2017/02/24/what-we-found-when-we-tested-tools-on-the-worlds-least-accessible-webpage/ [V/gouvernemental]
- https://developer.chrome.com/docs/lighthouse/accessibility/scoring [V]
- https://playwright.dev/docs/test-snapshots [V]
- https://kgajos.seas.harvard.edu/papers/reinecke13aesthetics.pdf (CHI 2013) [PR]

**Lacunes** :
- aucun guide officiel Google trouvé ;
- table chiffrée de l'auto-révision dans Design2Code non obtenue ;
- chiffres de DesignRepair non vérifiés ;
- aucune étude trouvée sur l'auto-préférence quand un modèle juge ses propres UI.