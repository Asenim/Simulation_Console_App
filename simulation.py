import os
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
        os.system('cls')
        self.renderer.displays_statistics()
        self.renderer.print_map()
        sleep(1)
        os.system('cls')

        # Методы которые будут вызываться в процессе симуляции
        while True:
            iterable_list_action = [
                move_creatures_action.MoveCreaturesAction(self.matrix),
                action_eat_object.ActionEatObject(self.matrix),
                generation_grass.GenerationGrass(self.matrix)
            ]

            for actions_during_game in iterable_list_action:
                actions_during_game.perform()

            self.renderer.displays_statistics()
            self.renderer.print_map()
            sleep(1)
            os.system('cls')

            # В Условии должно быть not
            if not self.stops_the_loop():
                self.renderer.displays_statistics()
                self.renderer.print_map()
                break

    def stops_the_loop(self):
        """
        Счетчик для условия остановки нашего цикла While.
        На данный момент условие остановки - это отсутствие
            травоядных на карте.
        :return: Возвращает True или False
        """
        counter_herbivore = 0

        for i in range(self.matrix.height+2):
            for j in range(self.matrix.width+2):
                all_object = self.matrix.get_object(i, j)
                if isinstance(all_object, Herbivore):
                    counter_herbivore = counter_herbivore + 1

        if counter_herbivore > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    sim = Simulation(5, 5)
