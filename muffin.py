"""
Muffin.Digital Present
 _______         ___   ___ __         ______
|   |   |.--.--.'  _|.'  _|__|.-----.|   __ \.--.--.
|       ||  |  |   _||   _|  ||     ||    __/|  |  |
|__|_|__||_____|__|  |__| |__||__|__||___|   |___  |
                                             |_____|

Super Easy, Super Clean.

Created by:
Dita Aji Pratama

Collaborators:
<null>

"""

import sys
import os.path

import cherrypy

import crock

# core modules
from core import config
from core import directory

if __name__ == '__main__':

    dirconfig   = directory.dirconfig
    update      = config.update

    if len(sys.argv) >= 3:
        update["server.socket_host"]    = sys.argv[1]
        update["server.socket_port"]    = int(sys.argv[2])

        cherrypy.config.update  ( update                             )
        cherrypy.quickstart     ( crock.crock(), config=dirconfig    )

    else:
        print "usage: python muffin.py <ipaddress> <port>"
