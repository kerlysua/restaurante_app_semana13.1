import tkinter as tk

class LoginView:
    def __init__(self, root, servicio, cambiar_a_main):
        self.root = root
        self.servicio = servicio
        self.cambiar_a_main = cambiar_a_main

        tk.Label(root, text="Usuario").pack()
        self.entry_usuario = tk.Entry(root)
        self.entry_usuario.pack()

        tk.Label(root, text="Contraseña").pack()
        self.entry_contrasena = tk.Entry(root, show="*")
        self.entry_contrasena.pack()

        self.label_mensaje = tk.Label(root, text="")
        self.label_mensaje.pack()

        tk.Button(root, text="Ingresar", command=self.validar_acceso).pack()

    def validar_acceso(self):
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()
        if self.servicio.validar_acceso(usuario, contrasena):
            self.cambiar_a_main()
        else:
            self.label_mensaje.config(text="Acceso denegado")
