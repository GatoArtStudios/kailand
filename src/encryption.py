import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Random import get_random_bytes

def encrypt_message(data: dict, file: str = 'encrypted_data.json') -> bool:
    '''
    Guardar un mensaje encriptado en un archivo JSON
    ```
    data: dict
    file: str = 'encrypted_data.json'
    ```
    '''
    # Encriptar un mensaje usando una combinación de RSA y AES
    from config import PUBLIC_KEY
    public_key = RSA.import_key(PUBLIC_KEY)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    
    # Convertir el diccionario a JSON y luego a bytes
    json_data = json.dumps(data).encode('utf-8')

    # Generar una clave AES aleatoria
    aes_key = get_random_bytes(32)  # Clave AES de 256 bits

    # Cifrar los datos JSON con AES
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(json_data)

    # Cifrar la clave AES con RSA
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)

    # Guardar los datos cifrados en un archivo JSON
    encrypted_data = {
        "ciphertext": ciphertext.hex(),
        "tag": tag.hex(),
        "nonce": cipher_aes.nonce.hex(),
        "encrypted_aes_key": encrypted_aes_key.hex()
    }

    with open(file, "w") as json_file:
        json.dump(encrypted_data, json_file, indent=4)

    return True

def decrypt_message(file: str = 'encrypted_data.json') -> dict:
    '''
    Desencriptar un mensaje y lo retorna como un diccionario
    ```
    file: str = 'encrypted_data.json'
    ```
    '''
    from config import PRIVATE_KEY
    private_key = RSA.import_key(PRIVATE_KEY)

    # Leer los datos cifrados desde el archivo JSON
    with open(file, "r") as json_file:
        encrypted_data = json.load(json_file)
    
    ciphertext = bytes.fromhex(encrypted_data["ciphertext"])
    tag = bytes.fromhex(encrypted_data["tag"])
    nonce = bytes.fromhex(encrypted_data["nonce"])
    encrypted_aes_key = bytes.fromhex(encrypted_data["encrypted_aes_key"])

    # Desencriptar la clave AES con RSA
    cipher_rsa = PKCS1_OAEP.new(private_key)
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)

    # Desencriptar los datos JSON con AES
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    decrypted_json_data = cipher_aes.decrypt_and_verify(ciphertext, tag).decode('utf-8')
    
    decrypted_data = json.loads(decrypted_json_data)
    
    return decrypted_data

# Ejemplo de uso:
# encrypt_message(data={
#         "message": "Hello, World!",
#     },
#     file='config.json')

# print(decrypt_message(file='config.json'))
# print(type(decrypt_message(file='config.json')))