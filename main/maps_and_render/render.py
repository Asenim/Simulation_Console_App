"""
Класс, который вызывает методы генерации
и рисует нашу карту.
"""
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator


class Render:
    def __init__(self, matrix):
        # Принимаем параметры
        self.matrix = matrix

    def print_map(self):
        """
        Отрисовка нашего словаря
        """
        # Основной алгоритм отрисовки
        for x in range(self.matrix.height):
            for y in range(self.matrix.width):
                if self.matrix.is_empty(x, y):
                    item = ' '
                else:
                    item = self.matrix.get_object(x, y).sprite

                print(str(item).ljust(3), end=' ')
            print()

    def displays_statistics(self):
        list_of_creatures = []

        for x in range(self.matrix.height):
            for y in range(self.matrix.width):
                if isinstance(self.matrix.get_object(x, y), (Herbivore, Predator)):
                    list_of_creatures.append(self.matrix.get_object(x, y))

        for creature_iteration in list_of_creatures:
            if isinstance(creature_iteration, Predator):
                print(f'Хищник - {creature_iteration.sprite}; '
                      f'Здоровье - {creature_iteration.hit_point}; '
                      f'Атака - {creature_iteration.attack_power}')
            else:
                print(f'Травоядное - {creature_iteration.sprite}; '
                      f'Здоровье - {creature_iteration.hit_point}; '
                      f'Восстанавливаемое здоровье - {creature_iteration.restore_hp_eat_grass}')
