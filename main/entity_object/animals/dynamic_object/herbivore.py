from main.entity_object.animals import creatures


class Herbivore(creatures.Creatures):
    def __init__(self, speed, hit_point, max_hit_point,
                 gender, restore_hp_eat_grass, x, y):
        """
        Класс Травоядного
        :param speed: Количество клеток которое существо может пройти за один ход
        :param hit_point: Количество здоровья существа
        :param max_hit_point: Максимальное количество здоровья существа
        :param gender: Пол существа
        :param restore_hp_eat_grass: Количество восстанавливаемого хп при поедании травы.
        :param x: Координата расположения объекта
        :param y: Координата расположения объекта
        :parameter self.sprite: То как будет выглядеть объект на карте
        """
        super().__init__(speed, hit_point, max_hit_point, gender, x, y)
        self.restore_hp_eat_grass = restore_hp_eat_grass
        self.sprite = 'Hrb'

    def make_move(self):
        pass

    def eat_grass(self, maps, coordinate_object):
        """
        Метод позволяет кушать траву, удалять объект
        травы и восстанавливать здоровье нашему травоядному.
        :param maps:
        :param coordinate_object:
        """
        matrix = maps
        coordinate = coordinate_object
        if not matrix.is_empty(coordinate.x, coordinate.y):
            creature = matrix.get_object(coordinate.x, coordinate.y)
            if creature.sprite == 'Gs':
                matrix.delete_object(coordinate.x, coordinate.y)
                if self.hit_point < self.max_hit_point:
                    self.hit_point = self.hit_point + self.restore_hp_eat_grass
                else:
                    self.hit_point = self.max_hit_point

    def reproduction(self):
        pass
