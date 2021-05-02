import subprocess

def installfi(chemin):
	subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:install", "--username", "glpi", "fusioninventory"])
	subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:plugin:activate", "fusioninventory"])
