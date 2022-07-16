"""
Головной класс позволяющий взаимодействовать с пользователем.
Запрашивает пользовательский ввод.
Генерирует матрицу.
Производит рендер.
"""

from main import map_matrix
from main import render
from main.actions.generation_actions import generation_tree
from main.actions.generation_actions import generation_rock
from main.actions.generation_actions import generation_grass
from main.actions.generation_actions import generation_herbivore
from main.actions.generation_actions import generation_predator


class Simulation:
	def __init__(self, height, width):
		# Принимаем значения
		self.height = height
		self.width = width

		# Создаём матрицу
		self.matrix = map_matrix.Map(self.height, self.width)
		self.matrix.print_map_matrix()

		# Создаём объекты генерации
		self.gen_tree = generation_tree.GenerationTree(self.height, self.width, self.matrix)
		self.gen_rock = generation_rock.GenerationRock(self.height, self.width, self.matrix)
		self.gen_grass = generation_grass.GenerationGrass(self.height, self.width, self.matrix)
		self.gen_herbivore = generation_herbivore.GenerationHerbivore(self.height, self.width, self.matrix)
		self.gen_predator = generation_predator.GenerationPredator(self.height, self.width, self.matrix)
		# Помещаем их в список
		self.list_actions = [self.gen_tree, self.gen_rock, self.gen_grass, self.gen_herbivore, self.gen_predator]

		# Вызываем предварительную генерацию перед началом игры
		for i in self.list_actions:
			i.generation()

		# Создаем рендер
		self.renderer = render.Render(self.height, self.width, self.matrix)

	def information(self):
		"""
		Временный метод показывающий
		количество всех объектов на матрице
		"""
		# Словарь с объектами матрицы
		dict_matrix_object = {
			self.gen_grass.G.sprite: 0,
			self.gen_tree.T.sprite: 0,
			self.gen_rock.R.sprite: 0,
			self.gen_predator.predator.sprite: 0,
			self.gen_herbivore.herbivore.sprite: 0
		}
		# Подсчёт объектов на матрице
		for i in range(self.height):
			for j in range(self.width):
				for key in dict_matrix_object:
					if self.matrix.map[i][j] == key:
						dict_matrix_object[key] = dict_matrix_object[key] + 1

		# Вывод количества объектов на матрице
		for key in dict_matrix_object:
			print(f'{key} = {dict_matrix_object[key]}')

		"""
		for i in range(self.height):
			for j in range(self.width):
				if self.matrix.map[i][j] == self.gen_grass.G.sprite:
					self.gen_grass.count_grass = self.gen_grass.count_grass + 1
				if self.matrix.map[i][j] == self.gen_rock.R.sprite:
					self.gen_rock.count_rock = self.gen_rock.count_rock + 1
				if self.matrix.map[i][j] == self.gen_tree.T.sprite:
					self.gen_tree.count_tree = self.gen_tree.count_tree + 1
				if self.matrix.map[i][j] == self.gen_herbivore.herbivore.sprite:
					self.gen_herbivore.count_herbivore = self.gen_herbivore.count_herbivore + 1
				if self.matrix.map[i][j] == self.gen_predator.predator.sprite:
					self.gen_predator.count_predator = self.gen_predator.count_predator + 1
		print(f'Количество Травы на матрице: {self.gen_grass.count_grass}')
		print(f'Количество Травы в списке: {len(self.gen_grass.list_grass)}')
		print(f'Количество Дерева на матрице: {self.gen_tree.count_tree}')
		print(f'Количество Дерева в списке {len(self.gen_tree.list_tree)}')
		print(f'Количество Камня на матрице: {self.gen_rock.count_rock}')
		print(f'Количество Камня в списке {len(self.gen_rock.list_rock)}')
		print(f'Количество Травоядных на матрице {self.gen_herbivore.count_herbivore}')
		print(f'Количество Травоядных в списке {len(self.gen_herbivore.list_herbivore)}')
		print(f'Количество Хищников на матрице {self.gen_predator.count_predator}')
		print(f'Количество Хищников в списке {len(self.gen_predator.list_predator)}')
		self.gen_grass.count_grass = 0
		self.gen_tree.count_tree = 0
		self.gen_rock.count_rock = 0
		self.gen_herbivore.count_herbivore = 0
		self.gen_predator.count_predator = 0
		"""


if __name__ == '__main__':
	sim = Simulation(5, 5)
	sim.information()
