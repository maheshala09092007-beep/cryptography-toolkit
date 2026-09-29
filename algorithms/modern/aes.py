import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

NAME = "AES"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["encrypt", "decrypt"]


def encrypt(text, key):
    key = key.encode("utf-8")

    if len(key) not in (16, 24, 32):
        raise ValueError("AES key must be 16, 24, or 32 bytes long")

    iv = os.urandom(16)

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv)
    )

    encryptor = cipher.encryptor()

    data = text.encode("utf-8")

    # PKCS#7-style padding
    padding_length = 16 - (len(data) % 16)
    padded_data = data + bytes([padding_length]) * padding_length

    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Store IV together with ciphertext
    result = iv + ciphertext

    return base64.b64encode(result).decode("ascii")


def decrypt(text, key):
    key = key.encode("utf-8")

    if len(key) not in (16, 24, 32):
        raise ValueError("AES key must be 16, 24, or 32 bytes long")

    encrypted_data = base64.b64decode(text)

    iv = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = Cipher(
        algorithms.AES(key),
        modes.CBC(iv)
    )

    decryptor = cipher.decryptor()

    padded_data = decryptor.update(ciphertext) + decryptor.finalize()

    padding_length = padded_data[-1]

    if padding_length < 1 or padding_length > 16:
        raise ValueError("Invalid padding or incorrect key")

    data = padded_data[:-padding_length]

    return data.decode("utf-8")
