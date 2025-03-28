import socket
import threading
import logging
import time
import struct
import os

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

# Настройка логирования: логи будут записываться в файл server.log
logging.basicConfig(
    filename='server.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# Глобальное событие для завершения работы сервера
shutdown_event = threading.Event()
# Список для хранения активных потоков клиентов
client_threads = []


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


def handshake_server(sock):
    """
    Протокол рукопожатия Диффи–Хеллмана.
    Сервер генерирует параметры и свою пару ключей, отправляет параметры и свой публичный ключ,
    затем получает публичный ключ клиента и вычисляет общий секрет, который хэшируется для получения AES-ключа.
    """
    # Генерируем параметры DH (можно оптимизировать: генерировать один раз и использовать для всех подключений)
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    param_bytes = parameters.parameter_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.ParameterFormat.PKCS3
    )
    send_msg(sock, param_bytes)

    # Генерируем пару ключей сервера
    server_private_key = parameters.generate_private_key()
    server_public_key = server_private_key.public_key()
    server_pub_bytes = server_public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    send_msg(sock, server_pub_bytes)

    # Получаем публичный ключ клиента
    client_pub_bytes = recv_msg(sock)
    if client_pub_bytes is None:
        raise Exception("Не получен публичный ключ клиента")
    client_public_key = serialization.load_pem_public_key(client_pub_bytes, backend=default_backend())

    # Вычисляем общий секрет
    shared_key = server_private_key.exchange(client_public_key)
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(shared_key)
    aes_key = digest.finalize()  # 32 байта для AES-256
    return aes_key


def send_encrypted(sock, aes_key, plaintext):
    """Шифрует сообщение с использованием AES-GCM и отправляет его с 4-байтовой длиной."""
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


def handle_client(client_socket, client_address):
    logging.info(f"Подключение от {client_address}")
    try:
        # Устанавливаем защищённый канал посредством DH-обмена ключами
        aes_key = handshake_server(client_socket)
        logging.info(f"Установлен AES ключ для {client_address}")

        while not shutdown_event.is_set():
            try:
                data = recv_encrypted(client_socket, aes_key)
                if not data:
                    logging.info(f"Клиент {client_address} закрыл соединение.")
                    break
                message = data.decode('utf-8').strip()
                logging.info(f"Сообщение от {client_address}: {message}")

                # Обработка специальной команды shutdown
                if message.lower() == 'shutdown':
                    logging.info("Получена команда shutdown. Завершаю работу сервера.")
                    send_encrypted(client_socket, aes_key, b"Server is shutting down.")
                    shutdown_event.set()
                    break

                # Эхо-ответ: отправляем обратно зашифрованное сообщение
                send_encrypted(client_socket, aes_key, data)
            except ConnectionResetError:
                logging.warning(f"Клиент {client_address} неожиданно разорвал соединение.")
                break
            except Exception as e:
                logging.error(f"Ошибка при обработке клиента {client_address}: {e}")
                break
    finally:
        client_socket.close()
        logging.info(f"Соединение с {client_address} закрыто.")


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 9090))
    server_socket.listen()
    logging.info("Сервер запущен и ожидает подключений...")
    print("Сервер запущен и ожидает подключений...")

    try:
        while not shutdown_event.is_set():
            try:
                server_socket.settimeout(1.0)
                client_socket, client_address = server_socket.accept()
                client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
                client_thread.start()
                client_threads.append(client_thread)
            except socket.timeout:
                continue
            except Exception as e:
                logging.error(f"Ошибка при принятии соединения: {e}")
    finally:
        server_socket.close()
        logging.info("Серверный сокет закрыт.")
        print("Серверный сокет закрыт. Ожидание завершения активных соединений...")
        for t in client_threads:
            t.join()
        logging.info("Сервер завершил работу.")
        print("Сервер завершил работу.")


if __name__ == '__main__':
    start_server()
