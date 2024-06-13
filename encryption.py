import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(data: dict, file: str = 'encrypted_data.json') -> bool:
    '''
    data: str or dict = json or dict
    '''
    # Encriptar un mensaje
    from config import PUBLIC_KEY
    public_key = RSA.import_key(PUBLIC_KEY)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    if isinstance(data, dict):
        encrypted_message = cipher_rsa.encrypt(json.dumps(data).encode('utf-8'))
    else:
        encrypted_message = cipher_rsa.encrypt(data.encode('utf-8'))

    # Guardar el mensaje encriptado en un archivo JSON
    data = {"encrypted_data": encrypted_message.hex()}
    with open(file, "w") as json_file:
        json.dump(data, json_file)

    return True

def decrypt_message(file: str = 'encrypted_data.json') -> dict:
    '''
    Desencriptar un mensaje y lo retorna como un diccionario
    '''
    from config import PRIVATE_KEY
    # Leer la clave privada desde el archivo
    private_key = RSA.import_key(PRIVATE_KEY)

    # Leer el mensaje encriptado desde el archivo JSON
    with open(file, "r") as json_file:
        data = json.load(json_file)
        encrypted_message = bytes.fromhex(data["encrypted_data"])

    # Desencriptar el mensaje
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message)
    if decrypted_message[0] == 123: # Si el primer caracter es un '{' es json
        decrypted_message = json.loads(decrypted_message.decode('utf-8'))
    else:
        decrypted_message = decrypted_message.decode('utf-8')
    return decrypted_message

# Ejemplo de uso:
# encrypt_message(data={
#         "message": "Hello, World!",
#     },
#     file='config.json')

# print(decrypt_message(file='config.json'))
