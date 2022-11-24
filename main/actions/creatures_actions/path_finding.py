from collections import deque
from main import coordinate
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator


class PathFinder:
    def __init__(self, creature=None, matrix=None):
        """
        Общий класс поиска пути.
        На вход принимает параметры:
        :param creature: класс, который будет охотиться.
        :param matrix: объект класса карты с которым будем работать

        P.S. Все методы где описана "Опция" - являются расширяемыми и
        дополняемыми после обсуждения и одобрения.
        """
        self.matrix = matrix
        self.__hunter = None
        self.__victim = None
        # Инициализируем очередь, множество и коллекцию для посещенных объектов
        self.__queue_of_pass = deque()
        self.__set_of_visited = set()

        # Объявляем поля класса
        # if hunter.sprite == 'Hrb':
        if isinstance(creature, Herbivore):
            self.__hunter = creature
            self.__victim = 'Gs'
        elif isinstance(creature, Predator):
            self.__hunter = creature
            self.__victim = 'Hrb'

        # if self.__hunter is not None and self.__victim is not None:
        coordinated = coordinate.Coordinates(self.__hunter.x, self.__hunter.y)
        self.__queue_of_pass.append([coordinated])

    def __filling_queue(self, path_list, crd_1, crd_2):
        """
        Метод заполняющий очередь массивом путей
        P.S. Опция - Инкапсуляция.
        :param path_list: принимаем массив координат.
        :param crd_1: принимаем сдвиг по первой координате.
        :param crd_2: принимаем сдвиг по второй координате.
        """
        # Переменная хранящая в себе массив с путем извлеченный мз очереди
        coordinates = path_list[-1]

        # Условие корректного заполнения очереди
        if (0 <= coordinates.x + crd_1 < self.matrix.height) and (0 <= coordinates.y + crd_2 < self.matrix.width):

            # Проверяем не находятся ли объекты по этим координатам
            if self.matrix.is_empty(coordinates.x + crd_1, coordinates.y + crd_2):
                coordinated = coordinate.Coordinates(coordinates.x + crd_1, coordinates.y + crd_2)

                if coordinated not in self.__set_of_visited:
                    new_path_list = path_list.copy()
                    new_path_list.append(coordinated)
                    self.__queue_of_pass.append(new_path_list)

            # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
            elif self.matrix.get_object(coordinates.x + crd_1, coordinates.y + crd_2).sprite == self.__victim:
                coordinated = coordinate.Coordinates(coordinates.x + crd_1, coordinates.y + crd_2)
                new_path_list = path_list.copy()
                new_path_list.append(coordinated)
                self.__queue_of_pass.append(new_path_list)

    def find_path(self):
        """
        Алгоритм поиска пути в ширину.
        Метод возвращает массив с путем или заканчивает поиск если искомый объект не найден.
        :return path_list: path_list[0] - это точка на которой расположен охотник,
        path_list[-1] - это точка на которой расположена добыча, что бы встать "возле" добычи
        нужно исключить последний индекс
        """
        # Работает пока очередь не пуста или не выполнено условие остановки
        while True:
            # Забираем координаты стартовой точки
            if len(self.__queue_of_pass) > 0:
                path_list = self.__queue_of_pass.popleft()

                # Заполняем очередь
                self.__filling_queue(path_list, +1, 0)
                self.__filling_queue(path_list, -1, 0)
                self.__filling_queue(path_list, 0, +1)
                self.__filling_queue(path_list, 0, -1)

                self.__set_of_visited.add(path_list[-1])

                # Останавливаем цикл и возвращаем искомый путь для дальнейшего пользования
                if not self.matrix.is_empty(path_list[-1].x, path_list[-1].y):
                    if self.matrix.get_object(path_list[-1].x, path_list[-1].y).sprite == self.__victim:

                        return path_list

            elif len(self.__queue_of_pass) == 0:
                return None
