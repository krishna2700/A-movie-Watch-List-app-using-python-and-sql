# Aplicación de Lista de Películas para Ver

Una aplicación de línea de comandos desarrollada en Python para administrar tu lista personal de películas que deseas ver. Rastrea películas, marca cuáles has visto y busca en tu colección usando SQLite como base de datos.

## Características

- ✨ **Agregar películas nuevas** con título y fecha de estreno
- 📅 **Ver películas próximas** que aún no se han estrenado
- 📋 **Ver todas las películas** en tu lista de seguimiento
- ✅ **Marcar películas como vistas** por usuario
- 👥 **Sistema de gestión de usuarios** para rastrear qué películas ha visto cada persona
- 🔍 **Búsqueda de películas** por título parcial
- 💾 **Almacenamiento persistente** usando SQLite

## Requisitos Previos

- Python 3.8 o superior
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd A-movie-Watch-List-app-using-python-and-sql
```

2. No se requieren dependencias externas. La aplicación utiliza únicamente bibliotecas estándar de Python.

## Uso

Ejecuta la aplicación desde la línea de comandos:

```bash
python app.py
```

### Opciones del Menú

Al iniciar la aplicación, verás las siguientes opciones:

1. **Agregar nueva película** - Añade una película con su título y fecha de estreno
2. **Ver películas próximas** - Muestra películas con fecha de estreno futura
3. **Ver todas las películas** - Lista todas las películas en la base de datos
4. **Agregar película vista** - Marca una película como vista por un usuario
5. **Ver películas vistas** - Muestra todas las películas que un usuario ha visto
6. **Agregar usuario a la aplicación** - Crea un nuevo usuario
7. **Buscar una película** - Busca películas por título parcial
8. **Salir** - Cierra la aplicación

### Ejemplo de Flujo de Trabajo

```
1. Agregar un usuario: "Juan"
2. Agregar una película: "Matrix" (23-03-1999)
3. Marcar la película como vista por Juan
4. Ver las películas vistas de Juan
```

## Estructura del Proyecto

- `app.py` - Archivo principal de la aplicación con la interfaz de usuario del menú
- `database.py` - Funciones de gestión de base de datos y consultas SQL
- `data.db` - Archivo de base de datos SQLite (se crea automáticamente)

## Esquema de Base de Datos

### Tabla `movies`
- `id` (INTEGER PRIMARY KEY) - Identificador único de la película
- `title` (TEXT) - Título de la película
- `release_timestamp` (REAL) - Fecha de estreno en formato timestamp

### Tabla `users`
- `username` (TEXT PRIMARY KEY) - Nombre de usuario único

### Tabla `watched`
- `user_username` (TEXT) - Referencia al usuario
- `movie_id` (INTEGER) - Referencia a la película
- Relación muchos-a-muchos entre usuarios y películas

## Características Técnicas

- Uso de **context managers** para manejo seguro de conexiones a la base de datos
- **Índices de base de datos** para consultas optimizadas
- **Claves foráneas** para mantener la integridad referencial
- Manejo de fechas usando el módulo `datetime` de Python
- Formato de entrada de fecha: `dd-mm-YYYY`

## Formato de Fecha

Al agregar películas, usa el formato: `dd-mm-YYYY`

Ejemplo: `23-03-2024` para el 23 de marzo de 2024

Si dejas el campo de fecha vacío, se usará la fecha actual.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, sigue estos pasos:

1. Haz un fork del proyecto
2. Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Haz push a la rama (`git push origin feature/nueva-caracteristica`)
5. Abre un Pull Request

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia correspondiente.

## Autor

Desarrollado como un proyecto de demostración de aplicaciones Python con bases de datos SQLite.

---

**Nota**: Esta aplicación está diseñada para uso educativo y demostrativo de conceptos de bases de datos relacionales con Python.
