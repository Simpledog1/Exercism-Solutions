def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 **(number-1)

def total():
    total = 0
    for num in range(1, 64 + 1):
        total += square(num)
    return total
