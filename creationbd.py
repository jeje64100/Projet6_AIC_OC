import mysql.connector

bd=mysql.connector.connect(host='localhost',
					user='root',
					password='root',
					unix_socket='/var/run/mysqld/mysqld.sock'
					)

cursor=bd.cursor()
cursor.execute("CREATE DATABASE glpidb")
cursor.execute("GRANT ALL privileges on glpidb.* to 'glpiuser'@'localhost' IDENTIFIED BY 'glpimdp'")

cursor.close()
bd.close()