# Aplicación de Lista de Películas para Ver usando Python y SQL

Una aplicación de línea de comandos para gestionar tu lista de películas para ver, construida con Python y SQLite.

## Descripción

Esta aplicación te permite realizar un seguimiento de las películas que deseas ver, marcar las películas que ya has visto y gestionar múltiples usuarios. Utiliza SQLite para el almacenamiento persistente de datos y proporciona una interfaz de menú simple e intuitiva.

## Características

- ✨ **Agregar nuevas películas** con título y fecha de estreno
- 📅 **Ver películas próximas** que aún no se han estrenado
- 📋 **Ver todas las películas** en tu lista de seguimiento
- ✅ **Marcar películas como vistas** por usuario
- 👤 **Gestión de múltiples usuarios**
- 🔍 **Buscar películas** por título parcial
- 💾 **Almacenamiento persistente** usando SQLite

## Requisitos

- Python 3.8 o superior
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio:
```bash
git clone <url-del-repositorio>
cd <directorio-del-proyecto>
```

2. No se requieren dependencias externas, ya que el proyecto utiliza solo bibliotecas estándar de Python.

## Uso

Ejecuta la aplicación:

```bash
python app.py
```

### Opciones del Menú

Al iniciar la aplicación, verás el siguiente menú:

```
Por favor, selecciona una de las siguientes opciones:
1) Agregar nueva película.
2) Ver películas próximas.
3) Ver todas las películas
4) Agregar película vista
5) Ver películas vistas.
6) Agregar usuario a la aplicación.
7) Buscar una película.
8) Salir.
```

### Ejemplos de Uso

#### Agregar una Nueva Película
1. Selecciona la opción `1`
2. Ingresa el título de la película
3. Ingresa la fecha de estreno en formato `dd-mm-YYYY` (o presiona Enter para usar la fecha actual)

#### Ver Películas Próximas
- Selecciona la opción `2` para ver todas las películas con fechas de estreno futuras

#### Marcar una Película como Vista
1. Selecciona la opción `4`
2. Ingresa tu nombre de usuario
3. Ingresa el ID de la película (obtenido de la lista de películas)

#### Buscar Películas
1. Selecciona la opción `7`
2. Ingresa un término de búsqueda parcial (por ejemplo, "Matrix" encontrará "The Matrix")

## Estructura del Proyecto

```
.
├── app.py          # Aplicación principal con interfaz de menú
├── database.py     # Funciones de base de datos y consultas SQL
├── data.db         # Archivo de base de datos SQLite (creado automáticamente)
└── README.md       # Este archivo
```

## Esquema de Base de Datos

### Tabla `movies`
- `id` (INTEGER PRIMARY KEY): Identificador único de la película
- `title` (TEXT): Título de la película
- `release_timestamp` (REAL): Fecha de estreno como timestamp Unix

### Tabla `users`
- `username` (TEXT PRIMARY KEY): Nombre de usuario único

### Tabla `watched`
- `user_username` (TEXT): Referencia al usuario
- `movie_id` (INTEGER): Referencia a la película
- Claves foráneas para mantener la integridad referencial

## Características Técnicas

- **Gestión de contexto**: Utiliza declaraciones `with` para el manejo seguro de conexiones a la base de datos
- **Índices**: Incluye un índice en `release_timestamp` para consultas eficientes
- **Validación de fechas**: Manejo robusto de fechas usando el módulo `datetime` de Python
- **Búsqueda**: Implementa búsqueda de texto parcial usando el operador SQL `LIKE`

## Contribuir

Las contribuciones son bienvenidas. Por favor, siéntete libre de enviar un Pull Request.

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## Autor

Creado como proyecto de demostración para aprender Python y SQLite.

## Soporte

Si encuentras algún problema o tienes sugerencias, por favor abre un issue en el repositorio del proyecto.
