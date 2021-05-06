import subprocess

def install(chemin, langue, hote, base, user, mdp):
	try:
		cmd1=subprocess.run(["php", chemin+"/glpi/bin/console", "glpi:system:check_requirements"], stderr=subprocess.PIPE)
		cmd2=subprocess.run(["php", chemin+"/glpi/bin/console", "db:install", "--no-interaction", "--default-language="+langue, "--db-host="+hote, "--db-name="+base, "--db-user="+user, "--db-password="+mdp], stderr=subprocess.PIPE)
		cmd3=subprocess.run(["rm", chemin+"/glpi/install/install.php"], stderr=subprocess.PIPE)
		cmd1.check_returncode()
		cmd2.check_returncode()
		cmd3.check_returncode()

	except subprocess.CalledProcessError as e:
		print("une erreur est survenue:\nreturncode: ",e.returncode, "\Output: ",e.stderr.decode("utf-8"))
		return exit()
