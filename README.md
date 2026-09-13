# NOMBRE DEL ESTUDIANTE
KERLY ALEXANDRA SUAREZ MALAVE

# Restaurante App - Semana 11

## Descripción

Este proyecto permite administrar productos, usuarios y ventas de un restaurante.

## Funcionalidades

- Registrar productos.
- Listar productos.
- Buscar productos.
- Registrar usuarios.
- Listar usuarios.
- Realizar ventas.
- Validar el stock disponible.
- Disminuir el stock después de una venta.
- Consultar ventas realizadas por un usuario.
- Guardar productos en JSON.
- Guardar usuarios en JSON.
- Guardar ventas en JSON.
- Recuperar la información al iniciar nuevamente el programa.
## Estructura

restaurante_app/
├── datos/
├── modelos/
├── servicios/
├── main.py
└── README.md

## Ejecución

Ejecutar el archivo:

python main.py

## 📂 Funcionalidades

- **[Productos] 
  - Registrar, listar, buscar, actualizar y eliminar productos.  
  - Persistencia en `productos.json`.  

- **[Usuarios] 
  - Registrar, listar, buscar, actualizar y eliminar usuarios.  
  - Persistencia en `usuarios.json`.  

- **[Ventas] 
  - Registrar ventas entre usuarios y productos.  
  - Consultar ventas de un usuario específico.  
  - Persistencia en `ventas.json`.
  Seleccione una opción: 1
Código del producto: P003
Nombre del producto: Ensalada
Stock inicial: 15
✅ Producto registrado correctamente.

Seleccione una opción: 4
Identificación del usuario: U003
Nombre del usuario: Kerly
✅ Usuario registrado correctamente.

Seleccione una opción: 6
Código del producto: P003
Identificación del usuario: U003
Cantidad: 2
✅ Venta registrada correctamente.
# RESTAURANTE APP - SEMANA 12
## 📌 Descripción
Este proyecto corresponde a la evolución de la aplicación **Restaurante App** desarrollada en la Semana 11.  
En la Semana 12 se aplicaron mejoras internas en el uso de colecciones para optimizar búsquedas, consultas y validaciones, manteniendo la arquitectura modular y la persistencia en JSON.

---

## 🔧 Mejoras aplicadas
- Conservación de las **listas principales** (`productos`, `usuarios`, `ventas`) para almacenar, recorrer y persistir objetos.
- Implementación de **índices con diccionarios**:
  - Productos por `codigo`.
  - Usuarios por `identificacion`.
- Creación de **índice de ventas por usuario** (`dict[str, list[Venta]]`) para consultas rápidas.
- Sincronización de índices al registrar productos, usuarios y ventas.
- Reconstrucción automática de índices al cargar información desde JSON.
- Validación de unicidad mediante claves únicas (códigos de producto y identificaciones de usuario).
- Uso opcional de `set` para validaciones de pertenencia o unicidad.
- Conservación de la lógica de negocio dentro de `servicios/restaurante.py`.  
- **Importante:** los modelos (`producto.py`, `usuario.py`, `venta.py`) se conservaron sin cambios, ya que cumplen su función y no requieren modificaciones para esta semana.
# Pruebas realizadas
Registrar producto

Se valida unicidad por código.

Ejemplo: P004 → Producto registrado correctamente.

Listar productos

Muestra todos los productos cargados desde JSON y los nuevos registrados.

Buscar producto

Búsqueda directa por código (dict), sin recorrer toda la lista.

Registrar usuario

Se valida unicidad por identificación.

Ejemplo: U004 → Usuario registrado correctamente.

Realizar venta
Se descuenta stock del producto.

Se guarda la venta en lista e índice de ventas por usuario.

Consultar ventas de un usuario

Recupera ventas directamente desde el índice (dict[str, list[Venta]]).

Persistencia y reconstrucción

Al cerrar y volver a ejecutar, los datos se cargan desde JSON y los índices se reconstruyen automáticamente.

# Conclusión
El proyecto conserva la arquitectura modular de la Semana 11 y aplica mejoras internas en el uso de colecciones para optimizar búsquedas, consultas y validaciones.
Se mantiene la persistencia en JSON, el control de stock y la relación Usuario–Producto mediante Venta.