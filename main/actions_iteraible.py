from main import paht_finding


class ActionsIterable:
    def __init__(self, matrix):
        self.matrix = matrix
        self.path_find = paht_finding.PathFinder(matrix=self.matrix)

    def start(self):
        self.path_find.start_point()
