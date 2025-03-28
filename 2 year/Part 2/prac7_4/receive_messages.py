# receive_messages.py
from cryptography.fernet import Fernet


def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    return f.decrypt(encrypted_message).decode()


def main():
    key = load_key()
    input_file = "encrypted_messages.txt"
    print("Дешифрование сообщений:")

    with open(input_file, "rb") as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    message = decrypt_message(line, key)
                    print("Сообщение:", message)
                except Exception as e:
                    print("Ошибка дешифрования:", e)


if __name__ == "__main__":
    main()
