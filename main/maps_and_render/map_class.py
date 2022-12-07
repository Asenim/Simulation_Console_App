from main import coordinate


class Map:
    def __init__(self, height, width):
        """
        Класс карты принимающий на вход два параметра
        :param height: высота
        :param width: ширина
        """
        # Проверка на передачу элементов
        if isinstance(height, int) and isinstance(width, int):
            self.height = height
            self.width = width
        else:
            print("Введите целые числа")

        self.__dict_object = {}

    def add_object(self, objects, x, y):
        """
        Метод позволяющий добавлять
        данные в словарь.
        :param objects: объект который мы будем добавлять в словарь
        :param x: координата объекта
        :param y: координата объекта
        """
        coordinates = coordinate.Coordinates(x, y)
        self.__dict_object[coordinates] = objects

    def get_object(self, x, y):
        """
        Метод позволяющий доставать
        значения из словаря по координатам.
        :param x: координата объекта
        :param y: координата объекта
        :return: объект находящийся по переданным координатам
        """
        coordinates = coordinate.Coordinates(x, y)
        if coordinates in self.__dict_object:
            return self.__dict_object[coordinates]

    def is_empty(self, x, y):
        """
        Метод для проверки наличия
        координат в словаре.
        :param x: координата объекта
        :param y: координата объекта
        :return: Если координат нет в словаре возвращает True,
        если они есть в словаре возвращает False
        """
        coordinates = coordinate.Coordinates(x, y)
        if coordinates not in self.__dict_object:
            return True
        else:
            return False

    def delete_object(self, x, y):
        """
        Метод позволяющий удалять объект с карты
        :param x: координата объекта
        :param y: координата объекта
        """
        coordinates = coordinate.Coordinates(x, y)
        del self.__dict_object[coordinates]

    @staticmethod
    def change_object_coordinates(creature, new_x, new_y):
        """
        Метод меняет поля координат существ, на новые
        :param creature: Передаётся объект существа
        :param new_x: Передаётся координата по х
        :param new_y: Передаётся координата по у
        """
        creature.x = new_x
        creature.y = new_y

    def map_size(self):
        """
        Метода возвращающий размер карты
        :return: кортеж координат (x, y)
        """
        x = self.height
        y = self.width
        return x, y
