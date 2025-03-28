# file_crypto.py
from cryptography.fernet import Fernet

def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()

def encrypt_file(input_path, output_path, key):
    f = Fernet(key)
    with open(input_path, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(output_path, "wb") as file:
        file.write(encrypted_data)
    print(f"Файл {input_path} зашифрован и сохранен как {output_path}.")

def decrypt_file(input_path, output_path, key):
    f = Fernet(key)
    with open(input_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(output_path, "wb") as file:
        file.write(decrypted_data)
    print(f"Файл {input_path} дешифрован и сохранен как {output_path}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("Usage: python file_crypto.py <encrypt/decrypt> <input_file> <output_file>")
    else:
        mode = sys.argv[1].lower()
        input_file = sys.argv[2]
        output_file = sys.argv[3]
        key = load_key()
        if mode == "encrypt":
            encrypt_file(input_file, output_file, key)
        elif mode == "decrypt":
            decrypt_file(input_file, output_file, key)
        else:
            print("Неизвестный режим. Используйте 'encrypt' или 'decrypt'.")
