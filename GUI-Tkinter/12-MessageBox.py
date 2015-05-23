from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo('Window Title', 'Monkey can live up to 300')

answer = tkinter.messagebox.askquestion(
    'Question1', 'Do you like silly faces?')

if answer == 'yes':
    print(' :D ')
root.mainloop()
