import base64
import os

from cryptography.hazmat.decrepit.ciphers import algorithms
from cryptography.hazmat.primitives.ciphers import Cipher, modes


NAME = "Triple DES (3DES)"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["encrypt", "decrypt"]


def _pad(data):
    padding_length = 8 - (len(data) % 8)
    return data + bytes([padding_length]) * padding_length


def _unpad(data):
    padding_length = data[-1]

    if padding_length < 1 or padding_length > 8:
        raise ValueError("Invalid padding")

    return data[:-padding_length]


def encrypt(text, key):
    key = key.encode()

    if len(key) not in (16, 24):
        raise ValueError(
            "3DES key must be 16 or 24 bytes long"
        )

    iv = os.urandom(8)

    cipher = Cipher(
        algorithms.TripleDES(key),
        modes.CBC(iv)
    )

    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(
        _pad(text.encode())
    ) + encryptor.finalize()

    return base64.b64encode(
        iv + ciphertext
    ).decode()


def decrypt(text, key):
    key = key.encode()

    if len(key) not in (16, 24):
        raise ValueError(
            "3DES key must be 16 or 24 bytes long"
        )

    data = base64.b64decode(text)

    iv = data[:8]
    ciphertext = data[8:]

    cipher = Cipher(
        algorithms.TripleDES(key),
        modes.CBC(iv)
    )

    decryptor = cipher.decryptor()

    padded = decryptor.update(
        ciphertext
    ) + decryptor.finalize()

    return _unpad(padded).decode()
