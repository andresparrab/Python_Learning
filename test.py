# list = [x**2 for x in [1,2,3,4,5]]
# print(list)

# print('Hello %s, my name is %s and i am %d years old' %('Gloria','Andy',35))
#
# str= 'hello my name is andy and im the best'
# print(str.replace('a','__A__',2))

# str1 = 'Happy Learning '
# str2 = 'Welcome to python'
#
# print(str1 + str2)
# print(str1*2)
#
# x= set("Welkome to Eureka")
# print(x)

# a={1,2,3,4,5,6}
# b={4,5,6,7,8,9}
# print(a-b)

def count_small(numbers):
  total = 0
  for n in numbers:
    if n < 10:
      total = total + 1
  return total

lotto = [4, 8, 15, 16, 23, 42]
small = count_small(lotto)
print (small)


##testing stuff
Print('mongo')



#CLASSES INNHERITANCES
class Shape(object):
  """Makes shapes!"""
  def __init__(self, number_of_sides):
    self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
  def __init__(self,side1,side2,side3):
    self.side1 = side1
    self.side2 = side2
    self.side3 = side3



