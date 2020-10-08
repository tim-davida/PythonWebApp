import os
from pathlib import Path
import cherrypy


class TestPage:

    @cherrypy.expose
    def index(self, page="default"):
        work_folder = Path(os.path.abspath(os.getcwd()))
        tmpl_folder = work_folder / "core" / "templates"
        template = open(tmpl_folder / ("%s.html" % page), encoding="utf8")
        return template.read()
