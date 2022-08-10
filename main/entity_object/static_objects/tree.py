"""
Дерево - является статическим объектом.
Существа будут его обходить
"""

from main.entity_object import entity


class Tree(entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = 'Te'
