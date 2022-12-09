from main.entitys import entity


class Tree(entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = 'Te'
