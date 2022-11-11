import random


class Charakters:
    HP = 100
    damage = 6

    def __init__(self, name):
        self.name = name

    def deal_damage(self, enemy):
        if random.randint(1, 8) == 1:
            enemy.HP -= self.damage * 2
            print(f"Char {self.name} dealt critical!")
        else:
            enemy.HP -= self.damage


class Dragon:
    HP = 1000
    damage = 8

    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        if random.randint(1, 8) == 1:
            enemy.HP -= self.damage * 2
            print(f"Drago dealt critical!")
        else:
            enemy.HP -= self.damage


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


class Gladiator(Charakters):
    HP = 125
    damage = 8

    def __init__(self, name):
        super().__init__(name)


class Necromancer(Charakters):
    HP = 85
    damage = 9

    def __init__(self, name):
        super().__init__(name)


class Assasin(Charakters):
    HP = 100
    damage = 7

    def __init__(self, name):
        super().__init__(name)


# ***********************************************************************************************************************

class PweMulti:
    def __init__(self, pwe_list_of_warriors: list, name="Drago"):
        self.pwe_list_of_warriors: list = pwe_list_of_warriors
        self.dragon = Dragon(name)

        if number_of_charakter1 == 1:
            self.charakter_1 = Amazon(name1)
        elif number_of_charakter1 == 2:
            self.charakter_1 = Barbarian(name1)
        elif number_of_charakter1 == 3:
            self.charakter_1 = Sorcerer(name1)
        elif number_of_charakter1 == 4:
            self.charakter_1 = Paladin(name1)
        elif number_of_charakter1 == 5:
            self.charakter_1 = Gladiator(name1)
        elif number_of_charakter1 == 6:
            self.charakter_1 = Necromancer(name1)
        elif number_of_charakter1 == 7:
            self.charakter_1 = Assasin(name1)
        else:
            exit("Number you have entered is out of range")

        if number_of_charakter2 == 1:
            self.charakter_2 = Amazon(name2)
        elif number_of_charakter2 == 2:
            self.charakter_2 = Barbarian(name2)
        elif number_of_charakter2 == 3:
            self.charakter_2 = Sorcerer(name2)
        elif number_of_charakter2 == 4:
            self.charakter_2 = Paladin(name2)
        elif number_of_charakter2 == 5:
            self.charakter_2 = Gladiator(name2)
        elif number_of_charakter2 == 6:
            self.charakter_2 = Necromancer(name2)
        elif number_of_charakter2 == 7:
            self.charakter_2 = Assasin(name2)
        else:
            exit("Number you have entered is out of range")

        if number_of_charakter3 == 1:
            self.charakter_3 = Amazon(name3)
        elif number_of_charakter3 == 2:
            self.charakter_3 = Barbarian(name3)
        elif number_of_charakter3 == 3:
            self.charakter_3 = Sorcerer(name3)
        elif number_of_charakter3 == 4:
            self.charakter_3 = Paladin(name3)
        elif number_of_charakter3 == 5:
            self.charakter_3 = Gladiator(name3)
        elif number_of_charakter3 == 6:
            self.charakter_3 = Necromancer(name3)
        elif number_of_charakter3 == 7:
            self.charakter_3 = Assasin(name3)
        else:
            exit("Number you have entered is out of range")

        if number_of_charakter4 == 1:
            self.charakter_4 = Amazon(name4)
        elif number_of_charakter4 == 2:
            self.charakter_4 = Barbarian(name4)
        elif number_of_charakter4 == 3:
            self.charakter_4 = Sorcerer(name4)
        elif number_of_charakter4 == 4:
            self.charakter_4 = Paladin(name4)
        elif number_of_charakter4 == 5:
            self.charakter_4 = Gladiator(name4)
        elif number_of_charakter4 == 6:
            self.charakter_4 = Necromancer(name4)
        elif number_of_charakter4 == 7:
            self.charakter_4 = Assasin(name4)
        else:
            exit("Number you have entered is out of range")

        if number_of_charakter5 == 1:
            self.charakter_5 = Amazon(name5)
        elif number_of_charakter5 == 2:
            self.charakter_5 = Barbarian(name5)
        elif number_of_charakter5 == 3:
            self.charakter_5 = Sorcerer(name5)
        elif number_of_charakter5 == 4:
            self.charakter_5 = Paladin(name5)
        elif number_of_charakter5 == 5:
            self.charakter_5 = Gladiator(name5)
        elif number_of_charakter5 == 6:
            self.charakter_5 = Necromancer(name5)
        elif number_of_charakter5 == 7:
            self.charakter_5 = Assasin(name5)
        else:
            exit("Number you have entered is out of range")

    def fight(self):
        while self.dragon.HP >= 0 and self.pwe_list_of_warriors != []:
            fighting_warrior: Charakters = self.pwe_list_of_warriors[0]
            fighting_warrior.deal_damage(Dragon)
            self.dragon.attack(fighting_warrior)
            print(f"HP Dragon is: {self.dragon.HP}")
            print(f"Warrior current HP is: {fighting_warrior.HP}")
            if fighting_warrior.HP <= 0:
                self.pwe_list_of_warriors.pop(0)

        if self.dragon.HP <= 0:
            print("Warrios Win!")
        else:
            print("Dragon Win!")


# ***********************************************************************************************************************

# class PWE:
#     def __init__(self, list_of_warriors: list, name="Drago"):
#         self.list_of_warriors: list = list_of_warriors
#         self.dragon = Dragon(name)
#
#     def fight(self):
#         while self.dragon.HP >= 0 and self.list_of_warriors != []:
#             fighting_warrior: Charakters = self.list_of_warriors[0]
#             fighting_warrior.deal_damage(self.dragon)
#             self.dragon.attack(fighting_warrior)
#             print(f"HP Dragon is: {self.dragon.HP}")
#             print(f"Warrior current HP is: {fighting_warrior.HP}")
#             if fighting_warrior.HP <= 0:
#                 self.list_of_warriors.pop(0)
#
#         if self.dragon.HP <= 0:
#             print("Warrios Win!")
#         else:
#             print("Dragon Win!")

# ***********************************************************************************************************************

# class Arena:
#     print("Choose your charakter")
#     print("1.Amazon")
#     print("2.Barbarian")
#     print("3.Sorcerer")
#     print("4.Paladin")
#     print("5.Gladiator")
#     print("6.Necromancer")
#     print("7.Assasin")

#
#     def __init__(self, name1, name2, number_of_charakter1, number_of_charakter2):
#
#         if number_of_charakter1 == 1:
#             self.charakter_1 = Amazon(name1)
#         elif number_of_charakter1 == 2:
#             self.charakter_1 = Barbarian(name1)
#         elif number_of_charakter1 == 3:
#             self.charakter_1 = Sorcerer(name1)
#         elif number_of_charakter1 == 4:
#             self.charakter_1 = Paladin(name1)
#          elif number_of_charakter1 == 5:
#             self.charakter_1 = Gladiator(name1)
#         elif number_of_charakter1 == 6:
#             self.charakter_1 = Necromancer(name1)
#         elif number_of_charakter1 == 7:
#            self.charakter_1 = Assasin(name1)
#         else:
#             exit("Number you have entered is out of range")
#
#         if number_of_charakter2 == 1:
#             self.charakter_2 = Amazon(name2)
#         elif number_of_charakter2 == 2:
#             self.charakter_2 = Barbarian(name2)
#         elif number_of_charakter2 == 3:
#             self.charakter_2 = Sorcerer(name2)
#         elif number_of_charakter2 == 4:
#             self.charakter_2 = Paladin(name2)
#         elif number_of_charakter2 == 5:
#             self.charakter_2 = Gladiator(name2)
#         elif number_of_charakter2 == 6:
#             self.charakter_2 = Necromancer(name2)
#         elif number_of_charakter2 == 7:
#             self.charakter_2 = Assasin(name2)
#         else:
#             exit("Number you have entered is out of range")
# #
#
#     def fight(self):
#         while self.charakter_1.HP >= 0 and self.charakter_2.HP >= 0:
#             self.charakter_1.deal_damage(self.charakter_2)
#             self.charakter_2.deal_damage(self.charakter_1)
#             self.show_score()
#
#         if self.charakter_1.HP > self.charakter_2.HP:
#             print(f"Charakter_1 Win. {self.charakter_1.name}")
#         else:
#             print(f"charakter_2 Win. {self.charakter_2.name}")
#
#     def show_score(self):
#         print("**********************************")
#         print(f"Char1 HP: {self.charakter_1.HP}")
#         print(f"Char2 HP: {self.charakter_2.HP}")

# ***********************************************************************************************************************

# list_of_warriors = []
# list_of_warriors.append(Amazon("Ama"))
# list_of_warriors.append(Barbarian("Konan"))
# list_of_warriors.append(Paladin("Pal"))
# list_of_warriors.append(Sorcerer("Mag"))
#
# pwe = PWE(list_of_warriors)
# pwe.fight()

# **********************************************************************************************************************
number_of_charakter1 = int(input("Enter number of 1. warrior: "))
number_of_charakter2 = int(input("Enter number of 2. warrior: "))
number_of_charakter3 = int(input("Enter number of 3. warrior: "))
number_of_charakter4 = int(input("Enter number of 4. warrior: "))
number_of_charakter5 = int(input("Enter number of 5. warrior: "))
name1 = input("Enter name of 1. warrior: ")
name2 = input("Enter name of 2. warrior: ")
name3 = input("Enter name of 3. warrior: ")
name4 = input("Enter name of 4. warrior: ")
name5 = input("Enter name of 5. warrior: ")

pwe_list_of_warriors = []
pwe_list_of_warriors.append(number_of_charakter1)
pwe_list_of_warriors.append(number_of_charakter2)
pwe_list_of_warriors.append(number_of_charakter3)
pwe_list_of_warriors.append(number_of_charakter4)
pwe_list_of_warriors.append(number_of_charakter5)

pwe_multi = PweMulti(pwe_list_of_warriors)
pwe_multi.fight()
# ***********************************************************************************************************************

# number_of_charakter1 = int(input("Enter number of first warrior: "))
# number_of_charakter2 = int(input("Enter number of second warrior: "))
# name1 = input("Enter name of first warrior: ")
# name2 = input("Enter name of second warrior: ")
#
# a = Arena(name1, name2, number_of_charakter1, number_of_charakter2)
# a.fight()

# ***********************************************************************************************************************
