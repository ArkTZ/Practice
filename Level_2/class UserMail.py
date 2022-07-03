class UserMail:
    def __init__(self, login, __email):
        self.login = login
        self.__email = __email

    def get_email(self):
        return self.__email

    def set_email(self, value):
        if '@' in value:
            if value.find('@') < value.find('.') and value.count("@") == 1:
                self.__email = value
            else:
                print(f"ErrorMail:{value}")
        else:
            print(f"ErrorMail:{value}")

    email = property(
        fset=set_email,
        fget=get_email,
        doc="The name property.")
