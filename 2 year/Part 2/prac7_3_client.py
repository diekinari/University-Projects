import socket
import struct
import os
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def send_msg(sock, msg):
    """Отправка сообщения с 4-байтовой длиной."""
    msg_len = len(msg)
    sock.sendall(struct.pack('!I', msg_len) + msg)


def recvall(sock, n):
    """Получает ровно n байтов из сокета."""
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data


def recv_msg(sock):
    """Получает сообщение, предварительно считав 4-байтовую длину."""
    raw_len = recvall(sock, 4)
    if not raw_len:
        return None
    msg_len = struct.unpack('!I', raw_len)[0]
    return recvall(sock, msg_len)


def handshake_client(sock):
    """
    Получает DH-параметры и публичный ключ сервера,
    генерирует свою пару ключей, отправляет публичный ключ,
    и вычисляет общий секрет для формирования AES-ключа.
    """
    # Получаем параметры DH от сервера
    param_bytes = recv_msg(sock)
    if param_bytes is None:
        raise Exception("Не получены параметры DH от сервера")
    parameters = serialization.load_pem_parameters(param_bytes, backend=default_backend())

    # Получаем публичный ключ сервера
    server_pub_bytes = recv_msg(sock)
    if server_pub_bytes is None:
        raise Exception("Не получен публичный ключ сервера")
    server_public_key = serialization.load_pem_public_key(server_pub_bytes, backend=default_backend())

    # Генерируем свою пару ключей с использованием полученных параметров
    client_private_key = parameters.generate_private_key()
    client_public_key = client_private_key.public_key()
    client_pub_bytes = client_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    send_msg(sock, client_pub_bytes)

    # Вычисляем общий секрет
    shared_key = client_private_key.exchange(server_public_key)
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(shared_key)
    aes_key = digest.finalize()
    return aes_key


def send_encrypted(sock, aes_key, plaintext):
    """Шифрует сообщение с использованием AES-GCM и отправляет его с длиной."""
    aesgcm = AESGCM(aes_key)
    nonce = os.urandom(12)
    ciphertext = aesgcm.encrypt(nonce, plaintext, None)
    payload = nonce + ciphertext
    send_msg(sock, payload)


def recv_encrypted(sock, aes_key):
    """Принимает зашифрованное сообщение, расшифровывает и возвращает его."""
    payload = recv_msg(sock)
    if payload is None:
        return None
    nonce = payload[:12]
    ciphertext = payload[12:]
    aesgcm = AESGCM(aes_key)
    plaintext = aesgcm.decrypt(nonce, ciphertext, None)
    return plaintext


def start_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(('localhost', 9090))
    except Exception as e:
        print("Ошибка подключения к серверу:", e)
        return

    try:
        aes_key = handshake_client(client_socket)
        print("Защищённый канал установлен с сервером.")
        while True:
            message = input("Введите сообщение (или 'exit' для выхода): ")
            if message.lower() == "exit":
                print("Завершение работы клиента.")
                break
            send_encrypted(client_socket, aes_key, message.encode('utf-8'))
            response = recv_encrypted(client_socket, aes_key)
            if not response:
                print("Сервер закрыл соединение.")
                break
            print("Ответ от сервера:", response.decode('utf-8'))
    except Exception as e:
        print("Ошибка при передаче данных:", e)
    finally:
        client_socket.close()


if __name__ == '__main__':
    start_client()
