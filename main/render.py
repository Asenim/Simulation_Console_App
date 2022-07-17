"""
Класс, который вызывает методы генерации
и рисует нашу карту.
"""


class Render:
	def __init__(self, height, width, matrix):
		# Принимаем параметры
		self.height = height
		self.width = width
		self.matrix = matrix

	def print_map_matrix(self):
		"""
		Отрисовка нашей матрицы
		"""
		for i in range(self.height):
			for j in range(self.width):
				print(str(self.matrix.map[i][j]).ljust(3), end=' ')
			print()
