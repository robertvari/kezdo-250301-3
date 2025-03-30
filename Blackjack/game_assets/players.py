import random

class Player_BASE:
    def __init__(self):
        self._name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

    def create(self):
        self._name = self.get_random_name()
        self.__credits = random.randint(10, 100)
    
    @staticmethod
    def get_random_name():
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    @property
    def name(self):
        return self._name
    
    @property
    def credits(self):
        return self.__credits

    @property
    def hand(self):
        return tuple(self.__hand)
    
    @property
    def playing(self):
        return self.__playing
    
    @playing.setter
    def playing(self, new_value):
        assert isinstance(new_value, bool), "Value must be either True or False"
        self.__playing = new_value

    def __str__(self):
        return f"Name: {self._name} Credits: {self.__credits}"

class Player(Player_BASE):
    def create(self):
        super().create()
        self._name = "Robert Vari"

class Computer(Player_BASE):
    pass


if __name__ == "__main__":
    player = Player()
    computer = Computer()

    player.create()
    computer.create()

    print(player.playing)
    player.playing = False
    print(player.playing)