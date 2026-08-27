NAME = "Binary"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]
def encode(text):
    return " ".join(format(byte, "08b") for byte in text.encode())


def decode(text):
    return bytes(int(byte, 2) for byte in text.split()).decode()
