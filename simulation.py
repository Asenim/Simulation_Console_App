import os
import msvcrt
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
        self.height = height
        self.width = width

        self.__stop_loop = True
        self.__collection_stopped_button = ['f', 'F', 'А', 'а']
        self.__collection_step_rendering_button = ['s', 'S', 'Ы', 'ы']

        self.__matrix = Map(self.height, self.width)
        self.__renderer = Render(self.__matrix)

        self.__list_generation_action = [
            GenerationTree(self.__matrix),
            GenerationRock(self.__matrix),
            GenerationGrass(self.__matrix),
            GenerationHerbivore(self.__matrix),
            GenerationPredator(self.__matrix)

        ]

        for pre_start_action in self.__list_generation_action:
            pre_start_action.perform()

        os.system('cls')
        self.__renderer.print_map()
        sleep(1)
        os.system('cls')

        while self.__stop_loop:
            self.__iterates_action()

            self.__renderer.print_map()
            sleep(1)
            os.system('cls')

            if msvcrt.kbhit():
                accept_button_press = msvcrt.getwch()

                if accept_button_press in self.__collection_stopped_button:
                    self.__user_stops_loop()
                elif accept_button_press in self.__collection_step_rendering_button:
                    self.__step_rendering()

            if not self.__auto_stops_the_loop():
                self.__renderer.print_map()
                break

    def __iterates_action(self):
        """
        Метод который создает список экшнов и итерируется по ним
        """
        iterable_list_action = [
            MoveCreaturesAction(self.__matrix),
            ActionEatObject(self.__matrix),
            GenerationGrass(self.__matrix)
        ]

        for actions_during_game in iterable_list_action:
            actions_during_game.perform()

    def __user_stops_loop(self):
        """
        Метод останавливает наш игровой цикл и завершает игру
        """
        self.__renderer.print_map()
        print('Симуляция завершена пользователем')
        self.__stop_loop = False
        sleep(1)

    def __step_rendering(self):
        """
        Метод для пошаговой отрисовки игры
        """
        while True:
            self.__renderer.print_map()
            print(f'Что бы выйти из пошаговой Симуляции: \n'
                  f'ВО ВРЕМЯ пошаговой симуляции нажмите кнопку S')
            int_input_keyboard = int(input('Введите количество ходов симуляции '))
            os.system('cls')

            while int_input_keyboard != 0:
                self.__iterates_action()
                self.__renderer.print_map()
                print('Нажмите S для выхода из пошаговой Симуляции')

                int_input_keyboard = int_input_keyboard - 1
                sleep(1)
                os.system('cls')

                if not self.__auto_stops_the_loop():
                    break

            if not self.__auto_stops_the_loop():
                break

            if msvcrt.kbhit():
                user_press_button = msvcrt.getwch()

                if user_press_button in self.__collection_step_rendering_button:
                    self.__renderer.print_map()
                    print('Вы вышли из пошаговой отрисовки симуляции')
                    print('Возвращаемся в бесконечную симуляцию. . .')
                    sleep(2)
                    os.system('cls')
                    break

    def __auto_stops_the_loop(self):
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
