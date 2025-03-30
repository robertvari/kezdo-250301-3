import random

class Player_BASE:
    def __init__(self):
        self.name = "Computer"
        self.magic_number = 1
    
    def think_number(self):
        self.magic_number = random.randint(1, 10)
    
    def say_hello(self):
        print(f"Hello! I'm {self.name}")

class Player(Player_BASE):
    def __init__(self):
        super().__init__()
        self.credits = 100  # extend BASE attributes

    # add new method to Player
    def ask(self, question):
        result = input(question)

class Computer(Player_BASE):
    pass


player = Player()
computer = Computer()

player.ask("Have you slept?")