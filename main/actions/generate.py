"""
Промежуточный класс.
Наследуется от Action.
Есть базовые поля и методы класса.
"""
from main.actions import actions
import random


class Generate(actions.Actions):
	def __init__(self, matrix):
		# Абстрактное количество генерируемых объектов которые необходимо сгенерировать
		self.object_quantity = None
		# Абстрактный счётчик сгенерированных объектов
		self.count_object = None
		# Абстрактный объект
		self.object = None
		# Матрица
		self.matrix = matrix

		# Количество клеток которое есть в матрице
		self.matrix_cells = self.matrix.height * self.matrix.width

	def perform(self):
		"""
		Всё ещё абстрактный
		служит для вызова остальных методов
		класса
		"""

	def spawn(self):
		"""
		Метод в котором будет реализован алгоритм
		генерации координат случайного расположения
		объектов на карте.
		"""
		# Основной цикл Генерации
		while True:
			# Подсчёт количества объектов на матрице
			for i in range(self.matrix.height):
				for j in range(self.matrix.width):
					if self.matrix.map[i][j] == self.object.sprite:
						self.count_object = self.count_object + 1

			# Если Количество объектов на матрице меньше чем необходимо
			if self.count_object < self.object_quantity:
				# Генерация случайных индексов матрицы
				num_1 = random.randint(0, self.matrix.height - 1)
				num_2 = random.randint(0, self.matrix.width - 1)

				# Условие генерации объектов на матрице
				if self.matrix.map[num_1][num_2] == 0:
					# Объекты располагаются на карте
					self.matrix.map[num_1][num_2] = self.object.sprite
				# Обнуляем счётчик для корректной работы условий
				self.count_object = 0

			# Условие выхода из цикла
			else:
				self.count_object = 0
				break

	def spawn_object(self):
		"""
		Абстрактный метод класса.
		В нем будет реализован алгоритм расположения
		объектов на матрице.
		"""
