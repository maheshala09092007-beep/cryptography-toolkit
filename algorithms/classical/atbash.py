NAME = "Atbash Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
def transform(text):
    result = ""

    for char in text:
        if char.isupper():
            result += chr(90 - (ord(char) - 65))
        elif char.islower():
            result += chr(122 - (ord(char) - 97))
        else:
            result += char

    return result
def encrypt(text):
    return transform(text)


def decrypt(text):
    return transform(text)
