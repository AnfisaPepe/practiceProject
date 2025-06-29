from tkinter import *
from tkinter import filedialog, simpledialog
from tkinter import Label
from PIL import Image, ImageFilter, ImageTk
from src.draw_line.DrawGreenLine import DrawGreenLine
from src.camera_capture.CameraCapture import CameraCapture


class Interface:
    def __init__(self, root=None):
        if root is None:
            self.root = Tk()
            self.label = Label(self.root)
            self.label.pack()
            self.img = None
            self.setup_window()
            self.work_menu()
        else:
            self.root = root

    def setup_window(self):
        self.root.title("WORKING WITH IMAGES")
        self.root.iconbitmap("assets/favicon.ico")
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
        main_menu.add_command(label="Сделать фото", command=self.camera_capture)
        return main_menu

    # n - индекс цвета
    def channels(self, n):
        if self.img:
            photo = ImageTk.PhotoImage(self.img.split()[n])
            self.label.config(image=photo)
            self.label.image = photo

    def image_channels_menu(self):
        channels_menu = Menu(self.root)
        channels_menu.add_command(
            label="Синий",
            command=lambda: self.channels(0)
        )
        channels_menu.add_command(
            label="Зеленый",
            command=lambda: self.channels(1)
        )
        channels_menu.add_command(
            label="Красный",
            command=lambda: self.channels(2)
        )
        return channels_menu

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
        if self.img:
            DrawGreenLine(self.img, self.root, self.label)

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
            command=self.draw_line
        )
        return edit_menu

    def work_file_menu(self):
        channels_menu = self.image_channels_menu()
        file_menu = Menu(self.root)
        file_menu.add_command(
            label="Открыть",
            command=lambda: self.png_file()
        )
        file_menu.add_cascade(
            label="Каналы изображения",
            menu=channels_menu
        )
        return file_menu

    def png_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
        )
        if file_path:
            self.img = Image.open(file_path)
            resized_img = self.img_correct(self.img)
            photo = ImageTk.PhotoImage(resized_img)
            self.label.config(image=photo)
            self.label.image = photo

    def img_correct(self, img):
        # Подстраиваем ширину image под окно
        new_width = self.root.winfo_width()
        # Параметры изображения
        orig_width, orig_height = img.size
        # Новая высота для изображения
        new_height = int(orig_height * (new_width / orig_width))
        # Если высота изображения больше окна:
        if new_height > self.root.winfo_height():
            new_height = self.root.winfo_height()
            new_width = int(orig_width * (new_height / orig_height))

        resized_img = self.img.resize((new_width, new_height), Image.LANCZOS)
        return resized_img

    def camera_capture(self):
        camera = CameraCapture(self.root)
        camera.open_camera()
        frame = camera.capture()
        self.img = frame
        photo = ImageTk.PhotoImage(self.img)
        self.label.config(image=photo)
        self.label.image = photo

    def open_interface(self):
        self.root.mainloop()
