import random

class Player_BASE:
    def __init__(self):
        self.__name = None
        self.__credits = random.randint(10, 100)
        self.__hand = []
        self.__playing = True

    def create(self):
        self.__name = self.get_random_name()
    
    @staticmethod
    def get_random_name():
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    def __str__(self):
        return f"Name: {self.__name} Credits: {self.__credits}"

class Player(Player_BASE):
    pass

class Computer(Player_BASE):
    pass


if __name__ == "__main__":
    player = Player()
    computer = Computer()

    player.create()
    computer.create()

    print(player)
    print(computer)