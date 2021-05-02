import subprocess
from crontab import CronTab

def installfi(chemin):
	subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:install", "--username", "glpi", "fusioninventory"])
	subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:activate", "fusioninventory"])

	cron=CronTab(user='www-data')
	job=cron.new(command='/usr/bin/php5 '+chemin+'/glpi/front/cron.php &>/dev/null')
	job.minute.every(1)
	cron.write()

	subprocess.run(["systemctl", "restart", "cron"])
