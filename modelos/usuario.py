class Usuario:
    def __init__(self, identificacion: str, nombre: str, contrasena: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.contrasena = contrasena

    def convertir_a_diccionario(self) -> dict:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "contrasena": self.contrasena
        }

    @classmethod
    def desde_diccionario(cls, datos: dict):
        return cls(
            identificacion=datos.get("identificacion"),
            nombre=datos.get("nombre"),
            contrasena=datos.get("contrasena")
        )

    def mostrar_informacion(self):
        return f"ID: {self.identificacion} | Nombre: {self.nombre}"