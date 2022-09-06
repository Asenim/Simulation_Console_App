from main import paht_finding
from main.actions import actions


class ActionsIterable(actions.Actions):
    def __init__(self, matrix):
        self.matrix = matrix
        self.path_find = paht_finding.PathFinder(matrix=self.matrix)

    def perform(self):
        self.path_find.start_point()
        # for i in range(self.matrix.height):
        #     for j in range(self.matrix.width):
        #         if not self.matrix.is_empty(i, j):
        #             creatures = self.matrix.get_object(i, j)
        #             if creatures.sprite == 'Hrb':
        #                 self.path_find.hunter = creatures
        #                 self.path_find.victim = 'Gs'
        #                 self.path_find.queues.appendleft(((i, j), (i, j)))
        #                 self.path_find.start_point_save = (i, j)
        #                 # Далее будет вызываться метод path_finder
        #                 # Который очистит очередь для дальнейшего использования
        #                 self.path_find.path_finder()
        #                 self.path_find.overcome_path()
        #                 self.path_find.moving_object()
        #                 # После использования всех коллекций очищаем их для корректной работы следующего объекта
        #                 self.path_find.queues.clear()
        #                 self.path_find.sets.clear()
        #
