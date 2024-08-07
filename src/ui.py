import os
import sys
import time
import utils
import requests
import webbrowser
import flet as ft
from typing import Any

class LauncherVentana:
    def __init__(self):
        self._page = None


    def __call__(self, flet_page: ft.Page) -> Any:
        from layout import data_widget
        self.data_widget = data_widget
        self._page = flet_page
        self._page.title = 'Kailand V'
        self._page.window.center()
        self._page.window.frameless = True
        self._page.bgcolor = ft.colors.TRANSPARENT
        self._page.window.bgcolor = ft.colors.TRANSPARENT
        self._page.window.height = 715
        self._page.window.width = 1277
        self._page.window.resizable = False
        self._page.window.title_bar_hidden = True
        self._page.window.title_bar_buttons_hidden = True
        self._page.padding = 0
        self._page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self._page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self._page.theme_mode = ft.ThemeMode.DARK
        self._page.overlay.append(data_widget.progressbar_install)
        self._page.overlay.append(data_widget.java_info)
        self._page.overlay.append(data_widget.user_alert)
        self._page.fonts = {
            'Minecraft': '/fonts/Minecrafter.Alt.ttf',
            'FiraCode': '/fonts/FiraCodeNerdFont-SemiBold.ttf'
        }
        self._page.add(
            ft.Container(
                content=ft.WindowDragArea(
                    content=ft.Text(
                    'Cargando Launcher de Kailand V, por favor espere...',
                    animate_scale=ft.animation.Animation(duration=300, curve="bounceout"),
                    scale=ft.transform.Scale(1),
                    )
                ),
                # Fondo del launcher
                bgcolor=ft.colors.with_opacity(0.3, 'black'),
                padding=20,
                border_radius=ft.border_radius.all(10),
            )
        )
        self.page_update()
        self.load_ui_final()

    def load_ui_final(self):
        import utils
        self._page.controls.pop(0)
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
                                        tooltip='Minimizar',
                                    ),
                                    ft.IconButton(
                                        content=ft.Image(
                                            src='cerrar.png',
                                            width=20,
                                            height=20,
                                            fit=ft.ImageFit.CONTAIN
                                        ),
                                        on_click=self.close_windows,
                                        tooltip='Cerrar',
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
                                            self.data_widget.buttom_perfil,
                                            self.data_widget.buttom_reglas,
                                            self.data_widget.buttom_mods,
                                            self.data_widget.buttom_shaders,
                                            self.data_widget.buttom_textures,
                                            self.data_widget.buttom_discord,
                                            self.data_widget.buttom_console,
                                            self.data_widget.buttom_ajustes,
                                            ft.Container(
                                                content=self.data_widget.buttom_jugar,
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
                                self.data_widget.c_derecho,
                            ],
                            vertical_alignment=ft.CrossAxisAlignment.START,
                            alignment=ft.MainAxisAlignment.CENTER,
                            spacing=15
                        ),
                        # data_widget.progressbar_install,
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
        self._page.update()

    def close_windows(self, e):
        self._page.window_close()

    def minimized_windows(self, e):
        self._page.window_minimized = True
        self._page.update()
    
    def reload_windows(self, e):
        self._page.update()

    def animacion_opacity(self, e):
        if e.data == "true":
            e.control.opacity = 1
            e.control.update()
        else:
            e.control.opacity = 0.5
            e.control.update()
    @utils.handle_exception('Error al conectar con el servidor, por favor verifique su conexion.')
    def open_dlg_modal(self):
        '''
        Abre alerta con opciones si faltan recursos ///// Se ejecuta al iniciar el launcher de forma automatica para comprodar datos
        '''
        from log import logger
        from layout import data_widget
        from game import mc
        import utils
        logger.info('Chequeando actualizaciones del servidor')
        if mc.check_update_launcher():
            response = requests.get("https://raw.githubusercontent.com/GatoArtStudios/kailand/config/mods.json", timeout=5)
            if response.status_code == 200:
                __temp_data_get = response.json()
                mc.url_new_vercion = __temp_data_get["launcherUrl"]
                data_widget.check_vercion_launcher.content = ft.Text(
                    __temp_data_get["updateDescription"]
                )
                self._page.dialog = data_widget.check_vercion_launcher
                data_widget.check_vercion_launcher.open = True
                self._page.update()
                time.sleep(20)
                webbrowser.open(__temp_data_get["launcherUrl"])
                self._page.window_destroy()
                time.sleep(3)
            sys.exit(0)

        elif not mc.validate_directory(): # Ejecuta el bloque de condigo si el metodo retorna False
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
        try:
            self._page.update()
        except Exception as e:
            pass

app = LauncherVentana()