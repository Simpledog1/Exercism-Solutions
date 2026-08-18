def rows(letter):
    max_index = ord(letter) - ord("A")
    result = []
    for i in range(ord(letter)- ord("A") + 1):
        if i == 0:
            result.append(" " * (max_index - i) + chr(ord("A") + i) + " " * (max_index - i))
        else:
            result.append(" " * (max_index - i) + chr(ord("A") + i) + " " * (2 * i - 1) + chr(ord("A") + i) + " " * (max_index - i))
    for i in range(max_index - 1, -1, -1):
        if i == 0:
            result.append(" " * (max_index - i) + chr(ord("A") + i) + " " * (max_index - i))
        else:
            result.append(" " * (max_index - i) + chr(ord("A") + i) + " " * (2 * i - 1) + chr(ord("A") + i) + " " * (max_index - i))
    return result