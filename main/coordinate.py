class Coordinates:
    def __init__(self, coordinates):
        """
        Класс принимающий в себя координаты и распаривающий их.
        """
        self.coordinates = coordinates
        self.x = coordinates[0][0]
        self.y = coordinates[0][1]

    def __eq__(self, other):
        """
        Если значения в кортеже равны у двух объектов:
        Возвращает True
        """
        return self.coordinates == other.coordinates

    #
    def __hash__(self):
        return hash(self.coordinates)

