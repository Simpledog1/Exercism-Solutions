def decode(string):

    decoded = ""
    number = ""

    for i in string:

        if i.isdigit():
            number += i
        else:
            if number == "":
                number = "1"

            decoded += i * int(number)
            number = ""

    return decoded

def encode(string):
    encoded = ""

    if string == "":
        return ""

    previous = string[0]
    count = 0
    
    for i in string:
        if previous == i:
            count += 1
        else:
            if count == 1:
                encoded += previous
            else: 
                encoded += str(count) + previous
            count = 1
            previous = i
    if count == 1:
        encoded += previous
    else:
        encoded += str(count) + previous
    return encoded
