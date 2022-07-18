"""
Класс, который вызывает методы генерации
и рисует нашу карту.
"""


class Render:
	def __init__(self, matrix):
		# Принимаем параметры
		self.matrix = matrix

	def print_map_matrix(self):
		"""
		Отрисовка нашей матрицы
		"""
		for i in range(self.matrix.height):
			for j in range(self.matrix.width):
				print(str(self.matrix.map[i][j]).ljust(3), end=' ')
			print()
