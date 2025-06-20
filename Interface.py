from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from PIL import Image, ImageTk, ImageFilter
from work_with_file import *
from editting import *

class Interface:
    def __init__(self, root=None):
        if root is None:
            self.root = Tk()
            self.label = Label(self.root)
            self.label.pack()
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
        file_menu = self.work_file_menu()
        edit_menu = self.work_edit_menu()
        main_menu.add_cascade(label="Файл", menu=file_menu)
        main_menu.add_cascade(label="Изменить", menu=edit_menu)
        main_menu.add_cascade(label="Сделать фото")
        return main_menu

    def sharpness_up(self, img):
        sharpened = img.filter(ImageFilter.SHARPEN)
        sharpened.save("sharpened.jpg")
        photo = ImageTk.PhotoImage(sharpened)
        label.config(image=photo)
        label.image = photo

    def work_edit_menu(self):
        edit_menu = Menu(self.root)
        img = self.png_file()
        edit_menu.add_cascade(
            label="Повысить резкость изображения",
            command=lambda: self.sharpness_up(img)
        )
        edit_menu.add_cascade(
            label="Выполнить вращение изображения"
        )
        edit_menu.add_cascade(
            label="Нарисовать линию на изображении зеленым цветом"
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
            img = Image.open(file_path)
            #Подстраиваем ширину image под окно
            new_width = self.root.winfo_width()
            #Параметры изображения
            orig_width, orig_height = img.size
            #Новая высота для изображения
            new_height = int(orig_height * (new_width/orig_width))
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)
            photo = ImageTk.PhotoImage(resized_img)
            self.label.config(image=photo)
            self.label.image = photo
            return photo

    def save_file(self):
        pass

    # def buttons(self):
    #     Button(
    #         text="Повысить резкость изображения.",
    #         font="Kefa",
    #         bg="tan",
    #         fg="#2F2F2F"
    #     ).pack(anchor=NW, padx=5, pady=5)
    #
    #     Button(
    #         text="Выполнить вращение изображения.",
    #         font="Kefa",
    #         bg="tan",
    #         fg="#2F2F2F"
    #     ).pack(anchor=NW, padx=5, pady=5)
    #
    #     Button(
    #         text="Нарисовать линию на изображении зеленым цветом.",
    #         font="Kefa",
    #         bg="tan",
    #         fg="#2F2F2F"
    #     ).pack(anchor=NW, padx=5, pady=5)

    def open_interface(self):
        self.setup_window()
        main_menu = self.work_menu()
        self.root.config(menu=main_menu)
        self.root.mainloop()

    def finish(self):
        self.root.destroy()
        print("Закрываемся")
