class User:
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} is attacking with the {self.power} spell ")


class Archer(User):
    def __init__(self, name, number_of_arrows):
        self.name = name
        self.number_of_arrows = number_of_arrows


wizard1 = Wizard("Andres", "Firaga 3")
print(wizard1.sign_in())
print(wizard1.power)
archer = Archer("green Arrow", 55)
print(archer.sign_in())
print(archer.name)
print(archer.number_of_arrows)
wizard1.attack()
