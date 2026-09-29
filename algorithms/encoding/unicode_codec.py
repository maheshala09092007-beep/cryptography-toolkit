NAME = "Unicode"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]


def encode(text):
    return " ".join(f"U+{ord(char):04X}" for char in text)


def decode(text):
    codes = text.split()

    result = ""

    for code in codes:
        if not code.upper().startswith("U+"):
            raise ValueError(f"Invalid Unicode code point: {code}")

        value = int(code[2:], 16)
        result += chr(value)

    return result
