from tkinter import *


class App:

    def __init__(self,	master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(
            frame, text="Print something", command=lambda: print('Hello World'))
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.pack(side=LEFT)


root = Tk()
a = App(root)
root.mainloop()
