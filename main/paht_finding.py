from collections import deque
from main import coordinate


class PathFinder:
    def __init__(self, hunter=None, matrix=None):
        """
        Общий класс поиска пути.
        На вход принимает параметры:
        :param hunter: класс, который будет охотиться.
        :param matrix: объект класса карты с которым будем работать

        P.S. Все методы где описана "Опция" - являются расширяемыми и
        дополняемыми после обсуждения и одобрения.
        """
        self.matrix = matrix
        self.hunter = None
        self.victim = None
        # Инициализируем очередь, множество и коллекцию для посещенных объектов
        self.queues = deque()
        self.sets = set()

        # Резервируем начало и конец
        self.start_point_save = None
        self.end_point_save = None

        # Объявляем поля класса
        if hunter.sprite == 'Hrb':
            self.hunter = hunter
            self.victim = 'Gs'
        elif hunter.sprite == 'Prd':
            self.hunter = hunter
            self.victim = 'Hrb'

        if self.hunter is not None:
            coordinated = coordinate.Coordinates(self.hunter.x, self.hunter.y)
            self.queues.appendleft([coordinated])
            self.start_point_save = coordinated

            # Запуск всех методов
            self.path_finder()
            self.print_collections()

    def filling_queue(self, path_list, crd_1, crd_2):
        """
        Метод заполняющий очередь массивом путей
        P.S. Опция - Инкапсуляция.
        :param path_list: принимаем массив координат.
        :param crd_1: принимаем сдвиг по первой координате.
        :param crd_2: принимаем сдвиг по второй координате.
        """
        # Переменная хранящая в себе массив с путем извлеченный мз очереди
        coordinates = path_list

        # Условие корректного заполнения очереди
        if (0 <= coordinates[-1].x + crd_1 < self.matrix.height) and\
                (0 <= coordinates[-1].y + crd_2 < self.matrix.width):

            # Проверяем не находятся ли объекты по этим координатам
            if self.matrix.is_empty(coordinates[-1].x + crd_1, coordinates[-1].y + crd_2):
                coordinated = coordinate.Coordinates(coordinates[-1].x + crd_1, coordinates[-1].y + crd_2)

                if coordinated not in self.sets:
                    new_path_list = path_list.copy()
                    new_path_list.append(coordinated)
                    self.queues.append(new_path_list)

            # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
            elif self.matrix.get_object(coordinates[-1].x + crd_1, coordinates[-1].y + crd_2).sprite == self.victim:
                coordinated = coordinate.Coordinates(coordinates[-1].x + crd_1, coordinates[-1].y + crd_2)
                new_path_list = path_list.copy()
                new_path_list.append(coordinated)
                self.queues.append(new_path_list)

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
                path_list = self.queues.popleft()

                # Заполняем очередь
                self.filling_queue(path_list, +1, 0)
                self.filling_queue(path_list, -1, 0)
                self.filling_queue(path_list, 0, +1)
                self.filling_queue(path_list, 0, -1)

                self.sets.add(path_list[-1])

                # Останавливаем цикл и возвращаем искомый путь для дальнейшего пользования
                if not self.matrix.is_empty(path_list[-1].x, path_list[-1].y):
                    if self.matrix.get_object(path_list[-1].x, path_list[-1].y).sprite == self.victim:
                        self.end_point_save = path_list[-1]
                        """
                        Проверка корректности пути - временный
                        """
                        print('path')
                        for i in path_list:
                            print((i.x, i.y), end='; ')
                        print()

                        # Возвращаем путь
                        return path_list

            elif len(self.queues) == 0:
                break

    def print_collections(self):
        """
        Временный.
        Вывод всех коллекций на экран.
        """
        print('queue')
        for lists in self.queues:
            for j in lists:
                print((j.x, j.y), end='; ')
            print()
        print()
        print('set')
        for i in self.sets:
            print((i.x, i.y), end='; ')
        print()
        print('points')
        print(f'start_point_save = {(self.start_point_save.x, self.start_point_save.y)} \n'
              f'end_point_save = {(self.end_point_save.x, self.end_point_save.y)}')
