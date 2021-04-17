from tqdm import tqdm
import requests

url = ""
response = requests.get(url, stream=True)

with open("glpi.tar", "wb") as fichier:
	for data in tqdm(response.iter_content()):
		fichier.write(data)

fichier.close()