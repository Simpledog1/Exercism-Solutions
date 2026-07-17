def is_valid(isbn):
    clean_text = isbn.replace("-","")
    if len(clean_text) != 10:
        return False
    if clean_text[:9].isdigit() and (clean_text.endswith("X") or clean_text[-1].isdigit()):
        results = 0
        for i in range(len(clean_text)):
            value = 0
            if clean_text[i] == "X":
                value = 10
            else:
                value = int(clean_text[i])
            results += value * (10 - i)
    else:
        return False
    total = results % 11
    if total == 0:
        return True
    return False

                
