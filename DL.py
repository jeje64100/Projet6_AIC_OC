from tqdm import tqdm
import requests

def telechargement(adresse, nom):
	try:
		url=adresse
		response = requests.get(url, stream=True)

		with open(nom, "wb") as fichier:
			for data in tqdm(response.iter_content()):
				fichier.write(data)
		fichier.close()

	except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
		print("L'url ne commence pas par http:// ou https:// :\n",url)
		return exit()

	except requests.exceptions.ConnectionError:
		print("Impossible d'établir une connexion", "\nURL inconnue",url,"\nou vérifiez votre connexion")
		return exit()
