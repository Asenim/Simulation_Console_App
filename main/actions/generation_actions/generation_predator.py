from main.actions import generate
from main.entity_object.animals.dynamic_object import predator
import random


class GenerationPredator(generate.Generate):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Максимальное Количество хищников на карте
        self.object_quantity = 1
        # Счетчик хищников
        self.count_object = 1
        # Объект для корректной работы словаря в information и цикла в generate
        self.object = predator.Predator(speed=random.randint(3, 4), hit_point=5, max_hit_point=5,
                                        gender=random.choice(['male', 'female']),
                                        successful_hunting=3, restore_hp_successful_hunt=random.randint(1, 2),
                                        range_attack=random.randint(1, 2), attack_power=random.randint(3, 4),
                                        x=self.matrix.height, y=self.matrix.width)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(predator.Predator(speed=random.randint(2, 4),
                                                 hit_point=5, max_hit_point=5,
                                                 gender=random.choice(['male', 'female']),
                                                 successful_hunting=3,
                                                 restore_hp_successful_hunt=random.randint(1, 2),
                                                 range_attack=random.randint(1, 2),
                                                 attack_power=random.randint(3, 4),
                                                 x=num_1, y=num_2),
                               num_1, num_2)
        # После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
        self.count_object = 0
