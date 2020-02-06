answer = 13
guess = int(input('Please guess a number:   '))

while(guess != answer):
    if(guess < answer):
        print('Number is too small...try again!')
        guess = int(input('Please guess a number:   '))
    elif(guess > answer):
        print('Number is to big...try again!')
        guess = int(input('Please guess a number:   '))

print('Congratulation you win!!!')

print('End of the game')