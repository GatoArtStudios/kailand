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

DIRECTORY_KAILAND = get_directory_kailand()

PRIVATE_KEY = ''''''

PUBLIC_KEY = ''''''