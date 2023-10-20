import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import win32api
import win32con

# Предопределенные разрешения экрана
resolutions = [
    (1920, 1080),
    (1280, 720),
    (1600, 900),
]

# Функция для изменения разрешения экрана
def change_resolution():
    selected_resolution = resolution_var.get()
    width, height = resolutions[selected_resolution]

    try:
        win32api.ChangeDisplaySettings(None, 0)
        dm = win32api.EnumDisplaySettings(None, 0)
        dm.PelsWidth = width
        dm.PelsHeight = height
        win32api.ChangeDisplaySettings(dm, 0)
        messagebox.showinfo("Успех", f"Разрешение экрана изменено на {width}x{height}.")

    except Exception as e:
        messagebox.showerror("Ошибка", "Не удалось изменить разрешение экрана.")

# Создаем главное окно
root = tk.Tk()
root.title("Изменение разрешения экрана")

# Создаем переменную для выбранного разрешения
resolution_var = tk.IntVar(value=0)

# Создаем интерфейс
label = tk.Label(root, text="Выберите разрешение:")
label.pack()

for i, (width, height) in enumerate(resolutions):
    rb = tk.Radiobutton(root, text=f"{width}x{height}", variable=resolution_var, value=i)
    rb.pack()

change_button = tk.Button(root, text="Изменить разрешение", command=change_resolution)
change_button.pack()

# Запускаем главный цикл
root.mainloop()
