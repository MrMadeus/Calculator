from tkinter import *

root = Tk()

WorkField = Entry(bg='white', fg='black', width=40)
def restart():
    WorkField.delete(0, END)
def insert(num):
    WorkField.insert(END, str(num))

C = Button(text="C", width=3, height=3, command=restart)

n = []

for i in range(10):
    n.append(Button(text=str(i), width=3, height=3))
    if i == 0:
        n[i].grid(row=2, column=4)
    elif (i%3) == 0:
        n[i].grid(row=i//3, column=3)
    elif (i%3) == 1:
        n[i].grid(row=1+(i//3), column=2)
    elif (i%3) == 2:
        n[i].grid(row=1+(i//3), column=1)


n[0].bind('<Button-1>', insert(0))
n[1].bind('<Button-1>', insert(1))
n[2].bind('<Button-1>', insert(2))
n[3].bind('<Button-1>', insert(3))
n[4].bind('<Button-1>', insert(4))
n[5].bind('<Button-1>', insert(5))
n[6].bind('<Button-1>', insert(6))
n[7].bind('<Button-1>', insert(7))
n[8].bind('<Button-1>', insert(8))
n[9].bind('<Button-1>', insert(9))

WorkField.grid(row=0, column=0)
C.grid(row=1, column=4)

root.mainloop()
