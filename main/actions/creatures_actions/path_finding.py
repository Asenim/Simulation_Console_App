from collections import deque
from main.coordinate import Coordinates


class PathFinder:
    def __init__(self, creature=None, food=None, matrix=None):
        """
        Общий класс поиска пути.
        Инициализатор Добавляет первую координату,
            на ноторой находится существо в очередь.
        На вход принимает параметры:
        :param creature: класс, который будет охотиться
        :param food: Принимает на вход класс на который ведется охота
        :param matrix: объект класса карты с которым будем работать

        """
        self.__matrix = matrix
        self.__creature = creature
        self.__food = food
        # Инициализируем очередь, множество и коллекцию для посещенных объектов
        self.__queue_of_pass = deque()
        self.__set_of_visited = set()

        coordinated = Coordinates(self.__creature.x, self.__creature.y)
        self.__queue_of_pass.append([coordinated])

    def find_path(self):
        """
        Алгоритм поиска пути в ширину.
        Метод возвращает массив с путем или заканчивает поиск если искомый объект не найден.
        :return coordinate_list: coordinate_list[0] - это точка на которой расположен охотник,
        coordinate_list[-1] - это точка на которой расположена добыча, что бы встать "возле" добычи
        нужно исключить последний индекс
        """
        while True:
            if len(self.__queue_of_pass) > 0:
                coordinate_list = self.__queue_of_pass.popleft()
                coordinate_shift_list = [[+1, 0], [-1, 0], [0, +1], [0, -1],
                                         [+1, +1], [+1, -1], [-1, +1], [-1, -1]]

                for coordinate_shift in coordinate_shift_list:
                    self.__filling_queue(coordinate_list, coordinate_shift[0], coordinate_shift[1])

                self.__set_of_visited.add(coordinate_list[-1])

                if not self.__matrix.is_empty(coordinate_list[-1].x, coordinate_list[-1].y):
                    if isinstance(
                            self.__matrix.get_object(coordinate_list[-1].x, coordinate_list[-1].y),
                            self.__food):

                        return coordinate_list

            else:
                return None

    def __filling_queue(self, coordinates_list, crd_x, crd_y):
        """
        Метод заполняющий очередь массивом путей
        :param coordinates_list: принимаем массив координат.
        :param crd_x: принимаем сдвиг по первой координате.
        :param crd_y: принимаем сдвиг по второй координате.
        """
        current_position_coordinate = coordinates_list[-1]

        # Условие выхода за границы поля
        if (0 < current_position_coordinate.x + crd_x < self.__matrix.height + 1) and (
                0 < current_position_coordinate.y + crd_y < self.__matrix.width + 1):

            # Проверяем не находятся ли объекты по этим координатам
            if self.__matrix.is_empty(
                    current_position_coordinate.x + crd_x, current_position_coordinate.y + crd_y):
                adjeccent_coordinate = Coordinates(
                    current_position_coordinate.x + crd_x, current_position_coordinate.y + crd_y)

                # Проверка нет ли данных координат в множестве посещенных координат
                if adjeccent_coordinate not in self.__set_of_visited:
                    self.__new_path(coordinates_list, adjeccent_coordinate)

            # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
            elif isinstance(
                    self.__matrix.get_object(
                        current_position_coordinate.x + crd_x, current_position_coordinate.y + crd_y),
                    self.__food):

                adjeccent_coordinate = Coordinates(
                    current_position_coordinate.x + crd_x, current_position_coordinate.y + crd_y)
                self.__new_path(coordinates_list, adjeccent_coordinate)

    def __new_path(self, path, coordinate):
        """
        Метод создаёт новый путь (список),
        # Создаётся копия списка путей
        # В копию добавляются новые координаты
        # Копия отправляется в очередь
        :param path: Принимаем на вход старый путь
        :param coordinate: Принимаем на вход координаты которые будем добавлять
            в новый путь
        """
        new_path_list = path.copy()
        new_path_list.append(coordinate)
        self.__queue_of_pass.append(new_path_list)
