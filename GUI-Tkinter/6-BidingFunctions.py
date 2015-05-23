from tkinter import *

root = Tk()

'''def printHi():
	print('Hello World')


button1 = Button(root, text="Print Hi",command=printHi)
button1.pack()
'''
def printHi(event):
	print('Hello World')

button1 = Button(root, text="Print Hi")
button1.bind("<Button-1>",printHi)
button1.pack()

root.mainloop()