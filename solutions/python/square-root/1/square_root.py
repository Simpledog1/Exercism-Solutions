def square_root(number):
    guess = 1

    while guess * guess != number:
        guess += 1
        
    return guess
        
