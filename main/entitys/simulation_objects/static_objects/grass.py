from main.entitys import entity


class Grass(entity.Entity):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.sprite = 'Gs'
