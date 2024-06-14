import os
import uuid
import requests
import flet as ft
import subprocess
import minecraft_launcher_lib
import encryption
import threading

class Mc:
    def __init__(self) -> None:
        '''
        Almacena todos los datos del minecraft y metodos para el mismo funcionamiento, tambien se encarga de checar la integridad de los datos al inicial el launcher
        '''
        from config import DIRECTORY_KAILAND
        self.data_nube = {}
        self.ID = uuid.uuid4().hex
        self.url_new_vercion = None
        self.launcherVersion = "1.0.24.0"
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
        return True

    def check_dependency_mods(self, x):
        if x in self.data_nube:
            if self.data_nube[x] > 0:
                self.data_nube[x] -= 1
            else:
                self.data_nube.update({x: 0})
        else:
            return False

    def descargar_mod(self, mod):
        '''
        Descarga los mods y los almacena en el directorio de mods
        '''
        from log import logger
        # Verifica si hay dependencias
        def descargar_dependencias(x):
            if len(x['dependencia']) > 0:
                # if x['file'] in self.data_nube:
                #     num = self.data_nube[x['file']] += 1
                #     self.data_nube.update({x['file']: 1})
                logger.info(f"Descargando dependencia: {len(x['dependencia'])}...")
                for dep in x['dependencia']:
                    self.descargar_mod(dep)
                    if dep['dependencia']:
                        if dep['dependencia'] > 0:
                            for d in dep['dependencia']:
                                self.descargar_mod(d)
        destino = os.path.join(self.ruta_mods, mod['file'])
        if os.path.exists(destino):
            logger.info(f"El mod '{mod['name']}' ya está descargado.")
            descargar_dependencias(mod)
        else:
            logger.info(f"Descargando el mod '{mod['name']}'...")
            try:
                response = requests.get(mod["url"])
                if response.status_code == 200:
                    with open(destino, 'wb') as archivo:
                        archivo.write(response.content)
                    logger.info(f"Descarga exitosa: {destino}")
                    descargar_dependencias(mod)
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
            self.eliminar_mod(os.path.join(self.ruta_mods, x['file']))
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

    def eliminar_mod(self, archivo):
        '''
        Elimina mods, pasandole como argumento la ruta del archivo a remover
        '''
        from log import logger
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
                if mod['dependencia'] > 0:
                    for d in mod['dependencia']:
                        self.eliminar_mod(os.path.join(self.ruta_mods, d['file']))
                        if d['dependencia'] > 0:
                            for dd in d['dependencia']:
                                self.eliminar_mod(os.path.join(self.ruta_mods, dd['file']))
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
            # Ejecuta y alamcena el debug de minecraft java
            if SYSTEM == "Windows":
                debug_minecraft_launch = subprocess.run(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, creationflags=subprocess.CREATE_NO_WINDOW)
            elif SYSTEM == "Linux":
                debug_minecraft_launch = subprocess.run(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            else:
                debug_minecraft_launch = subprocess.run(minecraft_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        from log import logger
        from layout import data_widget
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

mc = Mc()