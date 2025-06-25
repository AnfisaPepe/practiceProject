from tkinter import *
from tkinter import messagebox
from PIL import ImageDraw, ImageTk


class DrawGreenLine:
    def __init__(self, img, root):
        self.frame = Frame(root)
        self.frame.pack(fill="both", expand=True)
        self.img = img.copy()
        self.draw = ImageDraw.Draw(self.img)
        self.photo = ImageTk.PhotoImage(self.img)
        self.label = Label(self.frame, image=self.photo)
        self.label.pack()
        input_frame = Frame(self.frame)
        input_frame.pack(pady=10)

        Label(input_frame, text="x1:").pack(side=LEFT, padx=2)
        self.x1 = Entry(input_frame, width=5)
        self.x1.pack(side=LEFT)

        Label(input_frame, text="y1:").pack(side=LEFT, padx=2)
        self.y1 = Entry(input_frame, width=5)
        self.y1.pack(side=LEFT)

        Label(input_frame, text="x2:").pack(side=LEFT, padx=2)
        self.x2 = Entry(input_frame, width=5)
        self.x2.pack(side=LEFT)

        Label(input_frame, text="y2:").pack(side=LEFT, padx=2)
        self.y2 = Entry(input_frame, width=5)
        self.y2.pack(side=LEFT)
        Label(input_frame, text="Толщина").pack(side=LEFT, padx=2)
        self.entry_width = Entry(input_frame, width=5)
        self.entry_width.pack(side=LEFT)

        self.draw_button = Button(
            self.frame,
            text="Нарисовать линию",
            command=self.draw_the_line
        )
        self.draw_button.pack(pady=5)

    def draw_the_line(self):
        try:
            x1 = int(self.x1.get())
            y1 = int(self.y1.get())
            x2 = int(self.x2.get())
            y2 = int(self.y2.get())
            entry_width = int(self.entry_width.get())
            self.draw.line(
                (x1, y1, x2, y2),
                fill="green",
                width=entry_width
            )
            self.photo = ImageTk.PhotoImage(self.img)
            self.label.image = self.photo
            self.label.config(image=self.photo)
        except ValueError:
            messagebox.showerror(
                "Ошибка",
                "Введены некорректные данные"
            )
