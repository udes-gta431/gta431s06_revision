# Réutiliser des solutions types pour la manipulation de données

L'analyse d'un problème de manipulation comme un système de traitement de données permet de décomposer un problème complexe en sous-problèmes plus gérables, ce qui facilite la conception et l'implémentation de solutions. Cette approche systémique est particulièrement utile dans le contexte de la manipulation de données d'affaires, où les problèmes peuvent être très complexes et impliquer de grandes quantités de données. Toutefois, ceci requiert une forte capacité à modéliser le problème en fonction du besoin, à concevoir la manipulation de données comme un système, à utiliser le pseudo-code pour esquisser comment le système atteindra l'objectif et à transformer le pseudo-code en instructions Python. L'expérience rend cette tâche plus facile et rapide, mais même sans expérience il est possible de réutiliser des solutions types pour soutenir la manipulation de données.

# Réutiliser des solutions types pour des problèmes connus

## Gérer les chemins de fichiers

### Définir un chemin relatif avec pathlib

Un chemin relatif permet d'accéder à un fichier ou un répertoire en fonction du répertoire de travail actuel. Ce répertoire de travail est distinct selon l'environnement de développement utilisé ou le système d'exploitation. On peut définir la racine du répertoire de travail actuel avec `Path` de la bibliothèque `pathlib` en spécifiant le répertoire du fichier à exécuter au moyen de la variable spéciale `__file__`. Pour définir un chemin relatif, on peut `parent` et `joinpath` afin de manipuler des chemins de fichiers et de répertoires de manière plus intuitive et plus sûre que les méthodes traditionnelles.

```python
# Définir un chemin relatif avec pathlib
from pathlib import Path

# . désigne le répertoire de travail actuel (le répertoire où le script Python est exécuté)
# .. désigne le répertoire parent du répertoire de travail actuel
# Dans Pycharm, le répertoire de travail actuel est le répertoire du fichier exécuté, dans VSCode, c'est le répertoire racine du projet

# Définir le répertoire de référence (le répertoire où le script Python est stocker)
repertoire_travail = Path(__file__).parent # __file__ est une variable spéciale qui contient le chemin du fichier actuel

# On peut utiliser parent pour remonter d'un niveau et joinpath pour descendre d'un niveau

# Chemin relatif vers un fichier
chemin_fichier = repertoire_travail.joinpath("./chemin/vers/le/fichier.txt")
print(chemin_fichier)

# Chemin relatif vers un répertoire
chemin_repertoire = repertoire_travail.joinpath("./chemin/vers/le/repertoire")
print(chemin_repertoire)
```

----------------

## Gérer des fichiers

### Lire un fichier texte
On a le choix de lire un fichier texte en entier, ligne par ligne ou en liste de lignes. Il est important de choisir la méthode appropriée au besoin et au contexte de la tâche.

```python
# Lire un fichier texte
with open("chemin/vers/le/fichier.txt", "r") as fh:
    contenu = fh.read()
    # liste = fh.readlines()
    # lighe = fh.readline()
    print(contenu)  # ou liste ou ligne
```


### Lire un fichier CSV

On peut lire un fichier CSV avec la bibliothèque `csv` de Python. On utilise alors un lecteur CSV pour lire chaque ligne du fichier une à une.

```python
# Lire un fichier CSV
import csv
with open("chemin/vers/le/fichier.csv", "r") as fh:
    lecteur = csv.reader(fh)
    for ligne in lecteur:
        print(ligne)
```

### Lire un fichier JSON

On peut lire un fichier JSON avec la bibliothèque `json` de Python. On utilise alors la fonction `load` pour lire le contenu du fichier en entier dans un dictionnaire ou une liste.

```python
# Lire un fichier JSON
import json
with open("chemin/vers/le/fichier.json", "r") as fh:
    contenu = json.load(fh)
    print(contenu)
```

----------------

## Gérer des listes

### Accéder aux éléments d'une liste

On accède à un élément d'une liste en utilisant son index. L'indexation des listes commence à 0.

```python
# Accéder à un élément d'une liste
liste = [1, 2, 3, 4, 5]

# Accéder au premier élément
premier_element = liste[0]

# Accéder au dernier élément
dernier_element = liste[-1]

# Accéder à une tranche de la liste
sous_liste = liste[1:3]  # [2, 3]
```

### Ajouter des éléments à une liste

On ajoute des éléments à une liste en utilisant la méthode `append` pour ajouter un élément à la fin de la liste ou la méthode `insert` pour ajouter un élément à un index spécifique.

```python
# Ajouter des éléments à une liste
liste = [1, 2, 3, 4, 5]

# Ajouter un élément à la fin de la liste
liste.append(6)

# Ajouter un élément à un index spécifique
liste.insert(2, 7)  # [1, 2, 7, 3, 4, 5, 6]
```

### Retirer des éléments d'une liste

On retire des éléments d'une liste en utilisant la méthode `remove` pour retirer un élément spécifique ou la méthode `pop` pour retirer un élément à un index spécifique.

```python
# Retirer des éléments d'une liste
liste = [1, 2, 3, 4, 5]

# Retirer un élément spécifique
liste.remove(3)  # [1, 2, 4, 5]

# Retirer un élément à un index spécifique en obtenant sa valeur
element_retire = liste.pop(2)  # [1, 2, 5]
```

### Remplacer des éléments d'une liste

On remplace des éléments d'une liste en utilisant l'index de l'élément à remplacer.

```python
# Remplacer des éléments d'une liste
liste = [1, 2, 3, 4, 5]

# Remplacer un élément à un index spécifique
liste[2] = 7  # [1, 2, 7, 4, 5]
```

### Trier une liste

On trie une liste en utilisant la méthode `sort` pour trier la liste en place ou la fonction `sorted` pour trier la liste sans modifier l'original.

```python
# Trier une liste
liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

# Trier la liste en place
liste.sort()  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

# Trier la liste sans modifier l'original
liste_triee = sorted(liste)  # [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

### Fusionner des listes

On fusionne des listes en utilisant l'opérateur `+` pour concaténer les listes ou la méthode `extend` pour ajouter les éléments d'une liste à une autre.

```python
# Fusionner des listes
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]

# Concaténer les listes
liste_fusionnee = liste1 + liste2  # [1, 2, 3, 4, 5, 6]

# Ajouter les éléments de liste2 à liste1
liste1.extend(liste2)  # [1, 2, 3, 4, 5, 6]
```

### Itérer sur une liste

On itère sur une liste en utilisant une boucle `for` pour accéder à chaque élément de la liste.

```python
# Itérer sur une liste
liste = [1, 2, 3, 4, 5]

# Afficher chaque élément de la liste
for element in liste:
    print(element)
```

On peut également définir un index pour chaque élément de la liste en utilisant la fonction `enumerate`.

```python
# Itérer sur une liste avec un index
liste = [1, 2, 3, 4, 5]

# Afficher chaque élément de la liste avec son index
for index, element in enumerate(liste):
    print(f"Index : {index}, Élément : {element}")
```

----------------

## Gérer des dictionnaires

### Accéder à un élément d'un dictionnaire 

On accède à un élément d'un dictionnaire en utilisant sa clé.

```python
# Accéder à un élément d'un dictionnaire
dictionnaire = {"nom": "Jean", "age": 30, "ville": "Montréal"}

# Accéder à la valeur associée à la clé "nom"
valeur = dictionnaire["nom"]  # "Jean"
```

### Ajouter un élément à un dictionnaire

On ajoute un élément à un dictionnaire en utilisant une nouvelle clé.

```python
# Ajouter un élément à un dictionnaire
dictionnaire = {"nom": "Jean", "age": 30, "ville": "Montréal"}

# Ajouter une nouvelle clé-valeur
dictionnaire["pays"] = "Canada"
```

### Retirer un élément d'un dictionnaire

On retire un élément d'un dictionnaire en utilisant la méthode `pop` pour retirer un élément spécifique ou l'opérateur `del` pour retirer une clé spécifique.

```python
# Retirer un élément d'un dictionnaire
dictionnaire = {"nom": "Jean", "age": 30, "ville": "Montréal"}

# Retirer un élément spécifique en obtenant sa valeur
element_retire = dictionnaire.pop("age")  # 30

# Retirer une clé spécifique
del dictionnaire["ville"]
```

### Remplacer un élément d'un dictionnaire

On remplace un élément d'un dictionnaire en utilisant la clé de l'élément à remplacer.

```python
# Remplacer un élément d'un dictionnaire
dictionnaire = {"nom": "Jean", "age": 30, "ville": "Montréal"}

# Remplacer la valeur associée à la clé "age"
dictionnaire["age"] = 35
```

### Fusionner des dictionnaires

On fusionne des dictionnaires en utilisant la méthode `update` pour ajouter les éléments d'un dictionnaire à un autre.

```python
# Fusionner des dictionnaires
dictionnaire1 = {"nom": "Jean", "age": 30}
dictionnaire2 = {"ville": "Montréal", "pays": "Canada"}

# Ajouter les éléments de dictionnaire2 à dictionnaire1
dictionnaire1.update(dictionnaire2)
```

### Accéder à l'ensemble des clés ou des valeurs d'un dictionnaire

On accède à l'ensemble des clés ou des valeurs d'un dictionnaire en utilisant les méthodes `keys` ou `values`.

```python
# Accéder à l'ensemble des clés ou des valeurs d'un dictionnaire
dictionnaire = {"nom": "Jean", "age": 30, "ville": "Montréal"}

# Accéder à l'ensemble des clés
cles = dictionnaire.keys()  # ["nom", "age", "ville"]

# Accéder à l'ensemble des valeurs
valeurs = dictionnaire.values()  # ["Jean", 30, "Montréal"]
```

### Itérer sur un dictionnaire

On itère sur un dictionnaire en utilisant une boucle `for` pour accéder à chaque clé et valeur du dictionnaire.

```python
# Itérer sur un dictionnaire
dictionnaire = {"nom": "Jean", "age": 30, "ville": "Montréal"}

# Afficher chaque clé et valeur du dictionnaire
for cle, valeur in dictionnaire.items():
    print(f"Clé : {cle}, Valeur : {valeur}")
```


