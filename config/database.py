import mysql.connector as mariadb

sample_db = mariadb.connect(
    host      = "localhost"     ,
    user      = "root"           ,
    password  = ""    ,
    database  = "mysql"
)

# another_db = mariadb.connect(
#     host      = "localhost"             ,
#     port      = 3306                    ,
#     user      = "root"                  ,
#     password  = ""                      ,
#     database  = "db_name"
# )
