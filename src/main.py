import os
import flet as ft
import utils
utils.ms_notify(message='Cargando Launcher de Kailand V, por favor espere...')
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