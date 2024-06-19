import os
import uuid
import shutil
import zipfile
import requests
import subprocess
import encryption
import flet as ft
import minecraft_launcher_lib

class Mc:
    def __init__(self) -> None:
        '''
        Almacena todos los datos del minecraft y metodos para el mismo funcionamiento, tambien se encarga de checar la integridad de los datos al inicial el launcher
        '''
        from config import DIRECTORY_KAILAND
        self.data_nube = {}
        self.ID = uuid.uuid4().hex
        self.url_new_vercion = None
        self.launcherVersion = "1.0.25.0"
        self.boton_jugar = "Iniciado"
        self.mc_disponible = True
        self.minecraft_directory = DIRECTORY_KAILAND
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
        self.archivo_mods_data = os.path.join(self.minecraft_directory, "mods_data.json")
        self.ruta_mods = os.path.join(self.minecraft_directory, "mods")
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

    def load_data_file_config(self):
        '''
        Carga los datos del archivo mods_data.json en la siguiente ruta:
        ```
        class Mc:
            def __init__(self):
                self.data_nube = {}
        ```
        '''
        if os.path.exists(self.archivo_mods_data):
            temp_data_mods = encryption.decrypt_message(self.archivo_mods_data)
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
            from log import logger
            # Lee el contenido del archivo JSON y actualiza el diccionario de la variable options
            data_options = encryption.decrypt_message(file=self.archivo_kailand)
            self.options.update(data_options)
            logger.info(self.options)

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

    def anticheat(self):
        '''
        Anticheat de mods
        '''
        from log import logger
        list_avalid_mods = []
        for mod in self.data_nube['mods']:
            if mod['disponible']:
                list_avalid_mods.append(mod['file'])
                if len(mod['dependencia']) > 0:
                    for dep in mod['dependencia']:
                        if dep['disponible']:
                            list_avalid_mods.append(dep['file'])
                            if len(dep['dependencia']) > 0:
                                for d in dep['dependencia']:
                                    if d['disponible']:
                                        list_avalid_mods.append(d['file'])
        for dep in self.data_nube['complementos']:
            if dep['disponible']:
                list_avalid_mods.append(dep['file'])
                if len(dep['dependencia']) > 0:
                    for d in dep['dependencia']:
                        if d['disponible']:
                            list_avalid_mods.append(d['file'])
                            if len(d['dependencia']) > 0:
                                for dd in d['dependencia']:
                                    if dd['disponible']:
                                        list_avalid_mods.append(dd['file'])
        for file in os.listdir(self.ruta_mods):
            if file not in list_avalid_mods:
                self.eliminar_mod(os.path.join(self.ruta_mods, file), file)
                logger.warning(f"Se elimino el mod '{file}' por no estar disponible. (No puedes usar mods/archivos externos a kailand)")

    def descargar_mod(self, mod):
        '''
        Descarga los mods y los almacena en el directorio de mods
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

    def download_comple(self, e, x):
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
        e.page.splash = ft.ProgressBar(tooltip=f"Configurando {x['name']}...", height=5)
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
                e.page.splash = None
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
                e.page.splash = None
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
        return True

    def changer_save_file_kailand(self):
        '''
        Guardar datos en un archivo JSON
        '''
        from log import logger
        encryption.encrypt_message(self.options, self.archivo_kailand)
        logger.info("Guardo las optiones en el archivo de configuracion")

    def consulta_nube(self, bt_play = False):
        '''
        Consulta el archivo de configuracon en el servidor'
        '''
        response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json")
        if response.status_code == 200:
            temp_json = response.json()
            if os.path.exists(self.archivo_mods_data):
                if temp_json["configVersion"] == self.data_nube["configVersion"]:
                    return True
                else:
                    if bt_play:
                        encryption.encrypt_message(temp_json, self.archivo_mods_data)
                        self.data_nube.update(temp_json)
                        return True
                    else:
                        return False

            else:
                self.data_nube.update(response.json())
                encryption.encrypt_message(self.data_nube, self.archivo_mods_data)
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
        if minecraft_launcher_lib.utils.is_minecraft_installed(self.minecraft_directory):
            from config import SYSTEM
            logger.info("Minecraft si esta instalado")
            data_widget.animate_buttom(e)
            # Guardar datos en un archivo JSON
            encryption.encrypt_message(self.options, self.archivo_kailand)
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
            self.anticheat()
            # Ejecuta y alamcena el debug de minecraft java
            if SYSTEM == "Windows":
                debug_minecraft_launch = subprocess.Popen(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW, text=True)
                while True:
                    output = debug_minecraft_launch.stdout.readline()
                    if output == '' and debug_minecraft_launch.poll() is not None:
                        break
                    if output:
                        if 'thread/INFO' in output or '/INFO' in output:
                            logger.info(output.strip())
                        elif 'thread/WARN' in output or '/WARN' in output:
                            logger.warning(output.strip())
                        elif 'thread/ERROR' in output or '/ERROR' in output:
                            logger.error(output.strip())
                        else:
                            logger.info(output.strip())
            elif SYSTEM == "Linux":
                debug_minecraft_launch = subprocess.Popen(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                while True:
                    output = debug_minecraft_launch.stdout.readline()
                    if output == '' and debug_minecraft_launch.poll() is not None:
                        break
                    if output:
                        if 'thread/INFO' in output or '/INFO' in output:
                            logger.info(output.strip())
                        elif 'thread/WARN' in output or '/WARN' in output:
                            logger.warning(output.strip())
                        elif 'thread/ERROR' in output or '/ERROR' in output:
                            logger.error(output.strip())
                        else:
                            logger.info(output.strip())
            else:
                debug_minecraft_launch = subprocess.Popen(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                while True:
                    output = debug_minecraft_launch.stdout.readline()
                    if output == '' and debug_minecraft_launch.poll() is not None:
                        break
                    if output:
                        if 'thread/INFO' in output or '/INFO' in output:
                            logger.info(output.strip())
                        elif 'thread/WARN' in output or '/WARN' in output:
                            logger.warning(output.strip())
                        elif 'thread/ERROR' in output or '/ERROR' in output:
                            logger.error(output.strip())
                        else:
                            logger.info(output.strip())

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
                    os.mkdir(directory)

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
        from config import DIRECTORY_KAILAND
        logger.info("Comprobando recursos")
        for config in self.data_nube['config']:
            if config['disponible']:
                if not os.path.exists(os.path.join(DIRECTORY_KAILAND, 'config', config['directory'])):
                    self.download_and_unzip(config)
            else:
                try:
                    shutil.rmtree(os.path.join(DIRECTORY_KAILAND, 'config', config['directory']))
                    logger.info(f"Se ha eliminado la configuración de {config['name']}")
                except Exception as e:
                    logger.error(f"Error al eliminar la configuración de {config['name']}: {e}")

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
        e.page.update()
        if self.comprobar_mods():
                logger.info("Todos los mods estan")
                data_widget.buttom_jugar.disabled = False
                data_widget.buttom_jugar.text = "Jugar"
                data_widget.buttom_jugar.icon = False
                e.page.splash = None
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
                e.page.update()
                data_widget.open_dlg(e)
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
                e.page.update()
                data_widget.open_dlg(e)

mc = Mc()