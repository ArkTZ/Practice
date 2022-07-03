class City:
    def __init__(self, name):
        self.name = name.title()

    def __str__(self):
        return self.name

    def __bool__(self):
        a = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(a)):
            if self.name[-1] in a:
                return False
            else:
                return True
