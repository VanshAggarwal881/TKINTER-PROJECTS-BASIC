from tkinter import *
# Fahrenheit To Celsius
# converting function
def F_to_C():
    # retrieve and give the value to f entered in the gui window
    f = enter_temp.get()
    # convert f into float
    f = float(f)
    # formula : c = (5/9) * (f - 32)
    c = (5/9) * (f - 32)
    # replace the text of label with value of c
    ans_label['text'] = f"{round(c,2)} \N{DEGREE CELSIUS}"

window = Tk()
window.title("Temperature Converter")
# window.rowconfigure(0,weight=1,minsize=50)
window.columnconfigure([0,1,2],weight=1,minsize=50)

# temperature input
frame_entry = Frame(master=window)
enter_temp = Entry(master=frame_entry,width=10)
temp_label = Label(master=frame_entry,text='\N{DEGREE FAHRENHEIT}')
'''with the help of frame container we can set the two widgets that is entry and label side by side
using grid '''
enter_temp.grid(row=0,column=0,sticky='w')
temp_label.grid(row=0,column=1,sticky='e')

# arrow button
button = Button(master=window,text='\N{RIGHTWARDS BLACK ARROW}',command=F_to_C)
# initial label for celsius
ans_label = Label(master=window,text='\N{DEGREE CELSIUS}')
# set up the layout
# padding lead to space between them
frame_entry.grid(row=0,column=0,padx=10)
button.grid(row=0,column=1,padx=10)
ans_label.grid(row=0,column=2,padx=10)
# run application
window.mainloop()