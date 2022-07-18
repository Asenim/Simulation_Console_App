"""
Промежуточный класс.
Наследуется от Action.
Есть базовые поля и методы класса.
"""
from main.actions import actions


class Generate(actions.Actions):
	def __init__(self, matrix):
		self.matrix = matrix

		# Количество клеток которое есть в матрице
		self.matrix_cells = self.matrix.height * self.matrix.width

	def perform(self):
		self.spawn()

	def spawn(self):
		"""
		Метод в котором будет реализован алгоритм
		генерации координат случайного расположения
		объектов на карте.
		"""
		pass

	def spawn_object(self):
		"""
		Абстрактный метод класса.
		В нем будет реализован алгоритм расположения
		объектов на матрице.
		"""
