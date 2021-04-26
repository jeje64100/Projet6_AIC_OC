import subprocess

def droits(path):
	subprocess.run(["chown", "-R", "www-data:www-data", path+"/glpi/"])
