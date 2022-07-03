class Date:
    def __init__(self, day, mounth, year):
        self.__day = str(day)
        self.__mounth = str(mounth)
        self.__year = str(year)

    @property
    def date(self):
        return f'{self.__day.rjust(2, "0")}/{self.__mounth.rjust(2, "0")}/{self.__year.rjust(4, "0")}'

    @property
    def usa_date(self):
        return f'{self.__mounth.rjust(2, "0")}-{self.__day.rjust(2, "0")}-{self.__year.rjust(4, "0")}'
