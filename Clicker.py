from tkinter import *
import time

window = Tk()
window.title('Clicker')
window.geometry("700x500")
count = 0
hand_made = 1
auto_add = 0
auto_add_period = 10000

def HandPlus(event):
    global count
    count += hand_made
    label['text'] = str(count)

def HandUpgrade():
    global hand_made
    global count
    if count >= 10:
        count -= 10
        label['text'] = str(count)
        hand_made += 1

def AutoUpgrade():
    global auto_add
    global count
    if count >= 50:
        count -= 50
        label['text'] = str(count)
        auto_add += 1

def auto_addiction():
    global count
    count += auto_add
    label['text'] = str(count)

def AutoPlus():
    auto_addiction()
    window.after(auto_add_period, AutoPlus)

window.bind('<space>', HandPlus)
label = Label(window, text=str(count)+'$', font=('Helvetica 100'))
HandUpgradeButton = Button(text="ручная работа - 10", background="#000", foreground="#fff",
             padx="50", pady="8", font="16", command=HandUpgrade)
AutoUpgradeButton = Button(text="авто работа - 50", background="#000", foreground="#fff",
             padx="50", pady="8", font="16", command=AutoUpgrade)
label.pack()
HandUpgradeButton.pack()
AutoUpgradeButton.pack()
AutoPlus()

mainloop()
