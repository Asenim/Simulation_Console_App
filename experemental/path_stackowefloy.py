from collections import deque
from main import coordinate

"""
Описание алгоритма.
1. Создаём пустую очередь [] и пустое множество {}
2. Добавляем в эту очередь список из стартовой координаты [[(0, 0)]]
3. Достаём из очереди первый элемент, который содержит список с коордитатой
    path_list = queue.popleft() -> [(0,0)], остаётся пустая очередь []
    3.1 Достаём последний элемент списка coordinates = path_list[-1] -> (0, 0)
    3.2 Проверяем соседние элементы coordinates [+1,0; -1,0; 0,+1; 0,-1]
        Что бы не выходили за границы поля: if coordinates < размеры поля
        и формируем из них списки путей добавляя новые соседние координаты ->
        if 0,+1 <= грананицам поля and 0,+1 not in set():
            new_path_list = path_list.copy() 
            new_path_list.append((0,1)) -> [(0,0); (0,1)] 
            queue.append(new_path_list) -> [[(0,0); (0,1)]]
        if +1,0 <= грананицам поля and 0,+1 not in set():
            new_path_list = path_list.copy()
            new_path_list.append((1,0)) -> [(0,0); (1,0)]
            queue.append(new_path_list) -> [[(0,0); (0,1)], [(0,0); (1, 0)]] 
    3.3 Добавляем исследованную координату в множество set()
4. Повторяем то же самое пока не будет найден путь до конечной точки или не закончится очередь
        
"""

# Есть карта с координатами
matrix = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)]
]
# Создаём пустую очередь
queue = deque()
sets = set()
# Создаём переменную хранящую нашу стартовую позицию
start_point = matrix[0][0]
# Добавляем нашу стартовую позицию в нашу очередь
queue.append([start_point])

while len(queue) >= 1:
    path_list = queue.popleft()

a = coordinate.Coordinates(5, 5)
b = coordinate.Coordinates(3, 4)
q = deque()
q.append([a])
lst_path = q.popleft()
collect = lst_path[-1]
print(collect)
