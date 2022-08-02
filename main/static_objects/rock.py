"""
Камень - является статичным объектом.
Существа будут его обходить
"""

from main import entity


class Rock(entity.Entity):
    def __init__(self):
        self.sprite = 'Rk'
