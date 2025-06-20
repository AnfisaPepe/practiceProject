from tkinter import *
from PIL import ImageDraw, Image, ImageTk

class DrawGreenLine:
    def __init__(self, img, root):
        self.root = root
        self.img = img
        self.draw = ImageDraw.Draw(self.img)
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(root, image=self.photo)
        self.label.pack()
        self.start_x = None
        self.start_y = None

        self.label.bind("<Button-1>", self.on_mouse_down)
        self.label.bind("<B1-Motion>", self.on_mouse_drag)
        self.label.bind("<ButtonRelease-1>", self.on_mouse_up)

