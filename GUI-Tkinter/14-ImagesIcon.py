from tkinter import *
root = Tk()

photo = PhotoImage(file='python.png')
label = Label(root, image=photo)
label.pack()

root.mainloop()
