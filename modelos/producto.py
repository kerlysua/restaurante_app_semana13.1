class Producto:
    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> None:

        self.codigo = self._validar_texto(
            codigo,
            "El código no puede estar vacío"
        )

        self.nombre = self._validar_texto(
            nombre,
            "El nombre no puede estar vacío"
        )

        self.categoria = self._validar_texto(
            categoria,
            "La categoría no puede estar vacía"
        )
        self.precio = self._validar_precio(precio)
        self.stock = self._validar_stock(stock)

    def _validar_texto(self, valor: str, mensaje: str) -> str:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError(mensaje)

        return valor.strip()

    def _validar_precio(self, precio: float) -> float:
        try:
            precio = float(precio)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número")

        if precio < 0:
            raise ValueError("El precio no puede ser negativo")

        return precio

    def _validar_stock(self, stock: int) -> int:
        try:
            stock = int(stock)
        except (TypeError, ValueError):
            raise ValueError("El stock debe ser un número entero")
        if stock < 0:
            raise ValueError("El stock no puede ser negativo")

        return stock

    def vender(self, cantidad: int) -> bool:
        if cantidad <= 0:
            return False

        if cantidad > self.stock:
            return False

        self.stock -= cantidad
        return True

    def convertir_a_diccionario(self) -> dict:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock
        }
    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            datos["codigo"],
            datos["nombre"],
            datos["categoria"],
            datos["precio"],
            datos["stock"]
        )

    def mostrar_informacion(self) -> str:
        return (
            f"Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )