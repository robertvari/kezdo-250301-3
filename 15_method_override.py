import random

class Player_BASE:
    def __init__(self):
        self.magic_number = 10
    
    def think_number(self):
        self.magic_number = random.randint(1, 10)
    
    def say_hello(self):
        print("Hello!")


class Player(Player_BASE):
    def say_hello(self):
        print("Hello! I'm the player :))")

class Computer(Player_BASE):
    pass


player = Player()
computer = Computer()

player.say_hello()
computer.say_hello()