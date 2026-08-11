def factors(value):
    factor = 2
    result = []
    while value > 1:
        if value % factor == 0:
            value //= factor
            result.append(factor)
        else:
            factor += 1
    return result
