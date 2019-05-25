"""
+--------+
| config |
+--------+
Config your muffin on here

"""

from core import html

class web:

    html_pages = {}

    def __init__(self):
        self.html_pages = html.html()._get_html_pages()
    #end def

# end class


# Config update for muffin.py
update = {
    'server.socket_timeout' : 0             ,
    'server.socket_host'    : "hostname"    ,
    'server.socket_port'    : "port"        ,
    'engine.autoreload.on'  : False         ,
}
