class Car(object):
  condition ='new'
  def __init__(self,model,color,mpg):
    self.model =model
    self.color = color
    self.mpg = mpg

  def display_car(self):
    return 'This is a %s %s with %s MPG.' % (self.color,self.model,str(self.mpg))

  def drive_car(self):
    self.condition = 'used'

class ElectricCar(Car):

    def __init__(self, battery_type):
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = 'Like new'


my_car = Car('DeLorean','silver',88)
print(my_car.display_car(),' And is in %s condition' %(my_car.condition))

print('After driving my car, the condition would be: ')
my_car.drive_car()
print(my_car.condition)

my_electric_car = ElectricCar('molten salt')
my_electric_car.model = 'Tesla'
my_electric_car.color = 'Black'
my_electric_car.mpg = 44

print(my_electric_car.display_car(),' And it runs on %s' %(my_electric_car.battery_type))
print('After driving my car, the condition would be: ')
my_electric_car.drive_car()
print(my_electric_car.condition)

