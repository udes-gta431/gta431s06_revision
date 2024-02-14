## Connaître les outils pour le traitement des données

À la base, le langage Python offre quelques outils élémentaires pour manipuler les données : les variables, les boucles et les conditions. En combinant ces outils, il est possible de réaliser des traitements sur les données. Par exemple, il est possible de parcourir une liste de données, de filtrer les données selon une condition, ou de modifier les données selon un critère. Plus les manipulations sur les données sont sophistiquées, plus il la combinaison de ces outils est complexe et requiert une analyse et une conception formalisées.

Les variables en Python sont des conteneurs de stockage de données. Les boucles en Python permettent d'exécuter un bloc de code plusieurs fois. Cela peut être particulièrement utile dans l'ingénierie de données pour effectuer des opérations sur chaque élément d'un ensemble de données. Les conditions en Python permettent d'exécuter un bloc de code seulement si une certaine condition est remplie. Dans l'ingénierie de données, cela pourrait être utilisé pour filtrer les données ou pour effectuer des calculs différents en fonction des caractéristiques des données.

En combinant ces trois concepts, on peut résoudre des problèmes d'ingénierie de données plus complexes. Par exemple, on pourrait utiliser une variable pour stocker un ensemble de données, une boucle pour parcourir chaque élément de l'ensemble de données et une condition pour effectuer un calcul différent en fonction des caractéristiques de chaque élément. Comme dans l'exemple suivant : 

```python
# Objectif : classifier un titre
# Variable pour stocker l'ensemble de données
data = [120, 130, 140, 150, 160]

# Boucle pour parcourir chaque élément de l'ensemble de données
for valeur in data:
    # Condition pour effectuer un calcul différent en fonction des caractéristiques de chaque élément
    if valeur > 150:
        print(f" La titre {valeur} et considérée élevée")
    else:
        print(f" La titre {valeur} et considérée basse")
```

Dans cet exemple, le code parcourt chaque élément de l'ensemble de données et imprime un message spécifiant que la valeur est élevée, si l'élément est supérieur à 150, et basse, sinon.


### Les variables en Python

Les variables en Python sont des conteneurs de stockage de données. Elles sont utilisées pour stocker des informations qui peuvent être référencées et manipulées dans un script Python. Par exemple, dans le contexte de l'ingénierie de données, une variable pourrait être utilisée pour stocker un ensemble de données financières à analyser. Par exemple, si nous voulons stocker le prix d'une action, nous pouvons le faire comme suit :

```python
prix_du_titre = 200.5
```

Dans cet exemple, `prix_du_titre` est une variable qui stocke la valeur `200.5`.

La principale difficulté dans la définition de variables est de choisir quelle information est stockée dans quelle variable. Pour bien reconnaître les variables, il est important de choisir des noms de variables clairs et descriptifs qui reflètent le contenu de la variable. 

Enfin, une variable peut stocker une valeur simple, mais peut aussi stocker des données dans des structures de données complexes comme les listes, les ensembles, les dictionnaires ou les dataframes. Il peut alors être nécessaire de créer de nouvelles variables pour stocker des parties ou des éléments de ces structures de données complexes. 

### Les boucles en Python

Les boucles sont utilisées pour répéter une certaine action plusieurs fois. Par exemple, si nous voulons calculer le retour sur l'investissement pour une série de prix d'actions, nous pouvons utiliser une boucle `for` :

```python
# Objectif : calcul du ROI (avec dividende à 0)
titres_financiers = [
    # Chaque liste contient : Nom du titre, Prix initial de l'action, Prix final de l'action
    ["DOO", 200, 210],
    ["RY", 220, 230],
    ["ABX", 240, 250],
    # Ajoutez autant de titres que nécessaire
]
roi = []

for titre in titres_financiers:
    roi = (titre[2] - titre[1])/titre[1] * 100
    print(f"Le ROI de {titre[0]} est roi")
```

Dans cet exemple, la boucle `for` calcule le retour sur l'investissement pour chaque titre disponible.

### Les conditions en Python

Les conditions sont utilisées pour effectuer différentes actions en fonction de certaines conditions. Par exemple, si nous voulons segmenter nos clients en fonction de leur dépense annuelle, nous pouvons utiliser une condition `if` :

```python
depenses_annuelles = 1200

if depenses_annuelles > 1000:
    print("Premium Customer")
elif depenses_annuelles > 500:
    print("Regular Customer")
else:
    print("Occasional Customer")
```

Dans cet exemple, le code vérifie d'abord si la dépense annuelle est supérieure à 1000. Si c'est le cas, il imprime "Premium Customer". Si ce n'est pas le cas, il vérifie si la dépense annuelle est supérieure à 500. Si c'est le cas, il imprime "Regular Customer". Si aucune de ces conditions n'est remplie, il imprime "Occasional Customer".


### Les autres outils

Il existe d'autres outils en Python qui permettent de soutenir la manipulation des données d'affaires, comme les modules (bibliothèques), les fonctions natives ou personnalisées, les classes et les exceptions.

Les **modules** en Python sont des fichiers contenant du code Python, généralement définissant des fonctions, des classes et des variables, qui peuvent être importés et utilisés dans d'autres scripts Python. Par exemple, le module `pandas` est largement utilisé pour la manipulation de données en Python.

Les **fonctions natives** sont des fonctions intégrées dans le langage Python, comme `print()`, `len()`, `type()`, etc. Les **fonctions personnalisées** sont des fonctions définies par l'utilisateur pour effectuer une tâche spécifique. Par exemple, une fonction personnalisée peut être créée pour calculer le retour sur investissement d'un titre financier.

Les **classes** en Python sont utilisées pour créer de nouveaux types d'objets, permettant de regrouper des données et des fonctions qui les manipulent. Par exemple, une classe `TitreFinancier` pourrait être définie pour représenter un titre financier, avec des attributs pour le nom du titre, le prix de l'action et des méthodes pour calculer le retour sur investissement.

Les **exceptions** en Python sont des erreurs détectées pendant l'exécution du programme. Elles peuvent être gérées à l'aide de blocs `try`/`except`, permettant au programme de continuer à s'exécuter même en cas d'erreur. Par exemple, une exception pourrait être levée si le prix d'une action est négatif, ce qui n'est pas possible dans la réalité.

Ces outils, combinés avec les variables, les boucles et les conditions, permettent de créer des scripts Python complexes pour la manipulation et l'analyse de données d'affaires.