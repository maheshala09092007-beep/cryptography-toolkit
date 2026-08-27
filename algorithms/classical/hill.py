NAME = "Hill Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]

def determinant(matrix):
    return (
        matrix[0][0] * matrix[1][1]
        - matrix[0][1] * matrix[1][0]
    )


def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    raise ValueError("Matrix is not invertible")


def inverse_matrix(matrix):
    det = determinant(matrix) % 26
    inverse_det = mod_inverse(det, 26)

    return [
        [
            matrix[1][1] * inverse_det % 26,
            -matrix[0][1] * inverse_det % 26
        ],
        [
            -matrix[1][0] * inverse_det % 26,
            matrix[0][0] * inverse_det % 26
        ]
    ]


def process(text, matrix):
    text = "".join(
        char for char in text.upper()
        if char.isalpha()
    )

    if len(text) % 2:
        text += "X"

    result = ""

    for i in range(0, len(text), 2):
        x = ord(text[i]) - 65
        y = ord(text[i + 1]) - 65

        result += chr(
            (matrix[0][0] * x + matrix[0][1] * y) % 26 + 65
        )

        result += chr(
            (matrix[1][0] * x + matrix[1][1] * y) % 26 + 65
        )

    return result


def encrypt(text, matrix):
    return process(text, matrix)


def decrypt(text, matrix):
    return process(text, inverse_matrix(matrix))
