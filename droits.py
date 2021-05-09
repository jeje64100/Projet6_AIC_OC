# Module de gestion des droits
# Jerome MARTIQUET v1.0
# Ce module a pour but de donner les droits au serveur web(www-data) récursivement sur le répertoire de glpi.

# Importation du module os
import os

# Création de la fonction droits avec les paramètres chemin, uid(numéro
# d'utilisateur www-data) et gid(numéro du groupe www-data).
def droits(chemin, uid, gid):

	try:
		path=chemin+"/glpi/"
		for root, dirs, files in os.walk(path):
			for d in dirs: # donne les droits aux répertoires
				os.chown(os.path.join(root, d), uid, gid)
			for f in files: # donne les droits aux fichiers
				os.chown(os.path.join(root, f), uid, gid)

# Gestion d'erreur si l'utilisateur n'a pas les droits nécessaires pour utiliser chown.
	except PermissionError:
		print("Vous n'avez pas les droits nécesssaires, veuillez passer en root ou super-utilisateur")
		return exit(13)

# Gestion d'erreur si iud et gid ne sont pas des entiers.
	except TypeError:
		print("L'UID et le GID doivent être des entiers")
		return exit(14)

