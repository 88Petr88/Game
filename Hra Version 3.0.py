import random


class Charakters:
    HP = 100
    damage = 6

    def __init__(self, name):
        self.name = name


class Amazon(Charakters):
    HP = 100
    damage = 9

    def __init__(self, name):
        super().__init__(name)


class Barbarian(Charakters):
    damage = 7
    HP = 150

    def __init__(self, name):
        super().__init__(name)


class Sorcerer(Charakters):
    HP = 80
    damage = 10

    def __init__(self, name):
        super().__init__(name)


class Paladin(Charakters):
    HP = 125
    damage = 8

    def __init__(self, name):
        super().__init__(name)


class Game:
    print("Choose your charakter")
    print("1.Amazon")
    print("2.Barbarian")
    print("3.Sorcerer")
    print("4.Paladin")

    def __init__(self, charakter1, charakter2):

        self.charakter_1 = charakter1
        self.charakter_2 = charakter2

        if self.charakter_1 == "1":
            self.charakter_1 = f"{Amazon(Charakters.HP)}"
        elif self.charakter_1 == "2":
            self.charakter_1 = f"{Barbarian(Charakters.HP)}"
        elif self.charakter_1 == "3":
            self.charakter_1 = f"{Sorcerer(Charakters.HP)}"
        elif self.charakter_1 == "4":
            self.charakter_1 = f"{Paladin(Charakters.HP)}"

        else:
            print("Number you have entered is out of range")

        if self.charakter_2 == "1":
            self.charakter_2 = f"{Amazon(Charakters.HP)}"
        elif self.charakter_2 == "2":
            self.charakter_2 = f"{Barbarian(Charakters.HP)}"
        elif self.charakter_2 == "3":
            self.charakter_2 = f"{Sorcerer(Charakters.HP)}"
        elif self.charakter_2 == "4":
            self.charakter_2 = f"{Paladin(Charakters.HP)}"
        else:
            print("Number you have entered is out of range")

    # def critical_amazon(self):
    #     self.critical_amazon = random.randint(1, 8)
    #     if self.critical_amazon == 1:
    #         self.damage = Amazon.damage * 2
    #
    # def holy_light(self):
    #     self.holy_light = random.randint(1, 10)
    #     if self.holy_light == 1:
    #         self.damage = Paladin.damage * 2.5
    #
    # def fire_ball(self):
    #     self.fire_ball = random.randint(1, 6)
    #     if self.fire_ball == 1:
    #         self.damage = Sorcerer.damage * 3

    def fight(self):
        while self.charakter_1 >= 0 and self.charakter_2 >= 0:
            self.charakter_1 -= f"{Charakters.damage}"
            self.charakter_2 -= f"{Charakters.damage}"
        if self.charakter_1 > self.charakter_2:
            print(f"Charakter_1 Win.{self.charakter_1}")
        else:
            print(f"charakter_2 Win. {self.charakter_2}")


game = Game("1", "2")
game.fight()
