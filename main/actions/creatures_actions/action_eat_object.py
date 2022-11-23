from main.actions import action
from main import coordinate


class ActionEatObject(action.Actions):
    def __init__(self, matrix):
        """
        Класс для поедания и атаки искомых объектов
        :param matrix: - Принимаем на вход карту
        """
        self.matrix = matrix

    def perform(self):
        self.__search_hunter()

    def __search_hunter(self):
        """
        Метод который ищет охотников и
        передает их дальше вместе с координатами,
        которые надо проверить
        Травоядное - охотится на траву
        Хищник - охотится на травоядное

        """
        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                if not self.matrix.is_empty(i, j):
                    creature = self.matrix.get_object(i, j)
                    self.__search_food(creature, 1, 0)
                    self.__search_food(creature, 0, 1)
                    self.__search_food(creature, -1, 0)
                    self.__search_food(creature, 0, -1)

    def __search_food(self, hunting_object, crd_x, crd_y):
        """
        Метод который будет смотреть
        вокруг объекта на наличие еды
        :param hunting_object: объект охоты
        :param crd_x: координата принимающая сдвиг по x
        :param crd_y: координата принимающая сдвиг по у
        """
        creature = hunting_object
        coordinated = coordinate.Coordinates(creature.x, creature.y)
        # Проверяем не выходим ли за поле
        if (0 <= coordinated.x + crd_x <= self.matrix.height) and (0 <= coordinated.y + crd_y <= self.matrix.width):

            # Проверяем не находятся ли объекты по этим координатам
            if not self.matrix.is_empty(coordinated.x + crd_x, coordinated.y + crd_y):
                coordinated = coordinate.Coordinates(coordinated.x + crd_x, coordinated.y + crd_y)
                if creature.sprite == 'Hrb':
                    creature.eat_grass(self.matrix, coordinated)
                elif creature.sprite == 'Prd':
                    creature.attack(self.matrix, coordinated)
