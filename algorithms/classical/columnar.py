NAME = "Columnar Transposition"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
def encrypt(text, key):
    key = key.upper()
    columns = len(key)

    rows = [
        text[i:i + columns]
        for i in range(0, len(text), columns)
    ]

    order = sorted(range(columns), key=lambda i: (key[i], i))

    result = ""

    for column in order:
        for row in rows:
            if column < len(row):
                result += row[column]

    return result


def decrypt(text, key):
    key = key.upper()
    columns = len(key)
    length = len(text)
    rows = (length + columns - 1) // columns

    short_columns = columns * rows - length

    order = sorted(range(columns), key=lambda i: (key[i], i))

    column_lengths = [rows] * columns

    for i in range(columns - short_columns, columns):
        if i >= 0:
            column_lengths[i] -= 1

    grid = [""] * columns
    index = 0

    for column in order:
        grid[column] = text[index:index + column_lengths[column]]
        index += column_lengths[column]

    result = ""

    for row in range(rows):
        for column in range(columns):
            if row < len(grid[column]):
                result += grid[column][row]

    return result
