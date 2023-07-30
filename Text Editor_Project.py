from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# giving commands to buttons by making functions
# open command
def open_file():
    '''using the askopenfilename() dialog from the tkinter.filedialog module to display a file open dialog
    and store the selected file path to filepath.'''
    # open file for editing
    path = askopenfilename(filetypes=[('Text Files','*.txt'),
                                      ('All Files','*.*')]
                           )
    '''if the user closes the dialog box or clicks the Cancel button ,path will be None,
    and the function will return without executing any of the code to read the file and set the text of text_edit.'''
    if not path:
        return

    text_edit.delete('1.0',END) # clears the current content of text edit. '1.0' means first(0) character
    # at first line(1) to the end of the text.

    # open the selected file and .read() its contents before storing the text as a string.
    with open(path,mode='r',encoding='utf-8') as chosen_file:
        file = chosen_file.read()
        text_edit.insert(END,file)
    window.title(f"Text Editor - {path}")

# save command
def save_file():
    path = asksaveasfilename(defaultextension='.txt',
                             filetypes=[('Text Files','.txt'),
                                        ('All Files','*.*')]
                             )

    if not path:
        return

    with open(path,mode='w',encoding='utf-8') as write_file:
        '''extracts the text from txt_edit with .get() method and assigns it to the variable text.'''
        file = text_edit.get('1.0',END)

        # writes text to the write_file.
        write_file.write(file)
    window.title(f"Text Editor - {path}")


window = Tk()
window.title('Text Editor')
window.rowconfigure(0,weight=1,minsize=600)
window.columnconfigure(1,weight=1,minsize=600)
'''By configuring just the second column, the text box will expand and contract naturally when the window is resized,
while the column containing the buttons will remain at a fixed width.'''
left_frame = Frame(master=window)
# text editor to write something
text_edit = Text(master=window)
# open button
open_btn = Button(master=left_frame,width=5,relief=RAISED,text='OPEN',bd=2,command=open_file)
# save button
save_btn = Button(master=left_frame,width=5,relief=RAISED,text = 'SAVE',bd=2,command=save_file)
'''inside the frame row and col. sticky forces it to stay in the respective direction'''
open_btn.grid(row=0,column=0,padx=5,pady=10,sticky='ew')
save_btn.grid(row=1,column=0,sticky='ew',padx=5)

'''since there are two columns inside the window one is taken by the frame'''
left_frame.grid(row=0,column=0,sticky='ns')
'''inside the second column text editor is present'''
text_edit.grid(row=0,column=1,sticky='nsew')

# runs the application
window.mainloop()