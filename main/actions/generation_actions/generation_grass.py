from main.actions import generate
from main.static_objects import grass


class GenerationGrass(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Необходимое количество травы на карте в зависимости от размера матрицы
		self.object_quantity = int(self.matrix_cells * 0.3)
		# Счётчик травы
		self.count_object = 0
		# Объект для подсчета в information и generate
		self.object = grass.Grass()

	def spawn_object(self, num_1, num_2):
		# Условие генерации объектов на матрице
		if self.matrix.map[num_1][num_2] == 0:
			# Объекты располагаются на карте
			self.matrix.map[num_1][num_2] = grass.Grass().sprite
		# После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
		self.count_object = 0
