from collections import deque


class PathFinder:
    def __init__(self, hunter=None, victim=None, matrix=None):
        """
        Общий класс поиска пути.
        На вход принимает параметры:
        :param hunter: класс, который будет охотиться.
        :param victim: класс, на который будут - охотится.
        :param matrix: объект класса карты с которым будем работать
        """
        self.hunter = hunter
        self.victim = victim
        self.matrix = matrix
        # Инициализируем очередь и множество
        self.queues = deque()
        self.sets = set()

        # Резервируем начало и конец
        self.start_point_save = None
        self.end_point_save = None

        # Запуск всех методов
        self.start_point()
        self.print_collections()

    def start_point(self):
        """
        Функция для добавления стартовой позиции
        """
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creatures = self.matrix.get_object(i, j)
                    if creatures.sprite == 'Hrb':
                        self.hunter = creatures
                        self.victim = 'Gs'
                        coordinated = Coordinates(((i, j), (i, j)))
                        self.queues.appendleft(coordinated)
                        self.start_point_save = coordinated.coordinate_1
                        # Далее будет вызываться метод path_finder
                        # Который очистит очередь для дальнейшего использования
                        self.path_finder()
                        self.overcome_path()
                        self.moving_object()
                        # После использования всех коллекций очищаем их для корректной работы следующего объекта
                        self.queues.clear()
                        self.sets.clear()

    def filling_queue(self, coordinates, crd_1, crd_2):
        """
        Метод позволяющий заполнять корректно очередь
        для поиска пути.
        :param coordinates: принимаем координаты стартовой точки.
        :param crd_1: принимаем сдвиг по первой координате.
        :param crd_2: принимаем сдвиг по второй координате.
        """
        # Условие корректного заполнения очереди
        if (0 <= coordinates.x + crd_1 < self.matrix.height) and (0 <= coordinates.y + crd_2 < self.matrix.width):
            # Проверяем не находятся ли объекты по этим координатам
            if self.matrix.is_empty(coordinates.x + crd_1, coordinates.y + crd_2):
                coordinated = Coordinates(((coordinates.x + crd_1, coordinates.y + crd_2),
                                           (coordinates.x, coordinates.y)))
                self.queues.append(coordinated)
            # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
            elif self.matrix.get_object(coordinates.x + crd_1, coordinates.y + crd_2).sprite == self.victim:
                coordinated = Coordinates(((coordinates.x + crd_1, coordinates.y + crd_2),
                                           (coordinates.x, coordinates.y)))
                self.queues.append(coordinated)

    def path_finder(self):
        """
        Алгоритм поиска пути в ширину.
        """
        # Работает пока очередь не пуста или не выполнено условие остановки
        while len(self.queues) < 1:
            # Забираем координаты стартовой точки
            coordinates = self.queues[0]

            self.filling_queue(coordinates, +1, 0)
            self.filling_queue(coordinates, -1, 0)
            self.filling_queue(coordinates, 0, +1)
            self.filling_queue(coordinates, 0, -1)

            # Извлекаем из очереди первый элемент
            result = self.queues.popleft()
            # Алгоритм для корректного добавления координат в множество
            flag = True
            for element in self.sets:
                if result.coordinate_1 == element.coordinate_2:
                    flag = False
                    break

            # Если флаг истинный добавляем в множество наш кортеж
            if flag:
                self.sets.update((result,))

            # Останавливаем алгоритм если находим необходимый объект
            if not self.matrix.is_empty(coordinates.x, coordinates.y):
                if self.matrix.get_object(coordinates.x, coordinates.y).sprite == self.victim:
                    self.end_point_save = result.coordinate_1
                    self.queues.clear()
                    break

    def overcome_path(self):
        """
        Возвращаем путь
        """
        self.queues.append(self.end_point_save)

        while len(self.queues) < 1:
            # Перебираем наше множество
            for elements in self.sets:
                if (self.queues[0] == elements.coordinate_1) and (elements.coordinate_2 not in self.queues):
                    self.queues.appendleft(elements.coordinate_2)

            if self.start_point_save == self.queues[0]:
                break

    def moving_object(self):
        """
        Метод двигающий объект к цели.
        Первое время он показываем путь, который проходит объект
        """
        # Двигаем объект к цели
        """
        1) Если длина пути больше двух:
        2) Вынимаем объект из карты
        3) Запускаем цикл for равной длине нашей очереди или 
        (Количеству клеток которое может пройти существо за одну итерацию):
            4) Вынимаем координаты из очереди
            5) Если это не первый и не последний элемент в очереди:
                6) Начинаем перемещение объекта следующим образом:
                        Добавляем объект по новым координатам в словарь
                        Резервируем старые координаты в переменную
                        Удаляем объект по старым координатам 
        """
        if len(self.queues) > 2:
            objects = self.matrix.get_object(self.start_point_save[0], self.start_point_save[1])
            # Параметр range будет принимать параметр скорости существ
            for element in range(2):
                coordinates = self.queues[element]
                if (coordinates != self.queues[0]) and (coordinates != self.queues[-1]):
                    self.matrix.add_object(objects, coordinates[0], coordinates[1])
                    coordinates_del = self.queues[element-1]
                    self.matrix.delete_objects(coordinates_del[0], coordinates_del[1])

    def print_collections(self):
        """
        Временный.
        Вывод всех коллекций на экран.
        """
        print('queue')
        print(self.queues)
        print('set')
        print(self.sets)
        print('points')
        print(f'start_point_save = {self.start_point_save} \n'
              f'end_point_save = {self.end_point_save}')


class Coordinates:
    def __init__(self, coordinates):
        """
        Класс принимающий в себя координаты и распаривающий их.
        """
        # Хранит в себе кортеж с двумя кортежами внутри которых лежат координаты
        self.coordinates = coordinates
        # crd_1 и crd_2 - хранят в себе первый и второй кортежи координат
        self.coordinate_1 = self.coordinates[0]
        self.coordinate_2 = self.coordinates[1]
        # х и у - хранят в себе элементы первого кортежа
        self.x = self.coordinates[0][0]
        self.y = self.coordinates[0][1]
