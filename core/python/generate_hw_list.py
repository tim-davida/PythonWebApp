from random import seed
from random import choice
from random import randint

hw_types = [
	['1',  'Wi-Fi адаптер D-Link DWA-121/B1A',     'NaNAXZaZZaAXZ'],
	['2',  'Wi-Fi адаптер D-Link DWA-131/E',       'aZZNaZAaXaZNAXXA'],
	['3',  'Wi-Fi адаптер D-Link DWA-137/A1A',     'NANNaAXaaXAaaZX'],
	['4',  'Wi-Fi адаптер TP-LINK TL-WN725N',      'XNNAaAaXNZZNAX'],
	['5',  'Wi-Fi адаптер TP-LINK TL-WN727N',      'NNZaaXAZAXNXZ'],
	['6',  'Wi-Fi адаптер TP-LINK TL-WN781ND',     'ZZNNXXXAaNXXZN'],
	['7',  'Wi-Fi адаптер TP-LINK TL-WN821N',      'ZAaNXaZaNaX'],
	['8',  'Точка доступа D-Link DAP-1360U',       'ZZXXaXAXXa'],
	['9',  'Точка доступа D-Link DAP-3310/RU/A1A', 'AXaZaaXXXZ'],
	['10', 'Wi-Fi роутер D-Link DIR-615S',         'NXZNaaNXXaA'],
	['11', 'Wi-Fi роутер D-Link DIR-615/T4',       'AaNAZNNaNaN'],
	['12', 'Wi-Fi роутер D-Link DIR-620S',         'AAXZZXZNZZ'],
	['13', 'Wi-Fi роутер Tenda AC10U',             'NaXAAZXNXaXNNZ'],
	['14', 'Wi-Fi роутер Tenda AC1200',            'XNaAXXXAANXANaX'],
	['15', 'Wi-Fi роутер Tenda AC15',              'XAXAXANXZAXAXX'],
	['16', 'Wi-Fi роутер Tenda AC5',               'NZNNNaANAXZ'],
	['17', 'Wi-Fi роутер TP-LINK Archer A9',       'AXaaNZaXZAaZAN'],
	['18', 'Wi-Fi роутер TP-LINK Archer AX20',     'aZaAaNaANZXXa'],
	['19', 'Wi-Fi роутер TP-LINK Archer C1200',    'NNZXaXaZXAA'],
	['20', 'Wi-Fi роутер TP-LINK Archer C2300 v2', 'NAXXXNaNNZAXX'],
	['21', 'Роутер TP-LINK M7200',                 'XXANNXAZAXaXN'],
	['22', 'Роутер TP-LINK TL-MR150',              'ZXaZANXZNAXANN'],
	['23', 'Роутер TP-LINK TL-MR6400 v4',          'NZaXZXNZaXZaNNa'],
	['24', 'Сетевая карта D-Link DFE-520TX',       'ZNaNNNaAXA'],
	['25', 'Сетевая карта D-Link DGE-528T',        'aNZANZZNAaaa'],
	['26', 'Сетевая карта D-Link DGE-530',         'AZAAAXXNXaX'],
	['27', 'Сетевая карта D-Link DGE-560T',        'XaZAANZAXNXX'],
	['28', 'Сетевая карта TP-LINK TG-3468',        'aNNANAXZXAZAN'],
	['29', 'Сетевая карта TP-LINK UE200',          'aZNANXAZAZZaaAa'],
	['30', 'Сетевая карта TP-LINK UE300',          'ZNZXNXXZZNXA']
]

def create_serial(serial_mask):
	serial_num = ""
	
	for ch in serial_mask:
		if ch == "N":
			serial_num += str(randint(0, 9))
		elif ch == "A":
			serial_num += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
		elif ch == "a":
			serial_num += choice("abcdefghijklmnopqrstuvwxyz")
		elif ch == "X":
			serial_num += choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
		elif ch == "Z":
			serial_num += choice("-_@")
	
	return serial_num


def main():
	
	seed(1)
		
	for x in range(100):
		rand_id = randint(0, 29)
		
		hw_id = x + 1
		
		type_id     = hw_types[rand_id][0]
		type_name   = hw_types[rand_id][1]
		serial_mask = hw_types[rand_id][2]
		serial_num  = create_serial(serial_mask)
		
		print("{0},\t{1},\t{2}".format(hw_id, type_id, serial_num))

if __name__ == "__main__":
	main()
