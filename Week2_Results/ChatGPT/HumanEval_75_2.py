def is_multiply_prime(a):
    count = 0
    divisor = 2
    while a > 1 and divisor <= a:
        if a % divisor == 0:
            count += 1
            a //= divisor
        else:
            divisor += 1
    return count == 3 and a == 1