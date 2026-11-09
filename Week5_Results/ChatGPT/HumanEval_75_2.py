def is_multiply_prime(a):
    count = 0
    divisor = 2

    while divisor <= a and count < 3:
        if a % divisor == 0:
            a //= divisor
            count += 1
        else:
            divisor += 1

    return count == 3 and a == 1