class Usuario:
    def __init__(self, identificacion: str, nombre: str, contrasena: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.contrasena = contrasena

    @classmethod
    def desde_diccionario(cls, datos: dict) -> "Usuario":
        return cls(
            identificacion=datos.get("identificacion"),
            nombre=datos.get("nombre"),
            contrasena=datos.get("contrasena")  # ahora sí se carga la contraseña
        )

    def mostrar_informacion(self) -> str:
        return f"ID: {self.identificacion} | Nombre: {self.nombre}"
