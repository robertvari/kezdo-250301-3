import os
from game_assets.cards import Deck

class Blackjack:
    def __init__(self):
        self.__deck = Deck()

        self.clear_screen()
        self.intro()

    @staticmethod
    def clear_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    @staticmethod
    def intro():
        print("-"*50, "BLACKJACK", "-"*50)
        print("Wellcome to Blackjack!")
        print("Get as close to 21 as possible without going over. Beat the others.")
        print("If your hand is higher than the others without going over 21 → You win.")
        input("Press Enter to continue...")

Blackjack()