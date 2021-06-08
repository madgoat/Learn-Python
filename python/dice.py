import random
class Die(object):
  def __init__(self, sides):
    self.sides = sides
  def roll(self):
    return random.randint(1, self.sides)

d = Die(6)
d1 = Die(6)
d20 = Die(20)
print ("First Die   : ", d.roll())
print ("Second Die  : ", d1.roll())
print ("Your D20 is : ", d20.roll())

