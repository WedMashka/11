import random
class Die:
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        x = random.randint(1, self.sides)
        print(x)

print("--------------------------10 sides------------------------")
die = Die(10)
for i in range(10):
    die.roll_die()


print("--------------------------20 sides------------------------")
die = Die(20)
for i in range(10):
    die.roll_die()