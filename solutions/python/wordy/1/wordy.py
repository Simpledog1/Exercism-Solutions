def answer(question):
    question = question.replace("?", "").split()

    known_operations = ("plus", "minus", "multiplied", "divided")

    if question[:2] != ["What", "is"]:
        raise ValueError("syntax error")

    expecting_number = True

    for word in question[2:]:
        if word == "by":
            continue

        if expecting_number:
            if word.lstrip("-").isdigit():
                expecting_number = False
            else:
                raise ValueError("syntax error")
        else:
            if word in known_operations:
                expecting_number = True
            elif word.lstrip("-").isdigit():
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")

    if expecting_number:
        raise ValueError("syntax error")

    numbers = []
    operations = []

    for word in question[2:]:
        if word.lstrip("-").isdigit():
            numbers.append(int(word))
        elif word in known_operations:
            operations.append(word)

    result = numbers[0]

    for x in range(len(operations)):
        if operations[x] == "plus":
            result += numbers[x + 1]
        elif operations[x] == "minus":
            result -= numbers[x + 1]
        elif operations[x] == "multiplied":
            result *= numbers[x + 1]
        elif operations[x] == "divided":
            result //= numbers[x + 1]

    return result