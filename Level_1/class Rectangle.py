class Rectangle:
    def __init__(self, height, weight):
        self.__height = height
        self.__weight = weight
        self.__area = None

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value
        self.__area = None

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value
        self.__area = None

    @property
    def area(self):
        if self.__area == None:
            self.__area = self.__height * self.weight
        return self.__area
