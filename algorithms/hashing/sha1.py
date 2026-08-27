import hashlib


NAME = "SHA-1"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash(text):
    return hashlib.sha1(text.encode()).hexdigest()
