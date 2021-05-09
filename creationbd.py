# Module de création de la base de donnée pour glpi
# Jerome MARTIQUET v1.0
# Ce module a pour but de se connecter à mysql, puis de créer
# une base de donnée pour glpi et un utilisateur pour cette base de donnée.

# Importation du module mysql.connector
import mysql.connector

# Création de la fonction creationdb avec les paramètres hote, admin,
# mdp, chemin,qui servent à la connexion à mysql, et les paramètres
# bd, utilbd, mdputilbd, qui servent à la création de la base de donnée
# et à l'utilisateur de cette base de donnée.
def creationbd(hote, admin, mdp, chemin, bd, utilbd, mdputilbd):
	try:
		mydb=mysql.connector.connect(host=hote, # connexion à mysql.
				user=admin,
				password=mdp,
				unix_socket=chemin
				)
		mycursor=mydb.cursor()
		mycursor.execute("CREATE DATABASE "+bd) # création de la base de donnée.
		mycursor.execute("GRANT ALL privileges on "+bd+".* to "+utilbd+"@"+hote+" IDENTIFIED BY \'"+mdputilbd+"\'") # création de l'utilisateur de la base de donnée.
		mycursor.close()
		mydb.close()

# Gestion d'erreur si l'utilisateur renseigné pour la connexion à mysql n'a pas les droits nécessaire.
	except mysql.connector.errors.ProgrammingError:
		print("Connexion à mysql impossible, ou l'utilisateur n'a pas les droits pour créer la base de donnée")
		return exit(7)

# Gestion d'erreur si le chemin renseigné pour l'unix_socket n'est pas correct.
	except mysql.connector.errors.InterfaceError:
		print("Le chemin unix_socket n'est pas correct, merci de vérifier la valeur de la clé dans le fichier .yaml")
		return exit(8)

# Gestion d'erreur si la base de donnée existe déjà.
	except mysql.connector.errors.DatabaseError:
		print("La base de donnée existe déjà, merci de l'effacer avant de relancer l'installation")
		return exit(9)
