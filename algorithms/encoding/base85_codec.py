import base64

NAME = "Base85"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    data = text.encode("utf-8")
    return base64.b85encode(data).decode("ascii")


def decode(text):
    data = base64.b85decode(text.encode("ascii"))
    return data.decode("utf-8")
