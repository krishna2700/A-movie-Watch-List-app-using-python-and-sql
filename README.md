# Aplicación de Lista de Películas para Ver

Una aplicación de línea de comandos desarrollada en Python y SQLite para gestionar tu lista de películas pendientes por ver.

## Descripción

Esta aplicación te permite llevar un registro de películas que deseas ver, marcar películas como vistas, y buscar películas en tu lista. Utiliza SQLite como base de datos para almacenar la información de películas, usuarios y el historial de visualización.

## Características

- **Agregar nuevas películas**: Registra películas con su título y fecha de estreno
- **Ver películas próximas**: Muestra películas cuya fecha de estreno aún no ha llegado
- **Ver todas las películas**: Lista completa de todas las películas registradas
- **Marcar películas como vistas**: Los usuarios pueden registrar las películas que han visto
- **Ver películas vistas**: Consulta el historial de películas vistas por usuario
- **Gestión de usuarios**: Agregar usuarios a la aplicación
- **Buscar películas**: Busca películas por título (búsqueda parcial)

## Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal
- **SQLite3**: Base de datos para almacenamiento persistente
- **datetime**: Manejo de fechas y timestamps

## Estructura de la Base de Datos

La aplicación utiliza tres tablas principales:

### Tabla `movies`
- `id`: Identificador único (clave primaria)
- `title`: Título de la película
- `release_timestamp`: Fecha de estreno en formato timestamp

### Tabla `users`
- `username`: Nombre de usuario (clave primaria)

### Tabla `watched`
- `user_username`: Referencia al usuario (clave foránea)
- `movie_id`: Referencia a la película (clave foránea)

## Requisitos

- Python 3.8 o superior
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd <nombre-del-directorio>
```

2. No se requieren dependencias adicionales ya que el proyecto utiliza solo bibliotecas estándar de Python.

## Uso

Ejecuta la aplicación con el siguiente comando:

```bash
python app.py
```

### Menú Principal

Al iniciar la aplicación, verás el siguiente menú:

```
Please select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Add watched movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Exit.
```

### Ejemplos de Uso

1. **Agregar una película nueva**:
   - Selecciona la opción `1`
   - Ingresa el título de la película
   - Ingresa la fecha de estreno en formato `dd-mm-YYYY` (o presiona Enter para usar la fecha actual)

2. **Agregar un usuario**:
   - Selecciona la opción `6`
   - Ingresa el nombre de usuario

3. **Marcar una película como vista**:
   - Selecciona la opción `4`
   - Ingresa el nombre de usuario
   - Ingresa el ID de la película

4. **Buscar una película**:
   - Selecciona la opción `7`
   - Ingresa parte del título de la película

## Archivos del Proyecto

- `app.py`: Archivo principal con la interfaz de usuario y lógica de la aplicación
- `database.py`: Módulo de gestión de base de datos con todas las operaciones SQL
- `data.db`: Base de datos SQLite (se crea automáticamente al ejecutar la app)

## Características Técnicas

- Índice en la columna `release_timestamp` para optimizar consultas de películas próximas
- Uso de context managers para gestión segura de conexiones a la base de datos
- Validación de fechas con formato específico `dd-mm-YYYY`
- Búsqueda de películas con LIKE para coincidencias parciales

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.