#!/usr/bin/python3

from DL import telechargement
from archivetar import desarchivage
from creationbd import creationbd
from droits import droits
from infosyaml import Fyaml
from scriptinstallglpi import install
from scriptinstallfi import installfi
import sys

try:
	fichier=str(sys.argv[1])
	data=Fyaml(fichier)

except IndexError:
	print("Merci de renseigner le nom du fichier .yaml en argument pour lancer le script")
	exit(1)

try:
	telechargement(data["lien"], data["nomarchive"])
	desarchivage(data["nomarchive"], data["pathglpi"])
	creationbd(data["host"], data["user"], data["password"], data["unix_socket"], data["database"], data["databaseuser"], data["passworddatabaseuser"])
	install(data["pathglpi"], data["langue"], data["host"], data["database"], data["databaseuser"], data["passworddatabaseuser"])
	telechargement(data["lienfi"], data["nomarchivefi"])
	desarchivage(data["nomarchivefi"], data["pathfi"])
	installfi(data["pathglpi"])
	droits(data["pathglpi"], int(data["uid"]), int(data["gid"]))

except KeyError as Erreur:
	print("La clé", Erreur, "dans le fichier .yaml n'existe pas")
	exit(2)
