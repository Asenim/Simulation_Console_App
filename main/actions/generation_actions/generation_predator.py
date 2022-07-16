from main.actions import generate
from main.animals.dynamic_object import predator
import random


class GenerationPredator(generate.Generate):
	def __init__(self, height, width, matrix):
		super().__init__(height, width, matrix)
		# Максимальное Количество хищников на карте
		self.amount_predator = 1
		# Счетчик хищников
		self.count_predator = 0
		self.predator = predator.Preadator(speed=3, hit_point=5, max_hit_point=5,
		                                   gender=random.choice(['male', 'female']),
		                                   successful_hunting=3, restore_hp_successful_hunt=1,
		                                   range_attack=2)
		# Список, который будет заполняться хищниками
		self.list_predator = []

	def generation(self):
		# Проверяем количество хищников на матрице
		for i in range(self.height):
			for j in range(self.width):
				if self.matrix.map[i][j] == self.predator.sprite:
					self.count_predator = self.count_predator + 1

		# Генерация хищников
		while len(self.list_predator) <= self.amount_predator-1:
			self.list_predator.append(self.predator.sprite)
		print(f'Список Хищников - {self.list_predator}')
		print(f'В списке {len(self.list_predator)} Хищников до размещения на матрице')

		# Основной цикл генерации
		while True:
			num_1 = random.randint(0, self.height - 1)
			num_2 = random.randint(0, self.width - 1)

			# Условие генерации на матрице
			if self.matrix.map[num_1][num_2] == 0:
				self.matrix.map[num_1][num_2] = self.list_predator[-1]
				self.list_predator.pop(-1)

			# Условие выхода из цикла
			if len(self.list_predator) <= 0:
				self.count_predator = 0
				break
