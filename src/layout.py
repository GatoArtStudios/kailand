import os
import sys
import json
import time
import utils
import requests
import threading
import flet as ft
import webbrowser
import memory

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
        from game import mc
        from log import log_console

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
        self.console_log = ft.Column(scroll=ft.ScrollMode.AUTO, controls=log_console, spacing=0)
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
            title=ft.Text("¿Quieres instalar los recursos necesarios para Kailand V?"),
            content=ft.Text("Si no acepta la instalacion de recursos no podras jugar. \nLa instalacion dura unos cuantos minutos, puedes ver los avances de la instalacion o comprobacion en la consola"),
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
        self.text_p = ft.TextField(label="Usuario (Offline)", label_style=ft.TextStyle(color="White"), hint_text="Coloca tu usuario y guarda de nuevo", hint_style=ft.TextStyle(color="white"), border_color="white", disabled=[True if not mc.options["username"] else False][0], color="white", bgcolor=ft.colors.with_opacity(0.2, "black"), focused_color="white", value=[None if not mc.options["username"] else mc.options["username"]][0])
        self.input_offline_name = ft.Container(content=self.text_p)
        self.text_reglas = self.consulta_reglas()
        self.text_reglas_list = self.text_reglas.split("\n")
        self.java_info = ft.FilePicker(on_result= self.result_java_path)
        self.info_execute_java = self.data_java_execute()
        self.text_save_setting = ft.Text(top=260, color="white")
        self.t = ft.Text(color="white")
        self.buttom_save = ft.ElevatedButton(text="Guardar", on_click=lambda e: (self.save_info(e), self.animate_buttom(e)), color="white", bgcolor=ft.colors.with_opacity(0.2, "white"), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.buttom_save_setting = ft.ElevatedButton(text="Guardar", on_click=lambda e: (self.save_setting(e), self.animate_buttom(e)), color="white", bgcolor=ft.colors.with_opacity(0.2, "white"), top=290, animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), scale=ft.transform.Scale(1))
        self.type_login = ft.Dropdown(label="Tipo de cuenta", label_style=ft.TextStyle(color="white"), hint_text="Seleccione el tipo", hint_style=ft.TextStyle(color="white"), options=[ft.dropdown.Option("Offline"), ft.dropdown.Option("(Online) Microsoft")], border_color="white", width=300, on_change=self.save_info, color="white", bgcolor="black", value=[None if not mc.options["username"] else "Offline"][0])
        self.select_bar_ram = ft.Slider(min=2, max=memory.memory_total(), divisions=memory.memory_divide(), label="{value}Gb", value=mc.valor_xmx, on_change=lambda e: self.change_ram_text(e, self.text_ram), width=620)
        self.java_path = ft.TextField(label="Ejecutable de Java", read_only=True, border_color="white", width=500, value='Por Defecto' if mc.options['executablePath'] == 'java' else mc.options['executablePath'], color="white")
        self.buttom_change_java = ft.ElevatedButton(
            text="Cambiar",
            on_click=lambda _: (self.java_info.pick_files(allowed_extensions=["exe"], initial_directory="C:\\Program Files\\Java", dialog_title="Seleccione el archivo java.exe o javaw.exe"), self.animate_buttom(e=_)),
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
                                        url="https://www.kailand.es/",
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
                                        content=ft.Text("GatoArtStudio", italic=True),
                                        url="https://linktr.ee/gatoartstudio",
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
                    ft.Text("Reglas de Kailand", color="white", size=50, weight=ft.FontWeight.W_900, selectable=True, font_family='Minecraft'),
                    ft.Container(
                        content=ft.Column(
                            [ft.Container(content=ft.Text(regla, font_family='FiraCode'), padding=10, border_radius=5, bgcolor=ft.colors.with_opacity(0.3, "black"), width=900, scale=ft.transform.Scale(1), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), on_hover=lambda e: self.animation_scale_zoom(e)) for regla in self.text_reglas_list],
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
            content=ft.Tabs(
                selected_index=1,
                animation_duration=300,
                tabs=[
                    ft.Tab(
                        text="Predeterminados",
                        content=ft.GridView(
                            [
                                self.contMods(x['name'], x['descripcion'], x['doct'] if x['doct'] else 'http://example.com', x) for x in mc.data_nube['complementos'] if x['active']
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
                                self.contMods(x['name'], x['descripcion'], x['doct'] if x['doct'] else 'http://example.com', x) for x in mc.data_nube['complementos'] if not x['active']
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
        self.progressbar_install = ft.ProgressBar(tooltip="Instalando recursos necesarios...", height = 5 , value=None, color='white', bgcolor='black', visible=False, border_radius=5)

    def contMods(self, titulo = 'Sin datos', descripcion = 'Sin datos', url = 'http://example.com', x = None, active = False):
        '''
        Crea el contendor que contendra la informacion de cada mod complementario.
        '''
        from game import mc
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
            padding=10,
        )

    def update_reglas_from_ui(self):
        from game import mc
        if mc.data_nube['reglas']:
            self.text_reglas_list = mc.data_nube['reglas'].split('\n')
            self.reglas_widget = ft.Container(
                content=ft.Column([
                        ft.Text("Reglas de Kailand", color="white", size=50, weight=ft.FontWeight.W_900, selectable=True, font_family='Minecraft'),
                        ft.Container(
                            content=ft.Column(
                                [ft.Container(content=ft.Text(regla, font_family='FiraCode'), padding=10, border_radius=5, bgcolor=ft.colors.with_opacity(0.3, "black"), width=900, scale=ft.transform.Scale(1), animate_scale=ft.animation.Animation(duration=400, curve="bounceout"), on_hover=lambda e: self.animation_scale_zoom(e)) for regla in self.text_reglas_list],
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

    def close_launcher_update(self, e):
        '''
        Cierra el launcher / programa
        '''
        from game import mc
        webbrowser.open(mc.url_new_vercion)
        e.page.window_destroy()
        time.sleep(3)
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)
        sys.exit(0)

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
        from game import mc
        from log import logger
        self.animate_buttom(e)
        folder = os.path.join(mc.minecraft_directory, "mods")
        if os.path.exists(os.path.join(mc.minecraft_directory, "mods")):
            logger.info(folder)
            import subprocess
            if sys.platform.startswith('linux'):
                subprocess.call(["xdg-open", folder])
            else:
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
        from game import mc
        from log import logger
        self.animate_buttom(e)
        folder = os.path.join(mc.minecraft_directory, "resourcepacks")
        if os.path.exists(os.path.join(mc.minecraft_directory, "resourcepacks")):
            logger.info(folder)
            import subprocess
            if sys.platform.startswith('linux'):
                subprocess.call(["xdg-open", folder])
            else:
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
        from game import mc
        from log import logger
        self.animate_buttom(e)
        folder = os.path.join(mc.minecraft_directory, "shaderpacks")
        if os.path.exists(os.path.join(mc.minecraft_directory, "shaderpacks")):
            logger.info(folder)
            import subprocess
            if sys.platform.startswith('linux'):
                subprocess.call(["xdg-open", folder])
            else:
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
        from ui import app
        e.page.dialog = self.dlg
        self.dlg.open = True
        data_widget.progressbar_install.visible = False
        app.page_update()

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
        from game import mc
        self.progressbar_install.visible = True
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
        Funcion que se ejecuta al precionar el boton "Guardar" en perfil
        '''
        from game import mc
        from encryption import encrypt_message, create_jwt
        # Verificamos si a selecionado un tipo de cuenta para su perfil de mc
        if not self.type_login.value:
            self.t.value = "Por favor seleccione un tipo de cuenta"
            e.page.update()
        else:
            # Este bloque se ejecuta si a elegido algun tipo de cuenta disponible
            if self.type_login.value == "Offline":
                # SI elegio Offline entonces guardara los datos para un usuario offline
                self.text_p.disabled = False
                self.buttom_login.disabled = True
                self.buttom_save.disabled = True
                e.page.update()
                kailand_username = mc.options["username"]
                if kailand_username:
                    self.t.value = f"Tipo de cuenta: {self.type_login.value}, Usuario: {mc.options['username']}, Estado: Procesando Registro (Espere por favor)..."
                    e.page.update()
                else:
                    self.t.value = f"Tipo de cuenta: {self.type_login.value} - (Recuerde escribir el Usuario que usara)"
                if self.text_p.value:
                    mc.options.update(
                        {
                            "username": self.text_p.value,
                            "uuid": utils.construct_offline_player_uuid(self.text_p.value),
                        }
                    )
                    # Guardar datos de session en un archivo JSON que guarda las configuraciones del usuario
                    encrypt_message(mc.options, mc.archivo_kailand)
                    print(mc.options['uuid'])
                    # Enviamos la informacion al servidor
                    try:
                        url_api = f'http://{mc.data_nube['api']}/api/v1'
                        data = {
                            "name": mc.options['username'],
                            "uuid": mc.options['uuid'],
                        }
                        token = create_jwt(data)
                        payload = {"token": token}
                        response = requests.post(
                            url_api,
                            headers={"Content-Type": "application/json"},
                            data=json.dumps(payload)
                        )
                        if response.status_code == 200:
                            response = "Registro exitoso"
                        else:
                            response = "Error al registrar usuario en el servidor"
                    except Exception as e:
                        response = "Error al registrar usuario en el servidor"
                    self.t.value = f"Tipo de cuenta: {self.type_login.value}, Usuario: {self.text_p.value}, Estado: {response}."
                self.buttom_save.disabled = False
                e.page.update()
            else:
                # De lo contrario se ejecuta este bloque si eligio (Online Microsoft)
                self.buttom_login.disabled = False
                self.buttom_login.bgcolor = ft.colors.with_opacity(0.2, "blue")
                self.text_p.disabled = True
                self.t.value = f"Tipo de cuenta: {self.type_login.value} - (Por favor dele a Login para completar el proceso)"
                e.page.update()

    def save_setting(self, e):
        '''
        Funcion llamada por el boton de guardar ajustes, se encarga de guardar los respectivos ajustes
        '''
        from game import mc
        from log import logger
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
        from game import mc
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

    def data_java_execute(self, e = None):
        from game import mc
        if mc.options["executablePath"] == "java":
            return "Por Defecto"
        else:
            return mc.options["executablePath"]

    def consulta_reglas(self, e = None):
        '''
        Consulta las reglas de la variable mc.data_nube -> Dict
        '''
        from game import mc
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
        from log import log_console
        from ui import app
        app.page_update()
        self.console_log.controls = []
        for linea in log_console:
            self.console_log.controls.append(linea)
            app.page_update()

    def console_gui(self, e):
        '''
        Muestra el contenedor de Consola
        '''
        import log
        from ui import app

        if self.c_derecho.content == self.console_widget:
            log.LOG_AVAILABLE = False
            self.c_derecho.content = self.c_derecho_cont
            self.c_derecho.disabled = True
            self.animate_buttom(e)
        else:
            log.LOG_AVAILABLE = True
            self.c_derecho.content = self.console_widget
            self.c_derecho.disabled = False
            app.page_update()
            self.animate_buttom(e)
            self.console_log.controls = log.log_console
            app.page_update()
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

    def load_app(self, app):
        '''
        Este metodo es para cargar el objeto de app en la clase
        '''
        from log import logger
        app = app
        logger.info("Cargando UI...")

data_widget = DataWidget()
