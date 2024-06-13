import os
import platform

# Obtener el nombre de usuario
if platform.system() == 'Windows':
    USERNAME = os.environ['USERNAME']
else:
    USERNAME = os.environ.get('USER')

def get_directory_kailand():
    # Definir la ruta del directorio de trabajo principal según el sistema operativo
    if platform.system() == 'Windows':
        return f"C://Users//{USERNAME}//AppData//Roaming//.kailand"
    elif platform.system() == 'Darwin':  # macOS
        return os.path.join("Users", USERNAME, ".kailand")
    else:  # Linux y otros sistemas UNIX-like
        return os.path.join("/home", USERNAME, ".kailand")

def get_system():
    if platform.system() == 'Windows':
        return "Windows"
    elif platform.system() == 'Darwin':  # macOS
        return "macOS"
    else:  # Linux y otros sistemas UNIX-like
        return "Linux"

DIRECTORY_KAILAND = get_directory_kailand()

SYSTEM = get_system()

PRIVATE_KEY = ''''''

PUBLIC_KEY = ''''''