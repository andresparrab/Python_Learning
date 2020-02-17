"""
Area calculator by Andres Parra
"""

from math import pi
from datetime import datetime
from time import sleep

print('Welcome to Area calculator, with this program you can calculate the area of a circle or a triangle.'
      '\n calculator is starting...\n')
sleep(2)
time = datetime.now()
print('Time of initialisation:  %02d-%02d-%02d @  %02d:%02d' %(time.year,time.month,time.day,time.hour,time.minute))

choice = input('Please enter the form of the shape: \nC for circle\nT for triangle')

while choice != 'c' and choice!= 't':
    input('Please enter C or T').lower()

if choice == 'c':
    while True:
        try:
            radius = float(input('Input the radius: '))
            break
        except:
            print('Wrong input. Please enter a valid radius: ')

    area = pi*radius**2
    print('Processing....')
    sleep(2)
    print('The Area is: %.2f' %(area)+' units')

else:
    while True:
        try:
            base = float(input('Input the base: '))
            break
        except:
            print('Wrong input. Please enter a valid base: ')
    while True:
        try:
            height = float(input('Input the height: '))
            break
        except:
            print('Wrong input. Please enter a valid height: ')
    area = (height*base)/2
    print('Processing.....')
    sleep(2)
    print('Triangles area is: %0.2f' %(area) +' units')