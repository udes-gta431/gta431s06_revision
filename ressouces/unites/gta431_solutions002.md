# Réutiliser des solutions types pour la manipulation de données

L'analyse d'un problème de manipulation comme un système de traitement de données permet de décomposer un problème complexe en sous-problèmes plus gérables, ce qui facilite la conception et l'implémentation de solutions. Cette approche systémique est particulièrement utile dans le contexte de la manipulation de données d'affaires, où les problèmes peuvent être très complexes et impliquer de grandes quantités de données. Toutefois, ceci requiert une forte capacité à modéliser le problème en fonction du besoin, à concevoir la manipulation de données comme un système, à utiliser le pseudo-code pour esquisser comment le système atteindra l'objectif et à transformer le pseudo-code en instructions Python. L'expérience rend cette tâche plus facile et rapide, mais même sans expérience il est possible de réutiliser des solutions types pour soutenir la manipulation de données.

# Réutiliser des solutions types pour des problèmes connus

### Vérifier la présence de valeur nulles, vides ou absentes

En manipulation de données, on distingue les valeurs nulles, vides et absentes. Les valeurs nulles sont des valeurs qui sont explicitement définies comme nulles (`None`). Les valeurs vide sont des valeurs qui sont définies, mais qui ne contiennent aucune donnée, comme une chaîne vide (`""`), une liste vide (`[]`), etc. Les valeurs absentes sont des valeurs qui ne sont pas définies du tout. On peut vérifier la présence de valeurs nulles ou vides dans le langage natif de Python en utilisant les opérateurs `is` et `==`. Par exemple, pour vérifier si une variable est nulle, on peut utiliser l'opérateur `is` :

```python 
# Vérifier la présence de valeur nulles, vides ou absentes dans une chaine de caractères
chaine = ""
if chaine is None:
    print("La chaine est nulle")
elif chaine == "":
    print("La chaine est vide")
else:
    print("La chaine contient des données")

# Vérifier la présence de valeur nulles, vides ou absentes dans une liste
liste = []
if liste is None:
    print("La liste est nulle")
elif liste == []:
    print("La liste est vide")
else:
    print("La liste contient des données")

# Vérifier la présence de valeur nulles, vides ou absentes dans un dictionnaire
dictionnaire = {}
if dictionnaire is None:
    print("Le dictionnaire est nul")
elif dictionnaire == {}:
    print("Le dictionnaire est vide")
else:
    print("Le dictionnaire contient des données")
```

En utilisant une boucle, il est également possible de vérifier si une liste ou un dictionnaire contient des valeurs nulles, vides ou absentes.

```python
# Vérifier la présence de valeur nulles, vides ou absentes dans une liste
liste = [1, 2, 3, None, 5]
for element in liste:
    if element is None:
        print("La liste contient une valeur nulle")
    elif element == "":
        print("La liste contient une valeur vide")
    else:
        print("La liste contient des données")

# Vérifier la présence de valeur nulles, vides ou absentes dans un dictionnaire
dictionnaire = {"cle1": 1, "cle2": None, "cle3": 3}
for cle, valeur in dictionnaire.items():
    if valeur is None:
        print(f"La clé {cle} contient une valeur nulle")
    elif valeur == "":
        print(f"La clé {cle} contient une valeur vide")
    else:
        print(f"La clé {cle} contient des données")
```

----------------

## Identifier des doublons

En affaires, on fait souvent face à des données qui contiennent des doublons. Les doublons peuvent être identifiés en utilisant des méthodes de comparaison et de tri. Par exemple, pour identifier des doublons dans une liste, on peut trier la liste et comparer les éléments consécutifs. Pour identifier des doublons dans un dictionnaire, on peut comparer les clés ou les valeurs. Voici comment identifier des doublons dans une liste et dans un dictionnaire :

```python
# Identifier des doublons dans une liste
liste = [1, 2, 3, 4, 5, 1, 6, 7, 8, 9, 2]

liste_triee = sorted(liste)
doublons = []
for i in range(len(liste_triee) - 1):
    if liste_triee[i] == liste_triee[i + 1]:
        doublons.append(liste_triee[i])

print(f"Les doublons dans la liste sont : {doublons}")

# Identifier des doublons dans un dictionnaire
dictionnaire = {"cle1": 1, "cle2": 2, "cle3": 3, "cle4": 1, "cle5": 5, "cle6": 2}

doublons_cle = []
doublons_valeur = []
cles = list(dictionnaire.keys())
valeurs = list(dictionnaire.values())

for i in range(len(cles) - 1):
    if cles[i] == cles[i + 1]:
        doublons_cle.append(cles[i])
    if valeurs[i] == valeurs[i + 1]:
        doublons_valeur.append(valeurs[i])

print(f"Les doublons dans les clés du dictionnaire sont : {doublons_cle}")  # Il ne peut y avoir des doublons dans les clés d'un même dictionnaire, mais on peut comparer les clés de deux dictionnaires et trouver les doublons. Il faudra alors adapter le code pour comparer les clés de deux dictionnaires.
print(f"Les doublons dans les valeurs du dictionnaire sont : {doublons_valeur}")
```

----------------

## Identifier des valeurs aberrantes

Une valeur aberrante est une valeur qui diffère considérablement des autres valeurs dans un ensemble de données. On peut aussi utiliser les règles d'affaires pour identifier des valeurs aberrantes. Les valeurs aberrantes peuvent aussi être identifiées en utilisant des méthodes statistiques, telles que la moyenne, l'écart-type, le quartile, ou la visualisation des données. 

Voici comment identifier des valeurs aberrantes dans une liste à partir d'une règle d'affaires :

```python
# Identifier des valeurs aberrantes dans une liste
liste = [1, 2, 3, 4, 5, 100]

# Règle d'affaires : une valeur aberrante est une valeur qui est plus grande que le double de la moyenne de la liste
moyenne = sum(liste) / len(liste)
seuil = 2 * moyenne

valeurs_aberrantes = [valeur for valeur in liste if valeur > seuil]  # [100], notez l'utilisation de la compréhension de liste
print(f"Les valeurs aberrantes dans la liste sont : {valeurs_aberrantes}")
```

----------------

## Fusionner des données

Une fusion de données consiste à combiner des données provenant de différentes sources en une seule source. Les données peuvent être fusionnées en utilisant une clé commune ou en concaténant les données ayant une structure identique. Voici comment fusionner des données en utilisant une clé commune et en concaténant les données :

```python
# Fusionner des données en utilisant une clé commune
donnees_1 = [
    ["cle1", "Ontrio", 100],
    ["cle2", "Québec", 200],
    ["cle3", "Colombie-Britannique", 300]
]
donnees_2 = [
    ["cle1", "Toronto", 1000],
    ["cle2", "Montréal", 2000],
    ["cle3", "Vancouver", 3000]
]

# On utilise une fonction pour fusionner les données afin de réutiliser la solution
def fusionner_donnees(donnees1, donnees2, cle):
    donnees_fusionnees = []
    # Itération sur le premier ensemble de données
    for ligne1 in donnees1:
        # Itération sur le second ensemble de données
        for ligne2 in donnees2:
            # Comparaison des clés
            if ligne1[cle] == ligne2[cle]:
                # Fusion des données si les clés correspondent
                donnees_fusionnees.append(ligne1 + ligne2)
    return donnees_fusionnees

donnees_fusionnees = fusionner_donnees(donnees_1, donnees_2, cle=0)
print("Premières lignes des données fusionnées :")
print(donnees_fusionnees[:5])
```



