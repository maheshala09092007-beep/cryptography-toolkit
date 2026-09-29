import os
import base64

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


NAME = "AES-GCM"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["encrypt", "decrypt"]


def encrypt(text, key):
    key = key.encode()

    if len(key) not in (16, 24, 32):
        raise ValueError(
            "AES-GCM key must be 16, 24, or 32 bytes long"
        )

    nonce = os.urandom(12)

    aes = AESGCM(key)

    ciphertext = aes.encrypt(
        nonce,
        text.encode(),
        None
    )

    result = nonce + ciphertext

    return base64.b64encode(result).decode()


def decrypt(text, key):
    key = key.encode()

    if len(key) not in (16, 24, 32):
        raise ValueError(
            "AES-GCM key must be 16, 24, or 32 bytes long"
        )

    data = base64.b64decode(text)

    nonce = data[:12]
    ciphertext = data[12:]

    aes = AESGCM(key)

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode()

