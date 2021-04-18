import tarfile

archive = tarfile.open('glpi.tar')
archive.extractall(path = '/var/www/html')
archive.close()