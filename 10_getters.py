import time, random 

class Dice:
    def __init__(self, sides, color):
        self.__color = color
        self.__sides = sides
    
    def roll(self):
        print("Rolling...")
        time.sleep(random.randint(1, 3))
        print(f"Result: {random.randint(1, self.__sides)}")
    
    def get_color(self):
        return self.__color
    
    def get_sides(self):
        return self.__sides

    def __str__(self):
        return f"{self.__color} {self.__sides}"


d6 = Dice(6, "White")
print(d6.get_color(), d6.get_sides())