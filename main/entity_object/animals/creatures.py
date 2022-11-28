from main.entity_object import entity


class Creatures(entity.Entity):
    def __init__(self, speed, hit_point, max_hit_point, gender, x, y):
        """
        Головной класс от которого будут наследоваться все классы существ.
        :param speed: Количество клеток которое существо может пройти за один ход
        :param hit_point: Количество здоровья существа
        :param max_hit_point: Максимальное количество здоровья существа
        :param gender: Пол существа
        :param x: Координата расположения объекта
        :param y: Координата расположения объекта
            """
        super().__init__(x, y)
        self.speed = speed
        self.hit_point = hit_point
        self.max_hit_point = max_hit_point
        self.gender = gender
