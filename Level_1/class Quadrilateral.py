class Quadrilateral:
    def __init__(self, width, height=None):
        if height != None:
            self.width = width
            self.height = height
        else:
            self.width = width
            self.height = width

    def __str__(self):
        if self.width == self.height:
            return f'Куб размером {self.width}х{self.width}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height
