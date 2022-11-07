from main import paht_finding
from main.actions import actions


class ActionsIterable(actions.Actions):
    def __init__(self, matrix):
        self.matrix = matrix

    def perform(self):
        self.paht_creatures()

    def paht_creatures(self):
        """
        Функция для поиска стартовой позиции
        """
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creatures = self.matrix.get_object(i, j)
                    paht_finding.PathFinder(matrix=self.matrix,
                                            hunter=creatures)
