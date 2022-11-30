from main.actions.generate import Generate
from main.entity_object.static_objects.rock import Rock


class GenerationRock(Generate):
    def __init__(self, matrix):
        super().__init__(matrix)
        # Необходимое количество камня на карте
        self.object_quantity = int(self.matrix_cells * 0.08)

    def spawn_object(self, num_1, num_2):
        # Размещаем объекты в карте
        self.matrix.add_object(Rock(num_1, num_2), num_1, num_2)
