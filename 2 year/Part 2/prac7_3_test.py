import os
import pytest
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, padding

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


def encrypt_decrypt_aes(mode_name, key, plaintext):
    backend = default_backend()
    iv = os.urandom(16)  # IV длиной 16 байт для AES

    if mode_name == 'CBC':
        mode = modes.CBC(iv)
    elif mode_name == 'CFB':
        mode = modes.CFB(iv)
    elif mode_name == 'OFB':
        mode = modes.OFB(iv)
    elif mode_name == 'GCM':
        mode = modes.GCM(iv)
    else:
        raise ValueError("Неизвестный режим")

    cipher = Cipher(algorithms.AES(key), mode, backend=backend)

    # Для режима CBC используем паддинг PKCS7
    if mode_name == 'CBC':
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    else:
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Для GCM важно получить tag для аутентификации
    tag = encryptor.tag if mode_name == 'GCM' else None

    # Дешифрование
    if mode_name == 'GCM':
        decrypt_mode = modes.GCM(iv, tag)
    else:
        decrypt_mode = mode

    cipher_dec = Cipher(algorithms.AES(key), decrypt_mode, backend=backend)
    decryptor = cipher_dec.decryptor()
    decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

    # Если CBC - распаковываем данные
    if mode_name == 'CBC':
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_text = unpadder.update(decrypted_data) + unpadder.finalize()
    else:
        decrypted_text = decrypted_data

    return ciphertext, decrypted_text, iv, tag


def test_dh_key_exchange():
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    alice_priv = parameters.generate_private_key()
    bob_priv = parameters.generate_private_key()
    alice_pub = alice_priv.public_key()
    bob_pub = bob_priv.public_key()

    alice_shared = alice_priv.exchange(bob_pub)
    bob_shared = bob_priv.exchange(alice_pub)

    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(alice_shared)
    alice_key = digest.finalize()

    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(bob_shared)
    bob_key = digest.finalize()

    assert alice_key == bob_key


@pytest.mark.parametrize("mode", ['CBC', 'CFB', 'OFB', 'GCM'])
def test_aes_encryption(mode):
    key = os.urandom(32)
    plaintext = b"Test message for AES encryption modes."
    ciphertext, decrypted, iv, tag = encrypt_decrypt_aes(mode, key, plaintext)
    assert decrypted == plaintext


if __name__ == "__main__":
    pytest.main()
