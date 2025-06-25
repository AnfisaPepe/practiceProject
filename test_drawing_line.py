import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw


class DrawGreenLine:
    def __init__(self, parent_widget, image_object):
        self.main_frame = tk.Frame(parent_widget)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.img = image_object.copy()
        self.draw = ImageDraw.Draw(self.img)

        # --- ИЗМЕНЕНИЕ №1: Сохраняем PhotoImage как атрибут класса ---
        self.photo_image = ImageTk.PhotoImage(self.img)

        # Передаем этот атрибут в Label
        self.label = tk.Label(self.main_frame, image=self.photo_image)
        self.label.pack()

        # Frame для полей ввода
        input_frame = tk.Frame(self.main_frame)
        input_frame.pack(pady=10)

        # Поля ввода (здесь без изменений)
        tk.Label(input_frame, text="x1:").pack(side=tk.LEFT, padx=2)
        self.x1 = tk.Entry(input_frame, width=5)
        self.x1.pack(side=tk.LEFT)
        # ... (остальные поля)
        tk.Label(input_frame, text="y1:").pack(side=tk.LEFT, padx=2)
        self.y1 = tk.Entry(input_frame, width=5)
        self.y1.pack(side=tk.LEFT)
        tk.Label(input_frame, text="x2:").pack(side=tk.LEFT, padx=2)
        self.x2 = tk.Entry(input_frame, width=5)
        self.x2.pack(side=tk.LEFT)
        tk.Label(input_frame, text="y2:").pack(side=tk.LEFT, padx=2)
        self.y2 = tk.Entry(input_frame, width=5)
        self.y2.pack(side=tk.LEFT)
        tk.Label(input_frame, text="Толщина:").pack(side=tk.LEFT, padx=2)
        self.entry_width = tk.Entry(input_frame, width=5)
        self.entry_width.pack(side=tk.LEFT)

        draw_button = tk.Button(self.main_frame, text="Нарисовать", command=self.draw_the_line)
        draw_button.pack()

    def draw_the_line(self):
        try:
            x1 = int(self.x1.get())
            y1 = int(self.y1.get())
            x2 = int(self.x2.get())
            y2 = int(self.y2.get())
            width = int(self.entry_width.get())
            self.draw.line((x1, y1, x2, y2), fill="green", width=width)

            # --- ИЗМЕНЕНИЕ №2: Обновляем тот же самый атрибут ---
            self.photo_image = ImageTk.PhotoImage(self.img)
            self.label.config(image=self.photo_image)
            # self.label.image = self.photo_image # Эта строка больше не нужна, т.к. ссылка уже сохранена в self.photo_image

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные числа!")


# --- Код для запуска теста ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Тест с сохранением ссылки")
    root.geometry("600x500")
    test_image = Image.new("RGB", (500, 300), "white")
    app = DrawGreenLine(root, test_image)
    root.mainloop()