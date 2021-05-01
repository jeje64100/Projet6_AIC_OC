import tarfile

def desarchivage(nom, chemin):
	try:
		with tarfile.open(nom) as archive:
			archive.extractall(path=chemin)
		archive.close()

	except tarfile.ReadError:
		print("Le format de l'archive n'est pas compatible")
		return exit()
