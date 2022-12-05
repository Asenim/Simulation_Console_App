import os
from main.entity_object.animals.dynamic_object.herbivore import Herbivore
from main.maps_and_render.map_class import Map
from main.maps_and_render.render import Render
from main.actions.generation_actions.generation_tree import GenerationTree
from main.actions.generation_actions.generation_rock import GenerationRock
from main.actions.generation_actions.generation_grass import GenerationGrass
from main.actions.generation_actions.generation_herbivore import GenerationHerbivore
from main.actions.generation_actions.generation_predator import GenerationPredator
from main.actions.creatures_actions.move_creatures_action import MoveCreaturesAction
from main.actions.creatures_actions.action_eat_object import ActionEatObject
from time import sleep


class Simulation:
    def __init__(self, height, width):
        # Принимаем значения
        self.height = height
        self.width = width

        # Создаём матрицу и рендер
        self.__matrix = Map(self.height, self.width)
        self.__renderer = Render(self.__matrix)

        # Список с генерацией объектов
        self.__list_generation_action = [
            GenerationTree(self.__matrix),
            GenerationRock(self.__matrix),
            GenerationGrass(self.__matrix),
            GenerationHerbivore(self.__matrix),
            GenerationPredator(self.__matrix)

        ]

        # Вызываем предварительную генерацию перед началом игры
        for pre_start_action in self.__list_generation_action:
            pre_start_action.perform()

        os.system('cls')
        # Отрисовываем заполненную матрицу рендер
        self.__renderer.displays_statistics()
        self.__renderer.print_map()
        sleep(1)
        os.system('cls')

        # Основной цикл симуляции
        while True:
            # Список экшнов итерируемый каждый ход
            iterable_list_action = [
                MoveCreaturesAction(self.__matrix),
                ActionEatObject(self.__matrix),
                GenerationGrass(self.__matrix)
            ]

            # Вызов всех итерируемых экшнов каждый ход
            for actions_during_game in iterable_list_action:
                actions_during_game.perform()

            # Отрисовка статистики и состояния карты
            self.__renderer.displays_statistics()
            self.__renderer.print_map()
            sleep(1)
            os.system('cls')

            # Условие остановки цикла с предварительной отрисовкой
            # состояния симуляции
            if not self.__stops_the_loop():
                self.__renderer.displays_statistics()
                self.__renderer.print_map()
                break

    def __stops_the_loop(self):
        """
        Счетчик для условия остановки нашего цикла While.
        На данный момент условие остановки - это отсутствие
            травоядных на карте.
        :return: Возвращает True или False
        """
        counter_herbivore = 0

        for i in range(self.__matrix.height + 2):
            for j in range(self.__matrix.width + 2):
                all_object = self.__matrix.get_object(i, j)
                if isinstance(all_object, Herbivore):
                    counter_herbivore = counter_herbivore + 1

        if counter_herbivore > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    sim = Simulation(10, 10)
