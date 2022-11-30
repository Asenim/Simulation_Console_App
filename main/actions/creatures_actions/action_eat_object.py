from main.actions import action
from main import coordinate
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator
from main.entity_object.static_objects.grass import Grass


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
        Метод который ищет существ и
        передает их дальше вместе с координатами,
        которые надо проверить
        Травоядное - охотится на траву
        Хищник - охотится на травоядное

        """
        creatures_objects_lists = []

        for i in range(self.matrix.height+2):
            for j in range(self.matrix.width+2):
                if not self.matrix.is_empty(i, j):
                    all_object = self.matrix.get_object(i, j)
                    if isinstance(all_object, (Herbivore, Predator)):
                        creatures_objects_lists.append(all_object)

        coordinate_shift_list = [[+1, 0], [-1, 0], [0, +1], [0, -1],
                                 [+1, +1], [+1, -1], [-1, +1], [-1, -1]]

        for creature_object in creatures_objects_lists:
            for coordinate_shift in coordinate_shift_list:
                self.__search_food(creature_object, coordinate_shift[0], coordinate_shift[1])

    def __search_food(self, creature_object, crd_x, crd_y):
        """
        Метод который будет смотреть
        вокруг объекта на наличие еды
        :param creature_object: объект охоты
        :param crd_x: координата принимающая сдвиг по x
        :param crd_y: координата принимающая сдвиг по у
        """
        creature = creature_object
        coordinated = coordinate.Coordinates(creature.x, creature.y)
        # Проверяем не выходим ли за поле
        if (0 <= coordinated.x + crd_x < self.matrix.height+1) and (0 <= coordinated.y + crd_y < self.matrix.width+1):

            # Проверяем не находятся ли объекты по этим координатам
            if not self.matrix.is_empty(coordinated.x + crd_x, coordinated.y + crd_y):
                coordinated = coordinate.Coordinates(coordinated.x + crd_x, coordinated.y + crd_y)

                if isinstance(creature, Herbivore) and isinstance(
                        self.matrix.get_object(coordinated.x, coordinated.y), Grass):
                    creature.eat_grass(self.matrix, coordinated)
                elif isinstance(creature, Predator) and isinstance(
                        self.matrix.get_object(coordinated.x, coordinated.y), Herbivore):
                    creature.attack(self.matrix, coordinated)
