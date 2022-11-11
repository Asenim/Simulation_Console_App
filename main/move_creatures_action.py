from main import paht_finding
from main.actions import actions


class MoveCreaturesAction(actions.Actions):
    def __init__(self, matrix):
        """
        Класс для перемещения существ по карте
        :param matrix: Получает на вход карту
        """
        self.matrix = matrix

    def perform(self):
        self.__paht_creatures()

    def __paht_creatures(self):
        """
        Функция для поиска стартовой позиции
        Сначала ищется стартовая позиция объекта.
        Затем создается объект класса поиска пути.
        Потом поправляются индексы на актуальные.
        После этого создаётся объект и вызывается метод поиска.
        Если путь найден - он возвращается в переменную и затем
            передаётся в метод двигающих существ.
        Под конец сходивший объект добавляется в список существ
            которые сделали свой ход.
        """
        # Список в котором будут храниться существа сделавшие ход
        moving_creatures = []

        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creatures = self.matrix.get_object(i, j)
                    creatures.x = i
                    creatures.y = j
                    path = paht_finding.PathFinder(matrix=self.matrix, hunter=creatures)
                    path_lists = path.path_finder()
                    if path_lists is not None and creatures not in moving_creatures:
                        print(f'Готовый путь {creatures}')
                        for crd in path_lists:
                            print((crd.x, crd.y), end='; ')
                        print()
                        self.__move_creature(path_lists)
                        moving_creatures.append(creatures)

    def __move_creature(self, path_list):
        """
        Метод который позволяет перемещать существ на карте
        """
        # Список содержащий объекты координат
        path = path_list

        if len(path) > 3:
            creatures = self.matrix.get_object(path[0].x, path[0].y)
            self.matrix.add_object(creatures, path[2].x, path[2].y)
            self.matrix.delete_object(path[0].x, path[0].y)
        elif len(path) > 2:
            creatures = self.matrix.get_object(path[0].x, path[0].y)
            self.matrix.add_object(creatures, path[1].x, path[1].y)
            self.matrix.delete_object(path[0].x, path[0].y)
        print('===========')
