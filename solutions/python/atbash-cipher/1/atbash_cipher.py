original = list("abcdefghijklmnopqrstuvwxyz")
converted = list("zyxwvutsrqponmlkjihgfedcba")

def encode(plain_text):
    result = []

    for letter in plain_text:
        if letter.isalpha():
            index = original.index(letter.lower())
            result.append(converted[index])
        elif letter.isdigit():
            result.append(letter)

    encoded = "".join(result)

    return " ".join(
        encoded[i:i + 5]
        for i in range(0, len(encoded), 5)
    )

def decode(ciphered_text):
    result = []

    for letter in ciphered_text:
        if letter.isalpha():
            index = converted.index(letter)
            result.append(original[index])
        elif letter.isdigit():
            result.append(letter)

    return "".join(result)