from main.actions.generate import Generate
from main.entity_object.static_objects.tree import Tree


class GenerationTree(Generate):
    def __init__(self, matrix):
        """
        Класс генерации Дерева
        :param matrix: принимает на вход объект класса карты
        """
        super().__init__(matrix)
        # Необходимое количество дерева на карте в зависимости от размера матрицы
        self._object_quantity = int(self.matrix_cells * 0.08)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(Tree(num_1, num_2), num_1, num_2)
