import hashlib

NAME = "SHA3-512"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash_text(text):
    return hashlib.sha3_512(
        text.encode("utf-8")
    ).hexdigest()
