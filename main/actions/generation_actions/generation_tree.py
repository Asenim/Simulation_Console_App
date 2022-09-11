from main.actions import generate
from main.entity_object.static_objects import tree


class GenerationTree(generate.Generate):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Необходимое количество дерева на карте в зависимости от размера матрицы
        self.object_quantity = int(self.matrix_cells * 0.1)
        # Счетчик дерева
        self.count_object = 0
        # Объект для подсчёта в information и generate
        self.object = tree.Tree(self.matrix.height, self.matrix.width)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(tree.Tree(self.matrix.height, self.matrix.width), num_1, num_2)
        # После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
        self.count_object = 0
