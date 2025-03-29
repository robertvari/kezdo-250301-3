class Dice:
    # the constructor
    def __init__(self, sides, color):
        self.color = color
        self.sides = sides


d10 = Dice(10, "Blue")
d6 = Dice(6, "White")
d20 = Dice(20, "Red")

print(d10.color, d10.sides)