class Hotel:
    __name = None
    __visitors_per_year = None
    __rooms = None

    public_numbers = 0
    public_string = "sentence"

    def __init__(self, name=None, visitors_per_year=0, rooms=0, public_numbers=0, public_string=""):
        self.__name = name
        self.__visitors_per_year = visitors_per_year
        self.__rooms = rooms
        self.public_numbers = public_numbers
        self.public_string = public_string

    @property
    def name(self):
        return self.__name

    @property
    def visitors_per_year(self):
        return self.__visitors_per_year

    @property
    def rooms(self):
        return self.__rooms

    @name.setter
    def name(self, name):
        self.__name = name

    @visitors_per_year.setter
    def visitors_per_year(self, visitors_per_year):
        self.__visitors_per_year = visitors_per_year

    @rooms.setter
    def rooms(self, rooms):
        self.__rooms = rooms

    def __str__(self):
        return (
            f"Готель: {self.__name}, "
            f"Відвідувачі на рік: {self.__visitors_per_year}, "
            f"Кількість номерів: {self.__rooms}"
        )

    def __repr__(self):
        return (
            f"Hotel(name={self.__name}, "
            f"visitors_per_year={self.__visitors_per_year}, "
            f"rooms={self.__rooms})"
        )

    def __del__(self):
        print(f"Готель '{self.__name}' видалений")


def main():
    hotel1 = Hotel("eazy hotel", 3000, 70)
    hotel2 = Hotel("mountain hotel", 2500, 50)
    hotel3 = Hotel("ocean hotel", 3200, 65)

    print(hotel1)
    print(hotel2)
    print(hotel3)

    print(repr(hotel1))
    print(repr(hotel2))
    print(repr(hotel3))

    print("Public numbers:", Hotel.public_numbers)
    print("Public string:", Hotel.public_string)


main()
