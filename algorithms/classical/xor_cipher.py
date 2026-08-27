NAME = "XOR Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
def encrypt(text, key):
    return bytes(
        byte ^ key
        for byte in text.encode()
    ).hex()


def decrypt(text, key):
    data = bytes.fromhex(text)

    return bytes(
        byte ^ key
        for byte in data
    ).decode()
