def prime(n):
    if n < 1:
        raise ValueError("there is no zeroth prime")

    count = 0
    number = 2

    while count < n:
        is_prime = True

        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            count += 1

        if count == n:
            return number

        number += 1