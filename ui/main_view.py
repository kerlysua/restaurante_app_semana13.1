import tkinter as tk

class MainView:
    def __init__(self, root, servicio, cambiar_a_login):
        self.root = root
        self.servicio = servicio
        self.cambiar_a_login = cambiar_a_login

        tk.Label(root, text="Panel Principal - Restaurante", font=("Arial", 14)).pack(pady=10)

        tk.Button(root, text="Listar productos", command=self.listar_productos).pack(pady=5)
        tk.Button(root, text="Listar usuarios", command=self.listar_usuarios).pack(pady=5)
        tk.Button(root, text="Cerrar sesión", command=self.cambiar_a_login).pack(pady=5)

        self.text_area = tk.Text(root, width=60, height=15)
        self.text_area.pack(pady=10)

    def listar_productos(self):
        productos = self.servicio.listar_productos()
        self.text_area.delete("1.0", tk.END)
        for p in productos:
            self.text_area.insert(tk.END, p.mostrar_informacion() + "\n")

    def listar_usuarios(self):
        usuarios = self.servicio.listar_usuarios()
        self.text_area.delete("1.0", tk.END)
        for u in usuarios:
            self.text_area.insert(tk.END, u.mostrar_informacion() + "\n")
