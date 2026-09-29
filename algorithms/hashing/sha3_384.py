import hashlib

NAME = "SHA3-384"
CATEGORY = "Hashing"
OPERATIONS = ["hash"]


def hash_text(text):
    return hashlib.sha3_384(
        text.encode("utf-8")
    ).hexdigest()
