NAME = "Octal"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    return " ".join(format(b, "03o") for b in text.encode("utf-8"))


def decode(text):
    try:
        data = bytes(int(part, 8) for part in text.split())
        return data.decode("utf-8")
    except ValueError:
        raise ValueError("Invalid octal input")
