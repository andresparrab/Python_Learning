#OOP
class PlayerCharacter:
    # Class Object attribute
    memberchip = True
    def __init__(self, name, age):
        if (PlayerCharacter.memberchip):
            self.name = name # attributes (dynamic)
            self.age = age
    def shout(self):
        shouting = print(f"my name is {self.name}")
        return "done"

player1 = PlayerCharacter("Cindy", 44)
player2 = PlayerCharacter("Tom", 21)
player2.attack = 50

print(player2.name)
print(player2.age)
print(player2.attack)
print(player2.shout())
