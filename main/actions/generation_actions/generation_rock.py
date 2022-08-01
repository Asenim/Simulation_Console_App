from main.actions import generate
from main.static_objects import rock


class GenerationRock(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Необходимое количество камня на карте
		self.object_quantity = int(self.matrix_cells * 0.1)
		# Счётчик камня
		self.count_object = 0
		# Объект для подсчёта в information и generate
		self.object = rock.Rock()

	def spawn_object(self, num_1, num_2):
		# Размещаем объекты в карте
		self.matrix.add_object(rock.Rock(), num_1, num_2)
		# После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
		self.count_object = 0
