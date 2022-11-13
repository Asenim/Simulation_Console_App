from main.actions import actions
from main import coordinate


class ActionEatObject(actions.Actions):
    def __init__(self, matrix):
        """
        Класс для поедания и атаки искомых объектов
        :param matrix:
        """
        self.matrix = matrix

    def perform(self):
        self.__search_hunter()

    def __search_hunter(self):
        """
        Метод который ищет охотников
        Травоядное - охотится на траву
        Хищник - охотится на травоядное
        :return:
        """
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creature = self.matrix.get_object(i, j)
                    if creature.sprite == 'Hrb':
                        self.__search_food(creature, 1, 0)
                        self.__search_food(creature, 0, 1)
                        self.__search_food(creature, -1, 0)
                        self.__search_food(creature, 0, -1)

    def __search_food(self, creature_object, crd_1, crd_2):
        """
        Метод который будет смотреть
        вокруг объекта на наличие еды
        """
        creature = creature_object
        coordinated = coordinate.Coordinates(creature.x, creature.y)
        # Проверяем не выходим ли за поле
        if (0 <= coordinated.x + crd_1 < self.matrix.height) and (0 < coordinated.y + crd_2 <= self.matrix.width):

            # Проверяем не находятся ли объекты по этим координатам
            if not self.matrix.is_empty(coordinated.x + crd_1, coordinated.y + crd_2):
                coordinated = coordinate.Coordinates(coordinated.x + crd_1, coordinated.y + crd_2)
                creature.eat_grass(self.matrix, coordinated)
