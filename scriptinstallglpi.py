# Module d'installation de glpi en ligne de commande
# Jerome MARTIQUET v1.0
# Ce module a pour rôle d'afficher un check des pré-requis, d'installer glpi en ligne de commande,
# et une fois l'installation faite supprimer le fichier install.php .

# Importation du fichier subprocess
import subprocess

# Création de la fonction install aves les paramètres chemin, langue(la langue d'installation),
# hote, base, user, mdp.
def install(chemin, langue, hote, base, user, mdp):
	try:
		cmd1=subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:system:check_requirements"], stderr=subprocess.PIPE) # Affichage de la check list.
		cmd2=subprocess.run(["php", chemin+"/glpi/bin/console", "db:install", "--no-interaction", "--default-language="+langue, "--db-host="+hote, "--db-name="+base, "--db-user="+user, "--db-password="+mdp], stderr=subprocess.PIPE) # Ligne de commande pour l'installation de glpi.
		cmd3=subprocess.run(["rm", chemin+"/glpi/install/install.php"], stderr=subprocess.PIPE) # Suppression du fichier install.php .
		cmd1.check_returncode() # renvoi le returncode de la cmd1, si différent de 0 crée un sibprocess.CalledProcessError
		cmd2.check_returncode() # renvoi le returncode de la cmd2, si différent de 0 crée un sibprocess.CalledProcessError
		cmd3.check_returncode() # renvoi le returncode de la cmd3, si différent de 0 crée un sibprocess.CalledProcessError

# Gestion d'erreur si un objet subprocess.CalledProcessError est créé.
	except subprocess.CalledProcessError as e:
		print("une erreur est survenue:\nreturncode: ",e.returncode, "\Output: ",e.stderr.decode("utf-8"))
		return exit(10)
