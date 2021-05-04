import os


def droits(chemin, uid, gid):

	try:
		path=chemin+"/glpi/"
		for root, dirs, files in os.walk(path):
			for d in dirs:
				os.chown(os.path.join(root, d), uid, gid)
			for f in files:
				os.chown(os.path.join(root, f), uid, gid)

	except PermissionError:
		print("Vous n'avez pas les droits nécesssaires, veuillez passer en root ou super-utilisateur")
		return exit()

	except TypeError:
		print("L'UID et le GID doivent être des entiers")
		return exit()

