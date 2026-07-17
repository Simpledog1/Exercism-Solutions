def square(number):
    """The number of grains on a given square."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 **(number-1)

def total():
    """The total number of grains on the chessboard."""
    total1 = 0
    for num in range(1, 64 + 1):
        total1 += square(num)
    return total1
