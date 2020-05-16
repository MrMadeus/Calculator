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
    n.append(Button(text=str(i), command=insert(i)))
    n[i].pack(side=LEFT)

WorkField.pack()
C.pack()

root.mainloop()
