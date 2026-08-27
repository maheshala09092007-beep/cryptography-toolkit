NAME = "Playfair Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
def create_matrix(key):
    key = "".join(
        char for char in key.upper()
        if char.isalpha()
    ).replace("J", "I")

    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    chars = []

    for char in key + alphabet:
        if char not in chars:
            chars.append(char)

    return [chars[i:i + 5] for i in range(0, 25, 5)]


def prepare_text(text):
    text = "".join(
        char for char in text.upper()
        if char.isalpha()
    ).replace("J", "I")

    result = []
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 >= len(text):
            result.extend([a, "X"])
            i += 1

        elif text[i + 1] == a:
            result.extend([a, "X"])
            i += 1

        else:
            result.extend([a, text[i + 1]])
            i += 2

    return result


def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col


def process(text, key, encrypting=True):
    matrix = create_matrix(key)
    text = prepare_text(text)
    result = []

    shift = 1 if encrypting else -1

    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]

        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:
            result.append(matrix[row1][(col1 + shift) % 5])
            result.append(matrix[row2][(col2 + shift) % 5])

        elif col1 == col2:
            result.append(matrix[(row1 + shift) % 5][col1])
            result.append(matrix[(row2 + shift) % 5][col2])

        else:
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])

    return "".join(result)


def encrypt(text, key):
    return process(text, key, True)


def decrypt(text, key):
    return process(text, key, False)
