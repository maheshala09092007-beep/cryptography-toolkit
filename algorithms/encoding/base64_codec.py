NAME = "Base64"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]
import base64


def encode(text):
    return base64.b64encode(text.encode()).decode()


def decode(text):
    return base64.b64decode(text).decode()
