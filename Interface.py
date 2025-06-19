from tkinter import *
from PIL import Image, ImageTk

# img = Image.open("HelloKitty.jpg")
# photo = ImageTk.PhotoImage(img)
# label = Label(self.root, image=photo)
# label.pack()

class Interface:
    def __init__(self, root=None):
        if root is None:
            self.root = Tk()
        else:
            self.root = root

    def setupWindow(self):
        self.root.title("WORKING WITH IMAGES")
        self.root.iconbitmap("favicon.ico")
        self.root.geometry("500x450+500+100")
        self.root.resizable(True, True)

    def openInterface(self):
        self.setupWindow()
        self.root.mainloop()

    def finish(self):
        self.root.destroy()
        print("Закрываемся")
