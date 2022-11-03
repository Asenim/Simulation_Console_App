from collections import deque
from main import coordinate


class PathFinder:
    def __init__(self, hunter=None, victim=None, matrix=None):
        """
        Общий класс поиска пути.
        На вход принимает параметры:
        :param hunter: класс, который будет охотиться.
        :param victim: класс, на который будут - охотиться.
        :param matrix: объект класса карты с которым будем работать

        P.S. Все методы где описана "Опция" - являются расширяемыми и
        дополняемыми после обсуждения и одобрения.
        """
        self.hunter = hunter
        self.victim = victim
        self.matrix = matrix
        # Инициализируем очередь, множество и коллекцию для посещенных объектов
        self.queues = deque()
        self.sets = set()
        self.graph = dict()

        # Резервируем начало и конец
        self.start_point_save = None
        self.end_point_save = None

        # Запуск всех методов
        self.start_point()

    def return_path(self):
        """
        Временный метод который будет интегрирован в поиск пути
        """
        """
        Примерный алгоритм:
        1) объявляем переменную coordinates и присваиваем ей значение переменной end_point
        2) Включаем цикл while проверяем - есть ли ключ с такими коордитатами в нашем графе (self.graph), 
            если да - добавляем координату coordinates в очередь (self.queue),
            после чего присваиваем ей (coordinates) значение из нашего self.graph и ищем ключ с новыми координатами
        3) Остановка цикла произойдет когда переменная coordinates == start_point
        4) Функция возвращает путь (self.queue) для дальнейшего использования
        """
        coordinates = self.end_point_save
        while True:
            if coordinates in self.graph:
                self.queues.appendleft(coordinates)
                coordinates = self.graph[coordinates]

            if coordinates == self.start_point_save:
                self.queues.appendleft(coordinates)
                break

    def filling_queue(self, coordinates, crd_1, crd_2):
        """
        Метод заполняющий очередь массивом путей
        P.S. Опция - Инкапсуляция.
        :param coordinates: принимаем координаты стартовой точки.
        :param crd_1: принимаем сдвиг по первой координате.
        :param crd_2: принимаем сдвиг по второй координате.
        """
        # Условие корректного заполнения очереди
        if (0 <= coordinates.x + crd_1 < self.matrix.height) and (0 <= coordinates.y + crd_2 < self.matrix.width):

            # Проверяем не находятся ли объекты по этим координатам
            if self.matrix.is_empty(coordinates.x + crd_1, coordinates.y + crd_2):
                coordinated = coordinate.Coordinates(coordinates.x + crd_1, coordinates.y + crd_2)
                """
                Идея - создать словарь который будет хранить в себе два вида координат.
                В качестве ключа будет использоваться координата с которой пришли. 
                    (coordinated).
                В качестве значения будет использоваться координата на которую пришли.
                    (coordinates)
                Словарь (self.graph) будет обрабатываться задом наперед, с точки endpoint к
                точке start point.
                """
                if coordinated not in self.graph:
                    self.graph[coordinated] = coordinates

                if coordinated not in self.sets and coordinated not in self.queues:
                    self.queues.append(coordinated)

            # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
            elif self.matrix.get_object(coordinates.x + crd_1, coordinates.y + crd_2).sprite == self.victim:
                coordinated = coordinate.Coordinates(coordinates.x + crd_1, coordinates.y + crd_2)
                self.queues.append(coordinated)
                self.graph[coordinated] = coordinates

    def path_finder(self):
        """
        Алгоритм поиска пути в ширину.
        Метод возвращает массив с путем
        PS. Опция - Инкапсуляция
        """
        # Работает пока очередь не пуста или не выполнено условие остановки
        while True:
            # Забираем координаты стартовой точки
            if len(self.queues) > 0:
                coordinates = self.queues.popleft()

                if coordinates not in self.graph:
                    self.graph[coordinates] = coordinates

                # Заполняем очередь
                self.filling_queue(coordinates, +1, 0)
                self.filling_queue(coordinates, -1, 0)
                self.filling_queue(coordinates, 0, +1)
                self.filling_queue(coordinates, 0, -1)

                self.sets.update((coordinates,))

                # Останавливаем алгоритм если находим необходимый объект
                if not self.matrix.is_empty(coordinates.x, coordinates.y):
                    if self.matrix.get_object(coordinates.x, coordinates.y).sprite == self.victim:
                        self.end_point_save = coordinates
                        self.queues.clear()
                        break
            elif len(self.queues) == 0:
                break

    def check_objects(self, hunters, x, y):
        """
        Метод для проверки кто у нас охотник и жертва
        и корректной работе алгоритма. (Очистка всех полей класса)
        P.S. Опция - Инкапсуляция.
        :param hunters: в зависимости от этого параметра
         будет определяться жертва.
        :param x: параметр отвечает за координаты и
         корректную работу с ними.
        :param y: то же самое что и x.
        """
        if hunters.sprite == 'Hrb':
            self.hunter = hunters
            self.victim = 'Gs'
        elif hunters.sprite == 'Prd':
            self.hunter = hunters
            self.victim = 'Hrb'

        if self.hunter is not None:
            coordinated = coordinate.Coordinates(x, y)
            self.queues.appendleft(coordinated)
            self.start_point_save = coordinated
            # Далее будет вызываться метод path_finder
            # Который очистит очередь для дальнейшего использования
<<<<<<< Updated upstream
            self.path_finder()
            self.return_path()
            """Тут должен будет быть метод return_path"""
=======
            path_list = self.path_finder()
>>>>>>> Stashed changes
            self.print_collections()
            # После использования всех коллекций очищаем их для корректной работы следующего объекта
            self.queues.clear()
            self.sets.clear()
            self.graph.clear()
            self.start_point_save = None
            self.end_point_save = None
            self.hunter = None
            self.victim = None
            return path_list

    def start_point(self):
        """
        Функция для поиска стартовой позиции
        """
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creatures = self.matrix.get_object(i, j)
                    self.check_objects(creatures, i, j)

    def print_collections(self):
        """
        Временный.
        Вывод всех коллекций на экран.
        """
        print('queue')
        for i in self.queues:
            print((i.x, i.y), end='; ')
        print()
        print('set')
        for i in self.sets:
            print((i.x, i.y), end='; ')
        print()
        print('points')
        print(f'start_point_save = {(self.start_point_save.x, self.start_point_save.y)} \n'
              f'end_point_save = {(self.end_point_save.x, self.end_point_save.y)}')
        print()
        print('Graph:')
        # for key in self.graph:
        #     print((key.x, key.y), [(i.x, i.y) for i in self.graph[key]])
        for key, value in self.graph.items():
            print((key.x, key.y), ':', (value.x, value.y))

    # def overcome_path(self):
    #     """
    #     Возвращаем путь
    #     P.S. Переписать в более классический способ
    #     """
    #     if self.end_point_save is not None:
    #         self.queues.append(self.end_point_save)
    #
    #     while len(self.queues) > 0:
    #         # Перебираем наше множество
    #         for elements in self.sets:
    #             if (self.queues[0] == elements.coordinates[0]) and (elements.coordinates[1] not in self.queues):
    #                 self.queues.appendleft(elements.coordinates[1])
    #
    #         if self.start_point_save == self.queues[0]:
    #             break

    # def moving_object(self):
    #     """
    #                     Метод двигающий объект к цели.
    #                     Первое время он показываем путь, который проходит объект.
    #                     P.S. Вынести в методы существ
    #                     """
    #     # Двигаем объект к цели
    #     """
    #     1) Если длина пути больше двух:
    #     2) Вынимаем объект из карты
    #     3) Запускаем цикл for равной длине нашей очереди или
    #     (Количеству клеток которое может пройти существо за одну итерацию):
    #         4) Вынимаем координаты из очереди
    #         5) Если это не первый и не последний элемент в очереди:
    #             6) Начинаем перемещение объекта следующим образом:
    #                     Добавляем объект по новым координатам в словарь
    #                     Резервируем старые координаты в переменную
    #                     Удаляем объект по старым координатам
    #     """
    #     if len(self.queues) > 2:
    #         objects = self.matrix.get_object(self.start_point_save[0], self.start_point_save[1])
    #         # Параметр range будет принимать параметр скорости существ
    #         for element in range(2):
    #             coordinates = self.queues[element]
    #             if (coordinates != self.queues[0]) and (coordinates != self.queues[-1]):
    #                 self.matrix.add_object(objects, coordinates[0], coordinates[1])
    #                 coordinates_del = self.queues[element-1]
    #                 self.matrix.delete_objects(coordinates_del[0], coordinates_del[1])
    #

# class Coordinates:
#     def __init__(self, coordinates):
#         """
#         Класс принимающий в себя координаты и распаривающий их.
#         """
#         # Хранит в себе кортеж с двумя кортежами внутри которых лежат координаты
#         self.coordinates = coordinates
#         # crd_1 и crd_2 - хранят в себе первый и второй кортежи координат
#         self.coordinate_1 = self.coordinates[0]
#         self.coordinate_2 = self.coordinates[1]
#         # х и у - хранят в себе элементы первого кортежа
#         self.x = self.coordinates[0][0]
#         self.y = self.coordinates[0][1]
#
#     def __eq__(self, other):
#         return self.coordinates == self.coordinates
