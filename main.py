import os
import flet as ft
import subprocess
import typing_extensions
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

# Verifica si el directorio de configuración existe
if not os.path.exists(os.path.join(DIRECTORY_KAILAND, "config")):
    # Si no existe, crea el directorio
    os.mkdir(os.path.join(DIRECTORY_KAILAND, "config"))

# se importan desde este punto para evitar que halla errores con la creacion de las carpetas
from ui import app
from log import logger

try:
    # Ejecuta el comando `java -version` y captura la salida
    result = subprocess.run(['java', '-version'], capture_output=True, text=True, check=True)
    # La salida del comando `java -version` se envía a stderr en lugar de stdout
    version_info = result.stderr.split('\n')[0].split(' ')[2].split('"')[1].split('.')[0]
    if int(version_info) >= 17:
        logger.info(f"Java version: {version_info}")
    else:
        logger.error(f'La version actual {version_info} de java no es compatible, descarge una version reciente: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html')
except subprocess.CalledProcessError as e:
    logger.error(f"Error al otener la vercion de Java, descarge una version reciente: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html", exc_info=True)
except FileNotFoundError:
    logger.error("Java no está instalado o no está en el PATH del sistema, descarge una version reciente: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html", exc_info=True)

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
