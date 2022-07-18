"""
Класс позволяющий генерировать
траву на нашей карте.

Принимает на вход значения:
matrix = саму матрицу.
Параметры будут передаваться из simulation.py

Генерация так же проводит все необходимые расчёты
и создаёт все необходимые объекты, если их не хватает

Наследуется от generate.py
"""
from main.actions import generate
from main.static_objects import grass
import random


class GenerationGrass(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Необходимое количество травы на карте в зависимости от размера матрицы
		self.amount_grass = int(self.matrix_cells * 0.3)
		# Счётчик травы
		self.count_grass = 0

		# Создаём объект класса дерево
		self.G = grass.Grass()
		# Список, который будет заполняться травой
		self.list_grass = []

	def generation(self):
		"""
		Метод, который генерирует статичные
		объекты в соответствии с размером матрицы и
		заполняет список в init
		"""
		# Проверяем количество травы на матрице
		for i in range(self.matrix.height):
			for j in range(self.matrix.width):
				if self.matrix.map[i][j] == self.G.sprite:
					self.count_grass = self.count_grass + 1

		# Генерация травы
		if self.count_grass <= self.amount_grass//2:
			while len(self.list_grass) <= self.amount_grass-1:
				self.list_grass.append(self.G.sprite)
		print(f'Список Травы - {self.list_grass}')
		print(f'В списке {len(self.list_grass)} Травы до размещения на матрице')

		# Основной цикл генерации
		while True:
			# Генерация случайных индексов для матрицы
			num_1 = random.randint(0, self.matrix.height - 1)
			num_2 = random.randint(0, self.matrix.width - 1)

			# Условие генерации Травы на матрице
			if self.matrix.map[num_1][num_2] == 0:
				if len(self.list_grass) > 0:
					# Трава располагается на карте
					self.matrix.map[num_1][num_2] = self.list_grass[-1]
					self.list_grass.pop(-1)

			# Условие выхода из цикла
			if len(self.list_grass) <= 0:
				self.count_grass = 0
				break

	def spawning(self):
		"""
		Метод позволяющий создать траву на карте если её недостаточно.
		Продумать реализацию посоветоваться с Серегой.
		(Не задействованный метод)
		"""
		# Проверяем количество травы
		for i in range(self.matrix.height):
			for j in range(self.matrix.width):
				if self.matrix.map[i][j] == self.G.sprite:
					self.count_grass = self.count_grass + 1

		# Если травы меньше чем половина лимита
		if self.count_grass <= self.amount_grass//2:
			# Генерация травы
			for i in range(self.amount_grass//2):
				self.list_grass.append(self.G.sprite)

			while True:
				# Генерация случайных индексов для матрицы
				num_1 = random.randint(0, self.matrix.height - 1)
				num_2 = random.randint(0, self.matrix.width - 1)

				# Условие генерации Травы на матрице
				if self.matrix.map[num_1][num_2] == 0:
					if len(self.list_grass) > 0:
						# Трава располагается на карте
						self.matrix.map[num_1][num_2] = self.list_grass[-1]
						self.list_grass.pop(-1)

				# Условие выхода из цикла
				if len(self.list_grass) <= 0:
					break

		# На всякий случай очищаем список и обнуляем счётчик
		self.list_grass.clear()
		self.count_grass = 0
