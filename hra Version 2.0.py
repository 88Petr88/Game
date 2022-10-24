import random


class Arena:

    def Fight(self):
        zivot_Barbara = 100
        zivot_Paladina = 100
        self.zivot_Barbara = zivot_Barbara
        self.zivot_Paladina = zivot_Paladina

        while self.zivot_Barbara >= 0 and self.zivot_Paladina >= 0:
            critical_Paladina = random.randint(1, 5)
            critical_Barbara = random.randint(1, 5)
            if critical_Paladina != 1 or critical_Barbara != 1:
                if critical_Paladina == 1:
                    poskozeni_Paladina = random.randint(4, 7)
                    poskozeni_Paladina *= 2
                    self.zivot_Barbara -= poskozeni_Paladina
                    poskozeni_Barbara = random.randint(3, 8)
                    self.zivot_Paladina -= poskozeni_Barbara
                    print(f"HP Paladina je: {self.zivot_Paladina} HP Barbara je: {self.zivot_Barbara}")
                elif critical_Barbara == 1:
                    poskozeni_Barbara = random.randint(3, 8)
                    poskozeni_Barbara *= 2
                    self.zivot_Paladina -= poskozeni_Barbara
                    poskozeni_Paladina = random.randint(4, 7)
                    self.zivot_Barbara -= poskozeni_Paladina
                    print(f"HP Paladina je: {self.zivot_Paladina} HP Barbara je: {self.zivot_Barbara}")
                else:
                    poskozeni_Paladina = random.randint(4, 7)
                    poskozeni_Barbara = random.randint(3, 8)
                    self.zivot_Paladina -= poskozeni_Barbara
                    self.zivot_Barbara -= poskozeni_Paladina
                    print(f"HP Paladina je: {self.zivot_Paladina} HP Barbara je: {self.zivot_Barbara}")
            else:
                poskozeni_Paladina = random.randint(4, 7)
                poskozeni_Paladina *= 2
                poskozeni_Barbara = random.randint(3, 8)
                poskozeni_Barbara *= 2
                self.zivot_Paladina -= poskozeni_Barbara
                self.zivot_Barbara -= poskozeni_Paladina
                print(f"HP Paladina je: {self.zivot_Paladina} HP Barbara je: {self.zivot_Barbara}")

        if self.zivot_Paladina > self.zivot_Barbara:
            print("Vyhral Paladin")
        else:
            print("Vyhral Barbar")


arena = Arena()
arena.Fight()
