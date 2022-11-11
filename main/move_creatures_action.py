from main import paht_finding
from main.actions import actions
from main.maps_and_render import render


class MoveCreaturesAction(actions.Actions):
    def __init__(self, matrix):
        """
        Класс для перемещения существ по карте
        :param matrix: Получает на вход карту
        """
        self.matrix = matrix

    def perform(self):
        self.move_creature()

    def paht_creatures(self):
        """
        Функция для поиска стартовой позиции
        Сначала ищется стартовая позиция объекта.
        Затем создается объект класса поиска пути.
        После этого вызывается метод поиска
        Если путь найден - он печатается и возвращается
        :return path_lists: готовый путь
        """
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creatures = self.matrix.get_object(i, j)
                    path = paht_finding.PathFinder(matrix=self.matrix,
                                                   hunter=creatures)
                    path_lists = path.path_finder()
                    if path_lists is not None:
                        print('Готовый путь')
                        for crd in path_lists:
                            print((crd.x, crd.y), end='; ')
                        print()
                        return path_lists

    def move_creature(self):
        """
        Метод который позволяет перемещать существ на карте
        """
        # Временная переменная
        renderer = render.Render(self.matrix)

        # Список содержащий объекты координат
        path_object = self.paht_creatures()

        for i in range(len(path_object)-2):
            creatures = self.matrix.get_object(path_object[i].x, path_object[i].y)
            self.matrix.add_object(creatures, path_object[i+1].x, path_object[i+1].y)
            self.matrix.delete_object(path_object[i].x, path_object[i].y)
            print('===========')
            renderer.print_map()
            print('===========')
