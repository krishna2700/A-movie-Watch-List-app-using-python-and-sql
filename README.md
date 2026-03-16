# Aplicación de Lista de Películas por Ver — Python y SQL

Una aplicación de línea de comandos (CLI) construida con **Python** y **SQLite** que permite gestionar una lista personalizada de películas por ver. Los usuarios pueden agregar películas, registrar las que ya vieron, buscar títulos y más.

---

## Características

- **Agregar películas**: Registra nuevas películas con su título y fecha de estreno.
- **Ver películas próximas**: Muestra las películas cuya fecha de estreno es posterior a la fecha actual.
- **Ver todas las películas**: Lista completa de todas las películas registradas.
- **Marcar película como vista**: Asocia una película vista a un usuario específico.
- **Ver películas vistas**: Consulta las películas que un usuario ya ha visto.
- **Agregar usuarios**: Registra nuevos usuarios en la aplicación.
- **Buscar películas**: Busca películas por título parcial.

---

## Tecnologías Utilizadas

| Tecnología | Uso |
|---|---|
| **Python 3** | Lenguaje principal de la aplicación |
| **SQLite** | Base de datos relacional embebida |
| **sqlite3** | Módulo estándar de Python para interactuar con SQLite |
| **datetime** | Módulo estándar para el manejo de fechas |

---

## Estructura del Proyecto

```
├── app.py          # Punto de entrada principal y menú interactivo
├── database.py     # Capa de acceso a datos (consultas SQL y conexión a SQLite)
├── data.db         # Archivo de base de datos SQLite (se genera automáticamente)
└── README.md       # Documentación del proyecto
```

---

## Esquema de Base de Datos

La aplicación utiliza tres tablas:

### `movies`
| Columna             | Tipo    | Descripción                          |
|---------------------|---------|--------------------------------------|
| `id`                | INTEGER | Clave primaria (autoincremental)     |
| `title`             | TEXT    | Título de la película                |
| `release_timestamp` | REAL    | Fecha de estreno (timestamp UNIX)    |

### `users`
| Columna    | Tipo | Descripción                  |
|------------|------|------------------------------|
| `username` | TEXT | Nombre de usuario (clave primaria) |

### `watched`
| Columna         | Tipo    | Descripción                                      |
|-----------------|---------|--------------------------------------------------|
| `user_username` | TEXT    | Referencia al usuario (`users.username`)          |
| `movie_id`      | INTEGER | Referencia a la película (`movies.id`)            |

---

## Instalación y Ejecución

### Requisitos Previos

- **Python 3.6** o superior instalado en el sistema.
- No se requieren dependencias externas; todos los módulos utilizados son parte de la biblioteca estándar de Python.

### Pasos

1. **Clonar el repositorio:**

   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-directorio>
   ```

2. **Ejecutar la aplicación:**

   ```bash
   python app.py
   ```

---

## Uso

Al ejecutar la aplicación, se presenta un menú interactivo con las siguientes opciones:

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

Your selection:
```

### Ejemplos

- **Agregar una película:** Selecciona la opción `1`, ingresa el título y la fecha de estreno en formato `dd-mm-AAAA`. Si no se proporciona una fecha, se usa la fecha actual.
- **Ver películas próximas:** Selecciona la opción `2` para ver las películas con fecha de estreno futura.
- **Marcar como vista:** Primero agrega un usuario con la opción `6`, luego usa la opción `4` indicando el nombre de usuario y el ID de la película.
- **Buscar:** Selecciona la opción `7` e ingresa un término parcial del título para buscar coincidencias.

---

## Licencia

Este proyecto es de código abierto y está disponible para uso educativo y personal.
