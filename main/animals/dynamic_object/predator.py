"""
Класс хищников, все хищники будут создаваться из этого класса
Дополнительные поля:
    successful_hunting - счетчик успешной охоты (Сколько надо убить что бы размножиться)
    restore_hp_successful_hunt - Количество восстанавливаемого ХП при успешной охоте
    range_attack - расстояние атаки
"""

from main.animals import creatures


class Preadator(creatures.Creatures):
    def __init__(self, speed, hit_point, max_hit_point, gender,
                 successful_hunting, restore_hp_successful_hunt, range_attack):
        super().__init__(speed, hit_point, max_hit_point, gender)
        self.successful_hunting = successful_hunting
        self.restore_hp_successful_hunt = restore_hp_successful_hunt
        self.range_attack = range_attack
        self.sprite = 'Prd'

    def make_move(self):
        pass

    def attack(self):
        pass

    def reproduction(self):
        pass
