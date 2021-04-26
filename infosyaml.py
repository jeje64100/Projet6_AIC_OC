import yaml

def Fyaml(fichier):
	with open(fichier, "r") as donnees:
		donnees_content=yaml.load(donnees, Loader=yaml.BaseLoader)
	return donnees_content
