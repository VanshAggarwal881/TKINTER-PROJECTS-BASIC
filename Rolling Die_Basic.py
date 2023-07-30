import random
from tkinter import *
window = Tk()

def random_roll():
    value = random.randint(1,6)
    num_lbl['text'] = f"{value}"


window.rowconfigure([0,1],weight=1,minsize=50)
window.columnconfigure(0,weight=1,minsize=50)
window.title("ROLL THE DIE")
roll_btn = Button(master=window,text="Roll",command=random_roll,relief=RAISED,borderwidth=2)
roll_btn.grid(row=0,column=0,sticky='nsew')
num_lbl = Label(master=window,text='1')
num_lbl.grid(row=1,column=0,sticky='nsew')
window.mainloop()
