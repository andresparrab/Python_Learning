class User:
    def sign_in(self):
        print("logged in")


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

    def check_arrows(self):
        print(f"{self.number_of_arrows} remaining")

    def attack(self):
        print(f"attacking with arrows: arrows left: {self.number_of_arrows}")

    def run(self):
        print("running really fast")


class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows):
        Archer.__init__(self, name, arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg("Andres", 50, 3)
print(hb1.run())
print(hb1.check_arrows())
print(hb1.attack())
