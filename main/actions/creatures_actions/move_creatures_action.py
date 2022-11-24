from main.actions.creatures_actions import path_finding
from main.actions import action
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator


class MoveCreaturesAction(action.Actions):
    def __init__(self, matrix):
        """
        Класс для перемещения существ по карте
        :param matrix: Получает на вход карту
        """
        self.matrix = matrix

    def perform(self):
        self.__paht_creatures()

    def __paht_creatures(self):
        """
        Функция для поиска стартовой позиции
        Сначала ищется стартовая позиция объекта.
        Затем создается объект класса поиска пути.
        Потом поправляются индексы на актуальные.
        После этого создаётся объект и вызывается метод поиска.
        Если путь найден - он возвращается в переменную и затем
            передаётся в метод двигающих существ.
        Под конец сходивший объект добавляется в список существ
            которые сделали свой ход.
        """
        iterable_creature_coordinates_list = []

        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                checked_object = self.matrix.get_object(i, j)
                if isinstance(checked_object, (Herbivore, Predator)):
                    iterable_creature_coordinates_list.append(checked_object)

        for iterable_creature in iterable_creature_coordinates_list:
            path = path_finding.PathFinder(matrix=self.matrix, creature=iterable_creature)
            path_lists = path.find_path()
            if path_lists is not None:
                # Вывод в консоль - подлежит удалению
                print(f'Готовый путь {iterable_creature.sprite}\n'
                      f'Скорость существа - {iterable_creature.speed}\n'
                      f'Здоровье существа - {iterable_creature.hit_point}')
                for crd in path_lists:
                    print((crd.x, crd.y), end='; ')
                print()
                self.__move_creature(path_lists)
            else:
                print('Пути нет')

        # Список в котором будут храниться существа сделавшие ход
        # moving_creatures = []
        #
        # for i in range(self.matrix.height):
        #     for j in range(self.matrix.width):
        #         if not self.matrix.is_empty(i, j):
        #             creatures = self.matrix.get_object(i, j)
        #             if isinstance(creatures, (Herbivore, Predator)):
        #                 creatures.x = i
        #                 creatures.y = j
        #                 path = path_finding.PathFinder(matrix=self.matrix, creature=creatures)
        #                 path_lists = path.find_path()
        #                 if path_lists is not None and creatures not in moving_creatures:
        #                     # print(f'Готовый путь {creatures.sprite}\n'
        #                     #       f'Скорость существа - {creatures.speed}\n'
        #                     #       f'Здоровье существа - {creatures.hit_point}'
        #                     # for crd in path_lists:
        #                     #     print((crd.x, crd.y), end='; ')
        #                     # print()
        #                     self.__move_creature(path_lists)
        #                     moving_creatures.append(creatures)

    def __move_creature(self, path_list):
        """
        Метод который позволяет перемещать существ на карте
        :param path_list: Принимает на вход готовый путь
        """
        # Список содержащий объекты координат
        path = path_list
        creatures = self.matrix.get_object(path[0].x, path[0].y)

        if len(path) > creatures.speed:
            if self.matrix.is_empty(path[creatures.speed].x, path[creatures.speed].y):
                self.matrix.add_object(creatures, path[creatures.speed].x, path[creatures.speed].y)
                self.matrix.change_object_coordinates(creatures, path[creatures.speed].x, path[creatures.speed].y)
                self.matrix.delete_object(path[0].x, path[0].y)
            else:
                self.matrix.add_object(creatures, path[creatures.speed-1].x, path[creatures.speed-1].y)
                self.matrix.change_object_coordinates(creatures, path[creatures.speed-1].x, path[creatures.speed-1].y)
                self.matrix.delete_object(path[0].x, path[0].y)

        elif len(path) > 2:
            if self.matrix.is_empty(path[1].x, path[1].y):
                self.matrix.add_object(creatures, path[1].x, path[1].y)
                self.matrix.change_object_coordinates(creatures, path[1].x, path[1].y)
                self.matrix.delete_object(path[0].x, path[0].y)

        #   if len(path) == creatures.speed:
        #    self.matrix.add_object(creatures, path[creatures.speed-1].x, path[creatures.speed-1].y)
        #    self.matrix.change_object_coordinates(creatures, path[creatures.speed-1].x, path[creatures.speed-1].y)
        #    self.matrix.delete_object(path[0].x, path[0].y)
        #   else:
        #    self.matrix.add_object(creatures, path[creatures.speed].x, path[creatures.speed].y)
        #    self.matrix.change_object_coordinates(creatures, path[creatures.speed].x, path[creatures.speed].y)
        #    self.matrix.delete_object(path[0].x, path[0].y)
        # elif len(path) <= 2:
        #     self.matrix.add_object(creatures, path[1].x, path[1].y)
        #     self.matrix.change_object_coordinates(creatures, path[1].x, path[1].y)
        #     self.matrix.delete_object(path[0].x, path[0].y)
