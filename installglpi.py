#!/usr/bin/python3

from DL import telechargement
from archivetar import desarchivage
from creationbd import creationbd
from droits import droits
from infosyaml import Fyaml
from scriptinstallglpi import install
import sys

fichier=str(sys.argv[1])
data=Fyaml(fichier)

telechargement(data["lien"], data["nomarchive"])
desarchivage(data["nomarchive"], data["pathglpi"])
creationbd(data["host"], data["user"], data["password"], data["unix_socket"], data["database"], data["databaseuser"], data["passworddatabaseuser"])
install(data["pathglpi"], data["langue"], data["host"], data["database"], data["databaseuser"], data["passworduser"])
droits(data["pathglpi"])
