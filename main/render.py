"""
Класс, который вызывает методы генерации
и рисует нашу карту.
"""


class Render:
	def __init__(self, matrix):
		# Принимаем параметры
		self.matrix = matrix

	def print_map(self):
		"""
		Отрисовка нашего словаря
		"""
		# Основной алгоритм отрисовки
		for i in range(self.matrix.height):
			for j in range(self.matrix.width):
				coordinates = (i, j)
				if coordinates not in self.matrix.dict_object:
					item = ' '
				else:
					item = self.matrix.dict_object[coordinates].sprite

				print(str(item).ljust(3), end=' ')
			print()
