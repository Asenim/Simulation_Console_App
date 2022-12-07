from main.actions.generate import Generate
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
import random


class GenerationHerbivore(Generate):
    def __init__(self, matrix):
        """
        Класс генерации Травоядного
        :param matrix: принимает на вход объект класса карты
        """
        super().__init__(matrix)
        # Количество травоядных
        self._object_quantity = 1

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(Herbivore(speed=2, hit_point=10, max_hit_point=15,
                                         gender=random.choice(['male', 'female']),
                                         restore_hp_eat_grass=random.randint(1, 2),
                                         x=num_1, y=num_2), num_1, num_2)
