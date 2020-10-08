import cherrypy
import json
from ..models.hardware_types_list import HWTypesList


@cherrypy.expose
class CtrlHardwareTypes(object):

    def __init__(self):
        self.hardware_types = HWTypesList()

    # Обработчик получения списка всех типов оборудования
    @cherrypy.tools.accept(media='application/json')
    def GET(self):
        types_list = self.hardware_types.get_types()
        return bytes(
                json.dumps(types_list, default=lambda obj: obj.__dict__),
                encoding="utf-8"
            )
