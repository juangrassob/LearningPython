from tkinter import *


def leftClick(event):
    print('Left')


def midClick(event):
    print('Mid')


def rightClick(event):
    print('Right')

frame = Frame(root, width=300, height=250)

frame.bind("<Button-1>", leftClick)
frame.bind("<Button-2>", midClick)
frame.bind("<Button-3>", rightClick)
frame.pack()

root = Tk()
root.mainloop()
