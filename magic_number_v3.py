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
        else:
            self.exit_game()
    
    def game_loop(self):
        self.clear_screen()
        try_count = 3
        print(f"You have {try_count} tries.")

        self.computer.think_number()
        self.player.think_number()

        while self.computer.magic_number != self.player.magic_number:
            try_count -= 1
            if try_count == 0:
                break
            self.clear_screen()

            print(f"Wrong guess! You have {try_count} tries left.")
            self.player.think_number()

        # End game condition
        self.clear_screen()

        if self.computer.magic_number == self.player.magic_number:
            print(f"You won. My number was {self.computer.magic_number}")
            self.player.give_credits(10)
        else:
            print("You lost this round :(")
            self.player.take_credits(10)

        if self.player.ask("Do you want to play again?"):
            self.game_loop()
        else:
            self.exit_game()
    
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
        print(f"You start with {self.player.credits} credits. On each round I give you 10 credits.")
        print("If you lost all your credits the game ends.")

class Player:
    def __init__(self):
        self.magic_number = None
        self.credits = 100
    
    def give_credits(self, credits):
        self.credits += credits
        print(f"You won {credits}. Now you have {self.credits}")
    
    def take_credits(self, credits):
        self.credits -= credits
        print(f"You lost {credits}. Now you have {self.credits}")

    def think_number(self):
        result = input("What is your guess? ")

        valid_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

        while result not in valid_numbers:
            MagicNumber.clear_screen()
            print("Wrong number.")
            result = input("What is your guess? ")

        self.magic_number = int(result)

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
        self.magic_number = None
    
    def think_number(self):
        self.magic_number = random.randint(self.min_number, self.max_number)


MagicNumber()