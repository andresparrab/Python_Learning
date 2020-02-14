from ATM.ATM_Menu_Class import Menu

def card_digits(digits):
    control = 1234
    tries = 0
    while control != digits and tries <2:
        digits = int(input('Wrong code. Please try again :'))
        tries += 1
    if tries == 2:
        print('\nYour card is blocked for live\n')
    else:
        return print('Correct PIN.\n\nPlease choose one of the following chooises: ')


digits = int(input('Please enter your PIN-code:   '))
card_digits(digits)

prompt_choises = [
    'a) Check Balance.',
    'b) Make withdrawal.',
    'c) Pay in.',
    'd) Return card',
]

menu = [
    Menu(prompt_choises[0],'a'),
    Menu(prompt_choises[1],'b'),
    Menu(prompt_choises[2],'c'),
    Menu(prompt_choises[3],'d')
]


def run_Atm(menu):
    for client in menu:
        print(client.prompt)
    answer = input('Enter your choice or die by the sword: ')
    if answer == 'a':
            print('Your balance is : ', client.balance, 'KR')
    elif answer == 'b':
#        new_balance = client.withdrawal()
        print('Your balance is now: ', client.withdrawal(), 'KR')
    elif answer == 'c':
        print('Your balance is now: ', client.pay_in(), 'KR')
    else:
        client.return_card()

rerun='y'
while rerun == 'y':
    run_Atm(menu)
    rerun = input("Do you wish to see the menu again?  yes/no   ")
    if rerun =='n':
        print('Thank you for using Andres banc, enjoy your day!')

