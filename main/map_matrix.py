"""
Класс для отрисовки карты с помощью произвольной матрицы
Класс принимает только число
и инициализирует матрицу с заданными параметрами
	height = высота матрицы
	width = ширина матрицы

Метод print_map_matrix - служит для вывода и отрисовки нашей матрицы
"""


class Map:
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

	def print_map_matrix(self):
		"""
		Отрисовка нашей матрицы
		"""
		for i in range(self.height):
			for j in range(self.width):
				print(str(self.map[i][j]).ljust(3), end=' ')
			print()
