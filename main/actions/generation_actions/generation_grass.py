from main.actions.generate import Generate
from main.entitys.simulation_objects.static_objects.grass import Grass


class GenerationGrass(Generate):
    def __init__(self, matrix):
        """
        Класс генерации Травы
        :param matrix: принимает на вход объект класса карты
        """
        super().__init__(matrix)
        # Необходимое количество травы на карте в зависимости от размера матрицы
        self._object_quantity = int(self.matrix_cells * 0.2)
        # Счётчик травы
        self.count_object = 0

    def perform(self):
        self.count_current()
        if self.if_dynamic_spawn():
            self.spawn()

    def count_current(self):
        """
        Метод для подсчёта травы на матрице
        для использования if_dynamic_spawn
        """

        # Для понимания границ в цикле - загляните в
        # метод print_map класса Render
        for x in range(self.matrix.height+2):
            for y in range(self.matrix.width+2):
                if self.matrix.is_empty(x, y):
                    pass
                elif isinstance(self.matrix.get_object(x, y), Grass):
                    self.count_object = self.count_object + 1

    def if_dynamic_spawn(self):
        """
        Метод - условие с помощью которого
        мы будем проверять необходимую границу
        для создания дополнительных объектов
        :return: True - если количество объектов на нашей карте
            < чем необходимое количество объектов, иначе False
        """
        return self.count_object <= (self._object_quantity // 2 + 1)

    def spawn(self):
        """
        Метод в котором будет реализован алгоритм
        генерации координат случайного расположения
        объектов на карте.
        """
        # Основной цикл Генерации
        for i in range(self._object_quantity // 2):
            # Генерация случайных индексов матрицы
            num_1, num_2 = self.random_coordinates()
            # Алгоритм генерации самих объектов на матрице
            self.spawn_object(num_1, num_2)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(Grass(num_1, num_2), num_1, num_2)
        # После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
        self.count_object = 0
