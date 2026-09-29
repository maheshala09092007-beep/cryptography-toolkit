import os
import base64

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms


NAME = "ChaCha20"
CATEGORY = "Modern Cryptography"
OPERATIONS = ["encrypt", "decrypt"]


def _create_cipher(key, nonce):
    return Cipher(
        algorithms.ChaCha20(nonce, key),
        mode=None
    )


def encrypt(text, key):
    key = key.encode("utf-8")

    if len(key) != 32:
        raise ValueError("ChaCha20 key must be exactly 32 bytes long")

    # ChaCha20 requires a 16-byte nonce/counter value in this API.
    nonce = os.urandom(16)

    cipher = _create_cipher(key, nonce)
    encryptor = cipher.encryptor()

    ciphertext = encryptor.update(text.encode("utf-8"))

    # Store nonce + ciphertext together.
    result = nonce + ciphertext

    return base64.b64encode(result).decode("ascii")


def decrypt(text, key):
    key = key.encode("utf-8")

    if len(key) != 32:
        raise ValueError("ChaCha20 key must be exactly 32 bytes long")

    encrypted_data = base64.b64decode(text)

    if len(encrypted_data) < 16:
        raise ValueError("Invalid ChaCha20 ciphertext")

    nonce = encrypted_data[:16]
    ciphertext = encrypted_data[16:]

    cipher = _create_cipher(key, nonce)
    decryptor = cipher.decryptor()

    plaintext = decryptor.update(ciphertext)

    return plaintext.decode("utf-8")
