import time


class Clicker:
    #Переменные
    def __init__(self):
        self.Count = 0.00      #Текущая сумма
        self.HandDelta = 1.00  #Бонус за клик мышкой/пробелом
        self.HandPrice = 10    #Цена улучшения клика мышкой/пробелом
        self.AutoDelta = 0.25  #Бонус от автоклика
        self.AutoPrice = 20    #Цена улучшения автоклика
        self.PrevUpdate = time.time()

    #Обновление данных на экране после действия
    def CountUpdate(self):
        self.Count = round(self.Count, 2)
        chr = {"Текущий счет: ": str(self.Count) + '$',
               "Цена ручного улучшения: ": str(self.HandPrice) + '$',
               "Цена авто улучшения: ": str(self.AutoPrice) + '$'}
        return dict(chr)

    #Действие при ручном клике
    def HandChange(self):
        self.Count += self.HandDelta

    #Действие при авто клике
    def AutoChange(self):
        self.Count += self.AutoDelta * (time.time() - self.PrevUpdate)
        self.PrevUpdate = time.time()

    #Действие при улучшении ручного клика
    def UpgradeFunction(self):
        if self.Count >= self.HandPrice:
            self.Count -= self.HandPrice
            self.HandDelta *= 1.5
            self.HandDelta = round(self.HandDelta)
            self.HandPrice *= 2

    #Действие при улучшении авто клика
    def AutoUpgradeFunction(self):
        if self.Count >= self.AutoPrice:
            self.Count -= self.AutoPrice
            self.AutoDelta *= 2
            self.AutoPrice *= 3
