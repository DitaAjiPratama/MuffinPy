"""
+-----+
| tin |
+-----+
Cook your muffins on here

"""

import mysql.connector as mariadb

from mako.template import Template

# core modules
from core import database
from core import directory

from modules import home

class tin(config.web):

    def __init__(self):
        config.web.__init__(self)

    def index(self, **kwargs):

        tulisan = "World"

        return Template(filename=directory.html+"index.html").render(testing=tulisan)

    index.exposed = True

    def sample(self, **kwargs):

        cursor = database.mariadb_contoh.cursor()
        cursor.execute("SELECT * FROM testing")

        list = ""
        for nama, telp in cursor:
            list = list + ("Nama: {}, Telp: {} <br>").format(nama,telp)

        return list

    sample.exposed = True
