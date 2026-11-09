def is_multiply_prime(a):
    count = 0
    d = 2
    n = a
    while d * d <= n:
        while n % d == 0:
            n //= d
            count += 1
        d += 1
    if n > 1:
        count += 1
    return count == 3