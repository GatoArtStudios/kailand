import os
import sys
import time
import uuid
import utils
import shutil
import zipfile
import hashlib
import requests
import threading
import subprocess
import encryption
import flet as ft
import minecraft_launcher_cunstom as minecraft_launcher_lib

class Mc:
    def __init__(self) -> None:
        '''
        Almacena todos los datos del minecraft y metodos para el mismo funcionamiento, tambien se encarga de checar la integridad de los datos al inicial el launcher
        '''
        from config import DIRECTORY_KAILAND, JAVA_PATH
        self.data_nube = {}
        self.ID = str(uuid.uuid4())
        self.url_new_vercion = None
        self.launcherVersion = "2.0.1.1"
        self.boton_jugar = "Iniciado"
        self.mc_disponible = True
        self.minecraft_directory = DIRECTORY_KAILAND
        self.options = {
            "username": None,
            "uuid": None,
            "token": "",
            "executablePath": JAVA_PATH,
            "jvmArguments": ["-Xmx5G", "-Xms2G", "-XX:+UnlockExperimentalVMOptions", "-XX:+UseG1GC", "-XX:G1NewSizePercent=20", "-XX:G1ReservePercent=20", "-XX:MaxGCPauseMillis=50", "-XX:G1HeapRegionSize=32M"],
            "launcherName": "Kailand V - Launcher",
            "gameDirectory": self.minecraft_directory,
            "customResolution": True,
            "resolutionHeight": "480",
            "resolutionWidth": "854",
            "launcherVersion": "1.0",
        }
        self.setting_progress = 0
        self.progress_time = 1
        self.archivo_kailand = os.path.join(self.minecraft_directory, "kaliand.json")
        self.archivo_mods_data = os.path.join(self.minecraft_directory, "mods_data.json")
        self.ruta_mods = os.sep.join([self.minecraft_directory, "mods"])
        self.ruta_texture_packs = os.sep.join([self.minecraft_directory, "resourcepacks"])
        self.url_base_mods = 'https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods'
        self.dependencias_mods = {}
        self.cheking()
        self.load_data_file_config()
        self.archivos_mods = []
        self.path_files_mods = []
        self.list_files_directory_mods()
        self.valor_xmx = self.ram_launcher()
        self.valor_xmx_temp = self.ram_launcher()
        self.changer_save_file_kailand()
        self.download_optional = 0
        self.anticheat()

    @utils.handle_exception('Error al conectar con el servidor, reinicie el launcher.')
    def load_data_file_config(self):
        '''
        Carga los datos del archivo mods_data.json en la siguiente ruta:
        ```
        class Mc:
            def __init__(self):
                self.data_nube = {}
        ```
        '''
        """
        Carga los datos del archivo mods_data.json en la siguiente ruta:

        Si el archivo existe, se decodifica y se actualiza `self.data_nube` con los datos.
        De lo contrario, se realiza una solicitud GET a la URL de los datos en el servidor.
        Si la solicitud es exitosa, `self.data_nube` se actualiza con los datos obtenidos.

        """
        if os.path.exists(self.archivo_mods_data):
            # Decodifica y actualiza los datos desde el archivo
            temp_data_mods = encryption.decrypt_message(self.archivo_mods_data)
            self.data_nube.update(temp_data_mods)
        else:
            # Realiza una solicitud GET a la URL de los datos en el servidor
            response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
            if response.status_code == 200:
                # Actualiza los datos desde la respuesta obtenida
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
        # Crea el directorio de Shader
        if not os.path.exists(os.path.join(self.minecraft_directory, "shaderpacks")):
            os.mkdir(os.path.join(self.minecraft_directory, "shaderpacks"))
        # Crea el directorio de Texturas
        if not os.path.exists(os.path.join(self.minecraft_directory, "resourcepacks")):
            os.mkdir(os.path.join(self.minecraft_directory, "resourcepacks"))

        # Verifica si el archivo existe
        if os.path.exists(self.archivo_kailand):
            """
            Si el archivo existe, se lee el contenido del archivo JSON y se actualiza el diccionario de la variable options con los datos obtenidos.
            El diccionario 'options' contiene las opciones de configuración del juego.
            El log se actualiza con los datos obtenidos.
            """
            from log import logger
            from config import JAVA_PATH
            # Lee el contenido del archivo JSON y actualiza el diccionario de la variable options
            data_options = encryption.decrypt_message(file=self.archivo_kailand)
            data_options['executablePath'] = JAVA_PATH
            self.options.update(data_options)
            ocult_uuid = self.options.copy()
            ocult_uuid.update({"uuid": "*************** privado **************"})
            ocult_uuid.update({"username": "*************** privado **************"})
            logger.info(ocult_uuid)

    def list_files_directory_mods(self) -> bool:
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
        self.register_dependency_mods()
        return True

    def register_dependency_mods(self):
        # Itera sobre cada item de la lista de mods disponible en el directorio de mods
        for file in os.listdir(self.ruta_mods):
            # file es igual al nombre del archivo
            # registra las dependencias de cada mod
            for x in self.data_nube['mods']:
                if x['file'] == file:
                    if len(x['dependencia']) > 0:
                        for d in x['dependencia']:
                            if d['file'] in self.dependencias_mods:
                                self.dependencias_mods.update({d['file']: self.dependencias_mods[d['file']] + 1}) # self.dependencias_mods[d['file']] += 1
                            else:
                                self.dependencias_mods.update({d['file']: 1})
            # Registra las dependencias de cada complemento
            for x in self.data_nube['complementos']:
                if x['file'] == file:
                    if len(x['dependencia']) > 0:
                        for d in x['dependencia']:
                            if d['file'] in self.dependencias_mods:
                                self.dependencias_mods.update({d['file']: self.dependencias_mods[d['file']] + 1}) # self.dependencias_mods[d['file']] += 1
                            else:
                                self.dependencias_mods.update({d['file']: 1})

    def check_dependency_mods(self, x):
        if x in self.data_nube:
            if self.data_nube[x] > 0:
                self.data_nube[x] -= 1
            else:
                self.data_nube.update({x: 0})
        else:
            return False

    def hash_file(self, path: str) -> str:
        sha256_hash = hashlib.sha256()
        with open(path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def checkin_file(self, x: dict) -> bool:
        '''
        Verifica si un archivo del apartadode mods esta instalado.
        '''
        from config import DIRECTORY_KAILAND
        if os.path.exists(os.path.join(DIRECTORY_KAILAND, 'mods', x['file'])):
            return True
        else:
            return False

    def anticheat(self):
        '''
        Anticheat de mods
        '''
        from log import logger
        
        # Carga la lista de mods validos
        list_mods = {}
        for mod in self.data_nube['mods']:
            if mod['disponible']:
                list_mods[mod['file']] = mod['hash']
                if len(mod['dependencia']) > 0:
                    for dep in mod['dependencia']:
                        if dep['disponible']:
                            list_mods[dep['file']] = dep['hash']
                            if len(dep['dependencia']) > 0:
                                for d in dep['dependencia']:
                                    if d['disponible']:
                                        list_mods[d['file']] = d['hash']
        # Cargamos la lista de complementos validos
        for mod in self.data_nube['complementos']:
            if mod['disponible']:
                list_mods[mod['file']] = mod['hash']
                if len(mod['dependencia']) > 0:
                    for dep in mod['dependencia']:
                        if dep['disponible']:
                            list_mods[dep['file']] = dep['hash']
                            if len(dep['dependencia']) > 0:
                                for d in dep['dependencia']:
                                    if d['disponible']:
                                        list_mods[d['file']] = d['hash']
        # Verfica si los mods, dependencias, complementos no han sido alterados
        for file in os.listdir(self.ruta_mods):
            hash_file = self.hash_file(os.path.join(self.ruta_mods, file))
            if file in list_mods and list_mods[file] == hash_file:
                pass
            else:
                self.eliminar_mod(os.path.join(self.ruta_mods, file), file)
                logger.warning(f'Anticheat: Mod {file} no valido, prohibido el uso de Cheats o mod no validos para kailand.')

        # Verifica si hay texture packs no validos
        for file in os.listdir(self.ruta_texture_packs):
            hash_file = self.hash_file(os.path.join(self.ruta_texture_packs, file))
            if hash_file in self.data_nube['textureBlackList']:
                os.remove(os.path.join(self.ruta_texture_packs, file))
                logger.warning(f'Anticheat: Texture pack {file} no valido, prohibido el uso de Cheats.')

        for fil in self.data_nube['mods']: # Iteramos sobre todos los mods en la base de datos
            if self.checkin_file(fil): # Verifica si el mod esta instalado
                if len(fil['dependencia']) > 0: # Verifica si hay dependencias
                    for d in fil['dependencia']: # Iteramos sobre las dependencias
                        if d['disponible']: # Verifica si la dependencia es disponible
                            if not self.checkin_file(d): # Verifica si la dependencia no esta instalada y si no esta instalada la descarga
                                logger.warning(f'La dependencia {d["name"]} no esta instalada, instalando dependencia.')
                                self.descargar_mod(d) # Descarga la dependencia

        for fil in self.data_nube['complementos']: # Iteramos sobre todos los mods en la base de datos
            if self.checkin_file(fil): # Verifica si el mod esta instalado
                if len(fil['dependencia']) > 0: # Verifica si hay dependencias
                    for d in fil['dependencia']: # Iteramos sobre las dependencias
                        if d['disponible']: # Verifica si la dependencia es disponible
                            if not self.checkin_file(d): # Verifica si la dependencia no esta instalada y si no esta instalada la descarga
                                logger.warning(f'La dependencia {d["name"]} no esta instalada, instalando dependencia.')
                                self.descargar_mod(d) # Descarga la dependencia

    def descargar_mod(self, mod: dict):
        '''
        Descarga el mod que se le pasa por la variable mod, y los descarga si es necesario y tambien sus dependencias.
        '''
        from log import logger
        destino = os.path.join(self.ruta_mods, mod['file'])
        if os.path.exists(destino):
            logger.info(f"El mod '{mod['name']}' ya está descargado.")
        else:
            logger.info(f"Descargando el mod '{mod['name']}'...")
            try:
                # -------------- Descarga el archivo ----------------
                response = requests.get(mod["url"])
                if response.status_code == 200:
                    with open(destino, 'wb') as archivo:
                        archivo.write(response.content)
                    logger.info(f"Descarga exitosa: {destino}")
                    # -------------- Verifica dependencias ---------------
                    # Verifica si hay dependencias y las descarga
                    if len(mod['dependencia']) > 0:
                        logger.info(f"Descargando dependencia: {len(mod['dependencia'])}...")
                        for dep in mod['dependencia']:
                            if dep['disponible']:
                                try:
                                    if not os.path.exists(os.path.join(self.ruta_mods, dep['file'])):
                                        response = requests.get(dep["url"])
                                        if response.status_code == 200:
                                            with open(os.path.join(self.ruta_mods, dep['file']), 'wb') as archivo:
                                                archivo.write(response.content)
                                            if dep['file'] in self.dependencias_mods:
                                                self.dependencias_mods.update({dep['file']: self.dependencias_mods[dep['file']] + 1})
                                            else:
                                                self.dependencias_mods.update({dep['file']: 1})
                                            logger.info(f"Descarga exitosa: {os.path.join(self.ruta_mods, dep['file'])}")
                                        else:
                                            logger.error(f"Error al descargar el mod '{dep['name']}'. Código de estado: {response.status_code}")
                                    else:
                                        logger.info(f"El mod '{dep['name']}' ya está descargado.")
                                except Exception as e:
                                    logger.error(f"Error al descargar el mod '{dep['name']}': {e}")
                                if len(dep['dependencia']) > 0:
                                    for d in dep['dependencia']:
                                        if d['disponible']:
                                            try:
                                                if not os.path.exists(os.path.join(self.ruta_mods, d['file'])):
                                                    response = requests.get(d["url"])
                                                    if response.status_code == 200:
                                                        with open(os.path.join(self.ruta_mods, d['file']), 'wb') as archivo:
                                                            archivo.write(response.content)
                                                        if d['file'] in self.dependencias_mods:
                                                            self.dependencias_mods.update({d['file']: self.dependencias_mods[d['file']] + 1})
                                                        else:
                                                            self.dependencias_mods.update({d['file']: 1})
                                                        logger.info(f"Descarga exitosa: {os.path.join(self.ruta_mods, d['file'])}")
                                                    else:
                                                        logger.error(f"Error al descargar el mod '{d['name']}'. Código de estado: {response.status_code}")
                                                else:
                                                    logger.info(f"El mod '{d['name']}' ya está descargado.")
                                            except Exception as e:
                                                logger.error(f"Error al descargar el mod '{d['name']}': {e}")
                else:
                    logger.error(f"Error al descargar el mod '{mod['name']}'. Código de estado: {response.status_code}")
            except Exception as e:
                logger.error(f"Error durante la descarga del mod '{mod['name']}': {e}")

    def download_comple(self, e: ft.ElevatedButton, x):
        '''
        Descarga los complementos.

        Args:
            e (Evento): El evento que se disparó.
            x (Objeto): El objeto asociado al complemento.
        '''
        from layout import data_widget
        # Deshabilita el control para evitar errores
        e.control.disabled = True
        # Agrega el proceso a la lista
        mc.download_optional += 1
        # Muestra el progreso de la configuración del complemento
        data_widget.progressbar_install.tooltip = f"Configurando {x['name']}..."
        data_widget.progressbar_install.value = None
        data_widget.progressbar_install.visible = True
        # Deshabilita el botón para evitar errores
        data_widget.buttom_jugar.disabled = True
        data_widget.buttom_jugar.text = 'Configurando'
        e.page.update()
        if e.data == 'true':
            # Si el evento es verdadero, descargar el complemento
            self.descargar_mod(x)
            # Disminuye el contador de descargas opcionales
            mc.download_optional -= 1
            if mc.download_optional == 0:
                # Si no hay más descargas opcionales, oculta la pantalla de progreso y habilita el botón
                data_widget.progressbar_install.visible = False
                data_widget.buttom_jugar.disabled = False
                data_widget.buttom_jugar.text = 'Jugar'
            # Habilita el control y actualiza la página
            e.control.disabled = False
            e.page.update()
        elif e.data == 'false':
            # Si el evento es falso, elimina el complemento
            self.eliminar_mod(os.path.join(self.ruta_mods, x['file']), x['file'])
            if len(x['dependencia']) > 0:
                    for d in x['dependencia']:
                        self.eliminar_mod(os.path.join(self.ruta_mods, d['file']), d['file'])
                        if len(d['dependencia']) > 0:
                            for dd in d['dependencia']:
                                self.eliminar_mod(os.path.join(self.ruta_mods, dd['file']), dd['file'])
            # Disminuye el contador de descargas opcionales
            mc.download_optional -= 1
            if mc.download_optional == 0:
                # Si no hay más descargas opcionales, oculta la pantalla de progreso y habilita el botón
                data_widget.progressbar_install.visible = False
                data_widget.buttom_jugar.disabled = False
                data_widget.buttom_jugar.text = 'Jugar'
            # Habilita el control y actualiza la página
            e.control.disabled = False
            e.page.update()

    def eliminar_mod(self, archivo, file):
        '''
        Elimina mods, pasandole como argumento la ruta del archivo a remover
        '''
        from log import logger
        try:
            if file in self.dependencias_mods:
                if self.dependencias_mods[file] == 1:
                    os.remove(archivo)
                    logger.info(f"Mod eliminado: {file}")
                    self.dependencias_mods.pop(file)
                elif self.dependencias_mods[file] > 1:
                    self.dependencias_mods[file] -= 1
                    logger.info(f"Dependencia requerida por otro mod: {file}")
            else:
                os.remove(archivo)
                logger.info(f"Mod eliminado: {file}")
        except Exception as e:
            logger.error(f"Error al eliminar el mod '{file}': {e}")

    def comprobar_mods(self):
        '''
        Comprueva si los mods estan de acuerdo a al archivo de configuracion
        '''
        from layout import data_widget
        # ----------------------- Cargar datos de la nube -----------------------
        self.consulta_nube(bt_play=True)
        # ----------------------- Descargar mods y complementos activos -----------------------
        for mod in self.data_nube['mods']:
            if mod['disponible']:
                self.descargar_mod(mod)
            elif mod['file'] in self.archivos_mods:
                self.eliminar_mod(os.path.join(self.ruta_mods, mod['file']), mod['file'])
                if len(mod['dependencia']) > 0:
                    for d in mod['dependencia']:
                        self.eliminar_mod(os.path.join(self.ruta_mods, d['file']), d['file'])
                        if len(d['dependencia']) > 0:
                            for dd in d['dependencia']:
                                self.eliminar_mod(os.path.join(self.ruta_mods, dd['file']), dd['file'])
        for dep in self.data_nube['complementos']:
            if dep['active'] and dep['disponible']:
                self.descargar_mod(dep)
        # ----------------------- Ejecuta el anticheat para limpiar mods no deceados -----------------------
        self.anticheat()
        # ----------------------- Actualiza las reglas -----------------------
        data_widget.update_reglas_from_ui()
        return True

    def changer_save_file_kailand(self):
        '''
        Guardar datos en un archivo JSON
        '''
        from log import logger
        encryption.encrypt_message(self.options, self.archivo_kailand)
        logger.info("Guardo las optiones en el archivo de configuracion")

    @utils.handle_exception('Error al consultar al servidor, reinicia el launcher y comprueba tu conexion a internet.')
    def consulta_nube(self, bt_play: bool = False) -> bool:
        """
        Consulta el archivo de configuración en el servidor.

        Args:
            bt_play (bool): Indica si se debe actualizar la configuración si es necesario.

        Retorna:
            bool: True si la configuración coincide con la del servidor, False si no coincide o si hay un error de conexión.
        """
        response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")

        temp_json = response.json()
        if os.path.exists(self.archivo_mods_data):
            if temp_json["configVersion"] != self.data_nube["configVersion"]:
                if bt_play:
                    encryption.encrypt_message(temp_json, self.archivo_mods_data)
                    self.data_nube.update(temp_json)
                    return True
                return False
        else:
            self.data_nube.update(temp_json)
            encryption.encrypt_message(self.data_nube, self.archivo_mods_data)
        return True

    def validate_directory(self):
        """
        Valida si los directorios y el minecraft están instalados.

        Retorna True si los directorios y el minecraft están instalados,
        False en caso contrario.
        """
        # Verifica si el directorio principal de Minecraft existe.
        if os.path.exists(self.minecraft_directory):
            # Verifica que todos los subdirectorios necesarios estén presentes.
            if all([os.path.exists(os.path.join(self.minecraft_directory, directory)) for directory in [
                    "mods", "assets", "libraries", "runtime", "versions",
                    "shaderpacks", "resourcepacks",
                    "versions/1.19.2",
                    "versions/1.19.2-forge-43.4.0",
                ]
            ]):
                # Verifica que la versión de Minecraft sea válida.
                if minecraft_launcher_lib.utils.is_version_valid('1.19.2', self.minecraft_directory):
                    # Verifica que la configuración de la nube sea válida.
                    if self.consulta_nube():
                        return True
                    else:
                        return False
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
            from log import logger
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
        from log import logger
        from layout import data_widget
        from ui import app
        if minecraft_launcher_lib.utils.is_minecraft_installed(self.minecraft_directory):
            from config import SYSTEM
            logger.info("Minecraft si esta instalado")
            data_widget.animate_buttom(e)
            # Guardar datos en un archivo JSON
            encryption.encrypt_message(self.options, self.archivo_kailand)
            # Obtiene el comando para ejecutar Minecraft
            minecraft_command = minecraft_launcher_lib.command.get_minecraft_command("1.19.2-forge-43.4.0", self.minecraft_directory, self.options)
            # Agrega datos al logger
            logger.info("Ejecutando Minecraft")
            e.control.bgcolor = ft.colors.with_opacity(0.1, "white")
            e.control.icon = ft.icons.PLAY_CIRCLE
            e.control.color = ft.colors.with_opacity(0.5, "white")
            e.control.text = "Jugando"
            e.control.disabled = True
            e.control.update()
            # Ejecuta y alamcena el debug de minecraft java
            if SYSTEM == "Windows":
                startinfo = subprocess.STARTUPINFO() # agregamos el startupinfo para que no se muestre la terminal
                startinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                debug_minecraft_launch = subprocess.Popen(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW  | subprocess.DETACHED_PROCESS, text=True, startupinfo=startinfo)
                # Da notificación de que el launcher se ha cerrado y el juego a iniciado
                logger.warning('Cerrando launcher, el juego iniciara en unos segundos...')
                utils.ms_notify(message='Juego iniciado, el launcher se cerrara.')
                time.sleep(2)
                self.anticheat() # Ejecutamos el AntiCheat antes de que el juego inicie para soluciona el bug de que se podian colocar mods antes de iniciar el juego
                utils.exit_app()
            elif SYSTEM == "Linux":
                debug_minecraft_launch = subprocess.Popen(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                # Da notificación de que el launcher se ha cerrado y el juego a iniciado
                logger.warning('Cerrando launcher, el juego iniciara en unos segundos...')
                time.sleep(2)
                self.anticheat() # Ejecutamos el AntiCheat antes de que el juego inicie para soluciona el bug de que se podian colocar mods antes de iniciar el juego
                utils.exit_app()
            else:
                debug_minecraft_launch = subprocess.Popen(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                # Da notificación de que el launcher se ha cerrado y el juego a iniciado
                logger.warning('Cerrando launcher, el juego iniciara en unos segundos...')
                time.sleep(2)
                self.anticheat() # Ejecutamos el AntiCheat antes de que el juego inicie para soluciona el bug de que se podian colocar mods antes de iniciar el juego
                utils.exit_app()

            # Agrega mensaje debug al logger
            logger.warning("Minecraft Detenido...")
            e.control.bgcolor = ft.colors.with_opacity(1, '#00bd1c')
            e.control.icon = None
            e.control.color = "black"
            e.control.text = "Jugar"
            e.control.disabled = False
            e.control.update()
        else:
            logger.warning("Minecraft no instalado")

    @utils.handle_exception('Error al comprovar actualizaciones, reinicie el laucher.')
    def check_update_launcher(self):
        '''
        Chequea actualizaciones en el servidor y retorna el estado en boleano

        Retorna True si hay una actualizacion disponible y False si no lo hay

        Comprueba si la version del launcher actual es igual a la version del launcher en el servidor.
        Si son diferentes retorna True, si son iguales retorna False.
        '''
        response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
        if response.status_code == 200:
            # Parsea el json obtenido
            __temp_data_get = response.json()
            if not __temp_data_get["launcherVersion"] == self.launcherVersion: # Si la vercion no es la misma es valido
                # Si hay una actualizacion disponible retorna True
                return True
            else: # Si la vercion es la misma ignora el resto
                # No hay actualizaciones disponibles retorna False
                return False
        else:
            # Faltó obtener la respuesta del servidor retorna False
            return False

    def download_and_unzip(self, config):
        from log import logger
        from config import DIRECTORY_KAILAND
        directory = os.path.join(DIRECTORY_KAILAND, 'config', config['directory'])
        name_zip = config['file']
        try:
            logger.info(f"Descargando configuración de {config['name']}")
            response = requests.get(config['url'])
            if response.status_code == 200:
                with open(name_zip, 'wb') as f:
                    f.write(response.content)

                logger.info(f"Descomprimiendo configuración de {config['name']}")
                if not os.path.exists(directory):
                    logger.info(f"Creando directorio {directory}")
                    os.makedirs(directory)

                with zipfile.ZipFile(name_zip, 'r') as zip_ref:
                    zip_ref.extractall(directory)

                os.remove(name_zip)
                logger.info(f"Se ha descargado la configuración de {config['name']} y se ha descomprimido correctamente")
            else:
                logger.error(f"Error al descargar configuración de {config['name']}: {e}")
        except Exception as e:
            logger.error(f"Error al descargar configuración de {config['name']}: {e}")

    def install_minecraft(self, e):
        '''
        Instala el minecraft
        '''
        from log import logger
        from layout import data_widget
        from config import DIRECTORY_KAILAND, JAVA_PATH
        from ui import app

        logger.info("Comprobando recursos instalados, estos puede demorar.")
        data_widget.progressbar_install.value = 0.05
        data_widget.progressbar_install.tooltip = 'Instalando configuraciones: 5%'
        app.page_update()
        # ----------------- Descarga y descomprime las configuraciones -----------------
        responde = self.data_nube
        try:
            response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
            if response.status_code == 200:
                response = response.json()
            else:
                response = self.data_nube
        except Exception as e:
            response = self.data_nube
        for config in self.data_nube['config']:
            if config['disponible']:
                if not os.path.exists(os.path.join(DIRECTORY_KAILAND, 'config', config['directory'])):
                    self.download_and_unzip(config)
                else:
                    try:
                        shutil.rmtree(os.path.join(DIRECTORY_KAILAND, 'config', config['directory']))
                        logger.info(f"Se ha eliminado la configuración de {config['name']}")
                        self.download_and_unzip(config)
                    except Exception as e:
                        logger.error(f"Error al eliminar la configuración de {config['name']}: {e}")
            else:
                try:
                    shutil.rmtree(os.path.join(DIRECTORY_KAILAND, 'config', config['directory']))
                    logger.info(f"Se ha eliminado la configuración de {config['name']}")
                except Exception as e:
                    logger.error(f"Error al eliminar la configuración de {config['name']}: {e}")
        data_widget.progressbar_install.value = 0.1
        data_widget.progressbar_install.tooltip = '10%'
        app.page_update()
        # ----------------- Carga de mods -----------------
        data_widget.div_mods = ft.Container(
                    content=ft.Tabs(
                        selected_index=1,
                        animation_duration=300,
                        tabs=[
                            ft.Tab(
                                text="Predeterminados",
                                content=ft.GridView(
                                    [
                                        ft.Text('Durante las descarga de los recursos no puedes editar este apartado')
                                    ],
                                    runs_count=3,
                                    max_extent=400,
                                    child_aspect_ratio=1.5,
                                )
                            ),
                            ft.Tab(
                                text="Recomendados",
                                content=ft.GridView(
                                    [
                                        ft.Text('Durante las descarga de los recursos no puedes editar este apartado')
                                    ],
                                    runs_count=3,
                                    max_extent=400,
                                    child_aspect_ratio=1.5,
                                )
                            )
                        ]
                    )
                    ,
                    height=630,
                    width=950,
                )
        # Actualiza la pagina web para mostrar los cambios anteriores
        app.page_update()
        # realizamos una comprobacion de los mods, para saber si estan todos instalados
        logger.info(f'Comprovando si los mods y dependecias estan instalados.')

        data_widget.progressbar_install.value = 0.25
        data_widget.progressbar_install.tooltip = 'Comprobando mods: 25%'
        app.page_update()

        # ------------------ Comprobacion de mods -----------------
        if self.comprobar_mods():
                logger.info("Todos los mods estan instalados correctamente")
                # Actualizamos el UI para mostrar los cambios realizados
                data_widget.progressbar_install.value = 0.3
                data_widget.progressbar_install.tooltip = '30%'
                app.page_update()

        data_widget.progressbar_install.value = 0.35
        data_widget.progressbar_install.tooltip = 'Validando directorios: 35%'
        app.page_update()
        if self.validate_directory():
            logger.info("Toda la estructura de directorios esta completa")
            data_widget.progressbar_install.value = 1.0
            data_widget.progressbar_install.tooltip = 'Instalacion terminada: 100%'
            data_widget.progressbar_install.visible = False
            app.page_update()
        else:
            logger.warning("Faltan algunos recursos necesarios")
            # Ejemplo de funciones de callback
            def set_status(text: str):
                logger.info(f"Estado: {text}")

            def set_progress(value: int):
                self.setting_progress = round((value / self.progress_time) * 100, 1)
                if self.setting_progress == 100.0:
                    logger.info(f"Progreso: 100%")
                    return
                elif self.setting_progress == 90.0:
                    logger.info(f"Progreso: 90%")
                    return
                elif self.setting_progress == 80.0:
                    logger.info(f"Progreso: 80%")
                    return
                elif self.setting_progress == 70.0:
                    logger.info(f"Progreso: 70%")
                    return
                elif self.setting_progress == 60.0:
                    logger.info(f"Progreso: 60%")
                    return
                elif self.setting_progress == 50.0:
                    logger.info(f"Progreso: 50%")
                    return
                elif self.setting_progress == 40.0:
                    logger.info(f"Progreso: 40%")
                    return
                elif self.setting_progress == 30.0:
                    logger.info(f"Progreso: 30%")
                    return
                elif self.setting_progress == 20.0:
                    logger.info(f"Progreso: 20%")
                    return
                elif self.setting_progress == 10.0:
                    logger.info(f"Progreso: 10%")
                    return
                elif self.setting_progress == 0.0:
                    logger.info(f"Progreso: 0%")
                    return

            def set_max(value: int):
                self.progress_time = value

            data_widget.progressbar_install.value = 0.4
            data_widget.progressbar_install.tooltip = 'Creando estructura de directorios: 40%'
            app.page_update()
            self.create_directory()
            data_widget.progressbar_install.value = 0.5
            data_widget.progressbar_install.tooltip = 'Consultando servidor: 50%'
            app.page_update()
            self.consulta_nube(bt_play=True)
            data_widget.progressbar_install.value = 0.6
            data_widget.progressbar_install.tooltip = 'Verificando Instalaciones de Minecraft: 60%'
            app.page_update()
            if not os.path.exists(os.path.join(self.minecraft_directory, "versions", "1.19.2")):
                logger.info("Instalando Minecraft vanila, esto puede tardar unos minutos.")
                minecraft_launcher_lib.install.install_minecraft_version("1.19.2", self.minecraft_directory, callback={'setStatus': set_status, 'setProgress': set_progress, 'setMax': set_max})
                data_widget.progressbar_install.value = 0.8
                data_widget.progressbar_install.tooltip = 'Minecraft instalado: 80%'
                from config import JAVA_PATH, get_path_java
                JAVA_PATH = get_path_java()
                self.options['executablePath'] = JAVA_PATH
                from layout import data_widget
                data_widget.java_path.value = JAVA_PATH
                app.page_update()
                logger.info(f'Java path configurado: {JAVA_PATH}')
                logger.info("Minecraft instalado correctamente")
            if not os.path.exists(os.path.join(self.minecraft_directory, "versions", "1.19.2-forge-43.4.0")):
                logger.info("Instalando Forge")
                minecraft_launcher_lib.forge.install_forge_version("1.19.2-43.4.0", self.minecraft_directory, callback={'setStatus': set_status, 'setProgress': set_progress, 'setMax': set_max}, java=None if JAVA_PATH == 'java' else JAVA_PATH)
                data_widget.progressbar_install.value = 1.0
                data_widget.progressbar_install.tooltip = 'Forge instalado: 100%'
                data_widget.progressbar_install.visible = False
                app.page_update()
                logger.info("Forge Instalado")

        # Actualiza la pagina con los cambios
        data_widget.div_mods = ft.Container(
            content=ft.Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        text="Predeterminados",
                        content=ft.GridView(
                            [
                                data_widget.contMods(x['name'], x['descripcion'], x['doct'] if x['doct'] else 'http://example.com', x) for x in self.data_nube['complementos'] if x['active']
                            ],
                            runs_count=3,
                            max_extent=400,
                            child_aspect_ratio=1.5,
                        )
                    ),
                    ft.Tab(
                        text="Recomendados",
                        content=ft.GridView(
                            [
                                data_widget.contMods(x['name'], x['descripcion'], x['doct'] if x['doct'] else 'http://example.com', x) for x in self.data_nube['complementos'] if not x['active']
                            ],
                            runs_count=3,
                            max_extent=400,
                            child_aspect_ratio=1.5,
                        )
                    )
                ]
            )
            ,
            height=630,
            width=950,
        )
        data_widget.buttom_jugar.disabled = False
        data_widget.buttom_jugar.text = "Jugar"
        data_widget.buttom_jugar.icon = False
        data_widget.progressbar_install.visible = False
        app.page_update()
        data_widget.open_dlg(e)

mc = Mc()