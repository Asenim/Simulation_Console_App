class MapMatrix:
	def __init__(self, height, width):
		# Проверка на передачу элементов
		if isinstance(height, int) and isinstance(width, int):
			self.height = height
			self.width = width
		else:
			print("Введите целые числа")

		# Переменная в которой хранится матрица
		self.map = []
		# Генерируем нашу матрицу
		for i in range(self.height):
			self.elements = []
			for j in range(self.width):
				self.elements.append(0)
			self.map.append(self.elements)
