# Class definition
class Dice:
    # attributes of the Dice class
    sides = 6
    color = "White"


# Instances of Dice
d6 = Dice()

d10 = Dice()
d10.sides = 10
d10.color = "Blue"

d20 = Dice()
d20.sides = 20
d20.color = "Red"

print(d6.sides)
print(d10.sides)
print(d20.sides)