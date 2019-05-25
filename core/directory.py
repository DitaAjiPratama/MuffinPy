"""
+-----------+
| directory |
+-----------+
Keep all your directory on here

"""

import os

html = "static/pages"

# Directory config for muffin.py
dirconfig = {

    '/'         :   {
                        'tools.sessions.on'     : True                          ,
                        'tools.staticdir.root'  : os.path.abspath(os.getcwd())  ,
                    },

    '/css'      :   {
                        'tools.staticdir.on'    : True                          ,
                        'tools.staticdir.dir'   : './static/css'                ,
                    },

    '/js'       :   {
                        'tools.staticdir.on'    : True                          ,
                        'tools.staticdir.dir'   : './static/js'                 ,
                    },

    '/images'   :   {
                        'tools.staticdir.on'    : True                          ,
                        'tools.staticdir.dir'   : './static/images'             ,
                    },

    '/lib'      :   {
                        'tools.staticdir.on'    : True                          ,
                        'tools.staticdir.dir'   : './static/lib'                ,
                    },

}
