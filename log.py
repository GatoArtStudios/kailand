import os
import logging
from logging import StreamHandler
import flet as ft

log_console = [] # Variable que almacena el log para la consola
LOG_AVAILABLE = False

def loger():
    """
    Configura el logger con la configuración básica necesaria para registrar mensajes.

    Establece el nivel de registro en INFO, el archivo de registro en "DIRECTORY_KAILAND",
    el formato de los mensajes de registro como "AAAA-MM-DD HH:MM:SS - NIVEL - MENSAJE" y devuelve el logger.

    :return: logger
    """
    from config import DIRECTORY_KAILAND
    # Configura el logger con la configuración básica
    logging.basicConfig(
        level=logging.INFO,  # Nivel de registro
        filename=os.path.join(DIRECTORY_KAILAND, "launcher.log"),  # Archivo de registro
        encoding='utf-8',  # Codificación de los mensajes de registro
        format='%(asctime)s - %(levelname)s - %(message)s',  # Formato de los mensajes de registro
        datefmt='%Y-%m-%d %H:%M:%S',  # Formato de la fecha y hora en los mensajes de registro
        )

    # Obtiene una instancia del logger
    logger = logging.getLogger(__name__)

    return logger

# Crea un manejador de transmisión para enviar los registros a una consola
class ConsoleHandler(StreamHandler):
    """
    Manejador de la consola que se encarga de capturar los registros y mostrarlos en la consola.
    """
    @property
    def update_lines_console(self):
        from config import DEBUG_LINES
        return int(DEBUG_LINES)
    
    def emit(self, record):
        """
        Método que se encarga de formatear el registro y actualizar la variable de log_console.

        :param record: El registro que se va a mostrar en la consola.
        :type record: dict
        """
        global log_console
        # Formatea el registro
        msg = self.format(record)

        # Agrega el registro a log_console
        if record.levelname == 'INFO':
            log_console.append(ft.Text(msg, color='green', selectable=True, font_family='FiraCode'))
        elif record.levelname == 'WARNING':
            log_console.append(ft.Text(msg, color='yellow', selectable=True, weight=ft.FontWeight.BOLD, font_family='FiraCode'))
        elif record.levelname == 'ERROR':
            log_console.append(ft.Text(msg, color='red', selectable=True, weight=ft.FontWeight.BOLD, font_family='FiraCode'))

        # Elimina los registros antiguos para proteger el rendimiento
        if len(log_console) > self.update_lines_console:
            log_console.pop(0)

        # Verifica si log_available es True
        if LOG_AVAILABLE:
            try:
                # Importa los módulos necesarios
                from layout import data_widget
                from ui import app

                # Actualiza el valor de console_log con log_console
                data_widget.console_log.controls = log_console
                # Actualiza la página de app
                app.page_update()
            except ImportError:
                pass

def log_logger():
    """
    Crea una instancia del logger, configura un manejador de handler para mostrar los registros en la consola y
    devuelve el logger.

    :return: logger
    """
    # Manejador de handler mostrado en consola
    logger = loger()  # Obtiene una instancia del logger
    handler = ConsoleHandler()  # Crea una instancia del manejador
    handler.setLevel(logging.INFO)  # Establece el nivel de registro a mostrar
    formatter = logging.Formatter('[+] %(asctime)s [-] %(levelname)s -> %(message)s', datefmt='%H:%M')  # Formatea el mensaje
    handler.setFormatter(formatter)  # Establece el formateador para el manejador
    logger.addHandler(handler)  # Agrega el manejador al logger
    return logger  # Devuelve la instancia del logger


logger = log_logger()