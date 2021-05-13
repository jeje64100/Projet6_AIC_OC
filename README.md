# Projet6_AIC_OC
# PROGRAMME D'AUTOMATISATION DE L'INSTALLATION DE GLPI ET DU PLUGIN FUSIONINVENTORY FOR GLPI EN PYTHON
# JEROME MARTIQUET 08/05/2021 v1.0

# Ce programme à pour but d'automatiser l'installation de GLPI et de son plugin FUSIONIVENTORY FOR GLPI à destination des distributions linux.
# Le serveur destiné a recevoir cette installation doit posséder certains pré-requis, les paquets suivant doivent être installés :

# - mysql ou mysqlmariadb
# - apache2 php libapache2-mod-php (actuellement la version php installée est php 7.3)
# - php-impa php-ladp php-curl php-gd php-mysql php-cas php-xml php-intl php3.7-mbstring php-apcu
# - apcupsd

# Ce programme fonctionne sous Python3 et utilise les modules (ceux sans asterisque sont inclus de base dans python3) :
# - sys
# - yaml* (python3 -m pip install Pyyaml)
# - tqdm* (python3 -m pip install tqdm)
# - requests
# - tarfile
# - mysql.connector* (python3 -m pip install mysql-connector-python)
# - subprocess
# - crontab* (python3 -m pip insatll python-crontab)
# - os

# * afin de pouvoir installer les modules manquants installer le paquet python3-pip


# Ce programme est composé d'un script de lancement, de 7 modules et d'un fichier infos.yaml (chaque fichier est lui même commenté) :

# !!!!!!!! ATTENTION CE PROGRAMME DOIT ETRE LANCE EN MODE ROOT OU SUPER-UTILISATEUR. LE FICHIER INFOS.YAML NE DOIT PAS ETRE MODIFIE DIRECTEMENT, VOUS DEVEZ
# EN FAIRE UNE COPIE ET MODIFIER CETTE DERNIERE.!!!!!!!!!!

# - Le script de lancement, installglpi.py, doit être appelé avec un argument. Cet argument est le fichier infos.yaml où sont renseignés les éléments 
# nécessaires à l'exécution du programme. Pour rappel un fichier YAML fonctionne avec une clé(key) à la quelle on affecte une valeur(value). Les valeurs de 
# ce fichier sont renseignées par défaut. Il est fortement conseillé de modifier la valeur de la clé du mot de passe pour la création de l'utilisateur de la 
# base de donnée de glpi. Concernant les autres valeurs vous pouvez les modifier si vous le souhaitez, mais ce n'est pas une obligation, hors mis bien sûr les clés pour
# vous connecter à mysql. Pour cela vous devez avant toute modification copier le fichier infos.yaml dans un autre fichier ( vous choisirez son nom, par exemple 
# "mesinfos.yaml"). En python ce type de variable, association d'une valeur à une clé, est appelé un dictionnaire.
# Ce script utilise les 7 autres modules et leur fonctions délarées.

# - Le module infosyaml.py qui permet d'ouvrir, de lire et de renvoyer au script les clés et les valeurs du fichier passé en argument au lancement du script.

# - Le module DL.py qui permet de télécharger le fichier/archive dans le répertoire courant et de le renommer. L'adresse du lien de téléchargement 
# et le nouveau nom sont des valeurs paramétrables dans le fichier .YAML. Ce module est utilisé pour le téléchargement de l'archive de GLPI mais aussi 
# pour l'archive de FUSIONINVENTORY FOR GLPI.  

# - Le module archivetar.py qui permet l'extraction de l'archive vers un répertoire en particulier. Le chemin de ce répertoire est paramétrable dans 
# le fichier .YAML. Ce module est lui aussi utilisé pour l'archive de GLPI et celle de FUSIONINVENTORY FOR GLPI.

# - Le module creationbd.py qui permet la connexion à mysql et la création d'une base de donnée pour glpi et d'un utilisateur pour cette dernière. Pour ce
# module les valeurs utilisées dans le fichier.YAML sont l'hôte, l'utilisateur, le mot de passe et l'adresse de l'unix_socket pour se connecter à mysql
# avec le compte root (ou administrateur). Puis le nom de la base de donner à créer, son utilisateur et le mot de passe de ce dernier.

# - Le module scriptinstallglpi.py qui permet l'installation de glpi.

# - Le module scriptinstallfi.py qui permet l'installation,l'activation du plugin fusioninventory et la création du crontab.

# - Le module droits.py qui permet de donner les droits sur le répertoire glpi au serveur apache2.

# La liste des clés/valeurs présente dans le fichier .YAML :

# lien: https://github.com/glpi-project/glpi/releases/download/9.5.0/glpi-9.5.0.tgz
# lienfi: https://github.com/fusioninventory/fusioninventory-for-glpi/releases/download/glpi9.5%2B3.0/fusioninventory-9.5+3.0.tar.bz2
# nomarchive: glpi.tgz
# nomarchivefi: fusioninventory.tar.bz2
# pathglpi: /var/www/html
# pathfi: /var/www/html/glpi/plugins
# host: localhost
# user: root
# password: root 
# unix_socket: /var/run/mysqld/mysqld.sock
# database: GLPIbd
# databaseuser: glpiuser
# passworddatabaseuser: glpimdp
# langue: fr_FR
# uid: 33
# gid: 33

# La liste des codes erreurs (Sur les systèmes linux vous pouvez afficher le numéro de l'erreur qui s'est produite avec la commande echo $?) :

# - Script installglpi.py :
#	  - 1 : IndexError: il manque l'argument pour le lancement d'installationglpi.py
#	  - 2 : KeyError: la clé "xxxx" n'existe pas

# - Module infosyaml.py :
#	  - 3 : FileNotFoundError: le fichier en argument au lancement d'installationglpi.py n'existe pas

# - Module DL.py :
# 	- 4 : requests.exceptions.MissingSchema et .InvalidSchema : l'URL "xxxx" ne commence pas par http ou https
# 	- 5 : requests.exceptions.ConnectorError: problème de connexion ou URL inconnue

# - Module archivetar.py :
# 	- 6 : ReadError : le format de l'archive est incompatible

# - Module creationbd.py :
# 	- 7 : mysql.connector.errors.ProgrammingError: la connexion à mysql est impossible ou l'utilisateur n'a pas les droits nécessaires.
# 	- 8 : mysql.connector.errors.InterfaceError: le chemin d'accès unix_socket est incorrect
# 	- 9 : mysql.connector.errors.DatabaseError: la base de donnée existe déjà

# - Module scriptinstallglpi :
# 	- 10 : erreur dans les commandes d'installation de glpi

# - Module scriptinstallfi.py :
# 	- 11 : TypeError: désinstaller le module crontab, installer le module python-crontab
# 	- 12 : erreur dans les commandes d'installation de fusioninventory

# - Module droits.py :
# 	- 13 : PermissionError: Pas les droits nécéssaires pour chown
# 	- 14 : TypeError: UID et GID doivent être des entiers  
