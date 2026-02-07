# Aplicación de Lista de Películas para Ver usando Python y SQL

Una aplicación de consola interactiva para gestionar tu lista de películas para ver, construida con Python y SQLite.

## Características

- **Agregar nuevas películas**: Añade películas con título y fecha de lanzamiento
- **Ver películas próximas**: Muestra películas con fechas de lanzamiento futuras
- **Ver todas las películas**: Lista todas las películas en la base de datos
- **Marcar películas como vistas**: Registra qué usuarios han visto qué películas
- **Ver películas vistas**: Consulta las películas que ha visto un usuario
- **Gestión de usuarios**: Añade usuarios a la aplicación
- **Buscar películas**: Busca películas por título parcial

## Tecnologías Utilizadas

- **Python 3**: Lenguaje de programación principal
- **SQLite3**: Base de datos para almacenamiento persistente
- **Módulo datetime**: Manejo de fechas y marcas de tiempo

## Estructura de la Base de Datos

La aplicación utiliza tres tablas principales:

- `movies`: Almacena información de películas (id, título, fecha de lanzamiento)
- `users`: Gestiona cuentas de usuario (nombre de usuario)
- `watched`: Tabla de relación que vincula usuarios con películas vistas

## Cómo Usar

1. Ejecuta la aplicación:
```bash
python app.py
```

2. Selecciona una opción del menú (1-8):
   - **1**: Agregar nueva película
   - **2**: Ver películas próximas
   - **3**: Ver todas las películas
   - **4**: Agregar película vista
   - **5**: Ver películas vistas
   - **6**: Agregar usuario a la aplicación
   - **7**: Buscar una película
   - **8**: Salir

## Requisitos

- Python 3.8 o superior
- SQLite3 (incluido con Python)

## Instalación

1. Clona este repositorio
2. No se requieren dependencias adicionales
3. Ejecuta `python app.py` para comenzar

## Características de la Base de Datos

- Índice automático en fechas de lanzamiento para búsquedas optimizadas
- Claves foráneas para integridad referencial
- Creación automática de tablas en el primer inicio

## Formato de Fecha

Las fechas deben ingresarse en formato `dd-mm-YYYY` (por ejemplo, 25-12-2024). Si no se proporciona una fecha, se usará la fecha actual.
