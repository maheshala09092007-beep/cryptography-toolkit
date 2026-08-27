NAME = "Rail Fence Cipher"
CATEGORY = "Classical Cryptography"
OPERATIONS = ["encrypt", "decrypt"]
def encrypt(text, rails):
    if rails <= 1:
        return text

    fence = [[] for _ in range(rails)]
    row = 0
    direction = 1

    for char in text:
        fence[row].append(char)

        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1

        row += direction

    return "".join("".join(line) for line in fence)


def decrypt(text, rails):
    if rails <= 1:
        return text

    pattern = list(range(rails)) + list(range(rails - 2, 0, -1))
    positions = [pattern[i % len(pattern)] for i in range(len(text))]

    counts = [positions.count(i) for i in range(rails)]

    rows = []
    index = 0

    for count in counts:
        rows.append(list(text[index:index + count]))
        index += count

    result = []
    indexes = [0] * rails

    for row in positions:
        result.append(rows[row][indexes[row]])
        indexes[row] += 1

    return "".join(result)
