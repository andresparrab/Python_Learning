class Menu:
    def __init__(self, prompt, choice):
        self.prompt = prompt
        self.choice = choice
        self.balance = 560000

    def withdrawal(self):
        amount = int(input('Please enter the amount you want to withdraw: '))
        self.balance -= amount
        return self.balance

    def pay_in(self):
        amount = int(input('Please enter the amount you want to pay: '))
        self.balance += amount
        return self.balance
    def return_card(self):
        return  input('Thank you for choosing Andres bank inc.\n We hope to see you again soon \n')




