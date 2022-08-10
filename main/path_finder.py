from collections import deque


class PathFinder:
    """
    Неготовый класс
    """
    def __init__(self, matrix):
        self.matrix = matrix

    def make_move(self):
        queue = deque()
        sets = set()
        for x in range(self.matrix.height):
            for y in range(self.matrix.width):
                if self.matrix.get_object(x, y).sprite:
                    pass
