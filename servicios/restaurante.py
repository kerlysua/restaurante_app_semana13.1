from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class Restaurante:
    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

        self.cargar_datos()

    def cargar_datos(self) -> None:
        # Cargar productos desde JSON
        datos_productos = self.archivo_servicio.cargar_productos()
        for datos in datos_productos:
            try:
                producto = Producto.desde_diccionario(datos)
                self._productos.append(producto)
            except (KeyError, ValueError) as error:
                print(f"Error al cargar producto: {error}")

        # Cargar usuarios desde JSON
        datos_usuarios = self.archivo_servicio.cargar_usuarios()
        for datos in datos_usuarios:
            try:
                usuario = Usuario.desde_diccionario(datos)
                self._usuarios.append(usuario)
            except (KeyError, ValueError) as error:
                print(f"Error al cargar usuario: {error}")

    # =========================
    # OPERACIONES
    # =========================

    def validar_acceso(self, identificacion: str, contrasena: str) -> bool:
        """Valida si existe un usuario con la identificación y contraseña dadas."""
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion and usuario.contrasena == contrasena:
                return True
        return False

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios
