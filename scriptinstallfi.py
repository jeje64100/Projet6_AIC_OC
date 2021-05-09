# Module d'insatallation du plugin fusioninventory
# Jerome MARTIQUET v1.0
# Ce module a pour rôle d'installer et d'activer fusioninventory en ligne de commande,
# puis de créer un crontab pour www-data, et de relancer le service cron.

# Importation du module subprocess et de la fonction CronTab du module crontab.
import subprocess
from crontab import CronTab

# création de la fonction installfi avec le parmètre chemin.
def installfi(chemin):

	try:
		cmd1=subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:install", "--username", "glpi", "fusioninventory"], stderr=subprocess.PIPE) # Commande d'installation.
		cmd2=subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:activate", "fusioninventory"], stderr=subprocess.PIPE) # Commande d'activation.
		cmd1.check_returncode() # renvoi le returncode de la cmd1, si différent de 0 crée un sibprocess.CalledProcessError
		cmd2.check_returncode() # renvoi le returncode de la cmd2, si différent de 0 crée un sibprocess.CalledProcessError

# Création du crontab pour l'utilisateur www-data.
		cron=CronTab(user='www-data')
		job=cron.new(command='/usr/bin/php5 '+chemin+'/glpi/front/cron.php &>/dev/null')
		job.minute.every(1) # fréquence de la tâche équivalent à * * * * * .
		cron.write()

# Gestion d'erreur si le mauvais module crontab est installé.
	except TypeError:
		print("Le mauvais module est installé.Merci de désinstaller crontab et d'installer python-crontab")
		return exit(11)

# Gestion d'erreur si un objet subprocess.callesProcessError est créé.
	except subprocess.CalledProcessError as e:
		print("une erreur est survenue:\nreturncode: ",e.returncode, "\Output: ",e.stderr.decode("utf-8"))
		return exit(12)

	subprocess.run(["systemctl", "restart", "cron"]) # redémarrage du servive cron.
