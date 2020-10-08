import cherrypy
from .ctrl_hardware_types import CtrlHardwareTypes
from .ctrl_hardware import CtrlHardware

class DataAccess:

    def __init__(self):
        self.hardware = CtrlHardware()
        self.hardware_types = CtrlHardwareTypes()

    @cherrypy.expose
    def index(self):
        return "<h1>Тебя не должно тут быть!</h1>"