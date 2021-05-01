import mysql.connector

def creationbd(hote, admin, mdp, chemin, bd, utilbd, mdputilbd):
	try:
		mydb=mysql.connector.connect(host=hote,
				user=admin,
				password=mdp,
				unix_socket=chemin
				)
		mycursor=mydb.cursor()
		mycursor.execute("CREATE DATABASE "+bd)
		mycursor.execute("GRANT ALL privileges on "+bd+".* to "+utilbd+"@"+hote+" IDENTIFIED BY \'"+mdputilbd+"\'")
		mycursor.close()
		mydb.close()

	except mysql.connector.errors.ProgrammingError:
		print("Connexion à mysql impossible, ou l'utilisateur n'a pas les droits pour créer la base de donnée")
		return exit()

	except mysql.connector.errors.InterfaceError:
		print("Le chemin unix_socket n'est pas correct, merci de vérifier la valeur de la clé dans le fichier .yaml")
		return exit()
