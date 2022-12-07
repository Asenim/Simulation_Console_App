from main.actions.generate import Generate
from main.entity_object.animals.dynamic_object.predator import Predator
import random


class GenerationPredator(Generate):
    def __init__(self, matrix):
        """
        Класс генерации Хищников
        :param matrix: принимает на вход объект карты
        """
        super().__init__(matrix)
        # Максимальное Количество хищников на карте
        self._object_quantity = 1

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(Predator(speed=random.randint(2, 4),
                                        hit_point=5, max_hit_point=5,
                                        gender=random.choice(['male', 'female']),
                                        successful_hunting=3,
                                        restore_hp_successful_hunt=random.randint(1, 2),
                                        range_attack=random.randint(1, 2),
                                        attack_power=random.randint(3, 4),
                                        x=num_1, y=num_2), num_1, num_2)
