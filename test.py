'''
import sys

print(len(sys.argv))

print(sys.argv)

name = input('Enter your name')
age = input('enter you age')

print('welcome %s'%(name))
print('your age is : %d'%(int(age)))

print('After five year you age woud be: %2d' %(int(age)+5))


from  functools import reduce
product = reduce(lambda x,y:(x**2)*y,[1,2,3,4])
print(product)

1*1=1
4*1=4
4*9=36
36*16
'''
import datetime
print(datetime.time)

import json
json_string = json.dumps(data)
print(type(json_string))
print(json_string)
json_string['name']= 'Andres'