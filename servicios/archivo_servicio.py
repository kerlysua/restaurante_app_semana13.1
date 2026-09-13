import json
import os


class ArchivoServicio:

    def __init__(self) -> None:

        carpeta_base = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__))
        )

        self.ruta_productos = os.path.join(
            carpeta_base,
            "datos",
            "productos.json"
        )

        self.ruta_usuarios = os.path.join(
            carpeta_base,
            "datos",
            "usuarios.json"
        )

        self.ruta_ventas = os.path.join(
            carpeta_base,
            "datos",
            "ventas.json"
        )

        os.makedirs(
            os.path.join(carpeta_base, "datos"),
            exist_ok=True
        )

    def guardar_productos(self, productos: list) -> None:
        datos = []

        for producto in productos:
            datos.append(
                producto.convertir_a_diccionario()
            )

        self._guardar_json(
            self.ruta_productos,
            datos
        )

    def cargar_productos(self) -> list:
        return self._cargar_json(
            self.ruta_productos
        )

    def guardar_usuarios(self, usuarios: list) -> None:
        datos = []

        for usuario in usuarios:
            datos.append(
                usuario.convertir_a_diccionario()
            )

        self._guardar_json(
            self.ruta_usuarios,
            datos
        )

    def cargar_usuarios(self) -> list:
        return self._cargar_json(
            self.ruta_usuarios
        )

    def guardar_ventas(self, ventas: list) -> None:
        datos = []

        for venta in ventas:
            datos.append(
                venta.convertir_a_diccionario()
            )

        self._guardar_json(
            self.ruta_ventas,
            datos
        )

    def cargar_ventas(self) -> list:
        return self._cargar_json(
            self.ruta_ventas
        )

    def _guardar_json(
        self,
        ruta: str,
        datos: list
    ) -> None:
        try:
            with open(
                ruta,
                "w",
                encoding="utf-8"
            ) as archivo:

                json.dump(
                    datos,
                    archivo,
                    ensure_ascii=False,
                    indent=4
                )

        except PermissionError:
            print("Error: no tiene permisos para guardar el archivo.")

    def _cargar_json(
        self,
        ruta: str
    ) -> list:

        try:
            with open(
                ruta,
                "r",
                encoding="utf-8"
            ) as archivo:

                return json.load(archivo)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                f"Error: el archivo {ruta} contiene JSON inválido."
            )
            return []

        except PermissionError:
            print(
                f"Error: no tiene permisos para leer {ruta}."
            )
            return []