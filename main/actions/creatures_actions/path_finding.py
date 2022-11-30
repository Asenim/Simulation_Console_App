from collections import deque
from main import coordinate


class PathFinder:
    def __init__(self, creature=None, food=None, matrix=None):
        """
        Общий класс поиска пути.
        На вход принимает параметры:
        :param creature: класс, который будет охотиться.
        :param matrix: объект класса карты с которым будем работать
        """
        self.matrix = matrix
        self.__creature = creature
        self.__food = food
        # Инициализируем очередь, множество и коллекцию для посещенных объектов
        self.__queue_of_pass = deque()
        self.__set_of_visited = set()

        coordinated = coordinate.Coordinates(self.__creature.x, self.__creature.y)
        self.__queue_of_pass.append([coordinated])

    def find_path(self):
        """
        Алгоритм поиска пути в ширину.
        Метод возвращает массив с путем или заканчивает поиск если искомый объект не найден.
        :return coordinate_list: coordinate_list[0] - это точка на которой расположен охотник,
        coordinate_list[-1] - это точка на которой расположена добыча, что бы встать "возле" добычи
        нужно исключить последний индекс
        """
        # Работает пока очередь не пуста или не выполнено условие остановки
        while True:
            if len(self.__queue_of_pass) > 0:
                coordinate_list = self.__queue_of_pass.popleft()
                coordinate_shift_list = [[+1, 0], [-1, 0], [0, +1], [0, -1],
                                         [+1, +1], [+1, -1], [-1, +1], [-1, -1]]

                for coordinate_shift in coordinate_shift_list:
                    self.__filling_queue(coordinate_list, coordinate_shift[0], coordinate_shift[1])

                self.__set_of_visited.add(coordinate_list[-1])

                # Останавливаем цикл и возвращаем искомый путь для дальнейшего пользования
                if not self.matrix.is_empty(coordinate_list[-1].x, coordinate_list[-1].y):
                    if isinstance(self.matrix.get_object(coordinate_list[-1].x, coordinate_list[-1].y), self.__food):

                        return coordinate_list

            else:
                return None

    def __filling_queue(self, path_list, crd_1, crd_2):
        """
        Метод заполняющий очередь массивом путей
        :param path_list: принимаем массив координат.
        :param crd_1: принимаем сдвиг по первой координате.
        :param crd_2: принимаем сдвиг по второй координате.
        """
        current_position_coordinate = path_list[-1]

        # Условие выхода за границы поля
        if (0 < current_position_coordinate.x + crd_1 < self.matrix.height+1) and (
                0 < current_position_coordinate.y + crd_2 < self.matrix.width+1):

            # Проверяем не находятся ли объекты по этим координатам
            if self.matrix.is_empty(current_position_coordinate.x + crd_1, current_position_coordinate.y + crd_2):
                adjeccent_coordinate = coordinate.Coordinates(
                    current_position_coordinate.x + crd_1, current_position_coordinate.y + crd_2)

                if adjeccent_coordinate not in self.__set_of_visited:
                    new_path_list = path_list.copy()
                    new_path_list.append(adjeccent_coordinate)
                    self.__queue_of_pass.append(new_path_list)

            # Если вдруг по проверяемым координатам находится искомый объект - то добавляем его в очередь
            elif isinstance(self.matrix.get_object(
                        current_position_coordinate.x + crd_1, current_position_coordinate.y + crd_2), self.__food):

                adjeccent_coordinate = coordinate.Coordinates(
                    current_position_coordinate.x + crd_1, current_position_coordinate.y + crd_2)
                new_path_list = path_list.copy()
                new_path_list.append(adjeccent_coordinate)
                self.__queue_of_pass.append(new_path_list)
