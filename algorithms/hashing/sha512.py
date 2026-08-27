import hashlib


NAME = "SHA-512"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash(text):
    return hashlib.sha512(text.encode()).hexdigest()
