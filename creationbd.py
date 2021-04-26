import mysql.connector

def creationbd(hote, admin, mdp, chemin, bd, utilbd, mdputilbd):
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


