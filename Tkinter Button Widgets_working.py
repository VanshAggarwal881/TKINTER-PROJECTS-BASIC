'''Every Button widget has a command attribute that you can assign to a function.
Whenever the button is pressed, the function is executed.'''

#create a window with a Label widget that holds a numeric value.
# You’ll put buttons on the left and right side of the label.
# The left button will be used to decrease the value in the Label,
# and the right one will increase the value.

from tkinter import *
window = Tk()

#giving button the commands by defining functions
'''inorder to increase or decrease the value of label getting and updating the value of text label 
is important so it can be done by usingit as an index or in the form of dictionary'''
def increase():
    value = int(lbl_value_0['text'])
    lbl_value_0['text'] = f"{value+1}"

def decrease():
    value = int(lbl_value_0['text'])
    lbl_value_0['text'] = f"{value-1}"


window.rowconfigure(0,weight=1,minsize=50)
window.columnconfigure([0,1,2],weight=1,minsize=50)

# giving decrease function to command attribute
btn_decrease = Button(master=window,text='-',command=decrease)
btn_decrease.grid(row=0,column=0,sticky='nsew')

lbl_value_0 = Label(master=window,text="0")
lbl_value_0.grid(row=0,column=1,sticky='nsew')

# giving increase function to command attribute
btn_increase = Button(master = window,text='+',command=increase)
btn_increase.grid(row=0,column=2,sticky='nsew')
window.mainloop()