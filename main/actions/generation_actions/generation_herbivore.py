"""
Класс генерации травоядных существ.
Следует реализовать класс генерации травоядных с
характеристиками "по умолчанию"

В будущем:
	Генерация должна позволять генерировать существ:
		1. С характеристиками по умолчанию
		2. С характеристиками которое передаёт пользователь
		3. С Характеристиками которые генерируются случайным образом

Идеи:
	Добавить "Двухуровневый" запрос:
		1. Для предварительной генерации.
		2. Для последующих генераций существ во время игры
		(Например: Пользователь может выбрать при
		предварительной генерации характеристики которые
		передаёт сам, а для последующих генераций -
		случайные характеристики)
		(Уточнить где именно лучше располагать эти уточняющие
		моменты. В классе generation_herbivore, или В классе simulation,
		или в классе herbivore, или вообще за пределами всех классов)

На Рассмотрении:
	Последующее размещение объектов на поле будет реализовано
	в этом классе, но вызываться он будет из соответствующего метода
	в классе herbivore (reproduction) - расположение шаблона в папке animals
	- dynamic object
"""
from main.actions import generate
from main.animals.dynamic_object import herbivore
import random


class GenerationHerbivore(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Количество травоядных
		self.amount_herbivore = 2
		# Счётчик травоядных
		self.count_herbivore = 0
		# Создаём объект травоядного
		self.herbivore = herbivore.Herbivore(speed=2, hit_point=10, max_hit_point=10,
		                                     gender=random.choice(['male', 'female']),
		                                     restore_hp_eat_grass=2)
		# Список, который будет заполняться травоядными
		self.list_herbivore = []

	def generation(self):
		# Генерация травоядных
		for i in range(self.amount_herbivore):
			self.list_herbivore.append(self.herbivore.sprite)
		print(f'Список Травоядных - {self.list_herbivore}')
		print(f'В списке {len(self.list_herbivore)} Травоядных до размещения на матрице')

		# Основной цикл генерации
		while True:
			# Генерация случайных индексов для матрицы
			num_1 = random.randint(0, self.matrix.height - 1)
			num_2 = random.randint(0, self.matrix.width - 1)

			# Условие генерации Травы на матрице
			if self.matrix.map[num_1][num_2] == 0:
				if len(self.list_herbivore) > 0:
					# Трава располагается на карте
					self.matrix.map[num_1][num_2] = self.list_herbivore[-1]
					self.list_herbivore.pop(-1)

			# Условие выхода из цикла
			if len(self.list_herbivore) <= 0:
				self.count_herbivore = 0
				break
