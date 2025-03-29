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

    def set_color(self, new_color):
        valid_colors = ["white", "red", "green", "blue"]
        assert new_color in valid_colors, f"New color is not valid. It can be {valid_colors}"
        self.__color = new_color    

    def get_sides(self):
        return self.__sides

    def __str__(self):
        return f"{self.__color} {self.__sides}"


d6 = Dice(6, "white")
d6.set_color(10)
print(d6)