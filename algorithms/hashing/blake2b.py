import hashlib


NAME = "BLAKE2b"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash(text):
    return hashlib.blake2b(text.encode()).hexdigest()
