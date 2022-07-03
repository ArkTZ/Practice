class Vector:
    def __init__(self, *args):
        self.values = []
        for i in args:
            if isinstance(i, int):
                self.values.append(i)
            self.values.sort()

    def __str__(self):
        if len(self.values) > 0:
            a = sorted(self.values)
            return f'Вектор{tuple(a)}'
        else:
            return "Пустой вектор"

    def __add__(self, other):
        if isinstance(other, int):
            vector = []
            for i in range(len(self.values)):
                vector.append(self.values[i] + other)
            return Vector(*vector)

        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                vector = []
                for i in range(len(other.values)):
                    vector.append(self.values[i] + other.values[i])
                return Vector(*vector)
            else:
                print("Сложение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя сложить с {other}")

    def __mul__(self, other):
        if isinstance(other, int):
            vector = []
            for i in range(len(self.values)):
                vector.append(self.values[i] * other)
            return Vector(*vector)

        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                vector = []
                for i in range(len(other.values)):
                    vector.append(self.values[i] * other.values[i])
                return Vector(*vector)
            else:
                print("Умножение векторов разной длины недопустимо")
        else:
            print(f"Вектор нельзя умножать с {other}")
