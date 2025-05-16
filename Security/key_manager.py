from cryptography.fernet import Fernet
import os


KEY_FILE_PATH = "clave.key"

def generate_and_save_key():
    key = Fernet.generate_key()
    with open(KEY_FILE_PATH, "wb") as key_file:
        key_file.write(key)
    print("Clave generada y guardada correctamente.")

def load_key():
    if os.path.exists(KEY_FILE_PATH):
        with open(KEY_FILE_PATH, "rb") as key_file:
            return key_file.read()
    else:
        generate_and_save_key()
        return load_key()