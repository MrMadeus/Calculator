from tkinter import *

global w, h

w = 4
h = 4

class NumButt:
    def __init__(self, n):
        self.n = n
        self.butt = Button(text=str(self.n), width=w, height=h)
        self.butt.bind('<Button-1>', self.input)
        if self.n == 0:
            self.butt.grid(row=4, column=1)
        elif (self.n % 3) == 0:
            self.butt.grid(row=i//3, column=3)
        elif (self.n % 3) == 1:
            self.butt.grid(row=1+(i//3), column=1)
        elif (self.n % 3) == 2:
            self.butt.grid(row=1+(i//3), column=2)

    def input(self, event):
        WorkField.insert(END, str(self.n))

class OperButt:
    def __init__(self, s, place):
        self.s = s
        self.place = place
        self.butt = Button(text=str(self.s), width=w, height=h)
        self.butt.bind('<Button-1>', self.input)
        self.butt.grid(row=self.place[0], column=self.place[1])
    def input(self, event):
        WorkField.insert(END, self.s)

root = Tk()

WorkField = Entry(bg='white', fg='black', width=30, justify=RIGHT)
def restart():
    '''function of resart working field'''
    WorkField.delete(0, END)
def calculate():
    '''function to get the result'''
    pass

C = Button(text="C", width=w, height=h, command=restart)
Calc = Button(text="=", width=w, height=h, command=calculate)

n = []

for i in range(10):
    n.append(NumButt(i))

Summ = OperButt('+', (2, 4))
Mult = OperButt('*', (3, 4))

WorkField.grid(row=0, column=0, columnspan=12)
C.grid(row=1, column=4)
Calc.grid(row=4, column=4)

root.mainloop()

