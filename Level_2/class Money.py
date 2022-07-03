class Money:
    def __init__(self, dollar, cents):
        self.total_cents = (dollar * 100) + cents

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_dollar):
        if isinstance(new_dollar, int) and new_dollar >= 0:
            cents = self.total_cents % 100
            self.total_cents = new_dollar * 100 + cents
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, new_cents):
        if isinstance(new_cents, int) and new_cents >= 0 and new_cents < 100:
            dollars = self.total_cents // 100
            self.total_cents = dollars * 100 + new_cents
        else:
            print("Error cents")

    def __str__(self):
        return f'Ваше состояние составляет {self.total_cents // 100} долларов {self.total_cents % 100} центов'
