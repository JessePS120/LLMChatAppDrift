def is_multiply_prime(a):
    """Return True if a is the product of exactly three prime numbers, counting multiplicity."""
    count = 0
    divisor = 2

    while a > 1 and divisor <= a:
        while a % divisor == 0:
            a //= divisor
            count += 1
            if count > 3:
                return False
        divisor += 1

    return count == 3 and a == 1