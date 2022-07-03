class Stack:
    def __init__(self, values=[]):
        self.values = values

    def push(self, item):
        self.values.insert(0, item)


    def pop(self):
        if len(self.values) == 0:
            print("Empty Stack")
        else:
            return self.values.pop(0)

    def peek(self):
        if len(self.values) == 0:
            print("Empty Stack")
            return None
        else:
            return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)