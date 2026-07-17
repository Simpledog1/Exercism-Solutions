def rotate(text, key):
    result = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in text:
        if letter.isupper() and letter.isalpha():
            finder = (alphabet.index(letter.lower()) + key) % 26
            result += alphabet[finder].upper()
        elif letter.islower() and letter.isalpha():
            finder = (alphabet.index(letter.lower()) + key) % 26
            result += alphabet[finder]
        else:
            result += letter
    return result
