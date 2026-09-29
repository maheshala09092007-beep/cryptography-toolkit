import hashlib

NAME = "BLAKE2s"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash_text(text):
    return hashlib.blake2s(
        text.encode("utf-8")
    ).hexdigest()
