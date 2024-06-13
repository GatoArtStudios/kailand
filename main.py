import os
import flet as ft
from config import DIRECTORY_KAILAND


"""
Crea el directorio de trabajo principal, si no existe,
lo crea y se cambia al directorio creado.
"""

# Verifica si el directorio de trabajo principal existe
if not os.path.exists(DIRECTORY_KAILAND):
    # Si no existe, crea el directorio
    os.mkdir(DIRECTORY_KAILAND)

    # Cambia al directorio creado
    os.chdir(DIRECTORY_KAILAND)
else:
    # Si existe, cambia al directorio
    os.chdir(DIRECTORY_KAILAND)

# se importan desde este punto para evitar que halla errores con la creacion de las carpetas
from ui import app
from log import logger

# Condición para ejecutar el código solo si el archivo es el archivo principal
# del programa, es decir, si se ejecuta directamente desde la línea de comandos.
if __name__ == "__main__":
    """
    Función principal del programa.
    Esta función se ejecuta cuando se inicia el programa directamente desde la línea de comandos.
    """

    # Registra un mensaje de información en el archivo de registro indicando el directorio de trabajo principal.
    logger.info("Directorio de trabajo principal: " + os.getcwd())

    # Registra un mensaje de información en el archivo de registro indicando que el debug del launcher ha sido iniciado.
    logger.info("Debug del launcher iniciado")

    # Crea e inicia la aplicación de Flet con la interfaz de usuario definida en el archivo ui.py y los recursos en la carpeta assets.
    ft.app(target=app, assets_dir="assets")
