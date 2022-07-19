"""
Класс позволяющий генерировать
камни на нашей карте.

Принимает на вход значения:
width = ширины, height = высоты и matrix = саму матрицу.
Параметры будут передаваться из render.py

Генерация так же проводит все необходимые расчёты
и создаёт все необходимые объекты, если их не хватает

Наследуется от generate.py
"""
from main.actions import generate
from main.static_objects import rock
import random


class GenerationRock(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Необходимое количество камня на карте
		self.object_quantity = int(self.matrix_cells * 0.1)
		# Счётчик камня
		self.count_object = 0

		# Создаём объект класса Камень
		self.object = rock.Rock()
		# Список, который будет заполняться камнем
		self.list_rock = []

	def generation(self):
		"""
		Метод, который генерирует статичные
		объекты в соответствии с размером матрицы и
		заполняет список в init (На удаление)
		"""
		# Генерация дерева
		for i in range(self.object_quantity):
			self.list_rock.append(self.object.sprite)
		print(f'Список Камня - {self.list_rock}')
		print(f'В списке {len(self.list_rock)} Камня до размещения на матрице')

		# Основной цикл Генерации
		while True:
			# Генерация случайных индексов матрицы
			num_1 = random.randint(0, self.matrix.height - 1)
			num_2 = random.randint(0, self.matrix.width - 1)

			# Условие генерации Деревьев на матрице
			if self.matrix.map[num_1][num_2] == 0:
				if len(self.list_rock) > 0:
					# Деревья располагаются на карте
					self.matrix.map[num_1][num_2] = self.list_rock[-1]
					self.list_rock.pop(-1)

			# Условие выхода из цикла
			if len(self.list_rock) <= 0:
				break

	def spawn_object(self):
		self.spawn()

	def perform(self):
		self.spawn()
