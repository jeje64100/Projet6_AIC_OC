import subprocess
from crontab import CronTab

def installfi(chemin):

	try:
		cmd1=subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:install", "--username", "glpi", "fusioninventory"], stderr=subprocess.PIPE)
		cmd2=subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:activate", "fusioninventory"], stderr=subprocess.PIPE)
		cmd1.check_returncode()
		cmd2.check_returncode()

		cron=CronTab(user='www-data')
		job=cron.new(command='/usr/bin/php5 '+chemin+'/glpi/front/cron.php &>/dev/null')
		job.minute.every(1)
		cron.write()

	except TypeError:
		print("Le mauvais module est installé.Merci de désinstaller crontab et d'installer python-crontab")
		return exit(11)

	except subprocess.CalledProcessError as e:
		print("une erreur est survenue:\nreturncode: ",e.returncode, "\Output: ",e.stderr.decode("utf-8"))
		return exit(12)

	subprocess.run(["systemctl", "restart", "cron"])
