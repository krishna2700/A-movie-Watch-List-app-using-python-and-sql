# Aplicación de Lista de Películas para Ver usando Python y SQL

Una aplicación de consola interactiva para gestionar tu lista personal de películas pendientes, construida con Python y SQLite.

## Características

- **Gestión de Películas**: Añade nuevas películas con fechas de estreno
- **Vista de Próximos Estrenos**: Consulta las películas que se estrenarán en el futuro
- **Seguimiento de Vistas**: Marca películas como vistas y lleva un registro de tus visualizaciones
- **Gestión de Usuarios**: Sistema multi-usuario para varios usuarios
- **Búsqueda de Películas**: Busca películas por título usando búsqueda parcial
- **Almacenamiento en Base de Datos**: Almacenamiento persistente usando SQLite

## Requisitos

- Python 3.8 o superior
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd A-movie-Watch-List-app-using-python-and-sql
```

2. No se requieren dependencias externas ya que el proyecto utiliza solo bibliotecas estándar de Python.

## Uso

Ejecuta la aplicación:

```bash
python app.py
```

### Opciones del Menú

1. **Añadir nueva película**: Añade una película con su título y fecha de estreno
2. **Ver próximos estrenos**: Muestra las películas que se estrenarán en el futuro
3. **Ver todas las películas**: Lista todas las películas en la base de datos
4. **Añadir película vista**: Marca una película como vista por un usuario
5. **Ver películas vistas**: Muestra todas las películas vistas por un usuario específico
6. **Añadir usuario a la app**: Registra un nuevo usuario en el sistema
7. **Buscar una película**: Busca películas por título parcial
8. **Salir**: Cierra la aplicación

## Estructura de la Base de Datos

La aplicación utiliza SQLite con tres tablas principales:

### Tabla `movies`
- `id`: Clave primaria (INTEGER)
- `title`: Título de la película (TEXT)
- `release_timestamp`: Fecha de estreno en formato timestamp (REAL)

### Tabla `users`
- `username`: Nombre de usuario (TEXT, clave primaria)

### Tabla `watched`
- `user_username`: Referencia al usuario (TEXT, clave foránea)
- `movie_id`: Referencia a la película (INTEGER, clave foránea)

## Archivos del Proyecto

- `app.py`: Archivo principal de la aplicación con la interfaz de usuario
- `database.py`: Módulo de gestión de base de datos con todas las operaciones SQL
- `data.db`: Archivo de base de datos SQLite (se crea automáticamente)

## Ejemplo de Uso

```
¡Bienvenido a la aplicación de lista de películas!

Por favor, selecciona una de las siguientes opciones:
1) Añadir nueva película.
2) Ver próximos estrenos.
3) Ver todas las películas
4) Añadir película vista
5) Ver películas vistas.
6) Añadir usuario a la app.
7) Buscar una película.
8) Salir.

Tu selección: 1
Título de la película: El Padrino
Fecha de estreno (dd-mm-AAAA): 24-03-1972
```

## Características Técnicas

- Utiliza el operador walrus (`:=`) de Python para entrada de bucle eficiente
- Implementa índices de base de datos para consultas optimizadas de fechas de estreno
- Gestores de contexto para operaciones seguras de base de datos
- Formato de fecha configurable (dd-mm-AAAA)
- Búsqueda con comodines SQL usando el operador LIKE

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Contribuciones

Las contribuciones, problemas y solicitudes de funcionalidades son bienvenidas.
