from tkinter import *

class NumButton:
    def __init__(self, master, num, field):
        self.num = num
        self.N = Button(master, text=str(num), width=3, height=3)
        self.N.pack()
        



class OperationButton:
    pass

root = Tk()

WorkField = Entry(bg='white', fg='black', width=40)
def restart():
    WorkField.delete(0, END)

C = Button(text="C", width=3, height=3, command=restart)

n1 = NumButton(root, 1)
n1.PrntNum(WorkField)

WorkField.pack()
C.pack()

root.mainloop()
