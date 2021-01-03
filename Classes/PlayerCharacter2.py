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
    def attack(self):
        print(f"attacking with arrows: arrows left: {self.number_of_arrows}")


wizard1 = Wizard("Andres", "Firaga 3")
print(wizard1.sign_in())
print(wizard1.power)
archer1 = Archer("green Arrow", 55)
print(archer1.sign_in())
print(archer1.name)
print(archer1.number_of_arrows)
#Polymorphism, same name of the method attack, but react different
# depending of the object tha call them
archer1.attack()
wizard1.attack()
print("---------------Using abstraction------------------------")
# Polymorphism abstraction
def player_attack(char):
    return char.attack()
player_attack(wizard1)
player_attack(archer1)

# Anothe way usin for loop
print("----------------Using for loop-----------------------")
for char in [wizard1, archer1]:
    char.attack()

# Check if the object is an instance
print(isinstance(wizard1,Wizard))