# Aplicación de Lista de Películas por Ver

Una aplicación de línea de comandos para administrar tu lista de películas por ver, desarrollada con Python y SQLite.

## Características

- **Gestión de películas**: Añade películas con sus fechas de lanzamiento
- **Seguimiento de próximos estrenos**: Visualiza las películas que se estrenarán en el futuro
- **Gestión de usuarios**: Crea múltiples usuarios para seguir individualmente las películas vistas
- **Seguimiento de películas vistas**: Marca películas como vistas y consulta tu historial
- **Búsqueda**: Busca películas por título
- **Almacenamiento persistente**: Todos los datos se almacenan en una base de datos SQLite

## Requisitos Previos

- Python 3.8 o superior
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd A-movie-Watch-List-app-using-python-and-sql
```

2. No se requieren dependencias externas. La aplicación utiliza únicamente la biblioteca estándar de Python.

## Uso

Ejecuta la aplicación desde la línea de comandos:

```bash
python app.py
```

### Menú Principal

La aplicación ofrece las siguientes opciones:

1. **Añadir nueva película**: Ingresa el título y la fecha de lanzamiento (formato: dd-mm-AAAA)
2. **Ver próximos estrenos**: Muestra todas las películas cuya fecha de lanzamiento es futura
3. **Ver todas las películas**: Muestra todas las películas en la base de datos
4. **Marcar película como vista**: Registra que un usuario ha visto una película específica
5. **Ver películas vistas**: Muestra todas las películas que un usuario ha visto
6. **Añadir usuario**: Crea un nuevo perfil de usuario
7. **Buscar película**: Busca películas por título parcial
8. **Salir**: Cierra la aplicación

## Estructura de la Base de Datos

La aplicación utiliza tres tablas principales:

- **movies**: Almacena información de películas (id, título, timestamp de lanzamiento)
- **users**: Almacena nombres de usuario
- **watched**: Tabla de relación que asocia usuarios con las películas que han visto

## Estructura de Archivos

- `app.py`: Archivo principal de la aplicación con la interfaz de usuario
- `database.py`: Funciones de gestión de base de datos y consultas SQL
- `data.db`: Archivo de base de datos SQLite (creado en la primera ejecución)

## Ejemplo de Uso

```
¡Bienvenido a la aplicación de lista de películas!

1. Añade un nuevo usuario (opción 6)
2. Añade películas a tu lista (opción 1)
3. Marca películas como vistas (opción 4)
4. Visualiza tus películas vistas (opción 5)
5. Busca películas específicas (opción 7)
```

## Licencia

Este proyecto es de código abierto y está disponible bajo la Licencia MIT.
