from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from editting import *
from cv2 import *

class Interface:
    def __init__(self, root=None):
        if root is None:
            self.root = Tk()
            self.label = Label(self.root)
            self.label.pack()
            self.img = None
            self.work_menu()
        else:
            self.root = root

    def setup_window(self):
        self.root.title("WORKING WITH IMAGES")
        self.root.iconbitmap("favicon.ico")
        self.root.geometry("800x600+400+100")
        self.root.resizable(True, True)
        self.root.option_add("*tearOff", False)

    def work_menu(self):
        main_menu = Menu(self.root)
        self.root.config(menu=main_menu)
        file_menu = self.work_file_menu()
        edit_menu = self.work_edit_menu()
        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Изменить", menu=edit_menu)
        main_menu.add_cascade(label="Сделать фото")
        return main_menu

    def sharpness_up(self):
        if self.img:
            sharpened = self.img.filter(ImageFilter.SHARPEN)
            photo = ImageTk.PhotoImage(sharpened)
            self.label.config(image=photo)
            self.label.image = photo
            self.img = sharpened

    def rotate_image(self):
        if self.img:
            angle = simpledialog.askfloat(
                "Вращение",
                "Угол наклона: ",
                minvalue=0,
                maxvalue=360
            )
            if angle is not None:
                rotated = self.img.rotate(angle, expand=True)
                photo = ImageTk.PhotoImage(rotated)
                self.label.config(image=photo)
                self.label.image = photo
                self.img = rotated

    def draw_line(self):
        pass

    def work_edit_menu(self):
        edit_menu = Menu(self.root)
        edit_menu.add_command(
            label="Повысить резкость изображения",
            command=lambda: self.sharpness_up()
        )
        edit_menu.add_command(
            label="Выполнить вращение изображения",
            command=lambda: self.rotate_image()
        )
        edit_menu.add_command(
            label="Нарисовать линию на изображении зеленым цветом",
            command=lambda: self.draw_line()
        )
        return edit_menu

    def work_file_menu(self):
        file_menu = Menu(self.root)
        file_menu.add_cascade(
            label="Открыть",
            command=lambda: self.png_file()
            )
        file_menu.add_cascade(
            label="Сохранить как",
            command=lambda: self.save_file())
        return file_menu

    def png_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.img = Image.open(file_path)
            #Подстраиваем ширину image под окно
            new_width = self.root.winfo_width()
            #Параметры изображения
            orig_width, orig_height = self.img.size
            #Новая высота для изображения
            new_height = int(orig_height * (new_width/orig_width))
            resized_img = self.img.resize((new_width, new_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(resized_img)
            self.label.config(image=photo)
            self.label.image = photo

    def save_file(self):
        pass

    def open_interface(self):
        self.setup_window()
        self.root.mainloop()

    def finish(self):
        self.root.destroy()
        print("Закрываемся")
