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
	except:
		print("Merci de vous assurez de la validité du lien de téléchargement de",nom)
		return exit()


