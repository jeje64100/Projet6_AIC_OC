#!/usr/bin/python3

# Script d'installation automatique de glpi et de son plugin fusioninventory for glpi.
# Jerome MARTIQUET v1.0
# Les informations utilisées pour cette installation sont renseignées dans le fichier .yaml.
# Le programme va donc lire le fichier .yaml,télécharger l'archive de glpi et renommer le fichier téléchargé,
# désarchiver ce fichier dans un répertoire, créer une base de donnée pour glpi et un utilisateur pour cette base de donnée,
# puis installer glpi.
# Puis il va télécharcher fusininventory, renommer l'archive, la désarchiver dans le réperoire plugins de glpi, installer le plugin et enfin donner les droits
# au serveur web récursivement sur le repertoire d'installation de glpi.

# importation des modules et des fonctions nécessaires au fonctionnement
from DL import telechargement
from archivetar import desarchivage
from creationbd import creationbd
from droits import droits
from infosyaml import Fyaml
from scriptinstallglpi import install
from scriptinstallfi import installfi
import sys

# Nécessité de lancer le programme avec un argument, le fichier .yaml,
# puis ouverture du fichier avec la fonction Fyaml et affectation dans la variable data.
try:
	fichier=str(sys.argv[1])
	data=Fyaml(fichier)

# Gestion d'erreur si le script est lancé sans argument
except IndexError:
	print("Merci de renseigner le nom du fichier .yaml en argument pour lancer le script")
	exit(1)

# Appel des fonctions avec les valeurs des clés du fichier .yaml .
try:
	telechargement(data["lien"], data["nomarchive"])
	desarchivage(data["nomarchive"], data["pathglpi"])
	creationbd(data["host"], data["user"], data["password"], data["unix_socket"], data["database"], data["databaseuser"], data["passworddatabaseuser"])
	install(data["pathglpi"], data["langue"], data["host"], data["database"], data["databaseuser"], data["passworddatabaseuser"])
	telechargement(data["lienfi"], data["nomarchivefi"])
	desarchivage(data["nomarchivefi"], data["pathfi"])
	installfi(data["pathglpi"])
	droits(data["pathglpi"], int(data["uid"]), int(data["gid"]))

# Gestion d'erreur si une clé du fichier .yaml a été effacée.
except KeyError as Erreur:
	dataDefault=Fyaml("infos.yaml") # Variable servant pour pour afficher la liste des clés utilisées par le programme.
	print("La clé", Erreur,"dans le fichier",fichier,"n'existe pas","\n Rappel des clés utilisées par le programme :\n",list(dataDefault.keys()))
	exit(2)
