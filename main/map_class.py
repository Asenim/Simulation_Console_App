class Map:
	def __init__(self, height, width):
		# Проверка на передачу элементов
		if isinstance(height, int) and isinstance(width, int):
			self.height = height
			self.width = width
		else:
			print("Введите целые числа")

		# Переменная в которой хранится карта (словарь)
		self.map = {}
