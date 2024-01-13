import sys
import os

VENV_NAME = "djangotemplate"
PYTHON_VERSION = "python3.10"
MINICONDA_ROOT = "/miniconda3"

"""
Diese Start Datei wird in dem von Netcup bestimmten Python Interpreter geladen.
mit os.execl("python","python","this_file") wird die Datei im definierten Python Interpreter neu geladen.
Alle Packages die der Python Interpreter zur Verfügung hat können importiert werden.
Code leicht geändert von: https://help.dreamhost.com/hc/en-us/articles/215769548-Passenger-and-Python-WSGI
"""

INTERPRETER_PATH = os.environ["HOME"] + MINICONDA_ROOT + "/envs/" + VENV_NAME + "/bin/" + PYTHON_VERSION

"""
os.environ["HOME"] ist wie ~/
wenn Passenger diese Datei als dein Webhosting User öffnet
befindet sich das Nutzer Verzeichnis nicht mehr unter:
"/" sonder "/var/www/vhosts/hosting*user*.*server*.netcup.net/"
"/miniconda3/envs/testenv/bin/python3.9" muss der Path zu den Python Binaries sein
python -m venv testenv // funzt nicht, denn dabei wird nur ein Link zur Haupt Python Anwendung erstellt.
lieber: conda create --name testenv // hierbei werden augenscheinlich die Python Binaries direkt in der Venv abgelegt.
"""

# INTERP is present twice so that the new Python interpreter knows the actual executable path
if sys.executable != INTERPRETER_PATH:
	os.execl(INTERPRETER_PATH, INTERPRETER_PATH, *sys.argv)

import djangotemplate.wsgi
application = djangotemplate.wsgi.application
