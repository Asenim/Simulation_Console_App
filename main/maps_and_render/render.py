from main.entitys.simulation_objects.dynamic_object import *


class Render:
    def __init__(self, matrix, move_counter=None):
        """
        Отрисовка карты и статуса существ
        :param matrix: Принимаем на вход объект карты
        :param move_counter: Принимаем на вход счетчик
        """
        self.__matrix = matrix
        self.__move_counter = move_counter

    def print_map(self, move_count=None):
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
        self.__draws_counter_of_moves(move_count)

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
    def __draws_counter_of_moves(move_count):
        """
        Вывод счетчика ходов.
        """
        if move_count is not None:
            print(f'{10*"-"} Ход номер - {move_count} {10*"-"}')
        else:
            print(f'{10*"-"} Ход номер - 0 {10*"-"}')

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
            'A': 'Кнопка для паузы',
            'F': 'Кнопка для остановки симуляции'
        }

        for button, description_button in dict_display_user_control.items():
            print(f'{button} - {description_button}')
        print()
