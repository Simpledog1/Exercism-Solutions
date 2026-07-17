def is_isogram(phrase):
    phrase = phrase.lower()
    possible_repeat = ""
    for letter in phrase:
        if letter.isalpha():
            if letter in possible_repeat:
                return False
            else:
                possible_repeat += letter
    return True
