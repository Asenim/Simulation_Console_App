from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.maps_and_render import map_class
from main.maps_and_render import render
from main.actions.generation_actions import generation_tree
from main.actions.generation_actions import generation_rock
from main.actions.generation_actions import generation_grass
from main.actions.generation_actions import generation_herbivore
from main.actions.generation_actions import generation_predator
from main.actions.creatures_actions import move_creatures_action
from main.actions.creatures_actions import action_eat_object
from time import sleep


class Simulation:
    def __init__(self, height, width):
        # Принимаем значения
        self.height = height
        self.width = width
        # Поле которое позволит нам конролировать цикл программы
        self.run = None

        # Создаём матрицу и рендер
        self.matrix = map_class.Map(self.height, self.width)
        self.renderer = render.Render(self.matrix)
        # Отрисовываем пустую матрицу
        self.renderer.print_map()

        self.list_generation_action = [
            generation_tree.GenerationTree(self.matrix),
            generation_rock.GenerationRock(self.matrix),
            generation_grass.GenerationGrass(self.matrix),
            generation_herbivore.GenerationHerbivore(self.matrix),
            generation_predator.GenerationPredator(self.matrix)

        ]

        # Вызываем предварительную генерацию перед началом игры
        for pre_start_action in self.list_generation_action:
            pre_start_action.perform()

        # Отрисовываем заполненную матрицу рендер
        print('---------------------')
        self.renderer.print_map()
        print('----------------------')

        # Создаём объект класса actions и объект класса поиска пути
        # self.move_creatures = move_creatures_action.MoveCreaturesAction(self.matrix)
        # self.eat_action = action_eat_object.ActionEatObject(self.matrix)

        # Методы которые будут вызываться в процессе симуляции
        while True:
            self.iterable_list_action = [
                move_creatures_action.MoveCreaturesAction(self.matrix),
                action_eat_object.ActionEatObject(self.matrix),
                generation_grass.GenerationGrass(self.matrix)
            ]

            for actions_during_game in self.iterable_list_action:
                actions_during_game.perform()

            print("=====================")
            self.renderer.print_map()
            print("=====================")
            sleep(1)

            # В Условии должно быть not
            if not self.stops_the_loop():
                break

    def stops_the_loop(self):
        """
        Счетчик для условия остановки нашего цикла While.
        На данный момент условие остановки - это отсутствие
            травоядных на карте.
        :return: Возвращает True или False
        """
        counter_herbivore = 0

        for i in range(self.matrix.height):
            for j in range(self.matrix.width):
                all_object = self.matrix.get_object(i, j)
                if isinstance(all_object, Herbivore):
                    counter_herbivore = counter_herbivore + 1

        if counter_herbivore > 0:
            return True
        else:
            return False

    # def information(self):
    #     """
    #     Временный метод показывающий
    #     количество всех объектов на матрице
    #     """
    #     # Словарь с объектами матрицы
    #     __dict_objects_info = {}
    #
    #     # Алгоритм заполнение словаря
    #     for action in self.list_generation_action:
    #         if action.object.sprite not in __dict_objects_info:
    #             __dict_objects_info[action.object.sprite] = 0
    #
    #     print()
    #     # Подсчёт объектов на карте для метода information
    #     for x in range(self.matrix.height):
    #         for y in range(self.matrix.width):
    #             for key in __dict_objects_info:
    #                 if self.matrix.is_empty(x, y):
    #                     pass
    #                 elif key in self.matrix.get_object(x, y).sprite:
    #                     __dict_objects_info[key] = __dict_objects_info[key] + 1
    #
    #     # Вывод количества объектов на матрице
    #     for key in __dict_objects_info:
    #         print(f'{key} = {__dict_objects_info[key]}')


if __name__ == '__main__':
    sim = Simulation(5, 5)
    # sim.information()
