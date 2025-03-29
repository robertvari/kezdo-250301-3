import time, random 

class Dice:
    def __init__(self, sides, color):
        # public attribute
        self.color = color

        # protected attribute
        self._color = color

        # private attribute
        self.__sides = sides
    
    def roll(self):
        print("Rolling...")
        time.sleep(random.randint(1, 3))
        print(f"Result: {random.randint(1, self.__sides)}")

    def __str__(self):
        return f"{self.color} {self.__sides}"


d6 = Dice(6, "White")
d6.roll()