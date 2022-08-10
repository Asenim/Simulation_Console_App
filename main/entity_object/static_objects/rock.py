"""
Камень - является статичным объектом.
Существа будут его обходить
"""

from main.entity_object import entity


class Rock(entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = 'Rk'
