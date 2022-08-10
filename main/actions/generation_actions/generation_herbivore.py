"""
Класс генерации травоядных существ.
Следует реализовать класс генерации травоядных с
характеристиками "по умолчанию"

В будущем:
    Генерация должна позволять генерировать существ:
        1. С характеристиками по умолчанию
        2. С характеристиками которое передаёт пользователь
        3. С Характеристиками которые генерируются случайным образом

Идеи:
    Добавить "Двухуровневый" запрос:
        1. Для предварительной генерации.
        2. Для последующих генераций существ во время игры
        (Например: Пользователь может выбрать при
        предварительной генерации характеристики которые
        передаёт сам, а для последующих генераций -
        случайные характеристики)
        (Уточнить где именно лучше располагать эти уточняющие
        моменты. В классе generation_herbivore, или В классе simulation,
        или в классе herbivore, или вообще за пределами всех классов)

На Рассмотрении:
    Последующее размещение объектов на поле будет реализовано
    в этом классе, но вызываться он будет из соответствующего метода
    в классе herbivore (reproduction) - расположение шаблона в папке animals
    - dynamic object
"""
from main.actions import generate
from main.entity_object.animals.dynamic_object import herbivore
import random


class GenerationHerbivore(generate.Generate):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Количество травоядных
        self.object_quantity = 2
        # Счётчик травоядных
        self.count_object = 0
        # Объект для корректной работы словаря в information и цикла в generate
        self.object = herbivore.Herbivore(speed=2, hit_point=10, max_hit_point=10,
                                          gender=random.choice(['male', 'female']),
                                          restore_hp_eat_grass=random.randint(1, 3),
                                          x=self.matrix.height, y=self.matrix.width)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(herbivore.Herbivore(speed=2, hit_point=10, max_hit_point=10,
                                                   gender=random.choice(['male', 'female']),
                                                   restore_hp_eat_grass=random.randint(1, 3),
                                                   x=self.matrix.height, y=self.matrix.width),
                               num_1, num_2)
        # После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
        self.count_object = 0
