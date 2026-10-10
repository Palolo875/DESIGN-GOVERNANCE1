# Grilles de qualité

**Statut :** grilles validées ; actualisées pour la suite de la phase 5. Elles mettent la [charte](charte.md) en critères vérifiables.

Chaque critère dit comment on le vérifie :
- **outil** : un script le mesure ;
- **lecture** : on le vérifie en lisant, avec une preuve citée ;
- **toi** : ton jugement décide.

**Verdicts possibles :** *conforme*, *à corriger*, *bloquant*. Un critère est bloquant s’il empêche le public visé d’utiliser le fichier ou s’il fait perdre du savoir.

**Seuils :** ceux marqués « indicatif » servent à repérer, pas à condamner. Les cibles chiffrées des chemins de l’agent sont fixées en phase 2, à partir des mesures de la phase 1.

---

## 1. Grille d’un fichier

Elle s’applique à chaque fichier, document ou script, pendant l’audit (phase 1), puis après chaque lot.

| # | Critère | Question | Vérification |
|---|---|---|---|
| F1 | Rôle | Les premières lignes disent-elles à quoi sert le fichier, et un seul rôle ? | lecture |
| F2 | Public | Le public visé est-il clair, et le contenu lui correspond-il ? | lecture |
| F3 | Structure | Les titres disent-ils leur contenu ? Les sections suivent-elles le même modèle ? Trois niveaux de titres au plus ? | outil (sommaire) et lecture |
| F4 | Une seule fois | Un passage est-il répété ailleurs, presque mot pour mot ou dans le fond ? | outil (recherche de passages proches) et lecture |
| F5 | Langue | Combien de codes internes sont visibles par un humain ? Un terme technique est-il défini à sa première apparition ? Cible : aucun code dans un fichier pour humains. | outil (comptage des codes) et lecture |
| F6 | Phrases | Quelle est la longueur moyenne des phrases ? Quelle part dépasse 40 mots ? (indicatif) | outil |
| F7 | Liens | Les liens et renvois mènent-ils quelque part ? | outil (contrôle existant) |
| F8 | Longueur | La longueur convient-elle à l’usage ? Une entrée se lit en quelques minutes ; une section de référence se comprend ouverte seule. | outil (taille par section) et lecture |
| F9 | Limites | Ce qui n’est pas vérifié est-il dit une fois par sujet, au bon endroit ? | outil (comptage) et lecture |
| F10 | Exemples | Contient-il un exemple que l’agent recopierait : valeur de couleur, police, mise en page type, code type ? Hors tendances datées. | outil (contrôle existant des mots de tendance) et lecture |
| F11 | Vestiges | Renvoi vide, fichier-pointeur, nom de révision de travail, mention d’un état passé ? | outil et lecture |
| F12 | Dépendances | Sait-on qui le cite, ce qu’il cite, et quel contrôle le protège ? | outil (carte des dépendances) |
| F13 | Fond protégé | Chaque règle et chaque élément de savoir figurent-ils dans la table de correspondance ? | outil (phases 3 et suivantes) |

**Pour les scripts**, F5, F6 et F10 sont remplacés par trois critères :
- **utilité** : à quoi sert-il pour un public, et qui l’appelle ;
- **simplicité** : pourrait-il faire la même chose en plus court ;
- **messages** : ses erreurs disent-elles quoi faire, en langage clair.

## 2. Grille du système

Elle s’applique à l’ensemble : à l’audit, à la fin de chaque phase et avant l’emballage.

| # | Critère | Question | Vérification | Valeur de départ |
|---|---|---|---|---|
| S1 | Portes | Chaque public a-t-il une entrée unique, à un clic du README ? | lecture | une seule entrée, commune |
| S2 | Charge de l’agent | Combien de caractères l’agent lit-il avant de produire, pour une petite correction, une page, un produit livré ? Le noyau commun et la lecture inutile s’allègent sans retirer une activation utile. Les caractères lus, les jetons et la durée sont des mesures distinctes ; toute augmentation est expliquée avec son effet attendu. | outil | page en direction : environ 80 000 ; les autres sont mesurés en phase 1 |
| S3 | Entrée débutant | Se lit-elle en cinq minutes, soit environ 6 000 caractères (indicatif) ? Sans code interne ? | outil et lecture | à mesurer |
| S4 | Trouvabilité | Le lecteur trouve-t-il la bonne route ? Testé sur le jeu actuel et sur un second jeu bâti avant les changements, à partir du vocabulaire d’un humain et non des alias. | outil | 98 termes sur 121, rang médian 1 ; second jeu à créer |
| S5 | Navigation | Toutes les routes sont-elles atteignables depuis l’entrée ? En combien d’étapes au plus ? | outil | 71 sur 71 ; étapes à mesurer |
| S6 | Vocabulaire | Un terme a-t-il un seul sens, et une notion un seul terme ? | outil (table du vocabulaire) et lecture | à établir en phase 2 |
| S7 | Rien de perdu | Chaque élément est-il placé, ou son retrait validé ? Cible : 100 %. | outil | à construire en phase 2 |
| S8 | Contrôles | Chaque contrôle protège-t-il un défaut identifié et échoue-t-il quand on le réintroduit ? Les doublons sont retirés ; le nombre total n’est pas un objectif. | outil | à inventorier en phase 1 |
| S9 | Gouvernance adaptée | Les contrôles et la trace suivent-ils le risque, la décision et les besoins de reprise ou d’acceptation, sans imposer une formalité inutile ? | outil (suivi des renvois) | non : les deux sont mêlés |
| S10 | Opérable | Fonctionne-t-il sans navigateur, en le disant ? Sans réseau ? Avec Python seul ? Installé depuis le zip ? | outil (installation de test) | Python seul : oui ; installation depuis le zip : à tester |
| S11 | Deux langues | Les deux versions ont-elles les mêmes sections, routes et liens ? | outil | français seul |
| S12 | Supports | Chaque support suit-il l’identité visuelle, en clair et en sombre, lisible sur mobile, avec un équivalent écrit ? | toi et outil | carte v3 externe ; un diagramme Mermaid |
| S13 | Taille | Quelle est la taille totale et par partie ? Suivie, pas un objectif ; elle ne grossit pas sans raison. | outil | environ 630 000 caractères |

## 3. Grille d’un résultat

Elle s’applique à ce que le système produit, lors des essais de phase 5 autorisés. Ton jugement décide pour R1 à R4 et R9 ; des tests techniques réussis ne décident pas de ces critères.

| # | Critère | Question | Vérification |
|---|---|---|---|
| R1 | Direction | Peut-on dire en une phrase le parti pris de la page ? | toi |
| R2 | Propre à la demande | Sans le nom, reconnaît-on le métier et le public ? | toi |
| R3 | Variété | Les choix d’identité et la composition répondent-ils aux particularités de chaque demande ? Sur une même demande, les alternatives sont-elles distinctes et justifiées, sans exiger la différence pour elle-même ? | toi, et outil (palettes, polices et enchaînement des sections comparés) |
| R4 | Finition | La hiérarchie, la typographie, les espacements et les détails sont-ils soignés ? | toi |
| R5 | Mobile | Pas de débordement ? Zones tactiles suffisantes ? Lecture confortable ? | outil (vérification du rendu) |
| R6 | Produit | Les états, interactions, liens et formulaires marchent-ils ? Rien ne mène nulle part sans le dire ? | outil et lecture |
| R7 | Accessibilité de base | Contrastes, textes alternatifs, focus visible, ordre des titres ? | outil |
| R8 | Vérité | Aucune fausse preuve ? Les exemples sont-ils signalés sans encombrer ? | lecture |
| R9 | Mise en ligne | La mettrais-tu en ligne telle quelle : oui, presque ou non ? Qu’est-ce qui manque ? | toi |
| R10 | Coût | Combien de jetons et de minutes, comparés à U5 (293 000 et 341 000 jetons pour les runs qui mobilisaient tout) ? | outil |
