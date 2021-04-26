import subprocess

def install(chemin, langue, hote, base, user, mdp):
	subprocess.run(["php", "bin/console", "glpi:system:check_requirements"])
	subprocess.run(["php", chemin+"/glpi/bin/console", "db:install", "--force", "--default-language="+langue, "--db-host="+hote, "--db-name="+base, "--db-user="+user, "--db-password="+mdp])
