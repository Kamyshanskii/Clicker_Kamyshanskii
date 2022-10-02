from tkinter import *

#Создание окна
root = Tk()
root.title("Clicker")

#Задание размеров
root.geometry("1280x560")
canvas_width = 1280
canvas_height = 560
root.resizable(0,0)


#Создание фона
img = PhotoImage(file="background.gif")
Back = Canvas(root, width=canvas_width, height=canvas_height)
Back.pack()
Back.create_image(canvas_width/2, canvas_height/2, image=img)

#Переменные
Count = 0.00      #Текущая сумма
HandDelta = 1.00  #Бонус за клик мышкой/пробелом
HandPrice = 10    #Цена улучшения клика мышкой/пробелом
AutoDelta = 0.25  #Бонус от автоклика
AutoPrice = 20    #Цена улучшения автоклика


#Обновление данных на экране после действия
def CountUpdate():
    global Count
    HandAddiction['text'] = "Текущий счет: " + str(Count) + '$'
    HandUpgrade['text'] = "Ручное улучшение за " + str(HandPrice) + '$'
    AutoUpgrade['text'] = "Авто улучшение за " + str(AutoPrice) + '$'

#Действие при ручном клике
def HandChange(event):
    global Count
    global HandDelta
    Count += HandDelta
    CountUpdate()

#Действие при авто клике
def AutoChange():
    global Count
    global AutoDelta
    Count += AutoDelta
    CountUpdate()

#Автоклик
def AutoUpdate():
    AutoChange()
    root.after(1000, AutoUpdate)

#Действие при улучшении ручного клика
def UpgradeFunction(event):
    global Count
    global HandPrice
    global HandDelta
    if Count >= HandPrice:
        Count -= HandPrice
        HandDelta *= 1.5
        HandDelta = round(HandDelta)
        HandPrice *= 2
    CountUpdate()

#Действие при улучшении авто клика
def AutoUpgradeFunction(event):
    global Count
    global AutoPrice
    global AutoDelta
    if Count >= AutoPrice:
        Count -= AutoPrice
        AutoDelta *= 2
        AutoPrice *= 3
    CountUpdate()


#Счетчик + Кнопка ручного клика
HandAddiction = Button(Back, text="Текущий счет: 0.0$", anchor="center")
HandAddictionCanvas = Back.create_window(canvas_width/2, canvas_height/2, anchor="center", window=HandAddiction)

#Кнопка улучшения ручного клика
HandUpgrade = Button(Back, text="Ручное улучшение за " + str(HandPrice) + '$', anchor="center")
HandUpgradeСanvas = Back.create_window(canvas_width/2, canvas_height/2 + 30, anchor="center", window=HandUpgrade)

#Кнопка улучшения авто клика
AutoUpgrade = Button(Back, text="Авто улучшение за " + str(AutoPrice) + '$', anchor="center")
AutoUpgradeСanvas = Back.create_window(canvas_width/2, canvas_height/2 + 60, anchor="center", window=AutoUpgrade)

#Cвязь событий
HandAddiction.bind('<Button-1>', HandChange)
root.bind('<space>', HandChange)
HandUpgrade.bind('<Button-1>', UpgradeFunction)
AutoUpgrade.bind('<Button-1>', AutoUpgradeFunction)

#запуск автокликера
AutoUpdate()

#запуск цикла обаботки событий
mainloop()