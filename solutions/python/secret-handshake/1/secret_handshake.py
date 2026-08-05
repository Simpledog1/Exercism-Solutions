def commands(binary_str):
    binary_container = []
    result = []
    for i in binary_str:
        binary_container += [i]
    if binary_container[-1] == "1":
        result += ["wink"]
    if binary_container[-2] == "1":
        result += ["double blink"]
    if binary_container[-3] == "1":
        result += ["close your eyes"]
    if binary_container[-4] == "1":
        result += ["jump"]
    if binary_container[-5] == "1":
        result.reverse()
    return result