# Module d'extraction d'une archive
# Jerome MARTIQUET v1.0
# Ce module effectue une extraction sur une archive vers un répertoire.

# Importation du module tarfile
import tarfile

# Création de la fonction de desarchivage avec les paramètres nom(le nom de l'archive créée par
# le module DL.py) et chemin(répertoire destinataire de l'extraction).
def desarchivage(nom, chemin):
	try:
		with tarfile.open(nom) as archive:
			archive.extractall(path=chemin)
		archive.close()

# gestion d'erreur en cas de format non pris en charge par le module tarfile.
	except tarfile.ReadError:
		print("Le format de l'archive n'est pas compatible")
		return exit(6)
