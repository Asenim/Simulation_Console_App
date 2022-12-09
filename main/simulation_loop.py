import os
import msvcrt
from time import sleep
from main.actions.generation_actions import *
from main.actions.creatures_actions import *
from main.entitys.simulation_objects.dynamic_object.herbivore import Herbivore


class SimulationLoop:
    def __init__(self, matrix, render):
        self.__matrix = matrix
        self.__renderer = render

        self.__stop_loop = True
        self.__collection_stopped_button = ['f', 'F', 'А', 'а']
        self.__collection_step_rendering_button = ['s', 'S', 'Ы', 'ы']
        self.__collection_pause_button = ['a', 'A', 'Ф', 'ф']

    def simulation_loop(self):
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
                elif accept_button_press in self.__collection_pause_button:
                    self.__pause_rendering()

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

    def __pause_rendering(self):
        """
        Метод для приостановки симуляции
        """
        while True:
            self.__renderer.print_map()

            print(f'Симуляция приостановлена. \n'
                  f'Для выхода из состояния паузы - нажмите клавишу A. \n'
                  f'Для запуска пошаговой симуляции - нажмите S. \n'
                  f'Для остановки симуляции - нажмите F.')
            sleep(2)
            os.system('cls')

            if msvcrt.kbhit():
                user_press_button = msvcrt.getwch()

                if user_press_button in self.__collection_pause_button:
                    self.__renderer.print_map()
                    print('Возобновляем бесконечную симуляцию...')
                    sleep(3)
                    os.system('cls')
                    break

                elif user_press_button in self.__collection_step_rendering_button:
                    self.__renderer.print_map()
                    print('Начинаем пошаговую симуляцию...')
                    sleep(3)
                    os.system('cls')
                    return self.__step_rendering()

                elif user_press_button in self.__collection_stopped_button:
                    self.__renderer.print_map()
                    print('Симуляция завершается...')
                    self.__stop_loop = False
                    sleep(3)
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
