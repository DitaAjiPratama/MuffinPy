WelcomeText = """
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

MuffinPyUsage = """
    Usage:
    python<ver> muffin.py <ipaddress> <port> <service_name>

    You can add nohup to run it on background.

    For example:
    nohup python3.6 muffin.py 127.0.0.1 15000 MUFFINAPPS &
"""

import sys
import os.path

import cherrypy

import tin

# core modules
from core import config
from core import directory

if __name__ == '__main__':

    dirconfig   = directory.dirconfig
    update      = config.update

    if len(sys.argv) >= 3:

        print (WelcomeText)

        update["server.socket_host"]    = sys.argv[1]
        update["server.socket_port"]    = int(sys.argv[2])

        cherrypy.config.update  ( update                             )
        cherrypy.quickstart     ( tin.tin(), config=dirconfig    )

    else:
        print (WelcomeText)
        print (MuffinPyUsage)
