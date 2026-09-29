import base64

NAME = "Base32"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    data = text.encode("utf-8")
    return base64.b32encode(data).decode("ascii")


def decode(text):
    data = base64.b32decode(text.strip().upper())
    return data.decode("utf-8")
