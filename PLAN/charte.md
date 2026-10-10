# Charte de la refonte

**Statut :** charte validée ; actualisée pour la suite de la phase 5. Toute décision des phases suivantes doit pouvoir s’y rattacher ; en cas de conflit entre deux principes, l’ordre de la section 3 tranche.

---

## 1. Ce qu’est le système, en une phrase

Un système qui aide un humain ou un agent à produire un design beau, propre à chaque demande et de qualité pro, en dépensant l’effort là où il change le résultat.

## 2. Pour qui

| Public | Ce qu’il vient chercher | Ce que le système lui doit |
|---|---|---|
| **Débutant** ou personne sans expérience | Un bon résultat sans apprendre le système | Une entrée d’une page, sans jargon ; savoir quoi demander, quoi fournir, ce qu’il recevra, comment poursuivre |
| **Designer** | Un savoir de référence pour juger et fabriquer | Un savoir parcourable par sujet, qui explique le pourquoi, utilisable sans agent |
| **Équipe** | Travailler à plusieurs, livrer, garder une trace | Le même savoir, plus un module de gouvernance clair : qui décide, ce qui est vérifié, ce qui reste ouvert |
| **Agent** | Savoir quoi lire, quand, et quoi produire | Une skill courte, des chemins selon l’effort, des renvois précis, aucune lecture inutile |

Un même contenu sert les quatre. Ce qui change, c’est la porte d’entrée et ce qu’on montre d’abord.

## 3. Principes, par ordre de priorité

1. **Vrai et prudent.** Le système ne perd rien sans décision écrite et n’affirme pas ce qu’il n’a pas vérifié. Chaque changement passe par le même cycle : diagnostic, proposition, accord, commit annulable. *Passe avant tout le reste : un système plus beau mais qui a perdu du savoir ou qui ment sur ses preuves est un recul.*
2. **Le design au cœur.** Le savoir, la direction et les formes sont le produit. La gouvernance aide à vérifier une affirmation, protéger un risque, permettre une reprise ou préparer une acceptation. Le niveau de trace et les contrôles suivent le travail : une exploration garde une trace légère ; un travail persistant, partagé, audité ou soumis à acceptation conserve les éléments formels nécessaires. Les preuves applicables restent dues.
3. **Des résultats beaux, variés et pro.**
   - *Beau* : une direction visible, une finition soignée, une typographie et une couleur choisies.
   - *Varié* : deux demandes différentes donnent deux résultats différents. La variété vient de ce que chaque demande a de propre, pas du hasard ni d’un catalogue.
   - *Pro* : un produit qu’on pourrait mettre en ligne. Rendu vérifié sur ordinateur et sur mobile, états et interactions qui marchent, contenu crédible, accessibilité de base, composants cohérents.
4. **L’effort proportionné.** L’effort suit la demande : une petite correction prend un chemin court, une page le chemin de direction, un travail persistant, partagé, audité ou soumis à acceptation y ajoute les éléments formels nécessaires. On dépense là où ça change le résultat ; on coupe la lecture et les formalités qui ne changent rien. L’agent choisit le chemin ; personne n’a à comprendre les modes.
5. **Clair pour chaque public.** Aucun code interne dans ce que lit un humain. Des phrases courtes. Un terme technique n’est gardé que s’il appartient au métier du design, et il est défini à sa première apparition.
6. **Bien structuré et peu chargé.** Chaque fichier a un rôle, un public et une structure prévisible. Chaque chose est dite une fois, à un seul endroit. On montre d’abord l’essentiel, puis le détail sur demande.
7. **Flexible et opérable partout.** Avec ou sans navigateur, avec ou sans assets, avec Claude Code ou un autre agent. Quand un moyen manque, le système continue et dit ce qu’il n’a pas pu vérifier.
8. **Beau lui-même.** Le système a une identité visuelle propre, appliquée à sa carte, à ses schémas et à ses supports. Un schéma n’existe que s’il explique mieux que le texte, et il garde un équivalent écrit.
9. **En deux langues.** Le français est la source, l’anglais une traduction dont l’alignement est contrôlé. L’agent répond dans la langue de la personne.
10. **Honnête sans encombrer.** Les limites et ce qui n’est pas vérifié sont dits une fois, au bon endroit, pas répétés à chaque page.

## 4. Ce que l’on garde quoi qu’il arrive

- Le **savoir de design** existant. Il peut être déplacé, reformulé ou regroupé, mais pas appauvri sans décision écrite.
- Les **décisions déjà prises** :
  - construire une première proposition complète dans le même tour ;
  - pas de fausse preuve ;
  - pas d’exemples ni de code qui figent ou créent du slop ;
  - tendances visuelles datées, jamais érigées en règle ;
  - accord de la personne avant toute action irréversible.
- La **vérification du rendu réel**, dans un navigateur, sur ordinateur et sur mobile.
- Le **lecteur de routes** et la **construction de la skill à partir des sources**, adaptés à la nouvelle architecture.
- La **traçabilité** : les documents de travail restent sur `refonte`, et chaque changement du système a son commit annulable et sa fiche.

## 5. Ce que l’on s’interdit

- Supprimer ou réécrire sur une impression, sans diagnostic écrit.
- Changer le fond du savoir pendant les phases de rangement et de langue.
- Ajouter une règle, un contrôle ou un mécanisme qui ne règle pas un défaut constaté.
- Ajouter des exemples visuels ou du code type que l’agent recopierait.
- Toucher à ce qui pilote l’agent (skill, chargement, chemins) avant la phase 5.
- Lancer un run, publier ou ouvrir une PR sans ta demande.

## 6. Comment on saura que c’est réussi

Les critères vérifiables sont dans [`grilles.md`](grilles.md) :

- la **grille d’un fichier**, appliquée à chaque fichier ;
- la **grille du système**, appliquée à l’ensemble ;
- la **grille d’un résultat**, appliquée à ce que le système produit lors des essais de phase 5 autorisés, avec leurs limites déclarées.
