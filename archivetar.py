import tarfile

archive = tarfile.open('glpi.tar', mode = 'r:tar')

archiveInfo = archive.next()
print(archiveInfo.name)
archive.extract(archiveInfo, path = '')