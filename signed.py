from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.asymmetric.rsa import generate_private_key
from messages import *
from cfgFIT import *

def sign_message(message, private_key):
    # Создание хеша сообщения
    digest = hashes.Hash(hashes.SHA256(), backend=default_backend())
    digest.update(message)
    message_hash = digest.finalize()

    # Подпись сообщения с использованием приватного ключа
    signature = private_key.sign(
        message_hash,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    return signature


