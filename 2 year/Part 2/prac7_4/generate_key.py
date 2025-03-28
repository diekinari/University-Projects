# generate_key.py
from cryptography.fernet import Fernet

def generate_and_save_key(filename="secret.key"):
    key = Fernet.generate_key()
    with open(filename, "wb") as key_file:
        key_file.write(key)
    print(f"Secret key generated and saved to {filename}")

if __name__ == "__main__":
    generate_and_save_key()
