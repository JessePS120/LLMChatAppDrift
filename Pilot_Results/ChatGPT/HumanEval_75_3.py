def is_multiply_prime(a):
    """Return True if a is the product of exactly three prime numbers."""
    count = 0
    divisor = 2

    while divisor * divisor <= a:
        while a % divisor == 0:
            a //= divisor
            count += 1
            if count > 3:
                return False
        divisor += 1

    if a > 1:
        count += 1

    return count == 3