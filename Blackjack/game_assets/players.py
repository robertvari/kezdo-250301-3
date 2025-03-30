import random, time

class Player_BASE:
    def __init__(self):
        self._name = None
        self.__credits = 0
        self.__hand = []
        self.__playing = True

    def create(self):
        self._name = self.get_random_name()
        self.__credits = random.randint(10, 100)
    
    def draw(self, deck):
        while self.playing:
            if self.hand_value <= 19:
                print(f"{self.name} draws card...")
                time.sleep(2)
                new_card = deck.draw()
                self.add_card(new_card)
            else:
                print(f"{self.name} finishes drawing")
                self.playing = False

    def show_hand(self):
        print(self.__hand, f"Hand value: {self.hand_value}")

    def add_card(self, card):
        if self.hand_value > 10 and card.value == 11:
            card.change_value()
        
        self.__hand.append(card)

    @staticmethod
    def get_random_name():
        first_names = ["Liam", "Emma", "Noah", "Olivia", "Ethan", "Ava", "James", "Sophia", "Benjamin", "Mia"]
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

        return f"{random.choice(first_names)} {random.choice(last_names)}"

    @property
    def hand_value(self):
        return sum([card.value for card in self.__hand])

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

    def draw(self, deck):
        print(f"This is your turn {self.name}")

        while self.playing:
            if self.hand_value > 21:
                print("Your hand value is greater than 21")
                self.playing = False
                break

            self.show_hand()
            response = input("Do you want to draw a card? (y/n)")
            if response == "y":
                new_card = deck.draw()
                print(f"You card: {new_card}")
                self.add_card(new_card)
            else:
                self.playing = False

class Computer(Player_BASE):
    pass


if __name__ == "__main__":
    from cards import Deck

    deck = Deck()

    computer = Computer()
    player = Player()

    player.create()
    computer.create()
    
    player.draw(deck)
    computer.draw(deck)

    player.show_hand()
    computer.show_hand()