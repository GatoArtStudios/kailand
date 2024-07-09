import os
import flet as ft
import utils
import subprocess
import typing_extensions
from ui import app
from config import DIRECTORY_KAILAND, JAVA_PATH, SYSTEM
from log import logger



"""
Crea el directorio de trabajo principal, si no existe,
lo crea y se cambia al directorio creado.
"""

if __name__ == "__main__":
    # Crea e inicia la aplicación de Flet con la interfaz de usuario definida en el archivo ui.py y los recursos en la carpeta assets.
    ft.app(target=app, assets_dir="assets")


# Verifica si el directorio de trabajo principal existe
if not os.path.exists(DIRECTORY_KAILAND):
    # Si no existe, crea el directorio
    utils.ms_notify(message='Estamos configurando todo, esto puede tomar unos segundos...')
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

try:
    # Ejecuta el comando `java -version` y captura la salida, sin mostrar la terminal
    if SYSTEM == "Windows":
        startinfo = subprocess.STARTUPINFO() # agregamos el startupinfo para que no se muestre la terminal
        startinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    result = subprocess.run([JAVA_PATH, '-version'], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True if SYSTEM == "Windows" else False, startupinfo=startinfo if SYSTEM == "Windows" else None)
    # La salida del comando `java -version` se envía a stderr en lugar de stdout
    version_info = result.stderr.split('\n')[0].split(' ')[2].split('"')[1].split('.')[0]
    if int(version_info) >= 17:
        logger.info(f"Java version: {version_info}")
    else:
        utils.ms_notify(message='Debe instalar una version de java compatible, debe ser openjkd 17 o superior.')
        logger.error(f'La version actual {version_info} de java no es compatible, descarge una version reciente: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html')
except subprocess.CalledProcessError as e:
    utils.ms_notify(message='Debe instalar una version de java compatible, debe ser openjkd 17 o superior.')
    logger.error(f"Error al obtener la versión de Java, descarga una versión reciente: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html", exc_info=True)
except FileNotFoundError:
    utils.ms_notify(message='Debe instalar una version de java compatible, debe ser openjkd 17 o superior.')
    logger.error("Java no está instalado o no está en el PATH del sistema, descarga una versión reciente: https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html", exc_info=True)