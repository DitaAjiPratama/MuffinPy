"""
+----------+
| database |
+----------+
Save the database connection that you want

"""

import mysql.connector as mariadb

mariadb_contoh = mariadb.connect(
  host      = "localhost"   ,
  user      = "root"        ,
  password  = ""  ,
  database  = "test"
)
