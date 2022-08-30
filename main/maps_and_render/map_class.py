class Map:
    def __init__(self, height, width):
        # Проверка на передачу элементов
        if isinstance(height, int) and isinstance(width, int):
            self.height = height
            self.width = width
        else:
            print("Введите целые числа")

        # Переменная в которой хранится карта (словарь)
        self.__dict_object = {}

    def add_object(self, objects, x, y):
        """
        Метод позволяющий добавлять
        данные в словарь.
        """
        coordinates = (x, y)
        self.__dict_object[coordinates] = objects

    def get_object(self, x, y):
        """
        Метод позволяющий доставать
        значения из словаря.
        """
        coordinates = (x, y)
        if coordinates in self.__dict_object:
            return self.__dict_object[coordinates]

    def is_empty(self, x, y):
        """
        Метод для проверки наличия
        координат в словаре.
        """
        coordinates = (x, y)
        if coordinates not in self.__dict_object:
            return True
        else:
            return False

    def delete_objects(self, x, y):
        coordinates = (x, y)
        del self.__dict_object[coordinates]

    def map_size(self):
        x = self.height
        y = self.width
        return x, y
