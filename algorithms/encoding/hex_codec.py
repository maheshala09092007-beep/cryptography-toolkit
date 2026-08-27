NAME = "Hexadecimal"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]
def encode(text):
    return text.encode().hex()


def decode(text):
    return bytes.fromhex(text).decode()
