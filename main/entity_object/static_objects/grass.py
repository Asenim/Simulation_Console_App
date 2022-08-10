"""
Трава - служит кормом для травоядных.
Является статичным объектом.
Ничего не принимает на вход, спрайт = Gr.
Заполняет нашу матрицу своими объектами
"""

from main.entity_object import entity


class Grass(entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = 'Gs'
