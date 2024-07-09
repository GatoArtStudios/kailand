import sys
import os
import time
from plyer import notification

def ms_notify(title: str = 'Kailand V', message: str = None) -> None:
    notification.notify(
        title=title,
        message=message,
        app_name="Kailand V",
    )


def exit_app() -> None:
    from ui import app
    if app._page is not None:
        app._page.window_destroy()
    time.sleep(3)
    try:
        sys.exit(1)
    except SystemExit:
        os._exit(1)
    sys.exit(0)

def handle_exception(msg: str = 'Error inesperado') -> None:
    def decorator(func):
        def wrapper(*args, **kwargs):
            from log import logger
            try:
                return func(*args, **kwargs)
            except Exception as e:
                ms_notify(message=msg)
                logger.error(e)
                exit_app()
        return wrapper
    return decorator