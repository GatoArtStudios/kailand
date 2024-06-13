import json
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def encrypt_message(data: str = "None", file: str = 'encrypted_data.json'):
    # Encriptar un mensaje
    from config import PUBLIC_KEY
    public_key = RSA.import_key(PUBLIC_KEY)
    cipher_rsa = PKCS1_OAEP.new(public_key)
    encrypted_message = cipher_rsa.encrypt(data.encode('utf-8'))

    # Guardar el mensaje encriptado en un archivo JSON
    data = {"encrypted_data": encrypted_message.hex()}
    with open(file, "w") as json_file:
        json.dump(data, json_file)

    return True

def decrypt_message(file: str = 'encrypted_data.json'):
    from config import PRIVATE_KEY
    # Leer la clave privada desde el archivo
    private_key = RSA.import_key(PRIVATE_KEY)

    # Leer el mensaje encriptado desde el archivo JSON
    with open(file, "r") as json_file:
        data = json.load(json_file)
        encrypted_message = bytes.fromhex(data["encrypted_data"])

    # Desencriptar el mensaje
    cipher_rsa = PKCS1_OAEP.new(private_key)
    decrypted_message = cipher_rsa.decrypt(encrypted_message).decode('utf-8')
    return decrypted_message
