class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power, email):
       # User.__init__(self,email)   # WE CALLED THE USER:s __INIT method inside the wizard to initiate the user email
        # MUCH BETTER WAY USE SUPER , see below
        super().__init__(email)
        self.name = name
        self.power = power


    def attack(self):
        print(f"{self.name} is attacking with the {self.power} spell ")


class Archer(User):
    def __init__(self, name, number_of_arrows):
        self.name = name
        self.number_of_arrows = number_of_arrows

    def attack(self):
        print(f"attacking with arrows: arrows left: {self.number_of_arrows}")


wizard1 = Wizard("Andres", "Firaga 3", "andres@gmail.com")
print(wizard1.sign_in())
print(wizard1.power)
print(wizard1.email)
