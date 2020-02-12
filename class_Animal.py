# Class definition
class Animal(object):
  is_alive = True
  health = 'good'
  """Makes cute animals."""
  # For initializing our instance objects
  def __init__(self, name, age, is_hungry):
    self.name = name
    self.age = age
    self.is_hungry = is_hungry

  def description(self):
      print(self.name)
      print(self.age)


zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
hippo= Animal('Blinkish',6,False)
sloth= Animal('Blindo',3,False)
ocelot = Animal('lotis',4,True)

print(zebra.name, zebra.age, zebra.is_hungry, zebra.is_alive)
print(giraffe.name, giraffe.age, giraffe.is_hungry, giraffe.is_alive)
print(panda.name, panda.age, panda.is_hungry, panda.is_alive)
print(hippo.description())
print(hippo.health)
print(sloth.health)
print(ocelot.health)