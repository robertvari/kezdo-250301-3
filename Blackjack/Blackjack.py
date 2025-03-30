import os
from game_assets.cards import Deck
from game_assets.players import Player, Computer


class Blackjack:
    def __init__(self):
        self.__deck = Deck()
        self.__player_list = [
            Computer(),
            Computer(),
            Computer()
        ]

        self.clear_screen()
        self.intro()

        self.__player = Player()
        self.__player_list.insert(0, self.__player)

        self.game_loop()

    def game_loop(self):
        self.clear_screen()
        self.__deck.create()

        for p in self.__player_list:
            p.init_hand(self.__deck)
        
        for p in self.__player_list:
            p.draw(self.__deck)

        self.get_winner()
        
    def get_winner(self):
        self.clear_screen()
        player_list = [p for p in self.__player_list if p.hand_value <= 21]

        if not player_list:
            print("House wins")
        else:
            sorted_winners = sorted(player_list, key=lambda p: p.hand_value)
            winner = sorted_winners[-1]
            print(f"The winner: {winner.name}")
        
        response = input("Do you want to play again? (y/n)")
        if response == "y":
            self.game_loop()
        else:
            self.exit_game()
    
    def exit_game(self):
        print("Thank you for playing my game :)")

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

Blackjack()