class Building:
    def __init__(self, floor):
        self.floor = floor
        self.company = list()
        self.company.extend([None] * floor)

    def __setitem__(self, key, value):
        if 0 <= key < len(self.company):
            self.company[key] = value
        elif key > len(self.company):
            diff = key - len(self.company)
            self.company.extend([None] * diff)
        else:
            raise IndexError('Setitem')

    def __getitem__(self, item):
        if 0 <= item < len(self.company):
            return self.company[item]
        else:
            raise IndexError('Getitem')

    def __delitem__(self, key):
        if 0 <= key < len(self.company):
            self.company[key] = None
        else:
            raise IndexError('DelItem')
