# Aquérir les données pour l'analytique d'affaires

L'acquisition de données est une étape fondamentale dans le processus de manipulation de données et sa complexité peut varier considérablement en fonction des besoins spécifiques du projet. Au niveau le plus simple, l'acquisition de données peut impliquer la lecture de données à partir de fichiers locaux, tels que des fichiers CSV ou Excel. Cela peut être réalisé en utilisant le langage natif Python ou des bibliothèques Python standard comme `pandas`. 

À un niveau intermédiaire, l'acquisition de données peut nécessiter l'interaction avec des bases de données, ce qui peut impliquer l'utilisation de bibliothèques spécifiques pour se connecter à la base de données, exécuter des requêtes SQL et récupérer les résultats. Les bibliothèques populaires pour cette tâche incluent `sqlite3`, `psycopg2` et `sqlalchemy`.

Enfin, au niveau le plus complexe, l'acquisition de données peut impliquer l'interaction avec des API web pour récupérer des données en temps réel, ou l'utilisation de techniques de web scraping pour extraire des données à partir de pages web. Ces méthodes nécessitent une compréhension plus approfondie des protocoles HTTP, de la structure des documents HTML et de l'utilisation de bibliothèques spécifiques comme `requests` ou `beautifulsoup`. 

Dans tous les cas, l'objectif est de récupérer des données de manière efficace et fiable pour les préparer à l'analyse ultérieure.


## Acquérir les données à partir de fichiers locaux

Lire des fichiers locaux est une tâche courante dans la manipulation de données. Cela permet de récupérer des données stockées dans des fichiers CSV, Excel, JSON, etc. et de les charger dans un format adapté à l'analyse. Pour y arriver, la personne experte en manipulation de données doit se poser différentes questions, comme "est-ce que ce sont les bons fichiers ?", "est-ce que les fichiers sont bien formatés ?", "est-ce que les fichiers sont bien structurés ?", etc.

Voici une séquence typique de tâches pour acquérir des données à partir de fichiers locaux :

- Identifier les fichiers appropriés à lire ;
- Vérifier que les fichiers sont bien formatés (ex. la virgule est-elle le séparateur de champ ?) ;
- Vérifier que les fichiers sont bien structurés (ex. les en-têtes de colonnes sont-elles présentes ?) ;
- Choisir la méthode de lecture appropriée (ex. `readline()`, `readlines()`, `read()`, `json.load()`, `csv.reader()`, `pandas.read_csv()`, `pandas.read_excel()`, etc.) ;
- Charger les données dans un format adapté à l'analyse (ex. une liste, un dictionnaire, un dataframe, etc.).

Il faut généralement accéder aux données et les visualiser pour comprendre leur structure et leur contenu. Cela permet de planifier l'acquisition des données avec les bons opérateurs. Pour des fichiers volumineux, il est recommandé de lire un échantillon des données pour valider la qualité des données avant de les charger complètement. On peut aussi avoir recours à la documentation des données pour comprendre leur structure et leur contenu avant l'acquisition.

### Acquérir des données au format texte

Les fichiers texte sont l'un des formats de données les plus courants dans la manipulation de données. Les fichiers texte sont souvent utilisés pour stocker des données structurées ou semi-structurées, comme des données tabulaires, des données séquentielles, des données hiérarchiques, etc. Ils peuvent être stockés dans des formats variés, tels que CSV, JSON, XML, etc. et peuvent être lus en utilisant des méthodes de lecture de fichiers standard en Python ou des bibliothèques spécialisées. 

 L'acquisition de données à partir de fichiers texte implique de connaître le format et la structure exact de stockage des données et de choisir la méthode de lecture appropriée pour extraire les données dans un format adapté au besoin d'affaires. Les méthodes `readline()`, `readlines()` et `read()` sont souvent utilisées. Le choix spécifique de la méthode dépend de la stratégie de traitement des données et de la taille des fichiers.

La méthode `readline()` lit une seule ligne du fichier à la fois. Elle est bien adaptée pour les fichiers de données structurées de grande taille, car elle ne charge qu'une seule ligne à la fois en mémoire. Dans ce contexte, on exécute généralement les traitements sur les données au moment de la lecture et on stocke immédiatement le résultat. Cela permet de traiter des fichiers de grande taille sans épuiser la mémoire du système. Cependant, elle nécessite une boucle pour lire toutes les lignes du fichier, ce qui peut prendre du temps.

La méthode `readlines()` lit toutes les lignes du fichier dans une liste. Elle est bien adaptée pour les fichiers de données structurées de petite à moyenne taille, car elle charge toutes les lignes en mémoire. Dans ce cas, on peut exécuter les traitements sur les données après la lecture et stocker le résultat à la toute fin du processus. Cela permet de traiter les fichiers de manière plus efficace, mais elle peut être inefficace pour les fichiers de grande taille. 

La méthode `read()` lit tout le contenu du fichier dans une seule chaîne de caractères. Ces méthodes sont utiles pour lire des fichiers texte non structuré ou semi-structuré de petite à moyenne taille, mais elles peuvent être inefficaces pour les fichiers de grande taille. La méthode `read()` est souvent utilisée pour lire des fichiers de configuration, des fichiers de log, des fichiers de données non structurées, etc. qui requièrent un traitement spécial sur des éléments spécifiques du texte. Il n'est pas rare de devoir utiliser des expressions régulières pour extraire des informations spécifiques à partir de la chaîne de caractères.

Lors de l'acquisition des données au format texte, il est parfois nécessaire d'éliminer des lignes de titres, lignes vides, des lignes mal formatées, des lignes mal encodées, etc. avant de les charger dans un format adapté à l'analyse. Cela peut être réalisé en utilisant des opérateurs de traitement de texte standard en Python.

Éliminer une ligne de titre est une tâche courante lors de l'acquisition de données à partir de fichiers texte. Les lignes de titre sont souvent utilisées pour décrire les colonnes de données dans un fichier tabulaire, mais elles ne contiennent pas de données réelles. Elles doivent être éliminées avant de charger les données dans un format adapté à l'analyse. Les approches diffèrent selon la méthode utilisée pour lire les données. Avec la méthode `readline()`, on peut simplement ignorer la première ligne lue. Avec la méthode `readlines()`, on peut supprimer la première ligne de la liste. Avec la méthode `read()`, on peut diviser la chaîne de caractères en lignes et supprimer la première ligne avec des outils avancés comme les expressions régulières. 

Éliminer une ligne vide est une autre tâche courante lors de l'acquisition de données à partir de fichiers texte. Les lignes vides sont souvent utilisées pour séparer les enregistrements dans un fichier tabulaire, mais elles ne contiennent pas de données réelles. Les approches diffèrent selon la méthode utilisée pour lire les données. Avec la méthode `readline()`, on peut simplement filtrer les lignes vides par une condition. Avec la méthode `readlines()`, on peut supprimer les éléments vides de la liste. Avec la méthode `read()`, on peut diviser la chaîne de caractères en lignes et supprimer les lignes vides avec des outils avancés comme les expressions régulières.  

Éliminer les lignes mal formatées ou mal encodées est une tâche plus complexe lors de l'acquisition de données à partir de fichiers texte. Les lignes mal formatées ou mal encodées peuvent contenir des caractères spéciaux, des caractères de contrôle, des caractères non imprimables, etc. qui peuvent interférer avec le processus de lecture des données. Une mécanique de gestion des erreurs est souvent nécessaire pour gérer ces cas comme les blocs `try` et `except` pour gérer les erreurs de lecture.

### Acquérir des données au format CSV

Le format CSV (Comma-Separated Values) est l'un des formats de données les plus courants dans la manipulation de données. Les fichiers CSV sont souvent utilisés pour stocker des données tabulaires, comme des données de feuilles de calcul, des données de bases de données, des données de rapports, etc. Ils sont stockés dans un format texte simple où les colonnes de données sont séparées par des virgules et les lignes de données sont séparées par des sauts de ligne.

Le format CSV est simple, lisible par l'humain et largement pris en charge par les outils de manipulation de données. Il est souvent utilisé pour échanger des données entre des systèmes informatiques, car il est facile à lire et à écrire. Cependant, le format CSV peut être complexe à gérer en raison de la variété des conventions de formatage, des caractères spéciaux, des caractères de contrôle, etc. qui peuvent être présents dans les fichiers CSV. De plus, il faut inférer le type de données de chaque colonne pour les charger dans un format adapté à l'analyse.

Pour simplifier l'acquisition des données au format CSV, la bibliothèque `csv` de Python offre des outils pour lire et écrire des fichiers CSV. Elle permet de lire des fichiers CSV ligne par ligne, de lire des fichiers CSV dans un format tabulaire, de lire des fichiers CSV dans un format de dictionnaire, etc. Elle offre également des outils pour écrire des fichiers CSV, pour gérer les délimiteurs de champ, pour gérer les délimiteurs de texte, pour gérer les caractères d'échappement, etc.

Les délimiteurs de champ et de texte sont des caractères spéciaux utilisés pour séparer les colonnes de données et pour encadrer les valeurs de texte dans un fichier CSV. Le délimiteur de champ est souvent une virgule, mais il peut être un point-virgule, une tabulation, un espace, etc. Le délimiteur de texte est souvent un guillemet, mais il peut être une simple citation, un crochet, un guillemet, etc. Les délimiteurs de champ et de texte peuvent être spécifiés lors de la lecture des fichiers CSV pour gérer les cas spéciaux.

Voici un exemple de ligne d'un fichier csv :

```csv
Nom,Prenom,Age,Ville
Dupont,Jean,30,Sherbrooke
Dupond,Marie,25,"Paris \"Ville lumière\""
Tremblay, "Daniel, Louis", 35, Montréal
```

Dans cet exemple, la virgule est le délimiteur de champ et le guillemet est le délimiteur de texte. Certaines valeurs de texte sont encadrées par des guillemets pour tenir compte des valeurs de texte contenant des caractéres spéciaux comme des virgules, des sauts de ligne, des doubles citations, etc. qui peuvent interférer avec le processus de lecture des données. 

Les caractères d'échappement sont des caractères spéciaux utilisés pour désactiver l'effet, ou échapper, des delimiteurs de champ et de texte dans un fichier CSV. Ils sont souvent utilisés pour gérer les cas où les délimiteurs de champ et de texte sont présents dans les valeurs de texte. Les caractères d'échappement peuvent être spécifiés lors de la lecture et l'écriture des fichiers CSV pour gérer les cas spéciaux. Dans cet exemple, le caractère d'échappement est la barre oblique inversée. Il indique que le guillemet suivant n'est pas un délimiteur de texte, mais un caractère de texte.

L'acquisition de données au format CSV implique parfois de connaître le format et la structure exacts de stockage des données. Toutefois, la bibliothèque `csv` de Python offre des outils pour gérer les cas spéciaux, pour inférer le type de données de chaque colonne et pour gérer les erreurs de lecture, ce qui facilite l'acquisition des données dans ce format.

La bibliothèque `csv` utilise un "lecteur" qui exige de lire les données du fichier ligne par ligne. Contrairement aux méthodes `readline()`, `readlines()` et `read()` qui lisent le contenu du fichier en mémoire, le lecteur CSV ne stocke pas le contenu, mais donne accès à une ligne à la demande. L'exemple suivant montre comment lire un fichier CSV ligne par ligne avec un lecteur de la bibliothèque `csv` :

```python
# Lecture d'un fichier CSV ligne par ligne avec un lecteur (reader)
import csv

with open('fichier.csv', 'r') as fh:
    lecteur = csv.reader(fh)
    for ligne in lecteur:
        print(ligne)
```

### Acquérir des données au format JSON

Le format JSON (JavaScript Object Notation) est un format de données courant dans la manipulation de données. Les fichiers JSON sont souvent utilisés pour stocker des données hiérarchiques, comme des données de configuration, des données de paramètres, des données de résultats, des données d'affaires, etc. Ils sont stockés dans un format texte simple où les données sont représentées sous forme de paires clé-valeur, de listes ordonnées, de dictionnaires imbriqués, etc.

Le format est plus volumineux que le format CSV, mais il est plus lisible par l'humain et plus facile à gérer en raison du contexte donné par les clés et de sa structure hiérarchique. Il est souvent utilisé pour stocker des données complexes, des données non structurées, des données semi-structurées, etc. Il est largement pris en charge par les outils de manipulation de données, car il est facile à lire et à écrire. 

Pour simplifier l'acquisition des données au format JSON, la bibliothèque `json` de Python offre des outils pour lire et écrire des fichiers JSON. Les données sont généralement lues en entier (load()) dans un format de dictionnaire ou de liste.

L'acquisition de données au format JSON implique de connaître le format et la structure exacte de stockage des données dans le fichier d'origine, car il est répliqué et adapté dans le langage Python. Cette connaissance garantit que les données en mémoire pourront être adéquatement utilisées pour les traitements qui suivront.

Voici un exemple de fichier JSON :

```json
{
    "Nom": "Dupont",
    "Prenom": "Jean",
    "Age": 30,
    "Ville": "Sherbrooke"
}
```

La lecture de ce contenu produit un dictionnaire Python équivalent :

```python
dictionnaire = {
    "Nom": "Dupont",
    "Prenom": "Jean",
    "Age": 30,
    "Ville": "Sherbrooke"
}
```

Si l'on ne connait pas la structure du fichier JSON original, il est possible de parcourir les données pour en comprendre la structure. Cela peut être réalisé en utilisant des opérateurs de traitement de dictionnaire standard en Python. Par exemple, on peut afficher les clés et les valeurs du dictionnaire pour comprendre la structure et le contenu des données.

```python
# Parcourir les clés et les valeurs du dictionnaire
for cle, valeur in dictionnaire.items():
    print(cle, valeur)
```

## Conclusion

Il existe d'autres formats de fichiers locaux, comme les fichiers Excel, les fichiers XML, les fichiers YAML, etc. qui peuvent être lus en utilisant des méthodes de lecture de fichiers standard en Python ou des bibliothèques spécialisées. L'acquisition de données à partir de fichiers locaux est une tâche courante dans la manipulation de données et elle nécessite une compréhension approfondie des formats et des structures de stockage des données. Elle nécessite également des outils pour gérer les cas spéciaux, pour inférer le type de données de chaque colonne et pour gérer les erreurs de lecture.

La préparation à la lecture des données peut exiger d'ouvrir le fichier dans un éditeur de texte adaptéet de consulter le contenu pour comprendre la structure et le contenu des données. Une autre approche est de consulter la documentation des données pour comprendre la structure et le contenu des données avant de les lire. Il est également possible de lire un échantillon ou l'entièreté des données ay moyen du langage Python pour analyser la structure et de contenu et les documenter.