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

		# Создаём матрицу и рендер
		self.matrix = map_matrix.Map(self.height, self.width)
		self.renderer = render.Render(self.matrix)
		# Отрисовываем пустую матрицу
		self.renderer.print_map_matrix()

		# Создаём объекты генерации
		self.gen_tree = generation_tree.GenerationTree(self.matrix)
		self.gen_rock = generation_rock.GenerationRock(self.matrix)
		self.gen_grass = generation_grass.GenerationGrass(self.matrix)
		self.gen_herbivore = generation_herbivore.GenerationHerbivore(self.matrix)
		self.gen_predator = generation_predator.GenerationPredator(self.matrix)
		# Помещаем их в список
		self.list_actions = [self.gen_tree, self.gen_rock, self.gen_grass, self.gen_herbivore, self.gen_predator]

		# Вызываем предварительную генерацию перед началом игры
		for i in self.list_actions:
			i.perform()
		print()

		# Отрисовываем заполненную матрицу рендер
		self.renderer.print_map_matrix()

	def information(self):
		"""
		Временный метод показывающий
		количество всех объектов на матрице
		"""
		# Словарь с объектами матрицы
		dict_matrix_object = {}

		# Алгоритм заполнение словаря
		for action in self.list_actions:
			if action.object.sprite not in dict_matrix_object:
				dict_matrix_object[action.object.sprite] = 0

		print()
		# Подсчёт объектов на матрице для словаря
		for i in range(self.height):
			for j in range(self.width):
				for key in dict_matrix_object:
					if self.matrix.map[i][j] == key:
						dict_matrix_object[key] = dict_matrix_object[key] + 1

		# Вывод количества объектов на матрице
		for key in dict_matrix_object:
			print(f'{key} = {dict_matrix_object[key]}')


if __name__ == '__main__':
	sim = Simulation(5, 5)
	sim.information()
