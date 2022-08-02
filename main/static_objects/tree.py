"""
Дерево - является статическим объектом.
Существа будут его обходить
"""

from main import entity


class Tree(entity.Entity):
    def __init__(self):
        self.sprite = 'Te'
