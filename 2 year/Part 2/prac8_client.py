import socket
import argparse
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 65432
BUFFER_SIZE = 1024


class EncryptedConnection:
    def __init__(self, conn=None):
        self.conn = conn
        self.shared_key = None

    def perform_dh_key_exchange(self):
        # Генерация ключей клиента
        client_private_key = dh.generate_parameters(generator=2, key_size=2048,
                                                    backend=default_backend()).generate_private_key()
        client_public_key = client_private_key.public_key()

        # Обмен ключами
        server_public_key = serialization.load_pem_public_key(
            self.conn.recv(BUFFER_SIZE),
            backend=default_backend()
        )
        self.conn.sendall(client_public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

        # Вычисление общего ключа
        shared_key = client_private_key.exchange(server_public_key)
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


def tcp_client(use_encryption):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((DEFAULT_HOST, DEFAULT_PORT))
        ec = EncryptedConnection(s) if use_encryption else None
        if ec: ec.perform_dh_key_exchange()

        message = input('Enter message: ').encode()

        if ec:
            data = ec.encrypt(message)
        else:
            data = message

        s.sendall(data)
        response = s.recv(BUFFER_SIZE)

        if ec:
            response = ec.decrypt(response)

        print('Received:', response.decode())


def udp_client(use_encryption):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = input('Enter message: ').encode()
        s.sendto(message, (DEFAULT_HOST, DEFAULT_PORT))
        response, addr = s.recvfrom(BUFFER_SIZE)
        print('Received:', response.decode())


if __name__ == "__main__":
    # parser = argparse.ArgumentParser(description='Client application')
    # parser.add_argument('--proto', choices=['tcp', 'udp'], required=True, help='Protocol to use')
    # parser.add_argument('--encrypt', action='store_true', help='Enable encryption')
    # args = parser.parse_args()
    #
    # if args.proto == 'tcp':
    #     tcp_client(args.encrypt)
    # elif args.proto == 'udp':
    #     udp_client(args.encrypt)

    encryption = input("Encryption Flag(t/f): ")
    if encryption == 't':
        encryption = True
    else:
        encryption = False

    protocol = input("Enter protocl(tcp/udp): ")
    if protocol == "tcp":
        tcp_client(encryption)
    else:
        udp_client(encryption)