from main.actions.action import Actions
import random


class Generate(Actions):
    def __init__(self, matrix):
        """
        Промежуточный класс, от этого класса наследуется вся генерация объектов
        :param matrix: Принимаем объект карты
        """
        self._object_quantity = None
        self.matrix = matrix

        self.matrix_cells = self.matrix.height * self.matrix.width

    def perform(self):
        """
        Метод позволяющий вызывать
        генерацию.
        """
        self.spawn()

    def spawn(self):
        """
        Метод в котором будет реализован алгоритм
        генерации координат случайного расположения
        объектов на карте.
        """
        for i in range(self._object_quantity):
            # Генерация случайных индексов матрицы
            num_1, num_2 = self.random_coordinates()
            # Алгоритм генерации самих объектов на матрице
            self.spawn_object(num_1, num_2)

    def random_coordinates(self):
        """
        Метод позволяющий генерировать
        случайные координаты для наших объектов.
        Размещение объектов начинается с левой границы +1,
        заканчивается по ширине и высоте карты
        :return x, y - возвращает два числа
        """
        while True:
            x = random.randint(1, self.matrix.height)
            y = random.randint(1, self.matrix.width)
            if self.matrix.is_empty(x, y):
                return x, y

    def spawn_object(self, num_1, num_2):
        """
        Абстрактный метод класса.
        В нем будет реализован алгоритм расположения
        объектов на матрице.
        Реализация данного метода происходит
        в классах генерации объектов.
        :param num_1: координата x расположения объекта
        :param num_2: координата y расположения объекта
        """
        pass
