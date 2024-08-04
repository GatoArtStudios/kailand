import sys
import os
import time
import hashlib
from plyer import notification
from config import APP_PATH
import platform

def ms_notify(title: str = 'Kailand V', message: str = None) -> None:
    notification.notify(
        title=title,
        message=message,
        app_name="Kailand V",
        app_icon=os.path.join(APP_PATH, 'icon.ico') if platform.system() == 'Windows' else os.path.join(APP_PATH, 'assets', 'icon.png'),
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

def construct_offline_player_uuid(username):
    #extracted from the java code:
    #new GameProfile(UUID.nameUUIDFromBytes(("OfflinePlayer:" + name).getBytes(Charsets.UTF_8)), name));
    string = "OfflinePlayer:" + username
    hash = hashlib.md5(string.encode('utf-8')).digest()
    byte_array = [byte for byte in hash]
    #set the version to 3 -> Name based md5 hash
    byte_array[6] = hash[6] & 0x0f | 0x30
    #IETF variant
    byte_array[8] = hash[8] & 0x3f | 0x80

    hash_modified = bytes(byte_array)
    offline_player_uuid = add_uuid_stripes(hash_modified.hex())

    return offline_player_uuid

def add_uuid_stripes(string):
    string_striped = (
        string[:8] + '-' +
        string[8:12] + '-' +
        string[12:16] + '-' +
        string[16:20] + '-' +
        string[20:]
    )
    return string_striped