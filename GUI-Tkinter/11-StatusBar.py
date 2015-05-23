from tkinter import *


def doSomething():
    print('Hello World')

root = Tk()

#  Main Menu

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

#  Tool Bar

toolbar = Frame(root, bg='blue')
insertButt = Button(toolbar, text='Insert Image', command=doSomething)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt = Button(toolbar, text='Print', command=doSomething)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

#  Status Bar

status = Label(root, text='Preparing to do do something', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)
root.mainloop()
