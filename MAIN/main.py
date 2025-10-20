print("INTERFACES GENERALES")
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import ImageTk, Image
import io
import base64

class GymApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("DAC PILATES")
        self.window.geometry("800x600")
        self.window.configure(bg="#d9b59c")
        self.usuario_actual = None
        self.celular_actual = None
    def crear_imagen(self,ancho, alto, color="#16213e"):
        img = Image.new("RGB", (ancho, alto), color)
        return ImageTk.PhotoImage(img)

    def mostrar_login(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.window.geometry("800x600")

        main_frame = tk.Frame(self.window, bg="#d9b59c")
        main_frame.pack(fill=tk.BOTH, expand=True)

        left_frame = tk.Frame(main_frame, bg="#d9b59c")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=40, pady=40)

        right_frame = tk.Frame(main_frame, bg="#d9b59c")
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        img = self.crear_imagen(350, 600, "#d9b59c")
        img_label = tk.Label(left_frame, image=img, bg="#d9b59c")
        img_label.image = img
        img_label.pack(fill=tk.BOTH, expand=True)
    def run(self):
        self.window.mainloop()
if __name__ == "__main__":
    app = GymApp()
    app.run()