# Intégration des bases de la manipulation de données en Python

## Concevoir la manipulation de données comme un système

La manipulation de données en Python peut être envisagée comme un système comprenant trois étapes principales : l'entrée, le traitement et la sortie. 

![Système de manipulation de données](./ressouces/images/gta431f001.png)

L'entrée correspond à l'acquisition des données, qui peut impliquer la collecte de données à partir de différentes sources, comme des fichiers CSV, des bases de données, des API web, etc. 

Le traitement est l'étape de préparation des données, où les données sont nettoyées et transformées pour être utilisées dans des analyses ultérieures. Cela peut impliquer la gestion des valeurs manquantes, la conversion des types de données, le filtrage des données, etc. 

Enfin, la sortie est l'étape de stockage des données pour une utilisation future, qui peut impliquer l'enregistrement des données préparées dans un format approprié pour une utilisation ultérieure, comme un fichier CSV, une base de données ou un fichier pickle. Cette étape permet de sauvegarder le travail effectué lors de la préparation des données et de faciliter l'accès aux données préparées pour des analyses ultérieures.

## Résoudre le problème à partir du besoin (la finalité)

Dans le domaine de la manipulation de données, il est essentiel de modéliser le problème en fonction du besoin final de la personne utilisatrice. Cette approche, qui consiste à définir clairement ce que l'on cherche à accomplir avec les données avant de commencer à les collecter, préparer ou stocker, est une étape préliminaire indispensable.

La modélisation du problème en fonction du besoin peut impliquer la définition d'objectifs spécifiques soit des données à utiliser ou de l'analyse à produire. On retrouvera parfois des indications comme une liste de champs de données précise, une liste de valeurs attendues, une liste de valeurs à ignorer, etc. Dans d'autres situations, on pourra avoir des indications sur le type d'analyse à produire, comme l'identification de tendances, la prédiction de résultats futurs, la résolution de problèmes spécifiques, etc.

Comme spécialiste de la manipulation de données, ou ingénieur de données, il est important de comprendre clairement ce que l'on cherche à accomplir avec ces données. Cela peut impliquer la définition de types de données spécifiques, de formats de données, de structures de données, des périodes temporelles ou une portée spécifique, etc.

Cette compréhension claire du besoin final aide à orienter toutes les étapes de la manipulation de données. Elle s'assure que les efforts sont concentrés sur la collecte des données appropriées, leur préparation de manière à répondre aux besoins spécifiques, et leur stockage de manière à faciliter l'analyse et l'utilisation ultérieures.

Les questions typiques à se poser pour modéliser le problème en fonction du besoin sont :

- Quels sont les objectifs spécifiques de l'analyse des données ?
- Quelles sont les données nécessaires pour atteindre ces objectifs ?
- Quels sont les formats, les structures et les types de données nécessaires ?
- Quelles sont les contraintes et les exigences spécifiques pour la collecte, la préparation et le stockage des données ?
- Quelles sont les attentes en termes de qualité, de précision et de fiabilité des données ?

Le plan de travail qui en découle permet de planifier et documenter les étapes de la manipulation, dont :

- Le format des données à la sortie, ex. CSV, Excel, JSON, etc.
- Les champs de données à inclure dans la sortie, ex. titre, date, prix, etc.
- La structure des données à la sortie, ex. tableau, liste, dictionnaire, etc.
- Les tests à effectuer pour valider la qualité des données, ex. valeurs manquantes, valeurs aberrantes, etc.
- Les étapes de préparation des données, ex. nettoyage, transformation, etc.
- Les sources de données à utiliser, ex. fichiers locaux, bases de données, API web, etc.

Plus la tâche est complexe, plus la modélisation du problème en fonction du besoin est importante et détaillée. Un exemple de documentation de cette modélisation est présenté dans le [fichier Excel](./ressources/fichier/gta431_modele_exemple.xslx) ci-joint. Il n'y a pas d'obligation de formaliser la modélisation du problème en fonction du besoin, mais c'est une pratique recommandée qui permet d'optimiser le processus de manipulation de données et d'obtenir des résultats pertinents.

La modélisation du problème en fonction du besoin permet d'assurer que le processus de manipulation de données est efficace, ciblé et conduit à des résultats significatifs et utiles. C'est une pratique recommandée qui permet d'optimiser le processus de manipulation de données et d'obtenir des résultats pertinents.

## Acquérir les données

La modélisation du problème de manipulation de données en fonction du besoin suit les pratiques de rétroingénierie. On part de la fin pour identifier la séquence de travail, puis on exécute les tâches une à une à partir de la première étape : l'acquisition des données. 

L'acquisition de données est abordée dans l'unité de formation [Acquisition de données](./ressources/unites/gta431_aquisition.md). Elle est une étape cruciale dans le processus de manipulation de données.