import subprocess

def install(chemin, langue, hote, base, user, mdp):
	subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:system:check_requirements"])
	subprocess.run(["php", chemin+"/glpi/bin/console", "db:install", "--no-interaction", "--default-language="+langue, "--db-host="+hote, "--db-name="+base, "--db-user="+user, "--db-password="+mdp])
