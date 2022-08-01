class Map:
	def __init__(self, height, width):
		# Проверка на передачу элементов
		if isinstance(height, int) and isinstance(width, int):
			self.height = height
			self.width = width
		else:
			print("Введите целые числа")

		# Переменная в которой хранится карта (словарь)
		self.dict_object = {}

	def add_object(self, objects, x, y):
		coordinates = (x, y)
		self.dict_object[coordinates] = objects

