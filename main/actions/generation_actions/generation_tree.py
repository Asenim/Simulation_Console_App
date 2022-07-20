from main.actions import generate
from main.static_objects import tree


class GenerationTree(generate.Generate):
	def __init__(self, matrix):
		super().__init__(matrix)
		# Необходимое количество дерева на карте в зависимости от размера матрицы
		self.object_quantity = int(self.matrix_cells * 0.2)
		# Счетчик дерева
		self.count_object = 0
		# Объект для подсчёта в information и generate
		self.object = tree.Tree()

	def spawn_object(self, num_1, num_2):
		# Условие генерации объектов на матрице
		if self.matrix.map[num_1][num_2] == 0:
			# Объекты располагаются на карте
			self.matrix.map[num_1][num_2] = tree.Tree().sprite
		# После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
		self.count_object = 0
