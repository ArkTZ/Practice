class Robot():

    def set_name(self, value):
        self.name = value

    def say_hello(instanse):
        if hasattr(instanse, 'name'):
            print(f'Hello, human! My name is {instanse.name}')
        else:
            print('У робота нет имени')


    def say_bye(self):
        print('See u later alligator')