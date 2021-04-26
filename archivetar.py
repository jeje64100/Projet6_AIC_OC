import tarfile

def desarchivage(nom, chemin):
	with tarfile.open(nom) as archive:
		archive.extractall(path=chemin)
	archive.close()

