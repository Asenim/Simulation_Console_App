from main.actions.creatures_actions.path_finding import PathFinder
from main.actions import action
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator
from main.entity_object.static_objects.grass import Grass


class MoveCreaturesAction(action.Actions):
    def __init__(self, matrix):
        """
        Класс для перемещения существ по карте
        :param matrix: Получает на вход карту
        """
        self.matrix = matrix

    def perform(self):
        self.__path_creatures()

    def __path_creatures(self):
        """
        Метод ищет всех существ на карте добавляет их в отдельный
        список
        Затем итерируется по списку существ и создаёт для каждого существа путь
        После создания пути начинает двигать существ
        """
        iterable_creature_coordinates_list = []

        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                checked_object = self.matrix.get_object(i, j)

                if isinstance(checked_object, (Herbivore, Predator)):
                    iterable_creature_coordinates_list.append(checked_object)

        for iterable_creature in iterable_creature_coordinates_list:

            if isinstance(iterable_creature, Herbivore):
                self.__creates_a_path(self.matrix, iterable_creature, Grass)

            elif isinstance(iterable_creature, Predator):
                self.__creates_a_path(self.matrix, iterable_creature, Herbivore)

    def __creates_a_path(self, matrix, creature, food):
        """
        Метод создаёт путь для поиска объектов
        :param matrix: Принимаем на вход карту
        :param creature: Принимаем на вход объект класса существа
        :param food: Принимаем на вход Класс еды
        """
        path = PathFinder(matrix=matrix, creature=creature, food=food)
        path_lists = path.find_path()

        # Вывод в консоль - подлежит удалению
        print(f'Готовый путь {creature.sprite}\n'
              f'Скорость существа - {creature.speed}\n'
              f'Здоровье существа - {creature.hit_point}')

        if path_lists is not None:
            for crd in path_lists:
                print((crd.x, crd.y), end='; ')
            print()
            self.__move_creature(path_lists)
        else:
            print('Пути нет')

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
