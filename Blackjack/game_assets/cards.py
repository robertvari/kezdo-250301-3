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

    def __str__(self):
        return f"Name: {self.__name} Value: {self.__value}"

    def __repr__(self):
        return self.__name

if __name__ == "__main__":
    card1 = Card("Club Ace", 11)
    card2 = Card("Diamon King", 10)
    card3 = Card("Spade 3", 3)
    
    deck = [card1, card2, card3]
    print(card1.name)