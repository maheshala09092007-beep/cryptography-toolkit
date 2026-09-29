import hashlib

NAME = "SHA3-224"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash_text(text):
    return hashlib.sha3_224(
        text.encode("utf-8")
    ).hexdigest()
