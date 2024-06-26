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

PRIVATE_KEY = '''-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAn5zA++iWBUfTHTjRlQmWgxShpVubgctdn58ckbS0YW7LK1kk
imBEGWccaIoJWT+ayfyB+7hFy6PEKra+TEEaxT+CU/rr2+AfDWrM7TYSi4VKsyeU
9db+aUG4SDAh3LSzebgBSeyBbHFw5XU8SXIaRH3cU1lZM/AgFTRV2IDton4/kYqx
qPAeoYCfV8ePBMuc0ib4ZPdbYmmYgknC5SxqfUj6m50Vl2wJh1+PQ4F9ZMSssgz1
kmf9iRpaOkvThJk0DPeZLWp11fYKLXoLK5VT7iFWioyOdIDaCmlwrrPmR04qCtvj
tKAGuv16exxcFBpwGgVUg9tMFFpzFFYn4zFtlQIDAQABAoIBAAh9pUKBWqGzSBwb
hAKtUjrCOTXRDBJj3XolU7a96dlDtJPSF9Xd+HbFe8cP43QXpHCu+cHd8/s481w2
Vnnl/g+U06ZgsyACPy9OiXzroyGVmKYJKq0dSnFnqURQfddTgYytvjEkNLUDyowE
/Y0GqzZjik9LcdRdJ3JuqKEY0rYRyFtrMc8t0/+kaQmSHwIt91hd4+TkzjrAHVKc
0FLb4KbSn1/yHMF2zVCfIw4fg68MoKkos1zFYGmRP/XJo43qFDTxdHVxum2Hol7+
WXHzJVTQ/kWoJZ/TvQ8n1Rp/TTS9/3oqZqs2FW0NYXKo/5mfyf0UmNrH7xvyX+zt
D9Wh38ECgYEAvYCo7c3uY5ysumQI071aSCsG0R2K4QvtYZj1obLA+VQOzB+YEoG9
ddVyjJ6nKtT2HN6Zs4NXTZbSGqTZgw2lCpFlTAYYhIylKD1JpHvswzoqyyr4ojPg
9fgBbIBsz142Yr1ZsiC/nFxDGpKmkS1ebBNa3RBHGR1zcM7jnY+T4+UCgYEA158A
RUKLbCU6pVbKN6vSoqKUhSmPWQ7RMQ6e70OvcwTPf5UYwxXP9GUoomhankAvtLpP
jrWMmTY6uRtjFtrxXOG8pAc3toxaQ60FgrCYGKxA7A6N4YibnakkBqc2AI9rnnbC
rU97n5JvyEwlDMVYJ8u7e4kogqs1vBl2ythAJ/ECgYB6bXi1yelNaZceBCq/wQFm
xoVs7E0g/3epKgznHnkVm3zD21V//1nLms6akpUlUth95kIee6gXdGzg0cfEpzgN
D8oFx5pnaAX7bTz6iyV3K0kiYOyoviOERWmGE6I4hoFUYUhlkEq6VdD0hfIesNTj
tc1qLG4Ch8hhBQiAbpX5EQKBgDxgQmQiaQXkOtK3RbJnA3kUyz+qToBifMMe0/Qt
YMB1NWEFL8TYo71MYh9v1wf+8xzJGqPcRD1WiQTyHUH2FqWqc/b+KmSMUm4m0acx
qbUm7prqzGG9rc1s4jCWu7FWd40MtiBvZC9fgrt0Tt+Plsq16o6B7n0AUfCUtMXB
3d0RAoGAP0mvkQdXZD2pY56J1/+yvYk/+I0ZsHzjGH7BJSKGNUJuJcbv9ZG8CrKP
+Xl9BDfsFlov8q7PPcwFX3UwEdSCRXnfVjaGQIZpqSOOvj02Y1MSqrXR6MQ9+0oT
8jtQysrGHKamwFPlX2uzuyKiWwKX0ElmdqWZSqQ2dc4Y6oXO7UI=
-----END RSA PRIVATE KEY-----'''

PUBLIC_KEY = '''-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn5zA++iWBUfTHTjRlQmW
gxShpVubgctdn58ckbS0YW7LK1kkimBEGWccaIoJWT+ayfyB+7hFy6PEKra+TEEa
xT+CU/rr2+AfDWrM7TYSi4VKsyeU9db+aUG4SDAh3LSzebgBSeyBbHFw5XU8SXIa
RH3cU1lZM/AgFTRV2IDton4/kYqxqPAeoYCfV8ePBMuc0ib4ZPdbYmmYgknC5Sxq
fUj6m50Vl2wJh1+PQ4F9ZMSssgz1kmf9iRpaOkvThJk0DPeZLWp11fYKLXoLK5VT
7iFWioyOdIDaCmlwrrPmR04qCtvjtKAGuv16exxcFBpwGgVUg9tMFFpzFFYn4zFt
lQIDAQAB
-----END PUBLIC KEY-----'''