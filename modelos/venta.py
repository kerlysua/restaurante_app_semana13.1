class Venta:
    def __init__(
            self,
            usuario_id: str,
            producto_codigo: str,
            cantidad: int
    ) -> None:

        if not usuario_id.strip():
            raise ValueError("La identificación del usuario no puede estar vacía")

        if not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío")

        try:
            cantidad = int(cantidad)
        except (TypeError, ValueError):
            raise ValueError("La cantidad debe ser un número entero")

        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")

        self.usuario_id = usuario_id.strip()
        self.producto_codigo = producto_codigo.strip()
        self.cantidad = cantidad

    def convertir_a_diccionario(self) -> dict:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            datos["usuario_id"],
            datos["producto_codigo"],
            datos["cantidad"]
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad}"
        )

    def __str__(self) -> str:
        return self.mostrar_informacion()

