# Design Governance V1 : poids de la gouvernance et créativité. Synthèse de recherche

**Étiquettes de preuve.** [DOC] désigne une documentation officielle (Anthropic, GOV.UK, Carbon). [PR] désigne un article évalué par les pairs : revue, ou conférence ACL/TACL/EMNLP. [PRE] désigne un preprint ou un rapport technique non évalué. [PRAT] désigne un texte de praticien, un blog ou une conférence. [MES] désigne une mesure que j'ai faite moi-même le 2026-10-07 sur les fichiers bruts GitHub.

---

## 1. Ce que dit Anthropic sur les Skills, et ce que disent les études sur les contextes longs

**Taille et divulgation progressive**
- La documentation prévoit trois niveaux de chargement. Les métadonnées coûtent environ 100 tokens et sont toujours chargées. Le corps du SKILL.md est chargé au déclenchement, avec une cible « Under 5k tokens ». Les ressources ne coûtent rien tant qu'elles ne sont pas lues. [DOC] https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- Le guide de rédaction recommande : « Keep SKILL.md body under 500 lines for optimal performance ». Il demande aussi des références à **un seul niveau de profondeur** : en cas de références imbriquées, Claude peut ne lire qu'un aperçu partiel (`head -100`). Au-delà de 100 lignes, un fichier de référence doit commencer par une table des matières. [DOC] https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- La concision est un principe explicite : « The context window is a public good », et « Default assumption: Claude is already very smart ». Chaque paragraphe doit justifier son coût en tokens. [DOC] même URL.
- Le guide parle de **degrés de liberté**. Une liberté élevée convient quand plusieurs approches sont valides et que le contexte décide. Une liberté faible, avec des scripts exacts, est réservée aux opérations « fragile and error-prone ». L'image du guide oppose le « narrow bridge with cliffs » au « open field ». [DOC] même URL.
- Le guide recommande les scripts fournis avec le skill : ils sont plus fiables et seule leur sortie entre dans le contexte. Il recommande aussi les boucles « run validator → fix errors → repeat » et le schéma plan → validation → exécution. Il les réserve aux opérations par lots, destructrices ou à fort enjeu. [DOC] même URL.
- Sur l'évaluation, le guide dit « Create evaluations BEFORE writing extensive documentation ». La méthode : trois scénarios minimum, une mesure de référence sans le skill, puis « Write minimal instructions ». Il faut ensuite observer ce que l'agent lit réellement. Un fichier jamais ouvert est peut-être inutile. Un fichier relu en permanence devrait peut-être remonter dans SKILL.md. [DOC] même URL.
- Le skill officiel `skill-creator` va plus loin. Il demande d'éviter les « oppressively constrictive MUSTs ». Il demande de garder un prompt léger : « Remove things that aren't pulling their weight ». Il demande d'expliquer le pourquoi : « If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag ». [DOC/MES] https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md
- Le guide de prompting confirme ce point. Donner la motivation d'une instruction améliore les réponses. Les modèles récents sont « more responsive to the system prompt » et peuvent sur-déclencher : il faut « dial back any aggressive language ». [DOC] https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Opus 4.8 suit les instructions **plus littéralement**. Ce modèle « requires less frontend design prompting than previous models ». Le même guide observe que les consignes génériques du type « don't use cream » ne produisent pas de variété : elles déplacent le modèle vers une autre palette fixe. Deux leviers marchent mieux : une spécification concrète, ou **proposer 4 directions distinctes avant de construire**. [DOC] https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8

**Ingénierie de contexte**
- Pour Anthropic, le « context rot » et l'« attention budget » sont des contraintes réelles : « Every new token introduced depletes this budget ». L'objectif est « the smallest set of high-signal tokens ». Le bon niveau d'altitude se situe entre deux excès : la logique fragile codée en dur dans le prompt, et le flou. Il vaut mieux des **exemples canoniques** qu'une « laundry list of edge cases ». [DOC/PRAT] https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Le billet sur le skill frontend explique la « distributional convergence » : sans guidage, le modèle échantillonne au centre de haute probabilité de sa distribution. L'invite de départ faisait **environ 400 tokens**. Le billet note aussi que « too many tokens in the context window can result in degradation of performance ». [DOC/PRAT] https://claude.com/blog/improving-frontend-design-through-skills

**Données empiriques**
- *Lost in the Middle* (Liu et al., TACL 2024) trouve une courbe en U : la performance est meilleure quand l'information pertinente se trouve au début ou à la fin du contexte, et elle se dégrade au milieu. [PR] https://aclanthology.org/2024.tacl-1.9/
- *Context Rot* (Chroma, juillet 2025) a testé 18 modèles. La performance devient « increasingly unreliable as input length grows ». Un seul distracteur suffit à la dégrader. Un résultat surprenant : un texte cohérent pénalise davantage qu'un texte mélangé. [PRE] https://www.trychroma.com/research/context-rot
- *IFScale* (Distyl AI, 2025) fait varier le nombre d'instructions de 10 à 500. Les meilleurs modèles plafonnent à environ 68 % de respect à 500 instructions. Les instructions placées en premier sont favorisées. Les modèles se répartissent en trois profils de dégradation : à seuil, linéaire ou exponentiel. [PRE, listé NeurIPS 2025] https://arxiv.org/abs/2507.11538
- *Curse of Instructions* (Harada et al., attribué à ICLR 2025) trouve que le respect simultané de N instructions chute de façon quasi multiplicative. Une boucle d'auto-révision améliore nettement le résultat. **Je n'ai pas pu vérifier la source primaire**, seulement un résumé secondaire. [PRE/non vérifié] https://viblo.asia/p/the-curse-of-instructions-khi-llm-ngop-tho-vi-qua-nhieu-yeu-cau-cung-luc-ymJXDDo6Jkq
- *Let Me Speak Freely?* (Tam et al., EMNLP 2024 Industry) montre que les contraintes de format, JSON en tête, dégradent le raisonnement. Plus la contrainte est stricte, plus la dégradation est forte. La conversion en deux temps (réponse libre, puis mise en format) limite la perte. [PR] https://arxiv.org/html/2408.02442v1

## 2. La gouvernance des design systems dans les équipes humaines

- Nathan Curtis (EightShapes) distingue trois modèles d'équipe : solitaire, centralisé et fédéré. La tendance va vers le fédéré. Il juge la position d'une équipe centrale « tenuous » : à force de vouloir prouver sa valeur, elle peut desservir des équipes produit qui tiennent à leur autonomie. [PRAT] https://eightshapes.com/articles/team-models-for-scaling-a-design-system (je n'ai pas pu charger la page directement ; les citations viennent de reprises secondaires, par exemple https://articles.centercentre.com/?p=860)
- Brad Frost décrit un processus en 10 étapes. La première est d'utiliser le système. Ensuite, on contacte l'équipe et on décide s'il s'agit d'un « snowflake » propre à un produit ou d'un ajout au système. Viennent ensuite le prototype, la revue, le build, la release semver et l'adoption. Il constate que les équipes contournent le système si celui-ci ne suit pas : « the whole system risks obsolescence ». Il recommande de revoir le modèle de gouvernance régulièrement. [PRAT] https://bradfrost.com/blog/post/a-design-system-governance-process/
- GOV.UK fonctionne en deux étapes. Une proposition doit d'abord être **useful et unique**, avec des preuves d'usage. Avant publication, elle doit être **usable, consistent et versatile**. Un groupe de travail pluridisciplinaire se réunit une fois par mois pour l'examiner. [DOC] https://design-system.service.gov.uk/community/contribution-criteria ; https://design-system.service.gov.uk/community/design-system-working-group. Le design system de l'ONS publie des composants sous étiquette « Experimental » quand la recherche n'est pas encore suffisante. [DOC] https://service-manual.ons.gov.uk/community/how-to-contribute/contribution-criteria
- IBM Carbon applique un processus rigoureux pour les nouveaux composants et un processus léger pour les améliorations. L'expérimental est isolé dans **Carbon Labs**, qui a son propre dépôt et son propre Storybook, avec une voie de promotion vers le cœur du système. Un comité de pilotage assure la supervision. [DOC] https://www.carbondesignsystem.com/contributing/get-started/overview ; https://v9.carbondesignsystem.com/experimental/about
- Pour la critique de design, NN/g recommande des rôles distincts : présentateur, critique, facilitateur et rapporteur. Le périmètre et les objectifs doivent être explicites. La critique ne doit pas se transformer en séance de résolution de problèmes. Les commentaires se rattachent aux objectifs, pas aux préférences, et sont formulés comme une conversation, pas comme des directives. Les sessions restent courtes. [PRAT] https://www.nngroup.com/articles/design-critiques/
- Mark Boulton résume la tension par l'opposition « guardrails ou handcuffs » : il faut à la fois passer à l'échelle et se différencier. [PRAT] https://conffab.com/presentation/guardrails-or-handcuffs-building-creative-and-sustainable-design-systems/

## 3. Contraintes et créativité

- La source souvent présentée comme la « méta-analyse » d'Acar, Tarakci et van Knippenberg (2019, *Journal of Management* 45(1)) est en fait une **revue intégrative**, pas une méta-analyse. Elle classe les contraintes en trois catégories : **input** (ressources), **process** (règles, procédures) et **output** (spécifications du résultat). Elle propose un **effet en U inversé** sur la créativité. Pour les contraintes de processus, elle écrit que « excessive process constraints can hamper motivational processes ». Elle cite aussi un résultat sur les processus stage-gate : « Strict controls in stage-gate processes hamper project flexibility and learning » (Sethi & Iqbal, 2008). [PR] https://openaccess.city.ac.uk/id/eprint/20459/
- Patricia Stokes propose des **contraintes appariées**. Une contrainte exclut une solution habituelle, l'autre lui substitue une alternative. La contrainte la plus importante est l'objectif de nouveauté lui-même. Certaines contraintes favorisent pourtant le conformisme. [PR] https://barnard.edu/sites/default/files/inline-files/Serra2009.pdf ; https://cool.barnard.edu/pat-stokes/wp-content/uploads/2015/03/CRJ.Guston.pdf
- Pour les LLM, plusieurs travaux montrent l'effet de la structure et des contraintes :
  - *The Price of Format* (EMNLP Findings 2025) : les gabarits structurés réduisent la diversité des sorties, même à température élevée. [PR] https://arxiv.org/abs/2505.18949
  - *CS4* (2024) : quand le nombre de contraintes passe de 7 à 39, on observe un arbitrage entre respect des instructions et cohérence narrative. [PRE] https://arxiv.org/abs/2410.04197
  - Doshi et Hauser (*Science Advances*, 2024) : l'IA générative améliore la créativité individuelle mais réduit la diversité collective. [PR] https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532

## 4. Taille des skills de design comparables

Mesures [MES] faites sur raw.githubusercontent.com le 2026-10-07 :

| Skill | SKILL.md | Architecture |
|---|---|---|
| anthropics/skills `frontend-design` | 9,4 Ko, 71 lignes | Principes, processus « plan → revue → build → critique », une seule liste d'anti-modèles. « the brief's own words always win ». « Spend your boldness in one place » |
| anthropics/skills `canvas-design` | 11,9 Ko | Une « philosophie visuelle » rédigée avant de produire |
| anthropics/skills `algorithmic-art` | 19,8 Ko | |
| anthropics/skills `brand-guidelines` / `theme-factory` | 2,2 / 3,1 Ko | |
| anthropics/skills `skill-creator` | 33 Ko, 485 lignes | Méta-skill avec évaluations |
| pbakaus/impeccable v4.5 | 12,5 Ko, 87 lignes | **Modes** (Persuade, Operate, Read, Experience). Environ 20 commandes renvoyant chacune à `reference/*.md`. Lanceur script. `craft-floor.md` lu juste avant toute modification. « Verify in bounded passes, not a loop » |
| nextlevelbuilder/ui-ux-pro-max | 16 Ko | Table de priorités ; règles complètes dans `references/` interrogées par script |
| vercel-labs `web-design-guidelines` | 1,2 Ko | Récupère les règles à distance au moment de l'exécution |

Sources : https://github.com/anthropics/skills ; https://raw.githubusercontent.com/pbakaus/impeccable/main/plugin/skills/impeccable/SKILL.md ; https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md ; https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md

Avec 43 Ko, le cœur de Design Governance est environ **4,5 fois** plus gros que `frontend-design` et environ 3,5 fois plus gros qu'impeccable. Les skills comparables qui ont beaucoup de règles les placent dans des références ou des scripts, pas dans le cœur.

---

## Implications pratiques pour Design Governance

### A. Ce qui est établi par les sources
1. Anthropic vise un SKILL.md de moins de 5 000 tokens et de moins de 500 lignes, avec des références à un seul niveau de profondeur [DOC].
2. Respecter beaucoup d'instructions à la fois devient plus difficile à mesure qu'elles s'accumulent, et les instructions placées en premier sont favorisées [PRE : IFScale]. Les contenus situés au milieu d'un contexte long sont moins bien exploités [PR : Lost in the Middle].
3. Les formats imposés réduisent le raisonnement [PR : Tam] et la diversité [PR : Price of Format].
4. Les contraintes de processus ont un effet en U inversé, et les stage-gates rigides nuisent à l'apprentissage [PR : Acar et al.].
5. Les design systems humains qui tiennent dans la durée distinguent trois choses : le cœur, l'expérimental (Carbon Labs, l'étiquette « Experimental » de l'ONS) et l'exception locale (le « snowflake » de Frost). Ils révisent aussi leur gouvernance périodiquement [DOC/PRAT].
6. Les modèles récents suivent les instructions plus littéralement et ont besoin de moins de prompting frontend. Contre la convergence, ce qui marche est de proposer plusieurs directions avant de construire [DOC].

### B. Ce que j'en infère (non démontré pour ce cas précis)
1. **Le cœur est probablement trop lourd.** En français, 43 Ko représentent à peu près 11 000 à 14 000 tokens. C'est une estimation, que `count_tokens` permettrait de vérifier. On serait donc à 2 ou 3 fois la cible de 5 000 tokens. Je propose un objectif d'environ 15 à 20 Ko pour le cœur : principes, routage, définition des modes et seuil de qualité. Gates, verdicts et traces détaillées passeraient dans les références.
2. **Sortir les 220 phrases verrouillées du contexte du modèle.** Les validateurs sont un bon mécanisme, car ils s'exécutent sans entrer dans le contexte. En revanche, si ces phrases figurent aussi en toutes lettres dans le cœur, elles servent au contrôle humain et non au modèle. Il faudrait garder dans le cœur seulement les invariants vraiment critiques, comme l'accessibilité ou les engagements légaux, et en expliquer le pourquoi plutôt que l'imposer en majuscules.
3. **Graduer la gouvernance selon le mode.** Une exploration ou un brouillon passerait par une gate légère et une trace minimale. Une livraison ou un artefact public passerait par une gate complète. C'est l'équivalent agentique de la séparation entre Carbon Labs et Carbon, et de l'étiquette « Experimental ».
4. **Séparer création et conformité.** Le modèle produit d'abord en format libre, puis la run card JSON est remplie et validée dans une seconde passe. On retrouve la logique NL→format de Tam et al., et la critique de NN/g qui ne devient pas une séance de résolution.
5. **Remplacer les listes d'interdits par des contraintes appariées et des exemples canoniques.** Chaque « ne pas faire X » s'accompagnerait d'un « faire plutôt Y, parce que… », comme le propose Stokes, avec 3 à 5 exemples de référence. Ajouter une étape « proposer N directions » avant de converger.
6. **Plafonner la vérification.** Une ou deux passes bornées, sur le modèle d'impeccable, plutôt que des boucles de gates illimitées.
7. **Faire évoluer le cadre à partir des preuves.** Il faudrait des évaluations avec et sans le skill (ou avec un cœur réduit), comparant qualité, diversité entre essais et coût en tokens. Les journaux montreraient quelles références sont réellement lues. Et chaque règle nouvelle passerait un test d'entrée inspiré de GOV.UK : est-elle utile (un échec observé), unique (pas un doublon) et versatile ? Prévoir aussi une revue périodique pour retirer les règles qui ne servent pas, comme le recommande Frost.

**Mises en garde.** Le cas « Curse of Instructions » repose sur une source secondaire, et la page EightShapes n'était pas accessible directement. Aucune étude ne mesure l'effet de la gouvernance sur un skill de design en particulier : les points B.1 à B.7 sont des extrapolations à valider par vos propres évaluations.

---

## Liste complète des sources
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices [DOC]
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview [DOC]
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices [DOC]
- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-4-8 [DOC]
- https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents [DOC/PRAT]
- https://claude.com/blog/improving-frontend-design-through-skills [DOC/PRAT]
- https://raw.githubusercontent.com/anthropics/skills/main/skills/skill-creator/SKILL.md [DOC/MES]
- https://github.com/anthropics/skills (frontend-design, canvas-design, algorithmic-art, brand-guidelines, theme-factory) [MES]
- https://aclanthology.org/2024.tacl-1.9/ [PR]
- https://www.trychroma.com/research/context-rot [PRE]
- https://arxiv.org/abs/2507.11538 [PRE]
- https://viblo.asia/p/the-curse-of-instructions-khi-llm-ngop-tho-vi-qua-nhieu-yeu-cau-cung-luc-ymJXDDo6Jkq [secondaire, non vérifié]
- https://arxiv.org/html/2408.02442v1 [PR]
- https://arxiv.org/abs/2505.18949 [PR]
- https://arxiv.org/abs/2410.04197 [PRE]
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532 [PR]
- https://openaccess.city.ac.uk/id/eprint/20459/ [PR]
- https://barnard.edu/sites/default/files/inline-files/Serra2009.pdf [PR]
- https://cool.barnard.edu/pat-stokes/wp-content/uploads/2015/03/CRJ.Guston.pdf [PR]
- https://eightshapes.com/articles/team-models-for-scaling-a-design-system [PRAT] ; https://articles.centercentre.com/?p=860 [PRAT]
- https://bradfrost.com/blog/post/a-design-system-governance-process/ [PRAT]
- https://design-system.service.gov.uk/community/contribution-criteria [DOC]
- https://design-system.service.gov.uk/community/design-system-working-group [DOC]
- https://service-manual.ons.gov.uk/community/how-to-contribute/contribution-criteria [DOC]
- https://www.carbondesignsystem.com/contributing/get-started/overview [DOC]
- https://v9.carbondesignsystem.com/experimental/about [DOC]
- https://www.nngroup.com/articles/design-critiques/ [PRAT]
- https://conffab.com/presentation/guardrails-or-handcuffs-building-creative-and-sustainable-design-systems/ [PRAT]
- https://raw.githubusercontent.com/pbakaus/impeccable/main/plugin/skills/impeccable/SKILL.md [MES]
- https://raw.githubusercontent.com/nextlevelbuilder/ui-ux-pro-max-skill/main/.claude/skills/ui-ux-pro-max/SKILL.md [MES]
- https://raw.githubusercontent.com/vercel-labs/agent-skills/main/skills/web-design-guidelines/SKILL.md [MES]

Note : aucun fichier du dépôt n'a été modifié. Les fichiers téléchargés pour les mesures se trouvent dans `/tmp/claude-0/-home-user-DESIGN-GOVERNANCE1/d50555cc-e888-5d84-bb8b-64d228442ef5/scratchpad/skills/` et `/scratchpad/acar/`.