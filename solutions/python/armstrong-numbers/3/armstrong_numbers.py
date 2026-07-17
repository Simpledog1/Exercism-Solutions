def is_armstrong_number(number):
    power = len(str(number))
    total = 0
    for num in str(number):
        digit = int(num)
        total += digit**(power)
    return number == total
