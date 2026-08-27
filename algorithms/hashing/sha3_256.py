import hashlib


NAME = "SHA3-256"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash(text):
    return hashlib.sha3_256(text.encode()).hexdigest()
