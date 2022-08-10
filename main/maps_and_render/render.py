"""
Класс, который вызывает методы генерации
и рисует нашу карту.
"""


class Render:
    def __init__(self, matrix):
        # Принимаем параметры
        self.matrix = matrix

    def print_map(self):
        """
        Отрисовка нашего словаря
        """
        # Основной алгоритм отрисовки
        for x in range(self.matrix.height):
            for y in range(self.matrix.width):
                if self.matrix.is_empty(x, y):
                    item = ' '
                else:
                    item = self.matrix.get_object(x, y).sprite

                print(str(item).ljust(3), end=' ')
            print()
