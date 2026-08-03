def abbreviate(words):
    sentence = words.split()
    result = ""
    for char in sentence:
        char = char.replace("-"," ").replace("_"," ")
        parts = char.split()
        for part in parts:
            if part:
                result += part[0].upper()
    return result
            
