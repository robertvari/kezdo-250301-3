class Person:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

csaba = Person("Kiss", "Csaba")
print(csaba.full_name)