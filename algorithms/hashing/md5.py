import hashlib


NAME = "MD5"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash(text):
    return hashlib.md5(text.encode()).hexdigest()
