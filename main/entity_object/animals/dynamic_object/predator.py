from main.entity_object.animals import creatures


class Predator(creatures.Creatures):
    def __init__(self, speed, hit_point, max_hit_point, gender,
                 successful_hunting, restore_hp_successful_hunt, range_attack, attack_power, x, y):
        """
        Класс Хищника
        :param speed: Количество клеток которое существо может пройти за один ход
        :param hit_point: Количество здоровья существа
        :param max_hit_point: Максимальное количество здоровья существа
        :param gender: Пол существа
        :param successful_hunting: счетчик успешной охоты (Сколько надо убить что бы размножиться)
        :param restore_hp_successful_hunt: Количество восстанавливаемого ХП при успешной охоте
        :param range_attack: расстояние атаки
        :param x: Координата расположения объекта
        :param y: Координата расположения объекта
        :parameter self.sprite: То как будет выглядеть объект на карте
        """
        super().__init__(speed, hit_point, max_hit_point, gender, x, y)
        self.successful_hunting = successful_hunting
        self.restore_hp_successful_hunt = restore_hp_successful_hunt
        self.range_attack = range_attack
        self.attack_power = attack_power
        self.sprite = 'Prd'

    def make_move(self):
        pass

    def attack(self, maps, coordinate_object):
        """
        Метод позволяет атаковать травоядное
        и снижать количество его здоровья/
        А так же удалять его с поля если здоровье
        травоядного опустилось до 0 и лечить свое пострадавшее здоровье.
        :param maps: карта
        :param coordinate_object: координаты объекта охоты
        """
        matrix = maps
        coordinate = coordinate_object
        if not matrix.is_empty(coordinate.x, coordinate.y):
            creature = matrix.get_object(coordinate.x, coordinate.y)
            if creature.sprite == 'Hrb':
                if creature.hit_point > 0:
                    creature.hit_point = creature.hit_point - self.attack_power
                elif creature.hit_point <= 0:
                    matrix.delete_object(coordinate.x, creature.y)
                    self.hit_point = self.hit_point + self.restore_hp_successful_hunt

    def reproduction(self):
        pass
