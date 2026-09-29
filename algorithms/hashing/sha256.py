import hashlib

NAME = "SHA-256"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash_text(text):
    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()
