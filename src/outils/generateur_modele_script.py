# Nom du fichier : generateur_modele_script.py
# Auteur : daniel.chamberland-tremblay@usherbrooke.ca
# Date de création : 20240123
# Description : générer le fichier de base selon les paramètres

# Section d'importation des modules
import re

from datetime import datetime
from pathlib import Path

# Variables globales
#dossier = "."
# dossier = "./../demonstrations"
dossier = "./../exercices"
# nom_fichier = 'demo004.py'
nom_fichier = 'exercices.py'
# nom_auteur = 'daniel.chamberland-tremblay@usherbrooke.ca'
nom_auteur = 'votre courriel'
date_creation = datetime.now().strftime("%Y%m%d")
description = "Consolidation des apprentisssages en manipulation de donnée"

contenu = """# Nom du fichier : {nom_fichier}
# Auteur : {nom_auteur}
# Date de création : {date_creation}
# Description : {description}

# Section d'importation des modules

# Variables globales

# Fonctions personnalisées

# Programme principal
if __name__ == "__main__":
    pass
"""

# Fonctions personnalisées
def creer_fichier(nom_fichier):
    base_path = Path(dossier).joinpath(nom_fichier)
    base_name = base_path.stem

    # Vérifiez si le fichier de base existe
    while base_path.exists():
        # Incrémentez la dernière lettre du nom de fichier
        base_name = base_path.stem

        # Vérifiez si le nom de base est vide (pas d'extension)
        ptrn = re.compile('.*?[a-z]$')
        if not ptrn.search(base_name):
            base_name = base_name + "a"
        else:
            # Récupérez la dernière lettre du nom de base
            last_char = base_name[-1]

            # Incrémente la dernière lettre
            if last_char == "z":
                base_name += "a"
            else:
                base_name = base_name[:-1] + chr(ord(last_char) + 1)

        # Remplacez le nom de fichier par le nouveau nom de base avec l'extension
        base_path = base_path.with_name(base_name + base_path.suffix)

    with open(str(base_path), "w+") as file:
        # Écrire le contenu dans le fichier
        file.write(contenu.format(nom_fichier=base_name, nom_auteur=nom_auteur, date_creation=date_creation, description=description))



# Programme principal (peut être dans un fichier distinct)
if __name__ == "__main__":
    print("Création du fichier {fichier} ou d'un dérivé incrémental.".format(fichier=nom_fichier))
    creer_fichier(nom_fichier)



