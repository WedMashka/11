import random
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = random.randint(1, self.sides)
        print(x)

die = Die()
for i in range(10):
    die.roll_die()