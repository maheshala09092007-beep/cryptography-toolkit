NAME = "ASCII"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    return " ".join(str(ord(char)) for char in text)


def decode(text):
    return "".join(chr(int(value)) for value in text.split())
