import os
from pathlib import Path
import cherrypy
import mysql.connector


class HomePage:

    @cherrypy.expose
    def index(self):
        work_folder = Path(os.path.abspath(os.getcwd()))
        tmpl_folder = work_folder / "core" / "templates"
        template = open(tmpl_folder / "default.html", encoding="utf8")
        return template.read()
