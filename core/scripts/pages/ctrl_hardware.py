import cherrypy
import json
from ..models.hardware import Hardware
from ..models.hardware_list import HardwareList
from ..models.hardware_types_list import HWTypesList


@cherrypy.expose
class CtrlHardware(object):

    def __init__(self):
        self.hardware_types = HWTypesList()
        self.hardware = HardwareList()

    # Обработчик получения списка всего оборудования
    @cherrypy.tools.accept(media='application/json')
    def GET(self):
        hw_list = self.hardware.get_all_hardware()
        return bytes(
                json.dumps(hw_list, default=lambda obj: obj.__dict__),
                encoding="utf-8"
            )
    
    # Обработчик запросов по работе с информацией об оборудовнии
    @cherrypy.tools.json_in()
    @cherrypy.tools.accept(media='application/json')
    def POST(self):
        data = cherrypy.request.json
        
        try:
            self.validate_request(data)
            response = self.handle_request(data)
        except Exception as ex:
            return bytes(
                    json.dumps({
                        'status': "error",
                        'message': str(ex)
                    }),
                    encoding="utf-8"
                )

        return bytes(json.dumps(response), encoding="utf-8")


    # Метод проверки правильности запроса
    def validate_request(self, request_data):
        if "action" not in request_data:
            raise Exception("Параметр запроса указан неверно!")
        if request_data['action'] not in {'add', 'update', 'delete'}:
            raise Exception("Значение параметра запроса указанно неверно!")
        if "data" not in request_data:
            raise Exception("Параметр запроса указан неверно!")
        if type(request_data['data']) is not dict:
            raise Exception("Входные данные указаны неверно!")
        return True


    # Метод обработки входящих запросов
    def handle_request(self, request_data):
        action = request_data['action']
        data   = request_data['data']

        if action == "add":
            return self.add_request(data)
        elif action == "update":
            # Наростить функционал - добавить возможность изменять записи
            pass
        elif action == "delete":
            # Наростить функционал - добавить возможность удалять записи
            pass
        else:
            raise Exception("Значение параметра запроса указанно неверно!")

    # Метод обработки запроса на добавление записи
    def add_request(self, data):
        type_id = int(data['hw_type_id'])
        hw_type = self.hardware_types.get_types()[type_id]
        hw_serial_num = data['hw_serial_num']

        hardware = Hardware(None, hw_type, hw_serial_num)
        result = self.hardware.add_hardware(hardware)

        return result
