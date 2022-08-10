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

    def eat_gross(self):
        pass

    def reproduction(self):
        pass
