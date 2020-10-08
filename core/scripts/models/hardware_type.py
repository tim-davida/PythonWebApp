import json

#
#  Модель типа оборудования
#
class HardwareType:

    type_id     = None
    type_name   = None
    serial_mask = None

    def __init__(self, type_id, type_name, serial_mask):
        self.type_id     = type_id
        self.type_name   = type_name
        self.serial_mask = serial_mask
