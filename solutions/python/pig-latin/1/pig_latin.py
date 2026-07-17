def translate_word(word):
    vowels = "aeiou"

    if word.startswith(("xr", "yt")) or word[0] in vowels:
        return word + "ay"
    for i in range(len(word)):
        if word[i] == "u" and i > 0 and word[i - 1] == "q":
            continue
        if word[i] == "y" and i != 0:
            break
        if word[i] in vowels:
            break

    return word[i:] + word[:i] + "ay"


def translate(text):
    words = text.split()
    translated = []

    for word in words:
        translated.append(translate_word(word))

    return " ".join(translated)