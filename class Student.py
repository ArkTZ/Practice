class Student:
    def __init__(self, __name, __age, __branch):
        self.__name = __name
        self.__age = __age
        self.__branch = __branch

    def __display_details(self):
        print(f"""Имя: {self.__name}
Возраст: {self.__age}
Направление: {self.__branch}""")

    def access_private_method(instant):
        instant.__display_details()
