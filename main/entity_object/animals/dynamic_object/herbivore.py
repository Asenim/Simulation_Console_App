"""
Класс травоядных, все травоядные будут создаваться из этого класса
Дополнительное поле:
    restore_hp_eat_grass - Количество восстанавливаемого хп при
    поедании травы.
"""
from main.entity_object.animals import creatures


class Herbivore(creatures.Creatures):
    def __init__(self, speed, hit_point, max_hit_point,
                 gender, restore_hp_eat_grass, x, y):
        super().__init__(speed, hit_point, max_hit_point, gender, x, y)
        self.restore_hp_eat_grass = restore_hp_eat_grass
        self.sprite = 'Hrb'

    def make_move(self):
        pass

    def eat_grass(self, maps, coordinate_object):
        matrix = maps
        coordinate = coordinate_object
        if not matrix.is_empty(coordinate.x, coordinate.y):
            creature = matrix.get_object(coordinate.x, coordinate.y)
            if creature.sprite == 'Gs':
                matrix.delete_object(coordinate.x, coordinate.y)
                self.hit_point = self.hit_point + self.restore_hp_eat_grass

    def reproduction(self):
        pass
