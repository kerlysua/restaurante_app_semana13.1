from datetime import datetime


class Venta:

    def __init__(
            self,
            usuario_id,
            producto_codigo,
            cantidad,
            fecha=None
    ):

        self.usuario_id = usuario_id
        self.producto_codigo = producto_codigo
        self.cantidad = int(cantidad)

        if fecha is None:

            self.fecha = (
                datetime.now()
                .strftime("%Y-%m-%d %H:%M:%S")
            )

        else:

            self.fecha = fecha

    def convertir_a_diccionario(self):

        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha
        }

    @classmethod
    def desde_diccionario(
            cls,
            datos
    ):

        return cls(
            datos["usuario_id"],
            datos["producto_codigo"],
            datos["cantidad"],
            datos.get("fecha")
        )

    def __str__(self):

        return (
            f"Usuario: {self.usuario_id} | "
            f"Producto: {self.producto_codigo} | "
            f"Cantidad: {self.cantidad} | "
            f"Fecha: {self.fecha}"
        )