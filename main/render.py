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

		# Выводим пустую матрицу на экран
		self.matrix.print_map_matrix()
