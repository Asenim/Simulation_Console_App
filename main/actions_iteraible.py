from main import paht_finding
from main.actions import actions


class ActionsIterable(actions.Actions):
    def __init__(self, matrix):
        self.matrix = matrix
        self.path_find = paht_finding.PathFinder(matrix=self.matrix)

    def perform(self):
        self.path_find.start_point()
