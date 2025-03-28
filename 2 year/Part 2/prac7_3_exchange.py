from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.backends import default_backend

# Генерация общих параметров
parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

# Генерация ключей для Алисы
alice_private_key = parameters.generate_private_key()
alice_public_key = alice_private_key.public_key()

# Генерация ключей для Боба
bob_private_key = parameters.generate_private_key()
bob_public_key = bob_private_key.public_key()

# Обмен публичными ключами (в реальности происходит по сети)
# Алиса вычисляет общий секрет
alice_shared_key = alice_private_key.exchange(bob_public_key)
# Боб вычисляет общий секрет
bob_shared_key = bob_private_key.exchange(alice_public_key)

# Проверка, что общий секрет совпадает (например, с помощью хэширования)
from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(alice_shared_key)
alice_key = digest.finalize()

digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
digest.update(bob_shared_key)
bob_key = digest.finalize()

assert alice_key == bob_key, "Общий секрет не совпадает!"
print("Общий секрет успешно установлен!")
