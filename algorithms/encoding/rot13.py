import codecs

NAME = "ROT13"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    return codecs.encode(text, "rot_13")


def decode(text):
    return codecs.decode(text, "rot_13")
