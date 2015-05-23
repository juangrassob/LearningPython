from tkinter import *

root = Tk()

one = Label(root, text="One",bg="red", fg="white")
one.pack()
two = Label(root, text="two",bg="yellow", fg="green")
two.pack(fill=X)
three = Label(root, text="Three",bg="blue", fg="white")
three.pack(side=LEFT,fill=Y)

root.mainloop()