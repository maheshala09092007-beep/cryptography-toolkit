NAME = "Affine Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
from math import gcd


def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Key has no modular inverse")


def encrypt(text, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a must be coprime with 26")

    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr((a * (ord(char) - base) + b) % 26 + base)
        else:
            result += char

    return result


def decrypt(text, a, b):
    inverse = mod_inverse(a, 26)
    result = ""

    for char in text:
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            result += chr(
                (inverse * ((ord(char) - base) - b)) % 26 + base
            )
        else:
            result += char

    return result
