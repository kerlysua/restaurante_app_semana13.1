from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
from servicios.archivo_servicio import ArchivoServicio


class Restaurante:

    def __init__(self):

        self.archivo_servicio = ArchivoServicio()

        # Colecciones principales
        self._productos = []
        self._usuarios = []
        self._ventas = []

        # Índices
        self._productos_por_codigo = {}
        self._usuarios_por_id = {}
        self._ventas_por_usuario = {}

        self.cargar_datos()

    # ========================================
    # CARGA DE DATOS
    # ========================================

    def cargar_datos(self):

        self._productos.clear()
        self._usuarios.clear()
        self._ventas.clear()

        self._productos_por_codigo.clear()
        self._usuarios_por_id.clear()
        self._ventas_por_usuario.clear()

        # PRODUCTOS

        datos_productos = (
            self.archivo_servicio.cargar_productos()
        )

        for datos in datos_productos:

            producto = Producto.desde_diccionario(
                datos
            )

            self._productos.append(producto)

            self._productos_por_codigo[
                producto.codigo
            ] = producto

        # USUARIOS

        datos_usuarios = (
            self.archivo_servicio.cargar_usuarios()
        )

        for datos in datos_usuarios:

            usuario = Usuario.desde_diccionario(
                datos
            )

            self._usuarios.append(usuario)

            self._usuarios_por_id[
                usuario.identificacion
            ] = usuario

        # VENTAS

        datos_ventas = (
            self.archivo_servicio.cargar_ventas()
        )

        for datos in datos_ventas:

            venta = Venta.desde_diccionario(
                datos
            )

            self._ventas.append(venta)

            if (
                venta.usuario_id
                not in self._ventas_por_usuario
            ):

                self._ventas_por_usuario[
                    venta.usuario_id
                ] = []

            self._ventas_por_usuario[
                venta.usuario_id
            ].append(venta)

    # ========================================
    # USUARIOS
    # ========================================

    def registrar_usuario(
        self,
        identificacion,
        nombre,
        contrasena
    ):

        if identificacion in self._usuarios_por_id:

            raise ValueError(
                "El usuario ya existe"
            )

        usuario = Usuario(
            identificacion,
            nombre,
            contrasena
        )

        self._usuarios.append(usuario)

        self._usuarios_por_id[
            identificacion
        ] = usuario

        self.archivo_servicio.guardar_usuarios(
            self._usuarios
        )

    def buscar_usuario(
        self,
        identificacion
    ):

        return self._usuarios_por_id.get(
            identificacion
        )

    def listar_usuarios(self):

        return self._usuarios

    # ========================================
    # PRODUCTOS
    # ========================================

    def registrar_producto(
        self,
        codigo,
        nombre,
        categoria,
        precio,
        stock
    ):

        if codigo in self._productos_por_codigo:

            raise ValueError(
                "El producto ya existe"
            )

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self._productos.append(producto)

        self._productos_por_codigo[
            codigo
        ] = producto

        self.archivo_servicio.guardar_productos(
            self._productos
        )

    def buscar_producto(
        self,
        codigo
    ):

        return self._productos_por_codigo.get(
            codigo
        )

    def actualizar_producto(
            self,
            codigo,
            nombre,
            categoria,
            precio,
            stock
    ):

        producto = self.buscar_producto(
            codigo
        )

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

    def listar_productos(self):

        return self._productos

    def eliminar_producto(
        self,
        codigo
    ):

        producto = self.buscar_producto(
            codigo
        )

        if producto is None:

            raise ValueError(
                "Producto no encontrado"
            )

        self._productos.remove(producto)

        del self._productos_por_codigo[
            codigo
        ]

        self.archivo_servicio.guardar_productos(
            self._productos
        )

    # ========================================
    # VENTAS
    # ========================================

    def registrar_venta(
            self,
            usuario_id,
            producto_codigo,
            cantidad
    ):
        usuario = self.buscar_usuario(
            usuario_id
        )

        if usuario is None:
            raise ValueError(
                "Usuario no existe"
            )

        producto = self.buscar_producto(
            producto_codigo
        )

        if producto is None:
            raise ValueError(
                "Producto no existe"
            )

        if cantidad <= 0:
            raise ValueError(
                "La cantidad debe ser mayor que cero"
            )

        if cantidad > producto.stock:
            raise ValueError(
                "Stock insuficiente"
            )

        producto.stock -= cantidad

        venta = Venta(
            usuario_id,
            producto_codigo,
            cantidad
        )

        self._ventas.append(
            venta
        )

        if (
                usuario_id
                not in self._ventas_por_usuario
        ):
            self._ventas_por_usuario[
                usuario_id
            ] = []

        self._ventas_por_usuario[
            usuario_id
        ].append(venta)

        self.archivo_servicio.guardar_ventas(
            self._ventas
        )

        self.archivo_servicio.guardar_productos(
            self._productos
        )

    def listar_ventas(self):
        return self._ventas

    def obtener_ventas_usuario(
        self,
        usuario_id
    ):

        return self._ventas_por_usuario.get(
            usuario_id,
            []
        )

    # ========================================
    # LOGIN
    # ========================================

    def validar_acceso(
        self,
        nombre,
        contrasena
    ):

        for usuario in self._usuarios:

            if (
                usuario.nombre.lower()
                ==
                nombre.lower()
                and
                usuario.contrasena
                ==
                contrasena
            ):
                return True

        return False