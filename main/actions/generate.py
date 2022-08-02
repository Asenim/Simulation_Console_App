"""
Промежуточный класс.
Наследуется от Action.
Есть базовые поля и методы класса.
"""
from main.actions import actions
import random


class Generate(actions.Actions):
    def __init__(self, matrix):
        # Абстрактное количество генерируемых объектов которые необходимо сгенерировать
        self.object_quantity = None
        # Абстрактный счётчик сгенерированных объектов
        self.count_object = None
        # Абстрактный объект
        self.object = None
        # Матрица
        self.matrix = matrix

        # Количество клеток которое есть в матрице
        self.matrix_cells = self.matrix.height * self.matrix.width

    def perform(self):
        """
        Метод позволяющий вызывать
        генерацию.
        """
        self.spawn()

    def count_current(self):
        """
        Метод для подсчёта объектов на матрице
        """
        for x in range(self.matrix.height):
            for y in range(self.matrix.width):
                if self.matrix.is_empty(x, y):
                    pass
                elif self.matrix.get_object(x, y).sprite == self.object.sprite:
                    self.count_object = self.count_object + 1

    def random_coordinates(self):
        """
        Метод позволяющий генерировать
        случайные координаты для наших объектов.
        :return x, y - возвращает два числа.
        """
        while True:
            x = random.randint(0, self.matrix.height - 1)
            y = random.randint(0, self.matrix.width - 1)
            if self.matrix.is_empty(x, y):
                return x, y

    def spawn_object(self, num_1, num_2):
        """
        Абстрактный метод класса.
        В нем будет реализован алгоритм расположения
        объектов на матрице.
        Реализация данного метода происходит
        в классах генерации объектов.
        """
        pass

    def if_dynamic_spawn(self):
        """
        Метод - условие с помощью которого
        мы будем проверять необходимую границу
        для создания дополнительных объектов
        """
        return self.count_object < (self.object_quantity//2)

    def spawn(self):
        """
        Метод в котором будет реализован алгоритм
        генерации координат случайного расположения
        объектов на карте.
        """
        # Подсчёт количества объектов на матрице
        self.count_current()
        # Основной цикл Генерации
        for i in range(self.object_quantity):
            # Генерация случайных индексов матрицы
            num_1, num_2 = self.random_coordinates()
            # Алгоритм генерации самих объектов на матрице
            self.spawn_object(num_1, num_2)

    def dynamic_spawn(self):
        """
        Метод, который позволит создавать
        выбранные объекты если их недостаточно на карте
        """
        if self.if_dynamic_spawn():
            self.spawn()
