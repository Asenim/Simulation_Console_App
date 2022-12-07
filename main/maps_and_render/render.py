from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.entity_object.animals.dynamic_object.predator import Predator


class Render:
    def __init__(self, matrix):
        """
        Отрисовка карты и статуса существ
        :param matrix: Принимаем на вход объект карты
        """
        self.__matrix = matrix

    def print_map(self):
        """
        Отрисовка нашей карты в консоли
        Сдвиг на +2 сделан для корректного добавления границ карты
        При измененнии границ отрисовки в этом методе так же надо
        будет изменить границы в следующих классах: (Класс: Методы)
            simulation: stops_the_loop
            render: displays_statistics
            generate: random_coordinates
            generation_grass: count_current
            path_finding: __filling_queue
            move_creatures_action: __path_creatures
            action_eat_object: __search_hunter, __search_food
        """
        self.__displays_statistics()

        for x in range(self.__matrix.height + 2):
            for y in range(self.__matrix.width + 2):
                if self.__matrix.is_empty(x, y):
                    if x == 0 or x == self.__matrix.height+1:
                        item = '==='
                    elif y == 0 or y == self.__matrix.width+1:
                        item = '||'
                    else:
                        item = ' '
                else:
                    item = self.__matrix.get_object(x, y).sprite

                print(str(item).ljust(3), end=' ')
            print()
        self.__displays_user_buttons()

    def __displays_statistics(self):
        """
        Метод отрисовки описания названия объектов и статуса существ
        """
        self.__displays_information()

        list_of_creatures = []

        for x in range(self.__matrix.height + 2):
            for y in range(self.__matrix.width + 2):
                if isinstance(self.__matrix.get_object(x, y), (Herbivore, Predator)):
                    list_of_creatures.append(self.__matrix.get_object(x, y))

        for creature_iteration in list_of_creatures:
            if isinstance(creature_iteration, Predator):
                print(f'Хищник - {creature_iteration.sprite}; '
                      f'Скорость = {creature_iteration.speed}; '
                      f'Здоровье - {creature_iteration.hit_point}; '
                      f'Атака - {creature_iteration.attack_power}')
            else:
                print(f'Травоядное - {creature_iteration.sprite}; '
                      f'Скорость = {creature_iteration.speed}; '
                      f'Здоровье - {creature_iteration.hit_point}; '
                      f'Регенерация - {creature_iteration.restore_hp_eat_grass}')

    @staticmethod
    def __displays_information():
        """
        Метод для отрисовки глоссария объектов на карте
        """
        sprite_dictionary = {
            'Prd': 'Хищник',
            'Hrb': 'Травоядное',
            'Gs': 'Трава',
            'Tr': 'Дерево',
            'Rk': 'Камень'
        }

        for sprite, description_sprite in sprite_dictionary.items():
            print(f'{sprite} - {description_sprite}')
        print()

    @staticmethod
    def __displays_user_buttons():
        """
        Метод выводит на экран информацию,
        какие кнопки ему доступны
        для управления программой
        """
        dict_display_user_control = {
            'S': 'Кнопка для пошаговой отрисовки симуляции',
            'F': 'Кнопка для остановки симуляции',
            'Y': 'Кнопка для Согласия',
            'N': 'Кнопка для Отказа'
        }

        for button, description_button in dict_display_user_control.items():
            print(f'{button} - {description_button}')
        print()
