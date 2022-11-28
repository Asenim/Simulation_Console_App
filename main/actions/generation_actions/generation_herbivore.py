from main.actions import generate
from main.entity_object.animals.dynamic_object import herbivore
import random


class GenerationHerbivore(generate.Generate):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Количество травоядных
        self.object_quantity = 1
        # Счётчик травоядных
        self.count_object = 2
        # Объект для корректной работы словаря в information и цикла в generate
        self.object = herbivore.Herbivore(speed=2, hit_point=8, max_hit_point=10,
                                          gender=random.choice(['male', 'female']),
                                          restore_hp_eat_grass=random.randint(1, 2),
                                          x=self.matrix.height, y=self.matrix.width)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(herbivore.Herbivore(speed=2, hit_point=10, max_hit_point=15,
                                                   gender=random.choice(['male', 'female']),
                                                   restore_hp_eat_grass=random.randint(1, 2),
                                                   x=num_1, y=num_2), num_1, num_2)
        # После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
        self.count_object = 0
