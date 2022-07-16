"""
Один из главных классов.
От него будут наследоваться, все классы существ в игре.

Поля класса:
	speed - Сколько клеток может пройти
		существо за один ход
	hit_point - количество здоровья существа
	max_hit_point - Максимальное количество
		здоровья существа
	gender - Пол существа

Методы класса:
	makeMove(map) - сделать ход.
	Аргументом принимают… карту?
	После каждого хода травоядные будут искать траву и убегать от хищников,
	хищники будут искать травоядных

"""


from main import entity


class Creatures(entity.Entity):
	def __init__(self, speed, hit_point, max_hit_point, gender):
		self.speed = speed
		self.hit_point = hit_point
		self.max_hit_point = max_hit_point
		self.gender = gender

	def make_move(self):
		pass
