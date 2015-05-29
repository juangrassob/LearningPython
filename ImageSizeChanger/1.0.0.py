from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


def resizeimage(path):
    load_image = Image.open(path)
    resize_image = load_image.resize((100, 100))
    render_image = ImageTk.PhotoImage(resize_image)
    return(render_image)


class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, 'ImageSizeChanger')
        self.path = 'asd.png'
        self.initwindow()

    def initwindow(self):
        self.frame = Frame(self)
        self.frame.pack()

        self.image_resized = resizeimage(self.path)
        self.image_label = Label(self.frame, image=self.image_resized)
        self.image_label.pack(side=TOP)
        load_button = Button(
            self.frame, text='Select...', command=self.changeimage)
        load_button.pack(side=TOP)
'''
        size_x = Entry(self.frame)
        size_x.pack(side=BOTTOM)
        size_y = Entry(self.frame)
        size_y.pack(side=BOTTOM)
        x = size_x.get()
        y = size_y.get()
        resize_button = Button(
            self.frame, text='Resize', command=tipona(x))
        resize_button.pack(side=BOTTOM)
'''

    def changeimage(self):
        self.path = askopenfilename()
        self.image_resized = resizeimage(self.path)
        self.image_label.destroy()
        self.image_label = Label(self.frame, image=self.image_resized)
        self.image_label.pack(side=TOP)


application = App()
application.mainloop()
