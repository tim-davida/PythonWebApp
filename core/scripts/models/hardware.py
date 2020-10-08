from .hardware_type import HardwareType

#
#  Модель оборудования
#
class Hardware:

	hw_id      = None
	hw_type    = None
	serial_num = None

	def __init__(self, hw_id, hw_type, serial_num):
		self.hw_id      = hw_id
		self.hw_type = HardwareType(
                hw_type.type_id,
                hw_type.type_name,
                hw_type.serial_mask
            )
		self.serial_num = serial_num
