import os, random, time


class MagicNumber:
    def __init__(self):
        # Create our attributes
        self.computer = Computer()
        self.player = Player()

        # Start our methods
        self.clear_screen()
        self.intro()

        time.sleep(2)

        if self.player.ask("Are you ready?"):
            self.game_loop()
        self.exit_game()
    
    def game_loop(self):
        print("Start game...")
    
    def exit_game(self):
        self.clear_screen()
        print("Thank you for playing my game :))) See you next time!")

    @staticmethod
    def clear_screen():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    def intro(self):
        print("-"*50, "The Magic Number Game", "-"*50)
        print(f"I think of a number between {self.computer.min_number} and {self.computer.max_number}. Can you guess it?")

class Player:
    def ask(self, question):
        result = input(f"{question} (y/n)")
        
        valid_characters = "yn"

        while result not in valid_characters:
            MagicNumber.clear_screen()
            print("Wrong answer. Only use y/n.")
            result = input(f"{question} (y/n)")
        
        return result == "y"

class Computer:
    def __init__(self):
        self.min_number = 1
        self.max_number = 10


MagicNumber()