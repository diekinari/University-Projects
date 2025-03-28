import socket
import threading
import selectors
import argparse
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

# Общие настройки
DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 65432
BUFFER_SIZE = 1024

# Глобальные переменные для DH
DH_PARAMETERS = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())


class EncryptedConnection:
    def __init__(self, conn=None, addr=None):
        self.conn = conn
        self.addr = addr
        self.shared_key = None

    def perform_dh_key_exchange(self):
        # Генерация ключей сервера
        server_private_key = DH_PARAMETERS.generate_private_key()
        server_public_key = server_private_key.public_key()

        # Отправка публичного ключа
        self.conn.sendall(server_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

        # Получение клиентского ключа
        client_public_key = serialization.load_pem_public_key(
            self.conn.recv(BUFFER_SIZE),
            backend=default_backend()
        )

        # Вычисление общего ключа
        shared_key = server_private_key.exchange(client_public_key)
        self.shared_key = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'DH Encryption',
            backend=default_backend()
        ).derive(shared_key)

    def encrypt(self, data):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.shared_key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        return iv + encryptor.update(data) + encryptor.finalize()

    def decrypt(self, data):
        iv = data[:16]
        ciphertext = data[16:]
        cipher = Cipher(algorithms.AES(self.shared_key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()


def tcp_server_threaded(use_encryption):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((DEFAULT_HOST, DEFAULT_PORT))
        s.listen()
        print(f"Threaded TCP server running on {DEFAULT_HOST}:{DEFAULT_PORT} [Encryption: {use_encryption}]")

        while True:
            conn, addr = s.accept()
            handler = threading.Thread(target=handle_tcp_client, args=(conn, addr, use_encryption))
            handler.start()


def handle_tcp_client(conn, addr, use_encryption):
    ec = EncryptedConnection(conn, addr) if use_encryption else None
    if ec: ec.perform_dh_key_exchange()

    with conn:
        print(f'Connected by {addr}')
        while True:
            try:
                data = conn.recv(BUFFER_SIZE)
                if not data: break

                if ec:
                    data = ec.decrypt(data)
                    response = ec.encrypt(data)
                else:
                    response = data

                print(f'Received from {addr}: {data.decode()}')
                conn.sendall(response)
            except ConnectionResetError:
                break


def udp_server(use_encryption):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((DEFAULT_HOST, DEFAULT_PORT))
        print(f"UDP server running on {DEFAULT_HOST}:{DEFAULT_PORT} [Encryption: {use_encryption}]")

        while True:
            data, addr = s.recvfrom(BUFFER_SIZE)
            print(f'Received from {addr}: {data.decode()}')
            s.sendto(data, addr)


def tcp_server_selector(use_encryption):
    sel = selectors.DefaultSelector()

    def accept(sock):
        conn, addr = sock.accept()
        print(f'Accepted connection from {addr}')
        conn.setblocking(False)
        sel.register(conn, selectors.EVENT_READ, read)

    def read(conn):
        data = conn.recv(BUFFER_SIZE)
        if data:
            print(f'Echoing: {data.decode()}')
            conn.sendall(data)
        else:
            print('Closing connection')
            sel.unregister(conn)
            conn.close()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((DEFAULT_HOST, DEFAULT_PORT))
        s.listen()
        s.setblocking(False)
        sel.register(s, selectors.EVENT_READ, accept)
        print(f"Selector TCP server running on {DEFAULT_HOST}:{DEFAULT_PORT} [Encryption: {use_encryption}]")

        while True:
            events = sel.select()
            for key, mask in events:
                callback = key.data
                callback(key.fileobj)


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Server application')
    # parser.add_argument('--proto', choices=['tcp', 'udp'], required=True, help='Protocol to use')
    # parser.add_argument('--mode', choices=['threaded', 'selector'], help='TCP processing mode')
    # parser.add_argument('--encrypt', action='store_true', help='Enable encryption')
    # args = parser.parse_args()
    #
    # if args.proto == 'tcp':
    #     if args.mode == 'threaded':
    #         tcp_server_threaded(args.encrypt)
    #     elif args.mode == 'selector':
    #         tcp_server_selector(args.encrypt)
    # elif args.proto == 'udp':
    #     udp_server(args.encrypt)


    encryption = input("Encryption Flag(t/f): ")
    if encryption == 't':
        encryption = True
    else:
        encryption = False

    protocol = input("Enter protocl(tcp/udp): ")
    if protocol == "tcp":
        mode = input("Enter mode for TCP connection(thread/selector): ")
        if mode == 'thread':
            tcp_server_threaded(encryption)
        elif mode == 'selector':
            tcp_server_selector(encryption)
    else:
        udp_server(encryption)