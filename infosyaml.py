# Module de lecture d'un fichier .yaml
# Jerome MARTIQUET v1.0
# Le module a pour fonction d'ouvrir et de lire un fichier .yaml,
# puis de retourner les données.

# Importation du module yaml
import yaml

# Création de la fonction Fyaml avec le paramètre fichier(argument du script installglpi.py).
def Fyaml(fichier):
	try:
		with open(fichier, "r") as donnees:
			donnees_content=yaml.load(donnees, Loader=yaml.BaseLoader)
		return donnees_content

# Gestion d'erreur si le fichier renseigné n'existe pas.
	except FileNotFoundError:
		print("Le fichier",fichier,"n'existe pas")
		return exit(3)
