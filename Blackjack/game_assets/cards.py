import random

class Card:
    def __init__(self, name, value):
        self.__name = name
        self.__value = value
  
    @property
    def value(self):
        return self.__value
    
    @property
    def name(self):
        return self.__name

    def change_value(self):
        if self.__value == 11:
            self.__value = 1

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"

    def __repr__(self):
        return self.__name

class Deck:
    def __init__(self):
        self.__cards = []
        self.create()

    def create(self):
        self.__cards.clear()

        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        suits = ["Heart ♥", "Club ♣", "Diamond ♦", "Spade ♠"]
        for suit in suits:
            for card in cards:
                new_card = Card(f"{suit} {card[0]}", card[1])
                self.__cards.append(new_card)

        random.shuffle(self.__cards)

    def draw(self):
        return self.__cards.pop(0)

    def show_cards(self):
        print(self.__cards)

if __name__ == "__main__":
    # creates a shuffled deck on instance
    # refresh deck on new round
    # ability to draw a card

    deck = Deck()

    cards = []

    for i in range(3):
        new_card = deck.draw()
        cards.append(new_card)

    print(cards)