from tqdm import tqdm
import requests


def telechargement(adresse, nom):
	url=adresse
	response = requests.get(url, stream=True)

	with open(nom, "wb") as fichier:
		for data in tqdm(response.iter_content()):
			fichier.write(data)
	fichier.close()


