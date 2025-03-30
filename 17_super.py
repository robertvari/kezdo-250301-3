import random

class Player_BASE:
    def __init__(self):
        self.name = "Computer"
        self.magic_number = 1
        self.health = 100
        self.dexterity = 30
        self.inteligence = 12
        self.inventory = []
    
    def think_number(self):
        self.magic_number = random.randint(1, 10)
    
    def say_hello(self):
        print(f"Hello! I'm {self.name}")

class Player(Player_BASE):
    # partial override
    def __init__(self):
        super().__init__()
        self.name = "Player"  # overrides BASE class name
        self.dexterity = 50
    
    # full override
    def say_hello(self):
        print("Hello! I'm the Player")

class Computer(Player_BASE):
    pass


player = Player()
computer = Computer()

player.say_hello()