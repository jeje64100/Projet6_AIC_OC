from tqdm import tqdm
import requests

url = "https://github.com/glpi-project/glpi/releases/download/9.3.3/glpi-9.3.3.tgz"
response = requests.get(url, stream=True)

with open("glpi.tar", "wb") as fichier:
	for data in tqdm(response.iter_content()):
		fichier.write(data)

fichier.close()