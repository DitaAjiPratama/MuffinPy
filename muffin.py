import sys
import cherrypy
import tin

from core import config
from core import directory

if __name__ == '__main__':

    dirconfig   = directory.dirconfig
    update      = config.update

    if len(sys.argv) >= 3:

        update["server.socket_host"]    = sys.argv[1]
        update["server.socket_port"]    = int(sys.argv[2])

        cherrypy.config.update  ( update                        )
        cherrypy.quickstart     ( tin.tin(), config=dirconfig   )

    else:
        print ("Usage: python<ver> muffin.py <ipaddress> <port> <service_name>")
