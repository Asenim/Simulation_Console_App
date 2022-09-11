from main.actions import generate
from main.entity_object.static_objects import grass


class GenerationGrass(generate.Generate):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Необходимое количество травы на карте в зависимости от размера матрицы
        self.object_quantity = int(self.matrix_cells * 0.2)
        # Счётчик травы
        self.count_object = 0
        # Объект для подсчета в information и generate
        self.object = grass.Grass(self.matrix.height, self.matrix.width)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(grass.Grass(self.matrix.height, self.matrix.width), num_1, num_2)
        # После расположения объектов на матрице - Обнуляем счётчик для корректной работы generate
        self.count_object = 0
