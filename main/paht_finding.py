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

        # Временная переменная которая будет показывать путь
        self.count = 0

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
                    herb = self.matrix.get_object(i, j)
                    if herb.sprite == 'Hrb':
                        self.queues.appendleft(((i, j), (i, j)))
                        self.start_point_save = (i, j)
                        # Далее будет вызываться метод path_finder
                        # Который очистит очередь для дальнейшего использования
                        self.path_finder()
                        self.overcome_path()
                        self.moving_object()
                        # После использования всех коллекций очищаем их для корректной работы следующего объекта
                        self.queues.clear()
                        self.sets.clear()

    def path_finder(self):
        """
        Алгоритм поиска пути в ширину.
        """
        # Работает пока очередь не пуста или не выполнено условие остановки
        while len(self.queues) != 0:
            # Забираем координаты стартовой точки
            coordinates = self.queues[0][0]

            # Условие корректного заполнения очереди
            if (0 <= coordinates[0]+1 < self.matrix.height) and (0 <= coordinates[1] < self.matrix.width):
                # Проверяем не находятся ли объекты по этим координатам
                if self.matrix.is_empty(coordinates[0]+1, coordinates[1]):
                    self.queues.append(((coordinates[0]+1, coordinates[1]), (coordinates[0], coordinates[1])))
                # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
                elif self.matrix.get_object(coordinates[0]+1, coordinates[1]).sprite == 'Gs':
                    self.queues.append(((coordinates[0]+1, coordinates[1]), (coordinates[0], coordinates[1])))

            if (0 <= coordinates[0]-1 < self.matrix.height) and (0 <= coordinates[1] < self.matrix.width):
                if self.matrix.is_empty(coordinates[0]-1, coordinates[1]):
                    self.queues.append(((coordinates[0]-1, coordinates[1]), (coordinates[0], coordinates[1])))
                elif self.matrix.get_object(coordinates[0]-1, coordinates[1]).sprite == 'Gs':
                    self.queues.append(((coordinates[0]-1, coordinates[1]), (coordinates[0], coordinates[1])))

            if (0 <= coordinates[0] < self.matrix.height) and (0 <= coordinates[1]+1 < self.matrix.width):
                if self.matrix.is_empty(coordinates[0], coordinates[1]+1):
                    self.queues.append(((coordinates[0], coordinates[1]+1), (coordinates[0], coordinates[1])))
                elif self.matrix.get_object(coordinates[0], coordinates[1]+1).sprite == 'Gs':
                    self.queues.append(((coordinates[0], coordinates[1]+1), (coordinates[0], coordinates[1])))

            if (0 <= coordinates[0] < self.matrix.height) and (0 <= coordinates[1]-1 < self.matrix.width):
                if self.matrix.is_empty(coordinates[0], coordinates[1]-1):
                    self.queues.append(((coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1])))
                elif self.matrix.get_object(coordinates[0], coordinates[1]-1).sprite == 'Gs':
                    self.queues.append(((coordinates[0], coordinates[1]-1), (coordinates[0], coordinates[1])))

            # Извлекаем из очереди первый элемент
            result = self.queues.popleft()
            # Алгоритм для корректного добавления координат в множество
            flag = True
            for element in self.sets:
                if result[0] == element[1]:
                    flag = False
            # Если флаг истинный
            if flag:
                self.sets.update((result,))

            # Останавливаем алгоритм если находим необходимый объект
            if not self.matrix.is_empty(coordinates[0], coordinates[1]):
                if self.matrix.get_object(coordinates[0], coordinates[1]).sprite == 'Gs':
                    self.end_point_save = result[0]
                    self.queues.clear()
                    break

    def overcome_path(self):
        """
        Возвращаем путь
        """
        self.queues.append(self.end_point_save)

        while True:
            # Перебираем наше множество
            for elements in self.sets:
                if (self.queues[0] == elements[0]) and (elements[1] not in self.queues):
                    self.queues.appendleft(elements[1])

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
