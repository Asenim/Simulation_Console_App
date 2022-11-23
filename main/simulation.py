from maps_and_render import map_class
from maps_and_render import render
from actions.generation_actions import generation_tree
from actions.generation_actions import generation_rock
from actions.generation_actions import generation_grass
from actions.generation_actions import generation_herbivore
from actions.generation_actions import generation_predator
from actions.creatures_actions import move_creatures_action
from actions.creatures_actions import action_eat_object
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

        # Создаём объекты генерации
        self.gen_tree = generation_tree.GenerationTree(self.matrix)
        self.gen_rock = generation_rock.GenerationRock(self.matrix)
        self.gen_grass = generation_grass.GenerationGrass(self.matrix)
        self.gen_herbivore = generation_herbivore.GenerationHerbivore(self.matrix)
        self.gen_predator = generation_predator.GenerationPredator(self.matrix)
        # Помещаем их в список
        self.list_actions = [self.gen_grass, self.gen_tree, self.gen_rock, self.gen_herbivore, self.gen_predator]

        # Вызываем предварительную генерацию перед началом игры
        for i in self.list_actions:
            i.perform()

        # Отрисовываем заполненную матрицу рендер
        print('---------------------')
        self.renderer.print_map()
        print('----------------------')

        # Создаём объект класса actions и объект класса поиска пути
        self.move_creatures = move_creatures_action.MoveCreaturesAction(self.matrix)
        self.eat_action = action_eat_object.ActionEatObject(self.matrix)

        counter = 0
        # Методы которые будут вызываться в процессе симуляции
        while counter != 20:
            self.iterable_list_actions = [self.eat_action, self.move_creatures, self.eat_action, self.gen_grass]

            for j in self.iterable_list_actions:
                j.perform()

            print("=====================")
            self.renderer.print_map()
            print("=====================")
            sleep(1)
            counter = counter + 1

    def information(self):
        """
        Временный метод показывающий
        количество всех объектов на матрице
        """
        # Словарь с объектами матрицы
        __dict_objects_info = {}

        # Алгоритм заполнение словаря
        for action in self.list_actions:
            if action.object.sprite not in __dict_objects_info:
                __dict_objects_info[action.object.sprite] = 0

        print()
        # Подсчёт объектов на карте для метода information
        for x in range(self.matrix.height):
            for y in range(self.matrix.width):
                for key in __dict_objects_info:
                    if self.matrix.is_empty(x, y):
                        pass
                    elif key in self.matrix.get_object(x, y).sprite:
                        __dict_objects_info[key] = __dict_objects_info[key] + 1

        # Вывод количества объектов на матрице
        for key in __dict_objects_info:
            print(f'{key} = {__dict_objects_info[key]}')


if __name__ == '__main__':
    sim = Simulation(5, 5)
    sim.information()
