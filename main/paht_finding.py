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

        # Резервируем начало и конец
        self.start_point_save = None
        self.end_point_save = None

        # Запуск всех методов
        self.start_point()

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
                        Проверка корректности пути
                        """
                        print('path')
                        for i in path_list:
                            print((i.x, i.y), end='; ')
                        print()

                        # Возвращаем путь
                        return path_list

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
            self.queues.appendleft([coordinated])
            self.start_point_save = coordinated
            # Далее будет вызываться метод path_finder
            # Который очистит очередь для дальнейшего использования
<<<<<<< Updated upstream
            self.path_finder()
<<<<<<< HEAD
            self.return_path()
            """Тут должен будет быть метод return_path"""
=======
            path_list = self.path_finder()
>>>>>>> Stashed changes
=======
>>>>>>> 85841eb (Реализован класс Алгорритма поиска пути)
            self.print_collections()
            # После использования всех коллекций очищаем их для корректной работы следующего объекта
            self.queues.clear()
            self.sets.clear()
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
