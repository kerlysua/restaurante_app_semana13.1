from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):
        self.archivo_servicio = ArchivoServicio()
        self._productos = []
        self._usuarios = []

        self.cargar_datos()

    def cargar_datos(self):

        datos_productos = (
            self.archivo_servicio.cargar_productos()
        )

        for datos in datos_productos:
            self._productos.append(
                Producto.desde_diccionario(datos)
            )

        datos_usuarios = (
            self.archivo_servicio.cargar_usuarios()
        )

        for datos in datos_usuarios:
            self._usuarios.append(
                Usuario.desde_diccionario(datos)
            )

    def validar_acceso(
            self,
            nombre,
            contrasena
    ):

        nombre = nombre.strip()
        contrasena = contrasena.strip()

        for usuario in self._usuarios:

            if (
                    usuario.nombre.lower() ==
                    nombre.lower()
                    and
                    usuario.contrasena ==
                    contrasena
            ):
                return True

        return False

    def listar_productos(self):
        return self._productos

    def listar_usuarios(self):
        return self._usuarios

    def buscar_producto(self, codigo):

        codigo = str(codigo).strip()

        for producto in self._productos:

            if str(producto.codigo).strip() == codigo:
                return producto

        return None

    def registrar_producto(
            self,
            codigo,
            nombre,
            categoria,
            precio,
            stock
    ):

        if self.buscar_producto(codigo):
            raise ValueError(
                "Ya existe un producto con ese código"
            )

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self._productos.append(producto)

        self.archivo_servicio.guardar_productos(
            self._productos
        )

    def actualizar_producto(
            self,
            codigo,
            nombre,
            categoria,
            precio,
            stock
    ):

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado"
            )

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = float(precio)
        producto.stock = int(stock)

        self.archivo_servicio.guardar_productos(
            self._productos
        )

    def eliminar_producto(self, codigo):

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "Producto no encontrado"
            )

        self._productos.remove(producto)

        self.archivo_servicio.guardar_productos(
            self._productos
        )