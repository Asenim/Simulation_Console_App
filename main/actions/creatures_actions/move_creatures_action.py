from main.actions.creatures_actions.path_finding import PathFinder
from main.actions.action import Actions
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator
from main.entity_object.static_objects.grass import Grass


class MoveCreaturesAction(Actions):
    def __init__(self, matrix):
        """
        Класс для перемещения существ по карте
        :param matrix: Получает на вход карту
        """
        self.__matrix = matrix

    def perform(self):
        self.__path_creatures()

    def __path_creatures(self):
        """
        Метод ищет всех существ на карте добавляет их в отдельный
        список
        Затем итерируется по списку существ и создаёт для каждого существа путь
        После создания пути начинает двигать существ
        """
        iterable_creatures_objects_list = []

        for i in range(self.__matrix.height + 2):
            for j in range(self.__matrix.width + 2):
                checked_object = self.__matrix.get_object(i, j)

                if isinstance(checked_object, (Herbivore, Predator)):
                    iterable_creatures_objects_list.append(checked_object)

        for iterable_creature_oject in iterable_creatures_objects_list:

            if isinstance(iterable_creature_oject, Herbivore):
                self.__creates_a_path(self.__matrix, iterable_creature_oject, Grass)

            elif isinstance(iterable_creature_oject, Predator):
                self.__creates_a_path(self.__matrix, iterable_creature_oject, Herbivore)

    def __creates_a_path(self, matrix, creature, food):
        """
        Метод создаёт путь для поиска объектов
        :param matrix: Принимаем на вход карту
        :param creature: Принимаем на вход объект класса существа
        :param food: Принимаем на вход Класс еды
        """
        path = PathFinder(matrix=matrix, creature=creature, food=food)
        path_lists = path.find_path()

        if path_lists is not None:
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
        creatures = self.__matrix.get_object(path[0].x, path[0].y)

        # Если длина пути больше чем скорость существа
        # И на пермещаемой координате - нет никого
        # Перемещаем существо по этим координатам
        # Иначе перемещаем существо на клетку рядом с объектом
        if len(path) > creatures.speed:

            if self.__matrix.is_empty(path[creatures.speed].x, path[creatures.speed].y):
                self.__works_with_map(creatures, path, creatures.speed)
            else:
                self.__works_with_map(creatures, path, creatures.speed-1)

        # В остальных случаях перемещаем существо на одну соседнюю клетку
        # При условии, что она пустая
        else:

            if self.__matrix.is_empty(path[1].x, path[1].y):
                self.__works_with_map(creatures, path, 1)

    def __works_with_map(self, creatures, path, speed):
        """
        Метод для работы с картой
        Он удаляет и добавляет нужные элементы по нужным координатам
        :param creatures: Объект класса существо
        :param path: Список координат являющиеся путём
        :param speed: Отвечает за сдвиг по списку с координатами
        """
        self.__matrix.add_object(creatures, path[speed].x, path[speed].y)
        self.__matrix.change_object_coordinates(
            creatures, path[speed].x, path[speed].y)
        self.__matrix.delete_object(path[0].x, path[0].y)
