import time, random

class Dice:
    def __init__(self, sides, color):
        self.color = color
        self.sides = sides
    
    def roll(self):
        print("Rolling....")
        time.sleep(random.randint(1, 3))
        print(f"The result is: {random.randint(1, self.sides)}")

class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print(f"Hello, my name is {self.name}. How are you?")

d6 = Dice(6, "White")
tamas = Person("Tamás")
csaba = Person("Csaba")

tamas.say_hello()
csaba.say_hello()