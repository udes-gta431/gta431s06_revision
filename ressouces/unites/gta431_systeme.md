# Penser la manipulation de données comme un système de traitement

Penser la manipulation de données comme un système implique de considérer chaque opération de manipulation de données comme un processus avec des entrées, des traitements et des sorties. Cette approche systémique permet de décomposer un problème complexe en sous-problèmes plus gérables, facilitant ainsi la conception et l'implémentation de solutions.

**Les entrées** sont les données brutes ou prétraitées qui sont fournies au système (ou à l'opération). Dans le contexte de la manipulation de données d'affaires, les entrées pourraient être des données financières, des données de ventes, des données de clients, etc.

**Les traitements** sont les opérations effectuées sur les entrées pour produire les sorties. Ils peuvent impliquer diverses opérations, telles que le filtrage, le tri, l'agrégation, la transformation, etc. Dans le contexte de la manipulation de données d'affaires, les traitements pourraient inclure le calcul du retour sur l'investissement, la division des clients selon un critère particulier, le calcul des ventes par succursale, etc.

**Les sorties** sont les résultats des traitements. Elles peuvent prendre diverses formes, telles que des données prêtes à l'analyse, des rapports, des graphiques, des prédictions, etc. Dans le contexte de la manipulation de données d'affaires, les sorties pourraient être une liste de titres avec la valeur du retour sur l'investissement, une liste de clients segmentés et étiquettés, une prévision des ventes, etc.

Une fois que l'_objectif_ du système (de traitement) a été défini, c'est-à-dire ce que le système doit accomplir, on peut utiliser le pseudo-code pour esquisser _comment_ le système atteindra cet objectif. Le pseudo-code est une description de haut niveau utile à la conversion de l'objectif en opérations, écrite dans un langage qui peut être compris par les humains. Il sert de guide pour la transformation de l'objectif en instructions Python.


## Exemple de l'utilisation de l'analyse par système

Voici l'exemple pour une manipulation de données qui ajoute le calcul du retour sur l'investissement pour une série de titres financiers.

[![Système de manipulation de données](../images/gta431f002.png)]

Voici un exemple de pseudo-code pour un système qui calcule le retour sur l'investissement pour une série de titres financiers :

1. Définir une liste de titres financiers (entrée).
2. Pour chaque titre financier dans la liste :
   1. Calculer le retour sur l'investissement (traitement).
   2. Ajouter le retour sur l'investissement à une liste de résultats (sortie).
3. Visualiser la liste de résultats (sortie) pour validation visuelle.
4. Sauvegarder la liste de résultats (sortie).

Une fois que le pseudo-code a été défini, il peut être transformé en instructions Python. Voici comment le pseudo-code ci-dessus pourrait être traduit en Python :

```python
# Définir une liste de titres financiers (entrée) (validation visuelle par l'ouverture du fichier)
# titres_financiers = [
#     # Chaque liste contient : Nom du titre, Prix initial de l'action, Prix final de l'action
#     ["DOO", 200, 210],
#     ["RY", 220, 230],
#     ["ABX", 240, 250],
#     # Ajoutez autant de titres que nécessaire
# ]
import json

fp_titres_financiers = "data/source/finances/titres.json"

with open(fp_titres_financiers, "r") as f:
    titres_financiers = json.load(f)

# Liste pour stocker les résultats
roi = []

# Pour chaque titre financier dans la liste
for titre in titres_financiers:
    # Calculer le retour sur investissement (traitement)
    roi_titre = (titre[2] - titre[1])/titre[1] * 100
    # Ajouter le retour sur investissement à une liste de résultats (sortie)
    titre.append(roi_titre)
    roi.append(titre)

# Afficher la liste de résultats (sortie) pour validation visuelle
for r in roi:
    print(f"Le ROI de {r[0]} est {r[1]}%")

# Ajouter dans un fichier de sortie
fp_sortie = "data/source/finances/titres.json"
with open(fp_sortie, "w+") as f:
    json.dump(roi, f)
```

En pensant la manipulation de données comme un système, on peut décomposer un problème complexe en sous-problèmes plus gérables, ce qui facilite la conception et l'implémentation de solutions. Cette approche systémique est particulièrement utile dans le contexte de la manipulation de données d'affaires, où les problèmes peuvent être très complexes et impliquer de grandes quantités de données.

