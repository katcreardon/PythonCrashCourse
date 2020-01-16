from random import randint

class Die():
    """Represents a die."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(randint(1, self.sides))


d6 = Die()
i = 0
while i < 10:
    d6.roll_die()
    i += 1

d10 = Die(10)
j = 0
while j < 10:
    d10.roll_die()
    j += 1

d20 = Die(20)
k = 0
while k < 10:
    d20.roll_die()
    k += 1
