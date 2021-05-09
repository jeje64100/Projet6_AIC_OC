# Module de téléchargement
# Jerome MARTIQUET v1.0
# Ce module a pour rôle de télécharger des données et de les enregistrer dans un fichier.

# Importation de la fonction tqdm  du module tqdm, et du module requests.
from tqdm import tqdm
import requests

# Création de la fonction telechargement avec les paramètres adresse(du téléchargement)
# et nom (nom du fichier créé avec les données du téléchargement).
def telechargement(adresse, nom):
	try:
		url=adresse
		response = requests.get(url, stream=True)

		with open(nom, "wb") as fichier:
			for data in tqdm(response.iter_content()):
				fichier.write(data)
		fichier.close()

# Gestion d'erreur s'il l'url ne commence pas par http ou https.
	except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema):
		print("L'url ne commence pas par http:// ou https:// :\n",url)
		return exit(4)

# Gestion d'erreur en cas de problèmes de connexion.
	except requests.exceptions.ConnectionError:
		print("Impossible d'établir une connexion", "\nURL inconnue",url,"\nou vérifiez votre connexion")
		return exit(5)
