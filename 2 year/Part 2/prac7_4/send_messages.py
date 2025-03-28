# send_messages.py
from cryptography.fernet import Fernet


def load_key(filename="secret.key"):
    with open(filename, "rb") as key_file:
        return key_file.read()


def encrypt_message(message, key):
    f = Fernet(key)
    return f.encrypt(message.encode())


def main():
    key = load_key()
    output_file = "encrypted_messages.txt"
    print("Введите сообщения. Введите 'exit' для завершения ввода.")

    # Открываем файл в режиме добавления в бинарном формате
    with open(output_file, "ab") as f:
        while True:
            message = input("Сообщение: ")
            if message.lower() == "exit":
                break
            encrypted = encrypt_message(message, key)
            # Каждое сообщение записывается в отдельной строке
            f.write(encrypted + b"\n")
            print("Сообщение зашифровано и сохранено.")


if __name__ == "__main__":
    main()
