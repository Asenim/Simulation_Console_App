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


matrix.print_map_matrix()
