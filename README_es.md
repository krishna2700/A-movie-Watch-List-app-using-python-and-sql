# Aplicación de Lista de Películas con Python y SQLite

## Descripción
Esta aplicación te permite gestionar una lista personal de películas que deseas ver. Utiliza Python para la lógica de la aplicación y SQLite como base de datos ligera para almacenar información de las películas.

## Características
- Agregar nuevas películas con título y año.
- Ver todas las películas guardadas en la base de datos.
- Actualizar o eliminar entradas existentes.
- Interfaz de línea de comandos sencilla.

## Requisitos
- Python 3.10 o superior
- Paquete `sqlite3` (incluido en la biblioteca estándar de Python)

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Revisa el archivo `requirements.txt` si existe, o instala manualmente cualquier dependencia adicional.

## Uso
1. Asegúrate de tener el archivo `data.db` o el script que inicializa la base de datos.
2. Ejecuta `python app.py` desde la terminal.
3. Sigue las instrucciones en pantalla para agregar, listar o modificar películas.

## Estructura del Proyecto
- `app.py`: Punto de entrada principal; maneja la interacción del usuario.
- `database.py`: Contiene las funciones para interactuar con SQLite.
- `data.db`: Base de datos con la información de las películas.

## Próximos Pasos Sugeridos
- Agregar una interfaz gráfica básica (por ejemplo, con Tkinter).
- Incluir búsqueda y filtrado de películas.
- Añadir pruebas automatizadas para asegurar la estabilidad del código.

## Licencia
Este proyecto se distribuye bajo los términos especificados en el archivo de licencia correspondiente (si aplica).
