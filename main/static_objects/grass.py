"""
Трава - служит кормом для травоядных.
Является статичным объектом.
Ничего не принимает на вход, спрайт = Gr.
Заполняет нашу матрицу своими объектами
"""

from main import entity


class Grass(entity.Entity):
    def __init__(self):
        self.sprite = 'Gs'
