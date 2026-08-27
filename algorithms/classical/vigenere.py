NAME = "Vigenere Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
def encrypt(text, key):
    result = []
    key = key.upper()
    index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[index % len(key)]) - 65

            if char.isupper():
                result.append(chr((ord(char) - 65 + shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 + shift) % 26 + 97))

            index += 1
        else:
            result.append(char)

    return "".join(result)


def decrypt(text, key):
    key = key.upper()
    result = []
    index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[index % len(key)]) - 65

            if char.isupper():
                result.append(chr((ord(char) - 65 - shift) % 26 + 65))
            else:
                result.append(chr((ord(char) - 97 - shift) % 26 + 97))

            index += 1
        else:
            result.append(char)

    return "".join(result)
