NAME = "Morse Code"
CATEGORY = "Encoding"
OPERATIONS = ["encode", "decode"]
MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----."
}

DECODE_MORSE = {value: key for key, value in MORSE_CODE.items()}


def encode(text):
    result = []

    for char in text.upper():
        if char == " ":
            result.append("/")
        elif char in MORSE_CODE:
            result.append(MORSE_CODE[char])
        else:
            result.append("?")

    return " ".join(result)


def decode(text):
    result = []

    for code in text.split():
        if code == "/":
            result.append(" ")
        elif code in DECODE_MORSE:
            result.append(DECODE_MORSE[code])
        else:
            result.append("?")

    return "".join(result)
