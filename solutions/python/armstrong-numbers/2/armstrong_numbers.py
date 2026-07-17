def is_armstrong_number(number):
    power = len(str(number))
    total = 0
    for num in str(number):
        num = int(num)
        total += num**(power)
    return number == total
