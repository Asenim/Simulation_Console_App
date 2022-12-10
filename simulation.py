import os
from main.maps_and_render import *
from main.actions.generation_actions import *
from time import sleep
from main.simulation_loop import SimulationLoop


class Simulation:
    def __init__(self, height, width):
        self.height = height
        self.width = width

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

        simulation_loop = SimulationLoop(self.__matrix, self.__renderer)
        simulation_loop.simulation_loop()


if __name__ == '__main__':
    sim = Simulation(5, 15)
