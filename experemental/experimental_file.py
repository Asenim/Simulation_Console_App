from main.static_objects import grass
from main import map_matrix
import random

# Создаём траву
T = grass.Grass()

# Создаём матрицу
matrix = map_matrix.Map(3, 4)

# Генерируем координаты травы
generate_gross = random.randint(0, 2)
generate_gross_2 = random.randint(0, 2)

# Проходимся по матрице
for i in range(3):
	for j in range(4):
		# Если в клетке нет объекта - создаем его
		if matrix.map[i][j] == 0:
			matrix.map[generate_gross][generate_gross] = T.sprite
		if matrix.map[i][j] == 0:
			matrix.map[generate_gross_2][generate_gross_2] = T.sprite


class Exsperimental:
	def __init__(self):
		self.print_line()

	def vizov_s_verhu(self):
		print('Эта функция вызов с верху')
		self.print_line()

	def print_line(self):
		print('Эта функция печати')
		print('Функция сработала')
		print()

	def vizov_s_nizu(self):
		print('Эта функция вызов с низу')
		self.print_line()


Exs = Exsperimental()
Exs.vizov_s_nizu()
Exs.vizov_s_verhu()