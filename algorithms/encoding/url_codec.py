from urllib.parse import quote, unquote

NAME = "URL Encoding"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    return quote(text, safe="")


def decode(text):
    return unquote(text)
