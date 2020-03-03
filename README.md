# MuffinPy
A Python Web Framework. Focus on easy code and clean framework. Made with cherrypy and mako.

# Installation MuffinPy in Linux

sh install-modules.sh

# Installation MuffinPy in Windows

\> python get-pip.py

\> python
\>\>\> import pip


\> python -m pip install mysql-connector
\> python -m pip install cherrypy
\> python -m pip install mako

Change html = "C:\Your_Directory_Project_Folder\static\pages\\" in config/directory.py

Change 'tools.staticdir.root'  : 'C:\Your_Directory_Project_Folder\\' in config/directory.py

# Running Application

python3 muffin.py \<IP_Adress\> \<Port\> \<Name\>

Sample:

python3 muffin.py 127.0.0.1 15000 YOUR_PROJECT_NAME

Running it in background:

nohup python3 muffin.py 127.0.0.1 15000 YOUR_PROJECT_NAME & disown

Show running service in background:

ps -ef | grep muffin.py

Debugging:

tail -f nohup.out
