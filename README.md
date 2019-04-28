# MuffinPy
A Tasty Python Web Framework

# Tahap install Muffin Py di windows

1. Install Python 2.7. Terbaru untuk windows
2. Buka CMD lalu ketik cd C:\Python27
3. ketik python
4. ketik import pip
5. exit()
6. ketik python -m pip install --upgrade pip
7. ketik python -m pip install mysql-connector
8. ketik python -m pip install cherrypy
9. ketik python -m pip install mako
10. Ubah html = "C:\directory-anda\folder-project-anda\static\pages\\" di core/directory.py
11. Ubah 'tools.staticdir.root'  : 'C:\directory-anda\folder-project-anda\\' di core/directory.py

# Menjalankan aplikasi

Contoh cara menjalankan: 
python muffin.py 127.0.0.1 15000 DITAAJIPRATAMA

Contoh cara menjalankan pada background: 
nohup python muffin.py 127.0.0.1 15000 DITAAJIPRATAMA &
