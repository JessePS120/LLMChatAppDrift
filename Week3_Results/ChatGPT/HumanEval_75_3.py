def is_multiply_prime(a):
    count = 0
    divisor = 2
    while a > 1:
        if a % divisor == 0:
            a //= divisor
            count += 1
            if count > 3:
                return False
        else:
            divisor += 1
    return count == 3