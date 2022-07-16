"""
Промежуточный класс.
Наследуется от Action.
Есть базовые поля и методы класса.
"""
from main.actions import actions


class Generate(actions.Actions):
	def __init__(self, height, width, matrix):
		self.height = height
		self.width = width
		self.matrix = matrix

		# Количество клеток которое есть в матрице
		self.matrix_cells = self.height * self.width

	def generation(self):
		pass

	# def spawning(self):
	# 	"""
	# 	Примечание:
	# 	Данный метод нигде не применяется,
	# 	есть мысли добавить его отдельным методом в классы
	# 	доспауна существ и травы через отдельную коллекцию
	# 	в которой будут вызываться actions итерирующаяся во время
	# 	игры
	# 	"""
	# 	pass

