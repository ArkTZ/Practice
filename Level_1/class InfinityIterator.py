class InfinityIterator:
    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        num = self.num
        self.num += 10
        return num
