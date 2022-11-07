class Coordinates:
    def __init__(self, x, y):
        """
        Класс принимающий в себя координаты и распаривающий их.
        """
        self.x = x
        self.y = y

    def __eq__(self, other):
        """
        Если значения в кортеже равны у двух объектов:
        :return: True или False
        """
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.__class__ and self.x and self.y)
