class Dice:
    # class attribute
    type = "Game"
    def __init__(self, sides):
        # instance attribute
        self.sides = sides


class Person:
    # class attribute
    type = "Human"
    def __init__(self, name):
        # instance attribute
        self.name = name


d6 = Dice(6)
d10 = Dice(10)
print(d6.sides, d10.sides, d6.type, d10.type)

tamas = Person("Tamás")
csaba = Person("Csaba")
csaba.name = "Béla"
Person.type = "Animal"
print(tamas.name, csaba.name, tamas.type, csaba.type)