from ..handlers.db_handler import DBHandler
from .hardware_type import HardwareType

#
#  Модель списка типов оборудования
#
class HWTypesList(DBHandler):

	# Метод получения всех типов оборудования
	def get_types(self):

		# Запрос сырого списка из БД
		raw_list = self.query("SELECT * FROM HardwareTypes")

		# Словарь объектов типов
		types_list = {}

		# Запись типов из списка в словарь
		for item in raw_list:
			type_id     = int(item[0])
			type_name   = item[1]
			serial_mask = item[2]

			# Объект типа
			hw_type = HardwareType(type_id, type_name, serial_mask)

			# Добавление объекта типа в словарь
			types_list[type_id] = hw_type

		# Возвращаем словарь типов
		return types_list
