import os
from time import sleep

game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]


def gameboard():
    print('   a  b  c')
    for count, row in enumerate(game):
        print(count, row)


os.system('clear')
gameboard()
game[0][0] = 1
sleep(2)
os.system('clear')
gameboard()
game[1][1] = 1
sleep(2)
os.system('clear')
gameboard()
