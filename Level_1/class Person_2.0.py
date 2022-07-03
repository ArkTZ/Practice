class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def display_person_info(self):
        print(f'Person: {self.name}, {self.age}')


class Company:
    def __init__(self, company_name, location ):
        self.company_name, self.location  = company_name, location

    def display_company_info(self):
        print(f'Company: {self.company_name}, {self.location}')


class Employee:
    def __init__(self, name, age, company_name, location):
        self.name, self.age = name, age
        self.company_name, self.location = company_name, location
        self.personal_data = Person(self.name, self.age)
        self.work = Company(self.company_name, self.location)
