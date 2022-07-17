"""
Класс позволяющий генерировать
деревья на нашей карте.

Принимает на вход значения:
width = ширины, height = высоты и matrix = саму матрицу.
Параметры будут передаваться из render.py

Генерация так же проводит все необходимые расчёты
и создаёт все необходимые объекты, если их не хватает

Наследуется от generate.py
"""
from main.actions import generate
from main.static_objects import tree
import random


class GenerationTree(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Необходимое количество дерева на карте в зависимости от размера матрицы
		self.amount_tree = int(self.matrix_cells * 0.2)
		# Счетчик дерева
		self.count_tree = 0

		# Создаём объект класса дерево
		self.T = tree.Tree()
		# Список, который будет заполняться деревом
		self.list_tree = []

	def generation(self):
		"""
		Метод, который генерирует статичные
		объекты в соответствии с размером матрицы и
		заполняет список в init
		"""
		# Генерация дерева
		for i in range(self.amount_tree):
			self.list_tree.append(self.T.sprite)
		print(f'Список Дерева - {self.list_tree}')
		print(f'В списке {len(self.list_tree)} Дерева до размещения на матрице')

		# Основной цикл Генерации
		while True:
			# Генерация случайных индексов матрицы
			num_1 = random.randint(0, self.matrix.height - 1)
			num_2 = random.randint(0, self.matrix.width - 1)

			# Условие генерации Деревьев на матрице
			if self.matrix.map[num_1][num_2] == 0:
				if len(self.list_tree) > 0:
					# Деревья располагаются на карте
					self.matrix.map[num_1][num_2] = self.list_tree[-1]
					self.list_tree.pop(-1)

			# Условие выхода из цикла
			if len(self.list_tree) <= 0:
				break
