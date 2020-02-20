
import sys

print(len(sys.argv))

print(sys.argv)

name = input('Enter your name')
age = input('enter you age')

print('welcome %s'%(name))
print('your age is : %d'%(int(age)))

print('After five year you age woud be: %2d' %(int(age)+5))