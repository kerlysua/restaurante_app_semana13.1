import tkinter as tk
from servicios.restaurante import Restaurante
from ui.login_view import LoginView
from ui.main_view import MainView

def main():
    root = tk.Tk()
    root.geometry("600x400")
    servicio = Restaurante()

    def mostrar_login():
        for widget in root.winfo_children():
            widget.destroy()
        LoginView(root, servicio, mostrar_main)

    def mostrar_main():
        for widget in root.winfo_children():
            widget.destroy()
        MainView(root, servicio, mostrar_login)

    mostrar_login()
    root.mainloop()

if __name__ == "__main__":
    main()
#fin