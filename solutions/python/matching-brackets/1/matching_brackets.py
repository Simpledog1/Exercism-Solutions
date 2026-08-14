def is_paired(input_string):
    stack = []
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }
    
    for char in input_string:
        if char in ("(", "[", "{"):
            stack.append(char)

        if char in (")","]","}"):
            if not stack:
                return False
            
            compare = stack.pop()

            if compare != pairs[char]:
                return False
            
    return not stack