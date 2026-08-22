import math
def cipher_text(plain_text):
    result = ""
    for i in plain_text:
        if i.isalpha() or i.isdigit():
            result += i.lower()

    if result == "":
        return ""
    
    for c in range(1, len(result) + 1):
        r = math.ceil(len(result) / c)

        if r * c >= len(result) and c >= r and c - r <= 1:
            break

    rows = []

    for i in range(0, len(result), c):
        row = result[i:i + c]
        row += " " * (c - len(row))
        rows += [row]

    encoded = ""

    for column in range(c):
        for row in rows:
            encoded += row[column]

    chunks = []

    for i in range(0, len(encoded), r):
        chunks += [encoded[i:i + r]]

    return(" ".join(chunks))