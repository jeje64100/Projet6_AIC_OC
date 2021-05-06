import yaml

def Fyaml(fichier):
	try:
		with open(fichier, "r") as donnees:
			donnees_content=yaml.load(donnees, Loader=yaml.BaseLoader)
		return donnees_content

	except FileNotFoundError:
		print("Le fichier",fichier,"n'existe pas")
		return exit()
