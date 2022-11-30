"""
Класс, который вызывает методы генерации
и рисует нашу карту.
"""
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator


class Render:
    def __init__(self, matrix):
        """
        Отрисовка карты и статуса существ
        :param matrix: Принимаем на вход объект карты
        """
        # Принимаем параметры
        self.matrix = matrix

    def print_map(self):
        """
        Отрисовка нашего словаря
        Сдвиг на +2 сделан для корректного добавления границ карты
        При измененнии границ отрисовки в этом методе так же надо
        будет изменить границы в следующих классах: (Класс: Методы)
            simulation: stops_the_loop
            render: displays_statistics
            generate: count_current, random_coordinates
            path_finding: __filling_queue
            move_creatures_action: __path_creatures
            action_eat_object: __search_hunter, __search_food
        """
        # Основной алгоритм отрисовки
        for x in range(self.matrix.height+2):
            for y in range(self.matrix.width+2):
                if self.matrix.is_empty(x, y):
                    if x == 0 or x == self.matrix.height+1:
                        item = '==='
                    elif y == 0 or y == self.matrix.width+1:
                        item = '||'
                    else:
                        item = ' '
                else:
                    item = self.matrix.get_object(x, y).sprite

                print(str(item).ljust(3), end=' ')
            print()

    def displays_statistics(self):
        list_of_creatures = []

        for x in range(self.matrix.height+2):
            for y in range(self.matrix.width+2):
                if isinstance(self.matrix.get_object(x, y), (Herbivore, Predator)):
                    list_of_creatures.append(self.matrix.get_object(x, y))

        for creature_iteration in list_of_creatures:
            if isinstance(creature_iteration, Predator):
                print(f'Хищник - {creature_iteration.sprite}; '
                      f'Скорость = {creature_iteration.speed}; '
                      f'Здоровье - {creature_iteration.hit_point}; '
                      f'Атака - {creature_iteration.attack_power}')
            else:
                print(f'Травоядное - {creature_iteration.sprite}; '
                      f'Скорость = {creature_iteration.speed}; '
                      f'Здоровье - {creature_iteration.hit_point}; '
                      f'Регенерация - {creature_iteration.restore_hp_eat_grass}')
