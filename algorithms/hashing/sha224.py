import hashlib

NAME = "SHA-224"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash_text(text):
    return hashlib.sha224(
        text.encode("utf-8")
    ).hexdigest()

