import html

NAME = "HTML Entities"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    return html.escape(text, quote=True)


def decode(text):
    return html.unescape(text)
