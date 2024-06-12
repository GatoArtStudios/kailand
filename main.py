import os
import flet as ft
from ui import app
from log import logger


# Crea el directorio de trabajo principal
if not os.path.exists(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand"):
    os.mkdir(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand")
    os.chdir(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand")
else:
    os.chdir(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand")

if __name__ == "__main__":
    logger.info("Debug del launcher iniciado")
    ft.app(target=app, assets_dir="assets")