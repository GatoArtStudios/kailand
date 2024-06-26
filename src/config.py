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

def get_path_java():
    if platform.system() == 'Windows':
        if os.path.exists('C:\\Program Files\\Java\jdk-17\\bin\\java.exe'):
            return 'C:\\Program Files\\Java\\jdk-17\\bin\\java.exe'
        else:
            return 'java'
    else:
        return 'java'

JAVA_PATH = get_path_java()

DIRECTORY_KAILAND = get_directory_kailand()

SYSTEM = get_system()

DEBUG_LINES = '300'

PRIVATE_KEY = ''''''

PUBLIC_KEY = ''''''