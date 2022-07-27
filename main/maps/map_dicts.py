class MapDict:
	def __init__(self, height, width):
		# Проверка на передачу элементов
		if isinstance(height, int) and isinstance(width, int):
			self.height = height
			self.width = width
		else:
			print("Введите целые числа")

		# Переменная в которой хранится карта (словарь)
		self.map = {}
		# Генерируем нашу карту
		for i in range(self.height):
			for j in range(self.width):
				coordinates = (i, j)
				if coordinates not in self.map:
					self.map[coordinates] = 0
