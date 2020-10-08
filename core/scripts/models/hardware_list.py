from ..handlers.db_handler import DBHandler
from .hardware_types_list import HWTypesList
from .hardware import Hardware

#
#  Модель списка оборудования
#
class HardwareList(DBHandler):

	def __init__(self):
		super().__init__()
		self.hw_types = HWTypesList()

	# Метод получения объекта оборудования по его ID
	def add_hardware(self, hardware: Hardware):

		type_id = hardware.hw_type.type_id
		serial_num = hardware.serial_num
				
		self.query(
				"INSERT INTO Hardware (TypeId, SerialNum) VALUES (%s, %s)",
				(type_id, serial_num)
			)
		self.connect.commit()

		return {
			'status': "success",
			'message': "Запись об оборудовании (S/N: %s) добавлена в базу данных" % (serial_num)
		}

	# Метод получения объекта оборудования по его ID
	def get_hardware_by_id(self, hw_id):

		# Запрос сырого списка оборудования из БД
		raw_list = self.query("SELECT * FROM Hardware WHERE HardwareId = %s", (hw_id, ))

		if raw_list.__len__() <= 0:
			raise Exception("Оборудование с указанным ID не существует в базе данных")

		raw_hw = raw_list[0]

		# Словарь объектов типов оборудования
		types_list = self.hw_types.get_types()

		# Поля с информацией об оборудовании
		hw_id      = int(raw_hw[0])
		type_id    = int(raw_hw[1])
		hw_type    = types_list[type_id]
		serial_num = raw_hw[2]

		# Объект оборудования
		hardware = Hardware(hw_id, hw_type, serial_num)

		# Возвращаем экземпляр оборудования
		return hardware

	# Метод получения всего оборудования
	def get_all_hardware(self):

		# Запрос сырого списка оборудования из БД
		raw_list = self.query("SELECT * FROM Hardware")

		# Словарь объектов типов оборудования
		types_list = self.hw_types.get_types()

		# Словарь объектов оборудования
		hw_list = {}

		# Запись оборудования из списка в словарь
		for item in raw_list:
			hw_id      = int(item[0])
			type_id    = int(item[1])
			hw_type    = types_list[type_id]
			serial_num = item[2]

			# Объект оборудования
			hardware = Hardware(hw_id, hw_type, serial_num)

			# Добавление объекта оборудования в словарь
			hw_list[hw_id] = hardware

		# Возвращаем словарь оборудования
		return hw_list
