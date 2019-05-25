import mysql.connector as mariadb
from mako.template import Template

from core import database

class select_sample:

    def __init__(self):
        pass
    #end def

    def html(self, params):

        html_page = params['html']

        cursor = database.mariadb_contoh.cursor()
        cursor.execute("SELECT * FROM testing")
        listing = list(cursor)

        return Template(html_page).render(
            cursor=listing
        )
    # end def

#end class
