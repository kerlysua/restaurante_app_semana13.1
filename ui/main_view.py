import tkinter as tk
from tkinter import ttk, messagebox


class MainView:

    def __init__(self, root, servicio, cambiar_a_login):

        self.root = root
        self.servicio = servicio
        self.cambiar_a_login = cambiar_a_login

        self.crear_interfaz()
        self.cargar_productos()

        self.root.bind(
            "<Return>",
            self.evento_enter
        )

        self.root.bind(
            "<Escape>",
            self.evento_escape
        )

    def crear_interfaz(self):

        panel_menu = tk.Frame(
            self.root,
            bg="#2c3e50",
            width=180
        )
        panel_menu.pack(side="left", fill="y")

        panel_principal = tk.Frame(self.root)
        panel_principal.pack(
            side="right",
            fill="both",
            expand=True
        )
        self.icon_producto = tk.PhotoImage(
            file="assets/producto.png"
        )

        self.icon_producto = self.icon_producto.subsample(8, 8)

        self.icon_usuario = tk.PhotoImage(
            file="assets/usario.png"
        )

        self.icon_usuario = self.icon_usuario.subsample(8, 8)

        self.icon_venta = tk.PhotoImage(
            file="assets/ventaa.png"
        )

        self.icon_venta = self.icon_venta.subsample(20, 20)


        tk.Label(
            panel_menu,
            text="RESTAURANTE",
            bg="#2c3e50",
            fg="white",
            font=("Arial", 14, "bold")
        ).pack(pady=10)
        tk.Button(
            panel_menu,
            text=" Productos",
            image=self.icon_producto,
            compound="left",
            command=self.mostrar_productos
        ).pack(pady=5)

        tk.Button(
            panel_menu,
            text=" Usuarios",
            image=self.icon_usuario,
            compound="left",
            command=self.mostrar_usuarios
        ).pack(pady=5)

        tk.Button(
            panel_menu,
            text=" Ventas",
            image=self.icon_venta,
            compound="left",
            command=self.mostrar_ventas
        ).pack(pady=5)

        tk.Button(
            panel_menu,
            text="Cerrar sesión",
            width=15,
            command=self.cambiar_a_login
        ).pack(pady=5)

        formulario = tk.LabelFrame(
            panel_principal,
            text="Gestión de Productos"
        )

        formulario.pack(
            fill="x",
            padx=10,
            pady=10
        )

        # Código
        tk.Label(
            formulario,
            text="Código"
        ).grid(row=0, column=0, padx=5, pady=5)

        self.codigo = tk.Entry(formulario)
        self.codigo.grid(row=0, column=1)



        # Nombre
        tk.Label(
            formulario,
            text="Nombre"
        ).grid(row=1, column=0, padx=5, pady=5)

        self.nombre = tk.Entry(formulario)
        self.nombre.grid(row=1, column=1)

        # Categoría
        tk.Label(
            formulario,
            text="Categoría"
        ).grid(row=2, column=0, padx=5, pady=5)

        self.categoria = tk.Entry(formulario)
        self.categoria.grid(row=2, column=1)

        # Precio
        tk.Label(
            formulario,
            text="Precio"
        ).grid(row=0, column=2, padx=5, pady=5)

        self.precio = tk.Entry(formulario)
        self.precio.grid(row=0, column=3)

        # Stock
        tk.Label(
            formulario,
            text="Stock"
        ).grid(row=1, column=2, padx=5, pady=5)

        self.stock = tk.Entry(formulario)
        self.stock.grid(row=1, column=3)

        # Botones CRUD
        tk.Button(
            formulario,
            text="Registrar",
            bg="green",
            fg="white",
            command=self.registrar_producto
        ).grid(row=3, column=0, padx=5, pady=5)

        tk.Button(
            formulario,
            text="Actualizar",
            bg="orange",
            command=self.actualizar_producto
        ).grid(row=3, column=1, padx=5, pady=5)

        tk.Button(
            formulario,
            text="Eliminar",
            bg="red",
            fg="white",
            command=self.eliminar_producto
        ).grid(row=3, column=2, padx=5, pady=5)

        tk.Button(
            formulario,
            text="Mostrar Todos",
            command=self.cargar_productos
        ).grid(row=3, column=3, padx=5, pady=5)

        # Consulta por código
        tk.Label(
            formulario,
            text="Buscar Código"
        ).grid(row=4, column=0, padx=5, pady=5)

        self.buscar_codigo = tk.Entry(formulario)
        self.buscar_codigo.grid(row=4, column=1)

        tk.Button(
            formulario,
            text="Consultar",
            bg="blue",
            fg="white",
            command=self.consultar_producto
        ).grid(row=4, column=2, padx=5, pady=5)

        # Tabla
        self.tabla = ttk.Treeview(
            panel_principal,
            columns=(
                "codigo",
                "nombre",
                "categoria",
                "precio",
                "stock"
            ),
            show="headings"
        )

        self.tabla.heading(
            "codigo",
            text="Código"
        )

        self.tabla.heading(
            "nombre",
            text="Nombre"
        )

        self.tabla.heading(
            "categoria",
            text="Categoría"
        )

        self.tabla.heading(
            "precio",
            text="Precio"
        )

        self.tabla.heading(
            "stock",
            text="Stock"
        )

        self.tabla.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_producto
        )

    def limpiar_campos(self):

        self.codigo.delete(0, tk.END)
        self.nombre.delete(0, tk.END)
        self.categoria.delete(0, tk.END)
        self.precio.delete(0, tk.END)
        self.stock.delete(0, tk.END)

    def cargar_productos(self):

        for fila in self.tabla.get_children():
            self.tabla.delete(fila)

        productos = self.servicio.listar_productos()

        for producto in productos:

            self.tabla.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    producto.precio,
                    producto.stock
                )
            )

    def registrar_producto(self):

        try:

            self.servicio.registrar_producto(
                self.codigo.get(),
                self.nombre.get(),
                self.categoria.get(),
                self.precio.get(),
                self.stock.get()
            )

            self.cargar_productos()
            self.limpiar_campos()

            messagebox.showinfo(
                "Éxito",
                "Producto registrado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def actualizar_producto(self):

        try:

            self.servicio.actualizar_producto(
                self.codigo.get(),
                self.nombre.get(),
                self.categoria.get(),
                self.precio.get(),
                self.stock.get()
            )

            self.cargar_productos()

            messagebox.showinfo(
                "Éxito",
                "Producto actualizado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def eliminar_producto(self):

        try:

            self.servicio.eliminar_producto(
                self.codigo.get()
            )

            self.cargar_productos()
            self.limpiar_campos()

            messagebox.showinfo(
                "Éxito",
                "Producto eliminado correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def consultar_producto(self):

        codigo = self.buscar_codigo.get()

        producto = self.servicio.buscar_producto(
            codigo
        )

        if producto is None:

            messagebox.showerror(
                "Error",
                "Producto no encontrado"
            )

            return

        self.limpiar_campos()

        self.codigo.insert(
            0,
            producto.codigo
        )

        self.nombre.insert(
            0,
            producto.nombre
        )

        self.categoria.insert(
            0,
            producto.categoria
        )

        self.precio.insert(
            0,
            producto.precio
        )

        self.stock.insert(
            0,
            producto.stock
        )

    def seleccionar_producto(self, event):

        seleccion = self.tabla.selection()

        if not seleccion:
            return

        valores = self.tabla.item(
            seleccion[0]
        )["values"]

        self.limpiar_campos()

        self.codigo.insert(0, valores[0])
        self.nombre.insert(0, valores[1])
        self.categoria.insert(0, valores[2])
        self.precio.insert(0, valores[3])
        self.stock.insert(0, valores[4])

    def mostrar_usuarios(self):

        ventana = tk.Toplevel(self.root)

        ventana.title("Usuarios")
        ventana.geometry("600x400")

        tk.Label(
            ventana,
            text="Rol"
        ).pack(pady=5)

        self.combo_rol = ttk.Combobox(
            ventana,
            state="readonly"
        )

        self.combo_rol["values"] = (
            "Administrador",
            "Cajero",
            "Supervisor"
        )

        self.combo_rol.pack(pady=5)

        self.combo_rol.bind(
            "<<ComboboxSelected>>",
            self.cambio_rol
        )

        tabla = ttk.Treeview(
            ventana,
            columns=(
                "id",
                "nombre"
            ),
            show="headings"
        )

        tabla.heading(
            "id",
            text="Identificación"
        )

        tabla.heading(
            "nombre",
            text="Nombre"
        )

        tabla.pack(
            fill="both",
            expand=True
        )

        tabla.bind(
            "<<TreeviewSelect>>",
            self.seleccionar_usuario
        )

        self.tabla_usuarios = tabla

        for usuario in self.servicio.listar_usuarios():
            tabla.insert(
                "",
                tk.END,
                values=(
                    usuario.identificacion,
                    usuario.nombre
                )
            )
    def mostrar_ventas(self):

        ventana = tk.Toplevel(self.root)

        ventana.title("Ventas")

        ventana.geometry("800x500")

        frame_form = tk.LabelFrame(
            ventana,
            text="Registrar Venta"
        )

        frame_form.pack(
            fill="x",
            padx=10,
            pady=10
        )

        tk.Label(
            frame_form,
            text="Usuario"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )

        self.combo_usuario = ttk.Combobox(
            frame_form,
            state="readonly"
        )

        self.combo_usuario.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        usuarios = self.servicio.listar_usuarios()

        self.combo_usuario["values"] = [
            usuario.identificacion
            for usuario in usuarios
        ]

        tk.Label(
            frame_form,
            text="Producto"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5
        )

        self.combo_producto_venta = ttk.Combobox(
            frame_form,
            state="readonly"
        )

        self.combo_producto_venta.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        productos = self.servicio.listar_productos()

        self.combo_producto_venta["values"] = [
            producto.codigo
            for producto in productos
        ]

        tk.Label(
            frame_form,
            text="Cantidad"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5
        )

        self.entry_cantidad = tk.Entry(
            frame_form
        )

        self.entry_cantidad.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        tabla_ventas = ttk.Treeview(
            ventana,
            columns=(
                "usuario",
                "producto",
                "cantidad",
                "fecha"
            ),
            show="headings"
        )

        tabla_ventas.heading(
            "usuario",
            text="Usuario"
        )

        tabla_ventas.heading(
            "producto",
            text="Producto"
        )

        tabla_ventas.heading(
            "cantidad",
            text="Cantidad"
        )

        tabla_ventas.heading(
            "fecha",
            text="Fecha"
        )

        tabla_ventas.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        tk.Button(
            frame_form,
            text="Registrar Venta",
            bg="green",
            fg="white",
            command=lambda: self.registrar_venta(
                tabla_ventas
            )
        ).grid(
            row=3,
            column=0,
            columnspan=2,
            pady=10
        )

        self.cargar_ventas(
            tabla_ventas
        )

    def mostrar_productos(self):

        ventana = tk.Toplevel(self.root)

        ventana.title("Productos")

        ventana.geometry("700x300")

        tabla = ttk.Treeview(
            ventana,
            columns=(
                "codigo",
                "nombre",
                "categoria",
                "precio",
                "stock"
            ),
            show="headings"
        )

        tabla.heading("codigo", text="Código")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("categoria", text="Categoría")
        tabla.heading("precio", text="Precio")
        tabla.heading("stock", text="Stock")

        tabla.pack(
            fill="both",
            expand=True
        )

        for producto in self.servicio.listar_productos():
            tabla.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    producto.precio,
                    producto.stock
                )
            )

    def cargar_ventas(self, tabla):

        for fila in tabla.get_children():
            tabla.delete(fila)

        ventas = self.servicio.listar_ventas()

        for venta in ventas:
            tabla.insert(
                "",
                tk.END,
                values=(
                    venta.usuario_id,
                    venta.producto_codigo,
                    venta.cantidad,
                    venta.fecha
                )
            )

    def registrar_venta(
            self,
            tabla_ventas
    ):

        try:

            usuario = self.combo_usuario.get()

            producto = self.combo_producto_venta.get()

            cantidad = int(
                self.entry_cantidad.get()
            )

            self.servicio.registrar_venta(
                usuario,
                producto,
                cantidad
            )

            self.cargar_ventas(
                tabla_ventas
            )

            self.cargar_productos()

            self.entry_cantidad.delete(
                0,
                tk.END
            )

            messagebox.showinfo(
                "Éxito",
                "Venta registrada correctamente"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def cambio_rol(self, event):

        rol = self.combo_rol.get()

        messagebox.showinfo(
            "Rol seleccionado",
            rol
        )

    def evento_enter(self, event):

        messagebox.showinfo(
            "Evento",
            "ENTER presionado"
        )

    def evento_escape(self, event):

        try:

            self.limpiar_campos()

            if hasattr(
                    self,
                    "tabla_usuarios"
            ):
                self.tabla_usuarios.selection_remove(
                    self.tabla_usuarios.selection()
                )

        except:
            pass

    def seleccionar_usuario(self, event):

        seleccion = event.widget.selection()

        if not seleccion:
            return

        identificacion = event.widget.item(
            seleccion[0]
        )["values"][0]

        usuario = self.servicio.buscar_usuario(
            str(identificacion)
        )

        if usuario:
            messagebox.showinfo(
                "Usuario seleccionado",
                f"ID: {usuario.identificacion}\n"
                f"Nombre: {usuario.nombre}"
            )