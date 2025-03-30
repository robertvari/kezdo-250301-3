import random

class Player_BASE:
    def __init__(self):
        self.name = "Computer"
        self.magic_number = 10
    
    def think_number(self):
        self.magic_number = random.randint(1, 10)
    
    def say_hello(self):
        print(f"Hello! I'm {self.name}")


class Player(Player_BASE):
    def __init__(self):
        self.name = "Player"  # overrides BASE class name

class Computer(Player_BASE):
    pass


player = Player()
computer = Computer()

player.say_hello()
computer.say_hello()