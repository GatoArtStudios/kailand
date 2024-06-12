import os
import sys
import time
import requests
import webbrowser
import flet as ft
from typing import Any

class LauncherVentana:
    def __init__(self):
        self._page = None


    def __call__(self, flet_page: ft.Page) -> Any:
        from layout import data_widget
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
        from log import logger
        from layout import data_widget
        from game import mc
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

app = LauncherVentana()