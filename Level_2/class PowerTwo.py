class PowerTwo:
    def __init__(self, degree):
        self.max_degree = degree

    def __iter__(self):
        self.degree = -1
        return self

    def __next__(self):
        if self.degree < self.max_degree:
            self.degree += 1
            return 2 ** self.degree
        raise StopIteration
