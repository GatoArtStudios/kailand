import os
import sys
import uuid
import json
import time
import threading
import logging
import requests
import webbrowser
import sqlite3
from typing import Any
import subprocess
import flet as ft
import minecraft_launcher_lib
from logging import StreamHandler

# Crea el directorio de trabajo principal
if not os.path.exists(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand"):
    os.mkdir(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand")
    os.chdir(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand")

else:
    os.chdir(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand")

log_console = '' # Variable que almacena el log para la consola
log_available = False

logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand", "launcher.log"),
    encoding='utf-8',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    )

logger = logging.getLogger(__name__)

# Crea un manejador de transmisión para enviar los registros a una consola
class ConsoleHandler(StreamHandler):
    def emit(self, record):
        global log_console
        msg = self.format(record)
        log_console += f'{msg}\n'
        if log_available:
            data_widget.console_log.value = log_console
            app.page_update()
        # print(msg) # Debug

# Manejador de handler mostrado en consola
logger = logging.getLogger(__name__)
handler = ConsoleHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('[+] %(asctime)s [-] %(levelname)s -> %(message)s', datefmt='%H:%M')
handler.setFormatter(formatter)
logger.addHandler(handler)

class DATABASE:
    def __init__(self) -> None:
        self.data_nube = {}
        self.name_database = "kailand_database.db"

    def build(self):
        with sqlite3.connect(self.name_database) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                            CREATE TABLE IF NOT EXISTS launcher(
                                configVersion TEXT,
                                launcherVersion TEXT,
                                launcherUrl TEXT,
                                updateDescription TEXT,
                                reglas TEXT,
                                horario TEXT,
                                mods TEXT,
                                complementos TEXT
                            )
            ''')

class Mc:
    def __init__(self) -> None:
        '''
        Almacena todos los datos del minecraft y metodos para el mismo funcionamiento, tambien se encarga de checar la integridad de los datos al inicial el launcher
        '''
        self.data_nube = {}
        self.ID = uuid.uuid4().hex
        self.url_new_vercion = None
        self.launcherVersion = "1.0.24.0"
        self.boton_jugar = "Iniciado"
        self.mc_disponible = True
        self.minecraft_directory = f"C://Users//{os.environ['USERNAME']}//AppData//Roaming//.kailand"
        self.options = {
            "username": None,
            "uuid": None,
            "token": "",
            "executablePath": "java",
            "jvmArguments": ["-Xmx5G", "-Xms2G"],
            "launcherName": "Kailand V - Launcher",
            "gameDirectory": self.minecraft_directory,
            "customResolution": True,
            "resolutionHeight": "480",
            "resolutionWidth": "854",
            "launcherVersion": "1.0",
        }
        self.archivo_kailand = os.path.join(self.minecraft_directory, "kaliand.json")
        self.ruta_mods = os.path.join(self.minecraft_directory, "mods")
        self.url_base_mods = 'https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods'
        self.cheking()
        self.load_data_file_config()
        self.archivos_mods = []
        self.path_files_mods = []
        self.list_files_directory_mods()
        self.valor_xmx = self.ram_launcher()
        self.valor_xmx_temp = self.ram_launcher()
        self.changer_save_file_kailand()
        self.download_optional = 0

    def load_data_file_config(self):
        '''
        Carga los datos del archivo mods_data.json en la siguiente ruta:
        ```
        class Mc:
            def __init__(self):
                self.data_nube = {}
        ```
        '''
        if os.path.exists(os.path.join(self.minecraft_directory, "mods_data.json")):
            with open(os.path.join(self.minecraft_directory, "mods_data.json"), "r") as read_data_mods:
                temp_data_mods = json.load(read_data_mods)
                self.data_nube.update(temp_data_mods)
        else:
            response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
            self.data_nube.update(response.json())

    def ram_launcher(self):
        '''
        Verficia la cantidad de ram que tiene el usuario
        '''
        ram_max = self.options["jvmArguments"][0]
        if ram_max == "-Xmx2G":
            return 2
        elif ram_max == "-Xmx3G":
            return 3
        elif ram_max == "-Xmx4G":
            return 4
        elif ram_max == "-Xmx5G":
            return 5
        elif ram_max == "-Xmx6G":
            return 6
        elif ram_max == "-Xmx7G":
            return 7
        elif ram_max == "-Xmx8G":
            return 8
        elif ram_max == "-Xmx9G":
            return 9
        elif ram_max == "-Xmx10G":
            return 10
        elif ram_max == "-Xmx11G":
            return 11
        elif ram_max == "-Xmx12G":
            return 12
        elif ram_max == "-Xmx13G":
            return 13
        elif ram_max == "-Xmx14G":
            return 14
        elif ram_max == "-Xmx15G":
            return 15
        elif ram_max == "-Xmx16G":
            return 16

    def ram_launcher_changer(self, ram):
        '''
        Cambia la ram a usar por el usuario en el juego
        ```
        def ram_launcher_changer(self, ram):
        ```
        '''
        if ram == 2:
            self.options["jvmArguments"][0] = "-Xmx2G"
            return True
        elif ram == 3:
            self.options["jvmArguments"][0] = "-Xmx3G"
            return True
        elif ram == 4:
            self.options["jvmArguments"][0] = "-Xmx4G"
            return True
        elif ram == 5:
            self.options["jvmArguments"][0] = "-Xmx5G"
            return True
        elif ram == 6:
            self.options["jvmArguments"][0] = "-Xmx6G"
            return True
        elif ram == 7:
            self.options["jvmArguments"][0] = "-Xmx7G"
            return True
        elif ram == 8:
            self.options["jvmArguments"][0] = "-Xmx8G"
            return True
        elif ram == 9:
            self.options["jvmArguments"][0] = "-Xmx9G"
            return True
        elif ram == 10:
            self.options["jvmArguments"][0] = "-Xmx10G"
            return True
        elif ram == 11:
            self.options["jvmArguments"][0] = "-Xmx11G"
            return True
        elif ram == 12:
            self.options["jvmArguments"][0] = "-Xmx12G"
            return True
        elif ram == 13:
            self.options["jvmArguments"][0] = "-Xmx13G"
            return True
        elif ram == 14:
            self.options["jvmArguments"][0] = "-Xmx14G"
            return True
        elif ram == 15:
            self.options["jvmArguments"][0] = "-Xmx15G"
            return True
        elif ram == 16:
            self.options["jvmArguments"][0] = "-Xmx16G"
            return True
        else:
            return False

    def cheking(self):
        '''
        Chequea que todos los archivos y datos esten en orden y crea los directorios necesarios.
        '''
        # Crea el directorio de trabajo principal
        if not os.path.exists(self.minecraft_directory):
            os.mkdir(self.minecraft_directory)
            os.chdir(self.minecraft_directory)
        else:
            os.chdir(self.minecraft_directory)
        # Crea el directorio de mods
        if not os.path.exists(os.path.join(self.minecraft_directory, "mods")):
            os.mkdir(os.path.join(self.minecraft_directory, "mods"))
        else:
            pass
        # Crea el directorio de Shader
        if not os.path.exists(os.path.join(self.minecraft_directory, "shaderpacks")):
            os.mkdir(os.path.join(self.minecraft_directory, "shaderpacks"))
        else:
            pass
        # Crea el directorio de Texturas
        if not os.path.exists(os.path.join(self.minecraft_directory, "resourcepacks")):
            os.mkdir(os.path.join(self.minecraft_directory, "resourcepacks"))
        else:
            pass

        # Comprueba si el archivo existe
        if os.path.exists(self.archivo_kailand):
            # Lee el contenido del archivo JSON y actualiza el diccionario de la variable options
            with open(self.archivo_kailand, 'r') as archivo:
                contenido_json = json.load(archivo)
                self.options.update(contenido_json)
            logger.info(self.options)

    def list_files_directory_mods(self):
        '''
        Carga una la lista de mods que tiene instalado el usuario y son almacenados en:
        ```
        class Mc:
            def __init__(self):
                self.archivos_mods = []
                self.path_files_mods = []
        ```
        '''
        for f in os.listdir(self.ruta_mods):
            ruta_completa_mod = os.path.join(self.ruta_mods, f)
            name_file_mod = f
            if os.path.isfile(ruta_completa_mod):
                self.archivos_mods.append(name_file_mod)
                self.path_files_mods.append(ruta_completa_mod)
        return True

    def descargar_mod(self, mod):
        '''
        Descarga los mods y los almacena en el directorio de mods
        '''
        destino = os.path.join(self.ruta_mods, mod['file'])
        if os.path.exists(destino):
            logger.info(f"El mod '{mod['name']}' ya está descargado.")
        else:
            logger.info(f"Descargando el mod '{mod['name']}'...")
            try:
                response = requests.get(mod["url"])
                if response.status_code == 200:
                    with open(destino, 'wb') as archivo:
                        archivo.write(response.content)
                    logger.info(f"Descarga exitosa: {destino}")
                else:
                    logger.error(f"Error al descargar el mod '{mod['name']}'. Código de estado: {response.status_code}")
            except Exception as e:
                logger.error(f"Error durante la descarga del mod '{mod['name']}': {e}")

    def download_comple(self, e, x):
        '''
        Descarga los complementos:
        `
        e: Evento
        x: Objeto
        `
        '''
        # Desabilita el control para evitar bugs
        e.control.disabled = True
        # Agrega proceso a la lista
        mc.download_optional += 1
        e.page.splash = ft.ProgressBar(tooltip=f"Configurando {x['name']}...", height=5)
        data_widget.buttom_jugar.disabled = True
        data_widget.buttom_jugar.text = 'Configurando'
        e.page.update()
        if e.data == 'true':
            self.descargar_mod(x)
            mc.download_optional -= 1
            if mc.download_optional == 0:
                e.page.splash = None
                data_widget.buttom_jugar.disabled = False
                data_widget.buttom_jugar.text = 'Jugar'
            e.control.disabled = False
            e.page.update()
        elif e.data == 'false':
            self.eliminar_mod(os.path.join(self.ruta_mods, x['file']))
            mc.download_optional -= 1
            if mc.download_optional == 0:
                e.page.splash = None
                data_widget.buttom_jugar.disabled = False
                data_widget.buttom_jugar.text = 'Jugar'
            e.control.disabled = False
            e.page.update()

    def eliminar_mod(self, archivo):
        '''
        Elimina mods, pasandole como argumento la ruta del archivo a remover
        '''
        try:
            os.remove(archivo)
            logger.info(f"Mod eliminado: {archivo}")
        except Exception as e:
            logger.error(f"Error al eliminar el mod '{archivo}': {e}")

    def comprobar_mods(self):
        '''
        Comprueva si los mods estan de acuerdo a al archivo de configuracion
        '''
        for mod in self.data_nube['mods']:
            if mod['disponible']:
                self.descargar_mod(mod)
            elif mod['file'] in self.archivos_mods:
                self.eliminar_mod(os.path.join(self.ruta_mods, mod['file']))
        return True

    def changer_save_file_kailand(self):
        '''
        Guardar datos en un archivo JSON
        '''
        with open(os.path.join(self.minecraft_directory, "kaliand.json"), "w") as json_file:
            json.dump(self.options, json_file, indent=4)
        logger.info("Guardo las optiones en el archivo de configuracion")

    def consulta_nube(self, bt_play = False):
        '''
        Consulta el archivo de configuracon en el servidor'
        '''
        response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
        if response.status_code == 200:
            temp_json = response.json()
            if os.path.exists(os.path.join(self.minecraft_directory, "mods_data.json")):
                if temp_json["configVersion"] == self.data_nube["configVersion"]:
                    return True
                else:
                    if bt_play:
                        with open(os.path.join(self.minecraft_directory, "mods_data.json"), "w") as save_data_mods:
                            json.dump(temp_json, save_data_mods, indent=4)
                        self.data_nube.update(temp_json)
                        return True
                    else:
                        return False

            else:
                self.data_nube.update(response.json())
                with open(os.path.join(self.minecraft_directory, "mods_data.json"), "w") as save_data_mods:
                    json.dump(self.data_nube, save_data_mods, indent=4)
                return True
        else:
            return False

    def validate_directory(self):
        '''
        Valida si los directorios y el minecraft esta instalado
        '''
        if os.path.exists(self.minecraft_directory):
            if os.path.exists(os.path.join(self.minecraft_directory, "mods")) and os.path.exists(os.path.join(self.minecraft_directory, "assets")) and os.path.exists(os.path.join(self.minecraft_directory, "libraries")) and os.path.exists(os.path.join(self.minecraft_directory, "runtime")) and os.path.exists(os.path.join(self.minecraft_directory, "versions"))  and os.path.exists(os.path.join(self.minecraft_directory, "shaderpacks")) and os.path.exists(os.path.join(self.minecraft_directory, "resourcepacks")) and os.path.exists(os.path.join(self.minecraft_directory, "versions","1.19.2")) and os.path.exists(os.path.join(self.minecraft_directory, "versions", "1.19.2-forge-43.3.8")):
                if self.consulta_nube():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def create_directory(self):
        '''
        Crea los directorios que falten
        '''
        if not self.validate_directory():
            logger.info("Creando directorios")
            if not os.path.exists(os.path.join(self.minecraft_directory, "mods")):
                os.mkdir(os.path.join(self.minecraft_directory, "mods"))
            if not os.path.exists(os.path.join(self.minecraft_directory, "resourcepacks")):
                os.mkdir(os.path.join(self.minecraft_directory, "resourcepacks"))
            if not os.path.exists(os.path.join(self.minecraft_directory, "shaderpacks")):
                os.mkdir(os.path.join(self.minecraft_directory, "shaderpacks"))
            logger.info("Directorios creados")
            return True
        else:
            return False

    def ejecuta_mc(self, e):
        '''
        Ejecuta el minecrat.
        '''
        if minecraft_launcher_lib.utils.is_minecraft_installed(self.minecraft_directory):
            logger.info("Minecraft si esta instalado")
            data_widget.animate_buttom(e)
            # Guardar datos en un archivo JSON
            with open(os.path.join(self.minecraft_directory, "kaliand.json"), "w") as json_file:
                json.dump(self.options, json_file, indent=4)
            # Obtiene el comando para ejecutar Minecraft
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.19.2-forge-43.3.8", self.minecraft_directory, self.options)
            # Agrega datos al logger
            logger.info("Ejecutando Minecraft")
            e.control.bgcolor = ft.colors.with_opacity(0.1, "white")
            e.control.icon = ft.icons.PLAY_CIRCLE
            e.control.color = ft.colors.with_opacity(0.5, "white")
            e.control.text = "Jugando"
            e.control.disabled = True
            e.control.update()
            # Ejecuta y alamcena el debug de minecraft java
            debug_minecraft_launch = subprocess.run(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
            # Registrar la salida estándar (stdout)
            if debug_minecraft_launch.stdout:
                logger.info(debug_minecraft_launch.stdout.decode("utf-8"))

            # Registrar la salida de error (stderr)
            if debug_minecraft_launch.stderr:
                logger.error(debug_minecraft_launch.stderr.decode("utf-8"))

            # Agrega mensaje debug al logger
            logger.warning("Minecraft Detenido...")
            e.control.bgcolor = ft.colors.with_opacity(0.2, "white")
            e.control.icon = None
            e.control.color = "white"
            e.control.text = "Jugar"
            e.control.disabled = False
            e.control.update()
        else:
            logger.warning("Minecraft no instalado")

    def check_update_launcher(self):
        '''
        Chequea actualizaciones en el servidor
        '''
        response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
        if response.status_code == 200:
            __temp_data_get = response.json()
            if not __temp_data_get["launcherVersion"] == self.launcherVersion: # Si la vercion no es la misma es valido
                return True
            else: # Si la vercion es la misma ignora el resto
                return False
        else:
            return False

    def install_minecraft(self, e):
        '''
        Instala el minecraft
        '''
        if self.validate_directory():
            logger.info("Todos los recursos estan")
        else:
            logger.warning("Faltan algunos recursos necesarios")
            self.create_directory()
            self.consulta_nube(bt_play=True)
            if not os.path.exists(os.path.join(self.minecraft_directory, "versions", "1.19.2")):
                logger.info("Instalando Minecraft vanila")
                minecraft_launcher_lib.install.install_minecraft_version("1.19.2", self.minecraft_directory)
                logger.info("Minecraft instalado")
            if not os.path.exists(os.path.join(self.minecraft_directory, "versions", "1.19.2-forge-43.3.8")):
                logger.info("Instalando Forge")
                minecraft_launcher_lib.forge.install_forge_version("1.19.2-43.3.8", self.minecraft_directory)
                logger.info("Forge Instalado")
            if self.comprobar_mods():
                data_widget.buttom_jugar.disabled = False
                data_widget.buttom_jugar.text = "Jugar"
                data_widget.buttom_jugar.icon = False
                e.page.splash = None
                e.page.update()
                data_widget.open_dlg(e)

class DataWidget:

    def __init__(self):
        '''
        Almacena todos los Widget de UI
        ```
        class DataWidget:
            data_widget: dict, # Almacena todos los widget.
            main_file: ft.Row, # Ejemplo de controles en fila.
            main: ft.Container # contenedor base del UI.
        ```
        '''
        self.data_widget = {
            'texto': ft.Text('Primer Texto'),
            'texto2': ft.Text('Segundo Texto'),
            'buttom': ft.ElevatedButton('Cambia de Texto', on_click=self.edit_main)
        }
        self.main_file = ft.Row(
            [
                self.data_widget['texto'],
                self.data_widget['buttom']
            ]
        )
        self.main = ft.Container(
            content=self.main_file
        )
        self.console_log = ft.Text("", selectable=True, color="white")
        self.dlg = ft.AlertDialog(title=ft.Text("Resumen de instalacion"), content=ft.Text("Todos los recursos necesarios para jugar ya estan instalados."))
        self.check_vercion_launcher = ft.AlertDialog(
            title=ft.Text("Actualizacion disponible"),
            content=ft.Text("Para seguir usando el launcher descarge la nueva version del launcher por favor"),
            on_dismiss=self.close_launcher_update,
            actions=[
                ft.TextButton("Descargar", on_click=self.close_launcher_update, icon=ft.icons.CLOUD_DOWNLOAD)
            ]
        )
        self.dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Aviso"),
            content=ft.Text("Quieres instalar los recursos necesarios para Kailand V? la instalacion dura unos cuantos minutos"),
            actions=[
                ft.TextButton("Si", on_click=self.close_dlg_exe),
                ft.TextButton("No", on_click=self.close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        self.user_alert = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("Para jugar debes agregar tu cuenta primero"),
                        ft.ElevatedButton("Ir a Perfil", on_click=lambda e: (self.accounts_gui(e), self.user_none_alert_close(e)), bgcolor=ft.colors.with_opacity(0.2, "black"), color="white", width=280, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
                    ],
                    tight=True,
                ),
                padding=20
            ),
            open=False,
            bgcolor=ft.colors.with_opacity(0.2, "white"),
        )
        self.resolution_width = ft.TextField(label="Ancho", hint_text="Ancho (pixeles)", border_color="white", disabled=False, value=mc.options["resolutionWidth"], color="white")
        self.resolution_x = ft.Text("X", color="white")
        self.resolution_height = ft.TextField(label="Alto", hint_text="Alto (pixeles)", border_color="white", disabled=False, value=mc.options["resolutionHeight"], color="white")
        self.buttom_mods = ft.ElevatedButton(text="Mods  ", bgcolor = ft.colors.with_opacity(0.2, "white"), color = "white", width=200, on_click=self.mods_gui, icon=ft.icons.FOLDER, icon_color="white", animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_shaders = ft.ElevatedButton(text="Shaders", bgcolor = ft.colors.with_opacity(0.2, "white"), color = "white", width=200, on_click=self.open_folder_shaderpacks, icon=ft.icons.FOLDER, icon_color="white", animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_textures = ft.ElevatedButton(text="Textures", bgcolor = ft.colors.with_opacity(0.2, "white"), color = "white", width=200, on_click=self.open_folder_resourcepacks, icon=ft.icons.FOLDER, icon_color="white", animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_login = ft.ElevatedButton(text="Login", bgcolor = ft.colors.with_opacity(0.2, "white"), disabled=True, color="white")
        self.text_p = ft.TextField(label="Usuario (Offline)", label_style=ft.TextStyle(color="White"), hint_text="Coloca tu usuario y guarda de nuevo", hint_style=ft.TextStyle(color="white"), border_color="white", disabled=True, color="white", bgcolor=ft.colors.with_opacity(0.2, "black"), focused_color="white")
        self.input_offline_name = ft.Container(content=self.text_p)
        self.text_reglas = self.consulta_reglas()
        self.text_reglas_list = self.text_reglas.split("\n")
        self.java_info = ft.FilePicker(on_result= self.result_java_path)
        self.info_execute_java = self.data_java_execute()
        self.text_save_setting = ft.Text(top=260, color="white")
        self.t = ft.Text(color="white")
        self.buttom_save = ft.ElevatedButton(text="Guardar", on_click=lambda e: (self.save_info(e), self.animate_buttom(e)), color="white", bgcolor=ft.colors.with_opacity(0.2, "white"), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_save_setting = ft.ElevatedButton(text="Guardar", on_click=lambda e: (self.save_setting(e), self.animate_buttom(e)), color="white", bgcolor=ft.colors.with_opacity(0.2, "white"), top=290, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.type_login = ft.Dropdown(label="Tipo de cuenta", label_style=ft.TextStyle(color="white"), hint_text="Seleccione el tipo", hint_style=ft.TextStyle(color="white"), options=[ft.dropdown.Option("Offline"), ft.dropdown.Option("(Online) Microsoft")], border_color="white", width=300, on_change=self.save_info, color="white", bgcolor="black")
        self.select_bar_ram = ft.Slider(min=2, max=16, divisions=14, label="{value}Gb", value=mc.valor_xmx, on_change=lambda e: self.change_ram_text(e, self.text_ram), width=620)
        self.java_path = ft.TextField(label="Ejecutable de Java", read_only=True, border_color="white", width=500, value=self.info_execute_java, color="white")
        self.buttom_change_java = ft.ElevatedButton(
            text="Cambiar",
            on_click=lambda _: (self.java_info.pick_files(allowed_extensions=["exe"], initial_directory="C:\Program Files\Java", dialog_title="Seleccione el archivo java.exe o javaw.exe"), self.animate_buttom(e=_)),
            color="white",
            bgcolor=ft.colors.with_opacity(0.2, "white"),
            animate_scale=ft.animation.Animation(duration=400, curve="bounceout"),
            scale=ft.transform.Scale(1)
        )
        self.text_ram = ft.Text(f"Ram Actual: ({mc.valor_xmx} Gb)", color="white")
        self.ajustes_widget = ft.Container(
            content=ft.Column([
                    ft.Text("Resolucion de Minecraft", color="white"),
                    ft.Row([
                        self.resolution_height,
                        self.resolution_x,
                        self.resolution_width
                        ],
                    ),
                    ft.Row(
                        [
                            self.java_path,
                            self.buttom_change_java
                        ]
                        ),
                    self.text_ram,
                    self.select_bar_ram,
                    ft.Stack([
                        self.text_save_setting,
                        self.buttom_save_setting,
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Container(
                                        content=ft.Text("Kailand V", italic=True),
                                        url="https://discord.gg/chwAE86T6W",
                                        opacity=0.5,
                                        animate_opacity=300,
                                        on_hover=self.animation_colaboracion,
                                        scale=ft.transform.Scale(1),
                                        animate_scale=ft.animation.Animation(duration=300, curve="bounceout")
                                        ),
                                    ft.Container(
                                        content=ft.Text("X"),
                                        opacity=0.5,
                                        animate_opacity=300,
                                        on_hover=self.animation_colaboracion,
                                        scale=ft.transform.Scale(1),
                                        animate_scale=ft.animation.Animation(duration=300, curve="bounceout")
                                        ),
                                    ft.Container(
                                        content=ft.Text("SoyGato_Hcc", italic=True),
                                        url="https://linktr.ee/soygato_hcc",
                                        opacity=0.5,
                                        animate_opacity=300,
                                        on_hover=self.animation_colaboracion,
                                        scale=ft.transform.Scale(1),
                                        animate_scale=ft.animation.Animation(duration=300, curve="bounceout")
                                    )
                                ]
                            ),
                            top=300,
                            left=760
                        )
                        ])
                    ],
                spacing=15,
                ),
            padding=30,
        )
        self.reglas_widget = ft.Container(
            content=ft.Column([
                    ft.Text("Reglas de Kailand", color="white", size=50, weight=ft.FontWeight.W_900, selectable=True),
                    ft.Container(
                        content=ft.Column(
                            [ft.Container(content=ft.Text(regla), padding=10, border_radius=5, bgcolor=ft.colors.with_opacity(0.3, "black"), width=900, scale=ft.transform.Scale(1), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), on_hover=lambda e: self.animation_scale_zoom(e)) for regla in self.text_reglas_list],
                            height=480,
                            width=1600,
                            scroll=ft.ScrollMode.ALWAYS,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER
                        ),
                        margin=ft.margin.only(top=50)
                    )
                    ],
                spacing=15,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
                ),
            padding=10
        )
        self.console_widget = ft.Container(
            content=ft.Container(
                content=self.console_log,
                bgcolor=ft.colors.with_opacity(0.8, "black"),
                border_radius=5,
                padding=10,
                height=610,
                width=1100
                ),
            padding=10
        )
        self.perfil_widget = ft.Container(
            content=ft.Column([
                    ft.Row([
                    self.type_login,
                    self.input_offline_name,
                    self.buttom_login,
                    ]),
                    self.t,
                    ft.Stack([self.buttom_save])
                    ]),
            padding=30
        )
        self.c_derecho_cont = ft.Text("ㅤ")
        self.c_derecho = ft.Container(
                        content=self.c_derecho_cont,
                            margin = 0,
                            padding = 0,
                            alignment = ft.alignment.center,
                            bgcolor = None,
                            width = 1010,
                            height = 650,
                            blur = 4,
                            on_hover = self.animation_opacity,
                            border_radius = 10,
                            opacity=0.3,
                            animate_opacity=300,
                            disabled=True,
                            # border=ft.border.all(2, ft.colors.GREEN)
        )
        self.user_alert = ft.BottomSheet(
            ft.Container(
                ft.Column(
                    [
                        ft.Text("Para jugar debes agregar tu cuenta primero"),
                        ft.ElevatedButton("Ir a Perfil", on_click=lambda e: (self.accounts_gui(e), self.user_none_alert_close(e)), bgcolor=ft.colors.with_opacity(0.2, "black"), color="white", width=280, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
                    ],
                    tight=True,
                ),
                padding=20
            ),
            open=False,
            bgcolor=ft.colors.with_opacity(0.2, "white"),
        )
        self.buttom_horario = ft.ElevatedButton(text="Horario", bgcolor=ft.colors.with_opacity(0.2, "white"), color="white", width=200, icon=ft.icons.CALENDAR_MONTH, icon_color="white", on_click=lambda e: (self.animate_buttom(e)), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_console = ft.ElevatedButton(text="Consola", bgcolor=ft.colors.with_opacity(0.2, "white"), color="white", width=200, icon=ft.icons.CODE, icon_color="white", on_click=self.console_gui, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))    
        self.buttom_perfil = ft.ElevatedButton(text="Perfil", bgcolor=ft.colors.with_opacity(0.2, "white"), color="white", width=200, icon=ft.icons.MANAGE_ACCOUNTS, icon_color="white", on_click=self.accounts_gui, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_reglas = ft.ElevatedButton(text="Reglas", bgcolor=ft.colors.with_opacity(0.2, "white"), color="white", width=200, icon=ft.icons.ADMIN_PANEL_SETTINGS, icon_color="white", on_click=lambda e:(self.reglas_gui(e), self.animate_buttom(e)), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_discord = ft.ElevatedButton(text = "discord",bgcolor = ft.colors.with_opacity(0.2, "white"), color = "white", width = 200, icon=ft.icons.DISCORD, url = "https://discord.gg/chwAE86T6W", on_click=self.animate_buttom, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_ajustes = ft.ElevatedButton(text = "Ajustes",bgcolor = ft.colors.with_opacity(0.2, "white"), color = "white", width = 200, icon=ft.icons.SETTINGS, icon_color="white", on_click=self.ajustes_gui, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_jugar = ft.ElevatedButton(
            text = mc.boton_jugar,
            bgcolor = ft.colors.with_opacity(1, '#00bd1c'),
            color = "black",
            width = 200,
            disabled = mc.mc_disponible,
            on_click=lambda e: mc.ejecuta_mc(e) if mc.options["username"] else (self.user_none_alert_show(e), self.animate_buttom(e)),
            animate_scale=ft.animation.Animation(duration=400, curve="bounceout"),
            scale=ft.transform.Scale(1),
            style=ft.ButtonStyle(
                shadow_color='green'
            )
        )
        self.div_mods = ft.Container(
            content=ft.Row(
                [
                    self.contMods(x['name'], x['descripcion'], x['doct'] if x['doct'] else 'http://example.com', x) for x in mc.data_nube['complementos']
                ],
                height=480,
                width=1600,
                scroll=ft.ScrollMode.ALWAYS,
            ),
            height=480,
            width=1600,
        )

    def contMods(self, titulo = 'Sin datos', descripcion = 'Sin datos', url = 'http://example.com', x = None):
        '''
        Crea el contendor que contendra la informacion de cada mod complementario.
        '''
        if os.path.exists(os.path.join(mc.ruta_mods, x['file'])):
            disponible = True
        else:
            disponible = False

        top_bar = ft.Container(
                        content=ft.Row(
                            [
                                ft.Text(titulo, width=200, size=20, weight=ft.FontWeight.W_900),
                                ft.Switch(
                                    value=disponible,
                                    active_color='green',
                                    on_change= lambda e: mc.download_comple(e, x)
                                )
                            ],
                        ),
                        height=40,
        )
        bottom = ft.Container(
                        content=ft.Column(
                            [
                                ft.Text(descripcion, height=100),
                                ft.Container(
                                    content=ft.Text('Mas...', color='yellow'),
                                    on_click=lambda e: webbrowser.open(url)
                                )
                            ]
                        ),
                        height=130,
        )
        return ft.Container(
            content=ft.Column(
                [
                    top_bar,
                    bottom
                ]
            ),
            bgcolor= ft.colors.with_opacity(0.3, 'black'),
            width=300,
            height=200,
            border_radius=10,
            padding=10
        )

    def close_launcher_update(self, e):
        '''
        Cierra el launcher / programa
        '''
        webbrowser.open(mc.url_new_vercion)
        e.page.window_destroy()
        time.sleep(3)
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)

    def edit_main(self, e) -> None:
        '''
        Edita el texto y actualiza la pagina:
        ```
        def edit_main(self, e):
            if self.main_file.controls[0] == self.data_widget['texto']:
                self.main_file.controls[0] = self.data_widget['texto2']
                e.page.update()
            else:
                self.main_file.controls[0] = self.data_widget['texto']
                e.page.update()
        ```
        '''
        if self.main_file.controls[0] == self.data_widget['texto']:
            self.main_file.controls[0] = self.data_widget['texto2']
            e.page.update()
        else:
            self.main_file.controls[0] = self.data_widget['texto']
            e.page.update()

    def animate_buttom(self, e):
        '''
        Anima los botones para darle dinamismo
        '''
        e.control.scale = ft.transform.Scale(0.75)
        e.control.update()
        time.sleep(0.3)
        e.control.scale = ft.transform.Scale(1)
        e.control.update()

    def open_folder_mods(self, e):
        '''
        Habre el directorio de mods
        '''
        self.animate_buttom(e)
        folder = os.path.join(mc.minecraft_directory, "mods")
        if os.path.exists(os.path.join(mc.minecraft_directory, "mods")):
            logger.info(folder)
            os.startfile(folder)
            return True
        else:
            logger.warning(f"El forder: {folder}, No existe, crando directorio")
            os.mkdir(folder)
            return False

    def open_folder_resourcepacks(self, e):
        '''
        Abre directorio de Resource Packs
        '''
        self.animate_buttom(e)
        folder = os.path.join(mc.minecraft_directory, "resourcepacks")
        if os.path.exists(os.path.join(mc.minecraft_directory, "resourcepacks")):
            logger.info(folder)
            os.startfile(folder)
            return True
        else:
            logger.warning(f"El forder: {folder}, No existe, creando directorio")
            os.mkdir(folder)
            return False

    def open_folder_shaderpacks(self, e):
        '''
        Abre el direcotrio de Shader Packs
        '''
        self.animate_buttom(e)
        folder = os.path.join(mc.minecraft_directory, "shaderpacks")
        if os.path.exists(os.path.join(mc.minecraft_directory, "shaderpacks")):
            logger.info(folder)
            os.startfile(folder)
            return True
        else:
            logger.warning(f"El forder: {folder}, No existe, creando directorio")
            os.mkdir(folder)
            return False

    def open_dlg(self, e):
        '''
        Abre cuadro de dialogo
        '''
        e.page.dialog = self.dlg
        self.dlg.open = True
        e.page.update()

    def close_dlg(self, e):
        '''
        Cierra alerta de instalacion de recursos necesarios
        '''
        self.dlg_modal.open = False
        e.page.update()

    def close_dlg_exe(self, e):
        '''
        Instala recursos
        '''
        e.page.splash = ft.ProgressBar(tooltip="Instalando recursos necesarios...", height=5)
        self.dlg_modal.open = False
        e.page.update()
        mc.install_minecraft(e)

    def user_none_alert_show(self, e):
        '''
        Muestra alerta a usuario
        '''
        self.user_alert.open = True
        self.user_alert.update()

    def user_none_alert_close(self, e):
        '''
        Cierra alerta a usuario
        '''
        self.user_alert.open = False
        self.user_alert.update()

    def save_info(self, e):
        '''
        Funcion que se ejecuta al precionar el boton "Guardar"
        '''
        if not self.type_login.value:
            self.t.value = "Por favor seleccione un tipo de cuenta"
            e.page.update()
        else:
            if self.type_login.value == "Offline":
                self.text_p.disabled = False
                self.buttom_login.disabled = True
                kailand_username = mc.options["username"]
                if kailand_username:
                    self.t.value = f"Tipo de cuenta: {self.type_login.value}, Usuario: {mc.options['username']}"
                    e.page.update()
                else:
                    self.t.value = f"Tipo de cuenta: {self.type_login.value} - (Recuerde escribir el Usuario que usara)"
                if self.text_p.value:
                    mc.options.update(
                        {
                            "username": self.text_p.value,
                            "uuid": mc.ID,
                        }
                    )
                    # Guardar datos de session en un archivo JSON que guarda las configuraciones del usuario
                    with open(os.path.join(mc.minecraft_directory, "kaliand.json"), "w") as json_file:
                        json.dump(mc.options, json_file, indent=4)
                    self.t.value = f"Tipo de cuenta: {self.type_login.value}, Usuario: {self.text_p.value}"
                e.page.update()
            else:
                self.buttom_login.disabled = False
                self.buttom_login.bgcolor = ft.colors.with_opacity(0.2, "blue")
                self.text_p.disabled = True
                self.t.value = f"Tipo de cuenta: {self.type_login.value} - (Por favor dele a Login para completar el proceso)"
                e.page.update()

    def save_setting(self, e):
        '''
        Funcion llamada por el boton de guardar ajustes, se encarga de guardar los respectivos ajustes
        '''
        try:
            self.resolution_height.value = int(self.resolution_height.value)
            self.resolution_width.value = int(self.resolution_width.value)
        except:
            self.text_save_setting.value = f"Por favor introdusca solo numeros como valor de la resolucion"
            e.page.update()
            pass
        if not self.resolution_height.value == mc.options["resolutionHeight"]: # Guarda la resulocion de altura elegida por el jugador (Resolucion)
            if type(self.resolution_height.value) == int:
                self.text_save_setting.value = "Guardado correctamente"
                mc.options["resolutionHeight"] = f"{self.resolution_height.value}"
                logger.info(f"Guardando los ajustes de resolucion: {self.resolution_height.value}")
                e.page.update()
        if not self.resolution_width.value == mc.options["resolutionWidth"]: # Guarda la resolucion el ancho elegido por el jugador (Resolucion)
            if type(self.resolution_width.value) == int:
                self.text_save_setting.value = "Guardado correctamente"
                mc.options["resolutionWidth"] = f"{self.resolution_width.value}"
                logger.info(f"Guardando los ajustes de resolucion: {self.resolution_width.value}")
                e.page.update()
        if not self.select_bar_ram.value == mc.valor_xmx:
            logger.info(f"Ejecutado changer ram {mc.valor_xmx_temp}")
            mc.ram_launcher_changer(ram = mc.valor_xmx_temp)
            logger.info(mc.options)
            self.text_save_setting.value = "Guardado correctamente"
            e.page.update()
        if not self.java_path.value == "Por Defecto":
            mc.options["executablePath"] = self.java_path.value
        mc.changer_save_file_kailand()

    def change_ram_text(self, e, text_data):
        text_data.value = f"Ram Seleccionada: ({int(e.control.value)} GB)"
        mc.valor_xmx_temp = int(e.control.value)
        e.page.update()

    def result_java_path(self, e: ft.FilePickerResultEvent):
        if e.files and e.files[0].name == "java.exe" or e.files[0].name == "javaw.exe":
            self.java_path.value = e.files[0].path
            self.java_path.update()
        else:
            self.text_save_setting.value = "Solo puedes elegir (java.exe o javaw.exe) como ejecutable de java"
            self.text_save_setting.update()

    def data_java_execute(e = None):
        if mc.options["executablePath"] == "java":
            return "Por Defecto"
        else:
            return mc.options["executablePath"]

    def consulta_reglas(e = None):
        '''
        Consulta las reglas de la variable mc.data_nube -> Dict
        '''
        try:
            __data_temp = mc.data_nube["reglas"]
            if mc.data_nube["reglas"]:
                return  mc.data_nube["reglas"]
            else:
                return "Aun no hay datos del servidor"
        except:
            return "Aun no hay reglas del servidor"

    def animation_colaboracion(self, e):
        '''
        Animaciones de los textos de colaborazion.
        '''
        if e.data == "true":
            e.control.opacity = 1
            e.control.scale = ft.transform.Scale(1.3)
            e.control.update()
        elif e.data == "false":
            e.control.opacity = 0.5
            e.control.scale = ft.transform.Scale(1)
            e.control.update()

    def animation_scale_zoom(self, e):
        '''
        Contenedor que Tiene las reglas consultadas de la nube
        '''
        if e.data == "true":
            e.control.scale = ft.transform.Scale(1.1)
            e.control.update()
        else:
            e.control.scale = ft.transform.Scale(1)
            e.control.update()

    def blur_container(self, e):
        '''
        Animacion del efecto Blur en contenedores.
        '''
        if self.c_derecho.blur == 4:
            self.c_derecho.blur = 0
            self.c_derecho.bgcolor = None
        else:
            self.c_derecho.blur = 4
            self.c_derecho.bgcolor = ft.colors.with_opacity(0.1, "black")
        e.page.update()

    def animation_opacity(self, e):
        '''
        Realiza la animacion de opacidad con hover en contenedores.
        '''
        if e.data == "true":
            e.control.opacity = 1
            e.control.update()
        else:
            e.control.opacity = 0.3
            e.control.update()

    def load_text_console(self):
        app.page_update()
        self.console_log.value = ''
        lines = log_console.split('\n')
        for linea in lines:
            self.console_log.value += f'{linea}\n'
            app.page_update()

    def console_gui(self, e):
        '''
        Muestra el contenedor de Consola
        '''
        global log_available

        if self.c_derecho.content == self.console_widget:
            log_available = False
            self.c_derecho.content = self.c_derecho_cont
            self.c_derecho.disabled = True
            self.animate_buttom(e)
        else:
            log_available = True
            self.c_derecho.content = self.console_widget
            self.c_derecho.disabled = False
            e.page.update()
            self.animate_buttom(e)
            hilo = threading.Thread(target=self.load_text_console)
            hilo.start()
        e.page.update()

    def reglas_gui(self, e):
        '''
        Muestra el contenedor de reglas
        '''
        if self.c_derecho.content == self.reglas_widget:
            self.c_derecho.content = self.c_derecho_cont
            self.c_derecho.disabled = True
        else:
            self.consulta_reglas()
            self.c_derecho.content = self.reglas_widget
            self.c_derecho.disabled = False
        e.page.update()
        self.animate_buttom(e)

    def mods_gui(self, e):
        '''
        Muestra el contenedor de mods opcionales
        '''
        if self.c_derecho.content == self.div_mods:
            self.c_derecho.content = self.c_derecho_cont
            self.c_derecho.disabled = True
        else:
            self.consulta_reglas()
            self.c_derecho.content = self.div_mods
            self.c_derecho.disabled = False
        e.page.update()
        self.animate_buttom(e)

    def ajustes_gui(self, e):
        '''
        Muestra el contenedor de ajustes 
        '''
        if self.c_derecho.content == self.ajustes_widget:
            self.c_derecho.content = self.c_derecho_cont
            self.c_derecho.disabled = True
        else:
            self.c_derecho.content = self.ajustes_widget
            self.c_derecho.disabled = False
        e.page.update()
        self.animate_buttom(e)

    def accounts_gui(self, e):
        '''
        Muestra el contenedor de perfil
        '''
        if self.c_derecho.content == self.perfil_widget:
            self.c_derecho.content = self.c_derecho_cont
            self.c_derecho.disabled = True
        else:
            self.c_derecho.content = self.perfil_widget
            self.c_derecho.disabled = False
        e.page.update()
        self.animate_buttom(e)

class LauncherVentana:
    def __init__(self):
        self._page = None


    def __call__(self, flet_page: ft.Page) -> Any:
        self._page = flet_page
        self._page.title = 'Kailand V'
        self._page.padding = 0
        self._page.bgcolor = ft.colors.TRANSPARENT
        self._page.window_bgcolor = ft.colors.TRANSPARENT
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._page.theme_mode = ft.ThemeMode.DARK
        self._page.window_height = 715
        self._page.window_width = 1277
        self._page.window_resizable = False
        self._page.window_center = True
        self._page.overlay.append(data_widget.java_info)
        self._page.overlay.append(data_widget.user_alert)
        self._page.window_title_bar_hidden = True
        self._page.window_title_bar_buttons_hidden = True
        self._page.add(
            # Contenedor Principal y donde se agrega el fondo de la ventana
            ft.Container(
                content=ft.Column(
                    [
                        ft.WindowDragArea(
                            content=ft.Row(
                                [
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='minimizar.png',
                                            width=20,
                                            height=20,
                                            fit=ft.ImageFit.CONTAIN
                                        ),
                                        on_click=self.minimized_windows,
                                    ),
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='cerrar.png',
                                            width=20,
                                            height=20,
                                            fit=ft.ImageFit.CONTAIN
                                        ),
                                        on_click=self.close_windows,
                                    )
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                alignment=ft.MainAxisAlignment.END
                            ),
                            maximizable=False,
                            height=30,
                        ),
                        ft.Row(
                            [
                                # Contenedor Izquierdo
                                ft.Container(
                                    content=ft.Column(
                                        [
                                            data_widget.buttom_perfil,
                                            data_widget.buttom_reglas,
                                            # data_widget.buttom_horario,
                                            data_widget.buttom_mods,
                                            data_widget.buttom_shaders,
                                            data_widget.buttom_textures,
                                            data_widget.buttom_discord,
                                            data_widget.buttom_console,
                                            data_widget.buttom_ajustes,
                                            ft.Container(
                                                content=data_widget.buttom_jugar,
                                                margin=ft.margin.only(0, 260, 0 , 0)
                                            )
                                        ]
                                    ),
                                    margin=0,
                                    padding=10,
                                    bgcolor = ft.colors.with_opacity(0.2, "black"),
                                    width=200,
                                    height = 650,
                                    border_radius=10,
                                    blur = 3,
                                    # border=ft.border.all(2, ft.colors.GREEN)
                                ),
                                # Contenedor derecho
                                data_widget.c_derecho,
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15
                        ),
                        ft.Row(
                            [
                                ft.Stack(
                                    [
                                        ft.Container(
                                            content = ft.Text(self.open_dlg_modal()),
                                            top = 500,
                                        )
                                    ]
                                )
                            ]
                        )
                    ],
                    spacing=1
                ),
                # Fondo del launcher
                image_src="fondo.png",
                image_fit=ft.ImageFit.FILL,
                expand=True,
                border_radius=ft.border_radius.all(10),
            )
        )

    def close_windows(self, e):
        self._page.window_close()

    def minimized_windows(self, e):
        self._page.window_minimized = True
        self._page.update()

    def animacion_opacity(self, e):
        print(vars(e))
        if e.data == "true":
            e.control.opacity = 1
            e.control.update()
        else:
            e.control.opacity = 0.5
            e.control.update()

    def open_dlg_modal(self):
        '''
        Abre alerta con opciones si faltan recursos ///// Se ejecuta al iniciar el launcher de forma automatica para comprodar datos
        '''
        logger.info('Chequeando actualizaciones del servidor')
        if mc.check_update_launcher():
            response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
            if response.status_code == 200:
                __temp_data_get = response.json()
                mc.url_new_vercion = __temp_data_get["launcherUrl"]
                data_widget.check_vercion_launcher.content = ft.Text(f"{__temp_data_get['updateDescription']}")
            self._page.dialog = data_widget.check_vercion_launcher
            data_widget.check_vercion_launcher.open = True
            self._page.update()
            time.sleep(20)
            webbrowser.open(__temp_data_get["launcherUrl"])
            self._page.window_destroy()
            time.sleep(3)
            try:
                sys.exit(1)
            except SystemExit:
                os._exit(1)

        elif not mc.validate_directory():
            logger.warning("Faltan Recursos necesarios, por favor verifica los recursos y acepta la instalacion de recursos")
            data_widget.buttom_jugar.text = "No instalado"
            data_widget.buttom_jugar.icon = ft.icons.DISABLED_BY_DEFAULT
            data_widget.buttom_jugar.disabled = True
            self._page.dialog = data_widget.dlg_modal
            data_widget.dlg_modal.open = True
            self._page.update()
        else:
            logger.info("Recursos necesarios estan instaldos correctamente")
            data_widget.buttom_jugar.text = "Jugar"
            data_widget.buttom_jugar.icon = False
            data_widget.buttom_jugar.disabled = False
            self._page.update()
            return True

    def page_update(self):
        '''
        Actualiza la pagina web desde una funcion externa
        '''
        self._page.update()


if __name__ == "__main__":
    mc = Mc()
    data_widget = DataWidget()
    app = LauncherVentana()
    logger.info("Debug del launcher iniciado")
    ft.app(target=app, assets_dir="assets")