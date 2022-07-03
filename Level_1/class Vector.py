class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)

    def __str__(self):
        if len(self.values) > 0:
            a = sorted(self.values)
            return f'Вектор{tuple(a)}'
        else:
            return "Пустой вектор"
