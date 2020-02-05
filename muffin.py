import sys
import cherrypy
import handler

from core   import web
from config import server
from config import directory

if __name__ == '__main__':

    dirconfig   = directory.dirconfig
    update      = server.update

    if len(sys.argv) >= 3:

        update["server.socket_host"]    = sys.argv[1]
        update["server.socket_port"]    = int(sys.argv[2])

        cherrypy.config.update  ( update                                )
        cherrypy.quickstart     ( handler.handler(), config=dirconfig   )

    else:
        print ("Usage: python<ver> muffin.py <ipaddress> <port> <service_name>")
