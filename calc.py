from tkinter import *

class NumButton:
    pass

class OperationButton:
    pass

root = Tk()

WorkField = Entry(bg='white', fg='black', width=40)
def restart():
    WorkField.delete(0, END)

C = Button(text="C", width=3, height=3, command=restart)

WorkField.pack()
C.pack()

root.mainloop()
