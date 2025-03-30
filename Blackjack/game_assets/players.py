class Player_BASE:
    def __init__(self):
        self.__name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

    def __str__(self):
        return f"Name: {self.__name} Credits: {self.__credits}"

class Player(Player_BASE):
    pass

class Computer(Player_BASE):
    pass


if __name__ == "__main__":
    player = Player()
    computer = Computer()

    print(player)