from tkinter import *


def doSomething():
    print('Hello World')

root = Tk()

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New File', command=doSomething)
subMenu.add_command(label='Open File...', command=doSomething)
subMenu.add_separator()
subMenu.add_command(label='Exit', command=quit)

editMenu = Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo', command=doSomething)

root.mainloop()
